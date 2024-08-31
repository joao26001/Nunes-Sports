from django.urls import path
from .views import ProdutoView


urlpatterns = [
    path('', ProdutoView.as_view(), name='home'),
]
