# AI Instructions & Skills

## Repository purpose

This private repository stores the source versions of personally maintained AI instructions and reusable Skills.

The original 14 ChatGPT sources (About Me, Custom Instructions, and 12 Skills) have been imported and are maintained here. The Skills collection now also includes `task-clarification`, bringing the source inventory to 13 Skills. The Codex Custom Instructions file remains a placeholder pending its own source import.

Since 2026-09-16 the repository also holds a Claude surface under `claude/` (see [`claude/README.md`](claude/README.md)): six Skills for claude.ai / Cowork / Claude Code, five of them ports of the ChatGPT Skills with the same exact names, plus a Claude variant of `task-clarification`. Same-named Skills on the two surfaces are the same contract; each `SKILL.md` records its source commit and the specific differences.

Source changes do not install or activate configurations.

## Truth layers

### GitHub

**Source Canonical**

Stores:

- ChatGPT About Me
- ChatGPT Custom Instructions
- ChatGPT Personal Skills (`chatgpt/skills/`)
- Claude Personal Skills (`claude/skills/`)
- Codex Custom Instructions
- future explicitly approved AI instruction sources

### Notion

**Governance / Architecture / Registry Canonical**

Stores:

- architecture
- governance
- Skills Registry
- version status
- testing status
- configuration decisions

Do not duplicate every SKILL.md as a second editable source in Notion.

### AI product UI

**Runtime / Active Configuration Truth**

The configuration actually installed or active in ChatGPT, Codex, or another AI surface must be verified independently.

GitHub source does not prove that the same version is currently installed.

## Change policy

Before changing an existing instruction or Skill:

1. Read the current source.
2. Preserve Git history.
3. Make the smallest complete change.
4. Keep useful project knowledge, safety rules, and permission boundaries.
5. Validate structure and references.
6. Run relevant regression tests when behavior or routing changes.
7. Do not claim performance, speed, or model improvements without testing.
8. Do not assume GitHub source equals currently installed runtime state.

## Source and package maintenance

Maintain each Skill as its complete folder: `SKILL.md` plus any linked `references/`, scripts, or assets. When the product supports Skill packages, import or replace the complete folder/package so supporting references remain available; copying only the entrypoint is insufficient for Skills that link supporting files.

The 2026-09-06 revision targets shared use by Astra and Sol. Five larger Skills route to optional references; short tasks keep essential instructions in the entrypoint. Validation results and installed state are recorded separately in Notion. A source revision or local test does not prove that the ChatGPT desktop installation has been updated or tested.

For future source imports, read the actual configuration or original package. Do not reconstruct source from Notion, Memory, a Registry, or inferred settings. Import the Codex Custom Instructions only when its current source is available.

## Task clarification

[`task-clarification`](chatgpt/skills/task-clarification/SKILL.md) (任務釐清) turns a directionally established request with missing key decisions or specifications into a complete task instruction. Use it only when the user explicitly asks for a clarification-first workflow or selects the skill, not merely because a task is ambiguous. Keep its complete folder, including `agents/openai.yaml`, which preserves the display name and enables implicit skill routing (`allow_implicit_invocation: true`) for matching requests. Existing authorization to execute after clarification carries forward. GitHub storage does not establish ChatGPT installation or product behavior.

The Claude surface variant, [`claude/skills/task-clarification/SKILL.md`](claude/skills/task-clarification/SKILL.md), keeps the same trigger scope and deliverable but composes Claude's built-in AskUserQuestion and Plan mode instead of restating the questioning logic; it carries no `agents/openai.yaml`, so explicit-scope routing is expressed in its description.
