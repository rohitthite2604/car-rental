from django.contrib import admin
from django.urls import include, path
from car import views

urlpatterns = [
path('', views.home, name='home'),
path('car',views.car, name='car'),
path('book/<int:car_id>/', views.book_car, name='book_car'),
]