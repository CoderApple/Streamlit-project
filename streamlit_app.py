import streamlit as st

st.title("CalcGPA")
st.header("Semester GPA Calculator for the BTech of IPU")

name = st.text_input('Full Name')
if(len(name) != 0):
    st.write("Hello! ", name)