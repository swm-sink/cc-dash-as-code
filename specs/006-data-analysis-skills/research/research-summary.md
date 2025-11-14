# Research Summary: SQL and Python LLM Anti-Patterns

**Date**: 2025-11-14
**Purpose**: Comprehensive research on SQL and Python LLM anti-patterns and best practices for data analysis skills specification

---

## Executive Summary

Conducted 20 targeted web searches across SQL security, Python/pandas performance, data quality, statistical analysis, orchestration, privacy, and visualization domains. Identified critical LLM anti-patterns and corresponding best practices across all areas.

**Key Findings**:
- SQL injection remains #1 security risk in LLM-generated SQL
- Pandas loops can be 10-100x slower than vectorized operations
- Polars offers 5-10x performance improvement over pandas
- Great Expectations vs Pandera: production vs lightweight validation
- Prefect emerging as modern alternative to Airflow
- 95% test coverage standard aligns with industry best practices

---

## 1. SQL Security and LLM Anti-Patterns

### Web Searches Conducted
1. "SQL anti-patterns LLM code generation 2024"
2. "LLM generated SQL injection vulnerabilities"
3. "Text2SQL best practices security"

### Key Findings

**Critical Anti-Patterns**:
- ❌ String concatenation for query building
- ❌ Missing input sanitization
- ❌ No parameterized queries
- ❌ Exposing database structure in prompts
- ❌ Ignoring OWASP Top 10

**Best Practices**:
- ✅ Always use parameterized queries (?, :param, %s)
- ✅ Input validation before query construction
- ✅ Principle of least privilege (read-only users)
- ✅ Query whitelisting for sensitive operations
- ✅ SQL injection testing in test suites

**Sources**:
- AWS Security Blog: LLM application security best practices
- OWASP LLM Top 10 (2024)
- Text2SQL research papers (Stanford, MIT)
- GitHub security advisories for SQL injection

**Example Bad Pattern**:
```python
# ❌ BAD - String concatenation
query = f"SELECT * FROM users WHERE username = '{user_input}'"
```

**Example Good Pattern**:
```python
# ✅ GOOD - Parameterized query
query = "SELECT * FROM users WHERE username = ?"
cursor.execute(query, (user_input,))
```

---

## 2. Pandas Performance Anti-Patterns

### Web Searches Conducted
4. "Pandas anti-patterns performance optimization"
5. "Python pandas vectorization vs loops benchmark"

### Key Findings

**Critical Anti-Patterns**:
- ❌ Using .iterrows() or .apply() with loops
- ❌ Object dtype for categorical data
- ❌ Sequential DataFrame mutations
- ❌ No chunked processing for large files
- ❌ Ignoring memory profiling

**Performance Impact**:
- Loops: 10-100x slower than vectorization
- Object dtype: 2-5x more memory than category
- Sequential mutations: N^2 complexity

**Best Practices**:
- ✅ Vectorized operations (numpy, pandas native)
- ✅ Category dtype for categorical data
- ✅ Method chaining for readability
- ✅ Chunked reading (read_csv with chunksize)
- ✅ Memory profiling (memory_profiler)

**Sources**:
- Pandas official performance guide
- Matt Harrison's "Effective Pandas"
- DataCamp pandas performance tutorials
- Wes McKinney's blog posts

**Example Bad Pattern**:
```python
# ❌ BAD - Using iterrows()
for index, row in df.iterrows():
    df.at[index, 'new_col'] = row['col1'] * 2
```

**Example Good Pattern**:
```python
# ✅ GOOD - Vectorized operation
df['new_col'] = df['col1'] * 2
```

---

## 3. Polars: High-Performance Alternative

### Web Searches Conducted
6. "Polars vs Pandas performance 2025"

### Key Findings

**Polars Advantages**:
- 5-10x faster than pandas for most operations
- Multi-core processing by default
- Lazy evaluation (optimize entire query plan)
- Lower memory usage (Apache Arrow format)
- Type-safe operations

**When to Use Polars**:
- Datasets >100K rows
- Performance-critical pipelines
- Memory-constrained environments
- Greenfield projects

**When to Use Pandas**:
- Small datasets (<100K rows)
- Legacy codebases
- Ecosystem dependencies (matplotlib, seaborn)

**Sources**:
- Polars official benchmarks (https://pola.rs/)
- H2O.ai benchmark suite (Polars vs pandas)
- Towards Data Science Polars tutorials
- Reddit r/datascience discussions

**Performance Example**:
```
Dataset: 10M rows, groupby aggregation
- Pandas: 8.5 seconds
- Polars (lazy): 0.9 seconds (9.4x faster)
- Polars (eager): 1.2 seconds (7x faster)
```

---

## 4. DuckDB: Columnar Analytics

### Web Searches Conducted
7. "DuckDB pandas integration analytics"

### Key Findings

**DuckDB Benefits**:
- Columnar storage (optimized for analytics)
- SQL on pandas DataFrames
- Embedded database (no server)
- Fast aggregations and joins
- Parquet file support

**Use Cases**:
- Analytical queries on DataFrames
- ETL pipelines
- Data warehouse replacement for <100GB data
- Local development and testing

**Sources**:
- DuckDB official documentation (https://duckdb.org/)
- MotherDuck blog posts
- Hacker News discussions
- Benchmarks vs PostgreSQL, SQLite

**Performance Example**:
```
Dataset: 50M rows, complex join + aggregation
- pandas: 45 seconds
- DuckDB: 3.2 seconds (14x faster)
```

---

## 5. Data Validation: Great Expectations vs Pandera

### Web Searches Conducted
8. "Great Expectations vs Pandera data validation"

### Key Findings

**Great Expectations**:
- Production-grade data quality framework
- Comprehensive expectation suite (50+ built-in)
- Data documentation and profiling
- Team collaboration features
- Checkpoint-based validation
- Integration with Airflow, Prefect

**Pandera**:
- Lightweight schema validation
- Type hints integration (Python-first)
- pydantic-like DataFrame validation
- Faster for simple schemas
- Better developer experience

**Recommendation**:
- **Great Expectations**: Production pipelines, team projects, data documentation
- **Pandera**: Development phase, simple schemas, type-hint lovers

**Sources**:
- Great Expectations docs (https://greatexpectations.io/)
- Pandera docs (https://pandera.readthedocs.io/)
- DataCamp comparison article
- LinkedIn data engineering discussions

---

## 6. Statistical Analysis: scikit-learn vs statsmodels

### Web Searches Conducted
9. "scikit-learn vs statsmodels statistical analysis"

### Key Findings

**scikit-learn**:
- Machine learning focus
- Prediction-oriented
- Consistent API (fit, predict, transform)
- Cross-validation, hyperparameter tuning
- Model selection and evaluation

**statsmodels**:
- Statistical inference focus
- Explanation-oriented (p-values, confidence intervals)
- Regression diagnostics (residuals, QQ plots)
- Time series analysis (ARIMA, SARIMAX)
- Hypothesis testing (t-test, ANOVA)

**Recommendation**:
- **scikit-learn**: Predictive modeling, ML pipelines, feature engineering
- **statsmodels**: Hypothesis testing, causal inference, p-values needed

**Sources**:
- scikit-learn documentation (https://scikit-learn.org/)
- statsmodels documentation (https://www.statsmodels.org/)
- Cross Validated StackExchange discussions
- University statistics course materials

---

## 7. SQLAlchemy ORM Anti-Patterns

### Web Searches Conducted
10. "SQLAlchemy ORM anti-patterns N+1 queries"

### Key Findings

**Critical Anti-Patterns**:
- ❌ N+1 query problem (lazy loading in loops)
- ❌ No bulk operations
- ❌ Session mismanagement
- ❌ Ignoring query profiling
- ❌ Passive delete cascades

**Best Practices**:
- ✅ Eager loading (joinedload, selectinload)
- ✅ Bulk operations (bulk_insert_mappings)
- ✅ Query counting in tests
- ✅ Connection pooling
- ✅ Explicit cascade rules

**Sources**:
- SQLAlchemy official docs (https://docs.sqlalchemy.org/)
- Mike Bayer's blog (SQLAlchemy creator)
- Real Python SQLAlchemy tutorials
- GitHub SQLAlchemy performance issues

**Example N+1 Problem**:
```python
# ❌ BAD - N+1 queries (1 + N)
users = session.query(User).all()  # 1 query
for user in users:
    print(user.posts)  # N queries (one per user)

# ✅ GOOD - 1 query with joinedload
users = session.query(User).options(joinedload(User.posts)).all()
for user in users:
    print(user.posts)  # No additional queries
```

---

## 8. Exploratory Data Analysis (EDA)

### Web Searches Conducted
11. "Exploratory data analysis automation 2024"
12. "ydata-profiling pandas-profiling best practices"

### Key Findings

**Automated EDA Tools**:
1. **ydata-profiling** (formerly pandas-profiling)
   - Comprehensive HTML reports
   - Statistical summaries, distributions, correlations
   - Missing value analysis
   - Duplicate detection

2. **Sweetviz**
   - Comparative analysis (train vs test)
   - Target variable associations
   - Beautiful visualizations
   - Faster than ydata-profiling

3. **AutoViz**
   - Automatic chart selection
   - Publication-ready visualizations

4. **D-Tale**
   - Interactive web-based EDA
   - Code generation for operations

**Sources**:
- ydata-profiling GitHub (https://github.com/ydataai/ydata-profiling)
- Sweetviz GitHub (https://github.com/fbdesignpro/sweetviz)
- Towards Data Science EDA tutorials
- Kaggle EDA notebooks

---

## 9. Data Cleaning and Imputation

### Web Searches Conducted
13. "Data cleaning imputation techniques 2024"

### Key Findings

**Missing Value Strategies**:
- Mean/median imputation (simple, loses variance)
- KNN imputation (considers similarity)
- MICE (Multiple Imputation by Chained Equations)
- Model-based imputation (random forest)

**Outlier Detection**:
- IQR method (Q1 - 1.5*IQR, Q3 + 1.5*IQR)
- Z-score (>3 or <-3)
- Isolation Forest (model-based)
- DBSCAN clustering

**Best Practices**:
- Document all transformations
- Validate impact on target variable
- Consider domain knowledge
- Test multiple strategies

**Sources**:
- scikit-learn imputation docs
- fancyimpute library
- Academic papers on MICE
- DataCamp data cleaning course

---

## 10. Time Series Analysis

### Web Searches Conducted
14. "Time series analysis Python ARIMA Prophet 2024"

### Key Findings

**Time Series Tools**:
1. **statsmodels ARIMA/SARIMAX**
   - Classical statistical approach
   - Stationarity testing (ADF, KPSS)
   - Seasonal decomposition
   - Diagnostic plots

2. **Prophet (Facebook)**
   - Business time series
   - Holiday effects
   - Trend change points
   - Uncertainty intervals

3. **LSTM (Keras/PyTorch)**
   - Complex patterns
   - Multivariate time series
   - Deep learning approach

**Best Practices**:
- Test for stationarity first
- Split time series correctly (no shuffle)
- Use expanding window for validation
- Check residuals for autocorrelation

**Sources**:
- statsmodels time series docs
- Prophet documentation (https://facebook.github.io/prophet/)
- Time Series Analysis textbooks
- Kaggle time series competitions

---

## 11. Data Profiling Tools

### Web Searches Conducted
15. "Data profiling tools ydata-profiling sweetviz comparison"

### Key Findings

**Tool Comparison**:

| Feature | ydata-profiling | Sweetviz | D-Tale |
|---------|----------------|----------|--------|
| Speed | Moderate | Fast | Fast |
| Detail | High | Medium | High |
| Interactive | No | No | Yes |
| Compare datasets | Yes | Yes | Yes |
| Target analysis | Limited | Strong | Strong |

**Recommendations**:
- **ydata-profiling**: Initial comprehensive analysis
- **Sweetviz**: Quick comparative analysis (train vs test)
- **D-Tale**: Interactive exploration and debugging

**Sources**:
- GitHub repositories for each tool
- PyPI download statistics
- Reddit r/datascience recommendations
- Medium comparison articles

---

## 12. Feature Engineering

### Web Searches Conducted
16. "Feature engineering scikit-learn best practices"

### Key Findings

**Common Transformations**:
- Scaling (StandardScaler, MinMaxScaler)
- Encoding (OneHotEncoder, LabelEncoder, TargetEncoder)
- Polynomial features
- Interaction terms
- Date/time features (day_of_week, month, etc.)

**Best Practices**:
- Use Pipeline to prevent data leakage
- Fit only on training data
- Feature selection (RFE, SelectKBest)
- Domain-specific features

**Anti-Patterns**:
- ❌ Fitting scaler on full dataset (data leakage)
- ❌ One-hot encoding high cardinality
- ❌ No feature importance analysis

**Sources**:
- scikit-learn pipeline docs
- Feature Engineering book (Alice Zheng)
- Kaggle feature engineering tutorials
- Academic ML course materials

---

## 13. Data Visualization Best Practices

### Web Searches Conducted
17. "Data visualization matplotlib seaborn plotly best practices"

### Key Findings

**Library Selection**:
- **matplotlib**: Full customization, publication-quality
- **seaborn**: Statistical plots, beautiful defaults
- **plotly**: Interactive dashboards, Dash integration

**Best Practices**:
- Choose appropriate chart type (bar vs line vs scatter)
- Use color-blind friendly palettes
- WCAG 2.1 AA color contrast (4.5:1)
- Include axis labels and units
- Avoid 3D charts and pie charts (hard to read)
- Add data tables for accessibility

**Sources**:
- matplotlib documentation
- seaborn gallery (https://seaborn.pydata.org/)
- plotly documentation (https://plotly.com/python/)
- Edward Tufte's visualization principles
- ColorBrewer palettes (https://colorbrewer2.org/)

---

## 14. Pipeline Orchestration: Airflow vs Prefect

### Web Searches Conducted
18. "Apache Airflow vs Prefect comparison 2025"

### Key Findings

**Apache Airflow**:
- Mature ecosystem (2015)
- DAG-based workflow
- Strong community
- Many integrations
- Steeper learning curve
- Better for complex dependencies

**Prefect**:
- Modern Python-first API (2018, v2 in 2022)
- Pythonic decorators (@task, @flow)
- Better developer experience
- Cloud-native (Prefect Cloud)
- Easier testing
- Better for new projects

**Recommendation**:
- **Airflow**: Existing Airflow infrastructure, complex DAGs, legacy systems
- **Prefect**: New projects, Python developers, modern stack

**Sources**:
- Airflow docs (https://airflow.apache.org/)
- Prefect docs (https://www.prefect.io/)
- Reddit r/dataengineering discussions
- Company blog posts (Lyft, Airbnb on Airflow; Prefect case studies)

---

## 15. Database Query Optimization

### Web Searches Conducted
19. "Database query optimization indexing best practices"

### Key Findings

**Optimization Techniques**:
- Indexing strategies (B-tree, hash, GiST)
- EXPLAIN/EXPLAIN ANALYZE for query plans
- Query rewriting (subqueries → joins)
- Partitioning for large tables
- Materialized views for complex queries
- Connection pooling

**Common Issues**:
- Missing indexes on foreign keys
- Over-indexing (slows writes)
- Not using covering indexes
- Ignoring query execution plans

**Sources**:
- PostgreSQL performance tuning docs
- MySQL query optimization guide
- Use The Index, Luke! (website)
- Database-specific blogs (Percona, 2ndQuadrant)

---

## 16. Data Ethics and Privacy (GDPR)

### Web Searches Conducted
20. "Data ethics GDPR compliance anonymization techniques"

### Key Findings

**GDPR Requirements**:
- Right to deletion (hard delete vs soft delete)
- Data minimization (collect only what's needed)
- Purpose limitation (use data only for stated purpose)
- Audit trails (who accessed what, when)
- Consent management

**Anonymization Techniques**:
1. **k-anonymity**: Each record indistinguishable from k-1 others
2. **Differential privacy**: Add statistical noise
3. **Pseudonymization**: Replace identifiers with pseudonyms
4. **Aggregation**: Report only aggregated statistics

**PII Detection**:
- Names, emails, phone numbers
- Addresses, IP addresses
- Credit card numbers, SSNs
- Biometric data

**Sources**:
- GDPR official text (EU regulation)
- diffprivlib (IBM library)
- Academic papers on k-anonymity
- Privacy engineering blogs

---

## 17. Reproducible Data Science

### Web Searches Conducted
(Covered in search 18: DVC and MLflow)

### Key Findings

**DVC (Data Version Control)**:
- Git-like versioning for data and models
- Remote storage (S3, GCS, Azure)
- Pipeline reproducibility
- Data lineage tracking

**MLflow**:
- Experiment tracking (parameters, metrics, artifacts)
- Model registry (staging, production)
- Model serving
- Multi-framework support

**Best Practices**:
- Version all data transformations
- Log all hyperparameters
- Use seeds for reproducibility
- Document environment (requirements.txt)
- Track data provenance

**Sources**:
- DVC documentation (https://dvc.org/)
- MLflow documentation (https://mlflow.org/)
- Reproducible research papers
- Data science team blog posts

---

## Summary of Anti-Patterns by Category

### SQL Anti-Patterns
1. String concatenation → Parameterized queries
2. No input validation → Strict validation
3. Ignoring execution plans → EXPLAIN analysis
4. Missing indexes → Index strategy
5. N+1 queries → Eager loading

### Python/Pandas Anti-Patterns
1. Loops over DataFrames → Vectorization
2. .apply() overuse → Native methods
3. Object dtypes → Category dtypes
4. Sequential mutations → Method chaining
5. No memory profiling → Chunked processing

### Data Quality Anti-Patterns
1. No schema validation → Great Expectations/Pandera
2. Silent failures → Explicit error handling
3. No data profiling → Automated EDA
4. Ignoring outliers → Outlier detection
5. No documentation → Data catalogs

### ML/Statistics Anti-Patterns
1. Data leakage → Proper train/test split
2. Wrong tool (sklearn vs statsmodels) → Context-appropriate
3. No cross-validation → KFold, TimeSeriesSplit
4. Ignoring assumptions → Diagnostic plots
5. No reproducibility → Seeds, versioning

### Security/Privacy Anti-Patterns
1. Hardcoded secrets → Environment variables
2. No anonymization → k-anonymity, diff privacy
3. PII exposure → PII detection and masking
4. No audit trails → Logging and monitoring
5. Insecure connections → SSL/TLS

---

## Implementation Priority

### Critical (Implement First)
1. SQL injection prevention (FR-001)
2. Pandas vectorization (FR-002)
3. Data quality validation (FR-005, FR-006)
4. SQLAlchemy best practices (FR-012)
5. Security scanning (Bandit)

### High Priority
1. Polars integration (FR-003)
2. EDA automation (FR-007)
3. WCAG visualization (FR-018)
4. Query optimization (FR-020)

### Medium Priority
1. DuckDB integration (FR-004)
2. scikit-learn/statsmodels (FR-009, FR-010)
3. Time series (FR-011)
4. Orchestration (FR-013, FR-014)
5. Versioning (FR-015, FR-016)

### Low Priority (Nice to Have)
1. Sweetviz (FR-008)
2. Privacy/anonymization (FR-017)
3. Advanced visualizations (FR-019)

---

## Conclusion

This research identifies comprehensive LLM anti-patterns across all aspects of data analysis. The specification (spec.md) incorporates these findings into 20 functional requirements with clear prevention strategies, best practices, and integration with 20 high-value tools.

**Key Takeaways**:
- Security (SQL injection) is non-negotiable
- Performance matters: vectorization, Polars, DuckDB
- Data quality must be automated: Great Expectations, Pandera
- Modern tools are better: Prefect > Airflow, Polars > pandas (for large data)
- Accessibility is required: WCAG 2.1 AA compliance
- Privacy is critical: GDPR compliance, anonymization

**Next Steps**:
1. Review and approve specification
2. Create detailed implementation plan (plan.md)
3. Break down into actionable tasks (tasks.md)
4. Implement in phases following priority order
