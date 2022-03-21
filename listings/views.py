from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Title


def hello(request):
    bands = Band.objects.all()
    return render(request, "listings/hello.html", context={"bands" : bands})

def about(request):
    return render(request, "listings/about.html")

def listings(request):
    title = Title.objects.all()
    return render(request, "listings/listings.html", context={"title" : title})

def contact(request):
    return render(request, "listings/contact.html")
