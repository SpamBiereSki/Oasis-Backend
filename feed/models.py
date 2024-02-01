from django.db import models
from django.utils.timezone import now

class Post(models.Model):
    title = models.CharField(max_length=1000)
    post_content = models.CharField(max_length=2000)
    pub_date = models.DateTimeField(default=now, editable=False)

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        ordering = ['pub_date']


class Comment(models.Model):
    comment_content = models.CharField(max_length=1000)
    related_post = models.ForeignKey(Post, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(default=now, editable=False)
    
    def __str__(self) -> str:
        return self.comment_content