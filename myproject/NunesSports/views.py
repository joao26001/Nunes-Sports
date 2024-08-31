from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from .models import Produto
from .forms import ProdutoForm


class ProdutoView(View):
    def get(self, request, *args, **kwargs):
        produtos = Produto.objects.all()
        produto_id = request.GET.get('edit')
        if produto_id:
            produto = get_object_or_404(Produto, id=produto_id)
            form = ProdutoForm(instance=produto)
        else:
            form = ProdutoForm()

        return render(request, 'home.html', {'produtos': produtos, 'form': form})

    def post(self, request, *args, **kwargs):
        if 'delete' in request.POST:
            return self.post_delete(request, *args, **kwargs)
        produto_id = request.POST.get('produto_id')
        if produto_id and produto_id != None:
            produto = get_object_or_404(Produto, id=produto_id)
            form = ProdutoForm(request.POST, instance=produto)
        else:
            form = ProdutoForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

        produtos = Produto.objects.all()
        return render(request, 'home.html', {'produtos': produtos, 'form': form})


    def post_delete(self, request, *args, **kwargs):
        produto_id = request.POST.get('delete')
        if produto_id:
            produto = get_object_or_404(Produto, id=produto_id)
            produto.delete()
        return redirect('home')
