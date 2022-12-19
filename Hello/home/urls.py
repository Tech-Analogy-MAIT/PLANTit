from django.contrib import admin
from django.urls import path
from home import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.index, name='home'),
    path('index/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contactus/', views.contactus, name='contactus'),
    path('social/', views.social, name='social'),
]

urlpatterns += staticfiles_urlpatterns()