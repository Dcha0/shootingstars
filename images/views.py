from django.shortcuts import render, redirect

# Create your views here.
def shootingStars(request):
    return render(request, "shootingStars.html")

def aboutme(request):
    return render(request, "aboutme.html")

def backhome(request):
    return redirect("/")