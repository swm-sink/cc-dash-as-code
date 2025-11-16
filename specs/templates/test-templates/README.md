# Test Templates and Scaffolding

This directory contains test templates and scaffolding to achieve 95%+ test coverage while avoiding LLM anti-patterns.

## Templates Available

1. **component_test_template.py** - Dash component testing
2. **data_loader_test_template.py** - Data pipeline testing
3. **callback_test_template.py** - Dash callback testing
4. **integration_test_template.py** - Integration testing
5. **conftest_template.py** - pytest fixtures and configuration
6. **factory_template.py** - Test data factories

## Usage

Copy the appropriate template and customize for your module. All templates include:
- ✅ 95%+ coverage patterns
- ✅ AAA (Arrange-Act-Assert) structure
- ✅ Edge case testing
- ✅ Error path testing
- ✅ Type hints and docstrings
- ✅ Parametrization examples
- ✅ Fixture usage
- ❌ No LLM anti-patterns

## Quick Start

```bash
# Copy template for your test
cp specs/templates/test-templates/component_test_template.py tests/unit/components/test_my_component.py

# Customize the template
# - Replace MyComponent with your component name
# - Add component-specific test cases
# - Ensure all branches are covered
# - Run coverage: pytest --cov=src --cov-branch
```

## Coverage Requirements

- **Minimum**: 95% line coverage
- **Branch Coverage**: Required
- **Missing Coverage**: Justify with comments
- **Edge Cases**: Required for all public functions
- **Error Paths**: Required for all exception handling

## Anti-Pattern Detection

Tests are automatically checked for LLM anti-patterns:
- ❌ Generic test names (`test_function`, `test_component`)
- ❌ Missing assertions
- ❌ Hardcoded values without explanation
- ❌ Incomplete error testing
- ❌ No parametrization for similar tests
- ❌ Missing docstrings
- ❌ Unclear test purpose
- ❌ No edge case coverage
- ❌ Magic numbers without constants
- ❌ Overly complex test logic

See individual templates for correct patterns.
