from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseServerError
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DNAConnection
from .serializers import DNAConnectionSerializer


class DNAConnectionListView(APIView):
    def get(self, request):
        connections = DNAConnection.objects.filter(active=True)
        serializer = DNAConnectionSerializer(connections, many=True)
        return Response(serializer.data)


def index(request):
    return render(request, 'core/index.html')


def partner_page(request, slug):
    connection = get_object_or_404(DNAConnection, slug=slug)
    template_name = f'core/partners/{connection.slug}.html'
    try:
        return render(request, template_name, {'connection': connection})
    except Exception as e:
        return HttpResponseServerError(f"Template not found or failed to render: {e}")
