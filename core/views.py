# import random
from django.shortcuts import render, get_object_or_404
from .models import Product, UserProfile, Post, Exhibit, Org, Insight
from django.contrib.auth.models import User

from django.http import FileResponse
import os
from django.conf import settings


from django.core.mail import send_mail
from django.http import HttpResponseRedirect


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

    orgs = Org.objects.all()

    context = {
        'page': page,
        'user_data': user_data,
        'orgs': orgs
    }
    return render(request, 'core/home.html', context)


def shop(request):
    page = "shop"
    query = request.GET.get('q', '')  # Get the search query from the request
    products = list(Product.objects.all())
    # random.shuffle(products)

    if query:
        # Filter products based on the search query
        products = products.filter(title__icontains=query)

    context = {
        'page': page,
        'products': products,
        'query': query,
    }

    return render(request, 'core/shop.html', context)


def product_detail(request, product_id):
    page = 'product_detail'
    product = get_object_or_404(Product, id=product_id)
    context = {
        'page': page,
        'product': product
    }
    return render(request, 'core/product_details.html', context)


def insight(request):
    return render(request, 'core/insight.html')


def portfolio_page(request):
    page = "portfolio-list"
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
        'page': page,
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
    page = "exhibition"

    query = request.GET.get('q', '')  # Get the search query from the request
    exhibits = list(Exhibit.objects.all())
    # random.shuffle(exhibits)

    if query:
        # Filter products based on the search query
        exhibits = exhibits.filter(title__icontains=query)

    context = {
        'page': page,
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


def org_info_detail(request, pk):
    org_info = get_object_or_404(Org, pk=pk)
    paragraphs = org_info.text.split('\n')
    context = {
        'org_info': org_info,
        'paragraphs': paragraphs
    }
    return render(request, 'core/org_info.html', context)


def about_page(request):
    page = "about"
    context = {
        'page': page,
    }
    return render(request, 'core/about.html', context)


def thanks_page(request):
    page = 'thanks'
    return render(request, 'core/thanks.html', {'page': page})


def contact_view(request):
    if request.method == 'POST':
        # Process the form submission
        # Assuming the form has fields 'subject' and 'message'
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        from_email = request.POST.get('email')

        # Send the email
        send_mail(
            subject,
            message,
            from_email, # Sender's email
            ['samuelaffedi@gmail.com'],  # List of recipient email addresses
            fail_silently=False,
        )

        return HttpResponseRedirect('thanks/')  # Redirect to thank you page

def download_pdf(request):
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'catalogue.pdf')
    if os.path.exists(pdf_path):
        return FileResponse(open(pdf_path, 'rb'), content_type='application/pdf')
    else:
        # Handle file not found scenario
        return HttpResponse("File not found", status=404)