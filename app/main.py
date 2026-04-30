from fastapi import FastAPI, APIRouter

app = FastAPI()
router = APIRouter()

@app.get("/")
def home():
    return {"status": "OK"}

@router.get("/health")
def health_check():
    return {"status": "healthy"}

app.include_router(router)