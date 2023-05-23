from django.shortcuts import render
import logging
import json,os
from django.http import JsonResponse

# Create your views here.
def index(request):
    # template = loader.get_template('index.html')
    # return HttpResponse(template.render())
    logger = logging.getLogger(__name__)
    path= os.path.join(os.path.dirname(os.path.dirname(__file__)),'kevin_web_app\data\personal_info.json')
    info=json.load(open(path,"r"))
    # logging.warning(info)
    return render(request,"kevin_web_app/index.html",{'info': info})
