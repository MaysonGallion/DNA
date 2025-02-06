from rest_framework import serializers
from .models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Partner
        fields = ['name', 'description', 'slug', 'link', 'active']
