from django.db import models
from django.contrib.auth.models import User

class Certificate(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class VerificationToken(models.Model):
    certificate = models.ForeignKey(Certificate, on_delete=models.CASCADE)
    token = models.CharField(max_length=100)

    def __str__(self):
        return self.token
