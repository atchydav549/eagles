from django.contrib import admin
from .models import *

# Register your models here.

class AppInfoAdmin(admin.ModelAdmin):
    list_display = ['id']

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    list_display = ['id', 'type', 'img', 'price', 'uploaded', 'featured', 'popular']


admin.site.register(AppInfo)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Size)
admin.site.register(Contact)
admin.site.register(Customer)
admin.site.register(Cart)
admin.site.register(Order)




