from django.shortcuts import render, redirect

# Create your views here.
def shootingStars(request):
    return render(request, "shootingStars.html")

def home(request):
    return render(request, "home.html")

def backhome(request):
    return redirect("/")