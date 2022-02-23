from django import forms
from .models import Prices, PickupLocation
from products.models import Product, Control
from events.models import Events


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ('name', 'price', 'description',
                    'nmbr_remaining', 'featured', 'discontinued',
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


class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = ('name', 'label', 'description',
                    'date', 'image_1')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        placeholders = {
            'name': "Event name",
            "label": "Label for you",
            'description': "Location/description",
        }

        self.fields['name'].widget.attrs['autofocus'] = True

class ControlForm(forms.ModelForm):
    class Meta:
        model = Control
        fields = ('no_orders',)


class PickupLocationForm(forms.ModelForm):
    class Meta:
        model = PickupLocation
        fields = ("name", "label", "postcode", 
                    "description", "town_or_city",
                    "street_address1",
                    "street_address2", "active",
                    )

    def __init(self, *args, **kwargs):
        super().__init__(*args, **kwargs)