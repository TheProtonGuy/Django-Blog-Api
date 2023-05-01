from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('get-all-posts/', views.GetAllPosts),
    path('create-new-post/', views.CreatePost),
    path('delete-post/', views.DeletePost),
    path('get-post/', views.GetPost),
    path('update-post/', views.UpdatePost),
]