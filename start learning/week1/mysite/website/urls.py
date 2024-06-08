
from django.urls import path
from website.views import index_view , Contact_view , about_view
urlpatterns = [
    #path ('urls address' , 'view')
    path('home',index_view),
    path('about',about_view),
    path('contact',Contact_view),


]

