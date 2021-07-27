from django.urls import path
from . import views

urlpatterns = [
    path('', views.shootingStars),
    path('shootingstars-aboutme', views.aboutme),
    path('go-home', views.backhome),
]