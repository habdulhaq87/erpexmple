import streamlit as st
from database import database_page

# Home Page
def home_page():
    st.title("Welcome to the ERP Visualization App")
    st.markdown(
        """
        This application allows you to explore and visualize retail grocery business transactions.
        Navigate to the **Database** page to analyze data and generate insights.
        """
    )
    st.image("https://via.placeholder.com/800x400?text=ERP+Visualization", use_column_width=True)
    st.markdown(
        """
        ### Features:
        - **Data Overview**: Explore the transaction dataset.
        - **Filtering Options**: Analyze specific subsets of data.
        - **Visualizations**: View insights with interactive charts.
        """
    )
    st.markdown("Navigate to the **Database** page to get started!")

# Main App
def main():
    # Navigation menu
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Database"])

    # Render selected page
    if page == "Home":
        home_page()
    elif page == "Database":
        database_page()

if __name__ == "__main__":
    main()
