from django.contrib import messages
from django.shortcuts import render
from .models import DataModel

# Create your views here.
def home(request):

    return render(request,'home.html')

def annual_data(request):
    api=''
    if request.method=='POST':
        API_WELL=request.POST.get('API_WELL_NUMBER')

        api=DataModel.objects.filter(API_WELL_NUMBER=API_WELL).values()

    return render(request,'quarted_data.html',{'data':api})