import pandas as pd
import streamlit as st
import joblib
from sklearn.preprocessing import StandardScaler

def data_preprocessing(data_input):
    df = pd.read_csv('filtered_student_data.csv')
    df = df.drop(columns=['Status'], axis=1)
    df = pd.concat([data_input, df], ignore_index=True)
    df = StandardScaler().fit_transform(df)
    return df[0].reshape(1, -1)

def model_predict(df):
    model = joblib.load('rf_model.joblib')
    return model.predict(df)

def main():
    st.title(':school: Jaya Jaya Institute: Student Graduation Prediction 🎓')

    # Mappings
    gender_mapping = {'Male': 1, 'Female': 0}
    marital_status_mapping = {
        'Single': 1, 'Married': 2, 'Widower': 3,
        'Divorced': 4, 'Cohabitation': 5, 'Legally Separated': 6
    }
    application_mapping = {
    '1st Phase - General Contingent': 1,
    'Regulation No. 612/93': 2,
    '1st Phase - Special Contingent (Azores Island)': 5,
    'Holders of Other Higher Courses': 7,
    'Regulation No. 854-B/99': 10,
    'International Student (Bachelor)': 15,
    '1st Phase - Special Contingent (Madeira Island)': 16,
    '2nd Phase - General Contingent': 17,
    '3rd Phase - General Contingent': 18,
    'Regulation No. 533-A/99, Item B2 (Different Plan)': 26,
    'Regulation No. 533-A/99, Item B3 (Other Institution)': 27,
    'Over 23 Years Old': 39,
    'Transfer': 42,
    'Change of Major': 43,
    'Technological Specialization Diploma Holders': 44,
    'Change of Institution/Major': 51,
    'Short Cycle Diploma Holders': 53,
    'Change of Institution/Major (International)': 57
    }


    # Form inputs
    gender = gender_mapping[st.radio('Gender', ['Male', 'Female'])]
    age = st.number_input('Age at Enrollment', 17, 70)
    marital_status = marital_status_mapping[st.selectbox('Marital Status', list(marital_status_mapping.keys()))]
    application_mode = application_mapping[st.selectbox('Application Mode', list(application_mapping.keys()))]
    prev_qualification_grade = st.number_input('Previous Qualification Grade', 0, 200)
    admission_grade = st.number_input('Admission Grade', 0, 200)
    scholarship_holder = 1 if st.checkbox('Scholarship') else 0
    tuition_fees = 1 if st.checkbox('Tuition up to date') else 0
    displaced = 1 if st.checkbox('Displaced') else 0
    debtor = 1 if st.checkbox('Debtor') else 0

    c1, c2 = st.columns(2)
    with c1:
        first_enrolled = st.number_input('1st Sem Enrolled', 0, 26)
        first_approved = st.number_input('1st Sem Approved', 0, 26)
        first_grade = st.number_input('1st Sem Grade', 0, 20)
    with c2:
        second_enrolled = st.number_input('2nd Sem Enrolled', 0, 23)
        second_evaluated = st.number_input('2nd Sem Evaluations', 0, 33)
        second_approved = st.number_input('2nd Sem Approved', 0, 20)
        second_grade = st.number_input('2nd Sem Grade', 0, 20)
        second_uneval = st.number_input('2nd Sem No Evaluations', 0, 12)

    # Build DataFrame
    input_data = pd.DataFrame([[
        marital_status, application_mode, prev_qualification_grade, admission_grade,
        displaced, debtor, tuition_fees, gender, scholarship_holder, age,
        first_enrolled, first_approved, first_grade,
        second_enrolled, second_evaluated, second_approved, second_grade, second_uneval
    ]], columns=[
        'Marital_status', 'Application_mode', 'Previous_qualification_grade', 'Admission_grade',
        'Displaced', 'Debtor', 'Tuition_fees_up_to_date', 'Gender', 'Scholarship_holder', 'Age_at_enrollment',
        'Curricular_units_1st_sem_enrolled', 'Curricular_units_1st_sem_approved', 'Curricular_units_1st_sem_grade',
        'Curricular_units_2nd_sem_enrolled', 'Curricular_units_2nd_sem_evaluations',
        'Curricular_units_2nd_sem_approved', 'Curricular_units_2nd_sem_grade',
        'Curricular_units_2nd_sem_without_evaluations'
    ])

    if st.button('✨ Predict'):
        processed = data_preprocessing(input_data)
        prediction = model_predict(processed)
        if prediction[0] == 1:
            st.success("🎉 This student is likely to **Graduate**.")
        else:
            st.error("⚠️ This student is likely to **Dropout**.")

if __name__ == '__main__':
    main()
