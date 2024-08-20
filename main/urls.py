from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('', main, name="main"),
    path('create', createUser, name="create_user"),
    path('delete', deleteAll, name="delete_all"),
    path('user/<int:pk>/edit/', update_user, name='edit'), 
    path('user/<int:pk>/delete/', delete_user, name='delete'), 
    path('accounts/login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
]
