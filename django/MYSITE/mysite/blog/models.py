from django.db import models
from django.contrib.auth.models import User

class category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) :
        return self.name
class Post(models.Model):
    image = models.ImageField(upload_to='blog/',default='blog/default.jpg')
    author = models.ForeignKey(User, related_name = "author" , on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    #tags
    category  = models.ManyToManyField(category, blank=True,)
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField( default= False)
    published_date = models.DateTimeField(null= True)
    created_date = models.DateTimeField(auto_now_add=True ) 
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_date']
        verbose_name = 'پست'
        verbose_name_plural = ' پست ها'
    def __str__(self):
        return" {}" .format(self.title ,)
