from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    prn = models.CharField(max_length=15, blank=True)
    email = models.EmailField(max_length=200, blank=True)
    avatar = models.ImageField(default = 'avatar.png', upload_to='avatars/')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.prn}-{self.created.strftime('%d-%m-%Y')}"