from django.urls import path 
from . import views

urlpatterns=[
   path('',views.home, name='home'),
   path('logout/', views.logoutUser, name='logout'),
   path('new/post', views.new_post, name='new-post'),
   path('profile/', views.profile, name='profile'),
   path('like/', views.like, name='like'),
]