from django.urls import path
from . import views
from django.contrib import admin
urlpatterns = [
    path('login/',views.login_user,name="login"),
    path('signup/',views.signup_user,name="signup"),
    path('logout/',views.logout_user,name="logout"),
    path('update_user/',views.update_user,name="update_user"),
    path('update_password/',views.update_password,name="update_password"),
]