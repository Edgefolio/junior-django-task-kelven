import django_filters
from .models import Fund

class FundFilter(django_filters.FilterSet):
    class Meta:
        model = Fund
        fields = ['strategy']