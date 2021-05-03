# Use the following commands after you modify the models.py file
# python3 manage.py makemigrations
# python3 manage.py migrate

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    # Things we want to put in product (fields in the product)
    # eg. title, sub-heading, body etc
    productName = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, default="Generic")
    price = models.IntegerField()
    productImage = models.ImageField(null=True, blank=False, upload_to="images/")
    rating = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(5)])
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    # this will delete all the product post created by any user
    # if the user is deleted from the database
    # productDetails = models.TextField()
    productDetails = RichTextField(blank=False, null=True, config_name='default')
    publishedDate = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="UnCategorized")

    def __str__(self):
        # on admin page this will allow us to see the
        # title on the product and the name of author
        return self.brand + ' | ' +self.productName + ' | ' + str(self.seller)

    def get_absolute_url(self):
        return reverse('home')


class Categories(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('home')


class Newsletter(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.name + ' | ' +self.email

    def get_absolute_url(self):
        return reverse('home')