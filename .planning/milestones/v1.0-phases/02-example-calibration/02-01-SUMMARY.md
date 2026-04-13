---
phase: 02-example-calibration
plan: 01
subsystem: skill-references
tags: [examples, induction, contrastive-learning]
dependency_graph:
  requires: []
  provides: [contrastive-example, case2-fix]
  affects: [skills/idea-to-task/references/examples.md]
tech_stack:
  added: []
  patterns: [contrastive-few-shot]
key_files:
  modified:
    - skills/idea-to-task/references/examples.md
decisions:
  - id: D-CASE7-APPEND
    summary: "案例 7 追加在当前文件末尾（案例 4 之后），因案例 5/6 由并行计划 02-02 创建，合并时将自动排序"
metrics:
  duration: 80s
  completed: 2026-04-13T01:26:05Z
---

# Phase 02 Plan 01: 修复案例 2 + 新增案例 7 正反对比 Summary

案例 2 改用面向读者的自然表述替代内部术语「静默回退」，案例 7 新增归纳型正反对比（平铺 vs 归纳），正确示例严格对齐 output-template.md 归纳型模板格式。

## Completed Tasks

| Task | Name | Commit | Files |
|------|------|--------|-------|
| 1 | 修复案例 2 + 新增案例 7 正反对比 | a654c04 | skills/idea-to-task/references/examples.md |

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 3 - Blocking] 案例 5/6 尚未创建，案例 7 追加位置调整**
- **Found during:** Task 1
- **Issue:** 计划要求在案例 6 之后追加案例 7，但案例 5/6 由并行计划 02-02 创建，当前文件仅有案例 1-4
- **Fix:** 将案例 7 追加在案例 4 之后（文件末尾），合并时由 orchestrator 处理排序
- **Files modified:** skills/idea-to-task/references/examples.md
- **Commit:** a654c04

## Verification Results

- `grep -c "^## 案例"` = 5（当前文件含案例 1-4 + 7，案例 5/6 待并行计划合并）
- `grep -c "❌ 错误示例（平铺）"` = 1
- `grep -c "✅ 正确示例（归纳）"` = 1
- `grep -c "CEO 真正在推动的是：产品 X 下季度上线"` = 2（检查点 + 正确示例各一处）
- `grep -c "单主题（归纳）"` = 2（正确示例 + 检查点各一处）
- `grep -c "不应出现.*总体方案设计.*作为独立主题"` = 1
- `grep -c "向上归纳检查"` = 1（案例 2 处理方式）
- `grep "静默回退"` = 0 行匹配（全文不含此术语）

## Key Changes

### 案例 2 修复
- 原文：`处理方式：先拆主题，再分别给任务树，可附 1 到 3 个关键问题。`
- 新文：`处理方式：先拆主题，再做向上归纳检查；因各方向不服务同一目标，按多主题分别输出，可附 1 到 3 个关键问题。`
- 自然表述归纳检查流程，不使用「静默回退」内部术语

### 案例 7 新增
- 输入文本复用 fixture 04 原文
- 错误示例：三个并列主题（主题 I/II/III），平铺结构
- 正确示例：单顶层主题「产品 X 上线」，技术/运营/市场降级为里程碑
- 5 条检查点，含战略型边界约束「不应出现总体方案设计作为独立主题」
