from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='home'),
    path('food/', views.food),
    path('example/', views.example),
    path('hello/', views.message)
]
