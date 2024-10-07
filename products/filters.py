# filters.py
import django_filters
from .models import Product

class ProductFilter(django_filters.FilterSet):
    type = django_filters.ChoiceFilter(choices=Product.TYPE_CHOICES)
    lifespan = django_filters.ChoiceFilter(choices=Product.LIFESPAN_CHOICES)
    light_exposure = django_filters.ChoiceFilter(choices=Product.LIGHT_EXPOSURE_CHOICES)
    soil_drainage = django_filters.ChoiceFilter(choices=Product.SOIL_DRAINAGE_CHOICES)

    class Meta:
        model = Product
        fields = ['type', 'lifespan', 'light_exposure', 'soil_drainage']