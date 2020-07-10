from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
        # if a user is deleted then it deletes their posts (.CASADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    # tells it to print our string form of the title when queried: 
    # <QuerySet [<Post: Blog 1>]> instead of <Post: Post object (1)>]>
    def __str__(self):
        return self.title

    # will send the user to the post detail page after creating a post 
    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
