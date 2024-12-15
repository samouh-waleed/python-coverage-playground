import pytest
from src.fully_tested import add, Greeter


def test_add():
    assert add(2, 3) == 5

def test_greeter():
    g = Greeter()
    assert g.greet("World") == "Hello, World!"
