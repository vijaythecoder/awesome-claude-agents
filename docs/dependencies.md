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
