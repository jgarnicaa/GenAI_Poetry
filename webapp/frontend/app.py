import streamlit as st
import requests

st.title("Poetry Generator 🎭")
st.write("Generate poems in English and Spanish using AI!")

prompt=st.text_input("Enter a prompt for your poem: ")

if st.button("Generate Poem"):
    response=requests.post("http://backend:8000/generate/", json={"prompt": prompt})
    if response.status_code==200:
        st.write(response.json()["poem"])
    else:
        st.write("Error generating poem. Try again later!")