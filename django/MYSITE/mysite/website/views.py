from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from website.models import Contact
from website.forms import NameForm, ContactForm, NewsletterForm
from django.contrib import messages

def index_view(request):
    return render(request, 'website/index.html')

def about_view(request):
    return render(request, 'website/about.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your ticket submitted successfully!')
            return HttpResponseRedirect('/contact')  # Redirect to the same page or any other page
        else:
            messages.error(request, 'Please correct the errors below.')

    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})

def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Newsletter subscription successful!')
            return HttpResponseRedirect('/')
        else:
            messages.error(request, 'There was an error with your submission.')
            return HttpResponseRedirect('/')
    form = NewsletterForm()
    return render(request, 'website/newsletter.html', {'form': form})

def test_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('done')
        else:
            return HttpResponse('not valid')
    form = ContactForm()
    return render(request, 'website/test.html', {'form': form})
