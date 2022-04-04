from django.urls import path
from .views import RegisterView, LoginView, LogoutView, password_reset_request
from django.contrib.auth import views

urlpatterns = [
    path('signup/',RegisterView.as_view(), name='signup'),
    path('signin/',LoginView.as_view(), name='signin'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('password-reset/',password_reset_request, name='password_reset'),
    path('password-reset/done/',views.PasswordResetDoneView.as_view(template_name='password-reset-done.html'),name='password_reset_done'),
    path('password-reset/confirm/<uidb64>/<token>/',views.PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html'),name='password_reset_confirm'),\
    path('reset/done/',views.PasswordResetCompleteView.as_view(template_name='password-reset-complete.html'),name='password_reset_complete'),
]