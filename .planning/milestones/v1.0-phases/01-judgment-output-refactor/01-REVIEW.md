---
phase: 01-judgment-output-refactor
reviewed: 2026-04-13T00:21:00+08:00
depth: standard
files_reviewed: 5
files_reviewed_list:
  - skills/idea-to-task/SKILL.md
  - skills/idea-to-task/references/decision-rules.md
  - skills/idea-to-task/references/output-template.md
  - tests/fixtures/idea-to-task/04-induction-success.md
  - tests/fixtures/idea-to-task/05-induction-failure.md
findings:
  critical: 0
  warning: 3
  info: 1
  total: 4
status: issues_found
---

# Phase 01: Code Review Report

**Reviewed:** 2026-04-13T00:21:00+08:00
**Depth:** standard
**Files Reviewed:** 5
**Status:** issues_found

## Summary

本次审查覆盖 idea-to-task skill 的核心定义文件（SKILL.md）、两个参考文档（decision-rules.md、output-template.md）以及两个新增的测试 fixture（04、05）。整体结构清晰，向上归纳逻辑在 SKILL.md 和 decision-rules.md 之间保持了一致。主要问题集中在三个方面：归纳型模板中"绝大多数"主题可归纳时剩余主题的处理未定义、归纳型模板的执行项层级结构与常规模板不一致、examples.md 案例 2 与新增的向上归纳检查逻辑存在描述冲突。

## Warnings

### WR-01: 归纳检查"绝大多数"场景下剩余主题处理未定义

**File:** `skills/idea-to-task/references/decision-rules.md:55`
**Issue:** 第 3 节步骤 2 写道"如果存在一个目标能覆盖全部（或绝大多数）主题"即归纳成功。但当只有"绝大多数"主题可归纳时，剩余的少数独立主题应如何处理（独立输出？附录？忽略？）没有任何规则说明。这会导致 LLM 在该边界场景下行为不确定——可能丢弃剩余主题，也可能强行塞入归纳后的主题树中。
**Fix:** 在 decision-rules.md 第 3 节步骤 2 中补充剩余主题的处理规则，例如：

```markdown
2. 如果存在一个目标能覆盖全部（或绝大多数）主题，则归纳成功：
   - 将该目标作为唯一顶层主题
   - 原来的各主题降级为该顶层主题下的里程碑或子任务线
   - 无法归入顶层目标的少数主题，作为独立主题单独输出（放在归纳主题之后）
   - 输出时走归纳型模板（见 output-template.md 第 2 节）
```

同时在 output-template.md 的归纳型模板末尾补充对独立剩余主题的输出位置说明。

### WR-02: 归纳型模板"具体执行项"层级结构不一致

**File:** `skills/idea-to-task/references/output-template.md:75-78`
**Issue:** 归纳型模板中，"具体执行项"与各里程碑平级放置，内容是"明确第一阶段聚焦的里程碑"和"输出整体推进节奏"——这些是元规划动作，不是某个里程碑下的具体执行项。而在常规模板和战略型模板中，执行项是嵌套在里程碑之下的。这种结构不一致会让 LLM 产生混淆：归纳型输出中的执行项到底应该挂在哪个里程碑下？
**Fix:** 将归纳型模板的执行项改为顶层规划动作，或明确其归属：

```markdown
### 主题：[顶层意图名称]
*由 [原主题A]、[原主题B]、[原主题C] 归纳而来。*

- **里程碑 1：[原主题A 方向]**
  - [ ] [执行项]
  - [ ] [执行项]
- **里程碑 2：[原主题B 方向]**
  - [ ] [执行项]
- **里程碑 3：[原主题C 方向]**
  - [ ] [执行项]
- **启动规划**
  - 明确第一阶段聚焦的里程碑
  - 输出整体推进节奏
```

或者将这两条移到"下一步动作"中，因为它们本质上就是下一步动作。

### WR-03: examples.md 案例 2 与向上归纳检查逻辑冲突

**File:** `skills/idea-to-task/references/examples.md:9-11`
**Issue:** 案例 2 描述的场景是"输入同时提到产品 AI 化、组织提效和商业化"，处理方式写的是"先拆主题，再分别给任务树"。但这个场景与 fixture 05（05-induction-failure.md）几乎完全相同，fixture 05 的期望行为明确要求"不应把三个主题强行归纳为一个顶层意图"。问题在于 examples.md 案例 2 完全没有提及向上归纳检查这一步骤——按新增的 decision-rules.md 第 3 节，所有多主题输入都必须先经过向上归纳检查，即使最终归纳失败。案例 2 的描述跳过了这一步，可能误导 LLM 在类似场景下直接跳过归纳检查。
**Fix:** 更新 examples.md 案例 2 的处理方式描述，补充向上归纳检查步骤：

```markdown
## 案例 2：输入混杂

输入同时提到产品 AI 化、组织提效和商业化。
处理方式：先拆主题，经向上归纳检查确认各主题独立（无法用一个目标覆盖），再分别给任务树，可附 1 到 3 个关键问题。
```

## Info

### IN-01: fixture 04 和 fixture 05 可补充对 examples.md 案例的交叉引用

**File:** `tests/fixtures/idea-to-task/04-induction-success.md:1`
**Issue:** fixture 04（归纳成功）和 fixture 05（归纳失败）是新增的测试场景，但 examples.md 中没有对应的归纳成功案例。案例 2 对应的是归纳失败场景，但缺少一个归纳成功的示例案例来对齐 fixture 04 的行为预期。
**Fix:** 考虑在 examples.md 中补充一个归纳成功的案例（案例 7），场景可直接复用 fixture 04 的输入（产品 X 上线，技术/运营/市场三条线），说明处理方式为向上归纳后走归纳型模板。

---

_Reviewed: 2026-04-13T00:21:00+08:00_
_Reviewer: Claude (gsd-code-reviewer)_
_Depth: standard_
