# Feature Specification: Data Analysis Skills with LLM Anti-Pattern Prevention

**Feature Branch**: `006-data-analysis-skills`
**Created**: 2025-11-14
**Status**: Draft
**Approved**: [Pending]
**Input**: Research SQL and Python LLM anti-patterns and best practices to create comprehensive data analysis skills that integrate with 20 high-value sources/tools

---

## Overview

This specification defines advanced data analysis skills for Claude Code that prevent common LLM anti-patterns in SQL and Python code generation while integrating with 20 high-value data analysis tools and frameworks. These skills provide expertise in:

- **SQL Security and Performance**: Preventing SQL injection, optimizing queries, Text2SQL best practices
- **Python/Pandas Performance**: Vectorization over loops, efficient data types, avoiding common anti-patterns
- **Modern Data Frameworks**: Polars (5-10x faster), DuckDB (columnar analytics), high-performance alternatives
- **Data Validation**: Great Expectations (production) vs Pandera (lightweight), schema validation
- **Statistical Analysis**: scikit-learn (ML), statsmodels (rigorous statistics), time series analysis
- **Exploratory Data Analysis**: Automated EDA (ydata-profiling, Sweetviz), data profiling
- **Data Pipeline Orchestration**: Apache Airflow vs Prefect, versioning with DVC and MLflow
- **Security and Privacy**: GDPR compliance, anonymization techniques (k-anonymity, differential privacy)
- **Visualization Best Practices**: matplotlib, seaborn, plotly with accessibility

**Key Innovation**: First-class LLM anti-pattern detection and prevention specifically for data analysis code, ensuring generated SQL and Python code follows industry best practices.

**Constitutional Alignment**: All skills must produce code meeting 95% test coverage (line and branch), WCAG 2.1 AA compliance for visualizations, and <3s load time requirements.

---

## Key Principles

### 1. LLM Anti-Pattern Prevention First

All data analysis code generation must actively prevent known LLM anti-patterns:

**SQL Anti-Patterns**:
- ❌ String concatenation for queries → ✅ Parameterized queries
- ❌ Missing input sanitization → ✅ Strict validation and escaping
- ❌ Ignoring execution plans → ✅ EXPLAIN analysis
- ❌ No indexing strategy → ✅ Index-aware query design

**Python/Pandas Anti-Patterns**:
- ❌ Using loops over DataFrames → ✅ Vectorized operations
- ❌ Overusing .apply() → ✅ Native pandas methods
- ❌ Inefficient data types (object) → ✅ category, int32, datetime64
- ❌ Sequential mutations → ✅ Method chaining
- ❌ No memory management → ✅ Chunked processing, dtypes optimization

### 2. Performance-First Data Processing

Prioritize high-performance tools and patterns:
- **Polars over pandas** for large datasets (5-10x faster, multi-core, lazy evaluation)
- **DuckDB** for analytical queries (columnar, SQL on DataFrames)
- **Efficient pandas** when required (vectorization, categorical dtypes)
- **SQLAlchemy best practices** (avoid N+1 queries, use bulk operations, eager loading)

### 3. Data Quality and Validation

Enforce data quality at ingestion and transformation:
- **Schema validation**: Great Expectations (production) or Pandera (lightweight)
- **Type safety**: pydantic models for data contracts
- **Automated profiling**: ydata-profiling for initial EDA
- **Continuous validation**: Data quality checks in pipelines

### 4. Security and Privacy by Design

Build in security from the start:
- **SQL Injection Prevention**: Parameterized queries only, input validation
- **Data Anonymization**: k-anonymity, differential privacy techniques
- **GDPR Compliance**: Right to deletion, data minimization, audit trails
- **Secure Credentials**: Environment variables, secret management, no hardcoding

### 5. Reproducibility and Versioning

Enable reproducible data science:
- **DVC (Data Version Control)**: Track data and model versions
- **MLflow**: Experiment tracking, model registry
- **Pipeline orchestration**: Airflow (DAG-based) or Prefect (Pythonic, modern)
- **Environment management**: requirements.txt, conda, poetry

---

## User Stories

### US-001: SQL Query Generation Without Injection Vulnerabilities
**As a** dashboard developer
**I want** Claude to generate SQL queries using parameterized statements
**So that** my application is secure from SQL injection attacks

**Acceptance Criteria**:
- All generated SQL uses parameterized queries (?, :param)
- Input validation precedes query construction
- No string concatenation with user input
- SQLAlchemy ORM preferred over raw SQL
- SQL injection testing included in test suite

---

### US-002: High-Performance DataFrame Operations
**As a** data analyst
**I want** Claude to generate vectorized pandas operations instead of loops
**So that** my data processing is 10-100x faster

**Acceptance Criteria**:
- No .iterrows() or manual loops over DataFrames
- Vectorized operations (numpy, pandas) used
- Appropriate data types (category, int32) selected
- Memory profiling included for large datasets
- Alternative to Polars suggested for >1M rows

---

### US-003: Modern Data Framework Recommendations
**As a** data engineer
**I want** Claude to recommend Polars or DuckDB for performance-critical workloads
**So that** I can process large datasets efficiently

**Acceptance Criteria**:
- Polars suggested for DataFrames >100K rows
- DuckDB suggested for analytical SQL queries
- Performance comparisons provided (benchmarks)
- Migration path from pandas documented
- Memory usage comparisons included

---

### US-004: Automated Data Quality Validation
**As a** ML engineer
**I want** Claude to integrate Great Expectations or Pandera for data validation
**So that** data quality issues are caught early

**Acceptance Criteria**:
- Schema validation on data load
- Data quality checks (nulls, ranges, distributions)
- Great Expectations for production pipelines
- Pandera for lightweight validation
- Validation reports generated automatically

---

### US-005: Exploratory Data Analysis Automation
**As a** data scientist
**I want** Claude to generate EDA reports using ydata-profiling or Sweetviz
**So that** I can quickly understand new datasets

**Acceptance Criteria**:
- Automated EDA report generation
- ydata-profiling for comprehensive analysis
- Sweetviz for comparative analysis
- Statistical summaries (mean, std, quartiles)
- Visualization of distributions and correlations

---

### US-006: Statistical Analysis with Appropriate Tools
**As a** researcher
**I want** Claude to choose statsmodels for statistical inference and scikit-learn for ML
**So that** I use the right tool for each analysis

**Acceptance Criteria**:
- statsmodels for hypothesis testing, regression with p-values
- scikit-learn for predictive modeling
- Appropriate test selection (t-test, ANOVA, chi-square)
- Model diagnostics included (residuals, QQ plots)
- Documentation of assumptions checked

---

### US-007: Time Series Analysis
**As a** financial analyst
**I want** Claude to implement time series analysis with proper techniques
**So that** I can forecast trends accurately

**Acceptance Criteria**:
- Stationarity testing (ADF, KPSS)
- Appropriate models (ARIMA, SARIMA, Prophet, LSTMs)
- Seasonality detection and handling
- Cross-validation for time series (TimeSeriesSplit)
- Forecast visualization with confidence intervals

---

### US-008: Data Pipeline Orchestration
**As a** data engineer
**I want** Claude to set up Airflow or Prefect for pipeline orchestration
**So that** my data workflows are scheduled and monitored

**Acceptance Criteria**:
- DAG definition for Airflow or Flow for Prefect
- Task dependencies clearly defined
- Error handling and retries configured
- Monitoring and alerting set up
- Modern alternative (Prefect) recommended over Airflow for Python-first approach

---

### US-009: Data and Model Versioning
**As a** ML engineer
**I want** Claude to integrate DVC and MLflow for versioning
**So that** my experiments are reproducible

**Acceptance Criteria**:
- DVC for data and model versioning
- MLflow for experiment tracking
- Model registry for production models
- Reproducible training pipelines
- Artifact storage configured

---

### US-010: GDPR-Compliant Data Handling
**As a** compliance officer
**I want** Claude to implement data anonymization and GDPR requirements
**So that** we comply with privacy regulations

**Acceptance Criteria**:
- PII detection and masking
- k-anonymity or differential privacy techniques
- Right to deletion implementation
- Data minimization enforced
- Audit trails for data access

---

### US-011: Accessible Data Visualizations
**As a** dashboard developer
**I want** Claude to create WCAG 2.1 AA compliant visualizations
**So that** all users can access insights

**Acceptance Criteria**:
- Color-blind friendly palettes
- Sufficient color contrast (4.5:1)
- Alt text for charts
- Keyboard navigation support
- Screen reader compatibility

---

### US-012: SQLAlchemy ORM Best Practices
**As a** backend developer
**I want** Claude to avoid N+1 query problems in SQLAlchemy
**So that** my application performs well

**Acceptance Criteria**:
- No N+1 query anti-patterns
- Eager loading (joinedload, selectinload) used appropriately
- Bulk operations for inserts/updates
- Query profiling included
- Connection pooling configured

---

## Functional Requirements

### FR-001: SQL Injection Prevention
**Priority**: Critical
**Category**: Security

Claude must generate all SQL queries using parameterized statements or ORM methods that prevent SQL injection.

**Implementation**:
- Detect user input in SQL context
- Always use parameterized queries (?, :param, or %s with psycopg2)
- Validate and sanitize inputs before queries
- Prefer SQLAlchemy ORM over raw SQL
- Include SQL injection tests in test suite

**Test Coverage**: 95%+ with injection attempt tests

---

### FR-002: Pandas Vectorization Detection
**Priority**: High
**Category**: Performance

Claude must detect and prevent loop-based DataFrame operations, replacing them with vectorized alternatives.

**Implementation**:
- Scan generated code for .iterrows(), .itertuples(), manual for loops
- Suggest vectorized alternatives (numpy operations, pandas native methods)
- Provide performance comparison (loop vs vectorized)
- Include memory profiling for large DataFrames

**Test Coverage**: 95%+ with performance benchmarks

---

### FR-003: Polars Integration and Recommendations
**Priority**: High
**Category**: Performance

Claude must recommend and integrate Polars for datasets >100K rows, providing 5-10x performance improvements.

**Implementation**:
- Analyze dataset size and recommend Polars if appropriate
- Provide migration path from pandas to Polars
- Use lazy evaluation for memory efficiency
- Demonstrate multi-core processing benefits
- Include performance benchmarks (pandas vs Polars)

**Test Coverage**: 95%+ with performance comparisons

**Sources**:
- https://pola.rs/
- Polars benchmarks vs pandas (2025 latest)

---

### FR-004: DuckDB Integration for Analytics
**Priority**: Medium
**Category**: Performance

Claude must integrate DuckDB for analytical SQL queries on DataFrames, providing columnar storage benefits.

**Implementation**:
- Install and configure DuckDB
- Convert pandas DataFrames to DuckDB tables
- Generate optimized analytical queries
- Leverage columnar storage for aggregations
- Compare performance to pandas groupby

**Test Coverage**: 95%+ with query performance tests

**Sources**:
- https://duckdb.org/
- DuckDB pandas integration documentation

---

### FR-005: Great Expectations Integration
**Priority**: High
**Category**: Data Quality

Claude must integrate Great Expectations for production-grade data validation with comprehensive expectation suites.

**Implementation**:
- Set up Great Expectations project structure
- Create expectation suites for data schemas
- Implement data quality checks (nulls, ranges, distributions)
- Generate data quality reports (HTML, JSON)
- Integrate validation into data pipelines
- Configure checkpoints for automated validation

**Test Coverage**: 95%+ with validation failure scenarios

**Sources**:
- https://greatexpectations.io/
- Great Expectations documentation and examples

---

### FR-006: Pandera Lightweight Validation
**Priority**: Medium
**Category**: Data Quality

Claude must provide Pandera as a lightweight alternative to Great Expectations for simple validation use cases.

**Implementation**:
- Define Pandera schemas with type hints
- Implement validation decorators
- Handle validation errors gracefully
- Compare to Great Expectations (when to use each)
- Integration with pydantic for data contracts

**Test Coverage**: 95%+ with schema violation tests

**Sources**:
- https://pandera.readthedocs.io/
- Pandera vs Great Expectations comparison

---

### FR-007: ydata-profiling EDA Reports
**Priority**: Medium
**Category**: Exploratory Analysis

Claude must generate comprehensive EDA reports using ydata-profiling (formerly pandas-profiling).

**Implementation**:
- Install ydata-profiling
- Generate ProfileReport for datasets
- Export HTML reports with visualizations
- Analyze statistical summaries
- Identify data quality issues (missing values, correlations)
- Provide recommendations based on profile

**Test Coverage**: 95%+ with various dataset types

**Sources**:
- https://github.com/ydataai/ydata-profiling
- ydata-profiling documentation

---

### FR-008: Sweetviz Comparative EDA
**Priority**: Low
**Category**: Exploratory Analysis

Claude must use Sweetviz for comparative analysis between datasets (train vs test, before vs after).

**Implementation**:
- Install Sweetviz
- Generate comparative analysis reports
- Visualize target variable associations
- Compare distributions between datasets
- Export HTML reports

**Test Coverage**: 95%+ with dataset comparison scenarios

**Sources**:
- https://github.com/fbdesignpro/sweetviz
- Sweetviz documentation

---

### FR-009: scikit-learn for Predictive Modeling
**Priority**: High
**Category**: Machine Learning

Claude must use scikit-learn for predictive modeling with proper cross-validation and hyperparameter tuning.

**Implementation**:
- Select appropriate algorithms (classification, regression, clustering)
- Implement cross-validation (KFold, StratifiedKFold, TimeSeriesSplit)
- Hyperparameter tuning (GridSearchCV, RandomizedSearchCV)
- Feature engineering (preprocessing, scaling, encoding)
- Model evaluation (metrics, confusion matrix, ROC curves)
- Avoid data leakage (fit on train only)

**Test Coverage**: 95%+ with pipeline tests

**Sources**:
- https://scikit-learn.org/
- scikit-learn best practices documentation

---

### FR-010: statsmodels for Statistical Inference
**Priority**: Medium
**Category**: Statistical Analysis

Claude must use statsmodels for statistical hypothesis testing and regression with p-values and diagnostics.

**Implementation**:
- Select appropriate statistical tests (t-test, ANOVA, chi-square)
- Implement regression models (OLS, GLM, mixed effects)
- Generate diagnostic plots (residuals, QQ plots)
- Report p-values, confidence intervals, R-squared
- Check assumptions (normality, homoscedasticity)

**Test Coverage**: 95%+ with statistical test scenarios

**Sources**:
- https://www.statsmodels.org/
- statsmodels regression documentation

---

### FR-011: Time Series Analysis
**Priority**: Medium
**Category**: Time Series

Claude must implement time series analysis with stationarity testing, appropriate models, and forecasting.

**Implementation**:
- Test for stationarity (ADF, KPSS)
- Implement ARIMA, SARIMA for univariate series
- Use Prophet for business time series with holidays
- Implement LSTMs for complex patterns
- Seasonal decomposition (STL, classical)
- Cross-validation for time series (expanding window)
- Forecast with confidence intervals

**Test Coverage**: 95%+ with synthetic time series

**Sources**:
- statsmodels ARIMA/SARIMA
- Prophet: https://facebook.github.io/prophet/
- Keras LSTMs for time series

---

### FR-012: SQLAlchemy ORM Best Practices
**Priority**: High
**Category**: Database

Claude must implement SQLAlchemy ORM patterns that avoid N+1 queries and performance anti-patterns.

**Implementation**:
- Use eager loading (joinedload, selectinload) for relationships
- Implement bulk operations (bulk_insert_mappings)
- Avoid lazy loading in loops
- Configure connection pooling
- Use query profiling and logging
- Implement proper session management

**Test Coverage**: 95%+ with query count assertions

**Sources**:
- https://docs.sqlalchemy.org/
- SQLAlchemy performance tips
- N+1 query detection

---

### FR-013: Apache Airflow DAG Creation
**Priority**: Medium
**Category**: Orchestration

Claude must create Airflow DAGs for data pipeline orchestration with proper dependencies and error handling.

**Implementation**:
- Define DAGs with tasks and dependencies
- Implement operators (PythonOperator, BashOperator, etc.)
- Configure retries and error handling
- Set up monitoring and alerting
- Use TaskGroups for organization
- Configure scheduling (cron expressions)

**Test Coverage**: 95%+ with DAG validation tests

**Sources**:
- https://airflow.apache.org/
- Airflow best practices documentation

---

### FR-014: Prefect Modern Orchestration
**Priority**: Medium
**Category**: Orchestration

Claude must recommend Prefect as a modern, Pythonic alternative to Airflow for new projects.

**Implementation**:
- Define Flows with tasks
- Implement task dependencies
- Configure retry logic and error handling
- Set up monitoring dashboard
- Use Prefect Cloud or self-hosted
- Compare to Airflow (when to use each)

**Test Coverage**: 95%+ with flow execution tests

**Sources**:
- https://www.prefect.io/
- Prefect 2.0 documentation
- Airflow vs Prefect comparison

---

### FR-015: DVC Data Versioning
**Priority**: Medium
**Category**: Versioning

Claude must integrate DVC for data and model versioning, enabling reproducible data science workflows.

**Implementation**:
- Initialize DVC repository
- Track data files with DVC (.dvc files)
- Configure remote storage (S3, GCS, Azure)
- Version models and datasets
- Create reproducible pipelines
- Document data lineage

**Test Coverage**: 95%+ with DVC commands

**Sources**:
- https://dvc.org/
- DVC documentation and tutorials

---

### FR-016: MLflow Experiment Tracking
**Priority**: Medium
**Category**: Versioning

Claude must integrate MLflow for experiment tracking, parameter logging, and model registry.

**Implementation**:
- Set up MLflow tracking server
- Log parameters, metrics, artifacts
- Register models in model registry
- Version models (staging, production)
- Compare experiments in UI
- Serve models via MLflow

**Test Coverage**: 95%+ with experiment logging tests

**Sources**:
- https://mlflow.org/
- MLflow documentation

---

### FR-017: Data Anonymization Techniques
**Priority**: High
**Category**: Privacy

Claude must implement data anonymization techniques (k-anonymity, differential privacy) for GDPR compliance.

**Implementation**:
- PII detection and masking
- k-anonymity implementation (generalization, suppression)
- Differential privacy (noise addition)
- Data minimization strategies
- Right to deletion (hard delete vs soft delete)
- Audit trails for data access

**Test Coverage**: 95%+ with anonymization scenarios

**Sources**:
- GDPR compliance guides
- Differential privacy libraries (diffprivlib)
- k-anonymity algorithms

---

### FR-018: WCAG 2.1 AA Visualization Compliance
**Priority**: High
**Category**: Accessibility

Claude must create data visualizations that comply with WCAG 2.1 Level AA accessibility standards.

**Implementation**:
- Use color-blind friendly palettes (ColorBrewer, Viridis)
- Ensure color contrast ratio ≥4.5:1
- Provide alt text for charts
- Support keyboard navigation
- Include data tables alongside visualizations
- Use patterns/textures in addition to color

**Test Coverage**: 95%+ with accessibility audits

**Sources**:
- WCAG 2.1 AA guidelines
- ColorBrewer palettes
- Plotly accessibility features

---

### FR-019: matplotlib/seaborn/plotly Best Practices
**Priority**: Medium
**Category**: Visualization

Claude must recommend appropriate visualization libraries and follow best practices for each.

**Implementation**:
- matplotlib for full customization and publication-quality
- seaborn for statistical visualizations (distributions, regression)
- plotly for interactive dashboards
- Appropriate chart selection guide (bar vs line vs scatter)
- Styling and theming
- Performance optimization for large datasets

**Test Coverage**: 95%+ with rendering tests

**Sources**:
- matplotlib documentation
- seaborn gallery
- plotly documentation

---

### FR-020: Database Query Optimization
**Priority**: High
**Category**: Performance

Claude must analyze and optimize database queries using indexing, execution plans, and query rewriting.

**Implementation**:
- Use EXPLAIN/EXPLAIN ANALYZE for query plans
- Identify missing indexes
- Rewrite inefficient queries (subqueries → joins)
- Implement proper indexing strategies
- Use query caching where appropriate
- Monitor query performance

**Test Coverage**: 95%+ with query performance tests

**Sources**:
- PostgreSQL query optimization
- MySQL query optimization
- Database indexing best practices

---

## Success Criteria

### SC-001: Zero SQL Injection Vulnerabilities
**Measurement**: Security scanning tools (Bandit, safety) report zero SQL injection vulnerabilities in generated code.

**Target**: 100% of generated SQL queries use parameterized statements.

**Validation**:
- Run Bandit security scanner on generated code
- Manual security code review
- Penetration testing with OWASP Top 10 SQL injection payloads

---

### SC-002: 5-10x Performance Improvement with Polars
**Measurement**: Benchmark pandas vs Polars operations on 1M+ row datasets.

**Target**: Polars operations complete in <1 second for operations taking pandas 5-10 seconds.

**Validation**:
- Performance benchmarks in test suite
- Memory profiling comparisons
- Real-world dataset testing

---

### SC-003: 95%+ Test Coverage for Generated Code
**Measurement**: pytest --cov-branch reports ≥95% line and branch coverage.

**Target**: All data analysis skills generate code with 95%+ coverage.

**Validation**:
- Automated coverage reporting
- Coverage gate in CI/CD
- Branch coverage analysis

---

### SC-004: Automated Data Quality Detection
**Measurement**: Great Expectations or Pandera detects data quality issues in <3 seconds.

**Target**: 100% of data ingestion points have validation checks.

**Validation**:
- Validation checkpoint execution
- Data quality reports generated
- Failure scenarios tested

---

### SC-005: WCAG 2.1 AA Visualization Compliance
**Measurement**: Accessibility audit tools report WCAG 2.1 AA compliance for all visualizations.

**Target**: 100% of visualizations pass color contrast and screen reader tests.

**Validation**:
- Automated accessibility testing (axe-core)
- Manual screen reader testing
- Color contrast verification

---

### SC-006: Reproducible ML Experiments
**Measurement**: DVC and MLflow track 100% of experiment artifacts.

**Target**: Any experiment can be reproduced from DVC/MLflow artifacts.

**Validation**:
- Reproduce experiment from artifacts
- Verify identical results
- Data lineage documentation complete

---

### SC-007: Zero N+1 Query Anti-Patterns
**Measurement**: SQLAlchemy query logging shows no N+1 query patterns.

**Target**: All relationship queries use eager loading.

**Validation**:
- Query count assertions in tests
- Database query logging analysis
- Performance profiling

---

### SC-008: Comprehensive EDA in <10 Seconds
**Measurement**: ydata-profiling generates EDA report in <10 seconds for datasets <100K rows.

**Target**: HTML report with statistical summaries, distributions, correlations.

**Validation**:
- Performance benchmarks
- Report completeness verification
- Multiple dataset types tested

---

## Technical Design

### Architecture Overview

```
┌──────────────────────────────────────────────────────────────────┐
│                    Data Analysis Skills Layer                     │
├──────────────────────────────────────────────────────────────────┤
│                                                                    │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐    │
│  │ SQL Security   │  │ Performance    │  │ Data Quality   │    │
│  │ & Optimization │  │ Optimization   │  │ Validation     │    │
│  ├────────────────┤  ├────────────────┤  ├────────────────┤    │
│  │ • Parameterized│  │ • Polars       │  │ • Great Expect.│    │
│  │   queries      │  │ • DuckDB       │  │ • Pandera      │    │
│  │ • SQLAlchemy   │  │ • Vectorization│  │ • Schema valid.│    │
│  │ • Query plans  │  │ • Efficient    │  │ • Quality      │    │
│  │ • Indexing     │  │   dtypes       │  │   checks       │    │
│  └────────────────┘  └────────────────┘  └────────────────┘    │
│                                                                    │
│  ┌────────────────┐  ┌────────────────┐  ┌────────────────┐    │
│  │ Statistical    │  │ EDA & Profiling│  │ Orchestration  │    │
│  │ Analysis       │  │                │  │ & Versioning   │    │
│  ├────────────────┤  ├────────────────┤  ├────────────────┤    │
│  │ • scikit-learn │  │ • ydata-profile│  │ • Airflow      │    │
│  │ • statsmodels  │  │ • Sweetviz     │  │ • Prefect      │    │
│  │ • Time series  │  │ • Automated    │  │ • DVC          │    │
│  │ • Cross-val    │  │   insights     │  │ • MLflow       │    │
│  └────────────────┘  └────────────────┘  └────────────────┘    │
│                                                                    │
│  ┌────────────────┐  ┌────────────────┐                         │
│  │ Privacy &      │  │ Visualization  │                         │
│  │ Security       │  │ & Accessibility│                         │
│  ├────────────────┤  ├────────────────┤                         │
│  │ • GDPR         │  │ • WCAG 2.1 AA  │                         │
│  │ • Anonymization│  │ • Color-blind  │                         │
│  │ • k-anonymity  │  │ • Plotly       │                         │
│  │ • Diff privacy │  │ • Seaborn      │                         │
│  └────────────────┘  └────────────────┘                         │
│                                                                    │
└──────────────────────────────────────────────────────────────────┘
```

### Skill Activation Patterns

**SQL Context Activation**:
- Keywords: "SQL", "query", "database", "SELECT", "INSERT", "UPDATE", "DELETE"
- File patterns: `*.sql`, `*_queries.py`, `*_database.py`
- Imports: `sqlalchemy`, `psycopg2`, `pymysql`, `sqlite3`

**Pandas/Polars Activation**:
- Imports: `pandas`, `polars`
- Keywords: "DataFrame", "data processing", "ETL"
- File patterns: `*_etl.py`, `*_transform.py`

**Data Validation Activation**:
- Keywords: "validation", "schema", "data quality"
- Imports: `great_expectations`, `pandera`, `pydantic`
- File patterns: `*_validation.py`, `*_schema.py`

**EDA Activation**:
- Keywords: "exploratory", "EDA", "profiling", "distribution"
- Imports: `ydata_profiling`, `sweetviz`
- File patterns: `*_eda.py`, `*_analysis.py`

**ML/Statistics Activation**:
- Imports: `sklearn`, `statsmodels`, `prophet`, `tensorflow`, `torch`
- Keywords: "model", "train", "predict", "forecast", "regression", "classification"
- File patterns: `*_model.py`, `*_train.py`

**Orchestration Activation**:
- Imports: `airflow`, `prefect`
- Keywords: "pipeline", "DAG", "flow", "orchestration"
- File patterns: `dags/*`, `flows/*`, `*_pipeline.py`

**Privacy/Security Activation**:
- Keywords: "GDPR", "anonymize", "privacy", "PII", "sensitive"
- Imports: `diffprivlib`
- File patterns: `*_privacy.py`, `*_security.py`

### Integration Points

**With Existing Skills**:
- `data-analysis` skill (from Spec 004) → Enhanced with LLM anti-pattern prevention
- `plotly-viz` skill → Enhanced with accessibility requirements
- `dash-components` skill → Enhanced with data validation integration

**With Commands**:
- `/workflow:act` → Uses skills during implementation
- `/workflow:verify` → Validates against anti-patterns
- `/utils:test` → Ensures 95% coverage requirement
- `/utils:lint` → Security scanning (Bandit)

**With MCP Servers** (optional):
- `mcp__postgres` → SQL query generation and optimization
- `mcp__filesystem` → Data file access and profiling
- `mcp__fetch` → API data ingestion

### Anti-Pattern Detection System

**Detection Mechanism**:
1. **Static Analysis**: Scan generated code for anti-patterns using AST parsing
2. **Runtime Detection**: Profile code execution for performance issues
3. **Test Coverage**: Ensure anti-pattern scenarios are tested
4. **Security Scanning**: Bandit for SQL injection, hardcoded secrets

**Anti-Pattern Catalog**:
```python
SQL_ANTIPATTERNS = {
    "string_concatenation": {
        "pattern": r"SELECT .* \+ .*",
        "message": "Use parameterized queries instead of string concatenation",
        "severity": "CRITICAL",
    },
    "missing_where_clause": {
        "pattern": r"DELETE FROM .* (?!WHERE)",
        "message": "DELETE without WHERE clause is dangerous",
        "severity": "HIGH",
    },
}

PANDAS_ANTIPATTERNS = {
    "iterrows_loop": {
        "pattern": r"\.iterrows\(\)",
        "message": "Use vectorized operations instead of iterrows()",
        "severity": "HIGH",
    },
    "object_dtype": {
        "pattern": r"dtype=object",
        "message": "Use category dtype for categorical data",
        "severity": "MEDIUM",
    },
}
```

**Enforcement**:
- Pre-commit hooks run anti-pattern detection
- CI/CD pipeline fails on CRITICAL anti-patterns
- `/workflow:verify` includes anti-pattern report
- Test suite includes anti-pattern detection tests

---

## 20 High-Value Sources and Tools

### 1. **Polars** (https://pola.rs/)
**Category**: DataFrame Library
**Value**: 5-10x faster than pandas, multi-core, lazy evaluation
**Integration**: FR-003

### 2. **DuckDB** (https://duckdb.org/)
**Category**: Analytical Database
**Value**: Columnar storage, SQL on DataFrames, embedded analytics
**Integration**: FR-004

### 3. **Great Expectations** (https://greatexpectations.io/)
**Category**: Data Quality
**Value**: Production-grade data validation, expectation suites
**Integration**: FR-005

### 4. **Pandera** (https://pandera.readthedocs.io/)
**Category**: Data Validation
**Value**: Lightweight schema validation, type hints integration
**Integration**: FR-006

### 5. **ydata-profiling** (https://github.com/ydataai/ydata-profiling)
**Category**: EDA
**Value**: Automated comprehensive EDA reports
**Integration**: FR-007

### 6. **Sweetviz** (https://github.com/fbdesignpro/sweetviz)
**Category**: EDA
**Value**: Comparative analysis, target variable associations
**Integration**: FR-008

### 7. **scikit-learn** (https://scikit-learn.org/)
**Category**: Machine Learning
**Value**: Comprehensive ML library, pipelines, cross-validation
**Integration**: FR-009

### 8. **statsmodels** (https://www.statsmodels.org/)
**Category**: Statistical Analysis
**Value**: Rigorous statistical inference, p-values, diagnostics
**Integration**: FR-010

### 9. **Prophet** (https://facebook.github.io/prophet/)
**Category**: Time Series
**Value**: Business time series forecasting, holiday effects
**Integration**: FR-011

### 10. **SQLAlchemy** (https://docs.sqlalchemy.org/)
**Category**: ORM
**Value**: Pythonic database access, query optimization
**Integration**: FR-012

### 11. **Apache Airflow** (https://airflow.apache.org/)
**Category**: Orchestration
**Value**: DAG-based pipeline orchestration, scheduling
**Integration**: FR-013

### 12. **Prefect** (https://www.prefect.io/)
**Category**: Orchestration
**Value**: Modern, Pythonic workflow orchestration
**Integration**: FR-014

### 13. **DVC (Data Version Control)** (https://dvc.org/)
**Category**: Versioning
**Value**: Git-like versioning for data and models
**Integration**: FR-015

### 14. **MLflow** (https://mlflow.org/)
**Category**: MLOps
**Value**: Experiment tracking, model registry, serving
**Integration**: FR-016

### 15. **diffprivlib** (IBM Differential Privacy Library)
**Category**: Privacy
**Value**: Differential privacy algorithms, anonymization
**Integration**: FR-017

### 16. **Plotly** (https://plotly.com/python/)
**Category**: Visualization
**Value**: Interactive dashboards, Dash integration
**Integration**: FR-018, FR-019

### 17. **Seaborn** (https://seaborn.pydata.org/)
**Category**: Visualization
**Value**: Statistical visualizations, beautiful defaults
**Integration**: FR-019

### 18. **Bandit** (https://bandit.readthedocs.io/)
**Category**: Security
**Value**: Security linting for Python, SQL injection detection
**Integration**: FR-001 (validation)

### 19. **PostgreSQL** (https://www.postgresql.org/)
**Category**: Database
**Value**: Advanced features, EXPLAIN ANALYZE, query optimization
**Integration**: FR-020

### 20. **ColorBrewer** (https://colorbrewer2.org/)
**Category**: Accessibility
**Value**: Color-blind friendly palettes, WCAG compliance
**Integration**: FR-018

---

## Dependencies

### Required Specifications
- **Spec 002**: Claude Code Commands Setup (provides `/workflow:*` commands)
- **Spec 004**: Production Skills (extends `data-analysis` skill)

### Optional Specifications
- **Spec 005**: MCP Integration (optional data source access)

### Python Package Dependencies
```
# Performance
polars>=0.20.0
duckdb>=0.10.0

# Data Quality
great-expectations>=0.18.0
pandera>=0.17.0

# EDA
ydata-profiling>=4.6.0
sweetviz>=2.3.0

# ML/Statistics
scikit-learn>=1.4.0
statsmodels>=0.14.0
prophet>=1.1.0

# Database
sqlalchemy>=2.0.0
psycopg2-binary>=2.9.0

# Orchestration
apache-airflow>=2.8.0
prefect>=2.14.0

# Versioning
dvc>=3.0.0
mlflow>=2.10.0

# Privacy
diffprivlib>=0.6.0

# Visualization
plotly>=5.18.0
matplotlib>=3.8.0
seaborn>=0.13.0

# Security
bandit>=1.7.0

# Testing
pytest>=7.4.0
pytest-cov>=4.1.0
pytest-benchmark>=4.0.0
```

### System Dependencies
- Python 3.11+
- Virtual environment (venv or conda)
- Database (PostgreSQL, SQLite)
- Git + DVC

---

## Clarifications

### Q1: When to use Polars vs Pandas?
**A**: Use Polars for:
- Datasets >100K rows
- Performance-critical pipelines
- Multi-core processing requirements
- Memory-constrained environments

Use pandas for:
- Small datasets (<100K rows)
- Legacy codebase compatibility
- Ecosystem dependencies (e.g., libraries requiring pandas)

### Q2: Great Expectations vs Pandera?
**A**:
- **Great Expectations**: Production data pipelines, comprehensive validation suites, team collaboration, data documentation
- **Pandera**: Lightweight validation, development phase, type-hint integration, simple schemas

### Q3: Airflow vs Prefect?
**A**:
- **Airflow**: Mature ecosystem, DAG-based, complex dependencies, large teams
- **Prefect**: Modern Python-first API, easier learning curve, better developer experience, new projects

### Q4: How to enforce SQL injection prevention?
**A**:
- Static analysis during code generation
- Bandit security scanning in CI/CD
- Test suite with injection payloads
- Code review checklist
- Pre-commit hooks

### Q5: Coverage requirements for generated code?
**A**: 95% line and branch coverage per Spec 002 constitution update. All generated code must meet this threshold.

---

## Implementation Phases

### Phase 1: SQL Security and Performance (FR-001, FR-012, FR-020)
- SQL injection prevention
- SQLAlchemy ORM best practices
- Query optimization

### Phase 2: Pandas Performance and Polars (FR-002, FR-003, FR-004)
- Vectorization detection
- Polars integration
- DuckDB integration

### Phase 3: Data Quality (FR-005, FR-006)
- Great Expectations integration
- Pandera lightweight validation

### Phase 4: EDA and Profiling (FR-007, FR-008)
- ydata-profiling reports
- Sweetviz comparative analysis

### Phase 5: ML and Statistics (FR-009, FR-010, FR-011)
- scikit-learn best practices
- statsmodels integration
- Time series analysis

### Phase 6: Orchestration and Versioning (FR-013, FR-014, FR-015, FR-016)
- Airflow DAGs
- Prefect flows
- DVC data versioning
- MLflow experiment tracking

### Phase 7: Privacy and Accessibility (FR-017, FR-018, FR-019)
- Data anonymization
- WCAG 2.1 AA visualizations
- Visualization best practices

---

## Approval Checklist

- [ ] All functional requirements (FR-001 to FR-020) defined
- [ ] Success criteria (SC-001 to SC-008) measurable
- [ ] 20 high-value sources documented with integration points
- [ ] Constitutional alignment (95% coverage, WCAG 2.1 AA, <3s load)
- [ ] Anti-pattern detection system designed
- [ ] Dependencies identified
- [ ] Implementation phases planned
- [ ] Skill activation patterns defined
- [ ] Integration with existing specs (002, 004)
- [ ] Test strategy covers all anti-patterns

---

**Status**: Ready for review and approval

**Next Steps**:
1. Review specification for completeness
2. Approve or request clarifications
3. Create plan.md with detailed implementation plan
4. Create tasks.md with actionable tasks
5. Begin implementation with `/workflow:observe`
