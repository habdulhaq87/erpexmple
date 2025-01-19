import streamlit as st
import pandas as pd
import plotly.express as px

# Load the dataset
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Home Page
def home_page():
    st.title("Welcome to the ERP Visualization App")
    st.write("""
    This application provides a comprehensive overview of retail grocery transactions.
    Navigate to the "Database" page to explore the dataset, filter data, and visualize key metrics.
    """)
    st.image(
        "https://source.unsplash.com/featured/?grocery,store", 
        use_column_width=True, 
        caption="Retail Grocery Insights"
    )
    st.markdown("""
    ### Features:
    - View transaction data in an easy-to-read format.
    - Apply filters by date, category, and payment method.
    - Visualize key metrics with interactive graphs.
    """)
    st.info("Use the navigation menu above to switch between pages.")

# Database Page
def database_page():
    st.title("Database and Visualizations")
    st.write("Explore the transaction data and gain insights with visualizations.")

    # Load data
    try:
        data = load_data("erp.csv")
    except FileNotFoundError:
        st.error("File 'erp.csv' not found in the main directory. Please ensure it exists.")
        return

    # Filter options in main UI
    st.subheader("Filter Options")
    with st.container():
        unique_dates = data["Date"].unique()
        unique_categories = data["Category"].unique()
        unique_payment_methods = data["Payment_Method"].unique()

        col1, col2, col3 = st.columns(3)

        with col1:
            selected_date = st.multiselect("Select Date(s)", unique_dates, default=unique_dates)
        with col2:
            selected_category = st.multiselect("Select Category(s)", unique_categories, default=unique_categories)
        with col3:
            selected_payment = st.multiselect("Select Payment Method(s)", unique_payment_methods, default=unique_payment_methods)

    # Apply filters
    filtered_data = data[
        (data["Date"].isin(selected_date)) &
        (data["Category"].isin(selected_category)) &
        (data["Payment_Method"].isin(selected_payment))
    ]

    # Display filtered data
    st.subheader("Filtered Data")
    st.dataframe(filtered_data)

    # Visualization section
    st.subheader("Visualizations")

    # Total Sales by Category
    sales_by_category = (
        filtered_data.groupby("Category")["Total_Price"].sum().reset_index()
    )
    st.write("### Total Sales by Category")
    fig1 = px.bar(sales_by_category, x="Category", y="Total_Price", title="Total Sales by Category")
    st.plotly_chart(fig1, use_container_width=True)

    # Total Sales by Date
    sales_by_date = (
        filtered_data.groupby("Date")["Total_Price"].sum().reset_index()
    )
    st.write("### Total Sales by Date")
    fig2 = px.line(sales_by_date, x="Date", y="Total_Price", title="Total Sales by Date")
    st.plotly_chart(fig2, use_container_width=True)

    # Payment Method Breakdown
    payment_breakdown = (
        filtered_data["Payment_Method"].value_counts().reset_index()
    )
    payment_breakdown.columns = ["Payment_Method", "Count"]
    st.write("### Payment Method Breakdown")
    fig3 = px.pie(payment_breakdown, names="Payment_Method", values="Count", title="Payment Method Breakdown")
    st.plotly_chart(fig3, use_container_width=True)

# Main app
def main():
    # Navigation menu
    st.set_page_config(page_title="ERP Visualization App", layout="wide")
    menu = ["Home", "Database"]
    choice = st.selectbox("Navigation", menu, index=0)

    if choice == "Home":
        home_page()
    elif choice == "Database":
        database_page()

if __name__ == "__main__":
    main()
