import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def eda_page():
    # Load the cleaned data directly within the function
    df = pd.read_csv("cleaned_housing.csv")

    st.title("Exploratory Data Analysis (EDA)")

    # Add the introductory text
    st.write("""
    Help clients understand key factors affecting house prices and provide insights into market trends.
    """)

    # Display histograms
    st.header("Histograms for Key Features")
    features = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income']
    for feature in features:
        st.subheader(f"Histogram for {feature}")
        fig, ax = plt.subplots()
        sns.histplot(df[feature], kde=True, ax=ax)
        st.pyplot(fig)

    # Display scatter plot
    st.header("Scatter Plot - Median Income vs. House Price")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df['median_income'], y=df['median_house_value'], ax=ax)
    ax.set_xlabel("Median Income")
    ax.set_ylabel("House Price")
    st.pyplot(fig)

    # Display heatmap of correlations
    st.header("Heatmap of Feature Correlations")
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

    # Display descriptive statistics
    st.header("Descriptive Statistics")
    st.write(df.describe())

if __name__ == "__main__":
    eda_page()