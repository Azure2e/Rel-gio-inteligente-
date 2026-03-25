from django.db import models
from django.contrib.auth.models import User
from datetime import date

class HealthRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=date.today)
    steps = models.PositiveIntegerField(default=0)
    heart_rate = models.PositiveIntegerField(default=70)
    calories = models.PositiveIntegerField(default=0)
    distance_km = models.FloatField(default=0.0)

    class Meta:
        unique_together = ['user', 'date']  # Apenas um registro por dia por usuário
        ordering = ['-date']

    def __str__(self):
        return f"{self.user.username} - {self.date} - {self.steps} passos"