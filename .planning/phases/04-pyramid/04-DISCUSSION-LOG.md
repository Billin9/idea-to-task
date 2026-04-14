# Phase 4: 金字塔原理输出结构 - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions captured in CONTEXT.md — this log preserves the analysis.

**Date:** 2026-04-14
**Phase:** 04-pyramid
**Mode:** discuss（推荐项快速收敛）

## Gray Areas Analyzed

识别出 4 个关键 gray area。其余 PROJECT.md / REQUIREMENTS.md / Phase 3 CONTEXT 已锁定的决策未再重议。

### 1. 三套模板统一策略
**问题:** 战略型/归纳型/常规三套模板如何统一为单一金字塔结构？
**选项:**
- A. 彻底合并为单一金字塔（推荐）
- B. 保留三套模板但套金字塔外壳
- C. 渐进合并，战略型留到 Phase 5/6

**选择:** A — 彻底合并
**理由:** PYMD-03 明确要求只有一套模板；保留外壳不算真正落实；渐进会延迟 v2.0 核心价值兑现

### 2. 战略型「总体方案设计」条件规则去留
**问题:** 跨部门/治理节奏/季度周期时第一主题必含「总体方案」的条件规则如何处理？
**选项:**
- A. 保留为金字塔第一支柱条件规则（推荐）
- B. 并入 SCQA 推演产物，由 Answer 自然导出
- C. 完全删除

**选择:** A — 保留为条件规则
**理由:** v1.0 已验证该规则有效；依赖模型推演自然导出稳定性风险高；完全删除可能导致战略型输出退化

### 3. 金字塔「战略支柱」层与现有「主题拆分」衔接
**问题:** 金字塔支柱层与现有主题术语如何衔接？
**选项:**
- A. 主题即支柱，术语不变（推荐）
- B. 新增支柱层，主题下沉
- C. 用「支柱」替代「主题」全面换词

**选择:** A — 术语不变
**理由:** 对用户透明；改动最小；不增加用户认知负担；避免与六段式输出格式冲突；Out of Scope 明确禁止暴露方法论术语

### 4. examples.md 金字塔对比案例（EXAM-02）本 phase 分工
**问题:** examples.md 的金字塔正反对比案例在本 phase 如何安排？
**选项:**
- A. 本 phase 同步新增 1 组（推荐）
- B. 本 phase 不动 examples，留给 Phase 6
- C. 全量重写 examples.md

**选择:** A — 同步新增 1 组
**理由:** 让本 phase 有可自我验证的锚点样本；避免 Phase 4 落实后缺示例导致漂移；不碰 v1.0 已有案例，降低回归风险

## Corrections Made

No corrections — all recommended options accepted.

## External Research

No external research triggered — all gray areas resolvable from codebase + PROJECT/REQUIREMENTS 约束。

## Scope Guardrails Applied

- MECE/So-what 内部校验推迟到 Phase 5（REQUIREMENTS 已分配）
- v1.0 fixture 全量回归和 examples 其余案例改造推迟到 Phase 6
- 不新增文件、不改目录结构（PROJECT.md 约束）
- 不引入 Action Items 表格（PROJECT.md Out of Scope）
- 用户侧不暴露「支柱」「金字塔」等方法论术语（PROJECT.md Out of Scope + Phase 3 review fix 负面示例清单）
