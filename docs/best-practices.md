# Crafting High‑Impact Claude Code Sub‑Agents

> **Goal –** Establish a repeatable playbook for designing small, focused “sub‑agents” that Claude can invoke automatically or on‑demand. Follow these practices to get predictable routing, strong task performance, and a maintainable agent library.

---

## 1. File & Folder Conventions

| Element            | Location              | Rationale                        |
| ------------------ | --------------------- | -------------------------------- |
| **Project agents** | `.claude/agents/`     | Highest precedence inside a repo |
| **User agents**    | `~/.claude/agents/`   | Global across projects           |
| **Filename**       | `kebab-case.md`       | Mirrors the `name` field         |
| **VCS**            | Commit project agents | Allows PR‑style reviews          |

*Clash rule:* a project‑level agent overrides a user‑level one with the same **name**.

---

## 2. Mandatory Front‑Matter

```yaml
---
name: unique-agent-name          # Lowercase & hyphens only
description: MUST BE USED …      # Natural‑language trigger phrase
tools: LS, Read, Grep            # Omit to inherit every tool
---
```

* **`name`** – unique, intent‑revealing.
* **`description`** – write **when** and **why** the agent should run; include “**MUST BE USED**” or “**use PROACTIVELY**” to prompt auto‑delegation.
* **`tools`** – whitelist only what’s essential; tighter scope = safer & faster.

---

## 3. System‑Prompt Blueprint

The body of the file (below the front‑matter) is the agent’s **system prompt**. Structure it like a micro‑spec:

1. **Mission / Role** – one sentence that nails the outcome.
2. **Workflow** – numbered steps Claude should always follow.
3. **Output Contract** – exact Markdown or JSON Claude must return.
4. **Heuristics & Checks** – bullet list of edge‑cases, validations, scoring rubrics.
5. *(Optional)* **Delegation cues** – “If X is detected, ask `<other‑agent>`.”

Keep it short but explicit; the prompt is re‑parsed every invocation.

---

## 4. Separate Router & Expert Logic

| Layer             | Audience             | Key phrases                                |
| ----------------- | -------------------- | ------------------------------------------ |
| **`description`** | Claude’s router      | “MUST BE USED…”, “use PROACTIVELY when…”   |
| **Prompt body**   | The sub‑agent itself | “You are an expert… Follow this workflow…” |

Never mix behavioural instructions meant for the agent into the `description` block.

---

## 5. Granularity & Single Responsibility

* One agent = one domain of expertise (`code-reviewer`, `api-architect`).
* Avoid “mega‑agents”; smaller prompts stay in‑context and converge faster.
* Chain work via delegation rather than bloating a single prompt.

---

## 6. Tool‑Granting Strategy

| Scenario                          | Recommended `tools` field                  |
| --------------------------------- | ------------------------------------------ |
| Broad prototyping                 | *(omit `tools`)* – inherit all             |
| Security‑sensitive                | Enumerate minimal set (e.g., `Read, Grep`) |
| Dangerous commands (e.g., `Bash`) | Grant only to trusted, well‑scoped agents  |

Explicit descriptions generally out‑perform code examples for guiding tool use.

---

## 7. Trigger Phrases for Auto‑Delegation

Claude scans conversations for cues that match the `description`. Embed action words to raise recall:

* review · analyze · optimize
* security audit · performance bottleneck
* generate docs · configure team

---

## 8. Testing an Agent

1. **Unit Test** – invoke the agent directly:

   ```
   > Use @agent-code-reviewer to check src/auth.js
   ```
2. **Context Test** – pose a natural request and confirm the router selects the agent automatically.
3. **Regression** – snapshot outputs and assert adherence to the declared schema.

---

## 9. Iteration Workflow

```bash
/agents            # interactive editor
e                  # open file in external editor
git add .claude/agents/*
git commit -m "tune(api-architect): clarify versioning strategy"
```

Iterate in small commits; pair with a `code-reviewer` agent for meta‑feedback.

---

## 10. Style Checklist

* ✅ Active voice, imperative verbs
* ✅ Lower‑case utility names (`code-reviewer`, not `CodeReviewer`)
* ✅ **No external links** inside prompts (keep docs offline)
* ✅ Markdown headings ≤ `###` inside prompt for readability
* ✅ Wrap code fences with language tags for syntax highlighting

---

## Quick‑Start Template

````md
---
name: <agent-name>
description: MUST BE USED to <do X> whenever <condition>. Use PROACTIVELY before <event>.
tools: <tool1>, <tool2>
---

# <Title> – <Concise Role Tagline>

## Mission
One sentence.

## Workflow
1. …
2. …
3. …

## Output Format
```markdown
## Section
- field: value
````

## Heuristics

* Bullet
* Bullet

```

Copy, fill, iterate – and your sub‑agents will perform reliably while keeping the main Claude context lean and focused.

---

**Remember:** crystal‑clear descriptions guide the router; crystal‑clear prompts guide the specialist. Do both, and your agent library becomes a super‑power.

```
