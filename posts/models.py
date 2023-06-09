from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               related_name='Owner',
                               on_delete=models.CASCADE)
    image = models.ImageField('Image',
                              upload_to='post/')
    posted_time = models.DateTimeField('Post_posted_time', auto_now_add=True)
    caption = models.CharField('Caption', max_length=50, blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                   related_name="Post_Likes",
                                   blank=True,
                                   symmetrical=False)


    def __str__(self):
        return "{}'s post({})".format(self.author, self.pk)


    def likes_count(self):
        if self.likes.count():
            return self.likes.count()
        return 0