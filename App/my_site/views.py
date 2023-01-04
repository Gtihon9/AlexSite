

from django.core.mail import send_mail
from django.http import HttpRequest
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from main_app.settings import EMAIL_HOST_USER

from .forms import CommentForm, ReportForm
from .models import Product
from .cart import add_cart_item


def product_list_view(request: HttpRequest):
    """redirect to catalogue"""
    products = Product.objects.all()
    return render(request, 'my_site/catalogue.html', {
        'products': products,
    })


def gallery_page(request):
    """redirect to gallery page"""
    return render(request, 'my_site/gallery.html')


def contacts_page(request: HttpRequest):
    if request.method == "POST":
        report_message_form = ReportForm(request.POST)
        if report_message_form.is_valid():
            report_message = report_message_form.save(commit=False)
            report_message.save()
            send_mail(subject="report from user",
                      message=f"{report_message.text}\nfrom {report_message.author_name}\n{report_message.email}\n{report_message.created_date}",
                      from_email=EMAIL_HOST_USER,
                      recipient_list=["gtihon9@gmail.com"])
            messages.success(request, "Ваше сообщение успешно отправлено")
            return render(request, 'my_site/contacts.html', {'report_message_form': ReportForm(request.GET)})
    else:
        report_message_form = ReportForm()

    return render(request, 'my_site/contacts.html', {
        'report_message_form': report_message_form,
    })


def news_page(request: HttpRequest):
    """redirect to news page"""
    return render(request, 'my_site/news.html')


def about_page(request: HttpRequest):
    """redirect to news page"""
    return render(request, 'my_site/about.html')


def home_page(request: HttpRequest):
    """return to home page"""
    return render(request, 'my_site/home.html')


def detail_view(request: HttpRequest, pk):
    product = get_object_or_404(Product, id=pk)
    # add comment
    if request.method == "POST":
        if request.POST.get('quantity'):
            add_cart_item(request, pk=pk)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = product
            comment.save()
            return redirect('detail', pk=product.id)
    else:
        comment_form = CommentForm()

    return render(request, 'my_site/detail.html', {
        'product': product,
        'comment_form': comment_form,
    })



