from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) :
        return self.name
class Post(models.Model):
    image = models.ImageField(upload_to='blog/', default='blog/default.jpg')
    author = models.ForeignKey(User, related_name="author", on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ManyToManyField(category, blank=True)
    # comment_count = models.IntegerField(default=0)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']
        verbose_name = 'پست'
        verbose_name_plural = ' پست ها'

    def __str__(self):
        return" {}" .format(self.title ,)
    
    def get_absolute_url(self):
        return reverse("blog:single", kwargs={"pid": self.id})
    

class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post)