# Dependencies

## Context7 MCP (Optional)

Some agents reference Context7 MCP for fetching up-to-date documentation. While not required (agents will use WebFetch as fallback), Context7 provides better documentation access.

### Installation

1. Install Context7 MCP server:
```bash
claude mcp add context7 -- npx -y @upstash/context7-mcp
```

2. Configure in Claude's MCP settings:
```json
{
  "mcpServers": {
    "context7": {
      "command": "context7-mcp",
      "args": []
    }
  }
}
```

3. Restart Claude Code to activate

### Benefits
- Faster documentation retrieval
- Better structured responses
- Cached documentation access

Without Context7, agents automatically use WebFetch to fetch documentation from official websites.

## Taskade MCP (Optional)

The `taskade-project-manager` agent uses [Taskade MCP](https://github.com/taskade/mcp) to manage projects, tasks, AI agents, and workflow automation directly from Claude Code. Provides 50+ tools for workspace coordination.

### Installation

1. Install Taskade MCP server:
```bash
claude mcp add taskade -- npx -y @taskade/mcp-server
```

2. Set your API key:
```bash
export TASKADE_API_KEY=your_api_key_here
```

Get your API key from [Taskade Settings](https://taskade.com/settings/api).

3. Restart Claude Code to activate

### Benefits
- Manage projects and tasks without leaving the terminal
- Deploy and configure Taskade AI agents from Claude Code
- Automate workflows with triggers and 100+ integrations
- Search and organize work across workspaces

Without Taskade MCP, the `taskade-project-manager` agent is not available.
