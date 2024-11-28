from django.db import models

# Create your models here.

from django.db import models

class MyProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    date = models.DateField()
    image = models.ImageField(upload_to='projects/')

    def __str__(self):
        return self.title

class GuestBook(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.date.strftime("%Y-%m-%d %H:%M:%S")}'