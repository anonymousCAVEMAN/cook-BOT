import os
import json
import pickle
import re
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel
from langchain.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.prompts import ChatPromptTemplate

from dotenv import load_dotenv
load_dotenv()
os.environ['HF_TOKEN']=os.getenv("HF_TOKEN")
embeddings=HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
groq_api_key=os.getenv("GROQ_API_KEY")
llm=ChatGroq(groq_api_key=groq_api_key,model_name="llama-3.1-70b-versatile")

df = pd.read_csv('E:\\python\\2.PROJECTS\\cook_bot\\artifacts\\filtered_df.csv')
# load 
db_load = FAISS.load_local(folder_path="artifacts",index_name="products",allow_dangerous_deserialization=True,embeddings=embeddings)

app = FastAPI()

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", '''
     "u are a helpful ai assitant, provide "
     "name": "Recipe Name",
            "ingredients": ["Ingredient 1", "Ingredient 2"] ,
            "items" :["Ingredient 1", "Ingredient 2"] provide without quantity,dont mess up all-purpose flour with flour,also vegtables like lemon need not be mentioned as lemon juice)
            "instructions": "Step-by-step instructions.",
            "prep_time": as suggested
     instructions and ingredients to cook a recipe strictly in json format '''),
    ("human", "{input}")
])

from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Message(BaseModel):
    message: str

with open("artifacts/corpus.pkl", "rb") as file:
    corpus = pickle.load(file)

def json_response(response):
        json_match = re.search(r"{.*}", response, re.DOTALL)
        if json_match:
                cleaned_output = json_match.group()
                recipe = json.loads(cleaned_output)
                print("Parsed Recipe:", recipe)
        else:
                print("No JSON found!") 
        return recipe

def item_search(items):
    df_list = []
    for item in items:
        a=db_load.similarity_search_with_relevance_scores(item,k=1)
        page_content = a[0][0].page_content
        score = a[0][1]
        if score >0.66:
            b = corpus.index(page_content)
            df_list.append(b)
    return df_list

@app.post("/chat")
async def chat_with_llm(message: Message):
    chain = qa_prompt | llm 
    result1 = chain.invoke({"input":message})
    response = result1.content
    recipe = json_response(response)
    ingredients = recipe.get('ingredients')
    df_list = item_search(ingredients)
    dataframe = df.loc[df_list]
    # df_dict = dataframe.to_dict()
    df_dict = dataframe.to_json(orient="records")
    # return {"reply": recipe,"ingredients":ingredients,"df_list":df_list}
    return {"reply": recipe,"ingredients":ingredients,"df_list":df_list,"df_dict":df_dict}

