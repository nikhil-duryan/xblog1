from django.urls import path
from Blog import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'Blog'

urlpatterns=[
    path('postComment', views.postComment, name="postComment"),
    path('upload', views.upload, name="upload"),
    path('', views.Blogs, name="Blogs"),
    path('<str:slug>', views.blogPost, name="blogPost"),    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)