from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

app = FastAPI()

# Serve frontend from public folder
app.mount("/", StaticFiles(directory="public", html=True), name="public")
