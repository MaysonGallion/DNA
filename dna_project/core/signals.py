from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import DNAConnection
import os

@receiver(post_save, sender=DNAConnection)
def create_partner_template(sender, instance, created, **kwargs):
    if created:
        templates_dir = os.path.join('core', 'templates', 'core', 'partners')
        try:
            # Убедимся, что директория существует
            os.makedirs(templates_dir, exist_ok=True)

            # Имя файла для шаблона
            template_path = os.path.join(templates_dir, f'{instance.slug}.html')

            # Содержимое шаблона
            template_content = f"""
            <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>{instance.title}</title>
            </head>
            <body>
                <h1>Welcome to {instance.title}'s page</h1>
                <p>{instance.description}</p>
            </body>
            </html>
            """

            # Создание файла шаблона
            with open(template_path, 'w', encoding='utf-8') as file:
                file.write(template_content)

        except Exception as e:
            print(f"Error creating template for {instance.slug}: {e}")

