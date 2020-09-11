from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from  django.views import defaults
from .models import Tweet


# Create your views here.
def home(request):
    context={
        'x':123,
        'y':'Not True',
        'z':True}
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

