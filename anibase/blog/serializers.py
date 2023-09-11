from rest_framework import serializers

from blog.models import Artwork


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artwork
        fields = ('title',)
