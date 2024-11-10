from django.urls import (
    include,
    path,
)
from rest_framework.routers import DefaultRouter

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
)

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('docs/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('docs/', SpectacularRedocView.as_view(url_name='schema'),
         name='redoc'),

    path('user/', include('users.urls')),
    path('product/',include('products.urls')),
    path('carts/',include ('carts.urls')),
    path('orders/',include ('orders.urls')),

]
