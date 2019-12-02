from django.shortcuts import render
from django.http import HttpResponse

from . import CV

# Create your views here.

def results(request):
    if request.GET.get(key='upload', default='false') == "True":
        imgfilename = request.COOKIES['imgfilename']
    else:
        imgfilename = "画像がアップロードされていません。"
    return render(request, 'results.html', {'imgfilename': imgfilename})