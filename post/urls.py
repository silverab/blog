from django.urls import path, include

from .views import AddCommentView
from post import views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
	path('accounts/', include('django.contrib.auth.urls')),
    path('', views.home, name='home'),
    path('about_us/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('blog/', views.postblog, name='blog'),
    path('blog/<slug:slug>/', views.single_post, name='single_post'),
    path('blog/<slug:slug>/comment/', AddCommentView.as_view(), name='add_comment'),
    path('signup/', views.SignUp, name='signup'),

]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)