from django.urls import include, path
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static

from . import views
from . import cart




urlpatterns = [

    path('gallery/', views.gallery_page, name="gallery"),
    path('catalogue/', views.product_list_view, name="product_list_view"),
    path('contacts/', views.contacts_page, name="contacts"),
    path('about/', views.about_page, name="about"),
    path('news/', views.news_page, name="news"),

    path('product/<int:pk>', views.detail_view, name="detail"),

    path('cart/', cart.view_cart, name="view_cart"),
    path('cart/delete/<int:pk>', cart.delete_cart_item, name="delete_cart_item"),
    path('cart/add/<int:pk>', cart.add_cart_item, name="add_cart_item"),
    path('', views.home_page, name='home'),
]
