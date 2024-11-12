# Simple fastapi app

Test fastapi with docker and postgres

_*Work In Progress*_

### Next steps:

- Fix Ruff errors B008: Depends
- Move orm interactions into services
- Investigate why the app reloads but the changes are not applied

### Later:

- Separate schemas
- Use uuid instead of int for id
- Add missing CRUD operations
- Investigate and add migrations
- Investigate multiple status codes for the same endpoint
- Remove echo from create_async_engine
- Investigate better approaches for sqlalchemy async
- Add installation instructions

### Maybe:

- Add auth
- Add tests
