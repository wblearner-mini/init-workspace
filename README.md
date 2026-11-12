# init-workspace

一个 Agent 技能：首次为长期项目建立工作文档（项目背景、当前进度、文件导航）和项目级 `AGENTS.md`，让之后换一个聊天、换一个 Agent 也能接着做。

技能分两轮工作：第一轮只读盘点工作区并给出文件清单；你确认清单后，第二轮才写入文件。

> 本 README 只供人阅读，不属于技能指令。技能的行为由 `SKILL.md` 定义。技能正文为英文，运行时会用你的语言和你交流，文档也会按工作区的语言来写。

## 安装

### 方式一：用 `npx skills` 安装（推荐）

[Skills CLI](https://github.com/vercel-labs/skills) 可以直接从 GitHub 安装，并按提示选择要装到哪些 Agent（如 Claude Code、Codex）：

```bash
npx skills add wblearner-mini/init-workspace
```

加上 `-g` 安装到用户级（所有项目可用），加上 `-y` 跳过确认提示：

```bash
npx skills add wblearner-mini/init-workspace -g -y
```

以后更新到最新版本：

```bash
npx skills update
```

### 方式二：手动安装

把整个 `init-workspace` 目录放到你所用工具的技能目录下：

| 工具 | 用户级（所有项目可用） | 项目级（仅当前项目） |
|---|---|---|
| Claude Code | `~/.claude/skills/init-workspace/` | `<项目>/.claude/skills/init-workspace/` |
| Codex | `~/.agents/skills/init-workspace/` | `<项目>/.agents/skills/init-workspace/` |

Codex 的技能发现路径见[官方文档](https://learn.chatgpt.com/docs/build-skills#where-codex-loads-local-skills)。

例如安装到 Claude Code 的用户级目录：

```bash
git clone https://github.com/wblearner-mini/init-workspace.git ~/.claude/skills/init-workspace
```

## 使用

- 直接用日常语言描述，例如「帮我整理这个工作区，方便以后接着做」。
- 也可以显式调用：Claude Code 中输入 `/init-workspace`，Codex 中输入 `$init-workspace`。

只需要生成代码库说明时，使用 Claude Code 自带的 `/init` 即可，不必使用本技能。

## 第一轮文件清单示例

以 [我的旅游的公开仓库](https://github.com/wblearner-mini/my-travel/tree/23b6b75) 为例。盘点时已有根目录 README 和服务端说明，分别介绍 App、目录结构和后端运行方式。假如接下来要在 Codex 和支持直接读取 `AGENTS.md` 的 Claude Code 中继续维护这个公开仓库，第一轮可以提出这份清单：

| 文件 | 处理方式 | 用途 |
|---|---|---|
| `README.md` | 复用 | 沿用已有的 App、演示和构建入口 |
| `server/README.md` | 复用 | 沿用后端启动、账号创建和测试说明 |
| `项目背景.md` | 新建 | 记录个人旅行 App 的用途、公开版范围和已确认决定 |
| `当前进度.md` | 新建 | 记录公开版现状、验证依据和下一步 |
| `AGENTS.md` | 新建 | 指向背景和进度，约定何时验证与更新 |

确认清单后才新建文件。这份清单取材自公开仓库的一次只读盘点。

## 为什么要保留这些文档

### 长期项目里，大模型容易丢信息

一个项目做上几周、几个月，信息往往只存在于聊天记录里，而聊天记录很不可靠：

- **新聊天从零开始**。上一次定下的目标、范围、做到哪一步、为什么这样做，新会话都不知道，只能重新解释一遍，或者让模型自己猜。
- **长会话会被压缩或截断**。上下文窗口装满后，最早的内容最先被总结或丢弃。偏偏早期定下的约束、口径和关键决定最重要。
- **事实、决定和猜测混在一起**。模型的推测、用户拍板的决定和已经核实的事实写在同一段对话里，过几轮就分不清哪些可信、哪些还没确认。
- **找不到当前版本**。资料和草稿一多，新会话不知道哪份是正式版本，可能会基于旧稿、旧数据继续干活。

init-workspace 把这些信息从聊天记录搬进项目文件：

| 文件 | 保存什么 |
|---|---|
| 项目背景 | 目标、范围、当前阶段，已确定和待定的事项，并标明每条是已核实事实、用户决定还是助手建议 |
| 当前进度 | 每次工作会话一条记录：改了什么、依据是什么、还缺什么、下一步做什么 |
| 文件导航 | 资料在哪里、哪份是当前版本 |
| `AGENTS.md` | 开工前先读什么、结论需要什么依据、怎么验证、收工前怎么更新文档 |

这样一来，不管隔多久、在哪个聊天里，只要读完这几份文件就能接上，不依赖任何一个工具的记忆功能。

### 多个 Agent 之间怎么串联

这套文档本身就是 Agent 之间的交接协议：

- **同一个入口**。Codex 读取项目的 `AGENTS.md`。Claude Code v2.1.277 起，在默认设置下，如果当前工作目录及其上级没有 `CLAUDE.md`、`.claude/CLAUDE.md` 或 `CLAUDE.local.md`，也会直接读取 `AGENTS.md`。如果已有同目录的 `CLAUDE.md`，可以在其中用 `@AGENTS.md` 导入共享规则。需要兼容旧版时，也可以通过这行导入。详见 [Claude Code 项目指令文档](https://code.claude.com/docs/en/memory#agentsmd)。
- **接力的方式**。规则里规定每个 Agent 开工先读背景和进度，收工前在进度最上面加一条记录。下一个 Agent 从上一条记录的"下一步"接着做。
- **可以追溯**。每条记录都写明依据，并区分事实、决定和建议。接手的 Agent 能判断哪些可以直接用、哪些需要再核实，不会把上一个 Agent 的猜测当成定论。
- **篇幅受控**。当前进度只保留最近 5 条，旧记录移到历史文件。交接文档不会越写越长，也就不会因为太长而在新会话里被截断。

一个典型的接力过程：

1. 在 Claude Code 里运行 `/init-workspace`，确认清单后生成背景、进度和 `AGENTS.md`，按目录现状复用或新建导航。
2. 换到 Codex 开发一个功能。Codex 读取 `AGENTS.md`，按规则先看背景和进度，完成后在进度里记一条。
3. 第二天在 Claude Code 里开一个新会话做验证。它直接读取 `AGENTS.md` 或通过 `CLAUDE.md` 的导入读到同一份规则，从进度里的"下一步"直接开始，不需要你重新交代。

## 目录结构

```
init-workspace/
├── SKILL.md                  # 技能主体
├── README.md                 # 本说明
├── LICENSE                   # MIT 许可证
└── references/
    ├── scenarios.md          # 不同目录现状和项目用途的处理示例
    └── templates.md          # 默认文件名和文档骨架
```

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

## 许可证

[MIT](LICENSE)
