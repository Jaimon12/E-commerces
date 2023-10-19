from django.contrib import admin
from .models import Category, Product,ContactMessage

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'stock', 'available', 'created', 'get_updated']  # Updated here
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}

    def get_updated(self, obj):
        return obj.updated.strftime('%Y-%m-%d %H:%M:%S') if obj.updated else ''
    get_updated.admin_order_field = 'updated'
    get_updated.short_description = 'Updated'
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')

admin.site.register(ContactMessage, ContactMessageAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
