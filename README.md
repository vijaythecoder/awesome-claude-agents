# Awesome Claude Agents 🤖

A curated collection of specialized Claude sub-agents for development, project management, and business workflows. Each agent is crafted with deep domain expertise to enhance your productivity with Claude Code.

## 🚀 Quick Start

### Prerequisites
- [Claude Code](https://github.com/anthropics/claude-code) installed
- Node.js 18+ (for Claude Code)
- MCP servers configured (optional, for enhanced functionality)

### Installation

1. Clone this repository:
```bash
git clone https://github.com/yourusername/awesome-claude-agents.git
cd awesome-claude-agents
```

2. Copy agents to your Claude Code directory:

**For project-specific agents:**
```bash
cp -r agents/* .claude/agents/
```

**For global user agents:**
```bash
cp -r agents/* ~/.claude/agents/
```

3. Verify installation:
```bash
claude /agents
```

## 📚 Agent Categories

### 🎨 Frontend Development
- **[tailwind-frontend-expert](agents/development/frontend/tailwind-frontend-expert.md)** - Tailwind CSS specialist with deep utility-first knowledge
- More coming soon...

### 🔧 Backend Development
- Laravel backend specialist (coming soon)
- API architect (coming soon)
- Database expert (coming soon)

### 🛠️ Full-Stack Development
- Laravel + Inertia.js expert (coming soon)
- Laravel + React specialist (coming soon)
- MERN stack developer (coming soon)

### 🔒 Security
- Security auditor (coming soon)
- Penetration tester (coming soon)
- OWASP specialist (coming soon)

### 📊 Project Management
- Agile project manager (coming soon)
- Sprint coordinator (coming soon)
- Technical project planner (coming soon)

### 💼 Business
- CEO strategic advisor (coming soon)
- CFO financial analyst (coming soon)
- Business analyst (coming soon)

### ✍️ Content Creation
- Technical blog writer (coming soon)
- YouTube script creator (coming soon)
- Documentation specialist (coming soon)

## 🎯 Featured Agents

### Tailwind CSS Frontend Expert
Our flagship agent specializing in modern frontend development with Tailwind CSS.

**Capabilities:**
- ✅ Responsive design implementation
- ✅ Component architecture with utility classes
- ✅ Dark mode and theming
- ✅ Performance optimization
- ✅ Framework integration (React, Vue, etc.)
- ✅ Accessibility best practices

**Usage:**
```bash
# Automatic invocation
> Create a responsive navigation component with dark mode support

# Explicit invocation
> Use the tailwind-frontend-expert to refactor this component
```

## 🔧 Configuration

### Agent Structure
Each agent follows this format:
```yaml
---
name: agent-name
description: When this agent should be used
tools: Read, Write, Edit, Bash, Grep  # Optional - inherits all if omitted
---

System prompt defining the agent's expertise and behavior...
```

### MCP Integration
Agents can leverage MCP servers for enhanced capabilities. When tools are omitted, agents inherit all available MCP tools from your configuration.

## 🤝 Contributing

We welcome contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on:
- Creating new agents
- Submitting improvements
- Reporting issues
- Code of conduct

### Quick Contribution Guide
1. Fork the repository
2. Create your agent in the appropriate category
3. Test thoroughly with Claude Code
4. Submit a pull request with examples

## 📖 Documentation

- [Agent Creation Guide](docs/creating-agents.md) - Learn how to create your own agents
- [Best Practices](docs/best-practices.md) - Guidelines for effective agents
- [Examples](examples/) - Real-world usage examples
- [Templates](templates/) - Starting templates for new agents

## 🧪 Testing

Test agents before deployment:
```bash
# Run validation script
python tests/validate_agents.py

# Test specific agent
claude --agent tailwind-frontend-expert "Create a button component"
```

## 📊 Stats & Community

- 🌟 Star this repo to show support
- 🐛 Report issues in the [issue tracker](https://github.com/yourusername/awesome-claude-agents/issues)
- 💬 Join discussions in [Discussions](https://github.com/yourusername/awesome-claude-agents/discussions)
- 📈 Track agent usage and performance

## 🗺️ Roadmap

### Phase 1 (Current)
- [x] Project structure
- [x] Tailwind CSS expert agent
- [ ] Basic documentation
- [ ] Testing framework

### Phase 2
- [ ] Laravel ecosystem agents
- [ ] Security-focused agents
- [ ] Project management suite

### Phase 3
- [ ] Business and content agents
- [ ] Agent marketplace features
- [ ] Community voting system

## 📄 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Claude Code](https://github.com/anthropics/claude-code) by Anthropic
- All contributors and agent creators
- The Claude community

---

<p align="center">
  Made with ❤️ by the Claude community
</p>

<p align="center">
  <a href="#awesome-claude-agents-">Back to top</a>
</p>