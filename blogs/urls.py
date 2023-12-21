from django.urls import path
from blogs.views import list_view

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('posts/<int:post_id>', list_view, name="blog_detail")
]
