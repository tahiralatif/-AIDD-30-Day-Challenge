from src.calculator.operations import add, subtract, multiply, divide, DivisionByZeroError
import pytest

def test_add_two_numbers():
    assert add(1, 2) == 3

def test_subtract_two_numbers():
    assert subtract(5, 2) == 3

def test_multiply_two_numbers():
    assert multiply(2, 3) == 6

def test_divide_two_numbers():
    assert divide(6, 3) == 2

def test_divide_by_zero():
    with pytest.raises(DivisionByZeroError, match="Cannot divide by zero."):
        divide(1, 0)
