from rest_framework import serializers
from .models import DNAConnection


class DNAConnectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DNAConnection
        fields = ['id', 'title', 'description', 'url', 'active']
