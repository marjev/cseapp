import ast

from astexport.export import export_json


def get_ast_tree(code):
    return ast.parse(code)


def get_ast_tree_as_json(tree):
    return export_json(tree)
