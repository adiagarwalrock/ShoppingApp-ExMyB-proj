"""shoppingApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('product/', include('product.urls'))
"""
from django.urls import path
from .views import ProductsListView, HomeView
from .views import AddNewProductView, UpdateProductView, DeleteProductView, ProductView
from .views import AddNewCategoryView, categoryView, CategoryListView
from .views import searchResultsView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('products/', ProductsListView.as_view(), name="products"),
    path('product/<int:pk>', ProductView.as_view(), name="product"),
    path('addNewProduct/', AddNewProductView.as_view(), name="addNewproduct"),
    path('product/update/<int:pk>', UpdateProductView.as_view(), name="updateProduct"),
    path('product/delete/<int:pk>', DeleteProductView.as_view(), name="deleteProduct"),
    path('addNewCategory/', AddNewCategoryView.as_view(), name="addNewCategory"),
    path('category/<str:category>', categoryView, name="category"),
    path('category/', CategoryListView, name="categoryList"),
    path('search/', searchResultsView, name="searchresults"),
]