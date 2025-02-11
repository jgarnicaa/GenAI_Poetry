from fastapi import FastAPI
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

app=FastAPI()

model_path="path_to_MLFlow_model"
model=GPT2LMHeadModel.from_pretrained(model_path)
tokenizer=GPT2Tokenizer.from_pretrained(model_path)

@app.post("/generate/")
def generate_poem(prompt: str, max_length: int=100):
    input_id=tokenizer.encode(prompt, return_tensors="pt")

    output=model.generate(
        input_id,
        max_length=max_length,
        num_return_sequences=1, #How many poems we want?
        temperature=0.7, ## Randomize generation all text (>1 and <0.5)
        top_p=0.9, ##Cut word less probable to apper, keep coherence
        do_sample=True
        )
    
    poem=tokenizer.decode(output[0]) #skip_special_tokens=True
    
    return {"poem": poem}