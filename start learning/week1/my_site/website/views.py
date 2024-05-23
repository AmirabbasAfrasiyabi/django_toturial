from django.shortcuts import render
from django.http import HttpResponse 

def Index_view(request):
    return render(request,'website/index.html')

def About_view(request):
    return render(request,'website/about.html')

def Contact_view(request):
    return render(request,'website/contact.html')