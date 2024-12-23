from django.shortcuts import render

# Create your views here.
def sheryians(request):
    return render(request,'sheryians.html')
def home(request):
    return render(request,'home.html')
def courses(request):
    return render(request,'courses.html')
def bootcamp(request):
    return render(request,'bootcamp.html')
def frontend(request):
    return render(request,'frontend.html')
def backend(request):
    return render(request,'backend.html')
def aptitude(request):
    return render(request,'aptitude.html')
def java(request):
    return render(request,'java.html')
