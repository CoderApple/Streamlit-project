import streamlit as st

st.title("CalcGPA")
st.header("Semester GPA Calculator for the BTech of IPU")

name = st.text_input('Full Name')
if(len(name) != 0):
    st.write("Hello! ", name)
    Semester = st.number_input('Semester', min_value = 0, max_value = 8, step = 1)

col1, col2 = st.columns(2);

if(Semester == 1):
    st.header("Enter your Marks!")
    with col1:
        st.expander("Theory Marks")

