# Feature Specification: Crypto DEX API Microservice

**Feature Branch**: `001-crypto-dex-api`  
**Created**: 2025-11-04  
**Status**: Draft  
**Input**: User description: "Create a microservice server which allow user to use standard api call to interact with major crypto dex like hyperliquid, lighter, drift protocol. create a set of abstract method to allow future feature extensibility."

## User Scenarios & Testing *(mandatory)*

### User Story 1 - Retrieve aggregated price data (Priority: P1)

As a trader, I want to retrieve real-time price data for a specific trading pair from multiple DEXs (Hyperliquid, Lighter, Drift) through a single API call, so that I can easily compare prices and find the best rate.

**Why this priority**: This is the core value proposition, providing a unified view of the market.
**Independent Test**: Can be tested by calling a single API endpoint with a trading pair and verifying that a consolidated response with data from all supported DEXs is returned.
**Acceptance Scenarios**:
1. **Given** a user is authenticated, **When** they request the price for "BTC/USD", **Then** the system returns a JSON object containing price quotes from Hyperliquid, Lighter, and Drift.
2. **Given** a user requests a trading pair not supported by a specific DEX, **When** the price is requested, **Then** the system returns prices from the DEXs that do support it and indicates which DEXs do not.

---

### User Story 2 - Place a Spot Order (Priority: P2)

As a trading bot developer, I want to execute a spot market order on a specific DEX using a standardized API format, so that I don't have to write and maintain custom integration code for each exchange.

**Why this priority**: Enables basic transactional capabilities.
**Independent Test**: Can be tested by sending a standardized spot order request to the API for a specific DEX and verifying that the order is successfully placed.
**Acceptance Scenarios**:
1. **Given** a user is authenticated and has sufficient funds, **When** they submit a spot market order to buy 0.1 BTC on Hyperliquid, **Then** the order is executed on Hyperliquid and a confirmation is returned.

---

### User Story 3 - Place a Perp Order (Priority: P3)

As a derivatives trader, I want to place a perpetual futures order with leverage on a specific DEX, so that I can execute more advanced trading strategies.

**Why this priority**: Adds support for a major class of financial instruments in the crypto space.
**Independent Test**: Can be tested by sending a standardized perpetual order request (including leverage) and verifying it is placed successfully on the target DEX.
**Acceptance Scenarios**:
1. **Given** a user is authenticated, **When** they submit a perpetual market order to long 1 ETH with 10x leverage on Drift, **Then** the order is executed on Drift and a confirmation is returned.

---

### User Story 4 - Place Multiple Orders (Priority: P4)

As a sophisticated trading firm, I want to place multiple orders across different DEXs and pairs in a single API call, so that I can execute complex strategies with low latency.

**Why this priority**: Provides a high-performance feature for advanced users.
**Independent Test**: Can be tested by sending a batch order request and verifying that all individual orders are placed successfully on their respective DEXs.
**Acceptance Scenarios**:
1. **Given** a user is authenticated, **When** they submit a batch request containing a spot order for BTC on Hyperliquid and a perp order for ETH on Drift, **Then** both orders are executed and a consolidated confirmation is returned.

---

### User Story 5 - View consolidated account balances (Priority: P5)

As a portfolio manager, I want to query my account balances across multiple DEXs with a single API call, so that I can get a quick, consolidated view of my total assets.

**Why this priority**: Provides essential portfolio management functionality.
**Independent Test**: Can be tested by calling an API endpoint and verifying that it returns a list of assets and their balances from all configured DEXs.
**Acceptance Scenarios**:
1. **Given** a user has configured API keys for Hyperliquid and Drift, **When** they request their balances, **Then** the system returns a combined list of all assets held on both exchanges.

---

### Edge Cases

- What happens when a downstream DEX API is unavailable or returns an error?
- How does the system handle API rate limiting from the underlying DEXs?
- What is the behavior for trading pairs with different naming conventions across exchanges?
- How are partial successes handled in batch order requests?

## Requirements *(mandatory)*

### Functional Requirements

- **FR-001**: The system MUST provide a unified API endpoint to fetch price quotes.
- **FR-002**: The system MUST provide a unified API endpoint to submit spot and perpetual orders.
- **FR-003**: The system MUST provide a unified API endpoint to submit a batch of multiple orders.
- **FR-004**: The system MUST provide a unified API endpoint to fetch account balances.
- **FR-005**: The system MUST include an abstraction layer that allows adding new DEX integrations.
- **FR-006**: The system MUST authenticate and authorize all API requests via API Keys.
- **FR-007**: The system MUST provide clear error messages.

### Key Entities *(include if feature involves data)*

- **DEX Connection**: Represents the configuration and credentials for connecting to a single DEX.
- **Trading Pair**: Represents a pair of assets to be traded.
- **Price Quote**: Represents the current price for a trading pair on a specific DEX.
- **Order**: Represents a request to buy or sell an asset. It MUST include `order_type` ('spot' or 'perp') and may include other fields like `leverage`.
- **Account Balance**: Represents the quantity of a specific asset held by a user on a DEX.

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: Aggregated price quote requests MUST complete in under 500ms.
- **SC-002**: Single trade execution requests MUST be acknowledged by the target DEX within 1 second.
- **SC-003**: Batch order requests of up to 10 orders MUST complete in under 2 seconds.
- **SC-004**: The API MUST maintain 99.9% uptime.
- **SC-005**: A new DEX integration can be developed and deployed in under 2 developer-weeks.
- **SC-006**: The system MUST be able to handle 100 concurrent API requests without performance degradation.
