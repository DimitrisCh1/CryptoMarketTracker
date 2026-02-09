# Real-Time Crypto Market Tracker

A Python-based tool that fetches live cryptocurrency data using the **CoinGecko API**. It provides a clean, color-coded dashboard directly in the terminal to monitor market trends in real-time.

Key Features
- **Live Market Data:** Fetches real-time prices for Bitcoin, Ethereum, Solana, and more.
- **Currency Support:** Fully configured to display prices in **Euros (€)**.
- **Visual Analytics:** Uses `colorama` for instant visual feedback (Green for 24h gains, Red for losses).
- **Pro Formatting:** Data is structured in professional-grade tables using `tabulate`.
- **API Integration:** Demonstration of REST API handling and JSON data parsing.

Tech Stack
- **Language:** Python 3.11+
- **Libraries:** `requests`, `tabulate`, `colorama`

How to Run
1. Clone this repository to your local machine.
2. Install the necessary dependencies:
   ```bash
   pip install requests tabulate colorama
