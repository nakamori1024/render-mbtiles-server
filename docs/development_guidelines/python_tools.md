1. Ruff
   - Format execution: `uv run --frozen ruff format .`
   - Check execution: `uv run --frozen ruff check .`
   - Fix execution: `uv run --frozen ruff check . --fix`
   - Important check items:
     - Line length (88 characters)
     - Import sorting (I001)
     - Unused imports
   - Line wrapping:
     - Use parentheses for strings
     - Break function calls into multiple lines with proper indentation
     - Split import statements into multiple lines

2. Type Checking
   - Tool: `uv run --frozen pyright`
   - Requirements:
     - Add explicit None checks for Optional types
     - Handle string types narrowly
     - Version warnings can be ignored if checks pass

3. Pre-commit
   - Configuration file: `.pre-commit-config.yaml`
   - Execution timing: On git commit
   - Tools used: Prettier (for YAML/JSON), Ruff (for Python)
   - Ruff update method:
     - Check PyPI version
     - Update revision in configuration file
     - Commit configuration file first