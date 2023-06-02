from django.shortcuts import render
import logging
import json,os
from django.http import JsonResponse
from django.views import View
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

class IndexView(View):
# Create your views here.
    def __init__(self):
        path= os.path.join(os.path.dirname(os.path.dirname(__file__)),'kevin_web_app/data/personal_info.json')
        self.info=json.load(open(path,"r"))
        self.logger = logging.getLogger(__name__)
    def get(self,request):
        # self.logger.warning(self.info)
        return render(request,"kevin_web_app/index.html",{'info': self.info})
    
class View_API(APIView):
# Create your views here.
    def __init__(self):
        path= os.path.join(os.path.dirname(os.path.dirname(__file__)),'kevin_web_app/data/personasl_info.json')
        self.info=json.load(open(path,"r"))
        self.logger = logging.getLogger(__name__)
    def get(self,request):
        sub_list=self.request.GET.get('sub_list')
        self.logger.warning(sub_list)
        return Response(self.info[sub_list],status=status.HTTP_200_OK)
        # return render(request,"kevin_web_app/index.html",{'info': self.info})
