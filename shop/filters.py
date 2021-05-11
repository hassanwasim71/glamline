import django_filters
from .models import product
class productFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='iexact')

    class Meta:
        model = product
        fields = ['colour', 'type']