from fastapi import FastAPI, File, UploadFile, Form
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from app.api import endpoints
from uvicorn import run

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(endpoints.router)

app.mount("/static", StaticFiles(directory="static"), name="static")

if __name__ == "__main__":
    run(app, host="0.0.0.0", port=8007)
