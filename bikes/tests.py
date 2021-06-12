from django.test import TestCase
from bikes.forms import BikeForm


class TestBikeForm(TestCase):

    def test_sku_is_not_required(self):
        form = BikeForm({'name': 'Test Name'
                        'description:' 'Test Description'
                        })
        self.assertFalse(form.is_valid())

    def test_bike_name_is_required(self):
        form = BikeForm({'name': 'Test name'})
        self.assertFalse(form.is_valid())

    def test_description_is_required(self):
        form = BikeForm({'description': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('description', form.errors.keys())
        self.assertEqual(form.errors['description'][0],
                         'This field is required.')

    def test_price_is_required(self):
        form = BikeForm({'price': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('price', form.errors.keys())
        self.assertEqual(form.errors['price'][0], 'This field is required.')


class TestViews(TestCase):

    def test_view_bikess(self):
        response = self.client.get('/bikess/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(
            response, 'bikes/bikess.html')
