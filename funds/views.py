from django.shortcuts import render
from django.db.models import Sum
from .models import Fund
from .filters import FundFilter


def home(request):
    return render(request, 'funds/home.html')


def view_funds(request):
    """ View to display all funds """
    funds = Fund.objects.all()
    
    """ Filter data by strategy """
    filter = FundFilter(request.GET, queryset=funds)
    funds = filter.qs

    """ Totals: Count / Sum """
    funds_num = funds.count()
    funds_aum = funds.aggregate(total_aum=Sum('aum'))    
    funds_val = funds_aum['total_aum']

    context = {
        'funds': funds,
        'funds_num': funds_num,
        'funds_val': funds_val,
        'filter': filter
    }
    return render(request, 'funds/funds.html', context)
