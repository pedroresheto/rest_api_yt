from django.shortcuts import render
from rest_framework.views import APIView
from .models import YoutubeVideo
from .serializer import YoutubeVideoSerializer
from rest_framework.response import Response
# Create your views here.

class YoutubeVideoView(APIView):
    def get(self, req):
        output =  [
            {
                'title': output.title, 
                'chanel': output.chanel
            } for output in YoutubeVideo.objects.all()
        ]
        return Response(output)
    #  метод получения информации

    def post(self, req):
        serialiyer = YoutubeVideoSerializer(data=req.data)
        if serialiyer.is_valid(raise_exception=True):
            serialiyer.save()
            return Response(serialiyer.data)