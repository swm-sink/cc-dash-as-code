---
name: workflow.act
description: Implement a task following TDD (Test-Driven Development) methodology (EPIC - Act phase)
parameters:
  - name: task
    description: Task description or task ID from tasks.md
    required: true
    type: string
tools:
  - Write
  - Edit
  - Read
  - Glob
  - Bash
---

# /workflow.act

Implement a task following Test-Driven Development (TDD) methodology.

## Usage

```
/workflow.act [task description or task ID]
```

**Arguments**:
- `task`: Task description (e.g., "Implement sales filter component") or task ID (e.g., "T024")

## EPIC Methodology

**EPIC** = Observe → **A**ct → Verify → Loop

This command implements the **Act** phase:
- Write failing tests first (TDD Red)
- Implement code to pass tests (TDD Green)
- Refactor for quality (TDD Refactor)
- Follow patterns and best practices

## Behavior

This command implements tasks using TDD workflow:

1. **Parse task description**:
   - Accept task description or task ID (T###)
   - If task ID provided, load details from tasks.md
   - Determine task type: component, callback, data loading, utility, etc.

2. **Analyze requirements**:
   - Extract relevant FR-NNN requirements from spec.md
   - Review patterns from `specs/memory/patterns.md`
   - Identify dependencies and prerequisites
   - Determine files to create/modify

3. **TDD Phase 1: RED (Write Failing Test)**:
   - Create or modify test file in `tests/` directory
   - Write test that describes desired behavior
   - Ensure test fails (no implementation yet)
   - Follow AAA pattern (Arrange, Act, Assert)
   - Add type hints and docstrings
   - Run test to confirm it fails with clear error message

4. **TDD Phase 2: GREEN (Implement Code)**:
   - Create or modify implementation file in `src/` directory
   - Write minimum code needed to pass the test
   - Add type hints (following patterns.md)
   - Add comprehensive docstrings
   - Follow naming conventions
   - Include requirement references (# FR-NNN)
   - Run test to confirm it passes

5. **TDD Phase 3: REFACTOR (Improve Quality)**:
   - Review code for clarity and efficiency
   - Extract common patterns
   - Remove duplication
   - Improve variable names
   - Add error handling
   - Run tests to ensure still passing

6. **Skills Integration**:
   - Auto-activate relevant Skills based on task type:
     - **dash-components**: For Dash UI components
     - **data-analysis**: For data loading/transformation
     - **plotly-viz**: For chart creation
     - **accessibility-audit**: For UI accessibility
     - **performance-optimizer**: For performance-critical code

7. **Output summary**:
   - Files created/modified
   - Tests written/updated
   - Requirements addressed
   - Next step (typically `/workflow.verify`)

## Examples

Example 1: Implement a Dash component
```
/workflow.act Implement sales filter dropdown component
```

Output:
```
════════════════════════════════════════════════════════════════════════════
EPIC Workflow: Act Phase
Task: Implement sales filter dropdown component
════════════════════════════════════════════════════════════════════════════

Analyzing task...
  Type: Dash Component
  Requirements: FR-023 (Filter components)
  Skills: dash-components, accessibility-audit (auto-activated)

TDD Phase 1: RED (Write Failing Test)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Created: tests/unit/components/test_sales_filter.py

Test written: test_sales_filter_renders_with_options()
  - Verifies component renders with dropdown
  - Checks default value
  - Validates option structure
  - Tests accessibility (ARIA labels)

Running test... ❌ FAIL (expected - no implementation yet)
  Error: ModuleNotFoundError: No module named 'src.components.sales_filter'

TDD Phase 2: GREEN (Implement Code)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Created: src/components/sales_filter.py

Implementation:
  - Function: create_sales_filter(region_options: list[str]) -> html.Div
  - Returns dcc.Dropdown with options
  - Includes ARIA labels for accessibility
  - Type hints and docstring added
  - Requirement reference: # FR-023

Running test... ✅ PASS

TDD Phase 3: REFACTOR (Improve Quality)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Improvements:
  - Extracted default options to constant
  - Added input validation for region_options
  - Enhanced docstring with usage examples
  - Added type validation in tests

Running tests... ✅ ALL PASS

Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Files Created:
  ✓ src/components/sales_filter.py (78 lines)
  ✓ tests/unit/components/test_sales_filter.py (45 lines)

Tests:
  ✓ 4 tests written, all passing
  ✓ Coverage: 100% for sales_filter.py

Requirements Addressed:
  ✓ FR-023: Filter components (Complete)

Code Quality:
  ✓ Type hints: Yes
  ✓ Docstrings: Yes (Google style)
  ✓ WCAG 2.1 AA: Compliant (ARIA labels present)

Next Step: /workflow.verify

════════════════════════════════════════════════════════════════════════════
```

Example 2: Implement data loading logic
```
/workflow.act T015 (Load customer data from CSV)
```

Output:
```
════════════════════════════════════════════════════════════════════════════
EPIC Workflow: Act Phase
Task: T015 - Load customer data from CSV
════════════════════════════════════════════════════════════════════════════

Analyzing task...
  Type: Data Loading
  Requirements: FR-012 (Data loading)
  Skills: data-analysis (auto-activated)
  Patterns: Data loading patterns from patterns.md

TDD Phase 1: RED (Write Failing Test)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Created: tests/unit/data/test_csv_loader.py

Tests written:
  1. test_load_csv_returns_dataframe()
  2. test_load_csv_validates_schema()
  3. test_load_csv_handles_missing_file()
  4. test_load_csv_handles_corrupted_data()

Running tests... ❌ FAIL (expected)

TDD Phase 2: GREEN (Implement Code)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Created: src/data/csv_loader.py

Implementation:
  - Function: load_customer_csv(file_path: str) -> pd.DataFrame
  - Uses pandas with proper error handling
  - Schema validation included
  - Follows data loading patterns from patterns.md
  - Requirement reference: # FR-012

Running tests... ✅ 4/4 PASS

TDD Phase 3: REFACTOR (Improve Quality)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Improvements:
  - Added logging for debugging
  - Created custom CSVLoaderError exception
  - Added data quality checks (nulls, dtypes)
  - Performance: Added chunking for large files

Running tests... ✅ 4/4 PASS (all improvements verified)

Summary
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Files Created:
  ✓ src/data/csv_loader.py (145 lines)
  ✓ src/data/exceptions.py (25 lines)
  ✓ tests/unit/data/test_csv_loader.py (98 lines)

Tests:
  ✓ 4 tests written, all passing
  ✓ Edge cases covered: missing file, corrupted data, schema mismatch
  ✓ Coverage: 95% for csv_loader.py

Requirements Addressed:
  ✓ FR-012: Data loading from CSV (Complete)
  ✓ FR-018: Error handling (Partial)

Performance:
  ✓ Loads 100K rows in 0.8s (target: <1s)

Next Step: /workflow.verify

════════════════════════════════════════════════════════════════════════════
```

Example 3: Task description ambiguous
```
/workflow.act Fix the dashboard
```

Output:
```
Error: Task description too vague

The task "Fix the dashboard" is not specific enough for implementation.

Please provide a clear, actionable task description with:
- What specifically needs to be fixed/implemented
- Which component or module
- Expected behavior

Good examples:
  ✓ "Fix null pointer error in sales_filter.py line 67"
  ✓ "Implement error handling for CSV loader"
  ✓ "Add date range validation to filter component"
  ✓ "T024" (reference specific task from tasks.md)

Bad examples:
  ✗ "Fix the dashboard"
  ✗ "Make it work"
  ✗ "Improve performance"

Try:
- /workflow.observe (to see recommended tasks)
- /spec.show [number] (to see requirements)
- Provide specific task from tasks.md
```

## Output

**Analysis Phase**:
- Task type identification
- Requirements mapping
- Skills activated
- Patterns to follow

**TDD Phase 1 (RED)**:
- Test file created/modified
- Test description
- Failing test confirmation

**TDD Phase 2 (GREEN)**:
- Implementation file created/modified
- Code summary
- Passing test confirmation

**TDD Phase 3 (REFACTOR)**:
- Improvements made
- Code quality checks
- Tests still passing

**Summary**:
- Files created/modified with line counts
- Tests written and passing
- Requirements addressed
- Code quality metrics
- Next step

## TDD Best Practices

This command enforces TDD best practices:

1. **Always write tests first**: Ensures testable design
2. **One test at a time**: Focus on one behavior
3. **Minimum code to pass**: Avoid over-engineering
4. **Refactor after green**: Improve without changing behavior
5. **Run tests frequently**: Immediate feedback

## Pattern Integration

The command automatically applies patterns from `specs/memory/patterns.md`:

- **Python patterns**: Type hints, error handling, module organization
- **Dash patterns**: Component structure, callback format
- **Data patterns**: Loading, transformation, validation
- **Testing patterns**: AAA structure, fixtures, mocking
- **Documentation patterns**: Google-style docstrings

## Skills Auto-Activation

Based on task type, relevant Skills activate automatically:

| Task Type | Skills Activated |
|-----------|------------------|
| Dash component | dash-components, accessibility-audit |
| Chart creation | plotly-viz, accessibility-audit |
| Data loading | data-analysis |
| Data transformation | data-analysis |
| Performance optimization | performance-optimizer |
| Callback implementation | dash-components |

## See Also

- `/workflow.observe` - Identify next task
- `/workflow.verify` - Validate implementation (next step)
- `/workflow.loop` - Complete cycle
- `/spec.show [number]` - View requirements
- `specs/memory/patterns.md` - Coding patterns and conventions
- `specs/memory/constitution.md` - Quality standards
