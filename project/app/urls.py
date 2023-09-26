from django.contrib import admin
from django.urls import path,URLPattern, re_path
from app import views

urlpatterns=[
    path('admin/',admin.site.urls),
    path('',views.home),
    path('login',views.login),
    path('compare',views.compare),
    path('newuser/',views.newuser,),
]