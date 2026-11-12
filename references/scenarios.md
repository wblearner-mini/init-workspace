# Workspace Scenario Examples

First decide what can be reused based on the current state of the directory, then pick the project scenario that fits best. One project can combine several examples. Use this material to draft the list; the first round stays read-only.

## By the current state of the directory

- **Empty directory.** "This folder is for my graduation thesis from now on. Set it up for me." Based on the goal the user stated, propose background, progress, navigation, and rules. The first progress entry records this initialization and the next step. If the purpose must be clear before you can draft the list, ask only one question.
- **Few files, with an existing README.** "This little tool needs long-term maintenance, and everything is explained in the README." Prefer reusing the README for navigation, and maintain background and progress separately.
- **Existing rules and records.** "This project has its own rules. Fill in the missing working documents." List which existing rules, background, and progress can be reused. Follow current conventions for retention periods or naming. When the material contains two conflicting versions, ask in the list which one should be treated as authoritative from now on.
- **Has a CLAUDE.md, but no AGENTS.md.** "This project has always used Claude Code, and the rules are all in CLAUDE.md." Keep the existing rules in `CLAUDE.md`. Propose an `AGENTS.md` that links to the background and progress and adds any missing handoff rules. Add an import of `AGENTS.md` at the top of `CLAUDE.md`, with a path relative to the importing file. If a proposed rule conflicts with an existing one, ask which to follow.
- **Several projects under one parent directory.** "This folder has several projects in it. Organize all of them." First ask whether the target this time is the parent directory itself or one of the subprojects. When the target is the parent directory, create only an overall navigation document and the rules shared by all projects. Keep each subproject's background and progress in that subproject's own directory, maintained separately, and do not merge them into the parent directory. When a subproject already has its own `AGENTS.md` or `CLAUDE.md`, the parent directory's rules must not conflict with it.

## By the project's purpose

### 1. Academic research and theses

> The school template, literature, and proposal draft are all here. I want to keep pushing my graduation thesis forward.

Keep the original material and the draft's structure, and link the template, literature, and current draft from navigation. When citations need tracking or experiments need to be reproducible, propose a literature index or an experiment log. In `AGENTS.md`, state what evidence conclusions need, such as the location of school documents, literature citations, or existing experiment results. A possible question: "Which requirements are official school rules, and which are your advisor's suggestions?"

### 2. Software development and maintenance

> I've taken over an Android project. It already has a README and build instructions. Help me set up an entry point for future development.

Reuse the README, build instructions, and any existing `AGENTS.md`, and fill in only the missing roles. Draft the verification approach from the existing build and test instructions. When requirements, design, and verification already have material, create links or topic records according to what they are actually used for. A possible question: "Which features need acceptance testing on a specific physical device?"

### 3. Data analysis and recurring reports

> Every month I use these spreadsheets for a business analysis. I want any new chat to know which version of the data to use and how to calculate things.

Link the raw data, existing scripts, and past reports from navigation. When metric definitions, data dates, or output versions need repeated checking, propose a definitions document or a report index. Progress records the inputs used this round, the results verified, and the items still to check. A possible question: "When the summary table and the detail table disagree for the same month, which source wins?"

### 4. Team collaboration and project handover

> I just took over an event project. Meeting notes, task lists, and deliverables are scattered across several directories.

Link the existing task lists, meeting notes, and deliverables. Use the background to explain the project's goals and how the team works together, and use progress to list current blockers and next steps. Propose a decision log only when long-term decisions need to be traceable. A possible question: "Which task list is the one the team officially uses? Who signs off on important decisions?"

### 5. Coursework and exam preparation

> I want to use this folder to prepare for an exam. I already have the syllabus, notes, and a collection of mistakes.

Use the background to record the goal, exam scope, and dates, and link the syllabus, notes, question bank, and mistake collection from navigation. Propose a review plan or a mistake index only when it is truly needed. Progress records what was reviewed recently, evidence of mastery, and the next practice session. A possible question: "Which version of the exam syllabus is authoritative?"

### 6. Job hunting and application management

> There are several versions of my résumé, job postings, and screenshots of applications here. I want to organize my campus recruitment progress.

Reuse the existing application tracker, and link résumé versions, job material, and application receipts from navigation. Progress marks applications as submitted, awaiting confirmation, or next step, based on verifiable records. If an application log needs to be created, state in the list which fields it will record. A possible question: "Which résumé is the current version? Which applications have an email or system receipt?"

### 7. Content creation and video production

> Scripts, footage, and several edit versions are all in this directory, and I'll keep revising them.

The background records the audience, output requirements, and the creative direction already agreed. Navigation links the scripts, raw footage, and current preview. Propose an asset list or a feedback log only when footage sources or version feedback truly need tracking. A possible question: "Which script and preview are current? Who signs off on the final cut?"

### 8. Travel and personal planning

> I have a draft itinerary and a budget, and I want to keep checking routes and bookings later.

Link the original itinerary and budget. The background records dates, the budget ceiling, constraints, and arrangements already settled. Progress distinguishes confirmed items, items to verify, and next steps. Propose a separate record only when bookings truly need tracking. A possible question: "Which items are already booked, and which are only options?"

### 9. Day-to-day operations and process maintenance

> Every week I sort out event sign-ups and do a retrospective. I have spreadsheets and an old process document.

Reuse the existing records, and point navigation to the current process, spreadsheets, and deliverable templates. When the weekly steps need to be fixed, propose a supplementary process document; progress records this round's exceptions and to-dos. A possible question: "Which steps in the old process are still in use? Which spreadsheet is the weekly deliverable based on?"

### 10. Mixed projects

> This project involves building an agent prototype, writing a paper, and giving a demo, and the material and code are all in one place.

Share one set of background, progress, and navigation, and link research material, code documentation, experiment logs, and demo outputs separately. Write verification rules by the purpose of each kind of material: for example, claims in the paper trace back to literature or experiments, code changes are verified according to the test instructions, and demos record a working version. A possible question: "For the next phase, should the prototype, the experiment results, or the demo deck come first?"
