# Quickstart: Crypto DEX API

This guide will help you get started with the Crypto DEX API.

## 1. Getting an API Key

First, you will need an API key to authenticate your requests.

*(This section would typically detail the process of signing up and generating a key, which is out of scope for this document).*

All requests must include your API key in the `X-API-KEY` header.

## 2. Connecting Your DEX Accounts

Before you can trade or view balances, you need to add the API credentials for your accounts on the supported DEXs. This is done via a separate administrative process (or a future API endpoint).

## 3. API Endpoints

### Get Prices

- **Endpoint**: `GET /prices`
- **Query Parameter**: `pair` (e.g., `BTC-USD`)
- **Description**: Retrieves the latest price for a trading pair from all supported DEXs.

**Example:**
```bash
curl -X GET "https://api.example.com/prices?pair=BTC-USD" \
     -H "X-API-KEY: YOUR_API_KEY"
```

### Place an Order

- **Endpoint**: `POST /orders`
- **Body**: JSON object with `dex`, `pair`, `side` (`buy` or `sell`), and `amount`.
- **Description**: Executes a market order on the specified DEX.

**Example:**
```bash
curl -X POST "https://api.example.com/orders" \
     -H "X-API-KEY: YOUR_API_KEY" \
     -H "Content-Type: application/json" \
     -d 
{
           "dex": "hyperliquid",
           "pair": "BTC-USD",
           "side": "buy",
           "amount": 0.1
         }
```

### Get Balances

- **Endpoint**: `GET /balances`
- **Query Parameter**: `dex` (optional, e.g., `drift`)
- **Description**: Retrieves your account balances. If `dex` is specified, it returns balances for that DEX only. Otherwise, it returns balances from all connected DEXs.

**Example:**
```bash
curl -X GET "https://api.example.com/balances" \
     -H "X-API-KEY: YOUR_API_KEY"
```
