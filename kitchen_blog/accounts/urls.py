from django.urls import path
from django.conf.urls.static import static
from .views import UserRegisterView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from kitchen_blog import settings


urlpatterns = [
    path('register/',UserRegisterView.as_view(), name='register'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
