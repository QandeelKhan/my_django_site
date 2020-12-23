from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateField(blank=True, null=True)



    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # create a string representation,rather then object form.good practice too.

    def __str__(self):
        # return f"({self.title} by {self.author})"
        return self.title
    