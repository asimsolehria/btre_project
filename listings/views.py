from django.shortcuts import render

# Create your views here.


def listings(request):
   return render(request,'listings/listings.html')


def listing(request):
    return render(request,'listings/listing.html')