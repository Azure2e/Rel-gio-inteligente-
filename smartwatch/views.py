from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.conf import settings
from datetime import datetime, date
import random
import requests
from .models import HealthRecord


@login_required(login_url='/login/')
def index(request):
    today = date.today()
    record, _ = HealthRecord.objects.get_or_create(
        user=request.user,
        date=today,
        defaults={'steps': 4500, 'heart_rate': 78, 'calories': 320, 'distance_km': 4.2}
    )

    # ==================== CLIMA REAL ====================
    try:
        url = "https://api.openweathermap.org/data/2.5/weather"
        params = {
            'q': settings.WEATHER_CITY,
            'appid': settings.WEATHER_API_KEY,
            'units': 'metric',
            'lang': 'pt_br'
        }
        response = requests.get(url, params=params, timeout=8)
        response.raise_for_status()
        data = response.json()
        temperatura = round(data['main']['temp'])
        cidade = data['name']
        descricao = data['weather'][0]['description'].capitalize()
        icon = data['weather'][0]['icon']
    except:
        temperatura = random.randint(18, 32)
        cidade = settings.WEATHER_CITY
        descricao = 'Parcialmente nublado'
        icon = '02d'

    context = {
        'hora': datetime.now().strftime("%H:%M"),
        'data': datetime.now().strftime("%d %b %Y"),
        'dia_semana': datetime.now().strftime("%A"),
        'temperatura': temperatura,
        'cidade': cidade,
        'descricao': descricao,
        'icon': icon,

        # Dados de saúde do banco
        'passos': record.steps,
        'meta_passos': 10000,
        'batimentos': record.heart_rate,
        'calorias': record.calories,
        'distancia': record.distance_km,

        'username': request.user.username,
        'notificacoes': [
            {"titulo": "WhatsApp", "mensagem": "Maria: Cheguei!"},
            {"titulo": "Lembrete", "mensagem": "Reunião em 30 min"},
        ]
    }
    return render(request, 'smartwatch/index.html', context)


# ==================== SINCRONIZAR API DE SAÚDE ====================
@login_required
def sync_health(request):
    today = date.today()
    record = HealthRecord.objects.get_or_create(user=request.user, date=today)[0]

    # ←←← AQUI VOCÊ COLOCA A INTEGRAÇÃO REAL COM A API DE SAÚDE ←←←
    # Exemplo com Fitbit/Google Fit (OAuth) ou qualquer outra API
    # Por enquanto estamos simulando dados "reais"

    record.steps = random.randint(6500, 13500)
    record.heart_rate = random.randint(72, 105)
    record.calories = random.randint(450, 950)
    record.distance_km = round(random.uniform(5.5, 14.0), 1)
    record.save()

    return redirect('index')


# ==================== LOGIN / CADASTRO / LOGOUT ====================
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'smartwatch/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'smartwatch/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')