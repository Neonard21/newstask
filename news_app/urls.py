from django.urls import path
from .views import newsarticlelist, newsarticledetail, tagged_articlelist, like_newsarticle, dislike_newsarticle


app_name = 'news_app'

urlpatterns = [
    path("", newsarticlelist, name = "news_article_list"),
    path("detail/<int:pk>/", newsarticledetail, name = "news_article_detail"),
    path("likes/<int:pk>/", newsarticledetail, name = "news_article_like"),
    path("dislikes/<int:pk>/", newsarticledetail, name = "news_article_dislike"),
    path("tag/<tag>/", tagged_articlelist, name = "news_tagged_list"),
]