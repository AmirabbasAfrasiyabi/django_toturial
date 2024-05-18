from django.shortcuts import render

from django.http import HttpResponse 
def index_view(request):
    return render(request,'website/index.html')

def Contact_view(request):
    return render(request,'about.html')