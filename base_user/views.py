from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from .models import Main_User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

class RegisterView(View):
    def get(self, request):
        return render(request, 'page-user-register.html')

    def post(self, request):
        user = User.objects.create_user(
            username=request.POST['email'],
            password=request.POST['password1']
        )
        if user.username in User.objects.all():
            messages.error(request, "Email already taken!")
            return redirect('signup')
        else:
            user.save()
            main_user = Main_User.objects.create(
                name=request.POST['first_name']+" "+request.POST['last_name'],
                email=request.POST['email'],
                gender=request.POST['gender'],
                user=user,
                city=request.POST['city'],
                country=request.POST['country'],
            )
            main_user.save()
            return redirect('home')

class LoginView(View):
    def get(self, request):
        return render(request, 'page-user-login.html')

    def post(self, request):
        username = request.POST['email']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "User notfound!")
            return redirect('signin')

class LogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('signin')

