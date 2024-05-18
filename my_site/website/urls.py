
from django.urls import path
from website.views import index_view , Contact_view
urlpatterns = [
    #path ('urls address' , 'view')
    path('home',index_view),
    path('about',Contact_view),
 

]
