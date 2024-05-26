from django.shortcuts import render
from .models import streamplatform
from django.http import JsonResponse

#listing all movie details whcich is like manual way of creating api
def movie_list(request): 
    platform = streamplatform.objects.all()
    
    theplatformvalue = list(platform.values())
   
    
    data = {
        'themovievalue': theplatformvalue,
    }
    
    return JsonResponse(data)

#listing individual movie details whcich is like manual way of creating api
def single_platform_detail(request, pk):
    single_platform = streamplatform.objects.get(pk = pk)
    name =  single_platform.name,
    about = single_platform.about,
    website = single_platform.about,
    
      
    
    data = {
        'name': name,
        'about': about,
        'website': website,
               
    }
        
    return JsonResponse(data)
    
 
    
    
    
    
    
    
    
