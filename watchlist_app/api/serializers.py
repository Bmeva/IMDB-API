from rest_framework import serializers
from watchlist_app.models import watchlist, streamplatform, Review


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only = True)
    class Meta:
        model = Review
        exclude = ('Watchlist',)
        #fields = "__all__"


class watchlistSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many = True, read_only=True)
    len_name = serializers.SerializerMethodField()
  
    class Meta:
        model = watchlist
        fields = "__all__" #you can also define indifidual fields
        #fields = ['id', 'name', 'description']
        #exclude =['active'] #if i remove the all fields and the fields section then this would display all fields except the once i excluded
  
    
    def get_len_name(self, object): #this methord adds a field or cutom field to our serializer without adding it to the model
        lenght = len(object.title)
        return lenght
        #return len(object.name) i can also take out the above two lines and return it directly



class StreamPlatformSerializer(serializers.ModelSerializer):
    watchlist = watchlistSerializer(many=True, read_only=True) #this is a nested relationship. watchlist has to be the same as the related name in the model
    #watchlist = serializers.StringRelatedField(many=True) #this would return only the title. it returns title becouse in the model the string representation is title
    #watchlist = serializers.PrimaryKeyRelatedField(many= True, read_only = True) # this returns only primary key

    class Meta:
        model = streamplatform
        fields = "__all__"
    
      
    # def validate(self, data): # this is an object validator 
    #      if data['name'] == data['description']: #this is an object level validation
    #         raise serializers.ValidationError('title and description should not be the same')
    #      else:
    #          return data
         
    # def validate_name(self, value): # this is a field level validator. validate_name (name is the field you are validating)
    #      if len(value) < 2:
    #        raise serializers.ValidationError('Name is too short')
    #      else:
    #          return value
        
        

# def name_lenght(value):
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too short')

# #creating serialiser for the Movie model
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only = True)
#     name = serializers.CharField(validators=[name_lenght]) # this is the third type of validators which is called validators
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
        
#         instance.save()
#         return instance
    
#     def validate(self, data): # this is an object validator 
#         if data['name'] == data['description']: #this is an object level validation
#             raise serializers.ValidationError('title and description should not be the same')
#         else:
#             return data
    
#     def validate_name(self, value): # this is a field level validator. validate_name (name is the field you are validating)
#         if len(value) < 2:
#             raise serializers.ValidationError('Name is too short')
#         else:
#             return value
        