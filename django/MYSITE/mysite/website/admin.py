from django.contrib import admin
from website.models import Contact , NewsLetter

# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    date_hierarchy = "created_date"
    empty_value_display = '-empty-'
    # fields = ("name","email","subject","massage","created_date") 
    list_display = ("name","email","subject","created_date",)
    # ordering = ['-created_date']
    list_filter = ('email',)
    search_fields = ['name','massage']
    

admin.site.register(Contact,ContactAdmin)
admin.site.register(NewsLetter)