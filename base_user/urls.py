from django.urls import path
from .views import RegisterView, LoginView, LogoutView

urlpatterns = [
    path('signup/',RegisterView.as_view(), name='signup'),
    path('signin/',LoginView.as_view(), name='signin'),
    path('logout/',LogoutView.as_view(), name='logout'),
]