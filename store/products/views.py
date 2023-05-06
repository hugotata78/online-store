from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from . models import Product

# Create your views here.

class HomePageView(ListView):
    model = Product
    template_name = 'home_page.html'

class ListProductView(ListView):
    model = Product
    template_name = 'template_product/list_product.html'
    context_object_name = 'products'

class DetailProductView(DetailView):
    model = Product
    template_name = 'template_product/detail_product.html'
    
    def get_context_data(self, **kwargs):
        context = super(DetailProductView,self).get_context_data(**kwargs)
        context['related'] = Product.objects.filter(brand=context['object'])[:3]
        print(context['related'])
        return context
