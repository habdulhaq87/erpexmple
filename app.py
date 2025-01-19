import streamlit as st
from database import database_page
import pandas as pd

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

# Add Data Page
def add_data_page():
    st.title("Add Data to ERP")

    st.markdown("### Enter New Transaction Details:")
    with st.form("add_data_form", clear_on_submit=True):
        transaction_id = st.number_input("Transaction ID", min_value=1000, step=1)
        date = st.date_input("Transaction Date")
        customer_id = st.number_input("Customer ID", min_value=1, step=1)
        product_id = st.number_input("Product ID", min_value=1, step=1)
        product_name = st.text_input("Product Name")
        category = st.selectbox("Category", ["Dairy", "Bakery", "Eggs", "Fruits", "Grains", "Meat", "Seafood", "Vegetables"])
        quantity = st.number_input("Quantity", min_value=1, step=1)
        unit_price = st.number_input("Unit Price", min_value=0.01, step=0.01, format="%.2f")
        payment_method = st.selectbox("Payment Method", ["Cash", "Credit Card", "Debit Card"])
        store_location = st.selectbox("Store Location", ["Downtown", "Suburb"])
        
        submitted = st.form_submit_button("Add Transaction")
        if submitted:
            # Calculate total price
            total_price = quantity * unit_price

            # Append the new data to the CSV
            new_data = pd.DataFrame({
                "Transaction_ID": [transaction_id],
                "Date": [date],
                "Customer_ID": [customer_id],
                "Product_ID": [product_id],
                "Product_Name": [product_name],
                "Category": [category],
                "Quantity": [quantity],
                "Unit_Price": [unit_price],
                "Total_Price": [total_price],
                "Payment_Method": [payment_method],
                "Store_Location": [store_location]
            })

            try:
                erp_data = pd.read_csv("erp.csv")
                updated_data = pd.concat([erp_data, new_data], ignore_index=True)
                updated_data.to_csv("erp.csv", index=False)
                st.success("Transaction added successfully!")
            except FileNotFoundError:
                st.error("The 'erp.csv' file does not exist. Please ensure the file is in the main directory.")
            except Exception as e:
                st.error(f"An error occurred: {e}")

# Main App
def main():
    # Navigation menu
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Home", "Database", "Add Data"])

    # Render selected page
    if page == "Home":
        home_page()
    elif page == "Database":
        database_page()
    elif page == "Add Data":
        add_data_page()

if __name__ == "__main__":
    main()
