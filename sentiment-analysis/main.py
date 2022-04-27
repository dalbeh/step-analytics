from fastapi import FastAPI
import predict


app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Call /sentiment/$(word)"}


@app.get("/sentiment/{word}")
async def sentiment(word: str):
    result = predict.main(word) 
    return {"text": word.replace('+',' '), "result": result}