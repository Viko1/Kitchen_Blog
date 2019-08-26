from django.urls import path
from .views import IndexView, PostDetailView, CreatePostView, PostEditView, PostDeleteView
from django.conf.urls.static import static

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from kitchen_blog import settings



urlpatterns = [
    path('',IndexView.as_view(), name='home'),
    path('article/<int:pk>/',PostDetailView.as_view(),name="post-detail"),
    path('article/new/',CreatePostView.as_view(),name="post-new"),
    path('article/edit/<int:pk>/',PostEditView.as_view(),name="post-edit"),
    path('article/<int:pk>/remove',PostDeleteView.as_view(),name="post-delete"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
