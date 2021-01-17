from django.db import models
import uuid
# Create your models here.
class Contacts(models.Model):
    unique_id = models.TextField()
    name = models.TextField()
    relationship = models.TextField()
    mobile = models.TextField()
