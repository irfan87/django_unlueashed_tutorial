from django.urls import path
from . import views

urlpatterns = [
		path('posts/', views.postList, name='post-list'),
		path('posts/<slug>/details/', views.postDetail, name='post-detail'),
]