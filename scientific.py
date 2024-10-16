import streamlit as st
import math

# Title of the application
st.title("Scientific Calculator")

# Dropdown for selecting the operation
operation = st.selectbox("Select Operation:", 
                          ["Addition", "Subtraction", "Multiplication", 
                           "Division", "Square", "Square Root", 
                           "Cosine", "Sine", "Tangent", "Factorial"])

# Input fields for values
value1 = st.number_input("Enter first value:", value=0.0)
# Only show the second input field for binary operations
if operation in ["Addition", "Subtraction", "Multiplication", "Division"]:
    value2 = st.number_input("Enter second value:", value=0.0)
else:
    value2 = None  # No second input for unary operations

# Button to calculate
if st.button("Calculate", key="calculate", use_container_width=True):
    result = None
    if operation == "Addition":
        result = value1 + value2
    elif operation == "Subtraction":
        result = value1 - value2
    elif operation == "Multiplication":
        result = value1 * value2
    elif operation == "Division":
        result = value1 / value2 if value2 != 0 else "Error: Division by Zero"
    elif operation == "Square":
        result = value1 ** 2
    elif operation == "Square Root":
        result = math.sqrt(value1) if value1 >= 0 else "Error: Negative Input"
    elif operation == "Cosine":
        result = math.cos(math.radians(value1))
    elif operation == "Sine":
        result = math.sin(math.radians(value1))
    elif operation == "Tangent":
        result = math.tan(math.radians(value1))
    elif operation == "Factorial":
        if value1 >= 0 and value1 == int(value1):
            result = math.factorial(int(value1))
        else:
            result = "Error: Factorial only defined for non-negative integers."

    st.success(f"Result: {result}")

# Styling buttons
st.markdown("""
<style>
div.stButton > button {
    background-color: #4CAF50;
    color: white;
    font-size: 20px;
    padding: 10px;
    border-radius: 5px;
}
</style>
""", unsafe_allow_html=True)





