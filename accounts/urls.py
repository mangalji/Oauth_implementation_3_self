from django.urls import path
from .views import RegisterView, LoginView, LogoutView, GoogleLoginSuccessView, profile_view
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/',RegisterView.as_view(),name='register'),
    path('login/',LoginView.as_view(),name="login"),
    path('logout/',LogoutView.as_view(),name="logout"),
    path("profile/",profile_view,name='profile'),
    path('token/refresh/',TokenRefreshView.as_view(),name="refresh-token"),
    path("google/success/",GoogleLoginSuccessView.as_view(),name="success-view"),
]
