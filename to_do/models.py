from django.db import models
from django.contrib.auth.models import User

class Tasks(models.Model):
    srno = models.AutoField(primary_key=True, auto_created=True)
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # models.CASCADE means if the user is deleted, all their tasks will also be deleted.

