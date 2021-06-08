from django.shortcuts import render, redirect
from django.contrib import messages


def view_cart(request):
    """A view that shows the cart page"""
    return render(request, 'cart/cart.html')


def add_to_cart(request, bike_id):
    """Function to add quantity to cart"""
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if quantity <= 0:
        print('Sorry, the minimum quantity you need to buy is 1')
        # Add toast message
    else:
        if quantity > 0 and quantity <= 5:
            if bike_id in list(cart.keys()):
                # Prevents user from adding more than 5 items
                if quantity + cart[bike_id] > 5:
                    messages.warning(
                        request,
                        'Sorry, the maximum quantity you can buy is 5')
                else:
                    cart[bike_id] += quantity
                    messages.success(request, 'Added to Cart')
            else:
                cart[bike_id] = quantity
                messages.success(request, 'Added to Cart')
        else:
            messages.warning(
                request, 'Sorry, the maximum quantity you can buy is 5')
    request.session['cart'] = cart

    return redirect(redirect_url)


def update_cart(request, bike_id):
    """Function to update the quantity in cart"""
    cart = request.session.get('cart', {})
    update_quantity = int(request.POST.get('update_quantity'))
    redirect_url = request.POST.get('redirect_url')

    if update_quantity < 0 or update_quantity > 5:
        messages.warning(
            request, 'Sorry, the quantity should be between 0 and 5')
    elif update_quantity > 0 and update_quantity <= 5:
        cart[bike_id] = update_quantity
        messages.warning(
            request, 'Your Cart is Up-To-Date')
    else:
        cart.pop(bike_id)
        messages.error(request, 'Item Removed From Cart')
    request.session['cart'] = cart

    return redirect(redirect_url)


def remove_from_cart(request, bike_id):
    """Function to remove an item from cart"""
    cart = request.session.get('cart', {})
    cart.pop(bike_id)
    messages.error(request, 'Item Removed From Cart')
    redirect_url = request.POST.get('redirect_url')
    request.session['cart'] = cart

    return redirect(redirect_url)
