---
name: utils.format
description: Auto-format code with Black and Ruff to fix style issues
parameters: []
tools:
  - Bash
---

# /utils.format

Auto-format code using Black (formatter) and Ruff (auto-fixable linting issues).

## Usage

```
/utils.format
```

## Purpose

Automatically fix code style issues:
- **Black**: Reformat code to Black style
- **Ruff**: Auto-fix linting violations (imports, whitespace, etc.)

## Behavior

1. **Activate venv**: Source venv/bin/activate
2. **Run Black**: `black src/ tests/` (write mode)
3. **Run Ruff with --fix**: `ruff check --fix src/ tests/`
4. **Capture changes**: List modified files
5. **Output summary**: Show files changed

## Examples

### Files Formatted

```
/utils.format
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Auto-Formatting Code
════════════════════════════════════════════════════════════════════════════

Running Black...
  reformatted src/data/csv_loader.py
  reformatted src/components/sales_filter.py
  reformatted tests/unit/data/test_csv_loader.py
  
  3 files reformatted, 45 files left unchanged

Running Ruff --fix...
  Fixed 8 issues in 4 files:
    - src/data/transformers.py (3 fixes: whitespace)
    - src/components/sales_filter.py (2 fixes: import order)
    - tests/unit/data/test_csv_loader.py (3 fixes: whitespace)

Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Files formatted: 7
  Changes applied: ✓

Next Steps:
  - Review changes: git diff
  - Run /utils.lint to verify
  - Commit changes: /utils.commit "style: Format code with Black and Ruff"

════════════════════════════════════════════════════════════════════════════
```

### Already Formatted

```
/utils.format
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Auto-Formatting Code
════════════════════════════════════════════════════════════════════════════

Running Black...
  All files already formatted ✓
  
Running Ruff --fix...
  No fixable issues found ✓

Summary: All files already formatted correctly!

════════════════════════════════════════════════════════════════════════════
```

## See Also

- `/utils.lint` - Check code quality (includes formatting check)
- `/workflow.verify` - Verify all quality standards
