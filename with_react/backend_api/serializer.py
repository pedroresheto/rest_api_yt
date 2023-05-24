from rest_framework import serializers
from .models import YoutubeVideo

#приобразует информацию из питон объекта в джсон
class YoutubeVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = YoutubeVideo
        fields = ['title', 'chanel']
