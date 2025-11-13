# Developer Preferences and Anti-Patterns

**Last Updated**: 2025-11-13
**Purpose**: Document developer preferences, naming conventions, and anti-patterns to avoid

---

## Overview

This file captures developer preferences and anti-patterns identified during development. It complements `patterns.md` (what to do) by documenting what NOT to do and team preferences.

**Related**:
- `constitution.md` - Core principles (must follow)
- `patterns.md` - Coding patterns (should follow)
- `decisions.md` - Architectural decisions (context for preferences)

---

## Naming Conventions

### Files and Directories

**Preferences**:
```
# Good
src/dashboards/revenue_dashboard.py    # Snake case for Python files
src/components/sales_filter.py
specs/003-agent-skills-development/    # Kebab case for spec directories

# Avoid
src/dashboards/RevenueDashboard.py     # Pascal case for files
src/components/sales-filter.py         # Kebab case for Python files
specs/003_agent_skills_development/    # Snake case for directories
```

**Rationale**: Consistent with Python ecosystem (PEP 8) and spec-kit methodology.

---

### Python Variables and Functions

**Preferences**:
```python
# Good - Descriptive snake_case
def calculate_year_over_year_growth(current_revenue, previous_revenue):
    annual_growth_rate = (current_revenue - previous_revenue) / previous_revenue
    return annual_growth_rate

# Avoid - Unclear abbreviations
def calc_yoy_gr(cur_rev, prev_rev):
    agr = (cur_rev - prev_rev) / prev_rev
    return agr

# Avoid - Camel case for variables/functions
def calculateYearOverYearGrowth(currentRevenue, previousRevenue):
    ...
```

**Rationale**: Python convention (PEP 8); clarity over brevity.

---

### Constants

**Preferences**:
```python
# Good - UPPER_SNAKE_CASE with clear names
MAX_DATA_POINTS = 10000
DEFAULT_REGION = "North"
CACHE_TTL_SECONDS = 3600

# Avoid - Lowercase or unclear
max_data = 10000
default = "North"
ttl = 3600
```

**Rationale**: Clear distinction between constants and variables.

---

### Dash Component IDs

**Preferences**:
```python
# Good - Kebab-case, descriptive, scoped
dcc.Dropdown(id='revenue-dashboard-region-filter')
dcc.Graph(id='sales-chart-main')
dcc.Store(id='user-preferences-store')

# Avoid - Generic or unclear
dcc.Dropdown(id='dropdown1')
dcc.Graph(id='chart')
dcc.Store(id='store')
```

**Rationale**: Prevents ID collisions; clear purpose; easier debugging.

---

## Code Style Preferences

### Import Organization

**Preferences**:
```python
# Good - Organized by type, alphabetized within groups
# Standard library
import os
from typing import List, Dict, Optional

# Third-party
import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc, Input, Output

# Local/application
from src.components.filters import create_region_filter
from src.data.loaders import load_sales_data

# Avoid - Unorganized imports
from dash import Dash, html, dcc, Input, Output
import os
from src.components.filters import create_region_filter
import pandas as pd
from typing import List, Dict, Optional
```

**Rationale**: Clear organization; easier to find imports; follows PEP 8.

---

### String Formatting

**Preferences**:
```python
# Good - f-strings for readability
name = "Revenue"
year = 2024
message = f"{name} Dashboard - {year}"

# Acceptable - format() for complex cases
template = "Year: {year}, Quarter: {quarter}, Revenue: ${revenue:,.2f}"
result = template.format(year=2024, quarter=1, revenue=125000.50)

# Avoid - Old % formatting
message = "%s Dashboard - %d" % (name, year)

# Avoid - Concatenation
message = name + " Dashboard - " + str(year)
```

**Rationale**: f-strings are modern, readable, performant.

---

### Line Length

**Preferences**:
```python
# Good - Break long lines logically
def create_dashboard_with_filters(
    region_options: List[str],
    date_range: tuple,
    initial_data: pd.DataFrame,
    theme: str = "default"
) -> html.Div:
    ...

# Good - Break long chains
result = (
    df
    .query('revenue > 0')
    .groupby('region')
    .agg({'revenue': 'sum', 'count': 'size'})
    .reset_index()
)

# Avoid - Long lines (>88 characters per Black default)
def create_dashboard_with_filters(region_options: List[str], date_range: tuple, initial_data: pd.DataFrame, theme: str = "default") -> html.Div:
    ...
```

**Rationale**: 88 characters (Black default) balances readability and screen real estate.

---

## Anti-Patterns to Avoid

### Anti-Pattern 1: Hardcoded Secrets

**DON'T**:
```python
# NEVER do this
DATABASE_URL = "postgresql://user:password@localhost/db"
API_KEY = "sk-1234567890abcdef"
```

**DO**:
```python
import os

DATABASE_URL = os.getenv('DATABASE_URL')
API_KEY = os.getenv('API_KEY')

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable not set")
```

**Rationale**: Secrets in code lead to security vulnerabilities; use environment variables.

---

### Anti-Pattern 2: Global State in Dash Callbacks

**DON'T**:
```python
# Global mutable state
current_filter = None

@callback(Output(...), Input(...))
def update_chart(filter_value):
    global current_filter
    current_filter = filter_value  # Don't use global state
    ...
```

**DO**:
```python
# Use dcc.Store for state
@callback(
    Output('filter-store', 'data'),
    Input('filter-dropdown', 'value')
)
def update_filter_store(filter_value):
    return {'filter': filter_value}

@callback(
    Output('chart', 'figure'),
    Input('filter-store', 'data')
)
def update_chart(filter_data):
    filter_value = filter_data.get('filter')
    ...
```

**Rationale**: Global state causes issues with concurrent users; use dcc.Store for state management.

---

### Anti-Pattern 3: Bare Except Clauses

**DON'T**:
```python
try:
    df = pd.read_csv(file_path)
except:  # Catches everything, even KeyboardInterrupt!
    df = pd.DataFrame()
```

**DO**:
```python
try:
    df = pd.read_csv(file_path)
except FileNotFoundError:
    logger.error(f"File not found: {file_path}")
    df = pd.DataFrame()
except pd.errors.EmptyDataError:
    logger.warning(f"Empty file: {file_path}")
    df = pd.DataFrame()
```

**Rationale**: Bare except catches system exceptions; specific exceptions provide better error handling.

---

### Anti-Pattern 4: Mutating DataFrames In-Place

**DON'T**:
```python
def process_data(df: pd.DataFrame) -> pd.DataFrame:
    df['new_column'] = df['existing'] * 2  # Mutates original!
    df.dropna(inplace=True)  # Mutates original!
    return df
```

**DO**:
```python
def process_data(df: pd.DataFrame) -> pd.DataFrame:
    result = df.copy()
    result['new_column'] = result['existing'] * 2
    result = result.dropna()
    return result
```

**Rationale**: Mutation causes unexpected side effects; explicit copies make data flow clear.

---

### Anti-Pattern 5: Magic Numbers

**DON'T**:
```python
if revenue > 10000:
    tier = "premium"
elif revenue > 5000:
    tier = "standard"
else:
    tier = "basic"
```

**DO**:
```python
PREMIUM_THRESHOLD = 10000
STANDARD_THRESHOLD = 5000

if revenue > PREMIUM_THRESHOLD:
    tier = "premium"
elif revenue > STANDARD_THRESHOLD:
    tier = "standard"
else:
    tier = "basic"
```

**Rationale**: Named constants are self-documenting and easier to maintain.

---

### Anti-Pattern 6: Nested Callbacks

**DON'T**:
```python
@callback(Output(...), Input(...))
def outer_callback(value):
    @callback(Output(...), Input(...))  # Don't nest callbacks!
    def inner_callback(inner_value):
        ...
    ...
```

**DO**:
```python
@callback(Output('intermediate-store', 'data'), Input(...))
def first_callback(value):
    return process_value(value)

@callback(
    Output(...),
    Input('intermediate-store', 'data')
)
def second_callback(processed_value):
    return format_output(processed_value)
```

**Rationale**: Nested callbacks don't work in Dash; use chained callbacks with dcc.Store.

---

### Anti-Pattern 7: Testing Implementation Details

**DON'T**:
```python
def test_calculate_revenue_uses_multiplication():
    """Don't test implementation details"""
    # Checking internal implementation
    assert 'price * quantity' in inspect.getsource(calculate_revenue)
```

**DO**:
```python
def test_calculate_revenue_returns_correct_total():
    """Test behavior, not implementation"""
    result = calculate_revenue(price=10.0, quantity=5)
    assert result == 50.0
```

**Rationale**: Tests should validate behavior, not implementation; allows refactoring.

---

### Anti-Pattern 8: Premature Optimization

**DON'T**:
```python
# Optimizing before measuring
def load_data(file_path: str) -> pd.DataFrame:
    # Complex chunking logic before knowing if it's needed
    chunks = []
    for chunk in pd.read_csv(file_path, chunksize=10000):
        chunks.append(process_chunk(chunk))
    return pd.concat(chunks)
```

**DO**:
```python
# Simple first, optimize if needed
def load_data(file_path: str) -> pd.DataFrame:
    return pd.read_csv(file_path)

# If profiling shows this is slow, THEN optimize
```

**Rationale**: "Premature optimization is the root of all evil" - Donald Knuth. Measure first, optimize later.

---

### Anti-Pattern 9: Ignoring Type Hints

**DON'T**:
```python
def calculate_total(items):  # No type hints
    return sum(item['price'] for item in items)
```

**DO**:
```python
from typing import List, Dict

def calculate_total(items: List[Dict[str, float]]) -> float:
    return sum(item['price'] for item in items)
```

**Rationale**: Type hints catch errors early, improve IDE support, serve as documentation.

---

### Anti-Pattern 10: Not Using Context Managers

**DON'T**:
```python
f = open('data.csv', 'r')
data = f.read()
f.close()  # Easy to forget!
```

**DO**:
```python
with open('data.csv', 'r') as f:
    data = f.read()
# File automatically closed
```

**Rationale**: Context managers ensure cleanup happens even if exceptions occur.

---

## Testing Preferences

### Test File Organization

**Preferences**:
```
tests/
  unit/
    test_data_loaders.py       # Mirror src/ structure
    test_transformers.py
  integration/
    test_dashboard_flows.py
  e2e/
    test_user_journeys.py
  fixtures/
    sample_data.py             # Shared fixtures
  conftest.py                  # Pytest configuration
```

**Rationale**: Clear organization; easy to find tests for specific modules.

---

### Test Naming

**Preferences**:
```python
# Good - Descriptive test names
def test_load_sales_data_returns_dataframe_with_expected_columns():
    ...

def test_filter_sales_by_region_returns_only_matching_rows():
    ...

def test_calculate_revenue_raises_value_error_for_negative_price():
    ...

# Avoid - Vague test names
def test_load_data():
    ...

def test_filter():
    ...

def test_calculate_error():
    ...
```

**Rationale**: Descriptive names make test failures self-explanatory.

---

## Documentation Preferences

### README Structure

**Preferences**:
```markdown
# Project Name

Brief description (1-2 sentences)

## Quick Start

Minimal steps to get running

## Installation

Detailed setup instructions

## Usage

Common use cases with examples

## Development

How to contribute, run tests, etc.

## License
```

**Rationale**: Users want to get started quickly; detailed docs come later.

---

### Comment Usage

**Preferences**:
```python
# Good - Comments explain WHY, not WHAT
# Apply 20% discount for bulk orders (>100 units)
# Based on business rule BR-042
if quantity > 100:
    price = base_price * 0.8

# Avoid - Comments that just restate code
# Set price to base price times 0.8
price = base_price * 0.8

# Better - No comment needed, code is self-explanatory
BULK_DISCOUNT_RATE = 0.8
BULK_THRESHOLD = 100

if quantity > BULK_THRESHOLD:
    price = base_price * BULK_DISCOUNT_RATE
```

**Rationale**: Good code is self-documenting; comments should add context, not repeat code.

---

## Preferences to Add

As development progresses, add preferences for:

- [ ] Accessibility implementation preferences
- [ ] Performance optimization preferences
- [ ] Deployment configuration preferences
- [ ] Monitoring and logging preferences
- [ ] Error handling patterns

---

**Note**: This is a living document. Add preferences and anti-patterns as they're identified during development.
