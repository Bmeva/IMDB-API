
from django.urls import path, include

from .import views  #or the one below
from watchlist_app.api import views


urlpatterns = [
    
    path('', views.Watchlist.as_view(), name= 'movie_list'),
    
    path('watchlist/', views.Watchlist.as_view(), name= 'watchlist'),
    
    path('watch_detail/<int:pk>/', views.watchDetailAV.as_view(), name= 'movie_detail'),
    
   
    path('stream', views.StreamPlatformAV.as_view(), name= 'stream'),
    path('streampltformdetail/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name= 'streampltformdetail'),
    
    
   
   #this is for the function based views
    # path('', views.movie_list, name= 'movie_list'),
    
    # path('movie_list/', views.movie_list, name= 'movie_list'),
    
         
    # path('movie_detail/<int:pk>/', views.movie_detail, name='movie_detail'),

    
]
