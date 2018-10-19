from django.db import models


class Task(models.Model):
    text = models.TextField()
    solution = models.TextField()

    def __str__(self):
        return 'Task {id}'.format(id=self.id)
