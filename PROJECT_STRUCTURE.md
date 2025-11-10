# Project Structure

```
cc-dash-as-code/
├── .git/                                   # Git repository
├── .specify/                               # Spec-kit infrastructure
│   ├── memory/
│   │   └── constitution.md                # Project principles & guidelines
│   ├── specs/
│   │   └── 001-dashboard-foundation/
│   │       └── spec.md                    # Foundation specification
│   ├── templates/
│   │   ├── agent-file-template.md
│   │   ├── checklist-template.md
│   │   ├── plan-template.md
│   │   ├── spec-template.md
│   │   └── tasks-template.md
│   └── scripts/                           # Helper scripts (to be added)
├── src/                                   # Application source code (to be added)
├── tests/                                 # Test files (to be added)
├── agents/                                # Claude Agent SDK configs (to be added)
├── docs/                                  # Documentation
│   ├── ARCHITECTURE.md                    # Architecture guide
│   └── QUICKSTART.md                      # Quick start guide
├── reference/                             # Reference repositories (23 repos cloned)
│   ├── dash/                             # Plotly Dash framework
│   ├── spec-kit/                         # GitHub spec-kit methodology
│   ├── claude-agent-sdk-python/          # Claude Agent SDK
│   ├── ai-experiments/                   # MCP agent experiments
│   ├── all-in-ai-demo-app/               # Dash + AI chatbot demo
│   ├── dash-ai-chat-tutorial/            # Dash AI integration tutorial
│   ├── dashboard-agents/                 # Agent-driven dashboard generation
│   ├── langchain/                        # LangChain framework
│   ├── langgraph/                        # LangGraph multi-agent orchestration
│   ├── pydantic-ai/                      # Type-safe AI agent framework
│   ├── phidata/                          # Production AI agent infrastructure
│   ├── openai-swarm/                     # Multi-agent collaboration patterns
│   ├── llama_index/                      # RAG framework
│   ├── mem0/                             # Agent memory layer
│   ├── autogpt/                          # Autonomous agent framework
│   ├── vercel-ai/                        # TypeScript AI SDK
│   ├── streamlit/                        # Alternative dashboard framework
│   ├── mcp-servers/                      # MCP server implementations
│   ├── mcp-python-sdk/                   # MCP Python SDK
│   ├── bedrock-agents-streamlit/         # AWS Bedrock + Streamlit
│   ├── amazon-bedrock-agentcore-samples/ # AWS enterprise agent samples
│   ├── AI-Agent-Host/                    # Agent testing environment
│   ├── anthropic-cookbook/               # Claude API examples
│   └── anthropic-courses/                # Anthropic learning materials
├── .gitignore                            # Git ignore patterns
├── README.md                             # Project overview
├── requirements.txt                      # Python dependencies
└── PROJECT_STRUCTURE.md                  # This file
```

## Key Files Created

### 1. Constitution (.specify/memory/constitution.md)
Establishes project-wide principles including:
- Specification-first development approach
- Code quality standards (80% test coverage, type hints, formatting)
- Dashboard development standards (responsive, accessible, performant)
- Security and privacy requirements
- Testing and validation requirements
- Documentation standards

### 2. Foundation Specification (.specify/specs/001-dashboard-foundation/spec.md)
Comprehensive specification covering:
- 6 prioritized user stories (P1-P3)
- 39 functional requirements
- 23 measurable success criteria
- Edge cases and clarifications
- Review & acceptance checklist

### 3. Documentation
- **README.md**: Project overview and getting started
- **QUICKSTART.md**: 10-minute quick start guide
- **ARCHITECTURE.md**: Detailed architectural documentation
- **REFERENCES.md**: Comprehensive catalog of 50+ AI agent and dashboard resources

### 4. Templates (.specify/templates/)
Ready-to-use templates for:
- New feature specifications
- Technical implementation plans
- Task breakdowns
- Checklists
- Agent configurations

### 5. Development Configuration
- **.gitignore**: Comprehensive Python/Dash ignore patterns
- **requirements.txt**: Curated dependencies for Dash development

## Reference Repositories

The `reference/` directory contains **23 cloned repositories** organized by category:

### Core Frameworks (4)
1. **dash** - Plotly Dash interactive dashboards
2. **spec-kit** - Specification-driven development methodology
3. **claude-agent-sdk-python** - Claude Agent SDK for production
4. **streamlit** - Alternative dashboard framework

### AI Agent Frameworks (9)
5. **langchain** - LLM application framework
6. **langgraph** - Stateful multi-actor applications
7. **pydantic-ai** - Type-safe agent framework
8. **phidata** - Production-ready agent infrastructure
9. **openai-swarm** - Multi-agent orchestration patterns
10. **llama_index** - RAG framework for LLM apps
11. **mem0** - Memory layer for agents
12. **autogpt** - Autonomous task execution
13. **vercel-ai** - TypeScript AI toolkit

### Dash + AI Integrations (3)
14. **all-in-ai-demo-app** - Complete Dash app with AI chatbot
15. **dash-ai-chat-tutorial** - AI API integration tutorial
16. **dashboard-agents** - Agent-driven dashboard generation

### Model Context Protocol (3)
17. **mcp-servers** - Official MCP server implementations
18. **mcp-python-sdk** - Python SDK for MCP
19. **ai-experiments** - MCP agent experiment (includes mcp-agent-experiment/)

### Cloud & Enterprise (3)
20. **bedrock-agents-streamlit** - AWS Bedrock + Streamlit examples
21. **amazon-bedrock-agentcore-samples** - Enterprise agent deployment
22. **AI-Agent-Host** - Docker-based agent testing environment

### Learning Resources (2)
23. **anthropic-cookbook** - Claude API recipes and examples
24. **anthropic-courses** - Official Anthropic learning materials

For a complete catalog including 50+ additional online resources, see **[docs/REFERENCES.md](docs/REFERENCES.md)**.

## Next Steps

1. **Review the constitution**: Read `.specify/memory/constitution.md`
2. **Study the foundation spec**: Review `.specify/specs/001-dashboard-foundation/spec.md`
3. **Follow the quick start**: Execute `docs/QUICKSTART.md`
4. **Create your first feature**: Use the spec → plan → tasks → implement workflow
5. **Deploy to production**: Configure Claude Agent SDK for deployment

## Development Workflow

1. Create specification using `/speckit.specify` or template
2. Create technical plan using `/speckit.plan` or template
3. Generate tasks using `/speckit.tasks` or template
4. Implement with Claude Code following TDD
5. Deploy with Claude Agent SDK

---

This structure supports the complete spec-driven dashboard development lifecycle from initial concept to production deployment.
