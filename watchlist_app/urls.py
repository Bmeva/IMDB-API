
from django.urls import path, include
from .views import movie_list, single_platform_detail
from .import views



urlpatterns = [
   
    
    path('movie_list/', views.movie_list, name= 'movie_list'),
    
         
    path('movie_detail/<int:pk>/', views.single_platform_detail, name='single_movie_detail'),

    
]
