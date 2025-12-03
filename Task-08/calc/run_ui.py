"""
This script is a simple entry point to run the Streamlit UI.
It exists to solve Python path issues when using 'streamlit run' with
applications that have a 'src' layout.
"""
from src.calculator.ui import main

if __name__ == "__main__":
    main()
