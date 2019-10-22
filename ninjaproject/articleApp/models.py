from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
      title = models.CharField(max_length=100)
      slug = models.SlugField()
      body = models.TextField()
      date = models.DateField(auto_now_add=True)
      # author = models.ForeignKey(User,on_delete=models.CASCADE)
      thumb = models.ImageField(default='default.png', blank=True)
      def __str__(self):
        return self.title
      def snippet(self):
        return self.body[:50] + "..."