from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import NotFound
from .models import Partner
from .serializers import PartnerSerializer
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework import status


class PartnerPagination(PageNumberPagination):
    page_size = 10


class PartnerListView(APIView):
    def get(self, request):
        partners = Partner.objects.filter(active=True)  # Только активные партнеры
        serializer = PartnerSerializer(partners, many=True, context={'request': request})
        return Response(serializer.data)


    def post(self, request):
        # Парсер для обработки файлов
        parser_classes = (MultiPartParser, FormParser)
        serializer = PartnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PartnerDetailView(APIView):
    def get(self, request, slug):
        partner = get_object_or_404(Partner, slug=slug)
        serializer = PartnerSerializer(partner, context={'request': request})
        return Response(serializer.data)


    def handle_exception(self, exc):
        if isinstance(exc, Partner.DoesNotExist):
            raise NotFound(detail="Партнер не найден.")
        return super().handle_exception(exc)
