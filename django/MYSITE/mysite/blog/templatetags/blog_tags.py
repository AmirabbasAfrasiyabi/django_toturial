from django import template
from blog.models import Post
from blog.models import category

register = template.Library()


@register.simple_tag(name ='totalPost')

def function():
    posts = Post.objects.filter(status=1).count()
    return posts


@register.filter
def snippet(value,arg=20):
    return value[:arg]+ '....'

@ register.inclusion_tag('blog/blog-popularpost.html')
def latestposts(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return{'posts': posts}

@ register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = category.objects.all()
    cat_dict = {}
    for name in categories:
       cat_dict[name]=posts.filter(category=name).count()
    
    return{'categories':cat_dict}