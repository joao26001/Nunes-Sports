from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView


class ProdutoListView(ListView):
    model = Produto
    template_name = 'home.html'   
