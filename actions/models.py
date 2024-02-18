from django.db import models

# Create your models here.

class Actions(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024, blank=True, null=True)
    prompt = models.TextField(default="")
    def __str__ (self):
        return self.name

class Prompts(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
    action = models.ForeignKey(
        Actions,
        on_delete=models.CASCADE,
        related_name='prompts',
    )
    def __str__ (self):
        return self.name
