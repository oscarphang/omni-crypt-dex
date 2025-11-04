# Research: Crypto DEX API Microservice

## 1. Storage for API Keys and User Configurations

### Decision
We will use SQLite.

### Rationale
- **Simplicity**: SQLite is a serverless, self-contained, transactional SQL database engine. It is incredibly easy to set up and requires no separate server process, making it ideal for a lightweight microservice.
- **Portability**: The entire database is stored in a single file, which simplifies backups and deployment.
- **Sufficient for Scope**: For the initial scope of supporting a few DEXs and a moderate number of users, SQLite's performance is more than adequate, especially for managing API keys and configurations which are not high-write-velocity operations.
- **Flask Integration**: Flask has built-in support for SQLite, making integration seamless.

### Alternatives Considered
- **PostgreSQL**: While more powerful and scalable, it introduces additional operational overhead (setup, maintenance, hosting) which is not necessary for the current scope of this project.

## 2. Best Practices for Flask Application Structure

### Decision
We will adopt a feature-based or "blueprint" application structure.

### Rationale
- **Scalability**: Using Flask Blueprints allows us to organize the application into logical, reusable components (e.g., `prices`, `orders`, `balances`). This makes the codebase easier to navigate and maintain as it grows.
- **Separation of Concerns**: It enforces a clean separation between different parts of the application, which aligns with the "Code Quality" principle.
- **Extensibility**: Adding a new DEX or a new feature can be done by creating a new blueprint or modifying an existing one without impacting the rest of the application.

## 3. Best Practices for DEX API Integration

### Decision
We will create an abstract base class (ABC) for DEX integrations.

### Rationale
- **Extensibility**: This directly addresses the requirement for future extensibility. Each new DEX will be a concrete implementation of the ABC, ensuring a consistent interface.
- **Maintainability**: It standardizes how the application interacts with different DEXs, making the code cleaner and easier to understand.
- **Testing**: The ABC can be easily mocked for unit tests, allowing us to test the core application logic without making live API calls. Each implementation of the ABC will have its own dedicated integration tests.