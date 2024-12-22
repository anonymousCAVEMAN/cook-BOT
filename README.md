# Chatbot-Powered Recommender System
======================================
## Overview
------------
This project leverages the output of Large Language Models (LLMs) to power a recommender system. Specifically, we use the LLM's response to a "recipe" query to extract ingredients and perform similarity searches, recommending relevant products from vector databases.
## Architecture
---------------
LLM Querying: Send a recipe query to an LLM .\
Ingredient Extraction: Extract ingredients from the LLM's response.\
Similarity Search: Perform similarity searches on a Faiss database to find relevant ingredients.\
Recommendation Generation: Return a dataframe of recommended ingredients from the csv file of products which has more info on the items
## Motivation
------------
As users increasingly rely on chatbots like ChatGPT and Meta for solutions, this project explores the potential of utilizing chatbot outputs to drive recommender systems. By tapping into the conversational AI ecosystem, we can create more personalized and context-aware recommendations.
## Environment Variables
------------
To run this project, you will need to add the following environment variables to your .env file

`GROQ_API_KEY` for 

`HF_TOKEN` for embeddings

## Features
------------
LLM Integration: Seamlessly integrates with LLMs to leverage their output.
Ingredient Extraction: We have provided prompts to the LLM, the ouput should be strictly in json format providing recipe name, recipe ingredients
Similarity Search: from the above mentioned output the ingredients is a list of items. We perform similarity search on list from the corpus(product names which are fed to the fiass db) and obtain the the dataframe .

https://github.com/user-attachments/assets/5fe1b657-cec4-43cd-a44b-ccf1e54058a3

## Requirements
---------------
-Python 3.x\
-Faiss library\
-LLM API access (here we have used groqAPI)\
-huggingface embeddings
-groqAPI
## Deployment
in command prompt
- to create the fiass DB (it is already created and available in artifacts)
  ```bash
  python src.db_feeder.py
  ```
- for fastapi 
  ```bash
  uvicorn fastapi_app:app --reload
  ```
- for streamlit visualisation
  ```bash
  streamlit run streamlit_app.py
  ```
## Future Work
--------------
Improve Ingredient Extraction: Enhance ingredient extraction accuracy using NLP techniques.
Enhance Recommendation Algorithm: Explore more advanced recommendation algorithms.
create a larger collection of vector dtabases with variety of products and explore recommednind multiple products as per user query.

## License
-------
This project is licensed under .
Feel free to modify this template to better suit your project's needs. Good luck with your project!
