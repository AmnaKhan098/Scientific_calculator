import streamlit as st
import math

st.title("Interactive Scientific Calculator")
st.write("Choose your desired operation, input values, and select an algorithm to perform calculations.")

# Dropdown for selecting an operation
operation = st.selectbox("Select an Operation:", ("Addition", "Subtraction", "Multiplication", "Division", "Power", "Square Root"))

# Dropdown for selecting an algorithm type (simple demonstration for different choices)
algorithm = st.selectbox("Select Algorithm:", ("Standard Calculation", "Algorithm X", "Algorithm Y"))

# Inputs for numbers based on the operation
if operation in ["Addition", "Subtraction", "Multiplication", "Division", "Power"]:
    num1 = st.number_input("Enter First Value:", value=0.0)
    num2 = st.number_input("Enter Second Value:", value=0.0)
else:  # Square root only requires one input
    num1 = st.number_input("Enter Value:", value=0.0)

# Perform calculation on button click
if st.button("Calculate"):
    if algorithm == "Standard Calculation":
        if operation == "Addition":
            result = num1 + num2
        elif operation == "Subtraction":
            result = num1 - num2
        elif operation == "Multiplication":
            result = num1 * num2
        elif operation == "Division":
            result = num1 / num2 if num2 != 0 else "Undefined"
        elif operation == "Power":
            result = math.pow(num1, num2)
        elif operation == "Square Root":
            result = math.sqrt(num1) if num1 >= 0 else "Complex Number"
    elif algorithm == "Algorithm X":
        result = f"Algorithm X result for {operation}"
    else:
        result = f"Algorithm Y result for {operation}"

    st.write("### Result:", result)

# Custom styling
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        font-size: 20px;
        width: 100%;
        height: 50px;
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)



