from django.urls import path
from .views import IndexPageView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', IndexPageView.as_view(), name='home'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)