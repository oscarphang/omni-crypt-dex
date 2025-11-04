# Data Model: Crypto DEX API Microservice

This document outlines the data entities for the microservice. Based on the requirement that this service will not have its own user module, authentication will be handled by API clients.

## 1. ApiClient

Represents a client of our API, identified by an API key.

- **id**: `INTEGER` (Primary Key)
- **api_key**: `TEXT` (Unique, Indexed) - The API key used to authenticate to this service.
- **description**: `TEXT` (Optional, e.g., "Trading Bot A")
- **created_at**: `DATETIME`

## 2. DexConnection

Stores the encrypted API credentials for a specific `ApiClient` to connect to a single DEX.

- **id**: `INTEGER` (Primary Key)
- **api_client_id**: `INTEGER` (Foreign Key to ApiClient.id)
- **dex_name**: `TEXT` (e.g., "hyperliquid", "lighter", "drift")
- **encrypted_credentials**: `TEXT` - The client's API key/secret for the DEX, encrypted.
- **created_at**: `DATETIME`

*Note: An `ApiClient` can have multiple `DexConnection` entries, one for each DEX they wish to connect to.*
