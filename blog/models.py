from django.db import models
from taggit.managers import TaggableManager
from django.contrib.syndication.views import Feed

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    create_at = models.DateField()
    tags = TaggableManager()

    def __unicode__(self):
        return self.title



class Blogfeed(Feed):
    title = "Ryan Blog"
    description = "Ryan XCCCXXX"
    link = "/blog/feed"

    def items(self):
        return Post.objects.all().order_by("-create_at")[:2]
    def item_title(self,item):
        return item.title
    def item_description(self,item):
        return item.body
    def item_link(self,item):
        return u'/blog/%d' % item.id

