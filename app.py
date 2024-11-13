import streamlit as st
from app_pages.multipage import MultiPage

# load pages scripts
from app_pages.page_summary import page_summary_body
from app_pages.page_eda import eda_page
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_prediction import page_prediction_body

app = MultiPage(app_name= "House prices") # Create an instance of the app 

# Add your app pages here using .add_page()
app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Exploratory Data Analysis (EDA)", eda_page)
app.add_page("Project Hypothesis and Validation", page_project_hypothesis_body)
app.add_page("Prediction", page_prediction_body)

app.run() # Run the  app