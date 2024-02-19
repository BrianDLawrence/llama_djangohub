"""
Action and Prompt model creation
"""
from django.db import models
#pylint: disable=invalid-str-returned
#pylint doesn't think CharField is str

class Actions(models.Model):
    """ Actions holding the name + description and prompt of LLM actions"""
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024, blank=True, null=True)
    prompt = models.TextField(default="")
    def __str__ (self):
        return self.name

class Prompts(models.Model):
    """ Prompts for LLM """
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024)
    action = models.ForeignKey(
        Actions,
        on_delete=models.CASCADE,
        related_name='prompts',
    )
    def __str__ (self):
        return self.name
