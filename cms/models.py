from django.db import models

from kms.ast import get_ast_tree, get_ast_tree_as_json


class Task(models.Model):
    text = models.TextField()
    solution = models.TextField()

    def __str__(self):
        return 'Task {id}'.format(id=self.id)

    @property
    def ast_tree(self):
        tree = get_ast_tree(self.solution)
        return tree
    
    @property
    def ast_json(self):
        return get_ast_tree_as_json(self.ast_tree)
