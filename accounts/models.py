from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from imagekit.models import ProcessedImageField
from imagekit.processors import ResizeToFill


# Create your models here.
class User(AbstractUser):
    followings = models.ManyToManyField('self', symmetrical=False, related_name='followers')
    profile_image = ProcessedImageField(upload_to='image/profile_image',
                                           processors=[ResizeToFill(300, 300)],
                                           format='JPEG',
                                           options={'quality': 60},
                                           blank=True)

# class ProfileImage(models.Model):
#     user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
#     profile_image = ProcessedImageField(upload_to='profile_image/',
#                                            processors=[ResizeToFill(300, 300)],
#                                            format='JPEG',
#                                            options={'quality': 200})


