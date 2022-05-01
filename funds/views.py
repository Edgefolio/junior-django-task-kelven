from django.shortcuts import render
from django.db.models import Q
from .models import Fund


def home(request):
    return render(request, 'funds/home.html')


def view_funds(request):
    """ View to display all funds """
    funds = Fund.objects.all()
    funds_num = Fund.objects.all().count()
    strat_filter = None
    
    """filter data by strategy"""
    if 'strategy_filter' in request.GET:
        strat_filter = request.GET['strategy_filter']
        filtered = Q(strategy__icontains=query)
        funds = funds.filter(filtered)

        print("Form get requested")

    context = {
        'funds': funds,
        'funds_num': funds_num,
        'filter': strat_filter
        
    }
    return render(request, 'funds/funds.html', context)
