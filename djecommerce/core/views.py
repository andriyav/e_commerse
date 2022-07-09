from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Item



class HomeView(ListView):
    model = Item
    template_name = "core/home.html"


class ItemViewDetail(DetailView):
    model = Item
    template_name = "core/product.html"
