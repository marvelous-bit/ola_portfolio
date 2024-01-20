from django.urls import path

from .views import indexView, blogdetail
from . import views

urlpatterns = [
    path('', views.indexView, name='index'),
    path('<slug:slug>/', views.blogdetail, name='blogdetail'),
]