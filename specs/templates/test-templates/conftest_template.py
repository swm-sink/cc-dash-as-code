"""
pytest configuration and shared fixtures.

This conftest.py template provides reusable fixtures, configuration,
and test utilities to achieve 95%+ coverage while avoiding anti-patterns.

Place this file in your tests/ directory or subdirectories.
"""

from pathlib import Path
from typing import Any, Generator
from unittest.mock import Mock

import pandas as pd
import pytest
from dash import Dash


# ============================================================================
# PYTEST CONFIGURATION
# ============================================================================


def pytest_configure(config: Any) -> None:
    """Configure pytest with custom markers and settings.

    Args:
        config: pytest configuration object
    """
    config.addinivalue_line("markers", "slow: marks tests as slow (deselect with '-m \"not slow\"')")
    config.addinivalue_line("markers", "integration: marks tests as integration tests")
    config.addinivalue_line("markers", "e2e: marks tests as end-to-end tests")
    config.addinivalue_line("markers", "accessibility: marks tests for WCAG 2.1 AA compliance")


# ============================================================================
# APPLICATION FIXTURES
# ============================================================================


@pytest.fixture
def dash_app() -> Generator[Dash, None, None]:
    """Provide a Dash application instance for testing.

    Yields:
        Configured Dash application instance

    Cleanup:
        Stops the dash application after test
    """
    app = Dash(__name__, suppress_callback_exceptions=True)
    yield app
    # Cleanup: Dash apps don't need explicit cleanup in tests


@pytest.fixture
def dash_duo(dash_thread_server: Any) -> Any:
    """Provide Dash testing duo for browser-based tests.

    Note: Requires dash[testing] to be installed

    Args:
        dash_thread_server: Dash test server from dash.testing

    Returns:
        Dash duo instance for browser testing
    """
    # This is used for selenium-based testing
    # Requires: pip install dash[testing]
    return dash_thread_server


# ============================================================================
# DATA FIXTURES
# ============================================================================


@pytest.fixture
def sample_dataframe() -> pd.DataFrame:
    """Provide sample DataFrame for testing.

    Returns:
        Sample pandas DataFrame with realistic test data
    """
    return pd.DataFrame(
        {
            "date": pd.date_range("2024-01-01", periods=100, freq="D"),
            "region": ["North", "South", "East", "West"] * 25,
            "sales": [1000 + i * 10 for i in range(100)],
            "units": [50 + i for i in range(100)],
        }
    )


@pytest.fixture
def empty_dataframe() -> pd.DataFrame:
    """Provide empty DataFrame for edge case testing.

    Returns:
        Empty pandas DataFrame with correct schema
    """
    return pd.DataFrame(columns=["date", "region", "sales", "units"])


@pytest.fixture
def large_dataframe() -> pd.DataFrame:
    """Provide large DataFrame for performance testing.

    Returns:
        Large pandas DataFrame (100K rows) for performance tests
    """
    num_rows = 100_000
    return pd.DataFrame(
        {
            "date": pd.date_range("2020-01-01", periods=num_rows, freq="H"),
            "region": ["North", "South", "East", "West"] * (num_rows // 4),
            "sales": [1000 + i * 0.1 for i in range(num_rows)],
            "units": [50 + i * 0.01 for i in range(num_rows)],
        }
    )


@pytest.fixture
def dataframe_with_nulls() -> pd.DataFrame:
    """Provide DataFrame with null values for validation testing.

    Returns:
        pandas DataFrame containing null values
    """
    data = {
        "date": [pd.Timestamp("2024-01-01"), None, pd.Timestamp("2024-01-03")],
        "region": ["North", "South", None],
        "sales": [1000, None, 1200],
        "units": [50, 60, None],
    }
    return pd.DataFrame(data)


@pytest.fixture
def dataframe_with_invalid_types() -> pd.DataFrame:
    """Provide DataFrame with invalid data types for error testing.

    Returns:
        pandas DataFrame with type mismatches
    """
    return pd.DataFrame(
        {
            "date": ["not-a-date", "2024-01-02", "2024-01-03"],
            "region": [1, 2, 3],  # Should be strings
            "sales": ["not-a-number", "1000", "1200"],
            "units": [50.5, 60.5, 70.5],  # Should be integers
        }
    )


# ============================================================================
# FILE PATH FIXTURES
# ============================================================================


@pytest.fixture
def test_data_dir(tmp_path: Path) -> Path:
    """Provide temporary directory for test data files.

    Args:
        tmp_path: pytest temporary path fixture

    Returns:
        Path to temporary test data directory
    """
    data_dir = tmp_path / "test_data"
    data_dir.mkdir()
    return data_dir


@pytest.fixture
def sample_csv_file(test_data_dir: Path, sample_dataframe: pd.DataFrame) -> Path:
    """Create sample CSV file for testing.

    Args:
        test_data_dir: Temporary test data directory
        sample_dataframe: Sample data to write

    Returns:
        Path to created CSV file
    """
    csv_path = test_data_dir / "sample_data.csv"
    sample_dataframe.to_csv(csv_path, index=False)
    return csv_path


@pytest.fixture
def empty_csv_file(test_data_dir: Path, empty_dataframe: pd.DataFrame) -> Path:
    """Create empty CSV file for edge case testing.

    Args:
        test_data_dir: Temporary test data directory
        empty_dataframe: Empty DataFrame

    Returns:
        Path to created empty CSV file
    """
    csv_path = test_data_dir / "empty_data.csv"
    empty_dataframe.to_csv(csv_path, index=False)
    return csv_path


@pytest.fixture
def corrupted_csv_file(test_data_dir: Path) -> Path:
    """Create corrupted CSV file for error testing.

    Args:
        test_data_dir: Temporary test data directory

    Returns:
        Path to corrupted CSV file
    """
    csv_path = test_data_dir / "corrupted_data.csv"
    with open(csv_path, "w") as f:
        f.write("date,region,sales,units\n")
        f.write("2024-01-01,North,1000\n")  # Missing column
        f.write("invalid line with no structure\n")
    return csv_path


# ============================================================================
# MOCK FIXTURES
# ============================================================================


@pytest.fixture
def mock_database_connection() -> Mock:
    """Provide mock database connection for testing.

    Returns:
        Mock database connection object
    """
    mock_conn = Mock()
    mock_conn.execute.return_value = Mock()
    mock_conn.commit.return_value = None
    mock_conn.close.return_value = None
    return mock_conn


@pytest.fixture
def mock_api_response() -> dict[str, Any]:
    """Provide mock API response for testing.

    Returns:
        Dictionary representing API response
    """
    return {
        "status": "success",
        "data": [
            {"id": 1, "name": "Item 1", "value": 100},
            {"id": 2, "name": "Item 2", "value": 200},
            {"id": 3, "name": "Item 3", "value": 300},
        ],
        "total": 3,
    }


@pytest.fixture
def mock_failed_api_response() -> dict[str, Any]:
    """Provide mock failed API response for error testing.

    Returns:
        Dictionary representing failed API response
    """
    return {
        "status": "error",
        "message": "Internal server error",
        "code": 500,
    }


# ============================================================================
# COMPONENT FIXTURES
# ============================================================================


@pytest.fixture
def component_options() -> list[str]:
    """Provide standard component options for testing.

    Returns:
        List of option strings
    """
    return ["Option 1", "Option 2", "Option 3", "Option 4"]


@pytest.fixture
def component_id() -> str:
    """Provide standard component ID for testing.

    Returns:
        Component ID string
    """
    return "test-component"


@pytest.fixture
def accessibility_config() -> dict[str, Any]:
    """Provide WCAG 2.1 AA accessibility configuration.

    Returns:
        Dictionary of accessibility settings
    """
    return {
        "aria_labels": True,
        "semantic_html": True,
        "keyboard_navigation": True,
        "color_contrast_ratio": 4.5,
        "focus_indicators": True,
    }


# ============================================================================
# PERFORMANCE FIXTURES
# ============================================================================


@pytest.fixture
def performance_thresholds() -> dict[str, float]:
    """Provide performance thresholds for testing.

    Returns:
        Dictionary of performance limits (in seconds)
    """
    return {
        "initial_load": 3.0,  # 3 seconds
        "callback_execution": 1.0,  # 1 second
        "data_loading_100k": 1.0,  # 1 second for 100K rows
    }


# ============================================================================
# VALIDATION FIXTURES
# ============================================================================


@pytest.fixture
def valid_date_range() -> tuple[str, str]:
    """Provide valid date range for testing.

    Returns:
        Tuple of (start_date, end_date) as ISO strings
    """
    return ("2024-01-01", "2024-12-31")


@pytest.fixture
def invalid_date_range() -> tuple[str, str]:
    """Provide invalid date range for error testing.

    Returns:
        Tuple of (start_date, end_date) where start > end
    """
    return ("2024-12-31", "2024-01-01")


@pytest.fixture
def schema_definition() -> dict[str, type]:
    """Provide schema definition for data validation.

    Returns:
        Dictionary mapping column names to expected types
    """
    return {
        "date": pd.Timestamp,
        "region": str,
        "sales": float,
        "units": int,
    }


# ============================================================================
# PARAMETRIZATION HELPERS
# ============================================================================


# Define common parametrization data
VALID_REGIONS = ["North", "South", "East", "West"]
INVALID_REGIONS = ["", None, 123, [], {}]

VALID_DATES = ["2024-01-01", "2024-06-15", "2024-12-31"]
INVALID_DATES = ["not-a-date", "2024-13-01", "2024-01-32", "", None]

BOUNDARY_VALUES = [
    pytest.param(0, id="zero"),
    pytest.param(1, id="minimum"),
    pytest.param(1000, id="typical"),
    pytest.param(1_000_000, id="large"),
    pytest.param(float("inf"), id="infinity", marks=pytest.mark.xfail),
]


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================


def assert_dataframe_equal(
    df1: pd.DataFrame, df2: pd.DataFrame, check_dtype: bool = True
) -> None:
    """Assert two DataFrames are equal with better error messages.

    Args:
        df1: First DataFrame
        df2: Second DataFrame
        check_dtype: Whether to check data types match

    Raises:
        AssertionError: If DataFrames are not equal
    """
    pd.testing.assert_frame_equal(df1, df2, check_dtype=check_dtype)


def assert_coverage_above_threshold(coverage_percent: float, threshold: float = 95.0) -> None:
    """Assert test coverage is above threshold.

    Args:
        coverage_percent: Measured coverage percentage
        threshold: Minimum required coverage (default 95%)

    Raises:
        AssertionError: If coverage below threshold
    """
    assert coverage_percent >= threshold, (
        f"Coverage {coverage_percent}% is below threshold {threshold}%. "
        f"Add tests to cover missing lines/branches."
    )


# ============================================================================
# ANTI-PATTERN PREVENTION
# ============================================================================

"""
This conftest.py prevents common LLM anti-patterns:

✅ PREVENTS: Duplicated test setup code
   - Fixtures provide reusable test data

✅ PREVENTS: Hardcoded file paths
   - tmp_path fixture provides clean temporary directories

✅ PREVENTS: No test isolation
   - Each test gets fresh fixtures

✅ PREVENTS: Missing edge case data
   - Fixtures for empty, null, invalid, and large data

✅ PREVENTS: No parametrization support
   - Common parametrization data defined

✅ PREVENTS: Unclear test utilities
   - Helper functions with clear docstrings

✅ PREVENTS: No performance testing support
   - Performance threshold fixtures included

✅ PREVENTS: No accessibility testing support
   - WCAG 2.1 AA configuration fixtures

✅ PREVENTS: Magic numbers in tests
   - Named constants and threshold fixtures
"""
