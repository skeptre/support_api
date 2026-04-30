from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@app.get("/")
def root():
    return {"message": "Hello World"}

app.include_router(router)