from django.shortcuts import render


def index(request):
    """
    Home.
    """
    return render(request, 'index.html')
