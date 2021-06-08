from django.shortcuts import get_object_or_404
from bikes.models import Bike


def cart_contents(request):
    """Returns the cart items through context"""
    cart_items = []
    total = 0
    bike_count = 0
    cart = request.session.get('cart', {})

    for bike_id, quantity in cart.items():
        bike = get_object_or_404(Bike, pk=bike_id)
        total += quantity * bike.price
        bike_count += quantity
        cart_items.append({
            'bike_id': bike_id,
            'quantity': quantity,
            'bike': bike,
        })

    context = {
        'cart_items': cart_items,
        'total': total,
        'bike_count': bike_count,
    }

    return context
