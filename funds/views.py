from django.shortcuts import render
from .models import Fund


def home(request):
    return render(request, 'funds/home.html')


def view_funds(request):
    """ View to display all funds """
    funds = Fund.objects.all()
    context = {
        'funds': funds
    }
    return render(request, 'funds/funds.html', context)
