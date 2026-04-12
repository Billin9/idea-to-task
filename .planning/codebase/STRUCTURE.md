# Codebase Structure

**Analysis Date:** 2026-04-12

## Directory Layout

```
idea-to-task/
├── skills/                        # 自研 AI skills（项目核心）
│   └── idea-to-task/              # idea-to-task skill 包
│       ├── SKILL.md               # Skill 入口：完整行为规范
│       ├── agents/                # 平台 UI 元数据
│       │   └── openai.yaml        # OpenAI 平台展示配置
│       ├── references/            # 按需加载的补充文档
│       │   ├── decision-rules.md  # 分流与风险判断规则
│       │   ├── output-template.md # 标准输出模板
│       │   └── examples.md        # 边界案例示例
│       └── scripts/               # 验证工具
│           └── validate_skill.py  # Skill 结构校验脚本
│
├── tests/                         # 测试资产
│   └── fixtures/
│       └── idea-to-task/          # Skill 行为 fixtures
│           ├── 01-clear-direction.md
│           ├── 02-mixed-topics.md
│           └── 03-high-risk-ambiguity.md
│
├── docs/                          # 项目文档
│   └── superpowers/
│       ├── plans/                 # 规划文档
│       │   └── 2026-04-11-idea-to-task.md
│       └── specs/                 # 设计规格文档
│           └── 2026-04-11-idea-to-task-design.md
│
├── .agent/                        # 通用 agent 运行时（GSD 框架 v1.34.2）
│   ├── get-shit-done/             # GSD 框架核心
│   │   ├── bin/                   # JavaScript CLI 工具
│   │   │   ├── gsd-tools.cjs      # 主入口：状态/上下文/配置管理
│   │   │   └── lib/               # 模块库（core, phase, milestone, roadmap 等）
│   │   ├── workflows/             # 68 个 orchestrator 工作流 prompt
│   │   ├── agents/                # 不含（通用 runtime 无 agents 子目录）
│   │   ├── references/            # 共享知识文档（~37 个文件）
│   │   ├── templates/             # 项目脚手架模板
│   │   │   ├── codebase/          # 代码类项目模板（STACK, ARCH 等）
│   │   │   └── research-project/  # 研究类项目模板
│   │   ├── contexts/              # Agent 上下文预设（dev, research, review）
│   │   └── VERSION                # GSD 版本号（当前：1.34.2）
│   ├── agents/                    # 24 个 subagent 定义（.md 系统 prompt）
│   │   ├── gsd-executor.md
│   │   ├── gsd-planner.md
│   │   ├── gsd-codebase-mapper.md
│   │   └── ...（共 24 个）
│   ├── hooks/                     # Agent 生命周期钩子
│   └── skills/                    # GSD 命令的 SKILL.md 分发层（每个 gsd-* 命令一个）
│
├── .claude/                       # Claude Code 专用运行时（GSD 框架镜像）
│   ├── get-shit-done/             # 与 .agent/get-shit-done/ 结构相同
│   ├── agents/                    # Claude Code subagent 定义（24 个）
│   ├── commands/
│   │   └── gsd/                   # Claude Code 斜杠命令（每命令一个 .md）
│   │       ├── execute-phase.md
│   │       ├── plan-phase.md
│   │       ├── map-codebase.md
│   │       └── ...（共 ~68 个）
│   └── hooks/                     # Claude Code 钩子
│
├── .codex/                        # Codex 专用运行时（GSD 框架镜像）
│   ├── get-shit-done/             # 与 .agent/get-shit-done/ 结构相同
│   ├── agents/                    # Codex subagent 定义（无此目录，skills 替代）
│   └── skills/                    # Codex 命令分发层
│
├── .planning/                     # GSD 项目规划状态（由 GSD 命令生成）
│   └── codebase/                  # Codebase 分析文档
│       ├── STACK.md
│       ├── ARCHITECTURE.md        # 本文件
│       └── STRUCTURE.md
│
└── .gitignore                     # 忽略 __pycache__/, *.pyc, .pytest_cache/, .DS_Store
```

## Directory Purposes

**`skills/`:**
- Purpose: 存放自研 AI skills，每个子目录是一个独立的 skill 包
- Contains: SKILL.md、platform 元数据、参考文档、验证脚本
- Key files: `skills/idea-to-task/SKILL.md`

**`skills/<name>/references/`:**
- Purpose: 存放 skill 按需加载的补充知识文档，在 SKILL.md 中以相对路径引用
- Contains: 决策规则、输出模板、示例案例
- Key files: `skills/idea-to-task/references/decision-rules.md`, `skills/idea-to-task/references/output-template.md`

**`skills/<name>/agents/`:**
- Purpose: 存放平台 UI 集成配置（非 GSD subagent 定义）
- Contains: `openai.yaml` — OpenAI 平台的展示名称、简介、默认 prompt

**`skills/<name>/scripts/`:**
- Purpose: 存放 skill 结构校验工具
- Contains: `validate_skill.py` — 使用 `uv run` 执行，校验 frontmatter 和必需章节

**`tests/fixtures/<skill-name>/`:**
- Purpose: 存放 skill 行为测试 fixtures，供 `validate_skill.py --strict` 校验和人工评估
- Contains: 按序号命名的 `.md` 文件，格式为 `## 输入` + `## 期望行为`
- Key files: `tests/fixtures/idea-to-task/01-clear-direction.md`

**`docs/superpowers/`:**
- Purpose: 项目规划和设计规格文档存档
- Contains: `plans/`（推进计划）和 `specs/`（设计规格）按日期命名的 Markdown

**`.agent/get-shit-done/bin/lib/`:**
- Purpose: GSD 工具链的模块化 JavaScript 库
- Contains: `core.cjs`, `state.cjs`, `phase.cjs`, `milestone.cjs`, `roadmap.cjs`, `template.cjs`, `config.cjs`, `intel.cjs`, `verify.cjs`, `workstream.cjs` 等
- Key files: `.agent/get-shit-done/bin/gsd-tools.cjs`（主入口，所有 workflow 通过它获取上下文）

**`.agent/get-shit-done/workflows/`:**
- Purpose: 68 个 orchestrator 工作流 prompt，每个对应一个 GSD 命令的完整执行逻辑
- Contains: `execute-phase.md`, `plan-phase.md`, `map-codebase.md` 等
- Key files: `execute-phase.md`, `plan-phase.md`

**`.agent/agents/`:**
- Purpose: 24 个专用 subagent 的系统 prompt 定义，由 orchestrator 通过 `Task(subagent_type=...)` 调用
- Contains: `gsd-executor.md`, `gsd-planner.md`, `gsd-verifier.md`, `gsd-codebase-mapper.md` 等
- Key files: `gsd-executor.md`, `gsd-planner.md`

**`.claude/commands/gsd/`:**
- Purpose: Claude Code 专用命令分发，每个文件对应一个用户可调用的 `/gsd-*` 斜杠命令
- Contains: 约 68 个 `.md` 文件，加载并执行对应的 workflow

**`.planning/codebase/`:**
- Purpose: 由 `/gsd-map-codebase` 生成的 codebase 分析文档，供其他 GSD 命令（plan-phase, execute-phase）加载
- Generated: Yes（由 `gsd-codebase-mapper` subagent 写入）
- Committed: Yes

## Key File Locations

**Entry Points:**
- `skills/idea-to-task/SKILL.md`: Skill 入口，LLM 运行时加载的主系统 prompt
- `skills/idea-to-task/agents/openai.yaml`: OpenAI 平台 UI 元数据
- `.claude/commands/gsd/execute-phase.md`: Claude Code `/gsd-execute-phase` 命令入口
- `.claude/commands/gsd/plan-phase.md`: Claude Code `/gsd-plan-phase` 命令入口

**Configuration:**
- `.agent/get-shit-done/VERSION`: GSD 框架版本（当前 1.34.2）
- `.gitignore`: 忽略 Python 缓存、`.DS_Store`

**Core Logic:**
- `.agent/get-shit-done/bin/gsd-tools.cjs`: 所有状态/上下文/配置操作的 JavaScript 入口
- `.agent/get-shit-done/bin/lib/core.cjs`: 核心工具函数
- `.agent/get-shit-done/bin/lib/phase.cjs`: Phase 生命周期管理
- `skills/idea-to-task/references/decision-rules.md`: Skill 核心判断逻辑

**Testing:**
- `skills/idea-to-task/scripts/validate_skill.py`: Skill 结构校验脚本
- `tests/fixtures/idea-to-task/`: 行为测试 fixtures

## Naming Conventions

**Files:**
- Skill 入口：`SKILL.md`（固定大写）
- References：`kebab-case.md`（如 `decision-rules.md`, `output-template.md`）
- Fixtures：`NN-kebab-case.md`，以两位数字前缀排序（如 `01-clear-direction.md`）
- GSD workflows：`kebab-case.md`（如 `execute-phase.md`）
- GSD agents：`gsd-kebab-case.md`（如 `gsd-executor.md`）
- GSD commands（Claude）：`kebab-case.md`（无 `gsd-` 前缀，如 `execute-phase.md`）
- GSD skill dirs（agent runtime）：`gsd-kebab-case/`（有 `gsd-` 前缀）
- Python scripts：`snake_case.py`（如 `validate_skill.py`）
- Docs：`YYYY-MM-DD-topic.md`（如 `2026-04-11-idea-to-task.md`）

**Directories:**
- Skill 目录：`skills/<skill-name>/`（kebab-case）
- Fixture 目录：`tests/fixtures/<skill-name>/`（与 skill 目录名一致）
- GSD 运行时目录：`.<runtime>/get-shit-done/`（隐藏目录）

## Where to Add New Code

**New Skill:**
- Skill 入口：`skills/<new-skill-name>/SKILL.md`
- Platform 元数据：`skills/<new-skill-name>/agents/openai.yaml`
- 决策规则：`skills/<new-skill-name>/references/decision-rules.md`
- 输出模板：`skills/<new-skill-name>/references/output-template.md`
- 示例：`skills/<new-skill-name>/references/examples.md`
- 校验脚本：`skills/<new-skill-name>/scripts/validate_skill.py`（复用现有脚本）
- Fixtures：`tests/fixtures/<new-skill-name>/01-*.md`（至少 3 个）

**New Reference Document for Existing Skill:**
- Implementation：`skills/<skill-name>/references/<topic>.md`
- 在 `SKILL.md` 中以相对路径 `[text](./references/<topic>.md)` 引用

**Utilities / Scripts:**
- Shared helpers：`skills/<skill-name>/scripts/`（每个 skill 自包含）

**Planning Documents:**
- Specs：`docs/superpowers/specs/YYYY-MM-DD-<topic>.md`
- Plans：`docs/superpowers/plans/YYYY-MM-DD-<topic>.md`

## Special Directories

**`.agent/`, `.claude/`, `.codex/`:**
- Purpose: 三个 AI 运行时（通用、Claude Code、Codex）各自的 GSD 框架安装副本
- Generated: No（版本控制管理）
- Committed: Yes
- 注意：三者 `get-shit-done/` 子目录结构相同，但 agents/commands/skills 分发层有运行时差异

**`.planning/`:**
- Purpose: GSD 命令生成的项目规划状态和分析文档
- Generated: Yes（由 GSD 命令写入）
- Committed: Yes（规划文档需要持久化供后续命令读取）

**`__pycache__/`（.gitignore）:**
- Purpose: Python 字节码缓存
- Generated: Yes
- Committed: No

---

*Structure analysis: 2026-04-12*
