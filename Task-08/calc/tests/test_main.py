from unittest.mock import patch, MagicMock
from io import StringIO
import sys
import pytest

from src.calculator.main import main # Import the main function directly
from src.calculator.main import history as global_history # Import the global history object

def run_calculator_direct(command_args):
    # Capture stdout and stderr
    old_stdout = sys.stdout
    old_stderr = sys.stderr
    redirected_stdout = StringIO()
    redirected_stderr = StringIO()
    sys.stdout = redirected_stdout
    sys.stderr = old_stderr

    exit_code = 0 # Default to success

    mock_sys_exit = MagicMock(side_effect=SystemExit)

    with patch('sys.exit', new=mock_sys_exit):
        try:
            # Simulate command-line arguments
            with patch('sys.argv', ['main.py'] + command_args):
                main() # Call the main function directly
        except SystemExit:
            # SystemExit is raised by our mock, but we don't need to do anything here
            # The exit code is captured by mock_sys_exit
            pass
        finally:
            sys.stdout = old_stdout # Restore stdout
            sys.stderr = old_stderr # Restore stderr
    
    # Get the exit code from the mock, if sys.exit was called
    print(f"DEBUG: mock_sys_exit.called: {mock_sys_exit.called}", file=sys.stderr)
    if mock_sys_exit.called:
        print(f"DEBUG: mock_sys_exit.call_args: {mock_sys_exit.call_args}", file=sys.stderr)
        exit_code = mock_sys_exit.call_args[0][0]
    
    return redirected_stdout.getvalue(), redirected_stderr.getvalue(), exit_code

# Acceptance tests for calc command (from previous tasks)
def test_add_operation():
    stdout, stderr, exit_code = run_calculator_direct(["calc", "5", "+", "3"])
    assert exit_code == 0
    assert stdout == "8.0\n"
    assert stderr == ""

# ... (other calc tests) ...

# New tests for history command
def test_history_empty():
    global_history.history.clear() # Ensure history is clear for this test
    stdout, stderr, exit_code = run_calculator_direct(["history"])
    assert exit_code == 0
    assert "No operations in history.\n" in stdout
    assert stderr == ""

def test_history_records_operations():
    global_history.history.clear() # Clear history before performing operations for this test
    # Perform some calculations
    run_calculator_direct(["calc", "1", "+", "1"])
    run_calculator_direct(["calc", "2", "*", "2"])
    run_calculator_direct(["calc", "10", "-", "5"])
    
    # Check history
    stdout, stderr, exit_code = run_calculator_direct(["history"])
    assert exit_code == 0
    expected_history_output = """Operation History (most recent first):
10.0 - 5.0 = 5.0
2.0 * 2.0 = 4.0
1.0 + 1.0 = 2.0
"""
    assert stdout == expected_history_output
    assert stderr == ""

def test_history_respects_capacity():
    global_history.history.clear() # Clear history before performing operations for this test
    # Perform more than 5 calculations
    run_calculator_direct(["calc", "1", "+", "1"]) # 1
    run_calculator_direct(["calc", "2", "+", "2"]) # 2
    run_calculator_direct(["calc", "3", "+", "3"]) # 3
    run_calculator_direct(["calc", "4", "+", "4"]) # 4
    run_calculator_direct(["calc", "5", "+", "5"]) # 5
    run_calculator_direct(["calc", "6", "+", "6"]) # 6 (oldest, 1+1, should be removed)
    
    # Check history
    stdout, stderr, exit_code = run_calculator_direct(["history"])
    assert exit_code == 0
    expected_history_output = """Operation History (most recent first):
6.0 + 6.0 = 12.0
5.0 + 5.0 = 10.0
4.0 + 4.0 = 8.0
3.0 + 3.0 = 6.0
2.0 + 2.0 = 4.0
"""
    assert stdout == expected_history_output
    assert stderr == ""
