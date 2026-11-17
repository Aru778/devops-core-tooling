# Unit tests for the main application

from main import add_numbers


def test_add_numbers():
    assert add_numbers(10, 20) == 30


def test_add_zero():
    assert add_numbers(10, 0) == 10


def test_add_negative_numbers():
    assert add_numbers(-5, -5) == -10