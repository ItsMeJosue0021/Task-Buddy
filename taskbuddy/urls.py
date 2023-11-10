from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name="about"),
    path('login/', views.login, name="login"),
    path('signup/', views.signup, name="signup"),

    # Dashboard
    path('projects/', views.projects, name="projects"),
    path('colleagues/', views.colleagues, name="colleagues"),
    path('tasks/', views.tasks, name="tasks"),
    
]