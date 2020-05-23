from django.conf.urls import url
from django.urls import path
from home.views import HomeView
from . import views

urlpatterns =[
    path('', HomeView.as_view( ) ,name='accounty'),
    path('connect/<str:operation>/<int:pk>',  views.friendship,   name='friendship')
]