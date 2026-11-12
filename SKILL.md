---
name: init-workspace
description: First-time setup of working documents (project background, current progress, file navigation) and a project-level AGENTS.md for a long-running project, so any later chat or agent can pick up where the last one left off. Works for empty folders and existing projects, e.g. "organize this workspace so I can keep working on it later" or "first time opening this folder, set up working docs for it". Invoke explicitly with /init-workspace in Claude Code or $init-workspace in Codex. Takes a read-only inventory and proposes a file list first; writes only after the user confirms. For a plain codebase summary, use Claude Code's built-in /init instead. Not for routine progress updates or one-off file tidying.
---

# Initialize Workspace

Work in two rounds. First take stock of the workspace and propose a list of files to create. Write project files only after the user explicitly confirms the list.

## Step 1: Take stock and propose a file list

1. **Identify the target and purpose.** Accept the user's everyday description of what the folder is for. Infer the target workspace and the project's purpose from the conversation and existing material where possible. Ask only when you cannot propose a list without the answer, and ask at most one short blocking question before presenting the list.
2. **Bound the inventory.** Look at the directory structure and top-level documents first, then go deeper only as needed. Do not traverse dependency directories, build outputs, or caches (such as `node_modules`, `dist`, `build`, `.venv`, `.git`), and do not open large binary files. For `.env` files, keys, certificates, and credential files, note only that they exist; never read or repeat their contents.
3. **Check existing rules and material.** Look for `AGENTS.md` and `CLAUDE.md` in this directory, its parent directories, and its subdirectories, as well as global rule files (such as `~/.claude/CLAUDE.md` and `~/.codex/AGENTS.md`). Then read the README and project material. Identify which files already fill the roles in the table below, and avoid new rules that duplicate or conflict with existing ones. Keep existing conventions and original material. When choosing topic documents or drafting the project's verification rules, consult the [scenario examples](references/scenarios.md).
4. **Settle language and naming.** If `~/.agents/init-workspace-preferences.md` exists, read the personal defaults in it. This file is optional, created by the user, and not shipped with the skill; its format is described in the README in the skill directory. Skip it if it does not exist. Resolve conflicts in this order:
   1. What the user explicitly asks for in the current conversation
   2. The project's existing rules
   3. The workspace's existing language and naming habits
   4. The personal preferences file
   5. This skill's defaults

   This skill's defaults: talk to the user in the user's language. In an existing workspace, write documents in the workspace's language; in a new workspace, write them in the user's language. When the conversation language and the document language differ, state the planned document language in the list. Default file names are in the [document templates](references/templates.md).
5. **Present the list.** In the conversation language, show a three-column table whose columns mean "File or path", "Reuse, extend, or create", and "Purpose and planned content". Use the actual file names you plan to use, and list only project files with a clear purpose. After the table, list open questions, limited to ones that affect project scope, acceptance criteria, or long-term rules, and at most three of them. Give each a plain-language default that will be used if the user does not answer it. Put routine naming and formatting directly into the list instead of asking about them. End with a short confirmation prompt, e.g. "Reply 'go ahead' to proceed."
6. **End the round and wait for confirmation.** Stay read-only in this round, even if the user asked to start immediately when invoking the skill. Handle the reply as follows:
   - Explicit confirmation (e.g. "go ahead"): move on to Step 2.
   - Change requests only: present the updated list and keep waiting.
   - A request to proceed with specific changes (e.g. "make these changes and go"): treat it as confirmation of the revised list and move on to Step 2.

   If, while writing, you find that an important item needs to be added, ask the user to confirm the addition first.

## Choosing the documents

| Role | Default approach |
|---|---|
| Project rules | Use `AGENTS.md` to point to the project background and current progress, and to state what evidence is required, how work is verified, and when the documents are updated. Keep existing rules and add the supplementary requirements the user confirmed. |
| Claude Code hookup | At startup Claude Code loads only `CLAUDE.md` automatically, not `AGENTS.md`. When running in Claude Code, or when the project already has a `CLAUDE.md`, include this item: if there is no `CLAUDE.md`, create one containing the single line `@AGENTS.md`; if there is one, add that line at the top (skip this if it already imports `AGENTS.md`). Omit this item when the project is used only in tools that read `AGENTS.md` directly, such as Codex. |
| Project background | Maintain a separate background document, or reuse an existing file of the same kind. Record the goals, scope, current phase, settled items, and open items, and distinguish verified facts, user decisions, and assistant suggestions. |
| Current progress | Maintain a separate progress document, or reuse an existing file of the same kind. Each entry records what changed, what it was based on, what is still missing, and what comes next. The first entry records the verifiable current state of the project and the work done by this initialization. |
| File navigation | When there are few files, reuse the existing README. When the material is numerous or structured enough to need its own index, propose a new navigation document. Link only to material that actually exists. |

Write new documents from the skeletons in the [document templates](references/templates.md). File names follow the project's language and naming habits. Propose topic documents only when there is a clear need for them. When the user has provided fairly complete requirements, link to the original material or keep it in a dedicated document. Mark facts awaiting verification and decisions awaiting confirmation in plain language. Keep applicable existing rules, and ask the user when they substantively conflict with new ones.

**Progress maintenance rules.** When the project has no established rules, use these defaults:
- Current progress keeps the 5 most recent entries, one per work session, newest first.
- When there are more than 5, move the entries that drop off to the top of the history file, so the history also stays newest first.
- Archive directory: if the workspace uses numbered directories (such as `01_sources`, `02_drafts`), name it according to that numbering scheme; otherwise use an unnumbered directory (see "Progress history" under default file names in the [document templates](references/templates.md)).
- Create the archive directory and history file only when the first entry is moved.

Follow existing conventions when there are any, and the user's instructions when they ask for something else. Write the final rules into `AGENTS.md`, including this update rule by default: before each work session ends, update current progress with what changed, what it was based on, what is still missing, and what comes next, and archive old entries according to the retention rule.

**Only when the user explicitly asks.** Include the following in the list only if the user explicitly asks for them:
- Changing anything in `CLAUDE.md` other than the line that imports `AGENTS.md`
- Initializing a Git repository
- Changing `.gitignore`

## Step 2: Write the files and hand off

1. In the target workspace, add or extend files according to the confirmed list. Reuse original material and existing project rules. Distinguish planned work, completed work, and verified results.
2. Check that:
   - Every file referenced by navigation links and reading rules actually exists.
   - In Claude Code, `CLAUDE.md` actually imports `AGENTS.md`.
   - The background and the first progress entry are consistent.
   - Every confirmed rule has been written down.

   Archive paths that will only be used later can be written into the rules now without creating them.
3. Tell the user which files were added or extended, which items are still open, and what can be done next. Give a one-line prompt suited to the project for resuming later, e.g. "Follow the project rules and continue with the next step in current progress." Later work follows the project rules: `AGENTS.md`, imported through `CLAUDE.md` in Claude Code.
