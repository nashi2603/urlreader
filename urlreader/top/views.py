from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect

from .forms import UploadFileForm
from django.conf import settings

# Create your views here.

def top(request):
    # x_value = request.GET.get(key='x', default='0')
    # y_value = request.GET.get(key='y', default='0')
    # numbers = int(x_value) + int(y_value)
    # params = {
    #     'numbers': numbers,
    # }
    print(request.FILES)
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            Handle_Uploaded_File(request.FILES['file'])
            return HttpResponseRedirect('/results')
    else:
        form = UploadFileForm()
    return render(request, 'top.html', {'form': form})

def Handle_Uploaded_File(f):
    BASE_DIR = getattr(settings, "BASE_DIR", None)
    with open(BASE_DIR + "\\images\\" + f.name, 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)