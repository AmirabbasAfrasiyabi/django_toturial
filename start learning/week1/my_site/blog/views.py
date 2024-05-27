from django.shortcuts import render

# Create your views here.
def blog_view (request):
    return render (request , 'blog/blog-home.html')

def blog_single (request):
    context = {'title' : 'bitcoin crashed again!' , 'context':'bitcoin was flying but now as always'}
    return render (request , 'blog/blog-single.html',context)