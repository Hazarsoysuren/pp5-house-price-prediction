import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def eda_page():
    # Load the data directly within the function
    df = pd.read_csv("/workspace/pp5-house-price-prediction/housing.csv")

    st.title("Exploratory Data Analysis (EDA)")

    # Display histograms
    st.header("Histograms for Key Features")
    features = ['bedrooms', 'bathrooms', 'sqft_living', 'price']
    for feature in features:
        st.subheader(f"Histogram for {feature}")
        fig, ax = plt.subplots()
        sns.histplot(df[feature], kde=True, ax=ax)
        st.pyplot(fig)

    # Display scatter plot
    st.header("Scatter Plot - Price vs. Square Footage")
    fig, ax = plt.subplots()
    sns.scatterplot(x=df['sqft_living'], y=df['price'], ax=ax)
    ax.set_xlabel("Square Footage (sqft_living)")
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
