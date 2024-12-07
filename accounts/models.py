from django.db import models
from crispy_forms.helper import FormHelper

# Create your models here.
import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    
    def __str__(self):
        return self.email
    
    # class Meta:
    #     db_table = 'auth_user'
    #     swappable = 'AUTH_USER_MODEL'

# User ID needs to be UUID
# class CustomUser(AbstractUser):
#     id = models.UUIDField(primary_key=True,
#                           default=uuid.uuid4,
#                           editable=False)

    def __str__(self):
        return self.email
