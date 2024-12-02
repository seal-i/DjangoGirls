from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  # Maps the home page to post_list
]
