from django.urls import path

from .views import BlogListView, BlogDetailsView, CreateBlogView, EditBlogView, DeleteBlogView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailsView.as_view(), name='post_details'),
    path('post/new', CreateBlogView.as_view(), name='new_post'),
    path('post/<int:pk>/edit/', EditBlogView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', DeleteBlogView.as_view(), name='delete_post')
]
