import requests
from tabulate import tabulate
from colorama import Fore, Style, init

# Αρχικοποίηση χρωμάτων
init(autoreset=True)

def get_crypto_prices():
    # Ορίζουμε το νόμισμα
    curr = 'eur' 
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        'ids': 'bitcoin,ethereum,cardano,solana,ripple',
        'vs_currencies': curr,
        'include_24hr_change': 'true'
    }
    
    try:
        response = requests.get(url, params=params)
        data = response.json()
        
        table_data = []
        for coin, info in data.items():
            # Εδώ ήταν το λάθος! Τώρα χρησιμοποιούμε το δυναμικό 'curr'
            price_val = info[curr]
            change_val = info[f'{curr}_24h_change']
            
            price_str = f"€{price_val:,}"
            
            color = Fore.GREEN if change_val > 0 else Fore.RED
            formatted_change = f"{color}{change_val:.2f}%{Style.RESET_ALL}"
            
            table_data.append([coin.capitalize(), price_str, formatted_change])
            
        return table_data
    except Exception as e:
        return f"Error fetching data: {e}"

def main():
    print(f"{Fore.CYAN}{Style.BRIGHT}--- Live Crypto Market Tracker (EUR) ---")
    print("Fetching latest prices...\n")
    
    prices = get_crypto_prices()
    
    if isinstance(prices, list):
        # Άλλαξα και το header να λέει Price (EUR)
        headers = [f"{Fore.YELLOW}Asset", f"{Fore.YELLOW}Price (EUR)", f"{Fore.YELLOW}24h Change"]
        print(tabulate(prices, headers=headers, tablefmt="fancy_grid"))
    else:
        print(prices)

if __name__ == "__main__":
    main()