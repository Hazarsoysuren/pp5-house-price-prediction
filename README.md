# California Housing Price Prediction

## Project Overview

**Link to live website**: [California Housing Price Prediction](#)

This project focuses on predicting housing prices in California based on various features such as the location, median income, and housing characteristics. The machine learning model aims to predict the median house value using a dataset with information about California's housing.

## Dataset Content

The dataset consists of information about housing in California. It includes various features such as:
- Longitude and latitude
- Median house value
- Number of rooms and bedrooms
- Population and households
- Median income, etc.

This dataset is sourced from a public dataset and is split into training, validation, and test sets for model development.

## Business Requirements

As data analysts from Code institute, i was tasked with developing a predictive model that can accurately estimate housing prices based on the dataset provided. The business requirements include:
1. **Data Analysis**: Understand key features affecting housing prices.
2. **Prediction Model**: Develop a machine learning model that can predict housing prices.
3. **Dashboard**: Create a dashboard that enables users to interact with the model and test predictions.

## Hypothesis and Validation

- **Hypothesis**: The features such as median income and number of rooms have a significant impact on housing prices.
- **Validation**: We will train a model using a **Convolutional Neural Network (CNN)** for feature analysis and a regression model for price prediction. We will compare the model's performance with and without augmented data.
  
### Hypothesis Testing:
1. **Hypothesis 1**: Higher median income results in higher housing prices.
2. **Hypothesis 2**: The number of rooms and bedrooms is positively correlated with the house price.

### Model Validation:
- The model will first be tested with a baseline approach, followed by the use of higher-quality images (features) for training.
- Fine-tuning hyperparameters will be conducted to optimize the performance.

## Rationale for Mapping Business Requirements to ML Tasks

### Business Requirement 1: Data Visualization
As a client, we want to access detailed data analysis to better understand the factors influencing housing prices.

- We will design a **Streamlit Dashboard** to showcase visualizations, including scatter plots, correlations, and distributions of key features.
- **Key Visualizations**:
  - Display the average price distribution across geographical regions.
  - Analyze the relationship between income levels and house prices.
  - Show a heatmap of correlations among various features.

### Business Requirement 2: Classification
As a client, we need to predict housing prices using an ML model based on the given dataset.

- We will develop a model to predict housing prices based on inputs like median income, number of rooms, and other features.
- A regression model will be created using **XGBoost** or **Linear Regression** and tested on both training and validation datasets.

## Model Success Metrics

- **Accuracy**: The model should predict the median house price with an accuracy of at least 80% on the test set.
- **Metrics**: 
  - Mean Absolute Error (MAE)
  - Root Mean Squared Error (RMSE)
  - R-squared (R²)

The model will output the predicted house price along with the probability for each prediction.

## Dashboard Design

### Page 1: Project Overview
- **General Information**: An overview of the project, its goals, and its significance.
- **Project Dataset**: Information about the dataset, including the source, size, and type of data.
- **Link to Resources**: Provide links to external documentation or related resources.
- **Business Requirements**: State the business requirements clearly.

### Page 2: Data Analysis
- **Exploratory Data Analysis (EDA)**:
  - **Feature Analysis**: Visualize key features like median income, the number of rooms, etc.
  - **Correlation Analysis**: Display correlations between features and house prices.
  - **Dataset Summary**: Provide a statistical overview of the dataset.

### Page 3: Housing Price Prediction Model
- **Prediction Model**: Show the results of the machine learning model used for price prediction.
- **Upload Image Widget**: Users can upload their own housing data to test the model.
- **Model Performance**: Display the model's accuracy and how it differentiates between different price ranges.

### Page 4: Hypothesis Testing
- **Hypothesis Validation**: Present the hypotheses and the validation methods used to test them.
- **Results**: Show how each hypothesis impacts the model performance.

### Page 5: Model Performance Metrics
- **Learning Curves**: Display loss/accuracy curves for training and validation sets.
- **Evaluation Results**: Summarize if the model meets the performance criteria, including error metrics like MAE and RMSE.

## Deployment

The project has been deployed on [Heroku](https://www.heroku.com/). You can access the live version of the housing price prediction model at the following link:

[Live App](https://pp5-house-prediction-price-c344e168753d.herokuapp.com)

### Deployment Steps:
1. **Create a Heroku App**: Sign up/log into Heroku, and create a new app.
2. **Deploy via GitHub**: Connect the app to the GitHub repository and deploy the project.
3. **Set Up the Environment**: Set Python version in the `runtime.txt` file and configure the environment.

### Local Development Setup:
1. **Fork the Repository**: Fork the GitHub repository to your own account.
2. **Clone the Project**: Clone the repository to your local machine.
3. **Create a Virtual Environment**: Use `python3 -m venv venv` to set up a virtual environment.
4. **Install Dependencies**: Install the required dependencies using `pip install -r requirements.txt`.
5. **Run the App**: Start the app with `streamlit run app.py`.

## Libraries Used

This project uses the following libraries:

- **numpy** (version >=1.18.5, <1.24) - For numerical operations.
- **pandas** (version ==1.4.2) - For data manipulation and analysis.
- **matplotlib** (version ==3.3.1) - For creating static, animated, and interactive visualizations.
- **seaborn** (version ==0.11.0) - For statistical data visualization.
- **ydata-profiling** (version ==4.4.0) - For performing exploratory data analysis (EDA) and generating data profiles.
- **plotly** (version ==4.12.0) - For creating interactive plots.
- **ppscore** (version ==1.2.0) - For calculating feature importance.
- **streamlit** (version ==0.85.0) - For creating the interactive web application/dashboard.
- **feature-engine** (version ==1.0.2) - For feature engineering and preprocessing.
- **imbalanced-learn** (version ==0.8.0) - For dealing with imbalanced datasets.
- **scikit-learn** (version ==0.24.2) - For machine learning algorithms and tools.
- **xgboost** (version ==1.2.1) - For gradient boosting algorithm implementation.
- **yellowbrick** (version ==1.3) - For visualizing machine learning models.
- **Jinja2** (version ==3.1.1) - For templating engine used in rendering HTML pages.
- **MarkupSafe** (version ==2.0.1) - For escaping text and making it safe to use in templates.
- **protobuf** (version ==3.20) - For working with protocol buffers.
- **ipywidgets** (version ==8.0.2) - For interactive widgets in Jupyter Notebooks.
- **altair** (version <5) - For declarative statistical visualization.

To install all the required dependencies, use:


pip install -r requirements.txt

## Credits

### Content 
The dataset is sourced from [Kaggle](https://www.kaggle.com/datasets/camnugent/california-housing-prices/data)
