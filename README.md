# init-workspace

一个 Agent 技能：首次为长期项目建立工作文档（项目背景、当前进度、文件导航）和项目级 `AGENTS.md`，让之后换一个聊天也能接着做。

技能分两轮工作：第一轮只读盘点工作区并给出文件清单；你确认清单后，第二轮才写入文件。

> 本 README 只供人阅读，不属于技能指令。技能的行为由 `SKILL.md` 定义。

## 目录结构

```
init-workspace/
├── SKILL.md                  # 技能主体
├── README.md                 # 本说明
└── references/
    ├── scenarios.md          # 不同目录现状和项目用途的处理示例
    └── templates.md          # 默认文件名和文档骨架
```

## 安装

把整个 `init-workspace` 目录放到你所用工具的技能目录下：

| 工具 | 用户级（所有项目可用） | 项目级（仅当前项目） |
|---|---|---|
| Claude Code | `~/.claude/skills/init-workspace/` | `<项目>/.claude/skills/init-workspace/` |
| Codex | `~/.codex/skills/init-workspace/` | 以 Codex 文档为准 |

## 使用

- 直接用日常语言描述，例如「帮我整理这个工作区，方便以后接着做」。
- 也可以显式调用：Claude Code 中输入 `/init-workspace`，Codex 中输入 `$init-workspace`。

在 Claude Code 中，技能会提议用 `CLAUDE.md` 中的一行 `@AGENTS.md` 引入项目规则，因为 Claude Code 启动时只自动读取 `CLAUDE.md`。

只需要生成代码库说明时，使用 Claude Code 自带的 `/init` 即可，不必使用本技能。

## 可选：个人偏好文件

如果你想固定自己的默认语言或文件名，可以自行创建 `~/.agents/init-workspace-preferences.md`。技能运行时会读取它；不存在时直接跳过，不影响使用。

偏好的优先级最低，只在以下几项都没有规定时生效：你在当次对话中的要求、项目已有的规则、工作区现有的语言和命名习惯。

示例：

```markdown
# init-workspace 个人偏好

## 语言
- 默认使用简体中文交流。
- 新建工作区的文档默认使用简体中文，已有工作区沿用其现有语言。

## 命名
- 新建文档时优先使用 `项目背景.md`、`当前进度.md` 和 `文件导航.md`。
- 归档目录使用 `历史归档/进度历史.md`。
```
