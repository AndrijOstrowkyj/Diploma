from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product, Reviews, Order
from django.contrib import messages
from django.db import IntegrityError


def index(request):
    query = request.GET.get('search', '')
    min_price = request.GET.get('min_price', '')
    max_price = request.GET.get('max_price', '')

    items = Product.objects.all()

    if query:
        items = items.filter(name__icontains=query)

    if min_price:
        items = items.filter(price__gte=min_price)

    if max_price:
        items = items.filter(price__lte=max_price)

    context = {
        'items': items,
        'search_query': query,
        'min_price': min_price,
        'max_price': max_price,
    }
    return render(request, 'myapp/index.html', context)


def indexItem(request, my_id):
   
    item = Product.objects.get(id = my_id)
    context = {
        'item': item
    }
    return render(request, 'myapp/details.html', context = context)


def place_order(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        phone_number = request.POST.get('phone_number')
        post_type = request.POST.get('post_type')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')
        payment_type = request.POST.get('payment_type')

        cart = request.session.get('cart', [])
        products_in_cart = Product.objects.filter(id__in=cart)

        if products_in_cart:
            total_price = sum(product.price for product in products_in_cart)

            user = request.user if request.user.is_authenticated else None

            try:
                order = Order.objects.create(
                    total_price=total_price,
                    phone_number=phone_number,
                    user=user,
                    first_name=first_name,
                    last_name=last_name,
                    post_type=post_type,
                    city=city,
                    postal_code=postal_code,
                    payment_type=payment_type
                )
                order.products.add(*products_in_cart)

                del request.session['cart']

                messages.success(request, 'Your order has been placed successfully.')

                if payment_type == 'Безготівково':
                    return redirect('myapp:card_payment')
                else:
                    return redirect('myapp:view_cart')

            except IntegrityError as e:
                messages.error(request, f'Error placing order: {e}')

    return redirect('myapp:index')


def contacts(request):
    return render(request, 'myapp/contacts.html')


def add_item(request):
    if request.method == "POST":
        product_id = request.POST.get("product_id")
        reviews_txt = request.POST.get("reviews_txt")
        
        if product_id:
            review = Reviews(product_id=product_id, reviews_txt=reviews_txt)
            review.save()
        else:
            return HttpResponse("Please provide a product ID.")
    
    return redirect(request.META['HTTP_REFERER'])



def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        cart = request.session.get('cart', [])
        cart.append(product_id)
        request.session['cart'] = cart
        return redirect('myapp:view_cart')

    

def view_cart(request):
    cart = request.session.get('cart', [])
    products_in_cart = Product.objects.filter(id__in=cart)
    context = {'products_in_cart': products_in_cart}
    return render(request, 'myapp/cart.html', context)


def card_payment(request):
    return render(request, 'myapp/card_payment.html')
