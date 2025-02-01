from django.urls import path
from .views import PartnerListView, PartnerDetailView

urlpatterns = [
    path('partners/', PartnerListView.as_view(), name='partners-list'),
    path('partners/<slug:slug>/', PartnerDetailView.as_view(), name='partner-detail'),  # Получить партнера по slug
]
