from django.shortcuts import render

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')

def login(request):
    return render(request, 'pages/login.html')

def signup(request):
    return render(request, 'pages/signup.html')


def projects(request):
    return render(request, 'pages/dashboard/projects.html')

def colleagues(request):
    return render(request, 'pages/dashboard/colleagues.html')

def tasks(request):
    return render(request, 'pages/dashboard/tasks.html')