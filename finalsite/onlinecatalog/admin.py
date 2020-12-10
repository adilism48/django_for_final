from django.contrib import admin

from .models import Product, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'category', 'pub_date', 'is_published')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description')
    list_editable = ('is_published',)
    list_filter = ('is_published', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id', 'title')
    search_fields = ('title',)


admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
