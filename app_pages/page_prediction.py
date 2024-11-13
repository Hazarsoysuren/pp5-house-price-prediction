import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

def page_prediction_body():
    # Load the dataset
    data = pd.read_csv("cleaned_housing.csv")

    st.title("Prediction Results")

    # Add the introductory text
    st.write("""
     Business requirement 2: Enable stakeholders to leverage predictive insights to make data-driven decisions about property investments.
    """)


    # Display the first few rows of the dataset
    st.header("First few rows of the dataset:")
    st.write(data.head())

    # Check for missing values
    st.header("Missing values in the dataset:")
    st.write(data.isnull().sum())

    # Drop rows with missing values
    data.dropna(inplace=True)

    # Display basic statistics
    st.header("Basic statistics of the dataset:")
    st.write(data.describe())

    # Histograms for each numeric column
    st.header("Histograms for each numeric column:")
    fig, ax = plt.subplots(figsize=(15, 10))
    data.hist(ax=ax)
    st.pyplot(fig)

    # Heatmap of correlations
    st.header("Heatmap of correlations:")
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.heatmap(data.corr(), annot=True, cmap="YlGnBu", ax=ax)
    st.pyplot(fig)

    # Scatter plot of latitude vs longitude colored by median house value
    st.header("Scatter plot of latitude vs longitude colored by median house value:")
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.scatterplot(x="latitude", y="longitude", hue="median_house_value", data=data, palette="coolwarm", ax=ax)
    st.pyplot(fig)

    # Feature engineering
    data["bedroom_ratio"] = data["total_bedrooms"] / data["total_rooms"]
    data["household_rooms"] = data["total_rooms"] / data["households"]

    # Display the first few rows after feature engineering
    st.header("First few rows after feature engineering:")
    st.write(data.head())

    # Heatmap of correlations after feature engineering
    st.header("Heatmap of correlations after feature engineering:")
    fig, ax = plt.subplots(figsize=(15, 8))
    sns.heatmap(data.corr(), annot=True, cmap="YlGnBu", ax=ax)
    st.pyplot(fig)

if __name__ == "__main__":
    page_prediction_body()