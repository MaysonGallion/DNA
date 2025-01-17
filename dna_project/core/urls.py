from django.urls import path
from .views import DNAConnectionListView, index

urlpatterns = [
    path('api/dna-connections/', DNAConnectionListView.as_view(), name='dna-connections'),
    path('', index, name='home')
]