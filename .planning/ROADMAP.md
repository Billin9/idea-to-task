# Roadmap: idea-to-task 输出质量优化

## Overview

本次优化的核心问题是：skill 在处理战略型输入时，会把本该有父子关系的意图平铺成并列主题。修复路径分两步：先重构判断逻辑和输出模板（Phase 1），再用正反对比案例校准模型行为（Phase 2）。

## Phases

**Phase Numbering:**
- Integer phases (1, 2, 3): Planned milestone work
- Decimal phases (2.1, 2.2): Urgent insertions (marked with INSERTED)

Decimal phases appear between their surrounding integers in numeric order.

- [ ] **Phase 1: 判断与输出重构** - 在 decision-rules.md 和 output-template.md 中实现向上归纳逻辑与单顶层意图输出结构
- [ ] **Phase 2: 示例校准** - 在 examples.md 中补充正反对比案例，对齐模型期望行为

## Phase Details

### Phase 1: 判断与输出重构
**Goal**: skill 能在主题拆分前先做向上归纳判断，输出结构支持「一句话顶层意图 + 子任务线展开」
**Depends on**: Nothing (first phase)
**Requirements**: JUDGE-01, JUDGE-02, OUT-01, OUT-02, OUT-03
**Success Criteria** (what must be TRUE):
  1. 用同一战略型输入调用 skill，核心判断段落的第一句是顶层意图，而非并列主题列表
  2. 主题拆分输出中，当检测到包含关系时只出现一个顶层主题，原来的并列主题变为其子任务线或里程碑
  3. 任务树模板中存在「归纳路径」层级，被包含的子主题能降级为里程碑节点
  4. decision-rules.md 中存在明确的「向上归纳」判断步骤，位于主题拆分步骤之前
**Plans:** 2 plans
Plans:
- [ ] 01-01-PLAN.md — decision-rules.md 新增归纳步骤 + output-template.md 新增归纳型模板与优先级规则
- [ ] 01-02-PLAN.md — SKILL.md 工作流与核心原则更新 + 行为级验证 fixture

### Phase 2: 示例校准
**Goal**: examples.md 包含正反对比案例，模型能直接参照期望行为而不是仅靠规则推理
**Depends on**: Phase 1
**Requirements**: EX-01
**Success Criteria** (what must be TRUE):
  1. examples.md 中存在至少一组正反对比案例，同一输入分别展示「平铺输出（错误）」和「归纳输出（正确）」
  2. 正确示例的结构与 Phase 1 重构后的 output-template.md 保持一致（顶层意图 + 子任务线）
**Plans**: TBD

## Progress

**Execution Order:**
Phases execute in numeric order: 1 → 2

| Phase | Plans Complete | Status | Completed |
|-------|----------------|--------|-----------|
| 1. 判断与输出重构 | 0/2 | Not started | - |
| 2. 示例校准 | 0/TBD | Not started | - |
