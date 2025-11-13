# Feature Specification: MCP Integration

**Feature Branch**: `005-mcp-integration`
**Created**: 2025-11-10
**Status**: Approved
**Approved Date**: 2025-11-13
**Priority**: P3 (Optional Enhancement)
**Input**: Configure Model Context Protocol (MCP) servers for enhanced data access (PostgreSQL, filesystem, API, search) to complement Agent Skills

## Overview

This specification defines the integration of Model Context Protocol (MCP) servers into the Claude Code dashboard development environment. MCP servers provide standardized access to external data sources and tools, complementing Agent Skills which provide methodology and domain expertise.

**MCP vs Skills**: MCP provides the WHAT (data access), Skills provide the HOW (methodology).

**Target MCP Servers**:

1. **mcp__postgres** - PostgreSQL database access for dashboard data
2. **mcp__filesystem** - File system operations for CSV, JSON, Parquet files
3. **mcp__fetch** - HTTP/REST API access for external data
4. **mcp__search** - Search reference documentation and examples

**Integration**: MCP servers are referenced by Skills (especially data-analysis) and used via tool calls during dashboard development.

**Configuration**: Centralized in `.claude/mcp_config.json` with per-server enable/disable control.

**Priority**: P3 (Optional) - Dashboard development works without MCP using direct file/database access, but MCP provides standardized, optimized patterns.

---

## User Scenarios & Testing *(mandatory)*

### User Story 1 - PostgreSQL Database Access (Priority: P3)

As a **dashboard developer**, I want to access PostgreSQL databases through MCP so that I can load dashboard data using standardized, secure connection patterns.

**Why this priority**: Optional because dashboards can use psycopg2 directly. MCP provides cleaner abstraction and connection management.

**Independent Test**: Can be tested by querying a database and verifying results match direct SQL access.

**Acceptance Scenarios**:

1. **Given** I need dashboard data from PostgreSQL, **When** I configure `mcp__postgres` with connection string, **Then** the server connects and is available for queries

2. **Given** MCP postgres is configured, **When** the `data-analysis` Skill activates, **Then** it references `mcp__postgres` in allowed-tools and provides usage patterns

3. **Given** I query via MCP, **When** executing SQL, **Then** results are returned as pandas DataFrame with proper type inference

4. **Given** I have connection issues, **When** MCP postgres fails, **Then** clear error messages guide troubleshooting (connection string, credentials, network)

---

### User Story 2 - Filesystem Access (Priority: P3)

As a **dashboard developer**, I want to access files through MCP so that I can load CSV, JSON, and Parquet data with consistent patterns.

**Why this priority**: Optional because Read tool works directly. MCP provides enhanced patterns for large files and directory operations.

**Independent Test**: Can be tested by loading files and comparing with direct file reads.

**Acceptance Scenarios**:

1. **Given** I have data files in `./data/`, **When** I configure `mcp__filesystem` with path: `./data`, **Then** server provides access to all files in that directory

2. **Given** MCP filesystem is configured, **When** loading CSV, **Then** it handles large files efficiently with streaming/chunking

3. **Given** I need to list files, **When** using MCP, **Then** it provides directory listing with file metadata (size, modified date)

---

### User Story 3 - API Access (Priority: P3)

As a **dashboard developer**, I want to fetch data from REST APIs through MCP so that I can integrate external data sources.

**Why this priority**: Optional. Useful for dashboards pulling live data from APIs, but not all dashboards need this.

**Independent Test**: Can be tested by calling an API and verifying response.

**Acceptance Scenarios**:

1. **Given** I need external API data, **When** I configure `mcp__fetch`, **Then** it's available for HTTP requests

2. **Given** MCP fetch is configured, **When** calling APIs, **Then** it handles authentication, retries, and error cases

---

### User Story 4 - Documentation Search (Priority: P3)

As a **dashboard developer**, I want to search reference documentation through MCP so that I can quickly find examples and patterns.

**Why this priority**: Optional. Nice-to-have for discovering patterns, but Skills already provide examples.

**Independent Test**: Can be tested by searching for keywords and verifying relevant results.

**Acceptance Scenarios**:

1. **Given** I have reference docs in `./reference/`, **When** I configure `mcp__search` with path, **Then** it indexes documentation for searching

2. **Given** I search for patterns, **When** querying, **Then** it returns relevant documentation with context

---

### Edge Cases

- **What happens when** MCP server fails to start?
  - System should gracefully degrade; dashboard development continues using direct access methods

- **What happens when** MCP server credentials are invalid?
  - Clear error message with credential configuration guidance; don't expose sensitive info in errors

- **What happens when** Skills reference MCP servers that aren't configured?
  - Skill should provide fallback guidance for direct access (e.g., psycopg2 instead of mcp__postgres)

- **What happens when** multiple MCP servers access the same resource?
  - Servers should coordinate or use separate resources; document conflicts

---

## Requirements *(mandatory)*

### Functional Requirements

#### MCP Configuration (FR-001 to FR-010)

- **FR-001**: System MUST provide `.claude/mcp_config.json` for centralized MCP server configuration
- **FR-002**: Configuration MUST support enabling/disabling servers individually via `"enabled": true/false`
- **FR-003**: Configuration MUST support connection strings via environment variables (e.g., `${POSTGRES_URL}`)
- **FR-004**: Configuration MUST validate on startup and report misconfigurations clearly
- **FR-005**: Configuration MUST support security settings: allowed paths, denied paths
- **FR-006**: Configuration MUST support caching with TTL (time-to-live) settings
- **FR-007**: Configuration changes MUST NOT require code changes (JSON file only)
- **FR-008**: System MUST log MCP server status (enabled/disabled, connection success/failure)
- **FR-009**: System MUST provide example configuration with all servers documented
- **FR-010**: Configuration MUST be version-controlled but credentials MUST use environment variables (not hardcoded)

---

#### PostgreSQL MCP Server (FR-011 to FR-020)

- **FR-011**: System MUST support `mcp__postgres` server for PostgreSQL database access
- **FR-012**: Server MUST connect using `${POSTGRES_URL}` environment variable
- **FR-013**: Server MUST support standard SQL queries with result type inference
- **FR-014**: Server MUST return results as pandas-compatible data structures
- **FR-015**: Server MUST handle connection pooling and timeout configuration
- **FR-016**: Server MUST provide clear error messages for connection failures
- **FR-017**: Server MUST support parameterized queries to prevent SQL injection
- **FR-018**: Server MUST be referenced in `data-analysis` Skill allowed-tools
- **FR-019**: Server MUST be disabled by default (opt-in via configuration)
- **FR-020**: Server MUST integrate with Skills via standard tool call patterns

---

#### Filesystem MCP Server (FR-021 to FR-028)

- **FR-021**: System MUST support `mcp__filesystem` server for file operations
- **FR-022**: Server MUST restrict access to configured path (default: `./data`)
- **FR-023**: Server MUST support reading CSV, JSON, Parquet, text files
- **FR-024**: Server MUST provide directory listing capabilities
- **FR-025**: Server MUST handle large files efficiently (streaming/chunking)
- **FR-026**: Server MUST enforce security boundaries (no access outside allowed paths)
- **FR-027**: Server MUST be referenced in `data-analysis` Skill allowed-tools
- **FR-028**: Server MUST support file metadata (size, modified date, permissions)

---

#### Fetch MCP Server (FR-029 to FR-034)

- **FR-029**: System MUST support `mcp__fetch` server for HTTP/REST API access
- **FR-030**: Server MUST support GET, POST, PUT, DELETE methods
- **FR-031**: Server MUST handle authentication (Bearer tokens, API keys)
- **FR-032**: Server MUST implement retry logic with exponential backoff
- **FR-033**: Server MUST respect rate limits and timeout configurations
- **FR-034**: Server MUST provide clear error messages for API failures

---

#### Search MCP Server (FR-035 to FR-040)

- **FR-035**: System MUST support `mcp__search` server for documentation search
- **FR-036**: Server MUST index documentation in configured path (default: `./reference`)
- **FR-037**: Server MUST support keyword search with relevance ranking
- **FR-038**: Server MUST return results with context (surrounding text)
- **FR-039**: Server MUST handle Markdown, text, and code files
- **FR-040**: Server MUST update index when files change

---

#### Skills Integration (FR-041 to FR-045)

- **FR-041**: `data-analysis` Skill MUST reference appropriate MCP servers in allowed-tools
- **FR-042**: Skills MUST provide fallback patterns when MCP servers unavailable
- **FR-043**: Skills MUST document MCP usage in Level 2 or Level 3 content
- **FR-044**: MCP tools MUST be callable via standard tool call syntax
- **FR-045**: MCP and Skills MUST complement each other (Skills provide methodology, MCP provides access)

---

### Key Entities

- **MCP Server**: External data/tool access provider
  - Attributes: name (mcp__*), type (postgres/filesystem/fetch/search), enabled status, configuration
  - Relationships: Referenced by Skills, called via tools, configured in mcp_config.json

- **MCP Configuration**: Central configuration file
  - Attributes: file path (.claude/mcp_config.json), server definitions, security settings, caching config
  - Relationships: Defines all MCP servers, read at startup, version-controlled

- **Connection String**: Database/service connection information
  - Attributes: environment variable name, format, security (masked in logs)
  - Relationships: Used by postgres and other servers, stored in environment

---

## Success Criteria *(mandatory)*

### Measurable Outcomes

- **SC-001**: MCP servers start successfully 100% of the time with valid configuration
- **SC-002**: Configuration errors provide actionable guidance 100% of the time
- **SC-003**: PostgreSQL queries via MCP match direct psycopg2 results 100% of the time
- **SC-004**: Filesystem operations via MCP are 20%+ faster than direct reads for large files
- **SC-005**: API calls via MCP handle retries and errors gracefully 95%+ of the time
- **SC-006**: Documentation search via MCP finds relevant results 85%+ of the time
- **SC-007**: Skills integrate with MCP seamlessly (no conflicts, clear usage patterns)
- **SC-008**: MCP unavailability degrades gracefully (fallback to direct access works)
- **SC-009**: No credentials hardcoded in mcp_config.json (100% use environment variables)
- **SC-010**: Developers can configure new MCP server in <15 minutes

---

## Non-Functional Requirements

### Performance
- MCP server startup: <5 seconds
- Database queries: comparable to direct SQL (<10% overhead)
- File operations: 20%+ faster for large files via streaming
- API calls: <100ms overhead vs direct HTTP

### Security
- No hardcoded credentials
- Path restrictions enforced (filesystem)
- SQL injection prevention (parameterized queries)
- API credentials encrypted in transit

### Reliability
- Graceful degradation when MCP unavailable
- Clear error messages with remediation guidance
- Connection retry logic with backoff
- Timeout configuration for all operations

### Maintainability
- Configuration via JSON (no code changes)
- Environment variables for credentials
- Version-controlled configuration
- Documentation for each server

---

## Technology Stack

### Required
- **Claude Code**: Environment with MCP support
- **MCP Servers**: mcp-server-postgres, mcp-server-filesystem, mcp-server-fetch, mcp-server-search (NPM packages)
- **Environment Variables**: For credentials (POSTGRES_URL, API_KEYS, etc.)

### Optional
- **PostgreSQL**: If using postgres server
- **Documentation**: Markdown files for search server

---

## Out of Scope

- Custom MCP server development (use existing servers only)
- Database migration tools (use separate tools)
- Real-time data streaming (MCP provides request/response)
- MCP server troubleshooting beyond configuration

---

## Clarifications

### Q1: Why is MCP optional (P3) if it provides data access?

**A**: Dashboards can access data directly without MCP. MCP provides standardization and optimization but isn't required.

**Without MCP**:
- Use psycopg2 for PostgreSQL (direct connection)
- Use pandas.read_csv() for files (direct read)
- Use requests for APIs (direct HTTP)

**With MCP**:
- Standardized patterns
- Connection management
- Caching and optimization
- Security boundaries

MCP is enhancement, not requirement.

---

### Q2: How do Skills and MCP work together?

**A**: Skills provide methodology (HOW), MCP provides access (WHAT).

**Example: Loading database data**:
```
User: Load sales data from PostgreSQL

MCP: mcp__postgres connects, executes query, returns data

Skill: data-analysis guides:
  - How to write query
  - What EDA to perform
  - How to check data quality
  - What visualizations to create

Result: MCP fetches data, Skill guides analysis
```

Complementary, not competing.

---

### Q3: What if MCP server configuration changes?

**A**: Edit `.claude/mcp_config.json`, restart Claude Code. No code changes needed.

**Example**:
```json
{
  "mcpServers": {
    "postgres": {
      "enabled": true,  // Enable server
      "command": "mcp-server-postgres",
      "env": {
        "POSTGRES_URL": "${POSTGRES_URL}"  // From environment
      }
    }
  }
}
```

Change `"enabled": false` to disable. Update `POSTGRES_URL` environment variable for different database.

---

## Dependencies

### Prerequisites
- Spec 002 (Claude Code Commands Setup) approved
- Claude Code with MCP support
- NPM for installing MCP servers
- Environment variables configured

### Internal Dependencies
- Spec 004 (Agent Skills - Production) for Skills integration
- data-analysis Skill references MCP in allowed-tools

### External Dependencies
- mcp-server-postgres NPM package
- mcp-server-filesystem NPM package
- mcp-server-fetch NPM package
- mcp-server-search NPM package
- PostgreSQL database (if using postgres server)

---

## Implementation Phases

### Phase 1: Configuration Framework
- Create .claude/mcp_config.json structure
- Implement server enable/disable logic
- Add environment variable support
- Test validation and error handling

### Phase 2: Core Servers
- Configure postgres server
- Configure filesystem server
- Test connections and operations
- Document usage patterns

### Phase 3: Extended Servers
- Configure fetch server
- Configure search server
- Test API calls and search
- Integration testing

### Phase 4: Skills Integration
- Update data-analysis Skill with MCP references
- Test MCP + Skills workflows
- Document fallback patterns
- Validate against success criteria

---

## Review & Acceptance Checklist

### Completeness
- [ ] All 4 MCP servers documented
- [ ] All 45 functional requirements defined
- [ ] All 10 success criteria measurable
- [ ] Configuration structure specified
- [ ] Security requirements addressed

### Clarity
- [ ] MCP vs Skills distinction clear
- [ ] Configuration format documented
- [ ] Environment variable usage explained
- [ ] Fallback patterns defined

### Feasibility
- [ ] MCP servers available as NPM packages
- [ ] Configuration approach validated
- [ ] Optional status appropriate (P3)
- [ ] Integration with Skills clear

---

**Next Steps**:
1. **Review this specification** - Validate scope and priority
2. **Approve specification** - Mark as "approved" when ready
3. **Create plan.md** - Define configuration details
4. **Create tasks.md** - Implementation tasks
5. **Implement** - Optional, after specs 002-004 complete

---

**Status**: Draft
**Priority**: P3 (Optional)
**Dependencies**: Spec 002 (approved), Spec 004 (for Skills integration)
**Blocks**: None (optional enhancement)
**Version**: 1.0.0
**Last Updated**: 2025-11-10
