# Retrospective

## Milestone: v1.0 — 输出质量优化

**Shipped:** 2026-04-13
**Phases:** 2 | **Plans:** 3

### What Was Built
- decision-rules.md 新增向上归纳检查步骤，在主题拆分后判断是否能收敛为统一顶层意图
- output-template.md 新增归纳型模板（一句话顶层意图 + 子任务线展开）和三级优先级规则
- SKILL.md 工作流集成归纳检查，核心原则泛化为多主题通用归纳原则
- 新增 2 个行为级 fixture（归纳成功 04 + 归纳失败 05）
- examples.md 新增案例 7 正反对比 + 案例 5/6 战略型正反例 + 案例 2 术语修复

### What Worked
- 两步修复路径（先规则后示例）清晰，Phase 1 和 Phase 2 解耦良好
- Cross-AI review（Gemini + Codex）发现了关键的术语泄漏风险（静默回退），避免了模型在输出中暴露内部推理过程
- 单文件修改的 phase 执行快速高效（单 plan 80s 完成）

### What Was Inefficient
- Phase 1 的案例 5/6 作为本地修改未提交，导致 Phase 2 worktree 合并时产生冲突，需要手动解决
- Worktree 执行器在文件不存在时（案例 5/6）做了错误假设，将案例 7 追加到了错误位置

### Patterns Established
- 内部处理术语（如「静默回退」）不应出现在 examples.md 等强提示材料中
- 正反对比案例格式：先 ❌ 后 ✅，保持信息量相当，区别在结构而非信息缺失
- 归纳型核心判断固定格式：「CEO 真正在推动的是：[顶层意图]」

### Key Lessons
- 未提交的本地修改是 worktree 合并的隐患——应在执行前确保工作区干净
- 纯 Markdown prompt 工程项目的 phase 执行非常快（全程 ~1.5 小时），但跨 AI review 和规划占了大部分时间

### Cost Observations
- Sessions: 2 (Phase 1 + Phase 2)
- Notable: Phase 2 单 plan 执行只用 42k tokens（executor agent）

## Milestone: v2.0 — 咨询方法论重构

**Shipped:** 2026-04-15
**Phases:** 4 | **Plans:** 11 | **Tasks:** 20

### What Was Built

- SCQA 优先解析入口：内部 `<scqa_analysis>` 推演 + 四要素完整度→证据强度映射，替换旧前置分流
- 统一金字塔任务树模板：`output-template.md` §3 单一骨架承载战略/归纳/常规输入，层级深度随证据强度（弱=2 层 / 中=3 层 / 强=4 层）弹性伸缩
- MECE 四维校验：`decision-rules.md` §6 新增互斥 / 完备 / 数量 2-4 / 分组一致性四维 + underflow/overflow cardinality 兜底
- So-what 空洞过滤：`decision-rules.md` §7 新增 5 类空洞模式黑名单 + 语义自问双道机制
- SKILL.md 工作流第 6 步：串行调度 `<mece_check>` → `<sowhat_filter>`，懒加载注册 + 扩展内部术语禁词
- examples.md 全量重写 8 个 v2.0 案例 + 作者侧 / 正文禁词双重边界声明
- Phase 6 UAT 主文档：v1.0 三 fixture 三维回归 + 端到端管线段 + 四文件术语终扫门禁

### What Worked

- SCQA 单入口统一替代三种前置分流，消除旧模板分叉带来的跨文件漂移
- 单一事实源原则（规则写 decision-rules，SKILL 只接入流程引用），避免了多处条文维护
- 禁词表作为全局门禁，把内部推理标签和分组术语封堵在输出之外，双重保障（SKILL 禁词段 + examples 作者侧声明）
- Phase 6 以「战略型案例承担端到端管线演示职责」的方式对 SCQA→金字塔→MECE→So-what 做了一次性 E2E 锚定

### What Was Inefficient

- Phase 5 的 `05-VERIFICATION.md` 在执行阶段遗漏，直到 v2.0 milestone audit 才回填——形式化验证 gap 在闭环前才被发现
- `05-UAT.md` 8 类行为断言手册产出后从未人工逐条执行（留作 v2.1 tech debt）
- Phase 4-03 计划内自动验收脚本存在文案检查冲突（标题 vs 禁词 grep），被迫在 Phase 6 阶段改造终扫策略
- Case 1-7 在 Phase 4 时先 deferred 到 Phase 6 才系统性重写，跨 phase 承接有额外协调成本

### Patterns Established

- **规则单一事实源**：条文只写在 `decision-rules.md`，`SKILL.md` 仅承担 workflow 编排与懒加载注册
- **内部推理 XML 隔离 + 禁词双重封堵**：`<scqa_analysis>` / `<mece_check>` / `<sowhat_filter>` + 禁词表 + 作者侧声明，三层保障不泄漏到用户输出
- **证据强度驱动弹性层级**：弱=2 层 / 中=3 层 / 强=4 层 + ±1 弹性，避免层级抖动
- **作者侧 vs 正文侧术语边界**：examples.md 作者注释允许方法论术语，案例正文遵循全禁词清单
- **v1.0 回归用 UAT 三维断言承接**：保持 fixture 基线不漂移，让回归验证可执行且不引入新 fixture

### Key Lessons

- VERIFICATION.md 不能因为下游 Phase 的 E2E 覆盖就被省略——形式化验证记录本身是 milestone audit 的必需输入
- 上游 Phase deferred 到下游 Phase 的承接需要在两边 ROADMAP 中显式声明「Upstream Carryover」段，避免 gap 在 audit 阶段才暴露
- 跨文件契约（层级术语、禁词清单、懒加载触发）必须在单个 Phase 内通过 grep 终扫一次性清零，不要跨 Phase 累积
- 混合信号优先级矩阵（战略型 > 归纳型 > 常规型）对 SCQA 推演收敛非常关键，必须写入单一事实源并用对抗样例锚定

### Cost Observations

- 4 个 Phase、11 个 Plan、4 次跨 AI 评审（Phase 4 reviews）、3 次 VERIFICATION 执行 + 1 次回填
- Sessions: 多 session 分散执行（2026-04-14 至 2026-04-15）
- 显著节省：统一金字塔模板替代三模板分叉后，decision-rules 维护成本从 O(3) 降为 O(1)

---

## Cross-Milestone Trends

| Metric | v1.0 |
|--------|------|
| Phases | 2 |
| Plans | 3 |
| Duration | ~1.5 hours |
| Key risk | 未提交本地修改导致合并冲突 |
