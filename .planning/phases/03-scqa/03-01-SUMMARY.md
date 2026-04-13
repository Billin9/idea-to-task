---
phase: 03-scqa
plan: 01
subsystem: prompting
tags: [scqa, markdown-skill, prompt-engineering, pyramid-principle]
requires: []
provides:
  - "SCQA 优先的输入解析规则"
  - "基于完整度的证据强度映射"
  - "使用 <scqa_analysis> 的统一工作流入口"
affects: [04-pyramid, output-template, examples]
tech-stack:
  added: []
  patterns:
    - "SCQA-first parsing"
    - "internal xml reasoning tags"
key-files:
  created:
    - .planning/phases/03-scqa/03-01-SUMMARY.md
  modified:
    - skills/idea-to-task/references/decision-rules.md
    - skills/idea-to-task/SKILL.md
key-decisions:
  - "用 SCQA 单入口替换战略型/归纳型/常规型前置分流"
  - "把多主题归纳吸收到核心判断推演中，不再保留独立归纳步骤"
  - "证据强度按 SCQA 完整度映射，并保留到 Phase 4 前的临时深度接口"
patterns-established:
  - "Pattern: 先在内部 <scqa_analysis> 中完成背景、矛盾、问题、判断的顺序推演，再组织用户可见输出"
  - "Pattern: 定向追问只在关键要素缺失且会改变方向时触发，并与通用补问分开计数"
requirements-completed: [SCQA-01, SCQA-02, SCQA-03, SCQA-04]
duration: 2min
completed: 2026-04-14
---

# Phase 03 Plan 01: SCQA 输入解析层 Summary

**为 CEO 碎片输入建立 SCQA 优先解析入口，用内部 `<scqa_analysis>` 推演和完整度映射替换旧的前置分流。**

## Performance

- **Duration:** 2 min
- **Started:** 2026-04-14T02:34:50+08:00
- **Completed:** 2026-04-14T02:36:20+08:00
- **Tasks:** 2
- **Files modified:** 3

## Accomplishments

- 用 5 节新结构重写 `decision-rules.md`，把 SCQA 推演、定向追问和完整度映射收拢为统一规则入口。
- 重写 `SKILL.md` 的核心原则、工作流、边界处理和补问规则，使主流程改为 SCQA 单入口。
- 保持 `output-template.md` 与 `examples.md` 不变，仅对接其既有接口，满足本阶段边界约束。

## Task Commits

Each task was committed atomically:

1. **Task 1: 重构 decision-rules.md — 嵌入 SCQA 推演规则** - `b2be954` (feat)
2. **Task 2: 重构 SKILL.md 工作流 — 替换为 SCQA 管线** - `907fb72`, `027c299`, `c713535` (feat/fix)

**Plan metadata:** `76cfef8` (docs)

## Files Created/Modified

- `.planning/phases/03-scqa/03-01-SUMMARY.md` - 记录 Phase 03-01 的执行结果、决策和验收状态
- `skills/idea-to-task/references/decision-rules.md` - 定义 SCQA 推演、追问触发和完整度到证据强度的映射
- `skills/idea-to-task/SKILL.md` - 将技能主工作流改为 SCQA 单入口并更新补问与懒加载说明

## Decisions Made

- 采用 SCQA 作为所有输入的第一层解析，不再保留战略型、归纳型、常规型前置分流。
- 把旧的多主题归纳逻辑并入核心判断推演，避免在主工作流中重复建模。
- 只在本阶段建立“完整度 → 证据强度”映射，具体层级展开继续留给 Phase 4。

## Deviations from Plan

### Auto-fixed Issues

**1. [Rule 1 - Bug] 补齐 SKILL.md 的计划级验收细节**
- **Found during:** Task 2（重构 SKILL.md 工作流）
- **Issue:** 初版工作流入口已切到 SCQA，但仍缺少一条通用补问边界和两条明确禁止项，导致执行计划中的字面校验条件没有全部覆盖。
- **Fix:** 在 `SKILL.md` 中补上“多个主题彼此独立时先拆主题再判断是否补问”、禁止暴露方法论术语、禁止跳过 SCQA 推演直接输出任务树，并补齐对 `decision-rules.md 第 1/2/3 节` 的字面引用。
- **Files modified:** `skills/idea-to-task/SKILL.md`
- **Verification:** `grep -c "decision-rules.md 第 1 节|decision-rules.md 第 2 节|decision-rules.md 第 3 节" skills/idea-to-task/SKILL.md` 与 `uv run skills/idea-to-task/scripts/validate_skill.py skills/idea-to-task --strict`
- **Committed in:** `027c299` (part of Task 2 commit)

**2. [Rule 1 - Bug] 修复弱证据输出层级的跨文件漂移**
- **Found during:** Phase 03 验证（`03-VERIFICATION.md`）
- **Issue:** `decision-rules.md` 规定弱证据“只输出项目级”，但 `SKILL.md` 允许“项目级或里程碑级”，导致 `SCQA-04` 和路线图成功标准 4 无法通过。
- **Fix:** 将 `SKILL.md` 的弱证据边界收紧为“只输出到项目级”，与 `decision-rules.md` 和 `ROADMAP.md` 保持一致。
- **Files modified:** `skills/idea-to-task/SKILL.md`
- **Verification:** `rg -n "弱证据|项目级|里程碑级|执行项级" skills/idea-to-task/SKILL.md skills/idea-to-task/references/decision-rules.md` 与 `uv run skills/idea-to-task/scripts/validate_skill.py skills/idea-to-task --strict`
- **Committed in:** `c713535` (verification follow-up fix)

---

**Total deviations:** 2 auto-fixed (2 bugs)
**Impact on plan:** 两次修正都用于消除提示层之间的契约缺口，不改变既定范围或阶段设计，只把 Phase 03 收敛到计划要求的严格边界。

## Issues Encountered

None

## User Setup Required

None - no external service configuration required.

## Next Phase Readiness

- Phase 03 的 SCQA 解析入口已经就位，可继续在 Phase 04 把输出层切到金字塔结构。
- `output-template.md` 和 `examples.md` 仍是旧接口，下一阶段需要围绕新的 SCQA 顶层判断更新模板与示例。

## Self-Check: PASSED

- 已确认 `.planning/phases/03-scqa/03-01-SUMMARY.md` 存在。
- 已确认任务提交 `b2be954`、`907fb72` 均可在 `git log --oneline --all` 中找到。

---
*Phase: 03-scqa*
*Completed: 2026-04-14*
