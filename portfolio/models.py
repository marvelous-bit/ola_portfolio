from django.db import models
from django.utils import timezone

# Create your models here.
class Web(models.Model):
    heading = models.CharField(max_length=55, default="I forgot to add heading..", blank=False, null=False)
    body = models.TextField(max_length=999, default="", null=True, blank=True)
    start_date = models.DateField(default=timezone.now, null=False, blank=False)
    slug = models.SlugField()
    end_date = models.DateField(default=timezone.now, null=False, blank=False)
    image = models.ImageField(upload_to='image/')
    urll = models.CharField(max_length=55, default="www. .com", blank=False, null=False)

    image_a = models.ImageField(upload_to="imagea", null=True, blank=True)
    image_b = models.ImageField(upload_to="imagess", null=True, blank=True)
    details = models.TextField(null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.heading}.. start: {self.start_date}, end:{self.end_date}"
class App(models.Model):
    heading = models.CharField(max_length=55, default="I forgot to add heading..", blank=False, null=False)
    urll = models.CharField(max_length=55, default="www. .com", blank=False, null=False)
    slug = models.SlugField()

    body = models.TextField(max_length=999, default="", null=True, blank=True)
    start_date = models.DateField(default=timezone.now, null=False, blank=False)
    end_date = models.DateField(default=timezone.now, null=False, blank=False)
    image = models.ImageField(upload_to="imagemjko", null=True, blank=True)
    details = models.TextField(null=True, blank=True)
    image_a = models.ImageField(upload_to="imagevfrd", null=True, blank=True)
    image_b = models.ImageField(upload_to="imagebhyughn", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.heading}.. start: {self.start_date}, end:{self.end_date}"

class Card(models.Model):
    """
    In timeline: Each achievement is shown in card
    """
    heading = models.CharField(max_length=55, default="I forgot to add heading..", blank=False, null=False)
    body = models.TextField(max_length=999, default="", null=True, blank=True)
    date = models.DateField(default=timezone.now, null=False, blank=False)


    def __str__(self) -> str:
        return f"{self.heading}.. on {self.date}"

class testimony(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images/')
    created = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=100)
    class Meta:
        ordering = ['-created']


    def __str__(self):
        return self.name + '' + self.message[:30]
class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    subject= models.CharField(max_length=30)

    email=models.EmailField()
    created = models.DateTimeField(auto_now_add=True)
    messagess = models.CharField(max_length=100)
    class Meta:
        ordering = ['-created']

    def __str__(self):
       return self.name + '' + self.messagess + '' + self.subject


