from src.calculator.history import OperationHistory
from src.calculator.operations import Operation

def test_operation_history_add_and_get():
    history = OperationHistory(capacity=2)
    op1 = Operation(1, "+", 2, 3)
    op2 = Operation(3, "-", 1, 2)
    history.add_operation(op1)
    history.add_operation(op2)
    assert history.get_history() == [op1, op2]

def test_operation_history_capacity_limit():
    history = OperationHistory(capacity=2)
    op1 = Operation(1, "+", 2, 3)
    op2 = Operation(3, "-", 1, 2)
    op3 = Operation(5, "*", 2, 10)
    history.add_operation(op1)
    history.add_operation(op2)
    history.add_operation(op3)
    assert history.get_history() == [op2, op3]
