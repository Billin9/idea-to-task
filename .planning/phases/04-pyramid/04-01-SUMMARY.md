---
phase: 04-pyramid
plan: 01
subsystem: prompting
tags: [pyramid-principle, markdown-skill, prompt-engineering, output-template]
requires:
  - phase: 03-scqa
    provides: "SCQA 顶层判断与证据强度映射"
provides:
  - "统一的分层任务树模板"
  - "弱/中/强证据对应的弹性层级规则"
  - "战略型/归纳型/常规触发下的单骨架填充约束"
affects: [04-02, 04-03, output-template, examples]
tech-stack:
  added: []
  patterns:
    - "single pyramid task tree template"
    - "evidence-driven depth control"
key-files:
  created:
    - .planning/phases/04-pyramid/04-01-SUMMARY.md
  modified:
    - skills/idea-to-task/references/output-template.md
key-decisions:
  - "删除模板分流，改为单一分层任务树骨架"
  - "把层级深度与证据强度绑定为弱=2层、中=3层、强=4层，并允许 ±1 弹性"
  - "保留六段式外部接口，只重写第 3 节"
patterns-established:
  - "Pattern: 模板层只保留骨架与条件字段，判定规则继续由 decision-rules.md 持有"
  - "Pattern: 用户可见输出继续使用主题/里程碑/执行项术语，不暴露内部方法论词汇"
requirements-completed: [PYMD-01, PYMD-02, PYMD-03, PYMD-04]
duration: 8min
completed: 2026-04-14
---

# Phase 04 Plan 01: 金字塔原理输出结构 Summary

**将 `output-template.md` 第 3 节重写为统一分层任务树模板，用单一骨架承载战略型、归纳型和常规输入，并把层级深度改为随证据强度弹性伸缩。**

## Performance

- **Duration:** 8 min
- **Started:** 2026-04-14T22:40:00+0800
- **Completed:** 2026-04-14T22:47:56+0800
- **Tasks:** 1
- **Files modified:** 2

## Accomplishments

- 删除第 3 节原有的三模板分叉与优先级说明，改为单一分层任务树模板。
- 写清同层 2 到 4 个、弱/中/强证据对应 2/3/4 层、以及 ±1 弹性规则。
- 在不改动第 1/2/4/5/6 节和输出风格段的前提下，为后续规则对齐与示例补充提供唯一模板事实源。

## Task Commits

Each task was committed atomically:

1. **Task 1: 重写 output-template.md §3 为统一分层任务树模板** - `069d8c7` (feat)

**Plan metadata:** 本 SUMMARY 所在的 `docs(04-01)` 提交

## Files Created/Modified

- `.planning/phases/04-pyramid/04-01-SUMMARY.md` - 记录 Plan 04-01 的执行结果、决策与验收状态
- `skills/idea-to-task/references/output-template.md` - 用统一骨架替换原三模板分流，并补齐层级规则与条件字段

## Decisions Made

- 只在模板层保留骨架与填充条件，不把战略型触发判定细则下沉到模板正文。
- 用主题/里程碑/执行项继续承载用户可见结构，避免在输出层暴露内部方法论术语。
- 允许极弱证据停在主题层，并把不确定性回收到第 5 节表达。

## Deviations from Plan

None - plan executed exactly as written.

## Issues Encountered

- 执行代理在完成文件改写后未返回完成信号，也未产出 `SUMMARY.md`。已按 execute-phase 工作流的 spot-check fallback 接管收尾，并在主工作区完成验收、总结与提交。

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- `output-template.md` 已成为 Phase 4 的唯一模板事实源，可继续对齐 `SKILL.md` 与 `decision-rules.md`。
- Phase 04-02 和 04-03 只依赖本模板字面约束，已具备进入 Wave 2 的条件。

## Self-Check: PASSED

- 已确认 `skills/idea-to-task/references/output-template.md` 通过计划内 grep 断言。
- 已确认 `uv run skills/idea-to-task/scripts/validate_skill.py skills/idea-to-task --strict` 通过。

---
*Phase: 04-pyramid*
*Completed: 2026-04-14*
