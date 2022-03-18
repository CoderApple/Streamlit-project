import streamlit as st
import time

st.set_page_config( page_title = "CalcGPA", page_icon = None)


def grades(marks):
    if marks >= 90:
        grade = 10
    elif marks >= 75:
        grade = 9
    elif marks >= 65:
        grade = 8
    elif marks >= 55:
        grade = 7
    elif marks >= 50:
        grade = 6
    elif marks >= 45:
        grade = 5
    elif marks >= 40:
        grade = 4
    else:
        grade = 0
    
    return grade



def calc(sem):
    subjects = {}
    labs = {}
    GPA = 0
    flag = 0 
    credits = 0
    col1, col2 = st.columns(2)

    if sem == 1 :
        subjects = { 'App. Maths-I' : 4, 'App. Physics-I' : 3, 'Manufacturing Processes' : 4, 'Electrical Science' : 3, 'Communication Skills' : 3, 'App. Chemistry' : 3 }
        labs = { 'App. Physics Lab-I' : 1, 'Elecrical Science Lab' : 1, 'Engg. Graphics Lab' : 2, 'App. Chemistry Lab' : 1 }
        credits = 25

    elif sem == 2:
        subjects = { 'App. Maths-II' : 4, 'App. Physics-II' : 3, 'Electronic Devices' : 3, 'Intro To Programming' : 3, 'Engineering Mechanics' : 3, 'Communication Skills' : 3, 'Environmental Studies' : 3 }
        labs = { 'App. Physics Lab-II' : 1, 'Programming Lab' : 1, 'Electronics Lab' : 1, 'Engineering Mechanics Lab' : 1, 'EVS Lab' : 1 }
        credits = 27

    elif sem == 3:
        subjects = { 'App. Maths-III' : 4, 'Foundation of CS' : 4, 'Switching Theory & Logic Design' : 4, 'Circuits & Systems' : 4, 'Data Structures' : 4, 'Computer Graphics & Multimedia' : 4, }
        labs = { 'STLD Lab' : 1, 'Data Stucture Lab' : 1, 'Circuits & Systems Lab' : 1, 'CGMM Lab' : 1 }
        credits = 28

    elif sem == 4:
        subjects = { 'App. Maths-IV' : 4, 'Computer Organisation & Architecture' : 4, 'Theory of Computation' : 4, 'Database Management' : 4, 'Object Oriented Programming' : 3, 'Control Systems' : 4 }
        labs = { 'App. Maths Lab' : 1, 'COA Lab' : 1, 'DBMS Lab' : 1, 'OOPS Lab' : 1, 'Control Systems Lab' : 1 }
        credits = 28

    elif sem == 5:
        subjects = { 'Algo. Design & Analysis' : 4, 'Software Engineering' : 4, 'Java Programming' : 4, 'Industrial Management' : 3, 'Communication Systems' : 4, 'Communication Skills' : 1 }
        labs = { 'Algo. Design Lab' : 1, 'Software Engineering Lab' : 1, 'Java Programming Lab' : 1, 'In-house Workshop' : 1, 'Communication Systems Lab' : 1, 'Communication Skills Lab' : 1 }
        credits = 26

    elif sem == 6:
        subjects = { 'Compiler Design' : 4, 'Operating Systems' : 4, 'Data Communication & Networks' : 4, 'Web Engineering' : 3, 'Artificial Intelligence' : 4, 'Microprocessors & Microcontrollers' : 4, }
        labs = { 'Operating Systems Lab' : 1, 'Networks Lab' : 1, 'Web Engineering Lab' : 1, 'Microprocessor & Microcontroller Lab' : 1 }
        credits = 27
    
    elif sem == 7:
        subjects = { 'Advanced Computer Networks' : 4, 'Cryptography and Network Security' : 3, 'Wireless Communication' : 3, 'Embedded Systems/Optoelectronics/Cloud Computing' : 3, 'Distributed Databases/Semantic Web Technologies/Software Testing/Digital Signal Processing' : 3, '.NET and C# Programming/Enterprise Computing in Java/System and Network Administration/Grid Computing' : 3, 'Advanced Database Administration/Probablistic Graphical Models/Sociology and Elements of Indian History for Engineers' : 3 }
        labs = { 'Advanced Computer Networks Lab' : 1, 'Cryptography and Network Security Lab' : 1, 'Wireless Communication Lab' : 1, 'Lab based on Elective Group– A or B' : 1, 'Summer Training/Industrial workshop/Certification' : 1 , 'Minor Project' : 3}
        credits = 24
    
    elif sem == 8:
        subjects = { 'Mobile Computing' : 4, 'Ad hoc and Sensor Networks' : 3, 'Human Values and Professional Ethics-II' : 1, 'Big Data Analytics/Social Network Analysis/Soft Computing' : 3, 'Bio Informatics/Web Application development using .NET/VLSI Design/Information Theory and Coding/Human Computer Interaction ' : 3, 'Digital Image Processing/Next Generation Networks/GPS and GIS' : 3, 'Satellite Communication/E-Commerce and M-Commerce/Distributed Systems/Selected Topics of Recent Trends in Information Technology' : 3 }
        labs = { 'Mobile Computing Lab' : 1, 'Ad hoc and Sensor Networks Lab' : 1, 'Lab based on Elective - I' : 1, 'Lab based on Elective - II' : 1, 'Major Project ' : 8}
        credits = 26

    with col1:
        st.markdown("<h4 style='text-align: center; color: crimson;'>Theory Subjects</h4>", unsafe_allow_html=True)
        for subject in subjects:
            marks = st.number_input("{}:".format( subject ), 0, 100)
            if marks == 0 :
                flag = 1
            num = grades(marks)
            GPA += num * subjects[subject]

    with col2:
        st.markdown("<h4 style='text-align: center; color: crimson;'>Practical Subjects</h4>", unsafe_allow_html=True)
        for lab in labs:
            marks = st.number_input("{}:".format( lab ), 0, 100)
            if marks == 0 :
                flag = 1
            num = grades(marks)
            GPA += num * labs[lab]

    if flag:
        st.warning("You haven't entered the marks of all subjects!")

    GPA = GPA / credits
    return GPA

    

st.markdown("<h1 style='text-align: center; color: black; background-image: linear-gradient(to bottom, #b71269, #cf5f5a, #d4996d, #d7cba4, #eef4e8);'>CalcGPA</h1>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center; background-image: linear-gradient(to top, #b71269, #cf5f5a, #d4996d, #d7cba4, #eef4e8);'>Semester GPA Calculator of B.Tech(IT)</h3>", unsafe_allow_html=True)

with st.container():
    name = st.text_input("ENTER YOUR NAME")

    if name:
        st.write("Hello {}!".format(name))
        sem = st.number_input("ENTER YOUR SEMESTER", 0, 8)

        if sem:
            st.write("")
            st.write("")
            st.markdown("<h3 style='text-align: center; '>Enter Marks!</h3>", unsafe_allow_html=True)

            GPA = calc(sem)

            st.write("")
            st.write("")

            cl1, cl2, cl3, cl4, cl5, cl6, cl7, cl8, cl9 = st.columns(9)
            with cl5:
                ans = st.button("Submit")
    
            if ans:
                my_bar = st.progress(0)
                for percent_complete in range(100):
                    time.sleep(0.1)
                    my_bar.progress(percent_complete + 1)
                
                msg = "Your GPA: {}".format(str(round(GPA,2)))
                st.markdown(f"<h3 style='text-align: center; '>{msg}</h3>", unsafe_allow_html=True)
                if GPA >= 8.0 :
                    st.balloons()
                    st.balloons()
                    