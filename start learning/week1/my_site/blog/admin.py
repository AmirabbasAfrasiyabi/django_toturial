from django.contrib import admin
from blog.models import Post

# Register your models here.

##second way
# @admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    
    date_hierarchy = "created_date"
    empty_value_display = "-empty-"
    # fields = ["title",]
    list_display = ["title" ,"author", "count_views" , "status" ,]
    list_filter = ('status','author')

    # created ordering in medels.py and in class meta
    # ordering = ['-created_date']
    
    search_fields = ['title','content']
##first way
admin.site.register(Post,PostAdmin)

