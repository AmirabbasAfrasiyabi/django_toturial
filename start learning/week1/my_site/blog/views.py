from django.shortcuts import render , get_object_or_404
from blog.models import Post
# Create your views here.
def blog_view (request):
    Posts = Post.objects.filter(status=1)
    context = {'Posts':Posts}
    return render (request , 'blog/blog-home.html',context)

def blog_single (request):
    return render (request , 'blog/blog-single.html')

def test (request,pid):
    #Posts = Post.objects.get(id = pid)
    Posts = get_object_or_404(Post, pk=pid)
    context = {'Posts':Posts}    
    # context = {'pid':pid}
    return render (request , 'test.html',context)