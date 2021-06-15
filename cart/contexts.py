from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from bikes.models import Bike


def cart_contents(request):

    cart_items = []
    total = 0
    bike_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        bike = get_object_or_404(Bike, pk=item_id)
        total += quantity * bike.price
        bike_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'bike': bike,
        })

    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'bike_count': bike_count,
        'grand_total': grand_total,
    }

    return context
