from django.shortcuts import render
from django.http import HttpResponseRedirect
from restaurant.setting.prod import SET_ENDTIME
from main.models import Addresses, Chef, About
from main.forms import ContactForm, NewsletterForm
from django.contrib import messages
from datetime import datetime


# Create your views here.
def index_view(request):
    return render(request, 'main/index.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            changed_form = form.save(commit=False)
            changed_form.name = 'Unknown'
            changed_form.save()
            messages.add_message(request, messages.SUCCESS,
                                 '{} ,your ticket has been submitted successfully.'.format(request.POST['name']))
        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.add_message(request, messages.ERROR, error)

    form = ContactForm()
    addresses = Addresses.objects.all()
    return render(request, 'main/contact.html', {'form': form, 'addresses': addresses})


def about_view(request):
    chefs = Chef.objects.all()
    about = About.objects.all()
    features = about.filter(type='Feature').order_by('-updated_date')
    summary = about.filter(type='Summary').order_by('-updated_date').first()
    context = {'chefs': chefs, 'features': features, 'summary': summary}
    return render(request, 'main/about.html', context=context)


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your email address has been saved successfully.')
        else:
            if form.errors:
                for field in form:
                    for error in field.errors:
                        messages.add_message(request, messages.ERROR, error)
    return HttpResponseRedirect('/')


def maintenance_view(request):
    datetime_object = datetime.strptime(SET_ENDTIME, '%Y/%m/%d %H:%M:%S')
    duration = datetime_object - datetime.now()
    duration_in_s = duration.total_seconds()
    hours = int(divmod(duration_in_s, 3600)[0])
    if hours < 0:
        hours = 24
    return render(request, 'maintenance/maintenance.html', {'hours': hours})
