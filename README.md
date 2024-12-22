# Chatbot-Powered Recommender System
======================================
## Overview
------------
This project leverages the output of Large Language Models (LLMs) to power a recommender system. Specifically, we use the LLM's response to a "recipe" query to extract ingredients and perform similarity searches, recommending relevant products from vector databases.
## Architecture
---------------
LLM Querying: Send a recipe query to an LLM (e.g., ChatGPT).\
Ingredient Extraction: Extract ingredients from the LLM's response.\
Similarity Search: Perform similarity searches on a Faiss database to find relevant ingredients.\
Recommendation Generation: Return a dataframe of recommended ingredients from the csv file of products which has more info on the items
## Motivation
------------
As users increasingly rely on chatbots like ChatGPT and Meta for solutions, this project explores the potential of utilizing chatbot outputs to drive recommender systems. By tapping into the conversational AI ecosystem, we can create more personalized and context-aware recommendations.
## Features
------------
LLM Integration: Seamlessly integrates with LLMs to leverage their output.
![flower](https://github.com/user-attachments/assets/b5d7e0bf-3f23-4f15-a3d5-cb6fc2903ec3)

Ingredient Extraction: Accurately extracts ingredients from LLM responses.
Similarity Search: Efficiently performs similarity searches using Faiss.
Personalized Recommendations: Generates relevant and personalized recommendations.
## Requirements
---------------
Python 3.x
-Faiss library
-LLM API access (here we have used groqAPI)
-huggingface embeddings
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
