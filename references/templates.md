# Document Templates

Use these minimal skeletons when creating new documents. When reusing or extending an existing file, add only the missing sections and leave the existing structure alone. Write "TBD" in sections that have no content yet, or omit them; never make content up.

The skeletons are written in English. When the document language is different, write the titles, section names, and placeholders in that language (in a Chinese workspace, for example, `# 当前进度` and `- 修改了什么：`) instead of copying the English headings.

## Default file names

The workspace's existing naming habits and the user's preferences take precedence.

| Role | English workspace | Chinese workspace |
|---|---|---|
| Project rules | `AGENTS.md` | `AGENTS.md` |
| Claude Code hookup | `CLAUDE.md` | `CLAUDE.md` |
| Project background | `docs/background.md` | `项目背景.md` |
| Current progress | `docs/progress.md` | `当前进度.md` |
| File navigation | `docs/navigation.md` | `文件导航.md` |
| Progress history | `archive/progress-history.md` | `历史归档/进度历史.md` |

## AGENTS.md

```markdown
# Project Rules

## Before starting work
- Read the [project background](docs/background.md) and [current progress](docs/progress.md) first.
- When looking for material, see [file navigation](docs/navigation.md).

## Evidence and verification
- Evidence required for conclusions: <e.g. citations, experiment logs, location of official documents>
- How to verify: <e.g. test commands, on-device acceptance, data reconciliation steps>

## Updating documents
- Before each work session ends, add an entry at the top of current progress recording what changed, what it was based on, what is still missing, and what comes next.
- Current progress keeps the 5 most recent entries. Move older entries to the top of `<history file path>`, keeping it newest first; create that file the first time an entry is moved.
- When the project's goals, scope, or settled items change, update the project background as well.

## Other conventions
- <supplementary rules the user confirmed>
```

## CLAUDE.md (Claude Code hookup)

When creating it, write only one line:

```markdown
@AGENTS.md
```

When a `CLAUDE.md` already exists, add the same line at the top and leave everything else unchanged.

## Project background

```markdown
# Project Background

## Goals

## Scope
- In scope:
- Out of scope:

## Current phase

## Settled items
- <item> (source: verified fact / user decision)

## Open items
- <item> (assistant suggestion: <suggestion>; awaiting user confirmation)
```

## Current progress

```markdown
# Current Progress

<!-- Newest first; keeps the 5 most recent entries. Older entries are in <history file path>. -->

## YYYY-MM-DD <short title for this session>
- What changed:
- Based on:
- Still missing:
- Next step:
```

## File navigation

```markdown
# File Navigation

| File or directory | Contents | Status |
|---|---|---|
| [<path>](<path>) | <description> | current / outdated / original material |
```
