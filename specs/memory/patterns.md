# Coding Patterns and Conventions

**Last Updated**: 2025-11-13
**Purpose**: Document coding patterns, conventions, and best practices learned during development

---

## Overview

This file captures coding patterns and conventions that emerge during dashboard development. It serves as a living reference for consistent code quality across the project.

**Related**:
- `constitution.md` - Core principles and standards
- `decisions.md` - Architectural decisions
- `preferences.md` - Developer preferences and anti-patterns

---

## Python Patterns

### Module Organization

**Pattern**: Organize modules by function, not by type.

```python
# Good - Organized by function
src/
  dashboards/
    revenue/
      __init__.py
      app.py           # Main app
      data.py          # Data loading
      components.py    # UI components
      callbacks.py     # Callbacks
    sales/
      ...

# Avoid - Organized by type
src/
  components/        # All components mixed together
  callbacks/         # All callbacks mixed together
  data/             # All data loaders mixed together
```

**Rationale**: Function-based organization makes it easier to understand and maintain related code together.

---

### Type Hints

**Pattern**: Use type hints for all function signatures and class attributes.

```python
from typing import List, Dict, Optional
import pandas as pd

def load_sales_data(
    start_date: str,
    end_date: str,
    region: Optional[str] = None
) -> pd.DataFrame:
    """Load sales data for specified date range.

    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        region: Optional region filter

    Returns:
        DataFrame with sales data
    """
    ...
```

**Rationale**: Type hints improve code clarity, enable better IDE support, and catch errors early with mypy.

---

### Error Handling

**Pattern**: Use specific exceptions and provide context in error messages.

```python
# Good
def load_data(file_path: str) -> pd.DataFrame:
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Data file not found: {file_path}. "
            f"Please ensure the file exists or check the path."
        )

    try:
        return pd.read_csv(file_path)
    except pd.errors.EmptyDataError:
        raise ValueError(f"Data file is empty: {file_path}")
    except pd.errors.ParserError as e:
        raise ValueError(f"Failed to parse {file_path}: {str(e)}")

# Avoid - Generic exceptions
def load_data(file_path: str) -> pd.DataFrame:
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise Exception(f"Error: {e}")
```

**Rationale**: Specific exceptions and detailed messages help with debugging and user guidance.

---

## Dash Patterns

### Component Creation

**Pattern**: Create reusable component functions with clear props and documentation.

```python
from dash import html, dcc
from typing import List, Optional

def create_filter_dropdown(
    id: str,
    options: List[Dict[str, str]],
    placeholder: str = "Select...",
    multi: bool = False,
    className: Optional[str] = None
) -> dcc.Dropdown:
    """Create a styled dropdown filter component.

    Args:
        id: Unique identifier for the dropdown
        options: List of {'label': '...', 'value': '...'} dicts
        placeholder: Placeholder text
        multi: Enable multiple selection
        className: Additional CSS classes

    Returns:
        Configured dcc.Dropdown component
    """
    return dcc.Dropdown(
        id=id,
        options=options,
        placeholder=placeholder,
        multi=multi,
        className=className or "custom-dropdown",
        clearable=True
    )
```

**Rationale**: Reusable components reduce code duplication and ensure consistency.

---

### Callback Patterns

**Pattern**: Use descriptive callback IDs and separate business logic from callback wiring.

```python
from dash import Input, Output, State, callback
from typing import Optional

# Business logic (testable)
def filter_sales_data(
    df: pd.DataFrame,
    region: Optional[str],
    date_range: tuple
) -> pd.DataFrame:
    """Filter sales data by region and date range."""
    filtered = df.copy()

    if region:
        filtered = filtered[filtered['region'] == region]

    if date_range:
        start, end = date_range
        filtered = filtered[
            (filtered['date'] >= start) &
            (filtered['date'] <= end)
        ]

    return filtered

# Callback wiring (thin wrapper)
@callback(
    Output('sales-chart', 'figure'),
    Input('region-filter', 'value'),
    Input('date-range-picker', 'start_date'),
    Input('date-range-picker', 'end_date'),
    State('sales-data-store', 'data')
)
def update_sales_chart(
    region: Optional[str],
    start_date: str,
    end_date: str,
    sales_data: Dict
) -> dict:
    """Update sales chart based on filter selections."""
    df = pd.DataFrame(sales_data)
    filtered_df = filter_sales_data(df, region, (start_date, end_date))

    return create_sales_figure(filtered_df)
```

**Rationale**: Separating business logic makes code more testable and maintainable.

---

### Layout Patterns

**Pattern**: Use responsive grid layouts with clear structure.

```python
from dash import html, dcc

def create_dashboard_layout() -> html.Div:
    """Create main dashboard layout."""
    return html.Div([
        # Header
        html.Header([
            html.H1("Sales Dashboard", className="dashboard-title"),
            html.Div(id="user-info", className="user-info")
        ], className="dashboard-header"),

        # Main content
        html.Div([
            # Sidebar
            html.Aside([
                html.H2("Filters", className="sidebar-title"),
                create_filter_section()
            ], className="sidebar"),

            # Content area
            html.Main([
                create_metrics_section(),
                create_charts_section()
            ], className="main-content")
        ], className="dashboard-body")
    ], className="dashboard-container")
```

**Rationale**: Consistent layout structure improves maintainability and accessibility.

---

## Data Patterns

### Data Loading

**Pattern**: Use dedicated data loading functions with caching.

```python
from functools import lru_cache
import pandas as pd
from typing import Optional

@lru_cache(maxsize=128)
def load_sales_data(
    cache_key: Optional[str] = None
) -> pd.DataFrame:
    """Load sales data with caching.

    Args:
        cache_key: Optional key for cache invalidation

    Returns:
        Sales data DataFrame
    """
    # Load from database or file
    df = pd.read_csv('data/sales.csv')

    # Standard transformations
    df['date'] = pd.to_datetime(df['date'])
    df['revenue'] = df['revenue'].astype(float)

    return df
```

**Rationale**: Caching improves performance; dedicated functions centralize data logic.

---

### Data Transformation

**Pattern**: Chain transformations with clear intermediate steps.

```python
def prepare_sales_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """Prepare sales data for analysis."""
    return (
        df
        .copy()
        .dropna(subset=['revenue', 'date'])
        .assign(
            month=lambda x: x['date'].dt.to_period('M'),
            year=lambda x: x['date'].dt.year,
            quarter=lambda x: x['date'].dt.quarter
        )
        .query('revenue > 0')
        .sort_values('date')
    )
```

**Rationale**: Method chaining makes transformations clear and easy to modify.

---

## Testing Patterns

### Unit Test Structure

**Pattern**: Use AAA (Arrange-Act-Assert) pattern with descriptive test names.

```python
import pytest
import pandas as pd

def test_filter_sales_data_by_region():
    """Test filtering sales data by region returns correct subset."""
    # Arrange
    test_data = pd.DataFrame({
        'region': ['North', 'South', 'North'],
        'revenue': [100, 200, 150]
    })

    # Act
    result = filter_sales_data(test_data, region='North', date_range=None)

    # Assert
    assert len(result) == 2
    assert all(result['region'] == 'North')
    assert result['revenue'].sum() == 250
```

**Rationale**: AAA structure makes tests easy to read and understand.

---

### Fixture Patterns

**Pattern**: Use fixtures for common test data and setup.

```python
import pytest
import pandas as pd

@pytest.fixture
def sample_sales_data() -> pd.DataFrame:
    """Provide sample sales data for testing."""
    return pd.DataFrame({
        'date': pd.to_datetime(['2024-01-01', '2024-01-02', '2024-01-03']),
        'region': ['North', 'South', 'East'],
        'revenue': [100, 200, 150],
        'product': ['A', 'B', 'A']
    })

def test_revenue_calculation(sample_sales_data):
    """Test revenue calculation uses fixture."""
    total = calculate_total_revenue(sample_sales_data)
    assert total == 450
```

**Rationale**: Fixtures reduce duplication and make tests more maintainable.

---

## Documentation Patterns

### Docstring Format

**Pattern**: Use Google-style docstrings with type information.

```python
def calculate_yoy_growth(
    current: pd.DataFrame,
    previous: pd.DataFrame,
    metric: str = 'revenue'
) -> pd.DataFrame:
    """Calculate year-over-year growth for specified metric.

    Args:
        current: Current year data
        previous: Previous year data
        metric: Column name to calculate growth for

    Returns:
        DataFrame with yoy_growth column added

    Raises:
        ValueError: If metric column doesn't exist in both DataFrames

    Example:
        >>> current = pd.DataFrame({'revenue': [100, 200]})
        >>> previous = pd.DataFrame({'revenue': [80, 150]})
        >>> result = calculate_yoy_growth(current, previous)
    """
    ...
```

**Rationale**: Consistent docstring format improves code documentation and enables auto-generation of docs.

---

## Git Patterns

### Commit Messages

**Pattern**: Follow Conventional Commits specification.

```
feat: Add sales region filter component

Implement dropdown filter for selecting sales regions with:
- Multi-select capability
- Clear all button
- Responsive styling

Closes #42
```

**Format**:
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`

**Rationale**: Structured commits enable automatic changelog generation and clear history.

---

### Branch Naming

**Pattern**: Use feature number and descriptive name.

```
002-claude-code-commands
003-agent-skills-development
004-agent-skills-production
```

**Format**: `{number}-{feature-name-kebab-case}`

**Rationale**: Aligns with spec-kit methodology; clear feature tracking.

---

## Performance Patterns

### Callback Optimization

**Pattern**: Use `prevent_initial_call` and memoization for expensive operations.

```python
from dash import callback, Input, Output
from functools import lru_cache

@lru_cache(maxsize=32)
def expensive_calculation(param: str) -> dict:
    """Perform expensive calculation with caching."""
    # Heavy computation here
    ...

@callback(
    Output('result', 'children'),
    Input('trigger', 'n_clicks'),
    prevent_initial_call=True
)
def update_result(n_clicks: int) -> str:
    """Update result only when triggered."""
    result = expensive_calculation('key')
    return format_result(result)
```

**Rationale**: Prevents unnecessary computation and improves responsiveness.

---

## Security Patterns

### Environment Variables

**Pattern**: Never hardcode secrets; use environment variables.

```python
import os
from typing import Optional

def get_database_url() -> str:
    """Get database URL from environment variable.

    Raises:
        ValueError: If DATABASE_URL not set
    """
    url = os.getenv('DATABASE_URL')
    if not url:
        raise ValueError(
            "DATABASE_URL environment variable not set. "
            "Please configure it in .env file."
        )
    return url
```

**Rationale**: Prevents accidental secret exposure in version control.

---

### Input Validation

**Pattern**: Validate and sanitize all user inputs.

```python
from typing import Optional
import re

def validate_date_input(date_str: Optional[str]) -> bool:
    """Validate date string format.

    Args:
        date_str: Date string in YYYY-MM-DD format

    Returns:
        True if valid, False otherwise
    """
    if not date_str:
        return False

    pattern = r'^\d{4}-\d{2}-\d{2}$'
    if not re.match(pattern, date_str):
        return False

    try:
        pd.to_datetime(date_str)
        return True
    except ValueError:
        return False
```

**Rationale**: Prevents injection attacks and data corruption.

---

## Patterns to Add

As development progresses, new patterns will be documented here:

- [ ] Accessibility patterns (WCAG 2.1 AA)
- [ ] Performance optimization patterns
- [ ] Advanced caching strategies
- [ ] Component composition patterns
- [ ] State management patterns
- [ ] Error recovery patterns
- [ ] Logging patterns
- [ ] Monitoring and metrics patterns

---

**Note**: This is a living document. Update it as new patterns emerge during development.
