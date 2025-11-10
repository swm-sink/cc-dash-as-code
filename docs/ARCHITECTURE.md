# Project Architecture

## Overview

This document describes the architectural approach for the spec-driven dashboard development project, including how specifications, code, and deployment infrastructure work together.

## Architecture Principles

### 1. Specification-Driven Design
```
┌─────────────────┐
│  Specification  │ ← Defines WHAT and WHY
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Technical Plan  │ ← Defines HOW (tech stack, architecture)
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Task Breakdown │ ← Defines step-by-step implementation
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Implementation  │ ← Executable code following spec
└─────────────────┘
```

### 2. Separation of Concerns

The project is organized into clear, independent layers:

```
┌──────────────────────────────────────────────────────┐
│                  User Interface Layer                │
│         (Dash Components, Layouts, Styling)          │
└────────────────┬─────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────┐
│                 Callback Layer                       │
│          (User Interactions, State Updates)          │
└────────────────┬─────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────┐
│              Business Logic Layer                    │
│      (Data Processing, Transformations, Rules)       │
└────────────────┬─────────────────────────────────────┘
                 │
                 ▼
┌──────────────────────────────────────────────────────┐
│                 Data Layer                           │
│         (Data Sources, APIs, Databases)              │
└──────────────────────────────────────────────────────┘
```

### 3. Development vs. Production

```
┌────────────────────┐              ┌─────────────────────┐
│  Development Env   │              │   Production Env    │
│                    │              │                     │
│  ┌──────────────┐  │              │  ┌──────────────┐   │
│  │ Claude Code  │  │              │  │ Agent SDK    │   │
│  │              │  │              │  │              │   │
│  │ - Hot reload │  │              │  │ - Orchestrate│   │
│  │ - Debug mode │  │              │  │ - Scale      │   │
│  │ - Rapid iter │  │              │  │ - Monitor    │   │
│  └──────────────┘  │              │  └──────────────┘   │
│         │          │              │         │           │
│         ▼          │              │         ▼           │
│  ┌──────────────┐  │              │  ┌──────────────┐   │
│  │ Dash Dev     │  │              │  │ Dash Prod    │   │
│  │ Server       │  │              │  │ (Gunicorn)   │   │
│  │ :8050        │  │              │  │ :8050        │   │
│  └──────────────┘  │              │  └──────────────┘   │
└────────────────────┘              └─────────────────────┘
```

## Directory Structure Details

### `.specify/` - Specification Infrastructure

```
.specify/
├── memory/
│   └── constitution.md         # Project-wide principles and standards
├── specs/
│   └── {nnn}-{feature-name}/  # Each feature gets its own directory
│       ├── spec.md            # Feature specification (WHAT & WHY)
│       ├── plan.md            # Technical plan (HOW)
│       ├── tasks.md           # Implementation tasks (STEPS)
│       ├── data-model.md      # Data structures (optional)
│       └── contracts/         # API specs, interfaces (optional)
├── templates/
│   ├── spec-template.md       # Template for new specifications
│   ├── plan-template.md       # Template for technical plans
│   └── tasks-template.md      # Template for task breakdowns
└── scripts/
    └── (helper scripts for automation)
```

### `src/` - Application Source Code

```
src/
├── app.py                     # Main application entry point
├── components/                # Reusable Dash components
│   ├── __init__.py
│   ├── charts/               # Chart components
│   │   ├── __init__.py
│   │   ├── bar_chart.py
│   │   ├── line_chart.py
│   │   └── scatter_plot.py
│   ├── layouts/              # Layout components
│   │   ├── __init__.py
│   │   ├── sidebar.py
│   │   ├── header.py
│   │   └── grid.py
│   └── controls/             # Control components (dropdowns, sliders, etc.)
│       ├── __init__.py
│       ├── date_picker.py
│       └── filter_panel.py
├── data/                     # Data access and processing
│   ├── __init__.py
│   ├── loaders.py           # Data loading utilities
│   ├── transformers.py      # Data transformation functions
│   └── validators.py        # Data validation
├── models/                   # Data models (Pydantic)
│   ├── __init__.py
│   └── dashboard_config.py  # Configuration models
├── utils/                    # Utility functions
│   ├── __init__.py
│   ├── logging.py           # Logging configuration
│   └── config.py            # Configuration management
└── dashboards/              # Individual dashboard implementations
    ├── __init__.py
    ├── sales_dashboard.py
    └── analytics_dashboard.py
```

### `tests/` - Test Suite

```
tests/
├── __init__.py
├── conftest.py              # Pytest configuration and fixtures
├── unit/                    # Unit tests (fast, isolated)
│   ├── __init__.py
│   ├── test_components.py
│   ├── test_data_loaders.py
│   └── test_transformers.py
├── integration/             # Integration tests (components working together)
│   ├── __init__.py
│   ├── test_callbacks.py
│   └── test_data_flow.py
└── e2e/                    # End-to-end tests (full user journeys)
    ├── __init__.py
    └── test_dashboard_workflows.py
```

### `agents/` - Claude Agent SDK Configuration

```
agents/
├── config/
│   ├── agent_config.yaml    # Agent capabilities and settings
│   ├── resources.yaml       # Resource limits (CPU, memory)
│   └── secrets.yaml.example # Template for secrets (NOT committed)
├── deployment/
│   ├── Dockerfile           # Container image for production
│   ├── docker-compose.yml   # Local multi-container setup
│   └── k8s/                # Kubernetes manifests (if using K8s)
└── monitoring/
    ├── health_checks.py     # Health check endpoints
    └── metrics.py           # Custom metrics collection
```

### `docs/` - Documentation

```
docs/
├── QUICKSTART.md           # Quick start guide
├── ARCHITECTURE.md         # This file
├── API.md                  # API documentation (if applicable)
├── DEPLOYMENT.md           # Deployment instructions
└── diagrams/               # Architecture diagrams
    └── (Mermaid or PlantUML files)
```

## Data Flow Architecture

### User Interaction Flow

```
┌─────────────────────────────────────────────────────────────────┐
│                         Browser (Client)                        │
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐         │
│  │   Layout     │  │  Components  │  │   Controls   │         │
│  │   (HTML)     │  │  (Plotly)    │  │  (Dropdowns) │         │
│  └──────┬───────┘  └──────┬───────┘  └──────┬───────┘         │
│         │                 │                 │                  │
│         └─────────────────┴─────────────────┘                  │
│                           │                                     │
│                           │ User interaction (click, change)    │
└───────────────────────────┼─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                      Dash Server (Backend)                      │
│                                                                 │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                   Callback Handler                       │  │
│  │                                                          │  │
│  │  @app.callback(                                         │  │
│  │      Output('chart', 'figure'),                         │  │
│  │      Input('dropdown', 'value')                         │  │
│  │  )                                                       │  │
│  │  def update_chart(selected_value):                      │  │
│  │      # Process input                                    │  │
│  │      # Fetch/transform data                             │  │
│  │      # Return updated figure                            │  │
│  └──────────────┬───────────────────────────────────────────┘  │
│                 │                                               │
│                 ▼                                               │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │              Business Logic Layer                        │  │
│  │  - Data transformation                                   │  │
│  │  - Filtering, aggregation                               │  │
│  │  - Validation                                            │  │
│  └──────────────┬───────────────────────────────────────────┘  │
│                 │                                               │
│                 ▼                                               │
│  ┌──────────────────────────────────────────────────────────┐  │
│  │                  Data Layer                              │  │
│  │  - Load from CSV, Database, API                          │  │
│  │  - Cache frequently accessed data                        │  │
│  └──────────────┬───────────────────────────────────────────┘  │
└─────────────────┼───────────────────────────────────────────────┘
                  │
                  ▼
         ┌─────────────────┐
         │  External Data  │
         │  - Database     │
         │  - API          │
         │  - Files        │
         └─────────────────┘
```

## Component Architecture

### Reusable Component Pattern

```python
# src/components/charts/bar_chart.py
from dash import dcc
import plotly.graph_objs as go
from typing import List, Dict, Any

def create_bar_chart(
    data: List[Dict[str, Any]],
    x_field: str,
    y_field: str,
    title: str,
    **kwargs
) -> dcc.Graph:
    """
    Create a reusable bar chart component.

    Args:
        data: List of dictionaries containing chart data
        x_field: Field name for x-axis
        y_field: Field name for y-axis
        title: Chart title
        **kwargs: Additional Plotly figure arguments

    Returns:
        dcc.Graph: Configured Dash graph component
    """
    figure = go.Figure(
        data=[
            go.Bar(
                x=[item[x_field] for item in data],
                y=[item[y_field] for item in data]
            )
        ],
        layout=go.Layout(
            title=title,
            **kwargs
        )
    )

    return dcc.Graph(figure=figure, id=f"bar-chart-{title.lower().replace(' ', '-')}")
```

### Callback Pattern

```python
# src/app.py
from dash import Dash, Input, Output, State
from src.components.charts.bar_chart import create_bar_chart
from src.data.loaders import load_sales_data
from src.data.transformers import filter_by_date_range

app = Dash(__name__)

@app.callback(
    Output('sales-chart', 'figure'),
    Input('date-range', 'start_date'),
    Input('date-range', 'end_date'),
    State('product-filter', 'value')
)
def update_sales_chart(start_date, end_date, product_filter):
    """
    Update sales chart based on date range and product filter.

    This callback demonstrates:
    - Loading data from the data layer
    - Transforming data based on user inputs
    - Returning updated figure to the UI
    """
    # Load raw data
    raw_data = load_sales_data()

    # Transform data based on filters
    filtered_data = filter_by_date_range(raw_data, start_date, end_date)

    if product_filter:
        filtered_data = [
            item for item in filtered_data
            if item['product'] == product_filter
        ]

    # Create figure
    chart = create_bar_chart(
        data=filtered_data,
        x_field='date',
        y_field='sales',
        title='Sales Over Time'
    )

    return chart.figure
```

## Testing Architecture

### Test Pyramid

```
                    ┌─────────────┐
                    │     E2E     │  ← Few, slow, high-value
                    │   (10%)     │     Full user journeys
                    └──────┬──────┘
                           │
                 ┌─────────┴─────────┐
                 │   Integration     │  ← Some, moderate speed
                 │     (30%)         │     Component interactions
                 └─────────┬─────────┘
                           │
              ┌────────────┴────────────┐
              │        Unit             │  ← Many, fast, focused
              │        (60%)            │     Individual functions
              └─────────────────────────┘
```

### Test Coverage Strategy

1. **Unit Tests** (60% of tests)
   - Individual functions in isolation
   - Data transformations
   - Utility functions
   - Model validation

2. **Integration Tests** (30% of tests)
   - Callback behavior
   - Component interactions
   - Data flow from source to UI
   - State management

3. **E2E Tests** (10% of tests)
   - Critical user journeys
   - Multi-step workflows
   - Cross-browser compatibility
   - Accessibility validation

## Deployment Architecture

### Local Development

```
┌─────────────────────────────────────────────┐
│          Developer Laptop                   │
│                                             │
│  ┌───────────────────────────────────────┐  │
│  │     Python Virtual Environment        │  │
│  │                                       │  │
│  │  Dash Dev Server (port 8050)         │  │
│  │  - Hot reload enabled                │  │
│  │  - Debug mode                        │  │
│  │  - SQLite (local data)               │  │
│  └───────────────────────────────────────┘  │
│                                             │
│  Access: http://localhost:8050              │
└─────────────────────────────────────────────┘
```

### Production Deployment

```
┌──────────────────────────────────────────────────────────────┐
│                    Load Balancer (HTTPS)                     │
└───────────┬────────────────────────────────┬─────────────────┘
            │                                │
            ▼                                ▼
┌─────────────────────┐          ┌─────────────────────┐
│  App Instance 1     │          │  App Instance 2     │
│                     │          │                     │
│  ┌───────────────┐  │          │  ┌───────────────┐  │
│  │ Claude Agent  │  │          │  │ Claude Agent  │  │
│  │     SDK       │  │          │  │     SDK       │  │
│  └───────┬───────┘  │          │  └───────┬───────┘  │
│          │          │          │          │          │
│          ▼          │          │          ▼          │
│  ┌───────────────┐  │          │  ┌───────────────┐  │
│  │   Gunicorn    │  │          │  │   Gunicorn    │  │
│  │ (Dash app)    │  │          │  │ (Dash app)    │  │
│  └───────────────┘  │          │  └───────────────┘  │
└──────────┬──────────┘          └──────────┬──────────┘
           │                                │
           └────────────┬───────────────────┘
                        │
                        ▼
              ┌──────────────────┐
              │  Shared Services │
              │                  │
              │  - Database      │
              │  - Redis Cache   │
              │  - S3 Storage    │
              └──────────────────┘
```

## Security Architecture

### Secrets Management

```
┌─────────────────────────────────────────────────────────┐
│                 Application Code                        │
│                 (No hardcoded secrets)                  │
└────────────────────────┬────────────────────────────────┘
                         │
                         │ Reads from environment
                         ▼
┌─────────────────────────────────────────────────────────┐
│              Environment Variables                      │
│              (Injected at runtime)                      │
└────────────────────────┬────────────────────────────────┘
                         │
                         │ Sourced from
                         ▼
┌─────────────────────────────────────────────────────────┐
│           Secret Management System                      │
│           (AWS Secrets Manager, HashiCorp Vault, etc.)  │
└─────────────────────────────────────────────────────────┘
```

### Input Validation

```
User Input
    │
    ▼
┌─────────────────┐
│  Sanitization   │ ← Remove/escape dangerous characters
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Validation    │ ← Check type, format, range
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Authorization  │ ← Verify user can access this data
└────────┬────────┘
         │
         ▼
   Process Input
```

## Monitoring & Observability

### Metrics Collection

```
┌──────────────────────────────────────────────┐
│           Dash Application                   │
│                                              │
│  ┌────────────────────────────────────────┐  │
│  │  Application Metrics                   │  │
│  │  - Request count                       │  │
│  │  - Response time                       │  │
│  │  - Error rate                          │  │
│  │  - Active users                        │  │
│  └──────────────┬─────────────────────────┘  │
│                 │                            │
│  ┌──────────────┴─────────────────────────┐  │
│  │  Business Metrics                      │  │
│  │  - Dashboard views                     │  │
│  │  - Feature usage                       │  │
│  │  - Data refresh frequency              │  │
│  └──────────────┬─────────────────────────┘  │
└─────────────────┼────────────────────────────┘
                  │
                  │ Export to
                  ▼
         ┌─────────────────┐
         │   Prometheus    │
         │   (Metrics DB)  │
         └────────┬────────┘
                  │
                  │ Visualize in
                  ▼
         ┌─────────────────┐
         │    Grafana      │
         │  (Dashboards)   │
         └─────────────────┘
```

## Scalability Considerations

### Horizontal Scaling

- **Stateless application**: No session state stored in app instances
- **Shared cache**: Redis for cross-instance caching
- **Load balancing**: Distribute traffic across multiple instances
- **Auto-scaling**: Scale instances based on CPU/memory/request metrics

### Performance Optimization

1. **Data Layer**
   - Cache frequently accessed data
   - Implement data pagination
   - Use efficient data structures (Pandas DataFrames)

2. **Visualization Layer**
   - Lazy load charts (render on viewport entry)
   - Virtualize large datasets (show subset, load on scroll)
   - Debounce user inputs to reduce callback frequency

3. **Callback Optimization**
   - Use `prevent_initial_call=True` when appropriate
   - Implement long callbacks for time-intensive operations
   - Cache callback results when inputs haven't changed

## Future Architecture Enhancements

### Planned Improvements

1. **Authentication & Authorization**
   - User login system
   - Role-based access control (RBAC)
   - API key management

2. **Real-time Data**
   - WebSocket connections for live updates
   - Server-sent events for data streaming

3. **Advanced Caching**
   - Multi-tier caching (in-memory → Redis → Database)
   - Cache invalidation strategies
   - Cache warming on deployment

4. **Microservices Architecture**
   - Separate data processing services
   - Dedicated API gateway
   - Service mesh for inter-service communication

---

*This architecture is designed to scale from a single developer working locally to a production system serving thousands of users. The spec-driven approach ensures all architectural decisions are documented and aligned with project requirements.*
