import csv, io
from django.shortcuts import render
from django.db.models import Sum
from django.contrib import messages
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Fund
from .filters import FundFilter
from .serializers import FundSerializer


def home(request):
    return render(request, 'funds/home.html')


def upload(request):
    """ Function to upload data from csv file """
    if request.method == 'POST':
        uploaded_file = request.FILES['data-file']
        
        # check to ensure file is .csv format
        if not uploaded_file.name.endswith('.csv'):
            messages.error(request, 'File not loaded - please upload data in .csv format')

        # load file data to the funds model
        file_data = uploaded_file.read().decode('UTF-8')
        io_string = io.StringIO(file_data)
        next(io_string) # skip first line of file holding field names
        for column in csv.reader(io_string, delimiter=','):
            _, created = Fund.objects.update_or_create(
                name = column[0],
                strategy = column[1],
                aum = column[2],
                inception_date = column[3]
            )

    return render(request, 'funds/upload.html')


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


@api_view(('Get',))
def funds_list(request):
    """ API View of All Fund Data """
    funds = Fund.objects.all()
    serializer = FundSerializer(funds, many=True)

    return Response(serializer.data)


@api_view(('Get',))
def fund_detail(request, id):
    """ API View of Individual Fund Data """
    
    try:
        fund = Fund.objects.get(pk=id)

    # display error if invalid ID keyed directly into url path / browser
    except:
        return Response({
            'error': 'Fund ID does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    serializer = FundSerializer(fund)

    return Response(serializer.data)
