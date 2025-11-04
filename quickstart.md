# Quickstart

This guide provides a few `curl` examples to get you started with the Omni Crypto DEX API.

## Get Aggregated Prices

```bash
curl "http://127.0.0.1:5000/prices?symbol=BTC-USD"
```

## Place a Spot Order

```bash
curl -X POST -H "Content-Type: application/json" -d '{
    "dex": "hyperliquid",
    "symbol": "BTC-USD",
    "side": "buy",
    "type": "spot",
    "quantity": 0.1
}' "http://127.0.0.1:5000/orders"
```

## Place a Batch Order

```bash
curl -X POST -H "Content-Type: application/json" -d '[
    {
        "dex": "hyperliquid",
        "symbol": "BTC-USD",
        "side": "buy",
        "type": "spot",
        "quantity": 0.1
    },
    {
        "dex": "drift",
        "symbol": "BTC-PERP",
        "side": "buy",
        "type": "perp",
        "quantity": 1
    }
]' "http://127.0.0.1:5000/orders/batch"
```

## Cancel an Order

```bash
curl -X POST "http://127.0.0.1:5000/orders/hyperliquid/hyper_spot_123/cancel"
```

## Get Consolidated Balances

```bash
curl "http://127.0.0.1:5000/balances"
```
