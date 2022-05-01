from django.shortcuts import render, HttpResponse

# Create your views here.
def view_funds(request):
    """ View to display all funds """
    return HttpResponse("Test - fund page displayed")
