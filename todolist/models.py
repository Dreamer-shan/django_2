from django.db import models

class Todo(models.Model):
    things = models.CharField(max_length=50)
    done = models.BooleanField(default=False)
    
