from django import forms
from .models import Prices, PickupLocation
from products.models import Product
from events.models import Events


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description', 'featured',
                    'nmbr_remaining', 'discontinued',
                    'vegan', 'gluten_free', 'nut_free',
                    'image_1', 'image_2', 'image_3')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': "Product name", 
            'price': "Specified price", 
            'description': "Description", 
            'featured': False,
            'discontinued': False,
            'vegan': False, 
            'gluten_free': False, 
            'nut_free': False,
        }

        self.fields['name'].widget.attrs['autofocus'] = True