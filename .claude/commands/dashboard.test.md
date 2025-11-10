---
allowed-tools: Bash(python -m pytest:*), Bash(python -m playwright:*), Read
description: Run comprehensive test suite with coverage reporting
---

# Run Test Suite

Execute the complete test suite for the dashboard project.

## Current Context

- Project Root: !`pwd`
- Python Version: !`python --version`
- Installed Packages: !`pip list | grep -E "(pytest|playwright|dash)"`

## Your Task

Run all tests with the following sequence:

1. **Unit Tests**
   ```bash
   python -m pytest tests/unit/ -v
   ```

2. **Integration Tests**
   ```bash
   python -m pytest tests/integration/ -v
   ```

3. **End-to-End Tests**
   ```bash
   python -m pytest tests/e2e/ -v
   ```

4. **Coverage Report**
   ```bash
   python -m pytest --cov=src --cov-report=html --cov-report=term
   ```

5. **Accessibility Tests** (if available)
   ```bash
   python -m pytest tests/accessibility/ -v
   ```

## Success Criteria

- All tests pass
- Coverage >= 80%
- No accessibility violations

## Output

Present:
- Total tests run
- Passed/failed count
- Coverage percentage
- Location of HTML coverage report
- Any failures with details

## Next Steps

- If tests fail: Fix issues and re-run
- If coverage < 80%: Add more tests
- If all pass: Run `/dashboard.review` for code quality check
