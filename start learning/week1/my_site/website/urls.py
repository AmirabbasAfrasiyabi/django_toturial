
from django.urls import path
from website.views import Index_view , Contact_view , About_view
urlpatterns = [
    #path ('urls address' , 'view')
    path('',Index_view),
    path('about',About_view),
    path('contact',Contact_view),

 

]
