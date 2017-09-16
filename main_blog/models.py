
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericRelation
from like_app.models import Like

# https://www.youtube.com/watch?v=fvcXyEUHh2c&list=PLrCZzMib1e9pg7ZLIOhmGSlmkMf8yEOLZ&index=6&t=4896s

"""
class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)

    item_type = models.ForeignKey(ContentType)
    item_id = models.PositiveIntegerField()
    item = GenericForeignKey("item_type", "item_id")
"""

class Article(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    article_title = models.CharField(max_length=120)
    article_text = models.TextField()
    article_rating = GenericRelation(Like, related_query_name="likes") # models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="liked")
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article_title

    def get_absolute_url(self):
        # return "/{}".format(self.id)
        from django.core.urlresolvers import reverse
        return reverse("main_blog:detail", args=[str(self.id)])

    class Meta:
        ordering = ("-pub_date",)

class Comment(models.Model):

    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=600)
    pub_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_text