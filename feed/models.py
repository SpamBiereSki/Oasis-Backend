from django.db import models
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length=1000)
    content = models.CharField(max_length=2000)
    created = models.DateTimeField(default=now, editable=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['created']


class Comment(models.Model):
    content = models.CharField(max_length=1000)
    idpost = models.ForeignKey(Post, on_delete=models.CASCADE)
    created = models.DateTimeField(default=now, editable=False)
    replyto = models.ForeignKey("self", default=None, blank=True, null=True, on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.content

    class Meta:
        ordering = ["created"]