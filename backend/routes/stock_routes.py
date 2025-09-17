from fastapi import APIRouter
from stock import Stock
from apis.finnhub import get_quote

router = APIRouter()

@router.get("/stock/{symbol}")
def get_stock(symbol: str):
    # Create stock object
    stock = Stock(symbol, "Placeholder Name")  # name could come from API later

    # Fetch price from API
    quote = get_quote(symbol)
    stock.set_price(quote["c"])

    # Return as JSON
    return stock.to_dict()
