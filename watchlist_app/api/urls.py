
from django.urls import path, include

from .import views  #or the one below
from watchlist_app.api import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('streamviewset', views.StreamPlatformVS2, basename='streamplatform')
#to access this url add /streamviewset and to access individual item add streamviewset/4/


urlpatterns = [
    
    path('', views.Watchlist.as_view(), name= 'movie_list'),
    
    path('watchlist/', views.Watchlist.as_view(), name= 'watchlist'),
    
    path('watch_detail/<int:pk>/', views.watchDetailAV.as_view(), name= 'movie_detail'),
    
   
    path('', include(router.urls)),
    
    path('stream', views.StreamPlatformAV.as_view(), name= 'stream'),
    path('streampltformdetail/<int:pk>/', views.StreamPlatformDetailAV.as_view(), name= 'streampltformdetail'),
    
    
    
    # path('review/', views.ReviewList.as_view(), name= 'review-list'),
    
    # path('review/<int:pk>/', views.reviewDetail.as_view(), name= 'review-detail'),
    
    
    path('stream/<int:pk>/review-create', views.ReviewCreate.as_view(), name= 'review-create'),
    path('stream/<int:pk>/Reviewsingle', views.Reviewsingle.as_view(), name= 'review-list'),
    path('streamreviewall/', views.ReviewList.as_view(), name= 'review-list'),
    path('stream/review/<int:pk>/', views.reviewDetail.as_view(), name= 'review-detail'),
    
    
    
   
   #this is for the function based views
    # path('', views.movie_list, name= 'movie_list'),
    
    # path('movie_list/', views.movie_list, name= 'movie_list'),
    
         
    # path('movie_detail/<int:pk>/', views.movie_detail, name='movie_detail'),

    
]
