from django.urls import path
from .views import DNAConnectionListView, index, partner_page

urlpatterns = [
path('', index, name='home'),
    path('api/dna-connections/', DNAConnectionListView.as_view(), name='dna-connections'),
    path('<slug:slug>/', partner_page, name='partner-page'),
]