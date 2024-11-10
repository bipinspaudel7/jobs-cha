from django.conf import settings
from django.conf.urls.static import static
from django.urls import (
    include,
    path,
)

from django.views.generic import TemplateView
from baton.autodiscover import admin

admin.site.site_title = 'IMS'
admin.site.site_header = 'IMS'
admin.site.index_title = 'IMS'

url_patterns = [
    path('baton/', include('baton.urls')),
    path('', admin.site.urls),

]

urlpatterns = static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(
    settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + url_patterns
