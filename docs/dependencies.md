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

## OpenPaw (Optional)

The `openpaw-personal-assistant` agent uses [OpenPaw](https://github.com/daxaur/openpaw) to turn Claude Code into a personal assistant with 38 skills across email, calendar, Spotify, smart home, messaging, notes, and more.

### Installation

```bash
npx pawmode
```

The interactive wizard walks through skill selection, service authentication, and interface setup (terminal, Telegram, or both). For a quick non-interactive install:

```bash
npx pawmode --preset essentials       # common skills, no prompts
npx pawmode --preset developer --yes  # fully non-interactive
```

### What It Adds

- 38 skills across 8 categories (productivity, communication, media, smart home, developer tools, web, system, interface)
- Telegram bridge for mobile access
- Local task dashboard with drag-and-drop kanban
- Smart scheduling with per-run and daily cost caps
- Persistent memory via Obsidian integration

No daemon, no cloud dependency. OpenPaw runs once, writes config, and gets out of the way. Everything runs locally through your existing Claude Code subscription.
