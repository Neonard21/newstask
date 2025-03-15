from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import NewsArticle, NewsTag
from django.db.models import F
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
#! REMEBER TO DELETE THE CRSF_EXEMPT DECORATOR 
@csrf_exempt
def newsarticlelist(request):
    if request.method == 'GET':
        newsfeed = NewsArticle.objects.all()
        json_data = serialize('json', newsfeed)
        return JsonResponse(json_data, safe=False)
    
    if request.method == 'POST':
        data = request.POST
        news_article = NewsArticle.objects.create(
            title = data['title'],
            text = data['text'],
            news_tag = NewsTag.objects.get(tag = data['news_tag'])
        )
        news_article.save()
        return JsonResponse({'message': 'News Article created successfully'})

def newsarticledetail(request, pk):
    if request.method == 'GET':
        news_article = NewsArticle.objects.get(pk = pk)
        json_data = serialize('json', [news_article])
        return JsonResponse(json_data, safe=False)
    
    if request.method == 'DELETE':
        news_article = NewsArticle.objects.get(pk = pk)
        news_article.delete()
        return JsonResponse({'message': 'News Article deleted successfully'})  
    

def like_newsarticle(request, pk):
    if request.method == 'PUT':
        news_article = NewsArticle.objects.get(pk = pk)
        news_article.likes = F('likes') + 1
        news_article.save()
        json_data = serialize('json', [news_article.likes])
        return JsonResponse(json_data, safe=False)

def dislike_newsarticle(request, pk):
    if request.method == 'PUT':
        news_article = NewsArticle.objects.get(pk = pk)
        news_article.dislikes = F('dislikes') + 1
        news_article.save()
        json_data = serialize('json', [news_article.dislikes])
        return JsonResponse(json_data, safe=False)

def tagged_articlelist(request, tag):
    news_tags = NewsArticle.objects.filter(news_tag__tag = tag)
    json_data = serialize('json', news_tags)
    return JsonResponse(json_data, safe=False)
