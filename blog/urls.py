from .views import BlogDetailView, BlogListView, BlogCreateView
from django.urls import path

urlpatterns = [path("",BlogListView.as_view(),name = 'home'),
                path("post/<int:pk>/", BlogDetailView.as_view(), name = "post_detail"),
                path("post/new/", BlogCreateView.as_view(),name = 'post_new')
               ]