import streamlit as st
import pandas as pd
import joblib

# --------------------------
# LOGIN SECTION
# --------------------------

USERNAME = "admin"
PASSWORD = "12345"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Invalid Username or Password")

# --------------------------
# MAIN APP AFTER LOGIN
# --------------------------

else:

    model = joblib.load("Logistic_hiring_model.pkl")

    st.title("AI Hiring Prediction System")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    candidate_id = st.number_input("Candidate ID", value=1)

    age = st.number_input("Age", 18, 70)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    education_level = st.selectbox(
        "Education Level",
        ["Bachelor", "Master", "PhD"]
    )

    university_tier = st.selectbox(
        "University Tier",
        [1, 2, 3]
    )

    years_experience = st.number_input(
        "Years of Experience",
        0,
        40
    )

    employment_gap_months = st.number_input(
        "Employment Gap (Months)",
        0,
        120
    )

    technical_skill_score = st.slider(
        "Technical Skill Score",
        0,
        100
    )

    communication_score = st.slider(
        "Communication Score",
        0,
        100
    )

    aptitude_test_score = st.slider(
        "Aptitude Test Score",
        0,
        100
    )

    coding_test_score = st.slider(
        "Coding Test Score",
        0,
        100
    )

    project_count = st.number_input(
        "Project Count",
        0,
        50
    )

    github_activity_score = st.slider(
        "GitHub Activity Score",
        0,
        100
    )

    certifications_count = st.number_input(
        "Certifications",
        0,
        20
    )

    expected_salary = st.number_input(
        "Expected Salary"
    )

    ai_resume_score = st.slider(
        "AI Resume Score",
        0,
        100
    )

    ai_bias_score = st.slider(
        "AI Bias Score",
        0.0,
        1.0
    )

    gender = 1 if gender == "Male" else 0

    education = {
        "Bachelor": 0,
        "Master": 1,
        "PhD": 2
    }

    education_level = education[education_level]

    if st.button("Predict"):

        data = pd.DataFrame({

            "candidate_id": [candidate_id],
            "age": [age],
            "gender": [gender],
            "education_level": [education_level],
            "university_tier": [university_tier],
            "years_experience": [years_experience],
            "employment_gap_months": [employment_gap_months],
            "technical_skill_score": [technical_skill_score],
            "communication_score": [communication_score],
            "aptitude_test_score": [aptitude_test_score],
            "coding_test_score": [coding_test_score],
            "project_count": [project_count],
            "github_activity_score": [github_activity_score],
            "certifications_count": [certifications_count],
            "expected_salary": [expected_salary],
            "ai_resume_score": [ai_resume_score],
            "ai_bias_score": [ai_bias_score]

        })

        prediction = model.predict(data)

        if prediction[0] == 1:
            st.success("✅ Candidate Selected")

        else:
            st.error("❌ Candidate Not Selected")
import streamlit as st
import pandas as pd
import joblib

# --------------------------
# LOGIN SECTION
# --------------------------

USERNAME = "admin"
PASSWORD = "12345"

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:

    st.title("🔐 Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):

        if username == USERNAME and password == PASSWORD:
            st.session_state.logged_in = True
            st.rerun()

        else:
            st.error("Invalid Username or Password")

# --------------------------
# MAIN APP AFTER LOGIN
# --------------------------

else:

    model = joblib.load("Logistic_hiring_model.pkl")

    st.title("AI Hiring Prediction System")

    if st.button("Logout"):
        st.session_state.logged_in = False
        st.rerun()

    candidate_id = st.number_input("Candidate ID", value=1)

    age = st.number_input("Age", 18, 70)

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    education_level = st.selectbox(
        "Education Level",
        ["Bachelor", "Master", "PhD"]
    )

    university_tier = st.selectbox(
        "University Tier",
        [1, 2, 3]
    )

    years_experience = st.number_input(
        "Years of Experience",
        0,
        40
    )

    employment_gap_months = st.number_input(
        "Employment Gap (Months)",
        0,
        120
    )

    technical_skill_score = st.slider(
        "Technical Skill Score",
        0,
        100
    )

    communication_score = st.slider(
        "Communication Score",
        0,
        100
    )

    aptitude_test_score = st.slider(
        "Aptitude Test Score",
        0,
        100
    )

    coding_test_score = st.slider(
        "Coding Test Score",
        0,
        100
    )

    project_count = st.number_input(
        "Project Count",
        0,
        50
    )

    github_activity_score = st.slider(
        "GitHub Activity Score",
        0,
        100
    )

    certifications_count = st.number_input(
        "Certifications",
        0,
        20
    )

    expected_salary = st.number_input(
        "Expected Salary"
    )

    ai_resume_score = st.slider(
        "AI Resume Score",
        0,
        100
    )

    ai_bias_score = st.slider(
        "AI Bias Score",
        0.0,
        1.0
    )

    gender = 1 if gender == "Male" else 0

    education = {
        "Bachelor": 0,
        "Master": 1,
        "PhD": 2
    }

    education_level = education[education_level]

    if st.button("Predict"):

        data = pd.DataFrame({

            "candidate_id": [candidate_id],
            "age": [age],
            "gender": [gender],
            "education_level": [education_level],
            "university_tier": [university_tier],
            "years_experience": [years_experience],
            "employment_gap_months": [employment_gap_months],
            "technical_skill_score": [technical_skill_score],
            "communication_score": [communication_score],
            "aptitude_test_score": [aptitude_test_score],
            "coding_test_score": [coding_test_score],
            "project_count": [project_count],
            "github_activity_score": [github_activity_score],
            "certifications_count": [certifications_count],
            "expected_salary": [expected_salary],
            "ai_resume_score": [ai_resume_score],
            "ai_bias_score": [ai_bias_score]

        })

        prediction = model.predict(data)

        if prediction[0] == 1:
            st.success("✅ Candidate Selected")

        else:
            st.error("❌ Candidate Not Selected")
