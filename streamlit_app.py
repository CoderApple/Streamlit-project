import streamlit as st

sem = 0;
def calc(sem):
    col1, col2 = st.columns(2);
    if sem == 1:
        with col1:
            with st.expander("Theory Marks"):
                ftfs = st.number_input("Programming in C/Applied Chemistry", min_value=0, max_value=100, step=1)
                stss = st.number_input("Applied Physics-I", min_value=0, max_value=100, step=1)
                ttts = st.number_input("Communication Skills/Indian Constitution/Human Values and Ethics", min_value=0, max_value=100, step=1)
                ftfs = st.number_input("Applied Mathematics-I", min_value=0, max_value=100, step=1)
                ftvs = st.number_input("Manufacturing Process", min_value=0, max_value=100, step=1)
                stxs = st.number_input("Electrical Science/Environmental Studies", min_value=0, max_value=100, step=1)

        with col2:
            with st.expander("Practical Marks"):
                fpfs = st.number_input("Programming in C Lab/Applied Chemistry", min_value=0, max_value=100, step=1)
                spss = st.number_input("Physics-I Lab", min_value=0, max_value=100, step=1)
                tpts = st.number_input("Engineering Graphics-I", min_value=0, max_value=100, step=1)
                fpfs = st.number_input("Electrical Science Lab/Environmental Studies Lab", min_value=0, max_value=100, step=1)

st.markdown("<h1 style='text-align: center; color: red;'>CalcGPA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; '>Semester GPA Calculator of B.Tech(EEE)</h3>", unsafe_allow_html=True)

with st.container():
    name = st.text_input('Full Name')
    if name:
        st.write("Hello! ", name)
        Semester = st.number_input('Semester', min_value = 0, max_value = 8, step = 1)
        sem += Semester
    

    if sem:
        st.write("")
        st.write("")
        st.markdown("<h3 style='text-align: center; '>Enter Marks!</h3>", unsafe_allow_html=True)
        
        calc(sem)