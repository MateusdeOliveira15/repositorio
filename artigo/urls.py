from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, search

urlpatterns = [
    path('', home),
    path('search', search, name='search')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
