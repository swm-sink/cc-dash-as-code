---
name: utils.test
description: Run pytest with coverage reporting for specified path or entire test suite
parameters:
  - name: path
    description: Optional path to test file or directory (default is tests/)
    required: false
    type: string
tools:
  - Bash
---

# /utils.test

Run the test suite with pytest and generate coverage reports.

## Usage

```
/utils.test                     # Run all tests
/utils.test [path]              # Run tests in specific path
/utils.test tests/unit/         # Run unit tests only
/utils.test tests/test_foo.py   # Run specific test file
```

**Arguments**:
- `path` (optional): Test file or directory path (default: `tests/`)

## Purpose

Execute the test suite with coverage analysis:
- Run pytest tests
- Generate coverage reports (HTML and terminal)
- Identify passing/failing tests
- Highlight uncovered code

## Behavior

This command runs tests with coverage:

1. **Parse Path Parameter**:
   - Accept optional path parameter
   - Default to `tests/` if not specified
   - Validate path exists

2. **Activate Virtual Environment**:
   - Check if venv is active
   - Activate if needed: `source venv/bin/activate`
   - Or use `./venv/bin/pytest` directly

3. **Execute pytest**:
   - Run command:
     ```bash
     pytest {path} --cov=src --cov-report=html --cov-report=term-missing -v
     ```
   - Flags:
     - `--cov=src`: Measure coverage of src/ directory
     - `--cov-report=html`: Generate HTML report in htmlcov/
     - `--cov-report=term-missing`: Show missing lines in terminal
     - `-v`: Verbose output

4. **Parse Output**:
   - **Test Results**:
     - Passed count
     - Failed count
     - Skipped count
     - Duration
   - **Coverage**:
     - Overall percentage
     - Per-module percentages
     - Missing lines
   - **Failed Tests**:
     - Test name
     - Error message
     - Traceback

5. **Generate Report**:
   - Summary statistics
   - Pass/fail status
   - Coverage breakdown
   - Path to HTML report
   - Recommendations

## Examples

Example 1: Run all tests (all pass)
```
/utils.test
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Running Test Suite
════════════════════════════════════════════════════════════════════════════

Activating virtual environment...
  ✓ venv/bin/activate

Executing pytest...
  Command: pytest tests/ --cov=src --cov-report=html --cov-report=term-missing -v

═══════════════════════════════ Test Results ═══════════════════════════════

tests/unit/components/test_sales_filter.py::test_renders ✓ PASSED
tests/unit/components/test_sales_filter.py::test_validates_input ✓ PASSED
tests/unit/components/test_date_picker.py::test_renders ✓ PASSED
tests/unit/components/test_date_picker.py::test_date_validation ✓ PASSED
tests/unit/data/test_csv_loader.py::test_loads_csv ✓ PASSED
tests/unit/data/test_csv_loader.py::test_handles_missing_file ✓ PASSED
tests/unit/data/test_csv_loader.py::test_validates_schema ✓ PASSED
tests/integration/test_dashboard.py::test_filter_updates_chart ✓ PASSED
... (45 more tests)

═══════════════════════════════ Test Summary ════════════════════════════════

  Passed:  53 tests ✓
  Failed:  0 tests
  Skipped: 2 tests
  Duration: 12.3s

Coverage Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Module                           Statements   Coverage   Missing Lines
───────────────────────────────────────────────────────────────────────────
src/components/sales_filter.py          67       100%   -
src/components/date_picker.py           52        96%   45-46
src/data/csv_loader.py                 145        92%   67-72, 134
src/data/validators.py                  89        85%   12-15, 78-89
src/layouts/dashboard_layout.py        112        88%   45-52, 98-105
───────────────────────────────────────────────────────────────────────────
TOTAL                                  465        91%

Overall Coverage: 91% ✓ (target: 80%)

HTML Report: htmlcov/index.html
  Open in browser: file:///home/user/cc-dash-as-code/htmlcov/index.html

Status: ✅ ALL TESTS PASS

════════════════════════════════════════════════════════════════════════════
```

Example 2: Run specific test directory (some failures)
```
/utils.test tests/unit/data/
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Running Test Suite: tests/unit/data/
════════════════════════════════════════════════════════════════════════════

Executing pytest...

═══════════════════════════════ Test Results ═══════════════════════════════

tests/unit/data/test_csv_loader.py::test_loads_csv ✓ PASSED
tests/unit/data/test_csv_loader.py::test_handles_missing_file ❌ FAILED
tests/unit/data/test_csv_loader.py::test_validates_schema ✓ PASSED
tests/unit/data/test_validators.py::test_validates_dtypes ❌ FAILED
tests/unit/data/test_validators.py::test_handles_nulls ✓ PASSED

═══════════════════════════════ Test Summary ════════════════════════════════

  Passed:  3 tests
  Failed:  2 tests ❌
  Skipped: 0 tests
  Duration: 2.1s

Failed Tests
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

1. tests/unit/data/test_csv_loader.py::test_handles_missing_file

  Error: AssertionError
  Expected CSVLoaderError to be raised, but got FileNotFoundError

  Location: tests/unit/data/test_csv_loader.py:45

  Traceback:
    File "tests/unit/data/test_csv_loader.py", line 45, in test_handles_missing_file
      with pytest.raises(CSVLoaderError):
    AssertionError: FileNotFoundError not caught

  Fix: Wrap FileNotFoundError in CSVLoaderError in csv_loader.py

2. tests/unit/data/test_validators.py::test_validates_dtypes

  Error: TypeError
  validate_dtypes() missing 1 required positional argument: 'schema'

  Location: tests/unit/data/test_validators.py:67

  Traceback:
    File "tests/unit/data/test_validators.py", line 67, in test_validates_dtypes
      result = validate_dtypes(df)
    TypeError: validate_dtypes() missing 1 required positional argument: 'schema'

  Fix: Update function call to include schema parameter

Coverage Report
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Module                        Statements   Coverage   Missing Lines
──────────────────────────────────────────────────────────────────────────
src/data/csv_loader.py              145        78%   45-52, 67-72, 134
src/data/validators.py               89        72%   12-15, 45-52, 78-89
──────────────────────────────────────────────────────────────────────────
TOTAL                               234        75%

Overall Coverage: 75% ⚠️ (target: 80%)

Status: ❌ TESTS FAILED

Recommendations:
  1. Fix 2 failing tests (see details above)
  2. Increase coverage to 80% (currently 75%)
  3. Re-run tests after fixes: /utils.test tests/unit/data/

════════════════════════════════════════════════════════════════════════════
```

Example 3: Run specific test file
```
/utils.test tests/unit/components/test_sales_filter.py
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Running Test Suite: tests/unit/components/test_sales_filter.py
════════════════════════════════════════════════════════════════════════════

═══════════════════════════════ Test Results ═══════════════════════════════

tests/unit/components/test_sales_filter.py::test_renders ✓ PASSED
tests/unit/components/test_sales_filter.py::test_validates_input ✓ PASSED
tests/unit/components/test_sales_filter.py::test_aria_labels ✓ PASSED
tests/unit/components/test_sales_filter.py::test_default_value ✓ PASSED

═══════════════════════════════ Test Summary ════════════════════════════════

  Passed:  4 tests ✓
  Failed:  0 tests
  Skipped: 0 tests
  Duration: 0.8s

Coverage Report (filtered to relevant modules)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Module                           Coverage
────────────────────────────────────────
src/components/sales_filter.py    100%

Status: ✅ ALL TESTS PASS

════════════════════════════════════════════════════════════════════════════
```

Example 4: No tests found
```
/utils.test tests/nonexistent/
```

Output:
```
Error: Test path not found

Path: tests/nonexistent/
Status: Does not exist

Available test directories:
  - tests/unit/
  - tests/integration/
  - tests/e2e/

Run: /utils.test (to run all tests)
```

Example 5: Virtual environment not found
```
/utils.test
```

Output:
```
Warning: Virtual environment not found

Expected: venv/ directory in project root
Found: No venv/ directory

Options:
  1. Create virtual environment:
     python -m venv venv
     source venv/bin/activate
     pip install -r requirements.txt

  2. Install pytest globally (not recommended):
     pip install pytest pytest-cov

Recommendation: Create and activate virtual environment first.
```

## Output

**Test Results**:
- Passed/failed/skipped counts
- Individual test status
- Failed test details with tracebacks
- Duration

**Coverage Report**:
- Overall percentage
- Per-module breakdown
- Missing line numbers
- Path to HTML report

**Status**:
- ✅ PASS: All tests pass, coverage ≥ 80%
- ⚠️  PARTIAL: Tests pass but coverage < 80%
- ❌ FAIL: One or more tests fail

**Recommendations**:
- Fix failing tests
- Increase coverage
- Next steps

## Coverage Targets

Per `specs/memory/constitution.md`:
- **Minimum**: 80% overall coverage
- **Goal**: 90%+ for critical modules
- **Acceptable**: 70%+ for UI components (harder to test)

## Integration with EPIC Workflow

This command is used in:
- `/workflow.verify`: Runs as part of verification
- `/workflow.act`: Tests are written during TDD

## See Also

- `/workflow.verify` - Comprehensive quality validation (includes tests)
- `/workflow.act` - Implement with TDD (writes tests)
- `/utils.lint` - Check code quality
- `specs/memory/constitution.md` - Coverage requirements
- `specs/memory/patterns.md` - Testing patterns
