from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes import stock_routes

app = FastAPI()

# ✅ Allow frontend to call backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # for testing, allow all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include your stock routes
app.include_router(stock_routes.router, prefix="/api", tags=["Stocks"])

@app.get("/")
def read_root():
    return {"message": "Stock Consensus API is running"}
