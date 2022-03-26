from email import message
from turtle import title
from django.http import HttpResponse
from django.shortcuts import redirect, render
from listings import models
from listings.models import Band, Title
from django.http import Http404
from listings.forms import ContactUsForm, BandForm, TitleForm
from django.core.mail import send_mail

def band_list(request):
    bands = Band.objects.all()
    return render(request, "listings/band_list.html", context={"bands" : bands})

def band_detail(request, id): 
    band = Band.objects.get(id=id)
    return render(request, "listings/band_detail.html", {"band": band})

def band_create(request): 
    if request.method == "POST":
        form = BandForm(request.POST)
        if form.is_valid():
            band = form.save()
            return redirect("band-detail", band.id)
    else:
        form = BandForm()
    return render(request, "listings/band_create.html", {"form": form})

def band_change(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        form = BandForm(request.POST, instance=band)
        if form.is_valid():
            form.save()
            return redirect('band-detail', band.id)
    else:
        form = BandForm(instance=band)

    return render(request, 'listings/band_change.html', {'form': form})

def band_delete(request, id):
    band = Band.objects.get(id=id)

    if request.method == 'POST':
        band.delete()
        return redirect('band-list')

    return render(request, 'listings/band_delete.html', {'band': band})

def about(request):
    return render(request, "listings/about.html")

def listings(request):
    title = Title.objects.all()
    return render(request, "listings/listings.html", context={"title" : title})

def listings_detail(request, id):
    title = Title.objects.get(id=id)
    return render(request, "listings/listings_detail.html", {'title': title})

def listings_create(request): 
    if request.method == "POST":
        form = TitleForm(request.POST)
        if form.is_valid():
            title = form.save()
            return redirect("listings-detail", title.id)
    else:
        form = TitleForm()
    return render(request, "listings/listings_create.html", {"form": form})

def listings_change(request, id):
    title = Title.objects.get(id=id)

    if request.method == 'POST':
        form = TitleForm(request.POST, instance=title)
        if form.is_valid():
            form.save()
            return redirect('listings-detail', title.id)
    else:
        form = TitleForm(instance=title)

    return render(request, 'listings/listings_change.html', {'form': form})

def listings_delete(request, id):
    title = Title.objects.get(id=id)

    if request.method == 'POST':
        title.delete()
        return redirect('listings-list')

    return render(request, 'listings/listings_delete.html', {'title': title})

def contact(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)

        if form.is_valid():
            send_mail(subject=f'Message from {form.cleaned_data["name"] or "anonyme"} via MerchEx Contact Us form',
            message=form.cleaned_data['message'],
            from_email=form.cleaned_data['email'],
            recipient_list=["admin@merchex.xyz"]),
        return redirect("email-sent")

    else:
        form = ContactUsForm()

    return render(request, "listings/contact.html", {"form": form})

def email_sent(request):
    return render(request, "listings/email_sent.html")
