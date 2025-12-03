import streamlit as st
from .operations import add, subtract, multiply, divide, DivisionByZeroError, Operation
from .history import OperationHistory

# Initialize session state for history if it doesn't exist
if 'history' not in st.session_state:
    st.session_state['history'] = OperationHistory(capacity=10) # Larger capacity for UI

def main():
    """
    The main function that defines the Streamlit UI and logic.
    """
    st.title("Calculator")

    # --- Calculation UI ---
    col1, col2, col3 = st.columns(3)
    with col1:
        operand1 = st.number_input("Operand 1", value=0.0, format="%.2f")
    with col2:
        operator = st.selectbox("Operator", ("+", "-", "*", "/"))
    with col3:
        operand2 = st.number_input("Operand 2", value=0.0, format="%.2f")

    if st.button("Calculate"):
        result = None
        try:
            if operator == "+":
                result = add(operand1, operand2)
            elif operator == "-":
                result = subtract(operand1, operand2)
            elif operator == "*":
                result = multiply(operand1, operand2)
            elif operator == "/":
                result = divide(operand1, operand2)

            # Display result
            st.success(f"Result: {result}")

            # Create and store the operation in history
            op = Operation(operand1, operator, operand2, result)
            st.session_state.history.add_operation(op)

        except DivisionByZeroError as e:
            st.error(f"Error: {e}")
        except Exception as e:
            st.error(f"An unexpected error occurred: {e}")

    # --- History Display ---
    st.header("Operation History")
    history_list = st.session_state.history.get_history()

    if not history_list:
        st.info("No operations have been performed yet.")
    else:
        # Display history in reverse order (most recent first)
        for op in reversed(history_list):
            st.text(f"{op.operand1} {op.operator} {op.operand2} = {op.result}")

if __name__ == "__main__":
    main()
