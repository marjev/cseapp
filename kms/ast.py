import ast

def get_ast_tree(code):
    tree = ast.parse(code)
    return ast.dump(tree)
