# Quick Start Guide - 100x Your Productivity in 5 Minutes

## Installation

```bash
# Clone the repository
git clone https://github.com/yourusername/awesome-claude-agents.git

# Copy agents to your Claude Code directory
cp -r awesome-claude-agents/agents/* ~/.claude/agents/

# Verify installation
claude /agents
```

## Your First Agent Experience

### Example 1: Understanding a Codebase
```bash
> I need to understand this React codebase I inherited

# Code Archaeologist automatically activates
# Provides architecture overview, patterns, and documentation
```

### Example 2: Building a Feature
```bash
> Build a user authentication system

# Tech Lead Orchestrator coordinates:
# - API design
# - Database schema
# - Frontend forms
# - Security review
```

### Example 3: Fixing Performance
```bash
> The app is slow, fix it

# Performance Optimizer analyzes and fixes:
# - Slow queries
# - Memory leaks
# - Bundle sizes
# - API bottlenecks
```

## How Agents Work Together

Agents automatically collaborate based on the task:

```
Simple Task → Single Agent
Complex Task → Orchestrator → Multiple Specialists
```

### Real Example Flow

**User**: "Build a REST API for a todo app"

```
1. Tech Lead Orchestrator activates
   ↓
2. API Architect designs endpoints
   ↓
3. Backend Developer implements
   ↓
4. Test Engineer writes tests
   ↓
5. Code Reviewer ensures quality
   ↓
6. Complete, tested API ready!
```

## Universal Technology Support

Works with ANY stack you're using:

### JavaScript/TypeScript
```bash
> Build a React component with TypeScript
> Create an Express API with authentication
> Optimize this Next.js application
```

### Python
```bash
> Create a Django REST API
> Build a FastAPI microservice
> Optimize this pandas data pipeline
```

### Java/Kotlin
```bash
> Create a Spring Boot application
> Build an Android app
> Refactor this legacy Java code
```

### Any Language!
Go, Rust, Ruby, PHP, C#, Swift - agents adapt to your technology.

## Key Commands

### List All Agents
```bash
claude /agents
```

### Force Specific Agent
```bash
> Use the code-reviewer to check my changes
```

### Get Help
```bash
claude /help
```

## Advanced Tips

### 1. Let Agents Delegate
Don't specify every agent - let them hand off tasks:
```bash
# Good
> Build a chat application

# Not needed
> Use tech lead, then backend, then frontend...
```

### 2. Provide Context
More context = better results:
```bash
# Good
> Build a real-time chat with React frontend and Node.js backend, supporting 1000 concurrent users

# Too vague
> Make a chat
```

### 3. Trust the Process
Agents know when to involve others:
- Tech Lead brings in specialists
- Code Reviewer calls Security Guardian if needed
- Performance Optimizer involves Database Optimizer

## Common Workflows

### New Feature
```
Describe feature → Tech Lead plans → Specialists implement → Review → Deploy
```

### Debug Issue
```
Describe problem → Debugger investigates → Expert fixes → Tester verifies
```

### Understand Code
```
Point to codebase → Code Archaeologist explores → Documentation ready
```

### Optimize Performance
```
Report slowness → Performance Optimizer profiles → Specialists fix → Faster app
```

## What's Next?

1. **Try Different Agents**
   - Each has unique expertise
   - They work better together

2. **Build Something**
   - Start with a small feature
   - Watch agents collaborate

3. **Create Custom Workflows**
   - Chain agents for your process
   - Save common patterns

4. **Contribute**
   - Create new agents
   - Improve existing ones
   - Share your workflows

## Troubleshooting

### Agents Not Found
```bash
# Check installation
ls ~/.claude/agents/

# Reinstall if needed
cp -r awesome-claude-agents/agents/* ~/.claude/agents/
```

### Wrong Agent Activated
```bash
# Be more specific
> Use the performance-optimizer to check database queries

# Or provide more context
> The database queries are slow (triggers database-optimizer)
```

### Need Specific Technology
```bash
# Agents adapt to your stack
> Build this in [Go/Rust/Elixir/any language]
```

## Pro Tips

1. **Start Small** - Let one agent impress you
2. **Think in Workflows** - Agents chain naturally
3. **Trust Delegation** - They know when to hand off
4. **Learn from Output** - See how experts approach problems

Ready to experience 100x productivity? Start with any task!