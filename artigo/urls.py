from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import home, search

urlpatterns = [
    path('', home, name="home"),
    path('search', search, name='search')
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
