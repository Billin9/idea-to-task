---
phase: 06-examples-compat
plan: 01
subsystem: skill-examples
tags: [markdown, prompt, examples, compatibility]

requires:
  - phase: 04-pyramid
    provides: 统一金字塔弹性层级与案例正反对比方式
  - phase: 05-mece-so-what
    provides: 术语黑名单、MECE 校验与 So-what 过滤规则
provides:
  - examples.md 顶部术语边界声明
  - 8 个重写案例，覆盖 Phase 5 UAT 5 类行为与 EXAM-01/02/03 封闭点
  - 战略型案例的完整管线演示锚点
affects: [06-examples-compat, idea-to-task, examples.md]

tech-stack:
  added: []
  patterns:
    - 作者侧注释与案例正文分离
    - 案例标题覆盖标签作为 UAT 映射锚点
    - 正反对比案例用于封闭结构缺陷

key-files:
  created:
    - .planning/phases/06-examples-compat/06-01-SUMMARY.md
  modified:
    - skills/idea-to-task/references/examples.md

key-decisions:
  - "examples.md 顶部新增术语边界声明，明确作者侧标题/注释允许方法论术语，案例正文仍执行完整禁词清单。"
  - "8 个案例按可读性排列：5 个正向行为案例在前，3 个封闭点正反对比案例在后。"
  - "战略型案例保留「完整管线演示」作者侧锚点，供 06-UAT.md 端到端管线段引用。"

patterns-established:
  - "案例正文按六段式输出；作者侧方法论解释放入 HTML 注释，避免污染模拟输出样板。"
  - "正反对比案例的禁词只允许出现在小节标题或作者侧注释中，正文段落保持清洁。"

requirements-completed: [COMP-02, EXAM-01, EXAM-02, EXAM-03]

duration: partial agent execution + orchestrator recovery
completed: 2026-04-15
---

# Phase 06 Plan 01: Examples Compatibility Rewrite Summary

**examples.md 已升级为 v2.0 咨询管线案例契约，覆盖 Phase 5 UAT 5 类行为与 3 个新增封闭点。**

## Performance

- **Duration:** partial agent execution + orchestrator recovery
- **Completed:** 2026-04-15
- **Tasks:** 2
- **Files modified:** 1

## Accomplishments

- 在 `examples.md` 顶部新增「## 术语边界声明」，明确作者侧与案例正文的术语边界。
- 全量重写 8 个案例，覆盖战略型、归纳型、常规型、中等证据三层、极弱证据两层，以及 EXAM-01/02/03 三个正反对比封闭点。
- 战略型案例作者侧注释显式包含「完整管线演示」锚点，并串联 SCQA 推演、金字塔展开、MECE 校验、So-what 过滤。
- 案例正文统一使用「主题 / 里程碑 / 执行项」弹性层级术语，旧层级术语已清零。

## Task Commits

1. **Task 1: examples.md 顶部新增术语边界声明** - `93e7f0b` (feat)
2. **Task 2: 全量重写 Case 1-8** - committed by orchestrator recovery after executor timeout

## Files Created/Modified

- `skills/idea-to-task/references/examples.md` - 新增术语边界声明并重写 8 个案例。
- `.planning/phases/06-examples-compat/06-01-SUMMARY.md` - 记录 Plan 06-01 执行结果、验证命令与恢复动作。

## Decisions Made

- 作者侧方法论术语只用于标题、HTML 注释和案例说明，不作为模型可模仿的运行时正文。
- 3 个对比案例保留 `### ❌` / `### ✅` 小节标题，以便人工和脚本快速定位结构差异。
- 极弱证据案例保留固定验收句「输入不足以支撑多主题拆分」，用于后续 UAT 静态断言。

## Verification

- `rg -c '^## 案例' skills/idea-to-task/references/examples.md`：返回 `8`。
- `rg -n '^## 术语边界声明' skills/idea-to-task/references/examples.md`：返回 1 行。
- `rg -n '完整管线演示|单主题（归纳）|总体方案设计|输入不足以支撑多主题拆分' skills/idea-to-task/references/examples.md`：关键锚点均命中。
- `rg -n '^### ❌|^### ✅' skills/idea-to-task/references/examples.md`：各返回 3 行。
- `rg -n '项目级|里程碑级|执行项级' skills/idea-to-task/references/examples.md`：零命中。
- `perl` 正文禁词抽检脚本：排除作者侧注释和正反对比标题后，输出正文无禁词命中。

## Deviations from Plan

- executor 在完成主体改写后未返回完成信号，orchestrator 通过 spot-check 接管收尾，补写 SUMMARY 并提交未提交改动。

## Issues Encountered

- executor 超时关闭前留下 `examples.md` 未提交改动；内容经验证完整后由 orchestrator 恢复提交。

## Known Stubs

None.

## Threat Flags

None - 本计划只修改 Markdown 提示案例，不引入新代码执行路径、网络访问或数据存储。

## User Setup Required

None.

## Next Phase Readiness

Plan 06-03 可以引用 `examples.md` 中的「完整管线演示」锚点创建 Phase 6 UAT 文档。

---
*Phase: 06-examples-compat*
*Completed: 2026-04-15*
