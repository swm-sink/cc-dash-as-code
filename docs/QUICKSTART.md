# Quick Start Guide

This guide will get you up and running with spec-driven dashboard development in under 10 minutes.

## Prerequisites Check

Before starting, ensure you have:

```bash
# Python 3.11+
python3 --version

# Git
git --version

# pip
pip --version
```

## Step 1: Environment Setup (2 minutes)

1. **Create and activate virtual environment**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Verify installation**:
   ```bash
   python -c "import dash; print(f'Dash version: {dash.__version__}')"
   ```

## Step 2: Understand the Project Structure (3 minutes)

Familiarize yourself with the key directories:

```
cc-dash-as-code/
├── .specify/                    # ← Spec-driven development infrastructure
│   ├── memory/
│   │   └── constitution.md     # ← READ THIS FIRST: Project principles
│   ├── specs/
│   │   └── 001-dashboard-foundation/
│   │       └── spec.md         # ← Foundation specification
│   └── templates/              # ← Templates for new specs, plans, tasks
├── src/                        # ← Your dashboard code goes here
├── tests/                      # ← Your tests go here
└── reference/                  # ← Reference documentation (read-only)
```

### Essential Reading (in order):

1. **[Constitution](.specify/memory/constitution.md)** - Project principles and standards
2. **[Foundation Spec](.specify/specs/001-dashboard-foundation/spec.md)** - Core requirements
3. **[Spec-Kit README](../reference/spec-kit/README.md)** - Methodology overview

## Step 3: Create Your First Dashboard (5 minutes)

### 3.1 Create a Simple Dashboard

Create `src/app.py`:

```python
import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

# Initialize the Dash app
app = dash.Dash(__name__)

# Sample data
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    "Sales": [4000, 3000, 2000, 2780, 3908, 4800]
})

# Create a figure
fig = px.bar(df, x="Month", y="Sales", title="Monthly Sales")

# Define the layout
app.layout = html.Div([
    html.H1("My First Spec-Driven Dashboard"),
    html.P("This dashboard follows the spec-kit methodology"),
    dcc.Graph(figure=fig)
])

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8050)
```

### 3.2 Run the Dashboard

```bash
python src/app.py
```

Open your browser to **http://localhost:8050**

You should see a simple dashboard with a bar chart!

## Step 4: Follow Spec-Driven Workflow

Now that you have a working dashboard, let's follow the proper workflow:

### 4.1 Create a Feature Specification

For any new feature, create a spec first:

```bash
# Create a new feature directory
mkdir -p .specify/specs/002-sales-dashboard

# Copy the template
cp .specify/templates/spec-template.md .specify/specs/002-sales-dashboard/spec.md
```

Edit `spec.md` to define:
- **User stories**: Who needs this and why?
- **Requirements**: What must the feature do?
- **Success criteria**: How will we measure success?

### 4.2 Create a Technical Plan

Once the spec is approved:

```bash
# Copy the plan template
cp .specify/templates/plan-template.md .specify/specs/002-sales-dashboard/plan.md
```

Edit `plan.md` to detail:
- **Tech stack**: Which libraries and frameworks?
- **Architecture**: How will components interact?
- **Data flow**: Where does data come from and go?

### 4.3 Break Down Tasks

```bash
# Copy the tasks template
cp .specify/templates/tasks-template.md .specify/specs/002-sales-dashboard/tasks.md
```

Edit `tasks.md` to create:
- **Ordered tasks**: Step-by-step implementation
- **Dependencies**: What must be done first?
- **Test plan**: How to verify each task?

### 4.4 Implement with Tests

Follow TDD (Test-Driven Development):

1. Write a test that fails
2. Implement the minimum code to pass
3. Refactor
4. Repeat

Example test structure:

```python
# tests/test_app.py
import pytest
from src.app import app

def test_app_runs():
    """Test that the app initializes without errors."""
    assert app is not None

def test_layout_has_title():
    """Test that the layout includes a title."""
    layout = app.layout
    assert any("Dashboard" in str(child) for child in layout.children)
```

Run tests:
```bash
pytest tests/ -v
```

## Step 5: Code Quality Gates

Before committing, ensure your code meets standards:

### Format Code
```bash
black src/ tests/
```

### Lint Code
```bash
ruff check src/ tests/
```

### Type Check
```bash
mypy src/ --strict
```

### Check Coverage
```bash
pytest --cov=src --cov-report=html --cov-report=term
```

Ensure coverage is **≥ 80%**.

## Step 6: Commit and Push

Follow the constitution's guidelines:

```bash
# Create a feature branch
git checkout -b feature/002-sales-dashboard

# Add your changes
git add .

# Commit with a descriptive message
git commit -m "Add sales dashboard feature

- Implement monthly sales visualization
- Add responsive layout for mobile devices
- Achieve 85% test coverage
- All quality gates passing

Implements: .specify/specs/002-sales-dashboard/spec.md"

# Push to remote
git push -u origin feature/002-sales-dashboard
```

## Common Commands Cheat Sheet

### Development
```bash
# Start dev server with hot reload
python src/app.py

# Start in debug mode
DASH_DEBUG=true python src/app.py
```

### Testing
```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=html

# Run specific test file
pytest tests/test_app.py

# Run tests matching a pattern
pytest -k "test_layout"
```

### Code Quality
```bash
# Format all code
black .

# Check linting
ruff check .

# Auto-fix linting issues
ruff check --fix .

# Type check
mypy src/
```

### Dependencies
```bash
# Install new package
pip install package-name

# Update requirements.txt
pip freeze > requirements.txt

# Install from requirements.txt
pip install -r requirements.txt
```

## Troubleshooting

### Port Already in Use
```bash
# Find process using port 8050
lsof -i :8050

# Kill the process
kill -9 <PID>

# Or use a different port
python src/app.py --port 8051
```

### Import Errors
```bash
# Ensure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Tests Failing
```bash
# Run tests in verbose mode
pytest -vv

# Run with print statements visible
pytest -s

# Stop at first failure
pytest -x
```

## Next Steps

1. **Read the Constitution**: Understand project principles in `.specify/memory/constitution.md`
2. **Study the Foundation Spec**: Review `.specify/specs/001-dashboard-foundation/spec.md`
3. **Explore Reference Repos**:
   - Dash examples in `reference/dash/`
   - Spec-kit methodology in `reference/spec-kit/`
   - Agent SDK docs in `reference/claude-agent-sdk-python/`
4. **Create Your First Real Feature**: Follow the spec → plan → tasks → implement workflow
5. **Deploy to Production**: Use Claude Agent SDK for production deployment

## Resources

- **Plotly Dash Documentation**: https://dash.plotly.com/
- **Spec-Kit Guide**: [reference/spec-kit/spec-driven.md](../reference/spec-kit/spec-driven.md)
- **Python Testing**: https://docs.pytest.org/
- **Type Hints**: https://mypy.readthedocs.io/

## Getting Help

- **Check the documentation** in `docs/` and `reference/`
- **Review the constitution** for project standards
- **Ask Claude Code** for assistance during development
- **Open an issue** for bugs or feature requests

---

**Remember**: Always start with a specification, never with code. The spec-driven approach ensures you build the right thing, not just build things right.
