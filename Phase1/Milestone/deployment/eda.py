import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def map_values(arr):
    mapping = {'Low': 0, 'Medium': 1, 'High': 2}
    return [mapping[value] for value in arr]

demographics_cols = ['Age_Group', 'Gender', 'Region']
job_cols = ['Job_Role', 'Industry', 'Years_of_Experience_Group']
work_condition_cols = ['Hours_Worked_Group', 'Work_Life_Balance_Group', 'Company_Support_Remote_Work_Group', 'Virtual_Meetings_Group', 'Work_Location',  'Satisfaction_with_Remote_Work', 'Productivity_Change']
mental_health_cols = ['Mental_Health_Condition', 'Access_to_Mental_Health_Resources', 'Stress_Level', 'Social_Isolation_Group']
physical_health_cols = ['Physical_Activity', 'Sleep_Quality']

color_palettes = [
    ['lightgreen', 'orange', 'lightblue', 'purple', 'pink', 'yellow', 'red'],    # Colors for the first pie chart
    ['cyan', 'magenta', 'grey', 'lightcoral', 'lightblue', 'gold', 'lightgreen'],      # Colors for the second pie chart
    ['lightyellow', 'violet', 'tan', 'salmon', 'lavender', 'teal', 'brown'],     # Colors for the third pie chart
    ['skyblue', 'coral', 'limegreen', 'slategray', 'orchid', 'crimson', 'khaki']  # Colors for the fourth pie chart
]

# Function to categorize age into 3 groups
def categorize_age(age):
    if 20 <= age <= 34:
        return 'Young adults (20-34)'
    elif 35 <= age <= 49:
        return 'Mid-career adults (35-49)'
    elif age >= 50:
        return 'Senior adults (50+)'
    else:
        return 'Unknown'
    
# Function to categorize years of experience into 3 groups
def categorize_experience(years):
    if 0 <= years <= 10:
        return 'Early career (0-10 years)'
    elif 11 <= years <= 20:
        return 'Mid-career (11-20 years)'
    elif years >= 21:
        return 'Senior career (21+ years)'
    else:
        return 'Unknown'
    
# Function to categorize hours worked into 3 groups
def categorize_hours(hours):
    if 0 <= hours <= 30:
        return 'Part-time (0-30 hours)'
    elif 31 <= hours <= 45:
        return 'Full-time (31-45 hours)'
    elif hours >= 46:
        return 'Overtime (46+ hours)'
    else:
        return 'Unknown'

# Function to categorize social isolation rating into 3 groups
def categorize_isolation(rating):
    if rating == 1:
        return 'Low Isolation (1)'
    elif rating in [2, 3]:
        return 'Moderate Isolation (2-3)'
    elif rating in [4, 5]:
        return 'High Isolation (4-5)'
    else:
        return 'Unknown'
    
# Function to categorize work-life balance rating into 3 groups
def categorize_work_life_balance(rating):
    if rating == 1:
        return 'Poor Balance (1)'
    elif rating in [2, 3]:
        return 'Moderate Balance (2-3)'
    elif rating in [4, 5]:
        return 'Good Balance (4-5)'
    else:
        return 'Unknown'
    
# Function to categorize company support rating into 3 groups
def categorize_company_support(rating):
    if rating == 1:
        return 'Poor Support (1)'
    elif rating in [2, 3]:
        return 'Moderate Support (2-3)'
    elif rating in [4, 5]:
        return 'Strong Support (4-5)'
    else:
        return 'Unknown'
    
# Function to categorize virtual meetings into 3 groups
def categorize_meetings(meetings):
    if 0 <= meetings <= 5:
        return 'Low Meetings (0-5)'
    elif 6 <= meetings <= 10:
        return 'Moderate Meetings (6-10)'
    elif meetings >= 11:
        return 'High Meetings (11+)'
    else:
        return 'Unknown'
    
st.markdown(
    """
    <style>
    .center {
        display: flex;
        justify-content: center;
    }
    </style>
    """, unsafe_allow_html=True
)

def app():
    df_original = pd.read_csv("data.csv")
    df = df_original.copy()
    df["Mental_Health_Condition"].fillna("Normal", inplace=True)
    df["Physical_Activity"].fillna("None", inplace=True)
    df['Stress_Level'] = map_values(df["Stress_Level"])
    df['Age_Group'] = df['Age'].apply(categorize_age)
    df['Years_of_Experience_Group'] = df['Years_of_Experience'].apply(categorize_experience)
    df['Hours_Worked_Group'] = df['Hours_Worked_Per_Week'].apply(categorize_hours)
    df['Social_Isolation_Group'] = df['Social_Isolation_Rating'].apply(categorize_isolation)
    df['Work_Life_Balance_Group'] = df['Work_Life_Balance_Rating'].apply(categorize_work_life_balance)
    df['Company_Support_Remote_Work_Group'] = df['Company_Support_for_Remote_Work'].apply(categorize_company_support)
    df['Virtual_Meetings_Group'] = df['Number_of_Virtual_Meetings'].apply(categorize_meetings)
    st.header('Remote Work & Mental Health Prediction Project', divider='rainbow')
    st.subheader('Exploratory Data Analysis')

    eda_list = ["Numerical Distributions", "Age Groups Chart", "Job Roles Chart", "Stress Level Correlations", "Social Isolation Rating Chart", "Stress Level By Job Role", "Mental Health Condition By Job Role", "Productivity Rate By Work Location", "Mental Health Condition By Work Location"]
    val = st.sidebar.radio("Choose plot to show", eda_list)
    if val == "Numerical Distributions":
        numerical_columns = ['Age', 'Years_of_Experience', 'Hours_Worked_Per_Week', 'Number_of_Virtual_Meetings']
        df[numerical_columns].hist(figsize=(12, 8))
        plt.tight_layout()
        plt.suptitle("Numerical values histogram")
        plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1, wspace=0.2, hspace=0.2)
        st.pyplot(plt)
        st.write("Insight: the numerical values in our data are all normal distributions.")
    elif val == "Age Groups Chart":
        the_count = df["Age_Group"].value_counts()
        
        plt.pie(the_count, labels=the_count.index, autopct='%1.1f%%', startangle=90, colors=color_palettes[0])
        plt.tight_layout()
        plt.title("Age Group Pie Chart")
        plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1, wspace=0.2, hspace=0.2)
        st.pyplot(plt)
        st.write("Insight: The age distribution seems to be quite balanced from the 3 categories, with the most data lies in Mid-career adults (Aged 35-49)")
    elif val == "Job Roles Chart":
        the_count = df["Job_Role"].value_counts()
        
        plt.pie(the_count, labels=the_count.index, autopct='%1.1f%%', startangle=90, colors=color_palettes[1])
        plt.tight_layout()
        plt.title("Job Roles Pie Chart")
        plt.subplots_adjust(left=0.1, right=0.9, top=0.85, bottom=0.1, wspace=0.2, hspace=0.2)
        st.markdown('<div class="center">', unsafe_allow_html=True)
        st.pyplot(plt)
        st.markdown('</div>', unsafe_allow_html=True)
        st.write("Insight: The job roles distribution seem to be quite balanced from the 7 categories, with the most data being Project Manager with 14.8% of the total")   
    elif val == "Stress Level Correlations":
        numerical_columns_with_stress_level = ['Stress_Level', 'Age', 'Years_of_Experience', 'Hours_Worked_Per_Week', 'Number_of_Virtual_Meetings']
        correlation_matrix = df[numerical_columns_with_stress_level].corr()
        plt.figure(figsize=(12, 8))
        sns.heatmap(correlation_matrix, annot=True, cmap='viridis', linewidths=0.5)  # Replace 'viridis' with your preferred colormap
        plt.title('Correlation Matrix of numerical columns and stress level with Heatmap')
        st.pyplot(plt)
        st.write("Insight: There does not seem to be much correlations between stress level and numerical features")
    elif val == "Social Isolation Rating Chart":
        sns.barplot(x='Access_to_Mental_Health_Resources', y='Social_Isolation_Rating', data=df[df["Work_Location"] == "Remote"])
        plt.title('Social Isolation Rating for Remote Workers with/without Access to Mental Health Resources')
        st.pyplot(plt)
        st.write("Insight: It appears that employees with access to mental health resources feel slightly socially more isolated")
    elif val == "Stress Level By Job Role":
        plt.figure(figsize=(12,6))
        sns.countplot(x='Job_Role',hue='Stress_Level',data=df_original)
        plt.title('Stress Level by Job Role')
        st.pyplot(plt)
        st.write("Insight: There does not seem to be any role that's too stressed, or least stressed. Everything seems balanced.")
    elif val == "Mental Health Condition By Job Role":
        plt.figure(figsize=(15,10))
        sns.countplot(x='Job_Role', hue='Mental_Health_Condition', data=df)
        plt.title('Mental Health Condition by Job Role')
        st.pyplot(plt)
        st.write("Insight: It can be seen that the role with the most burnout and least normal is Data Scientist. All others seem to be quite balanced.")
    elif val == "Productivity Rate By Work Location":
        plt.figure(figsize=(12,6))
        sns.countplot(data=df, x='Work_Location', hue='Productivity_Change')
        plt.title('Rate Of Productivity By Work Location')
        st.pyplot(plt)
        st.write("Insight: There does not seem to be any work location that contribute to increase/decrease in productivity change, all seems balanced.")
    elif val == "Mental Health Condition By Work Location":
        plt.figure(figsize=(12,6))
        sns.countplot(x='Work_Location',hue='Mental_Health_Condition',data=df)
        plt.title('Mental Health Condition by Work Location')
        st.pyplot(plt)
        st.write("Insight: There does not seem to be any work location that contribute to more burnout or more depression, all seems balanced.")