import streamlit as st
import eda
import prediction
import home

PAGES = {
    "Home": home,
    "Exploratory Data Analysis": eda,
    "Prediction": prediction
}
st.sidebar.title('Navigation')

selection = st.sidebar.selectbox("Go to", list(PAGES.keys()))
page = PAGES[selection]
page.app()