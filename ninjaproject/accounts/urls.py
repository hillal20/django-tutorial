from django.urls import path
from . import views



# app_name = 'account'

urlpatterns =[

path('', views.sign_up),
path('login/', views.loginView, name="login")
]