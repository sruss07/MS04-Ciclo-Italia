from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('first_name', 'last_name', 'email_address', 'address', 
                  'town', 'county', 'postcode')

        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Last Name'}),
            'email_address': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Email Address'}),
            'address1': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Address1'}),
            'town': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Town'}),
            'county': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'County'}),
            'postcode': forms.TextInput(attrs={
                'class': 'input',
                'placeholder': 'Postcode'}),
        }

    def __init__(self, *args, **kwargs):
        """
        Add placeholders and classes, code from CI checkout lesson
        """
        super().__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = False

