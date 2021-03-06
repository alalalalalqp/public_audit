from django.db import models
from django.conf import settings

AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')

# Create your models here.

class AuditRequest(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, null=True)
    name = models.CharField(max_length=200, default=" ")
    storage_file_id = models.IntegerField()
    client_message = models.TextField(null=True)
    server_message = models.TextField(null=True)
    result = models.CharField(default="Auditing...",max_length=200)
