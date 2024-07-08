
from watchlist_app.models import streamplatform, watchlist, Review


from django.shortcuts import get_object_or_404


#from rest_framework import mixins 
    


def calculate(pk, serializer):
    movie = get_object_or_404(watchlist, pk=pk)
        
    new_rating = serializer.validated_data['rating']
    if movie.number_rating == 0:
        movie.avg_rating = new_rating
    else:
        movie.avg_rating = (movie.avg_rating * movie.number_rating + new_rating) / (movie.number_rating + 1)
    
    movie.number_rating = movie.number_rating + 1 
    movie.save()
    
    

from watchlist_app.models import watchlist
from django.shortcuts import get_object_or_404

class RatingCalculator:
    def __init__(self, pk, serializer):
        self.pk = pk
        self.serializer = serializer
        self.movie = get_object_or_404(watchlist, pk=self.pk)

    def calculateAvgRating(self):
        new_rating = self.serializer.validated_data['rating']
        if self.movie.number_rating == 0:
            self.movie.avg_rating = new_rating
        else:
            self.movie.avg_rating = (self.movie.avg_rating * self.movie.number_rating + new_rating) / (self.movie.number_rating + 1)

        self.movie.number_rating = self.movie.number_rating + 1
        self.movie.save()
