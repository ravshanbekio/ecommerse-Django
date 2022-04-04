from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.views import View
from .models import Main_User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse
from django.contrib.auth.forms import PasswordResetForm
from django.template.loader import render_to_string
from django.db.models.query_utils import Q
from django.utils.http import urlsafe_base64_encode
from django.contrib.auth.tokens import default_token_generator
from django.utils.encoding import force_bytes

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
            foydalanuvchi = authenticate(request, username=main_user.user, password=main_user.user.password)
            login(request, foydalanuvchi)
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

def password_reset_request(request):
	if request.method == "POST":
		password_reset_form = PasswordResetForm(request.POST)
		if password_reset_form.is_valid():
			data = password_reset_form.cleaned_data['email']
			associated_users = User.objects.filter(Q(username=data))
			if associated_users.exists():
				for user in associated_users:
					subject = "Password Reset Requested"
					email_template_name = "password_reset_email.txt"
					c = {
					"email":user.username,
					'domain':'127.0.0.1:8000',
					'site_name': 'Alistyle',
					"uid": urlsafe_base64_encode(force_bytes(user.pk)),
					"user": user,
					'token': default_token_generator.make_token(user),
					'protocol': 'http',
					}
					email = render_to_string(email_template_name, c)
					try:
						send_mail(subject, email, 'ravshanbekrm06@gmail.com' , [user.username], fail_silently=False)
					except BadHeaderError:
						return HttpResponse('Invalid header found.')
					return redirect ("password_reset_done")
	password_reset_form = PasswordResetForm()
	return render(request=request, template_name="password-reset.html", context={"form":password_reset_form})