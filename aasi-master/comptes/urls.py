from django.contrib import admin
from django.urls import path
from comptes import views 

urlpatterns = [
    path('',views.Login,name="accueil"),
    path('logout',views.Logout,name="deconnexion")
]
