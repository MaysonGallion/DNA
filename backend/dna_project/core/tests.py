from django.test import TestCase
from core.models import Partner


class PartnerModelTest(TestCase):
    def test_slug_generation(self):
        """Проверка генерации slug при создании партнера."""
        partner = Partner.objects.create(name="Test Partner")
        self.assertEqual(partner.slug, "test-partner")

    def test_link_generation(self):
        """Проверка генерации ссылки при создании партнера."""
        partner = Partner.objects.create(name="Test Partner")
        self.assertEqual(partner.link, "http://127.0.0.1:8000/test-partner/")
