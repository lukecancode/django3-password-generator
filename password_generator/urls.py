"""password_generator URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from generator import views #first you import the file views from generator
from django.urls import path


urlpatterns = [
    path('', views.home, name='home'),#and here in the urlpatterns (what shows in you page) you specify the name
    #of the page, in this case the 1st page named "home"
    path('password/', views.password),#and views again, because it's gonna show, and the second page name
    #"password".
    #after that you have to modify in "views.py", by defining a function with the same specification (home and password).
    path('about/', views.about, name='about'),

    ]
