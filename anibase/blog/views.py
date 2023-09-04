from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("404")


def vive_post_to_slug(request, post_slug):
    return HttpResponse(f"post = {post_slug}")
