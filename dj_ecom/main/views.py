from django.shortcuts import render
from django.views.generic import ListView,DetailView, View
from .models import Product

# Create your views here.

def home(request):

    return render(request, 'main/home.html', )

class CategoryView(View):

    def get(self, request, val):

        product = Product.objects.filter(category = val)
        # title
        return render(request, 'main/category.html', locals()) 
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'main/product_detail.html'