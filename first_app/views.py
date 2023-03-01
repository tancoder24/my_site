from django.shortcuts import render
from django.http.response import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse

# Create your views here.

article = {
    'sports': "sports view",
    'temp': "temp news",
    "politics": "politics news",
    "national": "India",
    "International": "World",
    "Global": "Earth"
}

def news_view(request, topic):
    try:
        return HttpResponse(article[topic])
    except:
        raise Http404("Request not found")
 
def add_view(request, num1, num2):
    return HttpResponse(f"{num1+num2}")

def num_page_view(request, num_page):
    topic_list = list(article.keys())
    topic = topic_list[num_page]

    return HttpResponseRedirect(reverse('topic-page', args=[topic]))