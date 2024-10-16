import streamlit as st
import math

st.title("Scientific Calculator")
st.write("### Perform complex calculations easily!")

# Layout with two columns
col1, col2 = st.columns(2)

# Display
display = st.text_input("Enter your expression", "")

# Button grid
if st.button("Clear"):
    display = ""

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+'],
]

# Creating function for calculations
def calculate(expression):
    try:
        return eval(expression)
    except:
        return "Error"

# Loop to create buttons
for row in buttons:
    with col1:
        for button in row:
            if st.button(button, key=button, use_container_width=True, style="background-color: #4CAF50; color: white; font-size: 20px"):
                if button == "=":
                    display = str(calculate(display))
                else:
                    display += button

# Scientific functions
with col2:
    st.write("### Functions")
    if st.button("sin"):
        display = str(math.sin(math.radians(float(display))))
    if st.button("cos"):
        display = str(math.cos(math.radians(float(display))))
    if st.button("tan"):
        display = str(math.tan(math.radians(float(display))))
    if st.button("log"):
        display = str(math.log10(float(display)))
    if st.button("√"):
        display = str(math.sqrt(float(display)))
    if st.button("^2"):
        display = str(float(display) ** 2)

# Display the result
st.write("### Result:", display)
