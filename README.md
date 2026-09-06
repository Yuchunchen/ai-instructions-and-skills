# AI Instructions & Skills

## Repository purpose

This private repository stores the source versions of personally maintained AI instructions and reusable Skills.

Phase 1 establishes the source skeleton only. Instruction and Skill files are placeholders awaiting manual import of the current active source. They are not active configurations or installed Skill definitions.

## Truth layers

### GitHub

**Source Canonical**

Stores:

- ChatGPT About Me
- ChatGPT Custom Instructions
- ChatGPT Personal Skills
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

## Manual import

Copy the current active ChatGPT About Me and Custom Instructions from the ChatGPT UI, each installed Personal Skill's original SKILL.md, and the current Codex Custom Instructions (if any) into their matching files.

Do not reconstruct these sources from Notion, Memory, a Skills Registry, or inferred settings. Add supporting Skill package files only when they actually exist in the source package.
