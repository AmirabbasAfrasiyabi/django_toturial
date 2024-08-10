from django.contrib import admin
from blog.models import Post , category ,Comment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'email', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ['name','post',]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)
class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = '-empty-'
    list_display = ("title","author","published_date", "status", "created_date" , "updated_date" )
    list_filter = ("status",'author')
    search_fields = ['title','content','author']
    summernote_fields = ('content',)

admin.site.register(category)
admin.site.register(Post,PostAdmin)
admin.site.register(Comment, CommentAdmin)















    
