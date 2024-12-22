# Chatbot-Powered Recommender System
======================================
## Overview
------------
This project leverages the output of Large Language Models (LLMs) like ChatGPT to power a recommender system. Specifically, we use the LLM's response to a recipe query to extract ingredients and perform similarity searches, recommending relevant products.
## Architecture
---------------
LLM Querying: Send a recipe query to an LLM (e.g., ChatGPT).
Ingredient Extraction: Extract ingredients from the LLM's response.
Similarity Search: Perform similarity searches on a Faiss database to find relevant ingredients.
Recommendation Generation: Return a dataframe of recommended ingredients.
## Motivation
------------
As users increasingly rely on chatbots like ChatGPT and Meta for solutions, this project explores the potential of utilizing chatbot outputs to drive recommender systems. By tapping into the conversational AI ecosystem, we can create more personalized and context-aware recommendations.
## Features
------------
LLM Integration: Seamlessly integrates with LLMs to leverage their output.
Ingredient Extraction: Accurately extracts ingredients from LLM responses.
Similarity Search: Efficiently performs similarity searches using Faiss.
Personalized Recommendations: Generates relevant and personalized recommendations.
## Requirements
---------------
Python 3.x
Faiss library
LLM API access (e.g., ChatGPT API)
## Future Work
--------------
Expand to Multiple LLMs: Integrate with multiple LLMs to increase robustness.
Improve Ingredient Extraction: Enhance ingredient extraction accuracy using NLP techniques.
Enhance Recommendation Algorithm: Explore more advanced recommendation algorithms.
## Contributing
------------
Contributions are welcome! Please submit issues or pull requests.
## License
-------
This project is licensed under .
Feel free to modify this template to better suit your project's needs. Good luck with your project!
