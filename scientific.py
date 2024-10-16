import streamlit as st
import math

# Title of the application
st.title("Scientific Calculator")

# Dropdown for selecting the operation
operation = st.selectbox("Select Operation:", 
                          ["Addition", "Subtraction", "Multiplication", 
                           "Division", "Square", "Square Root", 
                           "Cosine", "Sine", "Tangent", "Algorithm"])

# Input fields for values
value1 = st.number_input("Enter first value:", value=0.0)
value2 = st.number_input("Enter second value (only for binary operations):", value=0.0)

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
    elif operation == "Algorithm":
        # Placeholder for algorithmic calculation
        result = "Algorithm applied (functionality to be defined)."

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




