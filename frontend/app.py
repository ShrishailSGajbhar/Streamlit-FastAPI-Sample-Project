import streamlit as st 
import json
import requests

st.title("Simple Calculator App :computer:")

# Taking the user input
option = st.selectbox(label="Select operation: ", 
                      options=("Addition", "Subtraction", "Multiplication", "Division"))

st.write("")
st.write("Select the numbers from the slider below: :point_down:")
num1 = st.slider("number1", 0, 100, 20)
num2 = st.slider("number2", 0, 130, 10)

inputs = {"operation": option, "number1": num1, "number2": num2}

# When user clicks on the button it will make an API call and fetch the result
res = requests.post(url="http://127.0.0.1:8000/calculate",
                    data=json.dumps(inputs))

st.subheader(f"Response from API :rocket:: {res.text}" )

