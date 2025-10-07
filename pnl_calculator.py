import requests

def get_current_price(coin_id, vs_currency="usd"):
    """Fetch current coin price from CoinGecko."""
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {"ids": coin_id, "vs_currencies": vs_currency}
    response = requests.get(url, params=params)
    data = response.json()
    return data.get(coin_id, {}).get(vs_currency, None)

def pnl_if_not_sold(buy_price, buy_amount_usd, sell_price, coin_id):
    current_price = get_current_price(coin_id)

    if current_price is None:
        print("❌ Could not fetch current price.")
        return

    tokens = buy_amount_usd / buy_price
    sold_value = tokens * sell_price
    current_value = tokens * current_price

    pnl_sold = sold_value - buy_amount_usd
    pnl_now = current_value - buy_amount_usd
    missed_profit = pnl_now - pnl_sold

    print("📊 Results:")
    print(f"— Token: {coin_id}")
    print(f"— Current price: ${current_price:.4f}")
    print(f"— Tokens bought: {tokens:.2f}")
    print(f"— Profit when sold: ${pnl_sold:.2f}")
    print(f"— Profit if held: ${pnl_now:.2f}")
    print(f"— Missed profit: ${missed_profit:.2f}")

# Example input
buy_price = 0.1
buy_amount_usd = 100
sell_price = 0.377
coin_id = "bitcoin"  # Example: ethereum, solana, etc.

pnl_if_not_sold(buy_price, buy_amount_usd, sell_price, coin_id)
