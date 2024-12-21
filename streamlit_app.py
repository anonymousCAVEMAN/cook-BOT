
# import streamlit as st
# import requests
# import pandas as pd


# # Set the FastAPI endpoint
# API_ENDPOINT = "http://localhost:8000/chat"  # Replace with your FastAPI endpoint

# # Streamlit app configuration
# st.set_page_config(page_title="Chat with LLM", layout="centered")

# # App title
# st.title("Chat with Your LLM")

# # Initialize session state to store chat history
# if "messages" not in st.session_state:
#     st.session_state["messages"] = []

# # Display chat history
# def display_chat():
#     for i, msg in enumerate(st.session_state["messages"]):
#         if msg["sender"] == "user":
#             st.markdown(f"**You:** {msg['content']}")
#         else:
#             st.markdown(f"**LLM:** {msg['content']}")

# # Input area
# with st.form(key="chat_form"):
#     user_input = st.text_input("Type your message:", key="input_field")
#     submit_button = st.form_submit_button(label="Send")

# # Handle user input
# if submit_button and user_input.strip():
#     # Add user message to chat history
#     st.session_state["messages"].append({"sender": "user", "content": user_input})

#     # Send message to FastAPI
#     try:
#         response = requests.post(API_ENDPOINT, json={"message": user_input})
        
#         # Check if the API call was successful
#         if response.status_code == 200:
#             # Parse the JSON response
#             result = response.json()  # Convert response to a dictionary
            
#             # Extract data from the response
#             llm_reply = result.get("reply", {})
#             ingredients = result.get("ingredients", [])
#             df_list = result.get("df_list", [])
#             df_dict = result.get("df_dict", {})

#             df = pd.read_json(df_dict, orient="records")
#             st.dataframe(df)

#             recipe_name = llm_reply.get("name", "Unknown")
#             instructions = llm_reply.get("instructions", "No instructions provided.")
#             ingredients = llm_reply.get("ingredients", [])
#             items = llm_reply.get("items", [])

#             # Add LLM response to chat history
#             st.session_state["messages"].append({
#                 "sender": "llm",
#                 "content": f"**Recipe Name:** {recipe_name}\n\n"
#                            f"**Instructions:** {instructions}\n\n"
#                            f"**Ingredients:** {', '.join(ingredients)}\n\n"
#                            f"**Items Needed:** {', '.join(items)}\n\n"
                           
#             })
#         else:
#             st.session_state["messages"].append({
#                 "sender": "llm",
#                 "content": f"Error: Unable to fetch response. Status code {response.status_code}."
#             })
#     except Exception as e:
#         st.session_state["messages"].append({
#             "sender": "llm",
#             "content": f"Error: {str(e)}"
#         })

# # Display updated chat history
# display_chat()


#######################################################################################################################

# import streamlit as st
# import requests
# import pandas as pd

# # Set the FastAPI endpoint
# API_ENDPOINT = "http://localhost:8000/chat"  # Replace with your FastAPI endpoint

# # Streamlit app configuration
# st.set_page_config(page_title="Chat with LLM", layout="centered")

# # App title
# st.title("Chat with Your LLM")

# # Initialize session state to store chat history and DataFrame
# if "messages" not in st.session_state:
#     st.session_state["messages"] = []

# if "dataframe" not in st.session_state:
#     st.session_state["dataframe"] = None  # Initialize with None

# # Display chat history
# def display_chat():
#     for i, msg in enumerate(st.session_state["messages"]):
#         if msg["sender"] == "user":
#             st.markdown(f"**You:** {msg['content']}")
#         else:
#             st.markdown(f"**LLM:** {msg['content']}")

#     # Display DataFrame if available
#     if st.session_state["dataframe"] is not None:
#         st.markdown("### Related Items (DataFrame)")
#         st.dataframe(st.session_state["dataframe"])

# # Input area
# with st.form(key="chat_form"):
#     user_input = st.text_input("Type your message:", key="input_field")
#     submit_button = st.form_submit_button(label="Send")

# # Handle user input
# if submit_button and user_input.strip():
#     # Add user message to chat history
#     st.session_state["messages"].append({"sender": "user", "content": user_input})

#     # Send message to FastAPI
#     try:
#         response = requests.post(API_ENDPOINT, json={"message": user_input})
        
#         # Check if the API call was successful
#         if response.status_code == 200:
#             # Parse the JSON response
#             result = response.json()  # Convert response to a dictionary
            
#             # Extract data from the response
#             llm_reply = result.get("reply", {})
#             ingredients = result.get("ingredients", [])
#             df_dict = result.get("df_dict", {})

#             # Convert the received df_dict to a Pandas DataFrame and store in session state
#             if df_dict:
#                 st.session_state["dataframe"] = pd.read_json(df_dict, orient="records")
#             else:
#                 st.session_state["dataframe"] = None

#             recipe_name = llm_reply.get("name", "Unknown")
#             instructions = llm_reply.get("instructions", "No instructions provided.")
#             ingredients = llm_reply.get("ingredients", [])
#             items = llm_reply.get("items", [])

#             # Add LLM response to chat history
#             st.session_state["messages"].append({
#                 "sender": "llm",
#                 "content": f"**Recipe Name:** {recipe_name}\n\n"
#                            f"**Instructions:** {instructions}\n\n"
#                            f"**Ingredients:** {', '.join(ingredients)}\n\n"
#                            f"**Items Needed:** {', '.join(items)}"
#             })
#         else:
#             st.session_state["messages"].append({
#                 "sender": "llm",
#                 "content": f"Error: Unable to fetch response. Status code {response.status_code}."
#             })
#     except Exception as e:
#         st.session_state["messages"].append({
#             "sender": "llm",
#             "content": f"Error: {str(e)}"
#         })

# # Display updated chat history
# display_chat()

#######################################################################################################################

import streamlit as st
import requests
import pandas as pd

# Set the FastAPI endpoint
API_ENDPOINT = "http://localhost:8000/chat"  # Replace with your FastAPI endpoint

# Streamlit app configuration
st.set_page_config(page_title="Chat with LLM", layout="centered")

# App title
st.title("Chat with Your LLM")

# Initialize session state to store chat history, DataFrame, and cart
if "messages" not in st.session_state:
    st.session_state["messages"] = []

if "dataframe" not in st.session_state:
    st.session_state["dataframe"] = None  # Initialize with None

if "cart" not in st.session_state:
    st.session_state["cart"] = []  # Initialize an empty cart

# Sidebar function
def display_sidebar():
    st.sidebar.title("Shopping Cart")
    
    # Check if a DataFrame exists and has a "product" column
    if st.session_state["dataframe"] is not None and "product" in st.session_state["dataframe"].columns:
        # Get the list of products from the DataFrame
        product_list = st.session_state["dataframe"]["product"].tolist()
        
        # Select box for products
        selected_product = st.sidebar.selectbox("Select a product to add to cart:", product_list)
        
        # Button to add the selected product to the cart
        if st.sidebar.button("Add to Cart"):
            st.session_state["cart"].append(selected_product)
            st.sidebar.success(f"{selected_product} added to cart!")
    else:
        st.sidebar.write("No products available.")

    # Display the cart items
    if st.session_state["cart"]:
        st.sidebar.subheader("Cart Items:")
        for item in st.session_state["cart"]:
            st.sidebar.markdown(f"- {item}")
        
        # Add a button to clear the cart
        if st.sidebar.button("Clear Cart"):
            st.session_state["cart"].clear()
            st.sidebar.success("Cart cleared!")

        # Create and display a DataFrame of selected items
        st.sidebar.subheader("Selected Items DataFrame:")
        cart_df = pd.DataFrame({"Selected Items": st.session_state["cart"]})
        st.sidebar.dataframe(cart_df)
    else:
        st.sidebar.write("Cart is empty.")

# Display chat history
def display_chat():
    # Display DataFrame if available
    if st.session_state["dataframe"] is not None:
        st.markdown("### Related Items (DataFrame)")
        st.dataframe(st.session_state["dataframe"])
    
    # Reverse the order of messages to show the latest first
    for i, msg in reversed(list(enumerate(st.session_state["messages"]))):
        if msg["sender"] == "user":
            st.markdown(f"**You:** {msg['content']}")
        else:
            st.markdown(f"**LLM:** {msg['content']}")

# Input area
with st.form(key="chat_form"):
    user_input = st.text_input("Type your message:", key="input_field")
    submit_button = st.form_submit_button(label="Send")

# Handle user input
if submit_button and user_input.strip():
    # Add user message to chat history
    st.session_state["messages"].append({"sender": "user", "content": user_input})

    # Send message to FastAPI
    try:
        response = requests.post(API_ENDPOINT, json={"message": user_input})
        
        # Check if the API call was successful
        if response.status_code == 200:
            # Parse the JSON response
            result = response.json()  # Convert response to a dictionary
            
            # Extract data from the response
            llm_reply = result.get("reply", {})
            ingredients = result.get("ingredients", [])
            df_dict = result.get("df_dict", {})

            # Convert the received df_dict to a Pandas DataFrame and store in session state
            if df_dict:
                st.session_state["dataframe"] = pd.read_json(df_dict, orient="records")
            else:
                st.session_state["dataframe"] = None

            recipe_name = llm_reply.get("name", "Unknown")
            instructions = llm_reply.get("instructions", "No instructions provided.")
            ingredients = llm_reply.get("ingredients", [])
            items = llm_reply.get("items", [])

            # Add LLM response to chat history
            st.session_state["messages"].append({
                "sender": "llm",
                "content": f"**Recipe Name:** {recipe_name}\n\n"
                           f"**Instructions:** {instructions}\n\n"
                           f"**Ingredients:** {', '.join(ingredients)}\n\n"
                           f"**Items Needed:** {', '.join(items)}"
            })
        else:
            st.session_state["messages"].append({
                "sender": "llm",
                "content": f"Error: Unable to fetch response. Status code {response.status_code}."
            })
    except Exception as e:
        st.session_state["messages"].append({
            "sender": "llm",
            "content": f"Error: {str(e)}"
        })

# Display updated chat history
display_chat()

# Display the sidebar
display_sidebar()
