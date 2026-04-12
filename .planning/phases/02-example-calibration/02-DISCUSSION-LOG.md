# Phase 2: 示例校准 - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-04-13
**Phase:** 02-示例校准
**Areas discussed:** 对比案例数量与场景, 对比案例展示格式, 现有案例 2 修复

---

## 对比案例数量与场景

### Q1: 应该加多少组正反对比案例？

| Option | Description | Selected |
|--------|-------------|----------|
| 一组最小满足（推荐） | 只加一组归纳成功场景 | ✓ |
| 两组（成功+失败） | 覆盖归纳成功和失败两个路径 | |
| 三组（成功+失败+战略型） | 额外展示战略型与归纳型的区别 | |

**User's choice:** 一组最小满足

### Q2: 对比案例用什么场景？

| Option | Description | Selected |
|--------|-------------|----------|
| 复用 fixture 04 场景（推荐） | 产品发布场景（技术+运营+团队） | ✓ |
| 用全新场景 | 与现有 fixture 不重复 | |
| Claude 决定 | 让实现时自行选择 | |

**User's choice:** 复用 fixture 04 场景

---

## 对比案例展示格式

### Q3: 正反对比案例用什么格式展示？

| Option | Description | Selected |
|--------|-------------|----------|
| 前后分段对比（推荐） | ❌/✅ 标记，先错误后正确 | ✓ |
| 并列表格对比 | 两列表格并排 | |
| Claude 决定 | 让实现时自行选择 | |

**User's choice:** 前后分段对比

### Q4: 对比案例的内容深度到哪里？

| Option | Description | Selected |
|--------|-------------|----------|
| 核心判断 + 主题拆分 + 任务树摘要（推荐） | 三个关键节点，任务树只到里程碑级 | ✓ |
| 完整六段输出对比 | 全部六段都展示 | |
| Claude 决定 | 让实现时自行判断 | |

**User's choice:** 核心判断 + 主题拆分 + 任务树摘要

---

## 现有案例 2 修复

### Q5: 案例 2 需要修复吗？

| Option | Description | Selected |
|--------|-------------|----------|
| 修复为归纳感知（推荐） | 加入归纳检查步骤描述 | ✓ |
| 保持不变 | 结果一样，无需改 | |
| Claude 决定 | 让实现时判断 | |

**User's choice:** 修复为归纳感知

---

## Claude's Discretion

- 对比案例中错误/正确示例的具体文案
- 检查点的具体条目数量
- 案例 2 修复后的具体措辞

## Deferred Ideas

None — discussion stayed within phase scope
