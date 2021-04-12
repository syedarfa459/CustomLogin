
from django.urls import path
from . import views

app_name = 'customapp'
urlpatterns = [
    
    path('', views.loginView, name='login'),
    path('logout', views.logoutView, name='logout'),
    path('register', views.registerView, name='register'),
]
