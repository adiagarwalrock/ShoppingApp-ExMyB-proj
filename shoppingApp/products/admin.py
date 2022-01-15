from django.contrib import admin
from .models import Post, Categories, Newsletter

# Register your models here.
# admin.site.register(Post) # shows the model in the admin panel

@admin.register(Post)
# admin.site.register(Url_data, Url_dataAdmin)
class PostAdmin(admin.ModelAdmin):
    # exclude = ['clicks', 'short_url', 'created_on'] # exclused fields from the form
    readonly_fields = ['rating']
    list_display = ['productName', 'brand', 'rating', 'seller', 'publishedDate', 'category']
    search_fields = ['seller', 'productName']
    # search_help_text = "Search actual url or short url from the database."
    date_hierarchy = 'publishedDate'
    list_display_links = ['productName', 'brand', 'rating', 'seller', 'publishedDate', 'category']
    ordering = ['productName', ]
    show_full_result_count = True

admin.site.register(Categories)
admin.site.register(Newsletter)