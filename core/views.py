from django.shortcuts import render, get_object_or_404
from .models import Product, UserProfile, Post, Exhibit
from django.contrib.auth.models import User


def home(request):
    page = 'home'
    # Fetch the first four images for each user
    users_with_images = User.objects.filter(posts__isnull=False).distinct()

    user_data = []
    for user in users_with_images:
        user_profile = UserProfile.objects.get(user=user)
        user_posts = Post.objects.filter(user=user)[:1]
        user_data.append({
            'user_profile': user_profile,
            'user_posts': user_posts,
        })

    context = {
        'page': page,
        'user_data': user_data,
    }
    return render(request, 'core/home.html', context)


def shop(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    products = Product.objects.all()

    if query:
        # Filter products based on the search query
        products = products.filter(title__icontains=query)

    context = {
        'products': products,
        'query': query,
    }

    return render(request, 'core/shop.html', context)


def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    context = {'product': product}
    return render(request, 'core/product_details.html', context)


def insight(request):
    return render(request, 'core/insight.html')


def portfolio_page(request):
    # Fetch the first four images for each user
    users_with_images = User.objects.filter(posts__isnull=False).distinct()

    user_data = []
    for user in users_with_images:
        user_profile = UserProfile.objects.get(user=user)
        user_posts = Post.objects.filter(user=user)[:4]
        user_data.append({
            'user_profile': user_profile,
            'user_posts': user_posts,
        })

    context = {
        'user_data': user_data,
    }
    return render(request, 'core/port_page.html', context)


def user_posts_view(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user_profile = get_object_or_404(UserProfile, user=user)

    query = request.GET.get('q', '')  # Get the search query from the request
    user_posts = Post.objects.filter(user=user)

    if query:
        # Filter user posts based on the search query
        user_posts = user_posts.filter(title__icontains=query)

    context = {
        'user_profile': user_profile,
        'user_posts': user_posts,
        'query': query,
    }

    return render(request, 'core/user_posts.html', context)


def exhibits(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    exhibits = Exhibit.objects.all()

    if query:
        # Filter products based on the search query
        exhibits = exhibits.filter(title__icontains=query)

    context = {
        'exhibits': exhibits,
        'query': query,
    }
    return render(request, 'core/exhibit.html', context)


def exhibit_detail(request, exhibit_id):
    page = "exhibit"
    exhibit = get_object_or_404(Exhibit, id=exhibit_id)
    context = {
        'page': page,
        'exhibit': exhibit
    }
    return render(request, 'core/product_details.html', context)