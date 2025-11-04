# Omni Crypto DEX API

This is a Flask-based API that provides a unified interface to interact with multiple decentralized exchanges (DEXs).

## Features

- **Aggregated Price Data**: Get a consolidated price view from all supported DEXs.
- **Spot and Perpetual Orders**: Place spot and perpetual futures orders on a specific DEX.
- **Batch Orders**: Place multiple orders in a single API call.
- **Order Cancellation**: Cancel an open order on a specific DEX.
- **Consolidated Balances**: View your asset balances across all connected DEXs.

## Setup

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   cd omni-crypto-dex
   ```

2. **Create a virtual environment and activate it**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install the dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**:
   ```bash
   python init_db.py
   ```

5. **Run the application**:
   ```bash
   flask run
   ```

## API Endpoints

- `GET /prices?symbol=<symbol>`: Retrieve aggregated price data for a given symbol.
- `POST /orders`: Place a spot or perpetual order.
- `POST /orders/batch`: Place multiple orders in a single API call.
- `POST /orders/<dex_name>/<order_id>/cancel`: Cancel an open order.
- `GET /balances`: View your consolidated account balances.

## Running Tests

To run the tests, use the following command:

```bash
pytest
```
