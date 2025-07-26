# Contributing to Awesome Claude Agents

Thank you for your interest in contributing to Awesome Claude Agents! This document provides guidelines and instructions for contributing to our collection of specialized Claude sub-agents.

## 🎯 Our Mission

We aim to build the most comprehensive, high-quality collection of Claude sub-agents that enhance productivity across various domains. Every contribution helps make Claude Code more powerful for the community.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How to Contribute](#how-to-contribute)
- [Creating New Agents](#creating-new-agents)
- [Improving Existing Agents](#improving-existing-agents)
- [Reporting Issues](#reporting-issues)
- [Pull Request Process](#pull-request-process)
- [Agent Quality Standards](#agent-quality-standards)
- [Testing Guidelines](#testing-guidelines)

## 📜 Code of Conduct

We are committed to providing a welcoming and inclusive environment. Please:

- Be respectful and constructive in all interactions
- Welcome newcomers and help them get started
- Focus on what is best for the community
- Show empathy towards other community members

## 🤝 How to Contribute

### 1. Fork and Clone

```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/awesome-claude-agents.git
cd awesome-claude-agents
git remote add upstream https://github.com/ORIGINAL_OWNER/awesome-claude-agents.git
```

### 2. Create a Branch

```bash
git checkout -b feature/agent-name
# or
git checkout -b fix/issue-description
```

### 3. Make Your Changes

Follow our guidelines below for creating or improving agents.

### 4. Test Your Changes

Ensure your agent works correctly with Claude Code before submitting.

### 5. Commit Your Changes

```bash
git add .
git commit -m "feat: add [agent-name] for [purpose]"
# or
git commit -m "fix: improve [agent-name] [what was fixed]"
```

Follow [Conventional Commits](https://www.conventionalcommits.org/) format.

### 6. Push and Create PR

```bash
git push origin feature/agent-name
```

Then create a Pull Request on GitHub.

## 🆕 Creating New Agents

### Agent File Structure

Place your agent in the appropriate category:
```
agents/
├── development/
│   ├── frontend/
│   ├── backend/
│   └── ...
├── project-management/
├── business/
└── content-creation/
```

### Agent Format

```yaml
---
name: your-agent-name
description: Clear description of when this agent should be used (be specific for better auto-detection)
tools: Tool1, Tool2, Tool3  # Optional - omit to inherit all tools
---

# Agent Name - Specialist in [Domain]

You are an expert [role] specializing in [specific area]. Your primary responsibilities include:

## Core Expertise
- [Expertise area 1]
- [Expertise area 2]
- [Expertise area 3]

## Working Principles
1. [Principle 1]
2. [Principle 2]
3. [Principle 3]

## Task Approach
When given a task, you:
1. [Step 1]
2. [Step 2]
3. [Step 3]

## Best Practices
- [Best practice 1]
- [Best practice 2]
- [Best practice 3]

## Common Patterns
[Include domain-specific patterns, frameworks, or methodologies]

## Quality Standards
[Define what constitutes quality work in this domain]
```

### Agent Naming Convention

- Use lowercase with hyphens: `tailwind-frontend-expert`
- Be specific: `react-component-architect` not just `react-developer`
- Include the domain: `api-architect`, `ui-specialist`

### Required Documentation

For each new agent, create:

1. **Agent file**: `agents/category/subcategory/agent-name.md`
2. **Example usage**: `examples/agent-name-example.md`
3. **Update README**: Add your agent to the appropriate section

## 🔧 Improving Existing Agents

### Enhancement Guidelines

- Test extensively before modifying core behavior
- Maintain backward compatibility
- Document what was changed and why
- Update examples if behavior changes

### Common Improvements

- Adding new tools or removing unnecessary ones
- Enhancing domain knowledge
- Improving task detection
- Adding error handling patterns
- Updating for new framework versions

## 🐛 Reporting Issues

### Before Reporting

1. Check existing issues to avoid duplicates
2. Test with the latest version of Claude Code
3. Verify the issue is with the agent, not Claude Code itself

### Issue Template

```markdown
**Agent Name**: [agent-name]
**Issue Type**: Bug / Enhancement / Feature Request
**Claude Code Version**: [version]

**Description**:
[Clear description of the issue]

**Steps to Reproduce**:
1. [Step 1]
2. [Step 2]

**Expected Behavior**:
[What should happen]

**Actual Behavior**:
[What actually happens]

**Additional Context**:
[Any other relevant information]
```

## 🔄 Pull Request Process

### PR Title Format
- `feat: add [agent-name] agent for [purpose]`
- `fix: correct [issue] in [agent-name]`
- `docs: update [what] for [agent-name]`
- `refactor: improve [what] in [agent-name]`

### PR Description Template

```markdown
## Description
[Describe your changes]

## Type of Change
- [ ] New agent
- [ ] Bug fix
- [ ] Enhancement
- [ ] Documentation update

## Testing
- [ ] Tested with Claude Code locally
- [ ] Added/updated examples
- [ ] Updated documentation

## Checklist
- [ ] Follows agent format guidelines
- [ ] Includes meaningful examples
- [ ] Tools are appropriate for the task
- [ ] No sensitive information included
- [ ] Commits follow conventional format

## Related Issues
Closes #[issue-number]
```

## ✅ Agent Quality Standards

### Essential Requirements

1. **Clear Purpose**: Agent must have a well-defined, specific purpose
2. **Appropriate Tools**: Only request necessary tools
3. **Professional Tone**: Maintain expertise while being helpful
4. **Error Handling**: Include guidance for common issues
5. **Best Practices**: Incorporate industry standards
6. **Proactive Assistance**: Anticipate user needs

### Quality Checklist

- [ ] Agent name follows naming convention
- [ ] Description enables good auto-detection
- [ ] System prompt is comprehensive but focused
- [ ] Examples demonstrate real-world usage
- [ ] No typos or grammatical errors
- [ ] Tools are minimal but sufficient
- [ ] Includes domain-specific best practices

### Anti-Patterns to Avoid

- ❌ Overly broad agents ("general-developer")
- ❌ Requesting all tools when only a few are needed
- ❌ Vague or generic system prompts
- ❌ Missing concrete examples
- ❌ Duplicating existing agents
- ❌ Including user-specific information

## 🧪 Testing Guidelines

### Local Testing

1. **Install your agent locally**:
   ```bash
   cp agents/category/your-agent.md ~/.claude/agents/
   ```

2. **Test auto-invocation**:
   ```bash
   claude "Task that should trigger your agent"
   ```

3. **Test explicit invocation**:
   ```bash
   claude "Use the your-agent to do something"
   ```

### Test Scenarios

Create test cases for:
- Common use cases
- Edge cases
- Error scenarios
- Integration with other tools
- Performance with large inputs

### Validation Script

Before submitting, run:
```bash
python tests/validate_agents.py agents/category/your-agent.md
```

## 🎉 Recognition

Contributors will be:
- Listed in our [Contributors](CONTRIBUTORS.md) file
- Credited in agent metadata
- Mentioned in release notes
- Eligible for "Top Contributor" badges

## 💡 Tips for Success

1. **Study existing agents**: Learn from well-rated agents
2. **Be specific**: Focused agents perform better than general ones
3. **Test thoroughly**: Real-world testing prevents issues
4. **Document well**: Good examples help users understand capabilities
5. **Iterate**: Start simple and enhance based on feedback

## 📞 Getting Help

- **Discord**: [Join our community](https://discord.gg/awesome-claude-agents)
- **Discussions**: Use GitHub Discussions for questions
- **Issues**: Report bugs via GitHub Issues
- **Email**: maintainers@awesome-claude-agents.dev

---

Thank you for contributing to Awesome Claude Agents! Your expertise helps make Claude Code more powerful for everyone. 🚀