from django.shortcuts import render


# Create your views here.


def home_view(request):
    return render(request, 'main/base.html')

def custom_view(request, resource):
    return render(request, 'main/base.html')


