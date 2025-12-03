"""
This module defines the core arithmetic operations for the calculator
and related data structures and exceptions.
"""
from dataclasses import dataclass

@dataclass
class Operation:
    operand1: float
    operator: str
    operand2: float
    result: float

class DivisionByZeroError(Exception):
    """Custom exception for division by zero."""
    pass

def add(a: float, b: float) -> float:
    """Adds two numbers and returns the sum."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Subtracts the second number from the first and returns the difference."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Multiplies two numbers and returns the product."""
    return a * b

def divide(a: float, b: float) -> float:
    """
    Divides the first number by the second and returns the quotient.

    Raises:
        DivisionByZeroError: If the second operand (divisor) is zero.
    """
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return a / b
