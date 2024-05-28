from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self) :
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=200)
    content = models.TextField()
    #tag
    category = models.ManyToManyField(Category)
    count_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True  )
    updated_date = models.DateTimeField(auto_now= True)

    class Meta:
        ordering = ['-created_date']
        # verbose_name = 'Amirabbas'
        # verbose_name_plural = "Amirabbases"
    
    def __str__(self) :
        return "{} - {}".format(self.title , self.id)
    

