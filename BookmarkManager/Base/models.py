from django.db import models
from django.contrib.auth.models import User

class Bookmark(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tittle = models.CharField(null=False, blank=False, max_length=40)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return str(self.title)

