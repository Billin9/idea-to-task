# Milestones

## v2.0 咨询方法论重构 (Shipped: 2026-04-15)

**Phases completed:** 4 phases, 11 plans, 20 tasks

**Key accomplishments:**

- 为 CEO 碎片输入建立 SCQA 优先解析入口，用内部 `<scqa_analysis>` 推演和完整度映射替换旧的前置分流。
- 将 `output-template.md` 第 3 节重写为统一分层任务树模板，用单一骨架承载战略型、归纳型和常规输入，并把层级深度改为随证据强度弹性伸缩。
- 把 `SKILL.md` 与 `decision-rules.md` 对齐到统一分层任务树模板的字面契约，收敛层级深度、术语禁令和触发引用的跨文件漂移。
- 在 `examples.md` 末尾新增案例 8，用售后体验场景展示常规多主题输入从平铺写法切换到分层写法后的结构改进。
- 在 `decision-rules.md` 中新增第 6 节 MECE 互斥完备校验，补齐四维校验、`<mece_check>` 内部格式，以及 underflow / overflow 的 cardinality 兜底规则。
- 在 `decision-rules.md` 中补齐混合信号优先级矩阵，并新增第 7 节 So-what 空洞过滤，用 5 类模式库和双道语义自问拦截空洞任务描述。
- 在 `SKILL.md` 中插入第 6 步内部质量校验，并同步补齐第 6/7 节懒加载入口与内部术语禁词表，使 Phase 5 的规则正式接入主工作流。
- 创建 `05-UAT.md` 行为验证手册，覆盖 5 类基础输入和 3 类对抗输入，使 Phase 5 的 MECE / So-what / 优先级 / cardinality 规则具备可执行的 spot-check 脚本。
- examples.md 已升级为 v2.0 咨询管线案例契约，覆盖 Phase 5 UAT 5 类行为与 3 个新增封闭点。
- SKILL.md 的 examples 作者侧术语边界已落地，三份运行时 skill 文档完成旧层级/模板术语清零验证。
- Phase 6 UAT 主文档已创建，覆盖 v1.0 不退化、端到端管线和四文件术语扫清门禁。

---

## v1.0 输出质量优化 (Shipped: 2026-04-13)

**Phases completed:** 2 phases, 3 plans, 5 tasks

**Key accomplishments:**

- decision-rules.md 新增向上归纳检查步骤，output-template.md 新增归纳型模板与三级优先级规则
- SKILL.md 工作流新增向上归纳检查步骤，核心原则泛化为多主题通用归纳原则，新增 2 个行为级 fixture 验证归纳成功和失败场景
- 1. [Rule 3 - Blocking] 案例 5/6 尚未创建，案例 7 追加位置调整

---
