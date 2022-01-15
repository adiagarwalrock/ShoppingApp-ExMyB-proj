from django.contrib import admin
from .models import Post, Categories, Newsletter


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    # exclude = ['clicks', 'short_url', 'created_on'] # exclused fields from the form
    readonly_fields = ['rating']
    list_display = ['productName', 'brand', 'rating',
                    'seller', 'publishedDate', 'category']
    search_fields = ['seller', 'productName']
    # search_help_text = "Search actual url or short url from the database."
    date_hierarchy = 'publishedDate'
    list_display_links = ['productName', 'brand',
                          'rating', 'seller', 'publishedDate', 'category']
    ordering = ['productName', ]
    show_full_result_count = True


@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    list_display_links = ['name', 'email']
    readonly_fields = ['name', 'email']
    ordering = ['name']
    search_fields = ['name', 'email']
    show_full_result_count = True
