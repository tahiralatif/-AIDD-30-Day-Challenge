# Quickstart Guide: calculator-app

This guide provides instructions on how to quickly set up and run the `calculator-app`.

## Prerequisites

- Python 3.12+
- `uv` package manager

## Setup

1.  **Clone the repository**:
    ```bash
    git clone [repository_url]
    cd calculator/calc
    ```

2.  **Install dependencies**:
    ```bash
    uv pip install -r requirements.txt
    ```
    (Note: `requirements.txt` will be generated during the implementation phase.)

## Usage

The calculator application has two interfaces: a command-line interface (CLI) and a web-based user interface (UI).

### Web-based UI (Streamlit)

To run the web-based UI, use the following command:

```bash
uv run streamlit run src/calculator/ui.py
```

This will open a new tab in your web browser with the calculator interface.

### Command-Line Interface (CLI)

The calculator is a command-line application that supports subcommands.

### Perform a calculation

To perform a basic arithmetic operation, use the `calc` subcommand followed by the two operands and the operator:

```bash
calculator calc <operand1> <operator> <operand2>
```

**Examples**:

```bash
calculator calc 5 + 3
# Expected output: 8.0

calculator calc 10 - 4
# Expected output: 6.0

calculator calc 6 "*" 7
# Expected output: 42.0

calculator calc 20 / 5
# Expected output: 4.0
```

### View Operation History

To view the history of performed operations, use the `history` subcommand:

```bash
calculator history
```

**Examples**:

```bash
# After performing some calculations
calculator history
# Expected output (example):
# Operation History (most recent first):
# 6.0 + 6.0 = 12.0
# 5.0 + 5.0 = 10.0
# 4.0 + 4.0 = 8.0
```

## Error Handling

If invalid input is provided, the application will display an informative error message and exit.

**Example of invalid input**:

```bash
calculator 5 x 3
# Expected output: Error: Invalid operator. Supported operators are +, -, *, /.
```
