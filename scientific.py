import streamlit as st
import math

# Set up the interface
st.title("Scientific Calculator")
st.write("Select an operation and enter values to perform a calculation.")

# Dropdown for operations
operation = st.selectbox("Choose an operation", 
                         ("Addition", "Subtraction", "Multiplication", "Division", 
                          "Square Root", "Power", "Sine", "Cosine", "Tangent"))

# Input fields
num1 = st.number_input("Enter first value", step=0.1, format="%.2f")
num2 = None  # Only used for two-operand operations

if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
    num2 = st.number_input("Enter second value", step=0.1, format="%.2f")

# Calculate button
if st.button("Calculate"):
    try:
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error: Division by zero"
        elif operation == "Square Root":
            result = math.sqrt(num1)
        elif operation == "Power":
            result = math.pow(num1, num2)
        elif operation == "Sine":
            result = math.sin(math.radians(num1))
        elif operation == "Cosine":
            result = math.cos(math.radians(num1))
        elif operation == "Tangent":
            result = math.tan(math.radians(num1))
        
        st.success(f"Result: {result}")
        
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")


