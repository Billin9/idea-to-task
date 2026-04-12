---
phase: 02-example-calibration
verified: 2026-04-13T01:32:00Z
status: passed
score: 4/4
overrides_applied: 0
---

# Phase 2: 示例校准 Verification Report

**Phase Goal:** examples.md 包含正反对比案例，模型能直接参照期望行为而不是仅靠规则推理
**Verified:** 2026-04-13T01:32:00Z
**Status:** passed
**Re-verification:** No -- initial verification

## Goal Achievement

### Observable Truths

| # | Truth | Status | Evidence |
|---|-------|--------|----------|
| 1 | examples.md 中存在案例 7，包含同一输入的错误示例（平铺）和正确示例（归纳）两段对比 | VERIFIED | `grep -c "^## 案例"` = 7; 案例 7 包含 `### ❌ 错误示例（平铺）` 和 `### ✅ 正确示例（归纳）` 各 1 处 |
| 2 | 正确示例的核心判断第一句是顶层意图格式 | VERIFIED | 第 69 行: `CEO 真正在推动的是：产品 X 下季度上线。原始拆出的技术实现、运营策略、市场传播三条线均服务于这一顶层目标，归纳为单主题。` |
| 3 | 案例 2 的处理方式中体现了向上归纳检查步骤，但不使用内部术语 | VERIFIED | 第 11 行含「向上归纳检查」; `grep -c "静默回退"` = 0，全文无内部术语泄露 |
| 4 | 案例 7 检查点包含「不触发战略型模板」边界约束 | VERIFIED | 第 86 行: `不应出现「总体方案设计」作为独立主题——归纳型与战略型是不同路径` |

**Score:** 4/4 truths verified

### Required Artifacts

| Artifact | Expected | Status | Details |
|----------|----------|--------|---------|
| `skills/idea-to-task/references/examples.md` | 正反对比案例 + 案例 2 修复 | VERIFIED | 文件存在，88 行，包含 7 个案例，案例 7 完整含错误/正确对比 + 5 条检查点 |

### Key Link Verification

| From | To | Via | Status | Details |
|------|-----|-----|--------|---------|
| examples.md 案例 7 正确示例 | output-template.md 归纳型模板 | 核心判断格式、主题拆分标记、任务树结构一致 | WIRED | 正确示例使用 `CEO 真正在推动的是：` 格式（对应模板第 1 节）; `单主题（归纳）` 标记（对应模板第 2 节）; `### 主题：产品 X 上线` + `*由...归纳而来。*` 结构（对应模板第 3 节归纳型模板） |
| examples.md 案例 2 | decision-rules.md 第 3 节 | 归纳检查流程描述一致，不暴露内部术语 | WIRED | 案例 2 写「先拆主题，再做向上归纳检查；因各方向不服务同一目标，按多主题分别输出」，与 decision-rules.md 第 3 节流程一致但避开了「静默回退」术语 |

### Data-Flow Trace (Level 4)

N/A -- 本阶段为 Markdown 内容编辑，无动态数据渲染。

### Behavioral Spot-Checks

Step 7b: SKIPPED (no runnable entry points -- this is a prompt-engineering content phase)

### Requirements Coverage

| Requirement | Source Plan | Description | Status | Evidence |
|-------------|------------|-------------|--------|----------|
| EX-01 | 02-01-PLAN | 补充正反对比案例 -- 同一输入分别展示「平铺输出」（错误）和「归纳输出」（正确），让模型对齐期望行为 | SATISFIED | 案例 7 使用 fixture 04 输入，错误示例展示三主题平铺，正确示例展示归纳为单顶层主题，含 5 条检查点 |

### Anti-Patterns Found

| File | Line | Pattern | Severity | Impact |
|------|------|---------|----------|--------|
| (none) | -- | -- | -- | 无 anti-pattern 检出 |

### Human Verification Required

(none -- all must-haves can be verified programmatically for this content-only phase)

### Gaps Summary

No gaps found. All 4 must-haves verified, both key links confirmed wired, requirement EX-01 satisfied. Phase goal achieved.

---

_Verified: 2026-04-13T01:32:00Z_
_Verifier: Claude (gsd-verifier)_
