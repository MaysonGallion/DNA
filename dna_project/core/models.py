from django.db import models


# Create your models here.
class DNAConnection(models.Model):
    title = models.CharField(max_length=100)  # Название точки
    description = models.TextField(blank=True, null=True)  # Описание
    url = models.CharField(max_length=200)  # Используем CharField для относительных URL
    active = models.BooleanField(default=True)  # Активна ли точка

    def __str__(self):
        return self.title
