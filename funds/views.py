from django.shortcuts import render
from django.db.models import Q
from .models import Fund
from .filters import FundFilter


def home(request):
    return render(request, 'funds/home.html')


def view_funds(request):
    """ View to display all funds """
    funds = Fund.objects.all()
    funds_num = Fund.objects.all().count()
    
    """filter data by strategy"""
    filter = FundFilter(request.GET, queryset=funds)
    funds = filter.qs
        

    context = {
        'funds': funds,
        'funds_num': funds_num,
        'filter': filter
    }
    return render(request, 'funds/funds.html', context)
