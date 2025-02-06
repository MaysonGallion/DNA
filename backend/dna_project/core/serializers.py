from rest_framework import serializers
from .models import Partner


class PartnerSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Partner
        fields = ['name', 'description', 'slug', 'link', 'image', 'video', 'active']

    def get_image(self, obj):
        request = self.context.get('request')
        if obj.image:
            return request.build_absolute_uri(obj.image.url)
        return None
