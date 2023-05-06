from django.urls import path
from . views import ListProductView, DetailProductView, HomePageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('products/', ListProductView.as_view(), name='products'),
    path('product/<int:pk>', DetailProductView.as_view(), name='product'),
]
