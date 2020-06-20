
from django.urls import path

from .import views


urlpatterns=[
    path('',views.home, name='home'),
    path('profile/',views.profile, name='profile'),
    path('accounts/signup/',views.signup,name='signup'),
    path('accounts/login/', views.login, name='login'),
    path('post/',views.post, name='post'),
    path('profile/<int:post_id>/', views.post_detail, name='post_detail'),
]