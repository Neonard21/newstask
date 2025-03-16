from django.db import models

# Create your models here.
class NewsArticle(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True, null=True)
    url = models.URLField(null=True, blank=True)
    url_to_image = models.URLField(null=True, blank=True, max_length = 500)   
    tag = models.CharField(max_length = 50)
    published_at = models.DateTimeField()
    likes = models.IntegerField(default = 0)
    dislikes = models.IntegerField(default = 0)

    def __str__(self):
        return self.title
    
    
    