#encoding:utf-8

from django.urls import path
from django.contrib import admin
from main import views

urlpatterns = [
    path('', views.index),
    path('populate/', views.populateDB),
    path('loadRS', views.loadRS),
    path('recommendedPeripheralsItems', views.recommendedFilmsItems),
    path('recommendedPeripheralsUser', views.recommendedFilmsUser),
    path('similarPeripheral', views.similarFilms),
    path('recommendedUsersPeripherals', views.recommendedUsersFilms),
    path('search', views.search),
    path('admin/', admin.site.urls),
]