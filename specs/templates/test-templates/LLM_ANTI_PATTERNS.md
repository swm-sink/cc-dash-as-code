# LLM Anti-Patterns in Testing

This document identifies common anti-patterns that LLMs produce when generating tests, and provides corrections to achieve 95%+ coverage.

## 🎯 95% Coverage Requirements

- **Minimum Line Coverage**: 95%
- **Branch Coverage**: Required (95%+)
- **Edge Cases**: All boundary conditions
- **Error Paths**: All exception handling
- **Accessibility**: WCAG 2.1 AA tests for UI

---

## ❌ Anti-Pattern 1: Generic Test Names

### BAD (LLM Anti-Pattern)
```python
def test_function():
    """Test the function."""
    result = my_function()
    assert result
```

### GOOD (Correct Pattern)
```python
def test_my_function_returns_valid_dataframe_with_expected_columns() -> None:
    """Test my_function returns DataFrame with date, region, sales columns.

    Verifies:
    - Returns pd.DataFrame type
    - Contains all required columns
    - No missing data in required columns
    """
    # Arrange
    input_data = load_test_data()

    # Act
    result = my_function(input_data)

    # Assert
    assert isinstance(result, pd.DataFrame)
    assert list(result.columns) == ["date", "region", "sales"]
    assert result.notna().all().all()
```

**Why**:
- Specific names document what is being tested
- Makes test failures easier to diagnose
- Self-documenting code

---

## ❌ Anti-Pattern 2: Missing Assertions

### BAD (LLM Anti-Pattern)
```python
def test_component():
    component = create_component()
    # Test passes but validates nothing!
```

### GOOD (Correct Pattern)
```python
def test_component_renders_with_required_structure() -> None:
    """Test component renders with Div container and Dropdown child."""
    # Arrange
    options = ["A", "B", "C"]

    # Act
    component = create_component(options)

    # Assert
    assert isinstance(component, html.Div), "Must return html.Div container"
    assert len(component.children) > 0, "Container must have children"
    assert isinstance(component.children[0], dcc.Dropdown), "First child must be Dropdown"
```

**Why**:
- Tests without assertions pass even when code is broken
- Each assertion should have a failure message
- Multiple specific assertions are better than one vague assertion

---

## ❌ Anti-Pattern 3: Hardcoded Magic Numbers

### BAD (LLM Anti-Pattern)
```python
def test_data_loading():
    df = load_data()
    assert len(df) == 1000  # What is 1000?
    assert df["sales"].max() < 50000  # What is 50000?
```

### GOOD (Correct Pattern)
```python
# In module constants
EXPECTED_ROW_COUNT = 1000
MAX_SALES_VALUE = 50_000

def test_data_loading_returns_expected_row_count() -> None:
    """Test load_data returns 1000 rows as per test dataset specification."""
    # Arrange
    test_file = "test_data_1000_rows.csv"

    # Act
    df = load_data(test_file)

    # Assert
    assert len(df) == EXPECTED_ROW_COUNT, (
        f"Expected {EXPECTED_ROW_COUNT} rows, got {len(df)}"
    )

def test_data_loading_validates_sales_within_business_limits() -> None:
    """Test sales values do not exceed $50,000 maximum per business rules."""
    # Arrange
    test_file = "test_data_valid_sales.csv"

    # Act
    df = load_data(test_file)

    # Assert
    assert df["sales"].max() <= MAX_SALES_VALUE, (
        f"Sales {df['sales'].max()} exceeds maximum ${MAX_SALES_VALUE:,}"
    )
```

**Why**:
- Named constants make tests self-documenting
- Easy to update when requirements change
- Failure messages are clearer

---

## ❌ Anti-Pattern 4: No Edge Case Testing

### BAD (LLM Anti-Pattern)
```python
def test_filter_data():
    """Only tests happy path."""
    df = pd.DataFrame({"value": [1, 2, 3]})
    result = filter_data(df, min_value=2)
    assert len(result) == 2
```

### GOOD (Correct Pattern)
```python
class TestFilterDataEdgeCases:
    """Test filter_data with boundary conditions and edge cases."""

    def test_filter_with_empty_dataframe(self) -> None:
        """Test filter_data handles empty DataFrame gracefully."""
        # Arrange
        empty_df = pd.DataFrame(columns=["value"])

        # Act
        result = filter_data(empty_df, min_value=0)

        # Assert
        assert len(result) == 0
        assert list(result.columns) == ["value"]

    def test_filter_with_all_values_below_minimum(self) -> None:
        """Test filter_data returns empty when all values filtered out."""
        # Arrange
        df = pd.DataFrame({"value": [1, 2, 3]})

        # Act
        result = filter_data(df, min_value=10)

        # Assert
        assert len(result) == 0

    def test_filter_with_all_values_above_minimum(self) -> None:
        """Test filter_data returns all rows when all pass filter."""
        # Arrange
        df = pd.DataFrame({"value": [10, 20, 30]})

        # Act
        result = filter_data(df, min_value=5)

        # Assert
        assert len(result) == 3

    def test_filter_with_exact_boundary_value(self) -> None:
        """Test filter_data handles min_value boundary correctly (inclusive)."""
        # Arrange
        df = pd.DataFrame({"value": [5, 10, 15]})

        # Act
        result = filter_data(df, min_value=10)

        # Assert
        assert len(result) == 2  # 10 and 15 (inclusive)
        assert result["value"].min() == 10
```

**Why**:
- Edge cases often contain bugs
- Boundary conditions must be tested explicitly
- 95% coverage requires testing all branches

---

## ❌ Anti-Pattern 5: No Error Path Testing

### BAD (LLM Anti-Pattern)
```python
def test_load_csv():
    """Only tests successful loading."""
    df = load_csv("test_data.csv")
    assert len(df) > 0
```

### GOOD (Correct Pattern)
```python
class TestLoadCsvErrorHandling:
    """Test CSV loading error paths and validation."""

    def test_load_csv_raises_file_not_found_for_missing_file(self) -> None:
        """Test load_csv raises FileNotFoundError with clear message."""
        # Arrange
        nonexistent_file = "does_not_exist.csv"

        # Act & Assert
        with pytest.raises(FileNotFoundError, match="does_not_exist.csv"):
            load_csv(nonexistent_file)

    def test_load_csv_raises_value_error_for_invalid_schema(self) -> None:
        """Test load_csv raises ValueError when required columns missing."""
        # Arrange
        invalid_csv = create_csv_missing_columns()

        # Act & Assert
        with pytest.raises(ValueError, match="Missing required columns: \\['date', 'sales'\\]"):
            load_csv(invalid_csv)

    def test_load_csv_raises_type_error_for_corrupted_data(self) -> None:
        """Test load_csv raises TypeError when data types invalid."""
        # Arrange
        corrupted_csv = create_csv_with_invalid_types()

        # Act & Assert
        with pytest.raises(TypeError, match="Column 'sales' must be numeric"):
            load_csv(corrupted_csv)
```

**Why**:
- Error handling is critical for robustness
- Each exception type should be tested
- Error messages should be validated

---

## ❌ Anti-Pattern 6: No Parametrization

### BAD (LLM Anti-Pattern)
```python
def test_validate_region_north():
    assert validate_region("North") is True

def test_validate_region_south():
    assert validate_region("South") is True

def test_validate_region_east():
    assert validate_region("East") is True

def test_validate_region_west():
    assert validate_region("West") is True
```

### GOOD (Correct Pattern)
```python
@pytest.mark.parametrize(
    "region,expected",
    [
        pytest.param("North", True, id="valid_north"),
        pytest.param("South", True, id="valid_south"),
        pytest.param("East", True, id="valid_east"),
        pytest.param("West", True, id="valid_west"),
        pytest.param("Invalid", False, id="invalid_region"),
        pytest.param("", False, id="empty_string"),
        pytest.param(None, False, id="none_value"),
    ],
)
def test_validate_region_with_various_inputs(region: str | None, expected: bool) -> None:
    """Test validate_region with valid and invalid region names.

    Args:
        region: Region name to validate
        expected: Expected validation result
    """
    # Arrange - provided by parametrize

    # Act
    result = validate_region(region)

    # Assert
    assert result == expected, f"validate_region('{region}') should be {expected}"
```

**Why**:
- Reduces code duplication (DRY)
- Easier to add new test cases
- Better test organization
- Clearer test output with IDs

---

## ❌ Anti-Pattern 7: Missing Docstrings

### BAD (LLM Anti-Pattern)
```python
def test_callback():
    input_val = "test"
    result = update_chart(input_val)
    assert result is not None
```

### GOOD (Correct Pattern)
```python
def test_update_chart_callback_returns_figure_when_region_selected() -> None:
    """Test update_chart callback returns valid Plotly figure for region selection.

    Verifies:
    - Returns dictionary (Plotly figure format)
    - Contains 'data' and 'layout' keys
    - Data includes filtered region values
    - Layout includes proper title

    Args:
        None (uses mock data)

    Returns:
        None (assertion-based test)
    """
    # Arrange
    selected_region = "North"
    mock_data = get_mock_sales_data()

    # Act
    figure = update_chart(selected_region)

    # Assert
    assert isinstance(figure, dict), "Figure must be dictionary"
    assert "data" in figure, "Figure must have 'data' key"
    assert "layout" in figure, "Figure must have 'layout' key"
    assert selected_region in str(figure["layout"]["title"]), "Title must include region"
```

**Why**:
- Documents what the test verifies
- Explains why test exists
- Makes test intent clear to future developers

---

## ❌ Anti-Pattern 8: No Fixture Usage

### BAD (LLM Anti-Pattern)
```python
def test_component_creation():
    options = ["A", "B", "C"]  # Duplicated setup
    component = create_component(options)
    assert component is not None

def test_component_props():
    options = ["A", "B", "C"]  # Same setup duplicated
    component = create_component(options)
    assert component.children[0].options == options
```

### GOOD (Correct Pattern)
```python
@pytest.fixture
def standard_options() -> list[str]:
    """Provide standard test options for component testing."""
    return ["A", "B", "C"]

@pytest.fixture
def test_component(standard_options: list[str]) -> html.Div:
    """Create component with standard options for testing."""
    return create_component(standard_options)

def test_component_creation(test_component: html.Div) -> None:
    """Test component is created successfully."""
    assert test_component is not None
    assert isinstance(test_component, html.Div)

def test_component_props(test_component: html.Div, standard_options: list[str]) -> None:
    """Test component receives correct options prop."""
    dropdown = test_component.children[0]
    option_values = [opt["value"] for opt in dropdown.options]
    assert option_values == standard_options
```

**Why**:
- DRY (Don't Repeat Yourself)
- Centralized test setup
- Easy to modify test data
- Better test isolation

---

## ❌ Anti-Pattern 9: No Branch Coverage

### BAD (LLM Anti-Pattern)
```python
def test_process_data():
    """Only tests one branch of if/else."""
    result = process_data(valid=True)
    assert result == "valid"
    # Never tests valid=False branch!
```

### GOOD (Correct Pattern)
```python
class TestProcessDataBranches:
    """Test all branches in process_data function."""

    def test_process_data_valid_branch_returns_success(self) -> None:
        """Test process_data returns 'valid' when valid=True branch executes."""
        # Arrange
        valid_flag = True

        # Act
        result = process_data(valid=valid_flag)

        # Assert
        assert result == "valid", "Valid branch should return 'valid'"

    def test_process_data_invalid_branch_returns_error(self) -> None:
        """Test process_data returns 'invalid' when valid=False branch executes."""
        # Arrange
        valid_flag = False

        # Act
        result = process_data(valid=valid_flag)

        # Assert
        assert result == "invalid", "Invalid branch should return 'invalid'"

    @pytest.mark.parametrize(
        "valid,expected",
        [
            (True, "valid"),
            (False, "invalid"),
        ],
    )
    def test_process_data_all_branches(self, valid: bool, expected: str) -> None:
        """Test both branches of process_data with parametrization."""
        result = process_data(valid=valid)
        assert result == expected
```

**Why**:
- 95% coverage requires testing all branches
- If statements create branches that must be tested
- Use `pytest --cov-branch` to measure

---

## ❌ Anti-Pattern 10: No Accessibility Testing

### BAD (LLM Anti-Pattern)
```python
def test_component():
    """UI component test without accessibility checks."""
    component = create_button("Click Me")
    assert component is not None
```

### GOOD (Correct Pattern)
```python
class TestButtonAccessibility:
    """Test button component WCAG 2.1 AA compliance."""

    def test_button_has_aria_label(self) -> None:
        """Test button includes ARIA label for screen readers.

        WCAG 2.1: 4.1.2 Name, Role, Value (Level A)
        """
        # Arrange & Act
        button = create_button("Click Me")

        # Assert
        assert hasattr(button, "aria-label") or hasattr(button, "title"), (
            "Button must have aria-label or title for screen readers"
        )

    def test_button_uses_semantic_html(self) -> None:
        """Test button uses semantic HTML element.

        WCAG 2.1: 1.3.1 Info and Relationships (Level A)
        """
        # Arrange & Act
        button = create_button("Click Me")

        # Assert
        assert isinstance(button, html.Button), (
            "Must use html.Button, not html.Div with onClick"
        )

    def test_button_keyboard_accessible(self) -> None:
        """Test button is keyboard accessible.

        WCAG 2.1: 2.1.1 Keyboard (Level A)
        """
        # Arrange & Act
        button = create_button("Click Me")

        # Assert
        # html.Button is natively keyboard accessible
        assert isinstance(button, html.Button), (
            "html.Button provides native keyboard support"
        )
```

**Why**:
- Accessibility is a requirement (WCAG 2.1 AA)
- UI components need specific accessibility tests
- Prevents regression in accessibility features

---

## ✅ Coverage Checklist

Before claiming 95% coverage, verify:

- [ ] **Line Coverage**: ≥95% of all lines executed
- [ ] **Branch Coverage**: ≥95% of all branches tested
- [ ] **Edge Cases**: Empty, null, boundary values tested
- [ ] **Error Paths**: All exceptions and error handling tested
- [ ] **Happy Paths**: All successful execution paths tested
- [ ] **Integration**: Component interactions tested
- [ ] **Accessibility**: WCAG 2.1 AA compliance tested (UI only)
- [ ] **Performance**: Targets validated (if applicable)
- [ ] **Parametrization**: Similar tests use @pytest.mark.parametrize
- [ ] **Fixtures**: Common setup uses pytest fixtures
- [ ] **Docstrings**: All tests have clear docstrings
- [ ] **AAA Structure**: All tests follow Arrange-Act-Assert
- [ ] **Type Hints**: All test functions have type hints
- [ ] **Assertions**: All assertions have failure messages

---

## 🔍 Anti-Pattern Detection

Run these checks before committing tests:

```bash
# Check coverage with branch measurement
pytest --cov=src --cov-branch --cov-report=term-missing

# Check for generic test names
grep -r "def test_function\|def test_component\|def test_data" tests/

# Check for missing docstrings
ruff check tests/ --select D

# Check for missing type hints
mypy tests/

# Check for hardcoded values (manual review)
grep -r "assert.*==" tests/ | grep -E "[0-9]{3,}"

# Run strict pytest configuration
pytest --strict-markers --strict-config
```

---

## 📚 Additional Resources

- [pytest Best Practices](https://docs.pytest.org/en/stable/goodpractices.html)
- [WCAG 2.1 Guidelines](https://www.w3.org/WAI/WCAG21/quickref/)
- [Test-Driven Development](https://martinfowler.com/bliki/TestDrivenDevelopment.html)
- [AAA Pattern](http://wiki.c2.com/?ArrangeActAssert)

---

## 🎓 Summary

**LLM Anti-Patterns to Avoid**:
1. ❌ Generic test names
2. ❌ Missing assertions
3. ❌ Hardcoded magic numbers
4. ❌ No edge case testing
5. ❌ No error path testing
6. ❌ No parametrization
7. ❌ Missing docstrings
8. ❌ No fixture usage
9. ❌ No branch coverage
10. ❌ No accessibility testing

**Correct Patterns to Follow**:
1. ✅ Specific, descriptive test names
2. ✅ Multiple clear assertions with messages
3. ✅ Named constants instead of magic numbers
4. ✅ Comprehensive edge case testing
5. ✅ All error paths tested with pytest.raises
6. ✅ Parametrization for similar tests
7. ✅ Google-style docstrings for all tests
8. ✅ Fixtures for reusable test data
9. ✅ Branch coverage measured and achieved
10. ✅ WCAG 2.1 AA accessibility tests for UI

**Result**: 95%+ coverage with robust, maintainable tests
