from django.shortcuts import render

# Create your views here.
def view_funds(request):
    """ View to display all funds """
    return render(request, 'funds/funds.html')
