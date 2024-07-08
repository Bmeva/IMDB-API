from rest_framework import permissions


#Only admin else read only for others
class AdminOrReadOnlyCustomPerm(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return bool(request.user and request.user.is_staff)
    
    #this is another way to acchieve the code above
    # def has_permission(self, request, view):
    #     admin_permision = bool(request.user and request.user.is_staff)
        
    #     return request.method=="GET" or admin_permision
    
    

#this permson allows only the the one that created the review to modify it
#review_user is coming from the model
class ReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        else:
            return obj.review_user == request.user 