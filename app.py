import streamlit as st
import pandas as pd
import random


# Initialize session state
if 'product_data' not in st.session_state:
    st.session_state.product_data = pd.DataFrame(columns=['Product_Name', 'Stock_On_Hand'])


# Function to generate random products
def generate_products():
    product_names = []
    stock_on_hand = []
    for i in range(40):
        product_name = f'Item {i + 1}'
        stock = random.randint(20, 50)
        product_names.append(product_name)
        stock_on_hand.append(stock)
    return product_names, stock_on_hand


# Function to add generated products to the session state
def add_products_to_session():
    product_names, stock_on_hand = generate_products()
    new_data = pd.DataFrame({'Product_Name': product_names, 'Stock_On_Hand': stock_on_hand})
    st.session_state.product_data = pd.concat([st.session_state.product_data, new_data])


# Function to sort by Product_Name ascending
def sort_by_product_name():
    st.session_state.product_data = st.session_state.product_data.sort_values(by='Product_Name')


# Function to sort by Stock_On_Hand descending
def sort_by_stock_on_hand():
    st.session_state.product_data = st.session_state.product_data.sort_values(by='Stock_On_Hand', ascending=False)


# Function to reduce Stock_On_Hand by 2 for all products
def reduce_stock():
    st.session_state.product_data['Stock_On_Hand'] -= 2


# Function to increase Stock_On_Hand by 2 for products ending in even numbers
def increase_stock_even():
    st.session_state.product_data.loc[st.session_state.product_data['Product_Name'].str[-1].astype(int) % 2 == 1, 'Stock_On_Hand'] += 2


# Streamlit UI
st.title("Product Inventory Management")
st.write("Click the buttons below to perform actions on the product data.")

# Button to generate products
if st.button("Generate Products"):
    add_products_to_session()

# Button to sort by Product_Name ascending
if st.button("Sort by Product Name (Asc)"):
    sort_by_product_name()

# Button to sort by Stock_On_Hand descending
if st.button("Sort by Stock On Hand (Desc)"):
    sort_by_stock_on_hand()

# Button to reduce Stock_On_Hand by 2
if st.button("Reduce Stock On Hand by 2"):
    reduce_stock()

# Button to increase Stock_On_Hand by 2 for even-ending product names
if st.button("Increase Stock On Hand for Even-Ending Names"):
    increase_stock_even()

# Display records
st.write(st.session_state.product_data.head(40))

