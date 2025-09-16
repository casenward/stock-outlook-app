from fastapi import FastAPI
from routes import stock_routes

app = FastAPI(
    title="Stock Consensus App",
    description="API that aggregates analyst ratings from multiple sources",
    version="1.0.0"
)

# Register routes
app.include_router(stock_routes.router, prefix="/api", tags=["Stocks"])

@app.get("/health")
def health_check():
    return {"status": "ok"}

