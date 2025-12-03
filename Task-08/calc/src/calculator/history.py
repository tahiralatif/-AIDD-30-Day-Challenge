from collections import deque
from .operations import Operation

class OperationHistory:
    """
    Manages a fixed-size history of operations performed by the calculator.
    Stores a maximum number of operations, automatically removing the oldest
    when new ones are added beyond capacity.
    """
    def __init__(self, capacity: int = 5):
        """
        Initializes the OperationHistory with a specified capacity.

        Args:
            capacity: The maximum number of operations to store in the history.
        """
        self.capacity = capacity
        self.history = deque(maxlen=capacity)

    def add_operation(self, operation: Operation):
        """
        Adds a new operation to the history.

        If the history is at its maximum capacity, the oldest operation
        will be automatically removed to accommodate the new one.

        Args:
            operation: The Operation object to add.
        """
        self.history.append(operation)

    def get_history(self) -> list[Operation]:
        """
        Retrieves the current list of operations in the history.

        The operations are returned in the order they were added, from oldest
        to newest, up to the history's capacity.

        Returns:
            A list of Operation objects currently in the history.
        """
        return list(self.history)
