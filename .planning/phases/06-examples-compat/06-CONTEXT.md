# Phase 6: 示例校准与兼容性验证 - Context

**Gathered:** 2026-04-15
**Status:** Ready for planning

<domain>
## Phase Boundary

用正反对比案例锚定完整咨询管线（SCQA → 金字塔 → MECE → So-what）的输出行为，并对 v1.0 非战略型 fixture 做回归验证，确保 CEO 碎片输入可端到端产出结构化结果、v1.0 已固化能力不退化。修改范围严格限于 `skills/idea-to-task/` 四个文件以及 `.planning/phases/06-examples-compat/` 新增的验收文档；不改 skill 目录结构、不新增 skill 侧 fixture。

</domain>

<decisions>
## Implementation Decisions

### Case 1-7 改造策略
- **D-01:** 全量重写 Case 1-7。Phase 4 评审共识的 1:7 Few-shot 污染风险由全量重写从根源消除，与 v2.0「全面重构」方向一致；不使用 `(Legacy Context - Pending Update)` 过渡前缀方案
- **D-02:** 输入素材替换为新素材。重写时不保留 Case 1-7 的原 CEO 碎片输入，按新咨询管线最佳 SOP 重新选题；不受旧输入形态束缚
- **D-03:** 重写后案例总数仍为 8。EXAM-01（SCQA 解析正反对比）与 EXAM-03（MECE 互斥完备正反对比）融入重写后的 8 个案例中，不作为独立新增 Case 9/10；避免案例总数膨胀
- **D-04:** Case 8（金字塔正反对比）同步重写。Phase 4 D-09 建立的「非金字塔平铺 vs 金字塔分层」正反对比方法论保留，但素材和输出一并按新风格更新，与其它 7 个案例对齐，避免风格独立

### 选题矩阵
- **D-05:** 8 个重写案例的选题对齐 Phase 5 UAT 5 类 + 3 个新增封闭点：
  - 5 类覆盖 Phase 5 05-UAT.md 已验证的输入场景——战略型、归纳型、常规型、中等证据三层、极弱证据两层
  - 3 个封闭点承载本 phase 新增对比——Case 8（金字塔正反）、1 组 SCQA 解析正反、1 组 MECE 互斥完备正反
  - 战略型 Case 同时承担端到端管线演示角色（见 D-07）
- **D-06:** 重写后 8 个案例在 examples.md 中的排列顺序由 Claude 在 plan/execute 阶段按可读性决定，不在此锁定

### 端到端验证载体
- **D-07:** Success Criteria 4 的端到端验证由 8 个重写案例中的「战略型 Case」承担。该 Case 覆盖跨部门协同/治理节奏输入，案例注释显式标注「完整管线演示」职责（SCQA 推演 → 金字塔支柱 → MECE 校验 → So-what 过滤全链路展示）
- **D-08:** 不新增 Case 9 专用端到端案例，不新增 skill 侧 fixture 文件。端到端管线的运行时断言由 06-UAT.md 补充（见 D-10/D-11）

### v1.0 回归基准
- **D-09:** v1.0 回归覆盖三个历史 fixture：`tests/fixtures/idea-to-task/01-clear-direction.md`、`02-mixed-topics.md`、`03-high-risk-ambiguity.md`。fixture 文件本身保持不动（Phase 4/5 未改，Phase 6 也不改）
- **D-10:** 新建 `.planning/phases/06-examples-compat/06-UAT.md`，承接 Phase 5 `05-UAT.md` 的 UAT 格式框架，新增「v1.0 回归段」和「端到端管线段」两块，作为 Phase 6 验收主文档
- **D-11:** 「不退化」采用三维断言：
  1. **结构完整性** — v1.0 三个 fixture 的 v2.0 输出仍具备「核心判断 → 主题拆分 → 分层任务树 → 执行建议 → 风险 → 下一步」六段式
  2. **禁词无泄漏** — 输出不含 `mece_check / sowhat_filter / scqa_analysis / 金字塔 / SCQA / MECE / So-what / grouping / inductive / deductive` 等方法论术语
  3. **输入类型未被硬扣** — 清晰指令型（如 01-clear-direction）不被错误地施加战略型三支柱结构，归纳型/常规型保留应有形态
  三维全中为通过；任一维失败记回归未通过

### 术语边界声明
- **D-12:** examples.md 顶部新增「术语边界声明」段落：明确作者侧标题、注释、章节名允许出现 SCQA / 金字塔 / MECE / So-what 等方法论术语，但案例正文（模拟模型输出部分）严格禁用；同时说明这是「给模型和读者的双重读者指引」
- **D-13:** SKILL.md 禁词段同步扩展一句「examples.md 作者侧标题和注释不在此禁词范围内，examples 正文（模型输出示例）遵循本禁词清单」，与 examples.md 顶部声明形成双重保障，避免自动验收脚本 grep 到作者侧术语产生误报

### 旧术语一致性扫清
- **D-14:** 四文件全扫统一替换。一次性扫描 SKILL.md / decision-rules.md / output-template.md / examples.md，清单包括但不限于：
  - 层级术语：「项目级 / 里程碑级 / 执行项级」→ 金字塔弹性层级术语（Phase 4 D-07 已约定）
  - 模板分类术语：「战略型模板 / 归纳型模板 / 常规型模板」→ 统一金字塔模板 + SCQA 内部条件字段
  - 其他残留：「三套模板 / 模板选择优先级 / 模板分流」等 Phase 4 未完全清理的表述
- **D-15:** 建立历史白名单说明：如 Phase 3-5 CONTEXT/ROADMAP 中「非战略型案例」等描述已成既定历史语言，skill 侧的「描述历史演进」类注释可保留但需加作者侧注释说明，避免模型误读为运行时术语

### Claude's Discretion
- 06-UAT.md 内部章节切分、断言脚本的具体表达形态、fixture 复算命令
- 8 个重写案例在 examples.md 中的排列顺序、小节标题措辞
- examples.md 顶部术语边界声明的具体文案长度与排版
- SKILL.md 禁词段新增句子的措辞
- 四文件旧术语扫清的 grep 脚本与替换规则表
- v1.0 回归 fixture 输入复算时采用的温度/种子约束（如需）

</decisions>

<canonical_refs>
## Canonical References

**Downstream agents MUST read these before planning or implementing.**

### 项目级约束
- `.planning/PROJECT.md` — v2.0 核心价值；Out of Scope（禁术语泄漏、只改 4 文件、不加 Action Items 表格）
- `.planning/REQUIREMENTS.md` §v2.0 Requirements / 兼容性 — COMP-01、COMP-02 两条
- `.planning/REQUIREMENTS.md` §v2.0 Requirements / 示例校准 — EXAM-01、EXAM-02、EXAM-03 三条
- `.planning/ROADMAP.md` §Phase 6 — Success Criteria 四条 + Upstream Carryover 五条（Phase 4 评审共识 HIGH/MEDIUM）

### 上游 Phase 决策
- `.planning/phases/03-scqa/03-CONTEXT.md` — Phase 3 SCQA 管线决策（D-04/D-05 XML 隔离、D-08/D-09 证据强度映射）
- `.planning/phases/04-pyramid/04-CONTEXT.md` — Phase 4 金字塔决策（D-01 合并三套模板、D-07 弹性层级、D-09 Case 8 作为 EXAM-02 落地、D-10 v1.0 非战略型案例兼容性留给 Phase 6）
- `.planning/phases/04-pyramid/04-REVIEWS.md` — Phase 4 跨 AI 评审共识，Phase 6 承接 HIGH carryover（Case 1-7 系统重写、Few-shot 污染防控）和 MEDIUM carryover（作者侧术语边界、跨文件一致性扫清）
- `.planning/phases/05-mece-so-what/05-CONTEXT.md` — Phase 5 校验决策（D-08 战略 > 归纳优先级已写 decision-rules.md §1、D-10 禁词已扩展、D-13 examples.md 零改动交 Phase 6、D-14 5 类 UAT 行为已验）
- `.planning/phases/05-mece-so-what/05-UAT.md` — Phase 5 UAT 脚本，Phase 6 的 06-UAT.md 承接其格式与风格

### 需修改的 skill 文件
- `skills/idea-to-task/SKILL.md` — 禁词段扩展一句 examples 作者侧边界说明（D-13）
- `skills/idea-to-task/references/decision-rules.md` — 扫清残留旧层级/模板术语（D-14）
- `skills/idea-to-task/references/output-template.md` — 扫清残留旧模板分类术语（D-14）
- `skills/idea-to-task/references/examples.md` — 顶部新增术语边界声明（D-12）；全量重写 Case 1-8（D-01/D-04）；融入 EXAM-01 / EXAM-03 对比（D-03）

### 需修改的 planning 文件
- `.planning/phases/06-examples-compat/06-UAT.md` — **新建**，承接 05-UAT.md 框架，新增 v1.0 回归段 + 端到端管线段（D-10/D-11）

### v1.0 回归基线（只读，不改）
- `tests/fixtures/idea-to-task/01-clear-direction.md` — 清晰指令型输入基线
- `tests/fixtures/idea-to-task/02-mixed-topics.md` — 混合主题输入基线
- `tests/fixtures/idea-to-task/03-high-risk-ambiguity.md` — 高风险模糊输入基线

</canonical_refs>

<code_context>
## Existing Code Insights

### Reusable Assets
- **05-UAT.md 框架**（Phase 5 D-14）：已建立 5 类行为输入 + 断言格式；06-UAT.md 直接继承此框架，只在其后追加「v1.0 回归段」和「端到端管线段」，不重造结构
- **Case 8 正反对比法**（Phase 4 D-09）：「非金字塔平铺 vs 金字塔分层」双样本对比已验证有效，作为 Case 1-7 重写模板；EXAM-01 和 EXAM-03 的正反对比直接复用该法
- **禁词扩展模式**（Phase 5 D-10）：SKILL.md 禁词段已扩容至 `mece_check / sowhat_filter / grouping / inductive / deductive`；D-13 的 examples 作者侧边界说明沿用同一位置
- **decision-rules.md §1 末尾战略 > 归纳优先级句**（Phase 5 D-08 已写入）：例子重写时战略型 Case 的选题可直接遵从此规则，无需新增判断逻辑
- **SCQA/MECE/So-what XML 内部推理范式**（Phase 3 D-04、Phase 5 D-01）：8 个重写案例可在作者侧注释中标注内部推理路径，但案例正文只呈现最终输出——与 D-12 的边界声明一致

### Established Patterns
- **「案例作为行为契约」纪律**（Phase 4 评审共识）：examples.md 是模型的主要 Few-shot 依据；输出结构的字面一致是核心验收点，重写必须端到端检视输出骨架
- **规则三处一致**（Phase 3 评审 takeaway）：Case 重写后，相关术语必须与 SKILL.md、decision-rules.md、output-template.md 字面一致；禁词 grep 做跨文件对齐的最后一道防线
- **懒加载参考**（SKILL.md 「何时读取参考文件」段）：examples.md 是按需读取而非全量加载，重写时需考虑新旧案例切换对 skill 上下文预算的影响
- **UAT 脚本作为行为断言**（Phase 5 D-14 落地）：06-UAT.md 继承这一模式，不把回归退化到人工对比层面

### Integration Points
- **examples.md 顶部**：D-12 术语边界声明的插入点；需在现有首段（如有）之前或替换式添加
- **examples.md §案例 1-8 主体**：D-01/D-02/D-04 全量重写的主战场；案例分隔符、小节命名与 v1.0 习惯兼容
- **SKILL.md 禁词段**：D-13 新增一句的插入点；位置与 Phase 5 D-10 相邻
- **06-UAT.md 新文件**：D-10 建立，与 05-UAT.md 同级；结构上可先分「第一部分：原 5 类行为复核（链接 05-UAT）」「第二部分：v1.0 回归段（D-11 三维断言）」「第三部分：端到端管线段（D-07 战略型 Case 管线追踪）」
- **旧术语扫清 grep 起点**：`rg -n '项目级|里程碑级|执行项级|战略型模板|归纳型模板|常规型模板|模板选择优先级|三套模板' skills/idea-to-task/`，结果作为 D-14 的处理清单

</code_context>

<specifics>
## Specific Ideas

- 用户明确表示 Case 1-7 要「全量重写 + 替换新素材」，这意味着不需要考虑「保留旧输入、降低疑惑度」的折衷方案；重写自由度高，可直接按新咨询管线 SOP 选题
- 用户明确三维断言作为「不退化」的判断标准：结构 + 禁词 + 输入类型未被硬扣；无需额外构造多维 rubric
- 用户要求 examples.md 顶部 和 SKILL.md 禁词段 双重写术语边界声明，用意是防止未来的 grep 式验收脚本对作者侧术语产生误报——这是 Phase 6 的一个隐性质量约束
- 战略型 Case 承担端到端演示 + 战略型 UAT 分类两个角色，Case 注释需要清楚标注这一双重身份，避免 plan-phase 时被当成普通 Case 处理
- 四文件旧术语扫清的第一次扫描发现结果可能影响 D-14 的替换清单；plan-phase 阶段应把这次扫描作为独立任务执行，产出物可进 06-UAT.md 附录

</specifics>

<deferred>
## Deferred Ideas

- **垂直问答关系检查（D1）、SCQA 变体适配（D3）、MECE 缺口标注（D4）** — REQUIREMENTS.md Future Requirements，v2.0 范围外
- **证据强度量化准则（强 = 3+业务维度；弱 = 单句口号）**— 由 Phase 6 重写案例素材间接锚定，不以独立规则形式落地
- **新增 skill 侧 fixture** — 本 phase 显式决策不新增；若未来发现行为 gap，归下一个 milestone
- **Action Items 表格输出** — PROJECT.md Out of Scope，Phase 6 继续遵守
- **多维详细 rubric** — 讨论中显式拒绝，保留三维断言

</deferred>

---

*Phase: 06-examples-compat*
*Context gathered: 2026-04-15*
