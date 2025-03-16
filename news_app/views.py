import requests
from django.http import JsonResponse
from django.core.serializers import serialize
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import NewsArticle
import logging
from datetime import datetime
from django.db.models import F
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

def getNews():
    all_articles =  []
    for category in categories:
        api_key = "8a5f4db75bef4f7a821b455919c0d677"
        url = f"https://newsapi.org/v2/everything?q={category}&apiKey={api_key}"
        news = requests.get(url)
        if news.status_code == 200:
            articles =  news.json().get("articles", [])

            filtered_articles = [
                {
                    'title': article['title'],
                    'description': article['description'],
                    'url': article['url'],
                    'url_to_image': article['urlToImage'],
                    'published_at': datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ"),
                    'tag': category
                }
                for article in articles
            ]

            all_articles.extend(filtered_articles)
            
    return all_articles

def save_news():
    articles = getNews()
    for article in articles:
        if not NewsArticle.objects.filter(title = article['title']).exists():
             NewsArticle.objects.create(
                title = article.get('title',"No title"),
                description = article.get('description', "No description available"),
                url = article.get('url',""),
                url_to_image = article.get('url_to_image',""),
                published_at = article.get('published_at',""),
                tag = article['tag']
            )


save_news()

#! REMEBER TO DELETE THE CRSF_EXEMPT DECORATOR 
@csrf_exempt
def newsarticlelist(request):
    if request.method == 'GET':
        newsfeed = [
            {   
                'id': article.id,
                'title': article.title,
                'description': article.description,
                'url': article.url,
                'url_to_image': article.url_to_image,
                'published_at': article.published_at,
                'tag': article.tag
            }
            for article in NewsArticle.objects.order_by('?')
        ]

        
        return JsonResponse(newsfeed, safe=False)
    
    if request.method == 'POST':
        data = request.POST
        categories.append(data['tag'])
        news_article = NewsArticle.objects.create(
            title = data['title'],
            description = data['description'],
            url = data['url'],
            url_to_image = data['url_to_image'],
            published_at = data['published_at'],
            tag = data['tag']
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
    

@csrf_exempt
def like_newsarticle(request, pk):
    if request.method == 'PUT':
        try:
            news_article = NewsArticle.objects.get(pk = pk)
            news_article.likes = F('likes') + 1
            news_article.save()
            news_article.refresh_from_db()  # Refresh the object to get the updated value
            return JsonResponse({'likes': news_article.likes}, safe=False)
        except NewsArticle.DoesNotExist:
            return JsonResponse({'error': 'News Article not found'}, status=404)

def dislike_newsarticle(request, pk):
     if request.method == 'PUT':
        try:
            news_article = NewsArticle.objects.get(pk = pk)
            news_article.likes = F('likes') + 1
            news_article.save()
            news_article.refresh_from_db()  # Refresh the object to get the updated value
            return JsonResponse({'likes': news_article.likes}, safe=False)
        except NewsArticle.DoesNotExist:
            return JsonResponse({'error': 'News Article not found'}, status=404)

def tagged_articlelist(request, tag):
    if request.method == 'GET':
        newsfeed = [
            {
                'id': article.id,
                'title': article.title,
                'description': article.description,
                'url': article.url,
                'url_to_image': article.url_to_image,
                'published_at': article.published_at,
                'tag': article.tag
            }
            for article in NewsArticle.objects.filter(tag = tag)
        ]

        return JsonResponse(newsfeed, safe=False)
