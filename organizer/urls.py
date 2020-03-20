from django.urls import path
from . import views

urlpatterns = [
		path('', views.tagList, name='tag-list'),
		path('<slug>/details/', views.tagDetails, name='tag-details'),
		path('startups/', views.startupList, name='startup-list'),
		path('startups/<slug>/details/', views.startupDetail, name='startup-detail'),
]