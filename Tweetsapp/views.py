from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from  django.views import defaults
from .models import Tweet
import random


# Create your views here.
def home(request):
    context={}
    return render(request,template_name='pages/home.html',context=context,status=200)

def tweet_detail_view(request, tweet_id,*args,**kwargs):
    data = {
        "id":tweet_id,
        #"image_path":obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "not found"
        status = 404
    
    return JsonResponse(data, status = status)

def tweet_list_view (request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id":x.id,"content":x.content, "like":random.randint(1,100)} for x in qs]
    data = {
        "isUser":False,
        "response": tweets_list
    }
    return JsonResponse(data)