import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Load the trained models and scalers
# Assuming you have saved your models and scalers
# For example:
# linear_model = joblib.load('linear_model.pkl')
# random_forest_model = joblib.load('random_forest_model.pkl')
# scaler = joblib.load('scaler.pkl')

# Dummy placeholders for models and scaler
linear_model = LinearRegression()
random_forest_model = RandomForestRegressor()
scaler = StandardScaler()

def predict_house_price(model, X_live):
    # Apply scaling
    X_live_scaled = scaler.transform(X_live)
    
    # Predict
    prediction = model.predict(X_live_scaled)
    
    return prediction

def main():
    st.title("California Housing Prices Prediction")

    st.write("""
    ## Input the features to get the predicted house price
    """)

    longitude = st.number_input("Longitude", value=-122.23)
    latitude = st.number_input("Latitude", value=37.88)
    housing_median_age = st.number_input("Housing Median Age", value=41.0)
    total_rooms = st.number_input("Total Rooms", value=880.0)
    total_bedrooms = st.number_input("Total Bedrooms", value=129.0)
    population = st.number_input("Population", value=322.0)
    households = st.number_input("Households", value=126.0)
    median_income = st.number_input("Median Income", value=8.3252)
    ocean_proximity = st.selectbox("Ocean Proximity", ["<1H OCEAN", "INLAND", "ISLAND", "NEAR BAY", "NEAR OCEAN"])

    # Create a DataFrame for the input
    input_data = pd.DataFrame({
        "longitude": [longitude],
        "latitude": [latitude],
        "housing_median_age": [housing_median_age],
        "total_rooms": [total_rooms],
        "total_bedrooms": [total_bedrooms],
        "population": [population],
        "households": [households],
        "median_income": [median_income],
        "ocean_proximity": [ocean_proximity]
    })
    # Rename the column if necessary

    input_data.rename(columns={'total_bedrooms': 'bedrooms'}, inplace=True)

    # Convert ocean_proximity to dummy variables
    input_data = input_data.join(pd.get_dummies(input_data.ocean_proximity)).drop(["ocean_proximity"], axis=1)

    # Log transformation
    input_data["total_rooms"] = np.log(input_data["total_rooms"] + 1)
    input_data["total_bedrooms"] = np.log(input_data["total_bedrooms"] + 1)
    input_data["population"] = np.log(input_data["population"] + 1)
    input_data["households"] = np.log(input_data["households"] + 1)

    # Feature engineering
    input_data["bedroom_ratio"] = input_data["total_bedrooms"] / input_data["total_rooms"]
    input_data["household_rooms"] = input_data["total_rooms"] / input_data["households"]

    if st.button("Predict with Linear Regression"):
        prediction = predict_house_price(linear_model, input_data)
        st.write(f"### Predicted House Price: ${prediction[0]:,.2f}")

    if st.button("Predict with Random Forest"):
        prediction = predict_house_price(random_forest_model, input_data)
        st.write(f"### Predicted House Price: ${prediction[0]:,.2f}")

if __name__ == "__main__":
    main()
