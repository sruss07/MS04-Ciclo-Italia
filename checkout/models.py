import uuid

from django.db.models import Sum
from django.db import models

from bikes.models import Bike


class Order(models.Model):

    order_number = models.CharField(max_length=32, null=False, editable=False)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    email_address = models.CharField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=100, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town = models.CharField(max_length=50, null=False, blank=False)
    comments = models.CharField(max_length=1000, null=True, blank=True)
    order_date = models.DateField("Order Date", auto_now_add=True)
    cart_total = models.DecimalField(
        max_digits=10, decimal_places=2, null=False, default=0)

    def _generate_order_number(self):
        """
        Creates a unique order number using UUID
        Code used from CI checkout lesson
        """
        return uuid.uuid4().hex.upper()

    def update_cart_total(self):
        """
        Cart total updated each time an item is added
        Code used from CI checkout lesson
        """
        self.cart_total = self.lineitems.aggregate(
                            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        self.save()

    def save(self, *args, **kwargs):
        """
        Override the original save method to set the order number
        Code used from CI checkout lesson
        """
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    order = models.ForeignKey(
                            Order, null=False, blank=False,
                            on_delete=models.CASCADE, related_name='lineitems')
    bike = models.ForeignKey(
                        Bike, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(
                                max_digits=6, decimal_places=2, null=False,
                                blank=False, editable=False)

    def save(self, *args, **kwargs):
        """
        Gets the order number if it hasn't been set already
        Code used from CI checkout lesson
        """
        self.lineitem_total = self.bike.price * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f'SKU {self.bike.sku} on order {self.order.order_number}'
