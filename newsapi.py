import requests
from datetime import datetime

categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']

def getNews():
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

            return filtered_articles
        return []

print(getNews())
