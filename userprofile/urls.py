from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.signup, name="signup"),  # è il sign up generico
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("myaccount/", views.myaccount, name="myaccount"),
    path("vendor/<int:pk>/", views.vendor_detail, name="vendor_detail"),
]

