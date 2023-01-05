from django.shortcuts import render
from django.http import HttpResponse
from listings.models import Listing
from realtors.models import Realtor
# Create your views here.

def index(request):
    latest_listings=Listing.objects.order_by('-list_date')[:3]
    context={
        'latest_listings':latest_listings
    }
    return render(request,'pages/index.html',context)


def about(request):
    realtors=Realtor.objects.all()
    realtorsAreMVP=Realtor.objects.filter(is_mvp=True)
    context={
        'realtorsAreMVP':realtorsAreMVP,
        'realtors':realtors
    }
    return render(request,'pages/about.html',context)