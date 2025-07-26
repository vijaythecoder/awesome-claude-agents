# Best Practices for Claude Agents

This guide outlines best practices for creating and maintaining high-quality Claude sub-agents.

## Agent Design Principles

### 1. Single Responsibility
Each agent should focus on one specific domain or skill set. Avoid creating "Swiss Army knife" agents that try to do everything.

✅ **Good**: `tailwind-frontend-expert` - Focused on Tailwind CSS
❌ **Bad**: `general-developer` - Too broad

### 2. Clear Expertise Definition
Define exactly what your agent knows and doesn't know. Set clear boundaries.

```yaml
# Good description
description: Expert in React component architecture, hooks, and performance optimization. Specializes in building scalable, maintainable React applications. Use proactively for React component design, state management, and optimization tasks.

# Bad description  
description: Helps with React stuff
```

### 3. Proactive Assistance
Design agents to anticipate user needs and offer help without being asked.

```markdown
When I see:
- Inefficient component re-renders
- Missing error boundaries
- Accessibility issues
- Performance bottlenecks

I proactively suggest improvements and offer to implement them.
```

## System Prompt Best Practices

### 1. Structure and Organization

Use clear sections with headers:
- Core Expertise
- Working Principles
- Task Approach
- Best Practices
- Common Patterns
- Quality Standards

### 2. Concrete Examples

Always include code examples:

```markdown
## Common Patterns

### Error Boundary Implementation
```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }
  
  static getDerivedStateFromError(error) {
    return { hasError: true };
  }
  
  componentDidCatch(error, errorInfo) {
    console.error('Error caught:', error, errorInfo);
  }
  
  render() {
    if (this.state.hasError) {
      return <h1>Something went wrong.</h1>;
    }
    return this.props.children;
  }
}
```
```

### 3. Actionable Guidelines

Provide step-by-step approaches:

```markdown
## Task Approach

When optimizing a React component:
1. Profile with React DevTools to identify bottlenecks
2. Check for unnecessary re-renders
3. Implement React.memo for pure components
4. Use useMemo/useCallback for expensive operations
5. Verify improvements with profiler
```

## Tool Usage Guidelines

### 1. Minimal Tool Set

Only request tools you actually need:

| Agent Type | Recommended Tools |
|------------|------------------|
| Frontend Developer | Read, Write, Edit, MultiEdit, Grep, WebFetch |
| Backend Developer | Read, Write, Edit, Bash, Grep, Glob |
| DevOps Engineer | All tools |
| Content Writer | Read, Write, WebFetch |

### 2. Tool Justification

Document why each tool is needed:

```yaml
tools: Read, Write, Edit, Bash, Grep
# Read: Analyze existing code
# Write: Create new components
# Edit: Modify existing files
# Bash: Run build commands and tests
# Grep: Search for patterns in codebase
```

## Communication Style

### 1. Professional Yet Approachable

- Use technical terms appropriately
- Explain complex concepts clearly
- Maintain expertise without condescension

### 2. Context-Aware Responses

```markdown
I adjust my communication based on:
- User's apparent skill level
- Project complexity
- Time constraints
- Specific requirements
```

### 3. Error Communication

```markdown
When encountering errors:
1. Clearly state what went wrong
2. Explain why it happened
3. Provide 2-3 solution options
4. Recommend the best approach
5. Offer to implement the fix
```

## Quality Standards

### 1. Code Quality

All generated code should:
- Follow language/framework conventions
- Include proper error handling
- Be well-commented when complex
- Pass linting standards
- Include TypeScript types when applicable

### 2. Performance

- Optimize for production use
- Consider bundle size impacts
- Implement lazy loading where appropriate
- Use efficient algorithms and data structures

### 3. Security

- Never expose sensitive data
- Validate all inputs
- Follow OWASP guidelines
- Use secure defaults
- Document security considerations

## Testing Your Agent

### 1. Scenario Testing

Create diverse test scenarios:
- Common use cases
- Edge cases
- Error conditions
- Complex requirements
- Integration scenarios

### 2. Quality Metrics

Measure your agent's performance:
- Task completion rate
- Code quality
- Response accuracy
- Tool usage efficiency
- User satisfaction

### 3. Continuous Improvement

- Gather user feedback
- Monitor common issues
- Update based on new best practices
- Add new patterns and examples

## Common Anti-Patterns to Avoid

### 1. Over-Engineering
❌ Creating complex solutions for simple problems
✅ Start simple, iterate based on needs

### 2. Tool Overuse
❌ Requesting all tools "just in case"
✅ Request only what you need

### 3. Vague Instructions
❌ "Follow best practices"
✅ Specific, actionable guidelines

### 4. Missing Context
❌ Ignoring existing code patterns
✅ Analyze and match project conventions

### 5. One-Size-Fits-All
❌ Same approach for all projects
✅ Adapt to project size and requirements

## Maintenance Guidelines

### 1. Regular Updates
- Review agent performance monthly
- Update for new framework versions
- Add new patterns and best practices
- Remove deprecated approaches

### 2. Version Compatibility
- Document framework version requirements
- Note breaking changes
- Provide migration guides
- Support multiple versions when needed

### 3. Community Feedback
- Monitor issues and discussions
- Implement suggested improvements
- Credit contributors
- Share learnings with community

## Example: Well-Designed Agent Section

```markdown
## Core Expertise

### State Management
- **React Context API**: Efficient global state management for small to medium apps
- **Redux Toolkit**: Modern Redux with less boilerplate for complex state
- **Zustand**: Lightweight alternative for component state sharing
- **React Query/SWR**: Server state management and caching
- **Local State Patterns**: useState, useReducer best practices

Each expertise area includes:
- When to use it
- Implementation patterns
- Performance considerations
- Common pitfalls
- Testing strategies
```

## Conclusion

Creating excellent Claude agents requires:
1. Clear focus and expertise
2. Well-structured system prompts
3. Concrete examples and patterns
4. Appropriate tool selection
5. Continuous improvement

Remember: The best agents solve real problems efficiently while maintaining high quality standards.