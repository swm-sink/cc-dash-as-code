---
name: dash.layout
description: Create a responsive dashboard layout with header, sidebar, and main content areas
parameters:
  - name: name
    description: Layout name in snake_case (e.g., sales_dashboard, analytics_view)
    required: true
    type: string
tools:
  - Write
---

# /dash.layout

Create a responsive dashboard layout following best practices for Dash applications.

## Usage

```
/dash.layout [name]
```

**Arguments**:
- `name`: Layout name in snake_case (e.g., sales_dashboard, analytics_view)

## Purpose

Generate production-ready dashboard layouts:
- Responsive grid structure
- Header, sidebar, main content areas
- WCAG 2.1 AA accessibility
- CSS theming support
- Mobile-friendly design

## Behavior

1. **Validate Name**: Check snake_case format
2. **Create Layout File**: `src/layouts/{name}.py`
   - Import Dash components
   - Define layout function
   - Responsive grid with dbc.Container/Row/Col (or html.Div)
   - Header section (title, logo, navigation)
   - Sidebar section (filters, controls)
   - Main content area (charts, tables)
   - Footer (optional)
3. **Apply Accessibility**:
   - Semantic HTML (header, nav, main, aside, footer)
   - ARIA landmarks
   - Proper heading hierarchy (h1, h2, h3)
4. **Create Test File**: `tests/unit/layouts/test_{name}.py`
5. **Output**: Files created

## Examples

```
/dash.layout sales_dashboard
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Creating Dashboard Layout: sales_dashboard
════════════════════════════════════════════════════════════════════════════

Creating layout file...
  ✓ Created: src/layouts/sales_dashboard.py (156 lines)

Layout structure:
  - Header: Title, logo, navigation
  - Sidebar: Filters and controls
  - Main: Chart and table areas
  - Responsive: Bootstrap grid

Creating test file...
  ✓ Created: tests/unit/layouts/test_sales_dashboard.py (45 lines)

WCAG 2.1 AA Compliance:
  ✓ Semantic HTML (header, nav, main, aside)
  ✓ ARIA landmarks
  ✓ Heading hierarchy (h1 → h2 → h3)

Next Steps:
  1. Add components to layout
  2. Create callbacks: /dash.callback
  3. Test layout: /utils.test tests/unit/layouts/

════════════════════════════════════════════════════════════════════════════
```

## See Also

- `/dash.component` - Create components for layout
- `/dash.callback` - Add interactivity
