from django.shortcuts import render,get_object_or_404
from blog.models import Post 

# Create your views here
def blog_view (request):
    posts = Post.objects.filter(status=1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request):
    context = {'title':'Bitcoin crashed againd','content':'Bitcoin was finally recovered','author':'amirabbas'}
    return render(request, 'blog/blog-single.html',context)

def blog_test(request,pid):

    # post = Post.objects.get(id=pid)
    post = get_object_or_404(Post,pk=pid)
    context = {'post': post}
    return render (request,'test.html',context)