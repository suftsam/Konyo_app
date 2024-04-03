from django.contrib import admin
from .models import Product, Post, UserProfile, Exhibit, Org, Insight

# Register your models here.
admin.site.register(Product)
admin.site.register(Post)
admin.site.register(UserProfile)
admin.site.register(Exhibit)
admin.site.register(Org)
admin.site.register(Insight)
