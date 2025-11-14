---
name: dash.component
description: Create a Dash component with tests and accessibility support
parameters:
  - name: name
    description: Component name in PascalCase (e.g., SalesFilter, DataTable)
    required: true
    type: string
  - name: type
    description: Component type (dropdown, table, datepicker, input, button, etc.)
    required: true
    type: string
tools:
  - Write
  - Read
---

# /dash.component

Create a Dash UI component with tests, type hints, and WCAG 2.1 AA accessibility compliance.

## Usage

```
/dash.component [name] [type]
```

**Arguments**:
- `name`: Component name in PascalCase (e.g., SalesFilter, DataTable)
- `type`: Component type (dropdown, table, datepicker, input, button, graph, etc.)

## Purpose

Generate production-ready Dash components:
- Component function with proper structure
- Type hints and Google-style docstrings
- WCAG 2.1 AA accessibility (ARIA labels, semantic HTML)
- Comprehensive unit tests
- Integration with dash-components and accessibility-audit Skills

## Behavior

1. **Validate Inputs**:
   - Check name is PascalCase
   - Convert to snake_case for file naming
   - Validate type is supported

2. **Determine Component Structure** based on type:
   - `dropdown`: dcc.Dropdown with options
   - `table`: dash_table.DataTable with columns
   - `datepicker`: dcc.DatePickerRange
   - `input`: dcc.Input with validation
   - `button`: html.Button with onClick
   - `graph`: dcc.Graph with figure

3. **Create Component File**: `src/components/{snake_case_name}.py`
   - Import statements (dash.html, dash.dcc)
   - Component function with type hints
   - Props: id, options/data, callbacks
   - ARIA labels for accessibility
   - Google-style docstring with usage examples

4. **Create Test File**: `tests/unit/components/test_{snake_case_name}.py`
   - Test: component renders
   - Test: props work correctly
   - Test: accessibility (ARIA labels present)
   - Test: default values

5. **Skills Integration**:
   - **dash-components**: Provides component patterns
   - **accessibility-audit**: Validates WCAG 2.1 AA compliance

6. **Output**: Files created with next steps

## Examples

### Create Dropdown Component

```
/dash.component SalesFilter dropdown
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Creating Dash Component: SalesFilter (dropdown)
════════════════════════════════════════════════════════════════════════════

Skills activated:
  - dash-components (component patterns)
  - accessibility-audit (WCAG 2.1 AA validation)

Creating component file...
  ✓ Created: src/components/sales_filter.py (89 lines)

Component structure:
  - Function: create_sales_filter(options: list[str], default: str = None) -> html.Div
  - Type: dcc.Dropdown
  - Accessibility: ARIA label, semantic HTML
  - Props: id, options, value, clearable
  - Docstring: Google-style with examples

Creating test file...
  ✓ Created: tests/unit/components/test_sales_filter.py (67 lines)

Tests created:
  - test_sales_filter_renders()
  - test_sales_filter_with_options()
  - test_sales_filter_default_value()
  - test_sales_filter_aria_labels()

WCAG 2.1 AA Compliance:
  ✓ ARIA label present (aria-label="Sales Filter")
  ✓ Semantic HTML structure
  ✓ Keyboard navigation supported (native dcc.Dropdown)

Next Steps:
  1. Review component: cat src/components/sales_filter.py
  2. Run tests: /utils.test tests/unit/components/test_sales_filter.py
  3. Integrate into layout: Use in src/layouts/*.py
  4. Create callback: /dash.callback "Update chart when sales filter changes"

════════════════════════════════════════════════════════════════════════════
```

### Create Data Table Component

```
/dash.component ProductTable table
```

Output similar structure with dash_table.DataTable.

### Create Date Picker Component

```
/dash.component DateRangePicker datepicker
```

Output similar structure with dcc.DatePickerRange.

## Supported Component Types

| Type | Dash Component | Use Case |
|------|----------------|----------|
| dropdown | dcc.Dropdown | Select from options |
| table | dash_table.DataTable | Display tabular data |
| datepicker | dcc.DatePickerRange | Date range selection |
| input | dcc.Input | Text input with validation |
| button | html.Button | Actions, form submission |
| graph | dcc.Graph | Charts and visualizations |
| slider | dcc.Slider | Numeric range selection |
| checklist | dcc.Checklist | Multiple selection |
| radio | dcc.RadioItems | Single selection |

## See Also

- `/dash.layout` - Create dashboard layout
- `/dash.callback` - Create Dash callback
- `/workflow.act` - Implement with TDD
- `specs/memory/patterns.md` - Component patterns
