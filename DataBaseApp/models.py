from django.db import models

class Team(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=30)
    description = models.TextField()
