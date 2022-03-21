from django.http import HttpResponse
from django.shortcuts import render
from listings.models import Band, Title


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
    <h1>Hello Django !</h1>
    <p>Mes groupes préférés sont :</p>
    <ul>
        <li>{bands[0].name}</li>
        <li>{bands[1].name}</li>
        <li>{bands[2].name}</li>
    </ul>
    """)

def about(request):
    return HttpResponse("<h1>About us</h1><p>We love merch !</p>")

def listings(request):
    title = Title.objects.all()
    return HttpResponse(f"""
    <h1>Listings</h1>
    <p>Annonces</p>
    <ul>
        <li>{title[0].name}</li>
        <li>{title[1].name}</li>
        <li>{title[2].name}</li>
        <li>{title[3].name}</li>
    </ul>""")

def contact(request):
    return HttpResponse("<h1>Contact</h1><p>Contact us !</p>")
