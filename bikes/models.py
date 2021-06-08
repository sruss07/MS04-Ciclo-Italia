from django.db import models


class Brand(models.Model):

    class Meta:
        verbose_name_plural = 'Brands'

    name = models.CharField(max_length=254)
    frontend_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_frontend_name(self):
        return self.frontend_name


class Bike(models.Model):

    class Meta:
        verbose_name_plural = 'Bikes'

    brand = models.ForeignKey(
        'Brand', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    has_sizes = models.BooleanField(default=False, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
