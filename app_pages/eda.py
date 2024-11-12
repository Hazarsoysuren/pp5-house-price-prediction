import streamlit as st
import pandas as pd
import seaborn as sns

import matplotlib.pyplot as plt

def eda_page(df):
    st.title("Exploratory Data Analysis (EDA)")

    st.header("Histograms for Key Features")
    features = ['bedrooms', 'bathrooms', 'sqft_living']
    for feature in features:
        st.subheader(f"Histogram for {feature}")
        fig, ax = plt.subplots()
        sns.histplot(df[feature], kde=True, ax=ax)
        st.pyplot(fig)

    st.header("Scatter Plots")
    st.subheader("Price vs. Square Footage")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df['sqft_living'], y=df['price'], ax=ax)
    st.pyplot(fig)

    st.header("Heatmap for Feature Correlations")
    fig, ax = plt.subplots()
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

    st.header("Descriptive Statistics")
    st.write(df.describe())

# Example usage
if __name__ == "__main__":
    # Load your dataset here
    df = pd.read_csv('/workspace/pp5-house-price-prediction/housing.csv')
    eda_page(df)