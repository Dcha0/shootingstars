from django.urls import path
from . import views

urlpatterns = [
    path('', views.shootingStars),
    path('shooting-stars', views.home)
]