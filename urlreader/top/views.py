from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def top(request):
    x_value = request.GET.get(key='x', default='0')
    y_value = request.GET.get(key='y', default='0')
    numbers = int(x_value) + int(y_value)
    params = {
        'numbers': numbers,
    }
    return render(request, 'top.html', params)