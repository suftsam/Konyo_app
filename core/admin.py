from django.contrib import admin
from .models import Product, Post, UserProfile, Exhibit

# Register your models here.
admin.site.register(Product)
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Exhibit)
