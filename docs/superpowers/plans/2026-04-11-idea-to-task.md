# Idea to Task Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 构建一个本地 skill，把 CEO 的凌乱聊天记录或会议碎片自动整理为分层任务树、执行建议和最小补问结果。

**Architecture:** 在当前工作区创建一个独立 skill 目录，采用“精简 SKILL.md + 按需 references + 本地校验脚本 + smoke fixtures”的结构。SKILL.md 只保留触发条件和核心流程，复杂判定规则、输出模板和案例拆到 references 中，避免主文件过长且难维护。

**Tech Stack:** Markdown、YAML、Python 3.11 + `uv`（PEP 723 单脚本）、Git

---

## 文件结构

### 目标目录与职责

- Create: `skills/idea-to-task/SKILL.md`
- Create: `skills/idea-to-task/references/decision-rules.md`
- Create: `skills/idea-to-task/references/output-template.md`
- Create: `skills/idea-to-task/references/examples.md`
- Create: `skills/idea-to-task/agents/openai.yaml`
- Create: `skills/idea-to-task/scripts/validate_skill.py`
- Create: `tests/fixtures/idea-to-task/01-clear-direction.md`
- Create: `tests/fixtures/idea-to-task/02-mixed-topics.md`
- Create: `tests/fixtures/idea-to-task/03-high-risk-ambiguity.md`
- Create: `.gitignore`

### 职责边界

- `SKILL.md`：触发条件、主工作流、何时读取 references、何时补问、何时停止下钻
- `references/decision-rules.md`：自动分流、证据强度、风险边界、补问规则
- `references/output-template.md`：固定的 6 段式输出模板和字段说明
- `references/examples.md`：最小案例，帮助实现者校准输出风格
- `agents/openai.yaml`：UI 元数据与默认调用提示
- `scripts/validate_skill.py`：本地结构校验脚本，确保 skill 结构完整
- `tests/fixtures/*`：人工 smoke test 场景与期望行为

### 实施顺序

1. 先搭建工作区和校验脚本
2. 再写 `SKILL.md`
3. 再补 references 和 UI 元数据
4. 最后补 fixtures，做人工 smoke test

### Task 1: 初始化工作区与校验脚本

**Files:**
- Create: `.gitignore`
- Create: `skills/idea-to-task/scripts/validate_skill.py`

- [ ] **Step 1: 初始化 git 仓库并创建目录**

Run:

```bash
git init
mkdir -p skills/idea-to-task/{scripts,references,agents} tests/fixtures/idea-to-task
```

Expected:

```text
Initialized empty Git repository in .../renwu/.git/
```

- [ ] **Step 2: 写入 `.gitignore`**

```gitignore
__pycache__/
*.pyc
.pytest_cache/
.DS_Store
```

- [ ] **Step 3: 编写校验脚本**

```python
#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml<7"]
# ///
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

import yaml

REQUIRED_SECTIONS = [
    "## 适用场景",
    "## 核心原则",
    "## 工作流",
    "## 补问规则",
    "## 输出结构",
]


def read_frontmatter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md 缺少合法的 YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter 必须是字典")
    return data


def extract_reference_paths(text: str) -> list[str]:
    paths = []
    for raw_path in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if raw_path.startswith("http://") or raw_path.startswith("https://"):
            continue
        if raw_path.startswith("#"):
            continue
        paths.append(raw_path)
    return paths


def validate_skill(skill_dir: Path, strict: bool) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["SKILL.md 不存在"]

    text = skill_md.read_text(encoding="utf-8")

    try:
        frontmatter = read_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not isinstance(name, str) or not name.strip():
        errors.append("frontmatter.name 缺失或为空")
    if not isinstance(description, str) or not description.strip():
        errors.append("frontmatter.description 缺失或为空")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"缺少必需章节：{section}")

    for rel_path in extract_reference_paths(text):
        target = (skill_dir / rel_path).resolve()
        if not target.exists():
            errors.append(f"引用文件不存在：{rel_path}")

    if strict:
        openai_yaml = skill_dir / "agents" / "openai.yaml"
        if not openai_yaml.exists():
            errors.append("strict 模式要求 agents/openai.yaml 存在")

        fixtures_dir = skill_dir.parent.parent / "tests" / "fixtures" / skill_dir.name
        if not fixtures_dir.exists():
            errors.append("strict 模式要求存在 tests/fixtures/<skill-name>/")
        else:
            fixture_count = len(list(fixtures_dir.glob("*.md")))
            if fixture_count < 3:
                errors.append("strict 模式要求至少 3 个 markdown fixtures")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="校验本地 skill 结构")
    parser.add_argument("skill_dir", help="skill 目录路径")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="额外校验 UI 元数据和 smoke fixtures",
    )
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    errors = validate_skill(skill_dir, strict=args.strict)
    if errors:
        print("校验失败：")
        for item in errors:
            print(f"- {item}")
        return 1

    print("校验通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
```

- [ ] **Step 4: 运行校验脚本，确认当前会失败**

Run:

```bash
uv run skills/idea-to-task/scripts/validate_skill.py skills/idea-to-task
```

Expected:

```text
校验失败：
- SKILL.md 不存在
```

- [ ] **Step 5: 提交初始化改动**

```bash
git add .gitignore skills/idea-to-task/scripts/validate_skill.py
git commit -m "chore: bootstrap idea-to-task skill workspace"
```

### Task 2: 编写核心 `SKILL.md`

**Files:**
- Create: `skills/idea-to-task/SKILL.md`
- Test: `skills/idea-to-task/scripts/validate_skill.py`

- [ ] **Step 1: 写入核心 skill 文件**

```markdown
---
name: idea-to-task
description: Use when the user wants to turn messy CEO chat fragments, meeting notes, or strategy thoughts into structured themes, task trees, execution suggestions, and minimal follow-up questions.
---

# Idea to Task

把 CEO 的凌乱表达整理成可推进的任务树。目标不是生成会议纪要，而是输出下一步可执行结果。

## 适用场景

- 会议记录、聊天原文、语音转文字、碎片短句
- 多个主题混在一起，需要拆主线和次线
- 需要把模糊方向整理成项目级、里程碑级、执行项级任务
- 需要判断是直接输出结果，还是先补少量关键问题

## 核心原则

- 先给结论，再给结构，最后给动作
- 默认先产出，只有高风险歧义时才补问
- 细化层级不能超过证据强度
- 只提醒真正会影响方向的高风险推断
- 输出重点是任务推进，不是复述原话

## 工作流

1. 识别输入类型：长文本、碎片短句或混合输入
2. 判断主题密度：单主题、多相关主题、多不相关主题
3. 判断可任务化程度：能否直接形成任务树
4. 将原始表达归一为稳定意图
5. 必要时拆主题，再分别生成任务树
6. 输出核心判断、主题拆分、任务树、执行建议、风险提醒、下一步动作

遇到边界不清的输入时：

- 如果只是信息不足，但主方向清楚：先给初版任务树，再补最少量问题
- 如果一句话可以导出两条相反任务路径：明确给出双路径，不偷偷选边
- 如果证据不足以支撑执行项：只输出到项目级或里程碑级

## 补问规则

- 只补会显著改变任务方向的问题
- 问题数量尽量控制在 2 到 5 个
- 如果输入已经足够推进，不要为了“更稳”而过度追问
- 如果多个主题彼此独立，先拆主题再判断是否需要补问

详细判定规则见 [decision-rules.md](./references/decision-rules.md)。

## 输出结构

默认按以下顺序输出：

1. 核心判断
2. 主题拆分
3. 分层任务树
4. 执行建议
5. 风险与高风险推断
6. 下一步动作

具体模板见 [output-template.md](./references/output-template.md)。

## 何时读取参考文件

- 当你需要判断“该直接输出还是该补问”时，读取 [decision-rules.md](./references/decision-rules.md)
- 当你需要稳定输出格式时，读取 [output-template.md](./references/output-template.md)
- 当你需要校准风格或边界时，读取 [examples.md](./references/examples.md)

## 明确禁止

- 不把所有模糊表达都包装成确定结论
- 不把多个无关主题硬拼成同一个项目
- 不在证据不足时伪造细执行项
- 不把输出写成长篇会议纪要
```

- [ ] **Step 2: 运行严格校验，确认它会因缺少引用文件和 UI 元数据而失败**

Run:

```bash
uv run skills/idea-to-task/scripts/validate_skill.py skills/idea-to-task --strict
```

Expected:

```text
校验失败：
- 引用文件不存在：./references/decision-rules.md
- 引用文件不存在：./references/output-template.md
- 引用文件不存在：./references/examples.md
- strict 模式要求 agents/openai.yaml 存在
- strict 模式要求至少 3 个 markdown fixtures
```

- [ ] **Step 3: 提交核心 skill 初稿**

```bash
git add skills/idea-to-task/SKILL.md
git commit -m "feat: add ceo idea orchestrator skill core flow"
```

### Task 3: 补齐 references 与 UI 元数据

**Files:**
- Create: `skills/idea-to-task/references/decision-rules.md`
- Create: `skills/idea-to-task/references/output-template.md`
- Create: `skills/idea-to-task/references/examples.md`
- Create: `skills/idea-to-task/agents/openai.yaml`
- Test: `skills/idea-to-task/scripts/validate_skill.py`

- [ ] **Step 1: 写入判定规则参考文件**

```markdown
# 自动分流与风险边界

## 1. 主题密度判断

- 单主题：整段内容围绕一个明确方向，直接进入任务化
- 多相关主题：先拆分主线和次线，再分别输出
- 多不相关主题：禁止强行汇总成一个总项目

## 2. 可任务化程度

满足以下至少两项时，可直接给初版任务树：

- 能看出在做什么
- 能看出为什么做
- 能看出大致面向谁
- 能判断是方向判断还是执行动作

## 3. 何时补问

只有当补问会显著改变任务方向时才补问，例如：

- 同一句话可能导出两条相反动作路径
- 是否投入会直接影响资源配置
- 当前表达只能支持口号，不能支持任务

## 4. 证据强度与下钻深度

- 证据弱：只输出项目级
- 证据中等：可输出到里程碑级
- 证据强：才允许输出执行项级

## 5. 高风险歧义

出现以下场景时，优先双路径输出：

- “先做高端还是先做大众”
- “先做平台还是先做单点功能”
- “现在投入还是继续观察”
```

- [ ] **Step 2: 写入输出模板参考文件**

```markdown
# 标准输出模板

## 1. 核心判断

用 3 到 6 句话回答：

- CEO 真正在推动什么
- 主线是什么
- 次线是什么
- 当前更偏战略、产品还是执行

## 2. 主题拆分

如果输入包含多个方向，先按主题拆开。

## 3. 分层任务树

按主题输出：

- 项目级
- 里程碑级
- 执行项级

## 4. 执行建议

至少包含：

- 优先级
- 建议负责人角色
- 推荐推进顺序

## 5. 风险与高风险推断

只提醒真正会改变任务方向的推断。

## 6. 下一步动作

固定给出 3 到 5 条最值得先推进的动作。
```

- [ ] **Step 3: 写入案例参考文件**

```markdown
# 示例案例

## 案例 1：输入清楚

输入已经表达了方向、目标用户和预期动作。
处理方式：直接给完整任务树，不补问。

## 案例 2：输入混杂

输入同时提到产品 AI 化、组织提效和商业化。
处理方式：先拆主题，再分别给任务树，可附 1 到 3 个关键问题。

## 案例 3：高风险歧义

输入在两个相反方向之间摇摆。
处理方式：双路径输出，并明确标注风险点。
```

- [ ] **Step 4: 写入 `agents/openai.yaml`**

```yaml
interface:
  display_name: "Idea to Task"
  short_description: "Turn messy CEO notes into task trees and action advice"
  default_prompt: "Use $idea-to-task to turn these CEO notes into structured tasks, risks, and next steps."
```

- [ ] **Step 5: 运行严格校验，确认只剩 fixtures 缺失**

Run:

```bash
uv run skills/idea-to-task/scripts/validate_skill.py skills/idea-to-task --strict
```

Expected:

```text
校验失败：
- strict 模式要求至少 3 个 markdown fixtures
```

- [ ] **Step 6: 提交 references 与 UI 元数据**

```bash
git add skills/idea-to-task/references skills/idea-to-task/agents/openai.yaml
git commit -m "feat: add idea-to-task skill references and ui metadata"
```

### Task 4: 创建 smoke fixtures 并完成结构校验

**Files:**
- Create: `tests/fixtures/idea-to-task/01-clear-direction.md`
- Create: `tests/fixtures/idea-to-task/02-mixed-topics.md`
- Create: `tests/fixtures/idea-to-task/03-high-risk-ambiguity.md`
- Test: `skills/idea-to-task/scripts/validate_skill.py`

- [ ] **Step 1: 创建“方向清晰”场景**

```markdown
# 场景 1：方向清晰

## 输入

CEO 说：我们今年要把销售跟进流程 AI 化，先别做大而全平台，先聚焦销售团队每天最耗时的客户整理和跟进提醒。目标是两周内拿出一个能试用的原型，看看一线销售愿不愿意用。

## 期望行为

- 不补问，直接输出
- 明确主线是“销售跟进 AI 化”
- 给出项目级、里程碑级、执行项级任务
- 建议角色至少覆盖产品、研发、销售运营
```

- [ ] **Step 2: 创建“多主题混杂”场景**

```markdown
# 场景 2：多主题混杂

## 输入

CEO 说：产品以后肯定要 AI 化，这条线得盯着。还有，我们最近会议太多、效率太低，内部协作得提效。另一个是商业化，不能一直只讲愿景，看看能不能先找几个愿意付费的试点客户。别三个一起硬上，但你们先帮我理一理。

## 期望行为

- 先拆成至少三个主题
- 可以给初版任务树
- 如果补问，问题数控制在 1 到 3 个
- 不把组织提效和商业化混成同一个项目
```

- [ ] **Step 3: 创建“高风险歧义”场景**

```markdown
# 场景 3：高风险歧义

## 输入

CEO 说：我们是不是应该先做高端客户？但我又担心高端客户销售周期太长，会不会反而应该先做中小客户，把模型跑起来再说。这个方向你先帮我拆一拆。

## 期望行为

- 显式给出两条可能路径
- 标记这是高风险歧义
- 两条路径都要有任务方向
- 不默认替 CEO 选边站
```

- [ ] **Step 4: 运行严格校验，确认结构完整**

Run:

```bash
uv run skills/idea-to-task/scripts/validate_skill.py skills/idea-to-task --strict
```

Expected:

```text
校验通过
```

- [ ] **Step 5: 提交 fixtures 与结构校验通过状态**

```bash
git add tests/fixtures/idea-to-task
git commit -m "test: add idea-to-task skill smoke fixtures"
```

### Task 5: 进行人工 smoke test 并收口文案

**Files:**
- Modify: `skills/idea-to-task/SKILL.md`
- Modify: `skills/idea-to-task/references/decision-rules.md`
- Modify: `skills/idea-to-task/references/output-template.md`
- Modify: `skills/idea-to-task/references/examples.md`
- Test: `tests/fixtures/idea-to-task/01-clear-direction.md`
- Test: `tests/fixtures/idea-to-task/02-mixed-topics.md`
- Test: `tests/fixtures/idea-to-task/03-high-risk-ambiguity.md`

- [ ] **Step 1: 用场景 1 做人工 smoke test**

在 Codex 新对话中粘贴以下提示：

```text
[$idea-to-task](/Users/Bai/Downloads/同步空间/works/Code/renwu/skills/idea-to-task/SKILL.md)

请按 skill 规则整理以下内容：

CEO 说：我们今年要把销售跟进流程 AI 化，先别做大而全平台，先聚焦销售团队每天最耗时的客户整理和跟进提醒。目标是两周内拿出一个能试用的原型，看看一线销售愿不愿意用。
```

Expected:

```text
- 直接输出 6 段式结果
- 不补问
- 有完整三层任务树
```

- [ ] **Step 2: 用场景 2 做人工 smoke test**

在 Codex 新对话中粘贴以下提示：

```text
[$idea-to-task](/Users/Bai/Downloads/同步空间/works/Code/renwu/skills/idea-to-task/SKILL.md)

请按 skill 规则整理以下内容：

CEO 说：产品以后肯定要 AI 化，这条线得盯着。还有，我们最近会议太多、效率太低，内部协作得提效。另一个是商业化，不能一直只讲愿景，看看能不能先找几个愿意付费的试点客户。别三个一起硬上，但你们先帮我理一理。
```

Expected:

```text
- 先拆主题
- 不会把三个方向混成一个项目
- 如果补问，数量不超过 3 个
```

- [ ] **Step 3: 用场景 3 做人工 smoke test**

在 Codex 新对话中粘贴以下提示：

```text
[$idea-to-task](/Users/Bai/Downloads/同步空间/works/Code/renwu/skills/idea-to-task/SKILL.md)

请按 skill 规则整理以下内容：

CEO 说：我们是不是应该先做高端客户？但我又担心高端客户销售周期太长，会不会反而应该先做中小客户，把模型跑起来再说。这个方向你先帮我拆一拆。
```

Expected:

```text
- 双路径输出
- 明确高风险歧义
- 不默认替 CEO 选方向
```

- [ ] **Step 4: 如果 smoke test 暴露问题，最小化修改文案**

优先修改这些位置：

```text
1. skills/idea-to-task/SKILL.md
2. skills/idea-to-task/references/decision-rules.md
3. skills/idea-to-task/references/output-template.md
```

改动原则：

```text
- 先改触发条件，再改判定规则，最后改输出模板
- 不新增长期记忆、自动接入项目管理工具等超范围能力
- 保持 SKILL.md 精简，把详细规则留在 references
```

- [ ] **Step 5: 再次运行严格校验**

Run:

```bash
uv run skills/idea-to-task/scripts/validate_skill.py skills/idea-to-task --strict
```

Expected:

```text
校验通过
```

- [ ] **Step 6: 提交最终收口改动**

```bash
git add skills/idea-to-task tests/fixtures/idea-to-task
git commit -m "feat: finalize ceo idea task orchestrator skill"
```

## 覆盖检查

- spec 中的“任务清单优先”由 `SKILL.md` 的输出目标和 6 段式模板覆盖
- spec 中的“自动判断直接输出还是补问”由 `decision-rules.md` 的自动分流规则覆盖
- spec 中的“三层任务树”由 `output-template.md` 和 smoke 场景 1 覆盖
- spec 中的“多主题拆分”由 smoke 场景 2 覆盖
- spec 中的“高风险歧义双路径”由 smoke 场景 3 覆盖
- spec 中的“第一版不做长期记忆”由 Task 5 的改动原则显式约束

## 占位词检查

本计划没有使用以下失败模式：

- 没有 `TODO` / `TBD`
- 没有“后续补充适当错误处理”这类空话
- 没有“参考上一任务自行处理”这类跳步表述
- 所有代码或文件步骤都给了具体内容
