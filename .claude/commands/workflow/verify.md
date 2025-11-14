---
name: workflow.verify
description: Validate implementation through tests, linting, type checking, and quality standards (EPIC - Verify phase)
parameters: []
tools:
  - Bash
  - Read
---

# /workflow.verify

Validate implementation against quality standards: tests, linting, type checking, accessibility, and performance.

## Usage

```
/workflow.verify
```

## EPIC Methodology

**EPIC** = Observe → Act → **V**erify → Loop

This command implements the **Verify** phase:
- Run complete test suite
- Check code quality (linting, typing)
- Validate accessibility compliance
- Check performance targets
- Generate comprehensive validation report

## Behavior

This command performs comprehensive quality validation:

1. **Run Test Suite**:
   - Execute: `pytest --cov=src --cov-report=html --cov-report=term`
   - Parse output for:
     - Test count (passed/failed/skipped)
     - Coverage percentage
     - Failed test details with traceback
   - **Pass Criteria**: All tests pass, coverage ≥ 80%

2. **Run Linter (Ruff)**:
   - Execute: `ruff check src/ tests/`
   - Parse violations by severity (error, warning, info)
   - Group by file and rule code
   - **Pass Criteria**: Zero errors, warnings acceptable

3. **Run Type Checker (mypy)**:
   - Execute: `mypy src/`
   - Parse type errors with locations
   - Check for untyped definitions
   - **Pass Criteria**: Zero type errors

4. **Run Formatter Check (Black)**:
   - Execute: `black --check src/ tests/`
   - Report files needing formatting
   - **Pass Criteria**: All files formatted

5. **Check Accessibility (if UI components)**:
   - Detect Dash components in recent changes
   - Skills Integration: accessibility-audit Skill activates
   - Check for:
     - ARIA labels present
     - Semantic HTML usage
     - Keyboard navigation support
     - Color contrast (WCAG 2.1 AA)
   - **Pass Criteria**: WCAG 2.1 Level AA compliant

6. **Check Performance (if applicable)**:
   - Detect performance-critical code (data loading, callbacks)
   - Skills Integration: performance-optimizer Skill activates
   - Verify targets:
     - Initial load: <3 seconds
     - Callback execution: <1 second
     - Data loading: per spec requirements
   - **Pass Criteria**: All performance targets met

7. **Generate Report**:
   - Overall status: PASS or FAIL
   - Detailed results for each check
   - Summary of issues found
   - Recommendations for fixes

## Examples

Example 1: All checks pass
```
/workflow.verify
```

Output:
```
════════════════════════════════════════════════════════════════════════════
EPIC Workflow: Verify Phase
════════════════════════════════════════════════════════════════════════════

Running quality validation...

✅ Tests
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Executed: pytest --cov=src --cov-report=html

  Results:
    Passed:  45 tests
    Failed:  0 tests
    Skipped: 2 tests

  Coverage:
    Overall:  87%
    src/components/: 92%
    src/data/: 85%
    src/layouts/: 80%

  Report: htmlcov/index.html
  Status: ✅ PASS (coverage ≥ 80%)

✅ Linting (Ruff)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Executed: ruff check src/ tests/

  Results:
    Errors:   0
    Warnings: 0

  Status: ✅ PASS (zero errors)

✅ Type Checking (mypy)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Executed: mypy src/

  Results:
    Errors:    0
    Files checked: 23

  Status: ✅ PASS (zero type errors)

✅ Formatting (Black)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Executed: black --check src/ tests/

  Results:
    Files checked: 48
    Would reformat: 0

  Status: ✅ PASS (all files formatted)

✅ Accessibility (WCAG 2.1 AA)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Skill: accessibility-audit (activated)

  Components checked:
    - sales_filter.py: ✓ ARIA labels present
    - date_picker.py: ✓ Keyboard navigation
    - data_table.py: ✓ Semantic HTML

  Color contrast:
    - All combinations: ✓ AA compliant (4.5:1 minimum)

  Status: ✅ PASS (WCAG 2.1 Level AA compliant)

✅ Performance
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Skill: performance-optimizer (activated)

  Measurements:
    - CSV loading (100K rows): 0.8s ✓ (target: <1s)
    - Dashboard render: 2.1s ✓ (target: <3s)
    - Filter callback: 0.3s ✓ (target: <1s)

  Status: ✅ PASS (all targets met)

Overall Verification Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ✅ Tests:        PASS
  ✅ Linting:      PASS
  ✅ Type Check:   PASS
  ✅ Formatting:   PASS
  ✅ Accessibility: PASS
  ✅ Performance:  PASS

  Result: ✅ ALL CHECKS PASS

Next Step: /workflow.loop (commit and continue)

════════════════════════════════════════════════════════════════════════════
```

Example 2: Some checks fail
```
/workflow.verify
```

Output:
```
════════════════════════════════════════════════════════════════════════════
EPIC Workflow: Verify Phase
════════════════════════════════════════════════════════════════════════════

Running quality validation...

❌ Tests
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Executed: pytest --cov=src --cov-report=html

  Results:
    Passed:  42 tests
    Failed:  3 tests
    Skipped: 2 tests

  Failed Tests:
    1. tests/unit/data/test_csv_loader.py::test_handles_missing_columns
       Error: AssertionError: Expected CSVLoaderError, got KeyError
       Location: tests/unit/data/test_csv_loader.py:67

    2. tests/unit/components/test_sales_filter.py::test_validates_input
       Error: TypeError: create_sales_filter() missing 1 required argument: 'options'
       Location: tests/unit/components/test_sales_filter.py:45

    3. tests/integration/test_dashboard.py::test_filter_updates_chart
       Error: TimeoutError: Callback did not complete within 5s
       Location: tests/integration/test_dashboard.py:89

  Coverage:
    Overall:  75% ⚠️ (target: 80%)
    Missing coverage:
      - src/data/csv_loader.py lines 67-72 (error handling)
      - src/components/sales_filter.py lines 34-38 (validation)

  Status: ❌ FAIL (3 tests failed, coverage below 80%)

⚠️ Linting (Ruff)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Executed: ruff check src/ tests/

  Results:
    Errors:   2
    Warnings: 5

  Errors:
    1. src/data/csv_loader.py:45:12: F841 Local variable 'schema' is assigned but never used
    2. src/components/sales_filter.py:78:1: E501 Line too long (92 > 88 characters)

  Warnings:
    1. src/data/transformers.py:23:5: W291 Trailing whitespace
    2. tests/unit/data/test_csv_loader.py:12:1: W293 Blank line contains whitespace
    ...

  Status: ⚠️ FAIL (2 errors must be fixed)

❌ Type Checking (mypy)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Executed: mypy src/

  Results:
    Errors:    4
    Files checked: 23

  Type Errors:
    1. src/data/csv_loader.py:67: error: Argument 1 to "validate_schema" has incompatible type "DataFrame"; expected "dict"
    2. src/components/sales_filter.py:34: error: Missing return statement
    3. src/components/sales_filter.py:45: error: Incompatible types in assignment (expression has type "None", variable has type "list[str]")
    4. src/layouts/dashboard_layout.py:89: error: Cannot call function of unknown type

  Status: ❌ FAIL (4 type errors)

✅ Formatting (Black)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  Executed: black --check src/ tests/

  Results:
    Files checked: 48
    Would reformat: 3

  Files needing formatting:
    - src/data/csv_loader.py
    - src/components/sales_filter.py
    - tests/unit/data/test_csv_loader.py

  Status: ⚠️ FAIL (3 files need formatting)

  Fix: Run /utils.format to auto-format

Overall Verification Status
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  ❌ Tests:        FAIL (3 failed, coverage 75%)
  ❌ Linting:      FAIL (2 errors)
  ❌ Type Check:   FAIL (4 errors)
  ⚠️  Formatting:   FAIL (3 files)

  Result: ❌ VERIFICATION FAILED

Recommendations:
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Priority 1 (Critical - Fix First):
  1. Fix failing tests (3 tests)
     - Add error handling for missing columns in csv_loader.py
     - Fix function signature in sales_filter.py
     - Optimize callback to complete within timeout

  2. Fix type errors (4 errors)
     - Correct type annotations in csv_loader.py:67
     - Add return statement in sales_filter.py:34
     - Fix None assignment in sales_filter.py:45
     - Add type hints in dashboard_layout.py:89

Priority 2 (Important - Fix Soon):
  3. Fix linting errors (2 errors)
     - Remove unused 'schema' variable
     - Break long line in sales_filter.py:78

  4. Run formatter
     - Execute: /utils.format
     - This will fix 3 files automatically

Priority 3 (Low - Optional):
  5. Address linting warnings (5 warnings)
     - Remove trailing whitespace
     - Clean up blank lines

Next Steps:
  1. Fix critical issues (tests, types)
  2. Run /utils.format to fix formatting
  3. Run /workflow.verify again
  4. Repeat until all checks pass
  5. Then /workflow.loop to commit

Do NOT proceed to /workflow.loop until all checks pass!

════════════════════════════════════════════════════════════════════════════
```

Example 3: No code to verify
```
/workflow.verify
```

Output:
```
Warning: No code changes detected

The verify command checks code quality, but no Python files were found in src/ or tests/.

Have you implemented code yet?

Options:
1. Implement code: /workflow.act [task description]
2. Check which task to do: /workflow.observe
3. View specification: /spec.show [feature-number]

Typical workflow:
  /workflow.observe  → Identify task
  /workflow.act      → Implement task
  /workflow.verify   → Validate quality (this command)
  /workflow.loop     → Commit and continue
```

## Output

**Per-Check Results**:
- Test results (passed/failed/skipped, coverage)
- Linting results (errors, warnings)
- Type checking results (errors)
- Formatting results (files needing formatting)
- Accessibility results (if applicable)
- Performance results (if applicable)

**Overall Status**:
- PASS: All checks pass
- FAIL: One or more checks fail

**Recommendations** (if failed):
- Prioritized list of issues to fix
- Specific file and line references
- Suggested commands to run
- Next steps

## Pass Criteria

For verification to PASS, all of the following must be true:

| Check | Criteria |
|-------|----------|
| Tests | All tests pass, coverage ≥ 80% |
| Linting | Zero errors (warnings acceptable) |
| Type Check | Zero type errors |
| Formatting | All files formatted correctly |
| Accessibility | WCAG 2.1 AA compliant (if UI) |
| Performance | All targets met (if applicable) |

**Note**: Only proceed to `/workflow.loop` when verification PASSES.

## Skills Integration

Skills auto-activate based on code type:

- **accessibility-audit**: Activates when Dash components detected
- **performance-optimizer**: Activates when performance targets defined

These Skills provide additional validation beyond standard checks.

## Constitutional Alignment

This command enforces quality standards from `specs/memory/constitution.md`:

- **Core Principle 2**: TDD for all features (tests must pass)
- **Core Principle 3**: Type safety (mypy must pass)
- **Core Principle 6**: WCAG 2.1 AA compliance (accessibility check)
- **Core Principle 8**: Performance (<3s load, <1s callbacks)
- **Quality Standard 1**: 80% test coverage minimum
- **Quality Standard 3**: Zero linting errors

## See Also

- `/workflow.act` - Implement task (previous step)
- `/workflow.loop` - Commit and continue (next step if PASS)
- `/utils.test` - Run tests only
- `/utils.lint` - Run linting only
- `/utils.format` - Auto-format code
- `specs/memory/constitution.md` - Quality standards
