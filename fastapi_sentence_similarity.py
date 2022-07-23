from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class s(BaseModel):
    s1 : str
    s2 : str

from sentence_transformers import SentenceTransformer
from sklearn.metric.pairwise import consine_similarity

model = SentenceTransformer('bert-base-nli-mean-tokens')

@app.post("/check_similarity")
async def check_similarity(string : s):
    return ({"score": str(consine_similarity([model.encode(string.s1), model.encode(string.s1)]))})
    
    
"""
  feeding the below json file to the api we get the similarity score
 {
  "s1": "Sentences are passed as a list of string.",
  "s2": "The quick brown fox jumps over the lazy dog."
 }
"""