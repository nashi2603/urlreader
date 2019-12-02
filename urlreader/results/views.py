from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.conf import settings

import os
import json
from . import CVReqMod
from . import separate_url
from . import shapehtmljson

# Create your views here.

BASE_DIR = getattr(settings, "BASE_DIR", None)
API_KEY = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'APIkey.json')))

def results(request):
    if request.GET.get(key='upload', default='false') == "True":
        imgfilename = request.COOKIES['imgfilename']
        imgjson = CVReqMod.DetectStringToJson(API_KEY['APIkey'], os.path.join(os.path.join(BASE_DIR, "images"), imgfilename))
        resultsdata = shapehtmljson.shapehtmltojson(separate_url.separate_url(imgjson['scantext'], True))
        nonresultsdata = shapehtmljson.shapehtmltojson(separate_url.separate_url(imgjson['scantext'], False))
        return render(request, 'results.html', {'resultsdata': resultsdata, 'nonresultsdata': nonresultsdata})
    else:
        resultdata = "画像がアップロードされていません。"
        return render(request, 'results.html', {'resultsdata': resultdata})