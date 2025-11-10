---
allowed-tools: Read, Write, Bash(docker:*)
description: Configure Claude Agent SDK deployment
---

# Configure Agent SDK Deployment

Prepare the dashboard for production deployment using Claude Agent SDK.

## Current Context

- Project: !`cat README.md | head -20`
- Current Features: !`ls -1 .specify/specs/`

## Your Task

Generate production deployment configuration:

1. **Create agents/ directory structure**
   ```
   agents/
   ├── config/
   │   ├── agent_config.yaml
   │   ├── resources.yaml
   │   └── secrets.yaml.example
   ├── deployment/
   │   ├── Dockerfile
   │   └── docker-compose.yml
   └── monitoring/
       ├── health_checks.py
       └── metrics.py
   ```

2. **Generate Agent SDK configuration**
   - Define agent capabilities
   - Set resource limits (CPU, memory)
   - Configure health checks
   - Define environment variables

3. **Create Dockerfile**
   - Base image: Python 3.11+
   - Install dependencies
   - Copy application code
   - Set entrypoint

4. **Create docker-compose.yml**
   - Dashboard service
   - Database service (if needed)
   - Redis cache (if needed)
   - Network configuration

5. **Create health check script**
   - Liveness endpoint
   - Readiness endpoint
   - Dependency checks

6. **Generate deployment documentation**
   - Environment variables needed
   - Deployment instructions
   - Rollback procedures

## Output Files

- `agents/config/agent_config.yaml`
- `agents/deployment/Dockerfile`
- `agents/deployment/docker-compose.yml`
- `agents/monitoring/health_checks.py`
- `docs/DEPLOYMENT.md`

## Next Steps

Inform the user:
1. Review generated configuration
2. Set environment variables
3. Test locally with Docker Compose
4. Deploy to Agent SDK platform
