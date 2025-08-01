# Awesome Claude Agents - AI Development Team 🚀

**Supercharge Claude Code with a team of specialized AI agents** that work together to build complete features, debug complex issues, and handle any technology stack with expert-level knowledge.

## ⚠️ Important Notice

**This project is experimental and token-intensive.** I'm actively testing these agents with Claude subscription - expect high token consumption during complex workflows. Multi-agent orchestration can consume 10-50k tokens per complex feature. Use with caution and monitor your usage.

## 🚀 Quick Start (3 Minutes)

### Prerequisites
- **Claude Code CLI** installed and authenticated
- **Claude subscription** - required for intensive agent workflows
- Active project directory with your codebase
- **Optional**: [Context7 MCP](docs/dependencies.md) for enhanced documentation access

### 1. Install the Agents
```bash
git clone https://github.com/vijaythecoder/awesome-claude-agents.git
```

#### Option A: Symlink (Recommended - auto-updates)

**macOS/Linux:**
```bash
# Create agents directory if it doesn't exist (preserves existing agents)
mkdir -p ~/.claude/agents

# Symlink the awesome-claude-agents collection
ln -sf "$(pwd)/awesome-claude-agents/agents/" ~/.claude/agents/awesome-claude-agents
```

**Windows (PowerShell):**
```powershell
# Create agents directory
New-Item -Path "$env:USERPROFILE\.claude\agents" -ItemType Directory -Force

# Create symlink
cmd /c mklink /D "$env:USERPROFILE\.claude\agents\awesome-claude-agents" "$(Get-Location)\awesome-claude-agents\agents"
```

#### Option B: Copy (Static - no auto-updates)
```bash
# Create agents directory if it doesn't exist
mkdir -p ~/.claude/agents

# Copy all agents
cp -r awesome-claude-agents/agents ~/.claude/agents/awesome-claude-agents
```

### 2. Verify Installation
```bash
claude /agents
# Should show all 24 agents.
```

### 3. Initialize Your Project
**Navigate** to your **project directory** and run the following command to configure your AI team:

```bash
claude "use @agent-team-configurator and optimize my project to best use the available subagents."
```

### 4. Start Building
```bash
claude "use @agent-tech-lead-orchestrator and build a user authentication system"
```

Your AI team will automatically detect your stack and use the right specialists!

## 🎯 How Auto-Configuration Works

The @agent-team-configurator automatically sets up your perfect AI development team. When invoked, it:

1. **Locates CLAUDE.md** - Finds existing project configuration and preserves all your custom content outside the "AI Team Configuration" section
2. **Detects Technology Stack** - Inspects package.json, composer.json, requirements.txt, go.mod, Gemfile, and build configs to understand your project
3. **Discovers Available Agents** - Scans ~/.claude/agents/ and .claude/ folders, building a capability table of all available specialists
4. **Selects Specialists** - Prefers framework-specific agents over universal ones, always includes @agent-code-reviewer and @agent-performance-optimizer for quality assurance
5. **Updates CLAUDE.md** - Creates a timestamped "AI Team Configuration" section with your detected stack and a Task|Agent|Notes mapping table
6. **Provides Usage Guidance** - Shows you the detected stack, selected agents, and gives sample commands to start building


## 👥 Meet Your AI Development Team

### 🎭 Orchestrators (3 agents)
- **[Tech Lead Orchestrator](agents/orchestrators/tech-lead-orchestrator.md)** - Senior technical lead who analyzes complex projects and coordinates multi-step development tasks
- **[Project Analyst](agents/orchestrators/project-analyst.md)** - Technology stack detection specialist who enables intelligent agent routing
- **[Team Configurator](agents/orchestrators/team-configurator.md)** - AI team setup expert who detects your stack and configures optimal agent mappings

### 💼 Framework Specialists (13 agents)
- **Laravel (2 agents)**
  - **[Backend Expert](agents/specialized/laravel/laravel-backend-expert.md)** - Comprehensive Laravel development with MVC, services, and Eloquent patterns
  - **[Eloquent Expert](agents/specialized/laravel/laravel-eloquent-expert.md)** - Advanced ORM optimization, complex queries, and database performance
- **Django (3 agents)**
  - **[Backend Expert](agents/specialized/django/django-backend-expert.md)** - Models, views, services following current Django conventions
  - **[API Developer](agents/specialized/django/django-api-developer.md)** - Django REST Framework and GraphQL implementations
  - **[ORM Expert](agents/specialized/django/django-orm-expert.md)** - Query optimization and database performance for Django applications
- **Rails (3 agents)**
  - **[Backend Expert](agents/specialized/rails/rails-backend-expert.md)** - Full-stack Rails development following conventions
  - **[API Developer](agents/specialized/rails/rails-api-developer.md)** - RESTful APIs and GraphQL with Rails patterns
  - **[ActiveRecord Expert](agents/specialized/rails/rails-activerecord-expert.md)** - Complex queries and database optimization
- **React (2 agents)**
  - **[Component Architect](agents/specialized/react/react-component-architect.md)** - Modern React patterns, hooks, and component design
  - **[Next.js Expert](agents/specialized/react/react-nextjs-expert.md)** - SSR, SSG, ISR, and full-stack Next.js applications
- **Vue (3 agents)**
  - **[Component Architect](agents/specialized/vue/vue-component-architect.md)** - Vue 3 Composition API and component patterns
  - **[Nuxt Expert](agents/specialized/vue/vue-nuxt-expert.md)** - SSR, SSG, and full-stack Nuxt applications
  - **[State Manager](agents/specialized/vue/vue-state-manager.md)** - Pinia and Vuex state architecture

### 🌐 Universal Experts (4 agents)
- **[Backend Developer](agents/universal/backend-developer.md)** - Polyglot backend development across multiple languages and frameworks
- **[Frontend Developer](agents/universal/frontend-developer.md)** - Modern web technologies and responsive design for any framework
- **[API Architect](agents/universal/api-architect.md)** - RESTful design, GraphQL, and framework-agnostic API architecture
- **[Tailwind Frontend Expert](agents/universal/tailwind-css-expert.md)** - Tailwind CSS styling, utility-first development, and responsive components

### 🔧 Core Team (4 agents)
- **[Code Archaeologist](agents/core/code-archaeologist.md)** - Explores, documents, and analyzes unfamiliar or legacy codebases
- **[Code Reviewer](agents/core/code-reviewer.md)** - Rigorous security-aware reviews with severity-tagged reports
- **[Performance Optimizer](agents/core/performance-optimizer.md)** - Identifies bottlenecks and applies optimizations for scalable systems
- **[Documentation Specialist](agents/core/documentation-specialist.md)** - Crafts comprehensive READMEs, API specs, and technical documentation

**Total: 24 specialized agents** working together to build your projects!

[Browse all agents →](agents/)


## 🔥 Why Teams Beat Solo AI

- **Specialized Expertise**: Each agent masters their domain with deep, current knowledge
- **Real Collaboration**: Agents coordinate seamlessly, sharing context and handing off tasks
- **Tailored Solutions**: Get code that matches your exact stack and follows its best practices
- **Parallel Execution**: Multiple specialists work simultaneously for faster delivery

## 📈 The Impact

- **Ship Faster** - Complete features in minutes, not days
- **Better Code Quality** - Every line follows best practices
- **Learn As You Code** - See how experts approach problems
- **Scale Confidently** - Architecture designed for growth

## 📚 Learn More

- [Creating Custom Agents](docs/creating-agents.md) - Build specialists for your needs  
- [Best Practices](docs/best-practices.md) - Get the most from your AI team

## 💬 Join The Community

- ⭐ **Star this repo** to show support
- 🐛 [Report issues](https://github.com/vijaythecoder/awesome-claude-agents/issues)
- 💡 [Share ideas](https://github.com/vijaythecoder/awesome-claude-agents/discussions)
- 🎉 [Success stories](https://github.com/vijaythecoder/awesome-claude-agents/discussions/categories/show-and-tell)

## 📄 License

MIT License - Use freely in your projects!

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=vijaythecoder/awesome-claude-agents&type=Date)](https://www.star-history.com/#vijaythecoder/awesome-claude-agents&Date)
---

<p align="center">
  <strong>Transform Claude Code into an AI development team that ships production-ready features</strong><br>
  <em>Simple setup. Powerful results. Just describe and build.</em>
</p>

<p align="center">
  <a href="https://github.com/vijaythecoder/awesome-claude-agents">GitHub</a> •
  <a href="docs/creating-agents.md">Documentation</a> •
  <a href="https://github.com/vijaythecoder/awesome-claude-agents/discussions">Community</a>
</p>