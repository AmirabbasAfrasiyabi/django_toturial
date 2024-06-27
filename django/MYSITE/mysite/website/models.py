from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=225)
    email = models.EmailField(max_length=225)
    subject = models.CharField(max_length=255)
    massage = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'کانتکت'
        verbose_name_plural = ' کانتکت ها'
    def __str__(self):
        return" {}" .format(self.name )