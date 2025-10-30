# btc_sim.py — simple live-price simulator + CLI trading
import requests, time, csv, argparse
from datetime import datetime, timezone

API = "https://api.coingecko.com/api/v3/simple/price"
SYMBOL = "bitcoin"
VS_CURRENCY = "usd"
LOG_CSV = "trades_and_prices.csv"

class Portfolio:
    def __init__(self, cash=10000.0):
        self.cash = float(cash)
        self.btc = 0.0

    def buy(self, price, usd):
        usd = min(usd, self.cash)
        qty = usd / price
        self.btc += qty
        self.cash -= usd
        return qty

    def sell(self, price, btc_qty):
        btc_qty = min(btc_qty, self.btc)
        self.btc -= btc_qty
        self.cash += btc_qty * price
        return btc_qty

    def value(self, price):
        return self.cash + self.btc * price

def fetch_price():
    r = requests.get(API, params={"ids": SYMBOL, "vs_currencies": VS_CURRENCY}, timeout=10)
    r.raise_for_status()
    return float(r.json()[SYMBOL][VS_CURRENCY])

def append_log(row):
    header = ["timestamp","price","cash","btc","action","amount"]
    try:
        with open(LOG_CSV, "r"):
            pass
    except FileNotFoundError:
        with open(LOG_CSV, "w", newline="") as f:
            csv.writer(f).writerow(header)
    with open(LOG_CSV, "a", newline="") as f:
        csv.writer(f).writerow(row)

def repl(portfolio, polling=10):
    print("Commands: buy <usd>, sell <btc>, show, wait <seconds>, exit, auto <simple_strategy>")
    while True:
        cmd = input(">> ").strip().split()
        if not cmd:
            continue
        op = cmd[0].lower()
        try:
            if op == "buy":
                usd = float(cmd[1])
                price = fetch_price()
                qty = portfolio.buy(price, usd)
                ts = datetime.now(timezone.utc).isoformat()
                print(f"[{ts}] Bought {qty:.6f} BTC @ {price:.2f} USD")
                append_log([ts, price, portfolio.cash, portfolio.btc, "buy", usd])
            elif op == "sell":
                btc = float(cmd[1])
                price = fetch_price()
                qty = portfolio.sell(price, btc)
                ts = datetime.now(timezone.utc).isoformat()
                print(f"[{ts}] Sold {qty:.6f} BTC @ {price:.2f} USD")
                append_log([ts, price, portfolio.cash, portfolio.btc, "sell", btc])
            elif op == "show":
                price = fetch_price()
                print(f"Price: {price:.2f} USD | Cash: {portfolio.cash:.2f} | BTC: {portfolio.btc:.6f} | Net: {portfolio.value(price):.2f}")
            elif op == "wait":
                s = int(cmd[1]) if len(cmd) > 1 else polling
                print(f"Waiting {s}s...")
                time.sleep(s)
            elif op == "auto":
                # super-simple auto: buy $100 when price down 1% vs last check, sell all when up 1%
                print("Auto mode. Ctrl+C to stop.")
                last = fetch_price()
                while True:
                    time.sleep(polling)
                    price = fetch_price()
                    change = (price - last) / last
                    if change <= -0.01:
                        portfolio.buy(price, 100)
                        ts = datetime.now(timezone.utc).isoformat()
                        append_log([ts, price, portfolio.cash, portfolio.btc, "auto_buy", 100])
                        print(f"[{ts}] auto_buy $100 @ {price:.2f}")
                    elif change >= 0.01 and portfolio.btc > 0:
                        qty = portfolio.btc
                        portfolio.sell(price, qty)
                        ts = datetime.now(timezone.utc).isoformat()
                        append_log([ts, price, portfolio.cash, portfolio.btc, "auto_sell", qty])
                        print(f"[{ts}] auto_sell {qty:.6f} BTC @ {price:.2f}")
                    last = price
            elif op == "exit":
                print("Bye.")
                break
            else:
                print("Unknown command.")
        except Exception as e:
            print("Error:", e)

if __name__ == "__main__":
    p = Portfolio(cash=10000)
    print("BTC trading simulator — starting portfolio $10,000")
    repl(p)
