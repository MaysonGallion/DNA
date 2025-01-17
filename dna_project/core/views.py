from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import DNAConnection
from .serializers import DNAConnectionSerializer


# Create your views here.

class DNAConnectionListView(APIView):
    def get(self, request):
        connections = DNAConnection.objects.filter(active=True)
        serializer = DNAConnectionSerializer(connections, many=True)
        return Response(serializer.data)

def index(request):
    return render(request, 'core/index.html')