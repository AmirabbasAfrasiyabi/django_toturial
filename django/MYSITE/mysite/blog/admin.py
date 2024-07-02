from django.contrib import admin
from blog.models import Post , category

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = '-empty-'
    # fields = ("title","content","published_date", "status", "created_date" , "updated_date" )
    list_display = ("title","published_date", "status", "created_date" , "updated_date" )
    list_filter = ("status",'author')
    # ordering = ['-created_date']
    search_fields = ['title','content','author']
admin.site.register(category)
admin.site.register(Post,PostAdmin)















    
