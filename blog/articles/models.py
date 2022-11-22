from django.db import models

# Create your models here.


class Topic(models.Model):
    topic_name = models.CharField(max_length = 256)

    def __str__(self):
        return self.topic_name

class Article(models.Model):

    title = models.CharField(max_length =256)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE, related_name='articles')
    articleText = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
