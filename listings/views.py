from turtle import title
from django.http import HttpResponse
from django.shortcuts import render
from listings import models
from listings.models import Band, Title
from django.http import Http404


def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", context={"bands" : bands})

def band_detail(request, id): 
    band = Band.objects.get(id=id)
    return render(request, "listings/band_detail.html", {"band": band})

def about(request):
    return render(request, "listings/about.html")

def listings(request):
    title = Title.objects.all()
    return render(request, "listings/listings.html", context={"title" : title})

def listings_detail(request, id):
    title = Title.objects.get(id=id)
    return render(request, "listings/listings_detail.html", {'title': title})

def contact(request):
    return render(request, "listings/contact.html")
