from django.db import models
#pylint: disable=invalid-str-returned
#pylint doesn't think CharField is str

class Context(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField()

    def __str__(self):
        return self.name

class Actions(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=1024, blank=True, null=True)
    success_criteria = models.TextField(default="")
    prompt = models.TextField(default="")
    created = models.DateTimeField(auto_now_add=True)
    context = models.ForeignKey(Context, on_delete=models.CASCADE, related_name='actions', null=True, blank=True)
    def __str__ (self):
        return self.name
