from django.urls import path
from post import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', views.home, name='home'),
    path('about_us/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.postblog, name='blog'),
    path('blog/<slug:slug>/', views.single_post, name='single_post'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)