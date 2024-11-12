import streamlit as st


def page_project_hypothesis_body():

    st.write("### Project Hypothesis and Validation")

    # conclusions taken from "02 - House Price Analysis" notebook
    st.success(
        f"* We suspect that houses with more bedrooms and bathrooms have higher prices: Correct. "
        f"The correlation study in the House Price Analysis supports that. \n\n"

        f"* A survey showed that buyers highly value properties with modern amenities. "
        f"Houses with features like updated kitchens and bathrooms tend to sell for higher prices, "
        f"as demonstrated by the House Price Analysis. "
        f"This insight will be used by realtors to better market and price properties."
    )
