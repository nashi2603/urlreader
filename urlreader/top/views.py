from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

import os

from .forms import UploadFileForm
from django.conf import settings

# Create your views here.

def top(request):
    #print(request.FILES)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            Handle_Uploaded_File(request.FILES['file'])
            response = HttpResponseRedirect('/results')
            response['location'] += '?upload=True'
            response.set_cookie('imgfilename', value=request.FILES['file'].name, max_age=604800, path='/')
            return response
    else:
        form = UploadFileForm()
    return render(request, 'top.html', {'form': form})

def Handle_Uploaded_File(f):
    BASE_DIR = getattr(settings, "BASE_DIR", None)
    with open(os.path.join(os.path.join(BASE_DIR, "images"), f.name), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)