from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied

class IsEmailVerified(BasePermission):
    """
    Custom permission to only allow access if the user's email is verified.
    """

    def has_permission(self, request, view):
        # Ensure the user is authenticated first
        if not request.user.is_authenticated:
            return False
        
        # Check if the email is verified
        if not request.user.profile.email_verified:
            raise PermissionDenied("Your email is not verified yet. Please verify it first by requesting the OTP")
        
        return True
