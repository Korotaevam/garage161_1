from django.shortcuts import render


def home(request):
    return render(request, 'garage_stock/home.html')
