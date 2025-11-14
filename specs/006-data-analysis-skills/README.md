# Spec 006: Data Analysis Skills with LLM Anti-Pattern Prevention

**Status**: Draft
**Created**: 2025-11-14
**Branch**: `006-data-analysis-skills`

## Quick Summary

Advanced data analysis skills for Claude Code that prevent common LLM anti-patterns in SQL and Python code generation while integrating with 20 high-value data analysis tools.

## Key Features

- **SQL Security**: Prevent SQL injection with parameterized queries
- **Performance**: Polars (5-10x faster), DuckDB (columnar analytics)
- **Data Quality**: Great Expectations, Pandera validation
- **EDA**: ydata-profiling, Sweetviz automated analysis
- **ML/Statistics**: scikit-learn, statsmodels best practices
- **Orchestration**: Airflow, Prefect pipeline management
- **Privacy**: GDPR compliance, anonymization techniques
- **Accessibility**: WCAG 2.1 AA compliant visualizations

## 20 High-Value Tools Integrated

1. Polars - 5-10x faster DataFrames
2. DuckDB - Columnar analytics
3. Great Expectations - Data quality
4. Pandera - Lightweight validation
5. ydata-profiling - Automated EDA
6. Sweetviz - Comparative analysis
7. scikit-learn - Machine learning
8. statsmodels - Statistical inference
9. Prophet - Time series forecasting
10. SQLAlchemy - ORM best practices
11. Apache Airflow - DAG orchestration
12. Prefect - Modern orchestration
13. DVC - Data versioning
14. MLflow - Experiment tracking
15. diffprivlib - Differential privacy
16. Plotly - Interactive dashboards
17. Seaborn - Statistical viz
18. Bandit - Security scanning
19. PostgreSQL - Query optimization
20. ColorBrewer - Accessible palettes

## Requirements Summary

- **20 Functional Requirements** (FR-001 to FR-020)
- **8 Success Criteria** (SC-001 to SC-008)
- **95% Test Coverage** (line and branch)
- **WCAG 2.1 AA** compliance for visualizations
- **Zero SQL Injection** vulnerabilities

## Files

- `spec.md` - Complete feature specification
- `plan.md` - Implementation plan (to be created)
- `tasks.md` - Actionable task list (to be created)

## Next Steps

1. Review and approve specification
2. Create implementation plan (plan.md)
3. Break down into tasks (tasks.md)
4. Begin implementation with `/workflow:observe`

## Research Sources

Based on comprehensive research of 20 web searches covering:
- SQL injection prevention and Text2SQL
- Pandas performance and Polars benchmarks
- Data validation frameworks
- EDA and profiling tools
- ML/statistical analysis best practices
- Pipeline orchestration (Airflow vs Prefect)
- Data versioning (DVC, MLflow)
- Privacy and GDPR compliance
- Accessible visualization techniques
- Database query optimization

## Constitutional Alignment

✅ 95% test coverage (line and branch)
✅ WCAG 2.1 AA accessibility
✅ <3s load time for operations
✅ Security-first (SQL injection prevention)
✅ Performance-first (Polars, DuckDB)
✅ Type hints and docstrings
✅ Comprehensive error handling
