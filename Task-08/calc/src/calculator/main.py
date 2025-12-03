import argparse
import sys
from .operations import add, subtract, multiply, divide, DivisionByZeroError, Operation
from .history import OperationHistory

history = OperationHistory() # Initialize history globally

def calculate_command(args: argparse.Namespace):
    """
    Executes a calculation based on the provided arguments and stores it in history.

    Args:
        args: An object containing operand1 (float), operator (str), and operand2 (float).
    """
    result = None
    try:
        if args.operator == "+":
            result = add(args.operand1, args.operand2)
        elif args.operator == "-":
            result = subtract(args.operand1, args.operand2)
        elif args.operator == "*":
            result = multiply(args.operand1, args.operand2)
        elif args.operator == "/":
            result = divide(args.operand1, args.operand2)
        else:
            print(f"Error: Invalid operator '{args.operator}'. Supported operators are +, -, *, /.", file=sys.stderr)
            sys.exit(1)
        
        op = Operation(args.operand1, args.operator, args.operand2, result)
        history.add_operation(op)

        print(result)
    except DivisionByZeroError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

def history_command(args: argparse.Namespace):
    """
    Displays the history of performed operations.

    Args:
        args: An object (typically empty for this command).
    """
    if not history.get_history():
        print("No operations in history.\n", file=sys.stdout) # Changed to sys.stdout
        return
    
    print("Operation History (most recent first):", file=sys.stdout) # Changed to sys.stdout
    # Print in reverse order to show most recent first
    for op in reversed(history.get_history()):
        print(f"{op.operand1} {op.operator} {op.operand2} = {op.result}", file=sys.stdout) # Changed to sys.stdout


def main():
    """
    Main function to parse command-line arguments and execute the appropriate calculator command.
    """
    parser = argparse.ArgumentParser(description="A simple CLI calculator.")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Calculate command
    calculate_parser = subparsers.add_parser("calc", help="Perform a calculation")
    calculate_parser.add_argument("operand1", type=float, help="The first operand")
    calculate_parser.add_argument("operator", type=str, help="The operator (+, -, *, /)")
    calculate_parser.add_argument("operand2", type=float, help="The second operand")
    calculate_parser.set_defaults(func=calculate_command)

    # History command
    history_parser = subparsers.add_parser("history", help="Show operation history")
    history_parser.set_defaults(func=history_command)

    args: argparse.Namespace = parser.parse_args()

    if hasattr(args, "func"):
        args.func(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
