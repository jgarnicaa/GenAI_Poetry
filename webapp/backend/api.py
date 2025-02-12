from fastapi import FastAPI
from pydantic import BaseModel
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch

app=FastAPI()

model=GPT2LMHeadModel.from_pretrained("/app/model/fine-tuned-gpt2-poetry")
tokenizer=GPT2Tokenizer.from_pretrained("gpt2")

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

class PromptInput(BaseModel):
    prompt: str
    max_length: int = 150
    temperature: float=1.2
    top_p: float=0.95

@app.post("/generate/")
def generate_poem(data: PromptInput):

    print("data: ", data )

    input_id=tokenizer.encode(data.prompt, return_tensors="pt").to(device)

    output=model.generate(
        input_id,
        max_length=data.max_length,
        num_return_sequences=1, #How many poems we want?
        temperature=data.temperature, ## Randomize generation all text (>1 and <0.5)
        top_p=data.top_p, ##Cut word less probable to apper, keep coherence
        do_sample=True
        )
    
    poem=tokenizer.decode(output[0], skip_special_tokens=True) 
    
    return {"poem": poem}