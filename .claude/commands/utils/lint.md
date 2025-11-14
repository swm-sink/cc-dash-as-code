---
name: utils.lint
description: Run code quality checks (Black, Ruff, mypy) and report all issues
parameters: []
tools:
  - Bash
---

# /utils.lint

Run comprehensive code quality checks: formatting (Black), linting (Ruff), and type checking (mypy).

## Usage

```
/utils.lint
```

## Purpose

Check code quality across three dimensions:
- **Black**: Code formatting compliance
- **Ruff**: Linting rules (PEP 8, complexity, security)
- **mypy**: Type safety and type hints

## Behavior

1. **Activate Virtual Environment**: Source venv/bin/activate
2. **Run Black Check**: `black --check src/ tests/`
3. **Run Ruff**: `ruff check src/ tests/`
4. **Run mypy**: `mypy src/`
5. **Aggregate Results**: Collect all issues
6. **Generate Report**: Show all violations with file:line references

## Examples

### All Checks Pass

```
/utils.lint
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Code Quality Checks
════════════════════════════════════════════════════════════════════════════

✅ Black (Formatting)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Command: black --check src/ tests/
  Files checked: 48
  Would reformat: 0
  Status: ✅ PASS

✅ Ruff (Linting)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Command: ruff check src/ tests/
  Errors: 0
  Warnings: 0
  Status: ✅ PASS

✅ mypy (Type Checking)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Command: mypy src/
  Type errors: 0
  Files checked: 23
  Status: ✅ PASS

Overall Status: ✅ ALL CHECKS PASS

Your code meets all quality standards!

════════════════════════════════════════════════════════════════════════════
```

### Some Issues Found

```
/utils.lint
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Code Quality Checks
════════════════════════════════════════════════════════════════════════════

❌ Black (Formatting)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Files needing formatting: 3
  
  - src/data/csv_loader.py
  - src/components/sales_filter.py
  - tests/unit/data/test_csv_loader.py
  
  Fix: Run /utils.format to auto-format
  Status: ❌ FAIL

❌ Ruff (Linting)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Errors: 2
  Warnings: 5
  
  Errors:
    src/data/csv_loader.py:45:12: F841 Local variable 'schema' assigned but never used
    src/components/sales_filter.py:78:1: E501 Line too long (92 > 88)
  
  Warnings:
    src/data/transformers.py:23:5: W291 Trailing whitespace
    tests/unit/data/test_csv_loader.py:12:1: W293 Blank line contains whitespace
    ...
  
  Status: ❌ FAIL (must fix errors)

❌ mypy (Type Checking)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Type errors: 4
  
  src/data/csv_loader.py:67: error: Argument has incompatible type "DataFrame"; expected "dict"
  src/components/sales_filter.py:34: error: Missing return statement
  src/components/sales_filter.py:45: error: Incompatible types in assignment
  src/layouts/dashboard_layout.py:89: error: Cannot call function of unknown type
  
  Status: ❌ FAIL

Overall Status: ❌ QUALITY CHECKS FAILED

Next Steps:
  1. Fix type errors (priority 1)
  2. Fix linting errors (priority 2)
  3. Run /utils.format to fix formatting
  4. Re-run /utils.lint to verify

════════════════════════════════════════════════════════════════════════════
```

## See Also

- `/utils.format` - Auto-fix formatting issues
- `/utils.test` - Run test suite
- `/workflow.verify` - Complete quality validation
