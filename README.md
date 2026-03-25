# 🕒 Relógio Inteligente - Django

Um smartwatch virtual completo feito com **Django**, com interface moderna, animações fluidas, clima em tempo real e integração com dados de saúde.

![Relógio Inteligente](https://via.placeholder.com/800x400/0f172a/22d3ee?text=Relógio+Inteligente)  
*(Substitua pela URL de uma captura ou GIF do seu projeto)*

## ✨ Funcionalidades

- ⌚ Interface de relógio digital elegante e animada
- 🌤️ Clima em tempo real (OpenWeatherMap)
- ❤️ Monitoramento de saúde (passos, batimentos, calorias, distância)
- 🔄 Botão de sincronização com Smartwatch
- 🔐 Sistema completo de login e cadastro
- 💾 Dados de saúde salvos no banco de dados
- 🎨 Animações modernas (pulsação, glow, heartbeat, etc.)

## 🛠️ Tecnologias Utilizadas

- **Backend**: Python + Django 6.0
- **Frontend**: HTML5, Tailwind CSS + Font Awesome
- **Banco de Dados**: SQLite3
- **API Externa**: OpenWeatherMap
- **Linguagem**: Python 3.13

## 📋 Como Instalar e Rodar

### 1. Clone o repositório
```bash
git clone https://github.com/Azure2e/Rel-gio-inteligente-.git
cd Rel-gio-inteligente-
2. Crie e ative o ambiente virtual
PowerShellpython -m venv .venv
.\.venv\Scripts\Activate.ps1
3. Instale as dependências
PowerShellpip install django requests
4. Configure a chave da API do Clima (OBRIGATÓRIO)

Acesse https://openweathermap.org/api e crie sua chave gratuita.
No PowerShell (com o ambiente virtual ativado), execute:

PowerShell$env:WEATHER_API_KEY = "SUA_CHAVE_AQUI"
⚠️ Não compartilhe sua chave real. Substitua SUA_CHAVE_AQUI pela chave que você gerou.
5. Rode o projeto
PowerShellpython manage.py makemigrations
python manage.py migrate
python manage.py runserver
Acesse no navegador: http://127.0.0.1:8000
🔑 Criar conta de usuário
PowerShellpython manage.py createsuperuser
Ou acesse a rota /register/ no navegador.

Desenvolvido por: Jaques
Data: Março 2026
⭐ Se gostou do projeto, deixe uma estrela!
text---

**Agora é só salvar** esse conteúdo no arquivo `README.md` e subir para o GitHub:

```powershell
git add README.md
git commit -m "Atualiza README.md com instruções claras da chave da API"
git push