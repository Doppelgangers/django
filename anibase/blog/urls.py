from django.urls import path

from . import views
from .views import BlogAPIView

urlpatterns = [
    path('', views.index),
    path('api/v1/bloglist', BlogAPIView.as_view())
]

