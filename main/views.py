from django.shortcuts import render, redirect
from django.views import View
from .models import Category, Category2, Shopping, Tovar
from base_user.models import Email
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

class IndexView(View):
    def get(self, request):
        return render(request, 'page-index-2.html')

    def post(self, request):
        email = Email.objects.create(
            email=request.POST['email']
        )
        email.save()
        messages.success(request, "Obunangiz muvaffaqiyatli qabul qilindi!")
        return redirect('index')

class HomeView(View):
    def get(self, request):
        # template = render_to_string('email_template.html',{'name':request.user.username})
        # email = EmailMessage(
        #     'Welcome to Alistyle!',
        #     template,
        #     settings.EMAIL_HOST_USER,
        #     [request.user.username],
        # )
        # email.fail_silently=False
        # email.send()
        return render(request, 'page-index.html')
    
    def post(self, request):
        email = Email.objects.create(
            email=request.POST['email']
        )
        email.save()
        messages.success(request, "Obunangiz muvaffaqiyatli qabul qilindi!")
        return redirect('home')

class CategoryView(View):
    def get(self, request):
        category = Category.objects.all()
        return render(request, 'page-category.html',{'category':category})

    def post(self, request):
        email = Email.objects.create(
            email=request.POST['email']
        )
        email.save()
        messages.success(request, "Obunangiz muvaffaqiyatli qabul qilindi!")
        return redirect('category')

class InternalView(View):
    def get(self, request, pk):
        internal = Category2.objects.get(id=pk)
        product = Tovar.objects.filter(inside_category=internal)
        return render(request, 'internal.html', {'internal':internal, 'product':product})

    def post(self, request, pk):
        internal = Category2.objects.get(pk=pk)
        email = Email.objects.create(
            email=request.POST['email']
        )
        email.save()
        messages.success(request, "Obunangiz muvaffaqiyatli qabul qilindi!")
        return redirect('internal', pk=internal.pk)

class ProductsView(View):
    def get(self, request, pk):
        product = Tovar.objects.get(id=pk)
        return render(request, 'page-listing-grid.html', {'product':product})

    def post(self, request, pk):
        product = Tovar.objects.get(id=pk)
        email = Email.objects.create(
            email=request.POST['email']
        )
        email.save()
        messages.success(request, "Obunangiz muvaffaqiyatli qabul qilindi!")
        return redirect('product', pk=product.id)

class ProductDetailView(View):
    def get(self, request, name, pk):
        internal = Category2.objects.get(id=pk)
        tovar = Tovar.objects.get(name=name)
        return render(request, 'page-detail-product.html',{'tovar':tovar, 'internal':internal})

    def post(self, request, pk,name):
        internal = Category2.objects.get(id=pk)
        tovar = Tovar.objects.get(name=name)
        email = Email.objects.create(
            email=request.POST['email']
        )
        email.save()
        messages.success(request, "Obunangiz muvaffaqiyatli qabul qilindi!")
        return redirect('product-detail',pk=internal.id, name=tovar.name)

class ShoppingCartView(View):
    def get(self, request, pk):
        tovar = Tovar.objects.get(id=pk)
        new_product = Shopping.objects.create(
            user=request.user,
            product=tovar
        )
        all = Shopping.objects.filter(id=pk)
        return render(request,'page-shopping-cart.html',{'all':all})

class WishlistView(View):
    def get(self, request, user):
        return render(request, 'page-profile-wishlist.html')