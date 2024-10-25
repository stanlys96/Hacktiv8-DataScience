import streamlit as st
import pandas as pd
import joblib

df = pd.read_csv('data.csv')
df["Mental_Health_Condition"].fillna("Normal", inplace=True)
df["Physical_Activity"].fillna("None", inplace=True)

def user_input():
    age = st.sidebar.number_input('Age', value=23, min_value=10, max_value=100)
    gender = st.sidebar.selectbox("Gender", df["Gender"].unique())
    job_role = st.sidebar.selectbox('Job Role', df["Job_Role"].unique())
    industry = st.sidebar.selectbox('Industry', df["Industry"].unique())
    years_of_experience = st.sidebar.number_input('Years of Experience', value=5, min_value=0, max_value=100)
    work_location = st.sidebar.selectbox('Work Location', df["Work_Location"].unique())
    hours_worked_per_week = st.sidebar.number_input('Hours Worked Per Week', value=40, min_value=1, max_value=100)
    numer_of_virtual_meetings = st.sidebar.number_input('Number of Virtual Meetings', value=4, min_value=1, max_value=100)
    work_life_balance_rating = st.sidebar.selectbox('Work Life Balance Rating', sorted(df["Work_Life_Balance_Rating"].unique()))
    mental_health_condition = st.sidebar.selectbox('Mental Health Condition', df["Mental_Health_Condition"].unique())
    access_to_mental_health_resources = st.sidebar.selectbox('Access to Mental Health Resources', df["Access_to_Mental_Health_Resources"].unique())
    productivity_change = st.sidebar.selectbox('Productivity Change', df["Productivity_Change"].unique())
    social_isolation_rating = st.sidebar.selectbox('Social Isolation Rating', sorted(df["Social_Isolation_Rating"].unique()))
    satisfaction_with_remote_work = st.sidebar.selectbox('Satisfaction With Remote Work', df["Satisfaction_with_Remote_Work"].unique(), index=1)
    company_support_for_remote_work = st.sidebar.selectbox('Company Support For Remote Work', sorted(df["Company_Support_for_Remote_Work"].unique()), index=2)
    physical_activity = st.sidebar.selectbox('Physical Activity', df["Physical_Activity"].unique(), index=0)
    sleep_quality = st.sidebar.selectbox('Sleep Quality', df["Sleep_Quality"].unique(), index=0)
    region = st.sidebar.selectbox('Region', df["Region"].unique(), index=1)

    data = {
        'Age': age,
        'Gender': gender,
        'Job_Role': job_role,
        'Industry': industry,
        'Years_of_Experience': years_of_experience,
        'Work_Location': work_location,
        'Hours_Worked_Per_Week': hours_worked_per_week,
        'Number_of_Virtual_Meetings': numer_of_virtual_meetings,
        'Work_Life_Balance_Rating': work_life_balance_rating,
        "Mental_Health_Condition": mental_health_condition,
        "Access_to_Mental_Health_Resources": access_to_mental_health_resources,
        "Productivity_Change": productivity_change,
        "Social_Isolation_Rating": social_isolation_rating,
        "Satisfaction_with_Remote_Work": satisfaction_with_remote_work,
        "Company_Support_for_Remote_Work": company_support_for_remote_work,
        "Physical_Activity": physical_activity,
        "Sleep_Quality": sleep_quality,
        "Region": region
    }
    features = pd.DataFrame(data, index=[0])
    return features

def app():
    st.title('Prediction')
    st.subheader('Stress Level Model Prediction')
    st.sidebar.title('User Input')
    input = user_input()
    model = joblib.load("model.pkl")

    if st.button('Predict', type="secondary"):
        prediction = model.predict(input)
        st.write("Your input:")
        st.write(input)
        st.write("The prediction:")
        the_prediction = ""
        if prediction == 0:
            the_prediction = "Low"
        elif prediction == 1:
            the_prediction = "Medium"
        else:
            the_prediction = "High"
        st.write(f"We have predicted that the stress level of this employee is {the_prediction}")
    else:
        st.write("Click the button to predict!")
