from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('post/<slug:post_slug>', views.vive_post_to_slug)

]