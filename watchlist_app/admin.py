from django.contrib import admin
from .models import watchlist, streamplatform, Review

class watchlistadmin(admin.ModelAdmin):
       
    list_display = ('id', 'title', 'description', 'created', 'active')
    ordering = ['id'] 
    list_display_links = ('id',)
    list_editable = ('title', 'description')
    
admin.site.register(watchlist, watchlistadmin)


    
    
class streamplatformadmin(admin.ModelAdmin):
       
    list_display = ('id', 'name', 'about', 'website')
    ordering = ['id'] 
    list_display_links = ('name',)
   
admin.site.register(streamplatform, streamplatformadmin)




admin.site.register(Review)