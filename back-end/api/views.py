from django.shortcuts import render
from .models import Mail
import io
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import MailSerializer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(requests):
    try:
        if(requests.method=='POST'):
            json_data=requests.body
            streams=io.BytesIO(json_data)
            pythondata=JSONParser().parse(streams)
            serializer=MailSerializer(data=pythondata)
            if serializer.is_valid():
                serializer.save()
                res={'msg':'Data inserted'}
                json_data=JSONRenderer().render(res)
                return HttpResponse(json_data,content_type='application/json')
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application/json')
    except:
         res={'msg':'Duplicate'}
         json_data=JSONRenderer().render(res)
         return HttpResponse(json_data,content_type='application/json')
    
    if(requests.method=="GET"):
        data=Mail.objects.all()
        serializer=MailSerializer(data,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

