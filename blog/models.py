from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=30)
    body = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    time = models.DateTimeField()

    def __str__(self):
        return self.title

class Comment(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    time = models.DateTimeField()
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)

    def __str__(self):
        return self.content
