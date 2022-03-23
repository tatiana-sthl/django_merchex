"""merchex URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django import views
from django.contrib import admin
from django.urls import path
from listings import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('bands/<int:id>/', views.band_detail, name="band-detail"),
    path('bands/', views.band_list, name='band-list'),
    path('bands/add/', views.band_create, name='band-create'),
    path('about/', views.about, name="about"),
    path('listings/', views.listings, name='title-list'),
    path('listings/<int:id>/', views.listings_detail, name="listings-detail"),
    path('contact/', views.contact, name="contact"),
    path('email_sent/',views.email_sent, name="email-sent"),
]
