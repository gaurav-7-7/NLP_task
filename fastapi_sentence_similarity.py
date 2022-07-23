from fastapi import FastAPI, Form

app = FastAPI()

@app.get("/login")
async def login(username: str = Form(), password: str = Form()):
    return {"username": username} 