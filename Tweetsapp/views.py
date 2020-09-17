from django.shortcuts import render, redirect
from django.conf import settings
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.views import defaults
from django.utils.http import is_safe_url
from .models import Tweet
from .forms import TweetForm
import random

ALLOWED_HOSTS = settings.ALLOWED_HOSTS

# Create your views here.
def home(request):
    context = {}
    return render(request, template_name='pages/home.html', context=context, status=200)


def tweet_detail_view(request, tweet_id, *args, **kwargs):
    data = {
        "id": tweet_id,
        # "image_path":obj.image.url
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "not found"
        status = 404

    return JsonResponse(data, status=status)


def tweet_list_view(request, *args, **kwargs):
    qs = Tweet.objects.all()
    tweets_list = [{"id": x.id, "content": x.content,
                    "likes": random.randint(0, 122)} for x in qs]
    data = {
        "isUser": False,
        "response": tweets_list
    }
    return JsonResponse(data)


def tweet_create_view(request, *args, **kwargs):
    form = TweetForm(request.POST or None)
    next_url = request.POST.get("next") or None
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        if request.is_ajax():
            return JsonResponse(obj.serialize(), status = 201)
        if next_url != None and is_safe_url(next_url, ALLOWED_HOSTS):
            return redirect(next_url)
        form = TweetForm()
    return render(request, 'components/form.html', context={"form": form})
