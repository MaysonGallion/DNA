from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Partner
from .serializers import PartnerSerializer


class PartnerListView(APIView):
    def get(self, request):
        partners = Partner.objects.filter(active=True)  # Только активные партнеры
        serializer = PartnerSerializer(partners, many=True)
        return Response(serializer.data)


class PartnerDetailView(APIView):
    def get(self, request, slug):
        partner = get_object_or_404(Partner, slug=slug)
        serializer = PartnerSerializer(partner)
        return Response(serializer.data)
