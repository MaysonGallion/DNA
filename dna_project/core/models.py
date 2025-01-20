from django.db import models
from django.utils.text import slugify


class DNAConnection(models.Model):
    title = models.CharField(max_length=100)  # Название точки
    description = models.TextField(blank=True, null=True)  # Описание
    url = models.CharField(max_length=200, blank=True, null=True)  # Ссылка на страницу
    slug = models.SlugField(unique=True, blank=True)  # Уникальный путь для страницы
    active = models.BooleanField(default=True)  # Активна ли точка

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.title)
            slug = base_slug
            num = 1

            # Проверяем уникальность slug
            while DNAConnection.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{num}"
                num += 1

            self.slug = slug

        super().save(*args, **kwargs)

    def __str__(self):
        return self.title
