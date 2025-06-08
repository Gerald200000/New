from .views import post_list, post_detail
from django.urls import path

urlpatterns = [path("",post_list,name = 'home'),
                path("post/<int:pk>/", post_detail, name = "post_detail")
               ]