# Data Model: calculator-app

This section details the data structures and entities relevant to the `calculator-app` feature.

## Entities

### Operation

**Description**: Represents a single arithmetic operation performed by the calculator.

**Attributes**:
- `operand1`: (Type: Number) The first operand of the operation.
- `operator`: (Type: String) The arithmetic operator (+, -, *, /).
- `operand2`: (Type: Number) The second operand of the operation.
- `result`: (Type: Number) The outcome of the operation.

## Relationships

### Operation History

**Description**: A collection that stores the most recent `Operation` entities.

**Attributes**:
- `history`: (Type: List of Operation) A list containing up to the last 5 `Operation` records. When a new operation is added and the list is full, the oldest operation is removed.
