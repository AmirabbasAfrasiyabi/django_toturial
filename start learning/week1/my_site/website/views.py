from django.shortcuts import render
from django.http import HttpResponse 

def Index_view(request):
    return render(request,'index.html')

def About_view(request):
    return render(request,'about.html')

def Contact_view(request):
    return render(request,'contact.html')