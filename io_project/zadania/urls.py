from django.urls import path
from . import views
urlpatterns = [
    path('', views.index2, name='index'),
    path('rozklad_lu/', views.rozklad_lu, name='rozklad_lu'),
    path('rozniczkowanie/', views.rozniczkowanie, name='rozniczkowanie'),
    path('rownania_nieliniowe/', views.rownania_nieliniowe, name='rownania_nieliniowe'),
    path('simplex/', views.simplex, name='simplex'),
    path('calkowanie/', views.calki, name='calki'),
    #path('register/', views.register2, name='register'),
    #path('login/', views.login, name='login'),
    #path('', views.logout, name='logout'),
]