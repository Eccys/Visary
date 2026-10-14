import ast
import builtins
import json
from pathlib import Path


REPO_DIR = Path(__file__).resolve().parent.parent


def test_config_json_is_valid():
    config_path = REPO_DIR / "config.json"
    data = json.loads(config_path.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    assert "token" in data
    assert "prefix" in data


def test_visary_ast_has_no_undefined_names():
    source = (REPO_DIR / "Visary.py").read_text(encoding="utf-8")
    tree = ast.parse(source)

    defined = set(dir(builtins)) | {"__file__"}
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
            defined.add(node.name)
        elif isinstance(node, ast.Import):
            for alias in node.names:
                defined.add((alias.asname or alias.name).split(".")[0])
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                defined.add(alias.asname or alias.name)
        elif isinstance(node, ast.Name) and isinstance(node.ctx, ast.Store):
            defined.add(node.id)
        elif isinstance(node, ast.arg):
            defined.add(node.arg)
        elif isinstance(node, ast.ExceptHandler) and node.name:
            defined.add(node.name)

    undefined = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Name) and isinstance(node.ctx, ast.Load):
            if node.id not in defined:
                undefined.append((node.lineno, node.id))
    assert undefined == [], f"Undefined names: {undefined}"

