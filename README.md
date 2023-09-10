# Products_Inventory_ST

A web-based product inventory management system using Streamlit, allowing users to generate and manipulate product data, all while persisting the data between interactions.

![Demo](https://github.com/Sagarkeshave/Products_Inventory_ST/blob/main/demo/ezgif.com-video-to-gif%20(3).gif)


## Features

- Generate 40 unique product names with random stock-on-hand values.
- Display product data in a tabular format with 20 records per page.
- Sort product data by product name (ascending) and stock-on-hand (descending).
- Reduce stock-on-hand by 2 for all products.
- Increase stock-on-hand by 2 for products with even-ending names.

## Requirements

- Python 3.10
- [Streamlit](https://streamlit.io/)
- [Pandas](https://pandas.pydata.org/)

You can install the required packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

## Installation
Clone the repository to your local machine:
```bash
git clone https://github.com/Sagarkeshave/Products_Inventory_ST.git
cd Products_Inventory_ST
```

## Usage
Run the Streamlit application:
bash
```
streamlit run app.py
```
Access the application in your web browser at http://localhost:8501.

Use the provided buttons to interact with the product data.
