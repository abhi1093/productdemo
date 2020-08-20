from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
    path('avi/', views.API_objects.as_view()),
    path('avi/<int:pk>/', views.API_objects_details.as_view()),
    path('',include('djoser.urls')),
    path('',include('djoser.urls.authtoken')),
]
