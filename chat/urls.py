from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

urlpatterns=[
    path('', views.index, name='index' ),
    path('<str:room>/', views.room, name='room'),
    path('checkview',views.checkview, name='checkview'),
    path('send',views.send, name='send'),
    path('getMessages/<str:room>/',views.getMessages, name = 'getMessages')
]