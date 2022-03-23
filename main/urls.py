from django.urls import path
from .views import IndexView, HomeView, CategoryView, InternalView, ProductsView, ProductDetailView

urlpatterns = [
    path('',IndexView.as_view(), name='index'),
    path('home/',HomeView.as_view(), name='home'),
    path('category/',CategoryView.as_view(), name='category'),
    path('category/<pk>/',InternalView.as_view(), name='internal'),
    path('category/<pk>/products/',ProductsView.as_view(),name='product'),
    path('category/<pk>/products/<name>/',ProductDetailView.as_view(), name='product-detail'),
    #path('wishlist/<user>/',WishlistView.as_view(), name='wishlist'),
]