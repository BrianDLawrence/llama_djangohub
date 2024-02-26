from django.db import models
#pylint: disable=invalid-str-returned
#pylint doesn't think CharField is str

class Actions(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=1024, blank=True, null=True)
    success_criteria = models.TextField(default="")
    prompt = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
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
