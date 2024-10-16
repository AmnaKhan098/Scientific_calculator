import streamlit as st
import math

st.title("Scientific Calculator")
st.write("### Perform complex calculations easily!")

# Display input field
display = st.text_input("Enter your expression", "")

# Button layout with Markdown for color styling
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

# Display the result in a text field
st.write("### Result:", display)

# Function buttons in a grid layout
for row in buttons:
    cols = st.columns([1, 1, 1, 1])
    for i, button in enumerate(row):
        if cols[i].button(button):
            if button == "=":
                display = str(calculate(display))
            else:
                display += button

# Scientific function buttons with Markdown
st.write("### Scientific Functions")
with st.container():
    col1, col2, col3 = st.columns(3)
    if col1.button("sin"):
        display = str(math.sin(math.radians(float(display))))
    if col2.button("cos"):
        display = str(math.cos(math.radians(float(display))))
    if col3.button("tan"):
        display = str(math.tan(math.radians(float(display))))
        
    col4, col5, col6 = st.columns(3)
    if col4.button("log"):
        display = str(math.log10(float(display)))
    if col5.button("√"):
        display = str(math.sqrt(float(display)))
    if col6.button("^2"):
        display = str(float(display) ** 2)

# Clear button to reset the calculator
if st.button("Clear"):
    display = ""

