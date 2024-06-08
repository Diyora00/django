from django.contrib import admin
from django.urls import path

from my_blog.views import index

urlpatterns = [
    path('', index, name='index'),
]
