from fastapi import FastAPI
from backend.routes import stock_routes

# Create the FastAPI app
app = FastAPI(
    title="Stock Consensus App",
    description="API that aggregates analyst ratings from multiple sources",
    version="1.0.0"
)

# Include routers
app.include_router(stock_routes.router, prefix="/api", tags=["Stocks"])

# Optional: health check endpoint
@app.get("/health")
def health_check():
    return {"status": "ok"}
