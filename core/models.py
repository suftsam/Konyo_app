from django.db import models
from django.contrib.auth.models import User
import uuid

ARTIST_CHOICES = [
    ('hacajaka', 'hacajaka'),
    ('oladapo', 'oladapo'),
    ('kwadwo', 'kwadwo'),
    ('massimo', 'massimo'),
    ('patrick', 'patrick')

]


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    artist = models.CharField(max_length=100, choices=ARTIST_CHOICES)
    product_image = models.ImageField(upload_to='product_image', null=True, blank=True)
    title = models.CharField(max_length=100, blank=True)
    medium = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)
    price = models.CharField(max_length=100, blank=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    middle_name = models.CharField(max_length=100, blank=True)


class Post(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='posts')
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    artwork = models.ImageField(upload_to='artworks', null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=100, blank=True)


class Exhibit(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    artist = models.CharField(max_length=100, choices=ARTIST_CHOICES)
    image = models.ImageField(upload_to='product_image', null=True, blank=True)
    title = models.CharField(max_length=100, blank=True)
    medium = models.CharField(max_length=100, blank=True)
    size = models.CharField(max_length=100, blank=True)
    price = models.CharField(max_length=100, blank=True)


class Org(models.Model):
    cover = models.ImageField(upload_to='org_cover', blank=True, null=True)
    title = models.CharField(max_length=100, blank=False)
    tex = models.TextField(blank=False)
