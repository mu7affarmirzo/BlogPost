from django.urls import path

from blog.api.views import (
    api_detail_blog_view,
    api_update_blog_view,
    api_create_blog_view,
    api_delete_blog_view,
    ApiBlogListView,
)

app_name = 'blog'

urlpatterns = [
    path('<slug>/', api_detail_blog_view, name="detail"),
    path('<slug>/update', api_update_blog_view, name="update"),
    path('<slug>/delete', api_delete_blog_view, name="delet"),
    path('create', api_create_blog_view, name="create"),
    path('list', ApiBlogListView.as_view(), name="list"),
]