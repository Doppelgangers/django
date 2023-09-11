from django.http import HttpResponse
from rest_framework import generics
from django.shortcuts import render

from .models import Artwork
from .serializers import BlogSerializer


# Create your views here.


def index(request):
    return HttpResponse('')


class BlogAPIView(generics.ListAPIView):
    queryset = Artwork.objects.all()
    serializer_class = BlogSerializer

