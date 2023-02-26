from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Dish, Chef, Why_us, Response, Event, Gallery, About, Footer
from .forms import UserReservationForm, UserContactForm


def main_view(request):
    form_reserve = UserReservationForm(request.POST or None)
    form_contact = UserContactForm(request.POST or None)

    if form_reserve.is_valid():
        form_reserve.save()
        return redirect('/')

    if form_contact.is_valid():
        form_contact.save()
        return redirect('/')

    dishes = Dish.objects.filter(is_visible=True)
    categories = Category.objects.filter(is_visible=True)
    chefs = Chef.objects.filter(is_visible=True)
    why_us = Why_us.objects.filter(is_visible=True)
    response = Response.objects.filter(is_visible=True)
    events = Event.objects.filter(is_visible=True)
    gallery = Gallery.objects.filter(is_visible=True)
    about = About.objects.filter(is_visible=True)
    footer = Footer.objects.all()

    return render(request, 'base.html', context={
        'categories': categories,
        'dishes': dishes,
        'chefs': chefs,
        'why_us': why_us,
        'response': response,
        'events': events,
        'gallery': gallery,
        'form_reserve': form_reserve,
        'about': about,
        'form_contact': form_contact,
        'footer': footer
    })
