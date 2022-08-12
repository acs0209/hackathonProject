from django.urls import path
from . import views

urlpatterns = [
    path('photolist/', views.photo_list, name='photo_list'),
    path('', views.home, name='home'),
]