import streamlit as st
import pandas as pd

st.set_page_config(page_title="Shopping Cart", layout="centered")

# st.title("🛒 Your Shopping Cart")

# # Initialize session state if not exists
# if "cart" not in st.session_state:
#     st.session_state["cart"] = []

# if "dataframe" not in st.session_state:
#     st.session_state["dataframe"] = None

# # Display cart items
# if st.session_state["cart"]:
#     st.subheader("Cart Items:")
#     for item in st.session_state["cart"]:
#         st.markdown(f"- {item}")

#     # Add a button to clear the cart
#     if st.button("Clear Cart"):
#         st.session_state["cart"].clear()
#         st.success("Cart cleared!")

#     # Create and display a DataFrame of selected items
#     st.subheader("Selected Items DataFrame:")
#     cart_df = pd.DataFrame({"Selected Items": st.session_state["cart"]})
#     st.dataframe(cart_df)
# else:
#     st.write("Your cart is empty.")

# #Option to add items manually (optional, for testing)
# if st.session_state["dataframe"] is not None and "product" in st.session_state["dataframe"].columns:
#     product_list = st.session_state["dataframe"]["product"].tolist()
#     selected_product = st.selectbox("Select a product to add to cart:", product_list)

#     if st.button("Add to Cart"):
#         st.session_state["cart"].append(selected_product)
#         st.success(f"{selected_product} added to cart!")


def display_sidebar():
    st.title("Shopping Cart")
    
    # Check if a DataFrame exists and has a "product" column
    if st.session_state["dataframe"] is not None and "product" in st.session_state["dataframe"].columns:
        # Get the list of products from the DataFrame
        product_list = st.session_state["dataframe"]["product"].tolist()
        
        # Select box for products
        selected_product = st.selectbox("Select a product to add to cart:", product_list)
        
        # Button to add the selected product to the cart
        if st.button("Add to Cart"):
            st.session_state["cart"].append(selected_product)
            st.success(f"{selected_product} added to cart!")
    else:
        st.write("No products available.")

    # Display the cart items
    if st.session_state["cart"]:
        st.subheader("Cart Items:")
        for item in st.session_state["cart"]:
            st.markdown(f"- {item}")
        
        # Add a button to clear the cart
        if st.button("Clear Cart"):
            st.session_state["cart"].clear()
            st.success("Cart cleared!")

        # Create and display a DataFrame of selected items
        st.subheader("Selected Items DataFrame:")
        cart_df = pd.DataFrame({"Selected Items": st.session_state["cart"]})
        st.dataframe(cart_df)
    else:
        st.write("Cart is empty.")

display_sidebar()