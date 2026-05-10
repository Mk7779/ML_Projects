
import streamlit as st
import pandas as pd
import numpy as np

# st.title("STREAMLIT SESSION")

# st.header("Header")

# st.subheader("Sub header")

# st.text("The is an interactive streamlit application")


# st.markdown("""
# # h1 tag
# ## h2 tag
# ### h3 tag

# :moon: <br>
# :sunglasses:
            
# **bold**
# _italic_

# """
# ,True)

# st.write(1,2,3,4)

# st.write('The numbers are',[1,2,3,4,5])

# st.write("## The is a text")

# dic = {
#     "name":"guvi",
#     'age':10,
#     'place':'chennai'
# }

# st.write(dic)

df = pd.read_csv("C:/users/ShadZz/Downloads/cancer.csv")

# st.write(df)

# st.dataframe(df)

#st.table(df)

data = {
    "user_id": 12345,
    "user_info": {
        "name": "Alice",
        "email": "alice@example.com",
        "age": 29
    },
    "purchases": [
        {
            "item_id": "A001",
            "item_name": "Laptop",
            "price": 1200.99,
            "quantity": 1
        },
        {
            "item_id": "B002",
            "item_name": "Mouse",
            "price": 25.50,
            "quantity": 2
        }
    ],
    "timestamp": "2024-08-11T15:30:00Z"
}

#st.json(data,expanded=False)

st.metric("TCS STOCK",value=897,delta="12.5")

st.metric("TCS STOCK",value=897,delta="-12.5")

st.metric("TCS STOCK",value=897,delta="12.5",delta_color="off")




