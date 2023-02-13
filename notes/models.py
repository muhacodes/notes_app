from django.db import models

class NoteModel(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    def __str__(self):
        return self.title