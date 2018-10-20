from django.db import models

from kms.ast import get_ast_tree


class Task(models.Model):
    text = models.TextField()
    solution = models.TextField()

    def __str__(self):
        return 'Task {id}'.format(id=self.id)

    @property
    def ast_tree(self):
        return get_ast_tree(self.solution)
