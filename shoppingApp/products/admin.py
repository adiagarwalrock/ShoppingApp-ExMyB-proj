from django.contrib import admin
from .models import Post, Categories, Newsletter

# Register your models here.
admin.site.register(Post) # shows the model in the admin panel
admin.site.register(Categories)
admin.site.register(Newsletter)