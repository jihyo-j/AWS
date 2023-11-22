from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework import routers

from posts.views import *
from posts.views import url_view, url_parameter_view, function_view, index
from posts.views import class_view

router=routers.DefaultRouter()
router.register('posts',PostModelViewSet)

urlpatterns = [

#    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('', include('posts.urls')),
    
    #path('post/<int:id>/', post_detail_view, name='post-detail'),
    #path('post/<int:id>/update/', post_update_view, name='post-update'),
    #path('post/<int:id>/delete/', post_delete_view, name='post-delete'),
    
    
    #path('posts/', include('posts.urls', namespace='posts')),
  
    # Function Based View
    path('url/', url_view),
    path('url/<str:username>/', url_parameter_view),
    path('fbv/', function_view),
    # Class Based View
    path('cbv/', class_view.as_view()), # as_view: 진입 메소드

    #path('', index, name='index'),
    
    path('accounts/', include('accounts.urls', namespace='accounts')),
    #path('posts/', include('posts.urls', namespace='posts')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)