from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('shop/', views.shop, name='shop'),
    path('product_detail/<uuid:product_id>/', views.product_detail, name='product_detail'),
    path('portfolio_page/', views.portfolio_page, name='portfolio_page'),
    path('user_posts/<int:user_id>/', views.user_posts_view, name='user_posts'),
    path('insight/', views.insight, name='insight'),
    path('exhibits/', views.exhibits, name='exhibits'),
    path('exhibit_detail/<uuid:exhibit_id>/', views.exhibit_detail, name='exhibit_detail'),
    path('org_info_detail/<int:pk>/', views.org_info_detail, name='org_info_detail'),
    # path('insight/', views.insight_view, name='insight'),
    path('about/', views.about_page, name='about'),
]
