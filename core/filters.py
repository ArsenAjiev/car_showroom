from django_filters import rest_framework as filters
from car.models import Car


# Create custom class
# BaseInFilter - use IN for filter
# CharFilter - use text for search
class CharFilterInFilter(filters.BaseInFilter, filters.CharFilter):
    pass


class CarFilter(filters.FilterSet):
    make = CharFilterInFilter(field_name='make', lookup_expr='in')
    year = filters.RangeFilter()

    class Meta:
        model = Car
        fields = ['make', 'year']
