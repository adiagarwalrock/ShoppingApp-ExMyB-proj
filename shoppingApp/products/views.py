from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.db.models import Q
from django.http import HttpResponse

from .forms import PostForm, UpdateForm, NewCategoryForm
from .models import Post, Categories

import json

# Create your views here.


class HomeView(TemplateView):
    model = Post
    template_name = 'home.html'


class ProductsListView(ListView):
    model = Post
    # Page to render all the Products(list the Product).
    template_name = 'products.html'
    # ordering = ['-publishedDate']
    ordering = ['-id']


class ProductView(DetailView):
    model = Post
    template_name = 'readProduct.html'


class AddNewProductView(CreateView):
    model = Post
    template_name = 'newProduct.html'
    form_class = PostForm


class UpdateProductView(UpdateView):
    model = Post
    template_name = 'updateProduct.html'
    form_class = UpdateForm


class DeleteProductView(DeleteView):
    model = Post
    template_name = 'deleteProduct.html'
    form_class = UpdateForm
    success_url = reverse_lazy('products')


class AddNewCategoryView(CreateView):
    model = Categories
    template_name = 'newCategory.html'
    form_class = NewCategoryForm


def categoryView(request, category):
    categoryPost = Post.objects.filter(category=category.replace('-', ' '))
    return render(
        request, 'category.html', {
            'category': category.title().replace('-', ' '),
            'categoryPost': categoryPost,
        })


def CategoryListView(request):
    categoryList = Categories.objects.all()
    return render(request, 'categories.html', {'categoryList': categoryList})


def searchResultsView(request):
    if request.method == 'POST':
        search = request.POST['search']
        product = Post.objects.filter(
            Q(productName__contains=search) | Q(brand__contains=search)
            | Q(productDetails=search))
        return render(request, 'search.html', {
            'search': search,
            'products': product
        })
    else:
        return render(request, 'search.html', {})


def search_auto(request):
    if request.is_ajax():
        search = request.GET.get('term', '')
        products = Post.objects.filter(
            Q(productName__contains=search) | Q(brand__contains=search)
            | Q(productDetails=search))
        results = []
        for quer in products:
            # product_json = {}
            product_json = quer.productName
            results.append(product_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
