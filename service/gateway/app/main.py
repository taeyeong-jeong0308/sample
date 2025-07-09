from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Hello from gateway!"} 


@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/health/live")
async def live_check():
    return {"status": "live"}
