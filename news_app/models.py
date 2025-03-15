from django.db import models

# Create your models here.
class NewsTag(models.Model):
    tag = models.CharField(max_length = 50)    

    def __str__(self):
        return self.tag
    
class NewsArticle(models.Model):
    title = models.CharField(max_length = 200)
    text = models.TextField()
    pictures = models.ImageField(upload_to="pixs")
    news_tag = models.ForeignKey(NewsTag, on_delete=models.CASCADE)
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)

    def __str__(self):
        return self.title
    
    
    