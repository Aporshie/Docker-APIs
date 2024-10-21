"""This is my first app, hurray!"""


import streamlit as st
import pandas as pd

st.title("Hello World")
y = st.slider('y')
st.text_input("Your name", key="name")

# You can access the value at any point with:
st.session_state.name

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

