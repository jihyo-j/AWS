from django.urls import path

from rest_framework.urlpatterns import format_suffix_patterns
from . import views
from .views import post_list_view, post_create_view, post_create_form_view
from .views import post_delete_view, post_detail_view, post_update_view

app_name = 'posts'

"""
urlpatterns = [
    path('', post_list_view, name = 'post-list'),
    # path('create/', post_create_view, name='post-create'),
    path('create/', post_create_form_view, name = 'post-create'),
    path('<int:id>/', post_detail_view, name='post-detail'),
    path('<int:id>/edit', post_update_view, name='post-update'),
    path('<int:id>/delete', post_delete_view, name='post-delete'),

]
"""
urlpatterns=[
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)