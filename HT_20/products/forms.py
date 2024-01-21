from django import forms
from django.core.validators import RegexValidator

from .models import Product


class GetProductIdsForm(forms.Form):
    ids_raw_data = forms.CharField(
        label='Введіть ID продуктів, розділені комою',
        max_length=5000,
        validators=[
            RegexValidator(
                regex=r'^[a-zA-Z\d,]+$',
                code='invalid_input',
            ),
        ]
    )


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['product_id', 'name', 'price', 'short_description', 'brand', 'category', 'link_to_product',
                  'update_date']
