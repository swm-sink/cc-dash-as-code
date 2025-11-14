---
name: dash.callback
description: Create a Dash callback with proper Input/Output/State configuration
parameters:
  - name: description
    description: Natural language description of callback behavior (e.g., "Update chart when filter changes")
    required: true
    type: string
tools:
  - Write
  - Edit
---

# /dash.callback

Create a Dash callback with proper decorator, type hints, and tests.

## Usage

```
/dash.callback [description]
```

**Arguments**:
- `description`: Natural language description (e.g., "Update chart when filter changes")

## Purpose

Generate production-ready Dash callbacks:
- @app.callback decorator with Input/Output/State
- Type hints for all parameters
- Business logic structure
- Error handling
- Unit tests

## Behavior

1. **Parse Description**: Infer inputs, outputs, logic
2. **Generate Callback**:
   - @app.callback decorator
   - Input(), Output(), State() from dash.dependencies
   - Function signature with type hints
   - Docstring with description
   - Business logic placeholder
3. **Suggest Module**: Where to place callback
4. **Create Test**: Unit test for callback logic
5. **Output**: Callback code and test

## Examples

```
/dash.callback "Update sales chart when region filter changes"
```

Output:
```
════════════════════════════════════════════════════════════════════════════
Creating Dash Callback
════════════════════════════════════════════════════════════════════════════

Parsed callback:
  Input: region-filter (value)
  Output: sales-chart (figure)
  Logic: Filter data by region, update chart

Generated callback code:
  
from dash import Input, Output
import plotly.express as px

@app.callback(
    Output("sales-chart", "figure"),
    Input("region-filter", "value")
)
def update_sales_chart(selected_region: str) -> dict:
    """Update sales chart based on selected region."""
    # Filter data by region
    filtered_df = df[df["region"] == selected_region]
    
    # Create figure
    fig = px.bar(filtered_df, x="month", y="sales")
    
    return fig

Suggested location: src/callbacks/sales_callbacks.py

Created test:
  tests/unit/callbacks/test_sales_callbacks.py

Next Steps:
  1. Add callback to appropriate module
  2. Implement business logic
  3. Run tests: /utils.test tests/unit/callbacks/

════════════════════════════════════════════════════════════════════════════
```

## See Also

- `/dash.component` - Create components
- `/dash.layout` - Create layouts
- Dash docs: https://dash.plotly.com/basic-callbacks
