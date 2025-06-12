1. Package Management
   - Use `uv` only, never use `pip`
   - Installation method: `uv add package`
   - Tool execution: `uv run tool`
   - Upgrade: `uv add --dev package --upgrade-package package`
   - Prohibited: `uv pip install`, using `@latest` syntax

2. Code Quality
   - Type hints are mandatory for all code
   - Public APIs must have documentation strings (docstrings)
   - Keep functions focused and small
   - Follow existing patterns precisely
   - Maximum line length is 88 characters

3. Testing Requirements
   - Test framework: `uv run --frozen pytest`
   - Use `anyio` instead of `asyncio` for async tests
   - Test coverage should include edge cases and errors
   - New features must include tests
   - Bug fixes must include unit tests