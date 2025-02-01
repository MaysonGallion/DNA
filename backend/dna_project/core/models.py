from django.db import models
from django.utils.text import slugify


class Partner(models.Model):
    name = models.CharField(max_length=100)  # Название партнера
    description = models.TextField(blank=True, null=True)  # Описание
    slug = models.SlugField(unique=True, blank=True)  # Слаг для ссылки
    link = models.URLField(blank=True, null=True)  # Полный URL для страницы партнера
    active = models.BooleanField(default=True)  # Активность записи

    def save(self, *args, **kwargs):
        # Генерация slug на основе имени
        if not self.slug:
            self.slug = slugify(self.name)
        # Генерация полного линка
        # Структура: "главная страница - страница партнера"
        self.link = f"http://127.0.0.1:8000/{self.slug}/"
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
