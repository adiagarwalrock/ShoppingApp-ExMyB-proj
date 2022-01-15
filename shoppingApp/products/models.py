from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
# Create your models here.


class Post(models.Model):
    productName = models.CharField(max_length=255)
    brand = models.CharField(max_length=255, default="Generic")
    price = models.IntegerField()
    productImage = models.ImageField(
        null=True, blank=False, upload_to="images/")
    rating = models.IntegerField(
        validators=[MinValueValidator(0),
                    MaxValueValidator(5)])
    seller = models.ForeignKey(User, on_delete=models.CASCADE)
    productDetails = RichTextField(
        blank=False, null=True, config_name='default')
    publishedDate = models.DateField(auto_now_add=True)
    category = models.CharField(max_length=255, default="UnCategorized")

    def get_absolute_url(self):
        return reverse('home')


class Categories(models.Model):
    name = models.CharField(max_length=255)

    def get_absolute_url(self):
        return reverse('home')


class Newsletter(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=254, unique=True)

    def get_absolute_url(self):
        return reverse('home')
