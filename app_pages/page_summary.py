import streamlit as st

def page_summary_body():
    st.write("### Project Summary")

    # text based on README file - "Dataset Content" section
    st.info(
        f"**Project Summary**\n"
        f"* A **real estate agency** is a business that arranges the selling, renting, or management of properties.\n"
        f"* An **investment area** is a location where the agency considers investing in properties.\n"
        f"* A **profitable area** is a location where the agency has successfully invested and gained profit.\n"
        f"* This project aims to identify **potential investment areas** based on various factors such as property prices, "
        f"rental yields, and market trends.\n\n"
        f"**Project Dataset**\n"
        f"* The dataset represents **real estate data** from various locations, containing information on property prices, "
        f"rental yields, market trends, and other relevant factors that influence investment decisions.")

    # Link to README file, so the users can have access to full project documentation
    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/your-repo/real-estate-investment).")
    

    # copied from README file - "Business Requirements" section
    st.success(
        f"The project has 2 business requirements:\n"
        f"* 1 - The client is interested in understanding the patterns from the real estate data "
        f"so that the client can learn the most relevant variables that are correlated to a "
        f"profitable investment area.\n"
        f"* 2 - The client is interested in determining whether or not a given area is worth investing in. "
        f"If so, the client is interested to know the potential return on investment. In addition, the client is "
        f"interested in learning from which cluster this area belongs in the market. "
        f"Based on that, present potential factors that could make the area more attractive for investment."
        )
