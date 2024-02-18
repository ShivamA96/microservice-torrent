from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import run

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"This is the comment microservice.": "Welcome to the comment microservice."}

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8003)
