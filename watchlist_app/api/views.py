from django.shortcuts import render
from watchlist_app.models import streamplatform, watchlist, Review
from django.http import JsonResponse
from rest_framework.response import Response
#from rest_framework.decorators import api_view #this would be used if i am using function based view

from rest_framework.views import APIView #for class based views use this 
from rest_framework import status
from django.shortcuts import get_object_or_404
from watchlist_app.api.serializers import (watchlistSerializer, StreamPlatformSerializer, 
                                           ReviewSerializer)

from rest_framework import generics
#from rest_framework import mixins 

from rest_framework import viewsets
from rest_framework.exceptions import ValidationError



class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        return Review.objects.all()
    
    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
       #movie = watchlist.objects.get(pk=pk)
        movie = get_object_or_404(watchlist, pk=pk)
        
       
        
        thereview_user = self.request.user
        review_queryset = Review.objects.filter(Watchlist = movie, review_user = thereview_user)
        
        if review_queryset.exists():
            raise ValidationError('You have already reviewd this movie')
        
        serializer.save(Watchlist = movie, review_user = thereview_user)

class Reviewsingle(generics.ListAPIView):
    #queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(Watchlist = pk)
    

class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    

class reviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    
# instead of using mixins we used the above two lines which are shorter
# class reviewDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
    

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
    
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


#using viewset which also work like the 
#API views below but i can also use its url to check individual
#stream plaltform by adding /4 or the pk of the stream platform
class StreamPlatformVS(viewsets.ViewSet):
    def list(self, request):
        queryset = streamplatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        queryset = streamplatform.objects.all()
        thewatchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(thewatchlist)
        return Response(serializer.data)
    
    def create(self, request):
        serializer = StreamPlatformSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    

#Second way to acchieve the up code easier 

class StreamPlatformVS2(viewsets.ModelViewSet):
#to make it read only use class StreamPlatformVS2(viewsets.ReadOnlyModelViewSet):
    queryset = streamplatform.objects.all()
    serializer_class = StreamPlatformSerializer
    
    

class StreamPlatformAV(APIView):
    def get(self, request):
        platform = streamplatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)
        return Response(serializer.data)
    
    
    def post(self, request):
        serializer = StreamPlatformSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
         
#single streamplatform detail view
class StreamPlatformDetailAV(APIView):
    def get(self, request, pk):
        try:
            theplatform = streamplatform.objects.get(pk = pk)
        except streamplatform.DoesNotExist:
            return Response({'Error': 'not found'}, status=status.HTTP_404_NOT_FOUND)           
                   
        serializer = StreamPlatformSerializer(theplatform)
        return Response(serializer.data)
            
            
    def put(self, request, pk):
        thestream = streamplatform.objects.get(pk = pk)
        serializer = watchlistSerializer 
        serializer = StreamPlatformSerializer(thestream, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):  
        thestream = streamplatform.objects.get(pk = pk)          
        thestream.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
      



class Watchlist(APIView):
    def get(self, request):
        thewatchlist = watchlist.objects.all()
        serializer = watchlistSerializer(thewatchlist, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = watchlistSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
        
    
        
   

#single watch detail view
class watchDetailAV(APIView):
    def get(self, request, pk):
        try:
            thewatchlist = watchlist.objects.get(pk = pk)
        except watchlist.DoesNotExist:
            return Response({'Error': 'not found'}, status=status.HTTP_404_NOT_FOUND)           
                   
        serializer = watchlistSerializer(thewatchlist)
        return Response(serializer.data)
            
            
    def put(self, request, pk):
        thewatchlist = watchlist.objects.get(pk = pk)
        serializer = watchlistSerializer 
        serializer = watchlistSerializer(thewatchlist, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request, pk):  
        thewatchlist = watchlist.objects.get(pk = pk)          
        thewatchlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            
      
            
    
#this uses function based views
#from rest_framework.decorators import api_view

# @api_view(['GET', 'POST'])
# def movie_list(request):
#     if request.method=='GET':
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)# when you have many objects you have to use many = True
#         return Response(serializer.data)

#     if request.method == 'POST':
#         serializer = MovieSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)




# @api_view(['GET', 'PUT', 'DELETE'])
# def movie_detail(request, pk):
#     try:
#         movie = Movie.objects.get(pk=pk)
#     except Movie.DoesNotExist:
#         return Response({'Error': 'Movie not found'}, status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'GET':
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)

#     elif request.method == 'PUT':
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         movie.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#     else:
#         return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


    


