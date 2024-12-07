from django.db import models

# Create your models here.
import uuid 
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.fields import SlugField
from django.urls import reverse
# from accounts.models import CustomUser
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

# Create your models here.

# Just one simple object for this project, it's the responce to the question
# "What is your favorite season?"

class Response(models.Model):

    CHOICE_LIST = (
        ('Spring', 'Spring'),
        ('Summer', 'Summer'),
        ('Fall', 'Fall'),
        ('Winter', 'Winter'),
    )

    created_by = models.OneToOneField(
        User,
        on_delete = models.CASCADE)
    Question1 = models.TextField(choices=CHOICE_LIST)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.created_by)

