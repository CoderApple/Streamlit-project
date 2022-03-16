import streamlit as st

sem = 0;

st.markdown("<h1 style='text-align: center; color: red;'>CalcGPA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Semester GPA Calculator of B.Tech(EEE)</h3>", unsafe_allow_html=True)

with st.container():
    name = st.text_input('Full Name')
    if name:
        st.write("Hello! ", name)
        Semester = st.number_input('Semester', min_value = 0, max_value = 8, step = 1)
        sem += Semester
    col1, col2 = st.columns(2);

    if(sem == 1):
        st.write("")
        st.write("")
        st.markdown("<h3 style='text-align: center; '>Enter Marks!</h3>", unsafe_allow_html=True)
        with col1:
            with st.expander("Theory Marks"):
                st.number_input("Programming in C/Applied Chemistry", min_value=0, max_value=100, step=1)

        with col2:
            with st.expander("Practical Marks"):
                st.number_input("Applied Chemistry", min_value=0, max_value=100, step=1)