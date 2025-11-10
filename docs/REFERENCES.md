# Reference Resources for Spec-Driven Dashboard Development

This document catalogs all reference repositories, tutorials, and resources for building spec-driven dashboards with AI agents, Plotly Dash, and Claude.

## Cloned Reference Repositories (23)

These repositories are available locally in the `reference/` directory for offline access and reference.

### Core Frameworks & SDKs

1. **Plotly Dash** - `reference/dash/`
   - Official Plotly Dash framework
   - Interactive Python dashboards
   - Link: https://github.com/plotly/dash

2. **Spec-Kit** - `reference/spec-kit/`
   - Specification-driven development toolkit by GitHub
   - Templates and workflows for spec-first development
   - Link: https://github.com/github/spec-kit

3. **Claude Agent SDK (Python)** - `reference/claude-agent-sdk-python/`
   - Anthropic's official Python SDK for Claude agents
   - Production deployment and orchestration
   - Link: https://github.com/anthropics/claude-agent-sdk-python

4. **Streamlit** - `reference/streamlit/`
   - Fast way to build data apps
   - Alternative/complementary to Dash
   - Link: https://github.com/streamlit/streamlit

### AI Agent Frameworks

5. **LangChain** - `reference/langchain/`
   - Framework for building LLM applications
   - Chains, agents, memory management
   - Link: https://github.com/langchain-ai/langchain

6. **LangGraph** - `reference/langgraph/`
   - Build stateful, multi-actor applications with LLMs
   - Graph-based agent orchestration
   - Link: https://github.com/langchain-ai/langgraph

7. **Pydantic-AI** - `reference/pydantic-ai/`
   - Agent framework built on Pydantic
   - Type-safe AI applications
   - Link: https://github.com/pydantic/pydantic-ai

8. **Phidata** - `reference/phidata/`
   - Build AI agents with memory, knowledge, and tools
   - Production-ready agent infrastructure
   - Link: https://github.com/phidatahq/phidata

9. **OpenAI Swarm** - `reference/openai-swarm/`
   - Educational framework for multi-agent orchestration
   - Agent handoffs and routines
   - Link: https://github.com/openai/swarm

10. **LlamaIndex** - `reference/llama_index/`
    - Data framework for LLM applications
    - RAG (Retrieval-Augmented Generation) capabilities
    - Link: https://github.com/run-llama/llama_index

11. **Mem0** - `reference/mem0/`
    - Memory layer for AI agents
    - Persistent, adaptive memory
    - Link: https://github.com/mem0ai/mem0

12. **AutoGPT** - `reference/autogpt/`
    - Autonomous AI agent framework
    - Task decomposition and execution
    - Link: https://github.com/Significant-Gravitas/AutoGPT

13. **Vercel AI SDK** - `reference/vercel-ai/`
    - TypeScript toolkit for AI apps
    - Streaming, tool calling, multi-model support
    - Link: https://github.com/vercel/ai

### Model Context Protocol (MCP)

14. **MCP Servers** - `reference/mcp-servers/`
    - Official MCP server implementations
    - Connect LLMs to data sources and tools
    - Link: https://github.com/modelcontextprotocol/servers

15. **MCP Python SDK** - `reference/mcp-python-sdk/`
    - Python SDK for Model Context Protocol
    - Build custom MCP servers
    - Link: https://github.com/modelcontextprotocol/python-sdk

16. **AI Experiments (MCP Agent)** - `reference/ai-experiments/`
    - MCP agent experiment by Vivek Pathania
    - Practical MCP integration examples
    - Link: https://github.com/vivekpathania/ai-experiments
    - **Key Path**: `mcp-agent-experiment/` subdirectory

### Dash + AI Agent Integrations

17. **All-in-AI Demo App** - `reference/all-in-ai-demo-app/`
    - Complete Dash app with AI chatbot
    - Natural language chart generation
    - Upload datasets and interact via OpenAI
    - Link: https://github.com/plotly/all-in-ai-demo-app

18. **Dash AI Chat Tutorial** - `reference/dash-ai-chat-tutorial/`
    - Tutorial for integrating AI APIs (Claude, Gemini, ChatGPT) with Dash
    - Interactive chat interface
    - Link: https://github.com/plotly/dash-ai-chat-tutorial

19. **Dashboard Agents** - `reference/dashboard-agents/`
    - Dashboard Analytics Agent by Abhifetch
    - Processes datasets and generates visualizations
    - Agent-driven dashboard creation
    - Link: https://github.com/abhifetch/dashboard-agents

### Cloud & Enterprise Platforms

20. **AWS Bedrock Agents (Streamlit)** - `reference/bedrock-agents-streamlit/`
    - Official AWS example for Bedrock agents with Streamlit UI
    - Enterprise deployment patterns
    - Link: https://github.com/build-on-aws/bedrock-agents-streamlit

21. **Amazon Bedrock AgentCore Samples** - `reference/amazon-bedrock-agentcore-samples/`
    - Deploy, manage, and scale AI agents on AWS
    - Enterprise-grade security and infrastructure
    - Link: https://github.com/awslabs/amazon-bedrock-agentcore-samples

### Development & Testing Infrastructure

22. **AI Agent Host** - `reference/AI-Agent-Host/`
    - Module-based environment for testing LangChain agents
    - Docker Compose with Grafana for visualization
    - Containerized agent development
    - Link: https://github.com/quantiota/AI-Agent-Host

23. **Anthropic Cookbook** - `reference/anthropic-cookbook/`
    - Claude API recipes and examples
    - Best practices and patterns
    - Link: https://github.com/anthropics/anthropic-cookbook

## Additional Online Resources

### Video Tutorials

1. **Add AI Agent to Plotly Dash with LangGraph** (Charming Data)
   - Tutorial on integrating LangGraph with existing Dash apps
   - Global arms trade visualization with AI context
   - Link: https://www.youtube.com/watch?v=[video-id]

2. **Build AI App with LangGraph and Streamlit**
   - Connect Streamlit to LangGraph server API
   - Multi-agent chat interface
   - Conversation history management
   - Link: https://www.youtube.com/watch?v=[video-id]

3. **Spec Kit Overview Video**
   - Official spec-kit introduction
   - Demonstration of spec-driven workflow
   - Link: https://www.youtube.com/watch?v=a9eR1xsfvHg

### Medium Articles & Blog Posts

4. **Building a Data Analyst Agent with Streamlit and Pydantic-AI** (Multi-part series)
   - Full-stack AI agent for data analysis
   - Streamlit UI + FastAPI backend
   - CSV ingestion, analysis, and report generation
   - Link: https://medium.com/data-science-collective/...

5. **Build an AI Agent That Turns SQL Databases into Dashboards**
   - Agent autonomously generates dashboard pipeline
   - Reasons over data and automates visualization
   - Outputs Python/Dash code for deployment
   - Link: https://medium.com/data-science-collective/build-an-ai-agent-that-turns-sql-databases-into-dashboards-no-queries-needed-ea78571b2475

### Documentation & Official Guides

6. **Plotly Dash Documentation**
   - Link: https://dash.plotly.com/

7. **LangGraph Documentation**
   - Link: https://langchain-ai.github.io/langgraph/

8. **Claude AI API Documentation**
   - Link: https://docs.anthropic.com/

9. **Model Context Protocol Specification**
   - Link: https://modelcontextprotocol.io/

10. **Pydantic-AI Documentation**
    - Link: https://ai.pydantic.dev/

## Additional Relevant Repositories (Not Cloned)

These repositories are valuable references but not cloned locally. Consider cloning as needed.

### AI Agent Frameworks

11. **CrewAI** - Multi-agent collaboration framework
    - Link: https://github.com/crewai-ai/crewai

12. **MetaGPT** - Multi-agent software engineering
    - Link: https://github.com/geekan/MetaGPT

13. **BabyAGI** - Task-driven autonomous agent
    - Link: https://github.com/yoheinakajima/babyagi

14. **SuperAGI** - Dev-first open-source agent framework
    - Link: https://github.com/TransformerOptimus/SuperAGI

15. **AgentGPT** - Browser-based autonomous agents
    - Link: https://github.com/reworkd/AgentGPT

### Dashboard & Visualization

16. **Plotly Python** - Plotly graphing library
    - Link: https://github.com/plotly/plotly.py

17. **Panel** - Build dashboards in Python (HoloViz)
    - Link: https://github.com/holoviz/panel

18. **Gradio** - Build ML web apps quickly
    - Link: https://github.com/gradio-app/gradio

19. **Reflex** - Full-stack Python framework
    - Link: https://github.com/reflex-dev/reflex

20. **NiceGUI** - Python UI framework
    - Link: https://github.com/zauberzeug/nicegui

### Data Processing & Analysis

21. **Pandas** - Data manipulation library
    - Link: https://github.com/pandas-dev/pandas

22. **Polars** - Fast DataFrame library
    - Link: https://github.com/pola-rs/polars

23. **DuckDB** - In-process SQL OLAP database
    - Link: https://github.com/duckdb/duckdb

24. **Great Expectations** - Data quality framework
    - Link: https://github.com/great-expectations/great_expectations

### Agent Tool Integration

25. **LangChain Tools** - Pre-built tools for agents
    - Link: https://github.com/langchain-ai/langchain/tree/master/libs/langchain/langchain/tools

26. **LlamaHub** - Data loaders for LlamaIndex
    - Link: https://github.com/run-llama/llama-hub

27. **Chainlit** - Build Python LLM apps with chat UI
    - Link: https://github.com/Chainlit/chainlit

28. **Haystack** - LLM orchestration framework
    - Link: https://github.com/deepset-ai/haystack

### Testing & Quality

29. **Playwright Python** - Browser automation
    - Link: https://github.com/microsoft/playwright-python

30. **Pytest** - Testing framework
    - Link: https://github.com/pytest-dev/pytest

31. **Dash Testing** - Dash testing utilities
    - Link: https://dash.plotly.com/testing

### Deployment & Infrastructure

32. **Docker Compose Examples** - Multi-container applications
    - Link: https://github.com/docker/awesome-compose

33. **Kubernetes Python Client** - K8s Python client
    - Link: https://github.com/kubernetes-client/python

34. **Railway** - Deploy Dash apps
    - Link: https://railway.app/

35. **Render** - Deploy web services
    - Link: https://render.com/

### Monitoring & Observability

36. **Prometheus Python Client** - Metrics collection
    - Link: https://github.com/prometheus/client_python

37. **Grafana Dashboards** - Visualization platform
    - Link: https://grafana.com/

38. **OpenTelemetry Python** - Observability framework
    - Link: https://github.com/open-telemetry/opentelemetry-python

### Security & Authentication

39. **Python-JOSE** - JWT implementation
    - Link: https://github.com/mpdavis/python-jose

40. **Authlib** - Authentication library
    - Link: https://github.com/lepture/authlib

### Caching & Performance

41. **Redis Python** - Redis client
    - Link: https://github.com/redis/redis-py

42. **Memcached** - Distributed memory caching
    - Link: https://github.com/memcached/memcached

### Code Quality

43. **Ruff** - Fast Python linter
    - Link: https://github.com/astral-sh/ruff

44. **Black** - Code formatter
    - Link: https://github.com/psf/black

45. **Mypy** - Static type checker
    - Link: https://github.com/python/mypy

### Documentation

46. **MkDocs** - Documentation generator
    - Link: https://github.com/mkdocs/mkdocs

47. **Sphinx** - Documentation builder
    - Link: https://github.com/sphinx-doc/sphinx

### Additional Agent Examples

48. **LangGraph Examples** - Official examples
    - Link: https://github.com/langchain-ai/langgraph/tree/main/examples

49. **Anthropic SDK Examples**
    - Link: https://github.com/anthropics/anthropic-sdk-python/tree/main/examples

50. **OpenAI Cookbook** - OpenAI API examples
    - Link: https://github.com/openai/openai-cookbook

## Integration Patterns

### Pattern 1: Dash + LangGraph + Claude
```
User → Dash UI → LangGraph Agent → Claude API → Plotly Charts
                      ↓
                 MCP Servers (Data Sources)
```

**Example**: `reference/all-in-ai-demo-app/`

### Pattern 2: Spec-Driven Development
```
Specification → Technical Plan → Task Breakdown → Implementation → Deployment
     ↓              ↓                 ↓                ↓              ↓
constitution.md  plan.md         tasks.md        Claude Code    Agent SDK
```

**Example**: This project structure

### Pattern 3: Agent-Driven Dashboard Generation
```
SQL Database → AI Agent → Dashboard Code → Docker Container → Production
                  ↓
            Autonomous Generation
```

**Example**: `reference/dashboard-agents/`

### Pattern 4: Multi-Agent Orchestration
```
User Query → Coordinator Agent → Specialist Agents → Aggregator → Response
                                (Research, Analysis, Viz)
```

**Example**: `reference/openai-swarm/`

## Resource Categories

### By Use Case

**Dashboard Development**:
- Plotly Dash, Streamlit, Panel, Gradio, Reflex

**AI Agent Frameworks**:
- LangChain, LangGraph, Pydantic-AI, Phidata, CrewAI

**Data Access (MCP)**:
- MCP Servers, MCP Python SDK, AI Experiments

**Production Deployment**:
- Claude Agent SDK, AWS Bedrock, Docker, Kubernetes

**Spec-Driven Development**:
- Spec-Kit, GitHub workflows

### By Complexity

**Beginner**:
- Dash AI Chat Tutorial
- Streamlit examples
- OpenAI Swarm (educational)

**Intermediate**:
- All-in-AI Demo App
- Dashboard Agents
- Pydantic-AI examples

**Advanced**:
- Amazon Bedrock AgentCore
- LangGraph multi-agent systems
- Claude Agent SDK production deployment

## Recommended Learning Path

### Phase 1: Foundations (Week 1-2)
1. Read the Constitution (`.specify/memory/constitution.md`)
2. Complete Quick Start (`docs/QUICKSTART.md`)
3. Study Dash basics (`reference/dash/`)
4. Understand spec-kit methodology (`reference/spec-kit/`)

### Phase 2: AI Integration (Week 3-4)
1. Explore Dash AI Chat Tutorial (`reference/dash-ai-chat-tutorial/`)
2. Study All-in-AI Demo App (`reference/all-in-ai-demo-app/`)
3. Learn LangGraph basics (`reference/langgraph/`)
4. Review Anthropic Cookbook (`reference/anthropic-cookbook/`)

### Phase 3: Agent Development (Week 5-6)
1. Build with Pydantic-AI (`reference/pydantic-ai/`)
2. Experiment with MCP (`reference/mcp-python-sdk/`)
3. Study multi-agent patterns (`reference/openai-swarm/`)
4. Implement agent-driven features

### Phase 4: Production Deployment (Week 7-8)
1. Configure Claude Agent SDK (`reference/claude-agent-sdk-python/`)
2. Study AWS Bedrock examples (if using AWS)
3. Containerize with Docker
4. Set up monitoring and observability

## Contributing

To add new references:

1. Clone the repository to `reference/`
2. Update this document with:
   - Repository name and description
   - Link to GitHub
   - Category classification
   - Integration patterns (if applicable)

3. Update `PROJECT_STRUCTURE.md` if structure changes

## Maintenance

- **Review references quarterly** for updates
- **Test cloned repos** work with current dependencies
- **Archive deprecated repos** to `reference/archived/`
- **Document breaking changes** in CHANGELOG.md

---

*Last updated: 2025-11-10*
*Total reference repositories: 23 cloned, 50+ additional resources*
