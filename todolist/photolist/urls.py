from django.urls import path
from . import views

app_name = 'photolist'  # URL Reverse에서 namespace역할을 함

urlpatterns = [
    path('new/', views.post_new, name='post_new'),
    path('photolist/', views.photo_list, name='photo_list'),
    path('', views.home, name='home'),
    path('account/', views.account, name='account'),

]