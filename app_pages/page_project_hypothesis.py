import streamlit as st

def page_project_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.write(
        """
        **Hypothesis**:
        We hypothesize that certain features, such as **median income** and the **number of rooms**, significantly impact housing prices. 
        Specifically:
        - **Hypothesis 1**: Higher **median income** leads to higher housing prices.
        - **Hypothesis 2**: The **number of rooms** and **bedrooms** are positively correlated with higher house prices.
        
        **Validation**:
        To validate these hypotheses, we employed two approaches:
        1. **Feature Analysis**: Using various feature engineering techniques, including data visualizations and correlation analysis, we investigate how these features influence house prices.
        2. **Modeling**: We trained multiple machine learning models, starting with a **baseline regression model**, followed by more advanced models to optimize performance. 
        We also tested the impact of data augmentation on model accuracy.

        **Insights**:
        - The **correlation study** in the House Price Analysis supports that houses with more **bedrooms** and **bathrooms** tend to have higher prices.
        - A key finding from the analysis suggests that houses with **modern amenities**—such as updated kitchens and bathrooms—sell for higher prices. Realtors can use this insight to better market and price homes.
        
        These insights were validated through comprehensive model testing and fine-tuning of hyperparameters to improve the accuracy of predictions.
        """
    )

    st.success(
        f"* **Hypothesis 1**: Higher **median income** results in higher housing prices: Supported by our analysis and correlation study. \n\n"
        f"* **Hypothesis 2**: More **rooms** and **bedrooms** correlate with higher house prices: Validated by model testing and data exploration. \n\n"
        f"We will continue refining our model using higher-quality data and feature engineering to improve prediction accuracy."
    )
