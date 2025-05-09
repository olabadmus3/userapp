from django.db import models
from django.contrib.auth.models import User
# Create your models here.


GENDER_CHOICES=(
    ('M','Male'),
    ('F','Female')
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fullname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15,null=True,blank=True)
    gender = models.CharField(max_length=6,choices=GENDER_CHOICES)
    image = models.ImageField(upload_to='profile',null=True,blank=True,default="https://www.silcharmunicipality.in/wp-content/uploads/2021/02/male-face.jpg")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.fullname


