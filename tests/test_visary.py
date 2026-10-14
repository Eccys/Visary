import builtins
import json
import symtable
from pathlib import Path


REPO_DIR = Path(__file__).resolve().parent.parent


def test_config_json_is_valid():
    config_path = REPO_DIR / "config.json"
    data = json.loads(config_path.read_text(encoding="utf-8"))
    assert isinstance(data, dict)
    assert "token" in data
    assert "prefix" in data


def test_visary_symtable_has_no_undefined_globals():
    source = (REPO_DIR / "Visary.py").read_text(encoding="utf-8")
    top = symtable.symtable(source, "Visary.py", "exec")
    builtin_names = set(dir(builtins)) | {"__file__", "__name__"}
    module_defined = {
        s.get_name()
        for s in top.get_symbols()
        if s.is_assigned() or s.is_imported() or s.is_namespace()
    }

    undefined = []

    def walk(table):
        for s in table.get_symbols():
            name = s.get_name()
            if s.is_global() and not s.is_assigned() and not s.is_imported():
                if name not in module_defined and name not in builtin_names:
                    undefined.append((table.get_name(), table.get_lineno(), name))
        for child in table.get_children():
            walk(child)

    walk(top)
    assert undefined == [], f"Undefined globals in lexical scopes: {undefined}"


