from django.urls import path

from . import views


app_name = 'products'
urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.post1, name='add'),
]