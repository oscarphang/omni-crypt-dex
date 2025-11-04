# Tasks: Crypto DEX API Microservice

**Input**: Design documents from `/specs/001-crypto-dex-api/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/

**Tests**: Tests are MANDATORY as per the constitution.

## Format: `[ID] [P?] [Story] Description`

- **[P]**: Can run in parallel
- **[Story]**: Which user story this task belongs to (US1, US2, etc.)

## Path Conventions

- Source code: `src/`
- Tests: `tests/`

---

## Phase 1: Setup (Project Initialization)

- [x] T001 Create project directories: `src/`, `tests/`
- [x] T002 Create `requirements.txt` with Flask, Flask-SQLAlchemy, pytest
- [x] T003 [P] Create basic Flask app in `src/app.py` and config in `src/config.py`
- [x] T004 [P] Configure linting and formatting tools (`ruff`, `black`) in `pyproject.toml`

---

## Phase 2: Foundational (Blocking Prerequisites)

- [x] T005 Configure SQLite database connection in `src/database.py`
- [x] T006 Implement `ApiClient` and `DexConnection` models in `src/models.py`
- [x] T007 Create a script `init_db.py` to initialize the database schema
- [x] T008 Implement API Key authentication decorator in `src/auth.py`
- [x] T009 Create the abstract base class for DEX integrations in `src/dex/abc.py`

---

## Phase 3: User Story 1 - Retrieve aggregated price data (Priority: P1) 🎯 MVP

**Goal**: Allow users to get a consolidated price view from all supported DEXs.
**Independent Test**: Call the `/prices` endpoint and verify a JSON response with quotes from all DEXs.

### Tests for User Story 1 ⚠️
- [x] T010 [P] [US1] Unit test for price aggregation logic in `tests/unit/test_price_service.py`
- [x] T011 [P] [US1] Integration test for the `/prices` endpoint in `tests/integration/test_prices.py`

### Implementation for User Story 1
- [x] T012 [P] [US1] Implement `Hyperliquid` client for `get_price` in `src/dex/hyperliquid.py`
- [x] T013 [P] [US1] Implement `Lighter` client for `get_price` in `src/dex/lighter.py`
- [x] T014 [P] [US1] Implement `Drift` client for `get_price` in `src/dex/drift.py`
- [x] T015 [US1] Implement `PriceService` to fetch and aggregate prices in `src/services/price_service.py`
- [x] T016 [US1] Create the `/prices` endpoint and blueprint in `src/routes/prices.py`

---

## Phase 4: User Story 2 - Place a Spot Order (Priority: P2)

**Goal**: Allow users to place spot market orders on a specific DEX.
**Independent Test**: Call the `/orders` endpoint with `order_type: "spot"` and verify the order is confirmed.

### Tests for User Story 2 ⚠️
- [x] T017 [P] [US2] Unit test for spot order logic in `tests/unit/test_order_service.py`
- [x] T018 [P] [US2] Integration test for the `/orders` endpoint (spot) in `tests/integration/test_orders.py`

### Implementation for User Story 2
- [x] T019 [P] [US2] Extend `Hyperliquid` client for spot orders in `src/dex/hyperliquid.py`
- [x] T020 [P] [US2] Extend `Lighter` client for spot orders in `src/dex/lighter.py`
- [x] T021 [P] [US2] Extend `Drift` client for spot orders in `src/dex/drift.py`
- [x] T022 [US2] Implement `OrderService` to handle spot orders in `src/services/order_service.py`
- [x] T023 [US2] Create the `/orders` endpoint and blueprint in `src/routes/orders.py`

---

## Phase 5: User Story 3 - Place a Perp Order (Priority: P3)

**Goal**: Allow users to place perpetual futures orders on a specific DEX.
**Independent Test**: Call the `/orders` endpoint with `order_type: "perp"` and verify the order is confirmed.

### Tests for User Story 3 ⚠️
- [x] T024 [P] [US3] Unit test for perpetual order logic in `tests/unit/test_order_service.py`
- [x] T025 [P] [US3] Integration test for the `/orders` endpoint (perp) in `tests/integration/test_orders.py`

### Implementation for User Story 3
- [x] T026 [P] [US3] Extend `Hyperliquid` client for perp orders in `src/dex/hyperliquid.py`
- [x] T027 [P] [US3] Extend `Drift` client for perp orders in `src/dex/drift.py`
- [x] T028 [US3] Extend `OrderService` to handle perpetual orders in `src/services/order_service.py`

---

## Phase 6: User Story 4 - Place Multiple Orders (Priority: P4)

**Goal**: Allow users to place multiple orders in a single API call.
**Independent Test**: Call the `/orders/batch` endpoint and verify all orders are confirmed.

### Tests for User Story 4 ⚠️
- [x] T029 [P] [US4] Unit test for batch order logic in `tests/unit/test_order_service.py`
- [x] T030 [P] [US4] Integration test for the `/orders/batch` endpoint in `tests/integration/test_orders.py`

### Implementation for User Story 4
- [x] T031 [US4] Extend `OrderService` to handle batch orders in `src/services/order_service.py`
- [x] T032 [US4] Create the `/orders/batch` endpoint in `src/routes/orders.py`

---

## Phase 7: User Story 6 - Cancel an Order (Priority: P2)

**Goal**: Allow users to cancel an open order on a specific DEX.
**Independent Test**: Call the `/orders/{order_id}/cancel` endpoint and verify the order is confirmed as cancelled.

### Tests for User Story 6 ⚠️
- [x] T044 [P] [US6] Unit test for order cancellation logic in `tests/unit/test_order_service.py`
- [x] T045 [P] [US6] Integration test for the `/orders/{order_id}/cancel` endpoint in `tests/integration/test_orders.py`

### Implementation for User Story 6
- [x] T046 [P] [US6] Extend `Hyperliquid` client for order cancellation in `src/dex/hyperliquid.py`
- [x] T047 [P] [US6] Extend `Lighter` client for order cancellation in `src/dex/lighter.py`
- [x] T048 [P] [US6] Extend `Drift` client for order cancellation in `src/dex/drift.py`
- [x] T049 [US6] Extend `OrderService` to handle order cancellation in `src/services/order_service.py`
- [x] T050 [US6] Create the `/orders/{order_id}/cancel` endpoint in `src/routes/orders.py`

---

## Phase 8: User Story 5 - View consolidated account balances (Priority: P5)

**Goal**: Allow users to view their asset balances across all connected DEXs.
**Independent Test**: Call the `/balances` endpoint and verify a JSON response with all assets.

### Tests for User Story 5 ⚠️
- [x] T033 [P] [US5] Unit test for balance consolidation logic in `tests/unit/test_balance_service.py`
- [x] T034 [P] [US5] Integration test for the `/balances` endpoint in `tests/integration/test_balances.py`

### Implementation for User Story 5
- [x] T035 [P] [US5] Extend `Hyperliquid` client to implement `get_balances` in `src/dex/hyperliquid.py`
- [x] T036 [P] [US5] Extend `Lighter` client to implement `get_balances` in `src/dex/lighter.py`
- [x] T037 [P] [US5] Extend `Drift` client to implement `get_balances` in `src/dex/drift.py`
- [x] T038 [US5] Implement `BalanceService` to fetch and consolidate balances in `src/services/balance_service.py`
- [x] T039 [US5] Create the `/balances` endpoint and blueprint in `src/routes/balances.py`

---

## Phase N: Polish & Cross-Cutting Concerns

- [x] T040 [P] Implement comprehensive error handling and logging across all services.
- [x] T041 [P] Create a `README.md` with detailed setup and usage instructions.
- [x] T042 Validate `quickstart.md` examples against the final implementation.
- [x] T043 Code cleanup and refactoring.