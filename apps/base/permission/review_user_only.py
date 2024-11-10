# from rest_framework import permissions

# from shareholder.models import Shareholder


# def shareholder(request, *args, **kwargs):
#     return Shareholder.objects.get(user=request.user)


# class IsShareholderReviewUser(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request:
#             return obj.shareholder == shareholder(request)


# class IsReviewUser(permissions.BasePermission):
#     def has_object_permission(self, request, view, obj):
#         if request:
#             return obj.user == request.user
