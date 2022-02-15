from django.db import models

# Create your models here.

class Post(models.Model):
     title = models.CharField(max_length=50)
     content = models.CharField(max_length=500)
     created_at =models.DateTimeField(auto_now_add=True)

     def __str__(self):
         return str(self.id) + " - " + self.title

class Task(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " - " + self.title

# Create your models here.
class Image(models.Model):
    code = models.CharField(max_length=20)
    benefit = models.CharField(max_length=1000)
    explanation = models.CharField(max_length=2000)
    image = models.ImageField(upload_to='images/', null=True) #追加
    store = models.CharField(max_length=1000)
    start = models.DateField()
    deadline = models.DateField()
    status = models.BooleanField()