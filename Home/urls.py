from django.contrib import admin
from django.urls import path
from Home import views
# from .views import *

urlpatterns = [
    path('', views.index, name='Home'),
    path("about", views.about, name='about'),
    path('services', views.services, name="services"),
    path('contact', views.contact, name='contact'), 
    path('services/interior', views.interior, name='interior' ),
    path('services/exterior', views.exterior, name='exterior' ),
    path('services/customization', views.customization, name='customization' ),
    # path('register/', views.register_user, name='register'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard')
]



