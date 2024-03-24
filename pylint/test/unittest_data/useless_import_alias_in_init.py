
"""
Unit tests for pylint.
Testing the 'import x as x' use case in __init__.py for explicit re-export.
"""

from useless_import_alias_module import Class1 as Class1, func1 as func1

def test_imports():
    assert Class1
    assert func1
