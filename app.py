import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title and description
st.title("Basic Streamlit App")
st.write("This is a simple Streamlit app deployed from GitHub.")

# Input and output
name = st.text_input("Enter your name:")
if name:
    st.write(f"Hello, {name}! Welcome to the app.")

data = pd.DataFrame({
    'Category': ['A', 'B', 'C'],
    'Values': [10, 20, 30]
})

st.write("Bar Chart Example:")
fig, ax = plt.subplots()
ax.bar(data['Category'], data['Values'])
st.pyplot(fig)
