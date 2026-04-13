# Requirements: idea-to-task v2.0 咨询方法论重构

**Defined:** 2026-04-14
**Core Value:** 输出必须用金字塔原理从顶层结论出发，向下分层展开战略支柱和关键任务，确保逻辑严密、不重不漏

## v2.0 Requirements

### SCQA 输入解析

- [ ] **SCQA-01**: AI 能从碎片输入中推演 Situation（背景）和 Complication（矛盾/变化）
- [ ] **SCQA-02**: AI 能从 S+C 推导隐含 Question，并基于全局推演 Answer（核心判断）作为金字塔顶点
- [ ] **SCQA-03**: 当 SCQA 中关键要素完全缺失且影响方向判断时，触发最少量定向追问，与现有补问规则融合
- [ ] **SCQA-04**: SCQA 完整度与证据强度关联——四要素齐全为强证据，S+C 有但 Q/A 需推演为中等，仅有 S 为弱证据

### 金字塔输出

- [ ] **PYMD-01**: 输出从顶层结论（SCQA 的 Answer）出发，向下分层展开战略支柱→关键任务
- [ ] **PYMD-02**: 弹性层级控制——每层 2-4 个支撑点，层级深度随证据强度伸缩（弱=2层，中=3层，强=4层）
- [ ] **PYMD-03**: 统一金字塔模板替代现有战略型/归纳型/常规型三套模板，消除分叉逻辑
- [ ] **PYMD-04**: 保持现有树形输出格式（核心判断→主题拆分→分层任务树→执行建议→风险→下一步）

### 内部质量校验

- [ ] **QUAL-01**: MECE 内部校验——检查同层分支互斥性、完备性、分组数量（2-4）和分组逻辑一致性
- [ ] **QUAL-02**: So-what 内部过滤——剔除五类空洞模式（无主语口号、无对象动作、无验收里程碑、父子重复、无法行动描述）
- [ ] **QUAL-03**: 归纳/演绎分组标记——AI 内部标记水平支撑点的分组逻辑类型，辅助选择正确分组方式

### 兼容性

- [ ] **COMP-01**: 现有非战略型输入处理逻辑不被破坏，v1.0 fixture 作为回归基线
- [ ] **COMP-02**: 能复用的 fixture 和 examples 保留，不兼容的按新方法论重写

### 示例校准

- [ ] **EXAM-01**: 为 SCQA 解析提供至少 1 组正反对比案例（无 SCQA 分析的平铺 vs 有 SCQA 的结构化）
- [ ] **EXAM-02**: 为金字塔结构提供至少 1 组正反对比案例（非金字塔 vs 金字塔输出）
- [ ] **EXAM-03**: 为 MECE 检查提供至少 1 组正反对比案例（有重叠遗漏 vs 不重不漏）

## Future Requirements

### 高级功能

- **D1**: 垂直问答关系检查——父节点必须是子节点的 "所以呢" 总结
- **D3**: SCQA 变体适配——支持 SCA/CSA 简化变体
- **D4**: MECE 缺口标注——遗漏检测时在风险区标注提醒

## Out of Scope

| Feature | Reason |
|---------|--------|
| Action Items 表格输出 | 保持任务树格式一致性，PROJECT.md 明确排除 |
| 向用户暴露 SCQA/MECE/So-what 过程 | 用户只关心结果质量，不关心生产过程 |
| 四要素逐一追问 | 违反"只补显著改变方向的问题"原则 |
| 方法论术语进入用户输出 | CEO 不是咨询顾问，术语增加认知负担 |
| 新增输入类型支持 | 只改工作流和输出逻辑 |
| 僵硬 3x3 硬约束 | 现实输入复杂度不均匀，2-4 皆可 |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| SCQA-01 | — | Pending |
| SCQA-02 | — | Pending |
| SCQA-03 | — | Pending |
| SCQA-04 | — | Pending |
| PYMD-01 | — | Pending |
| PYMD-02 | — | Pending |
| PYMD-03 | — | Pending |
| PYMD-04 | — | Pending |
| QUAL-01 | — | Pending |
| QUAL-02 | — | Pending |
| QUAL-03 | — | Pending |
| COMP-01 | — | Pending |
| COMP-02 | — | Pending |
| EXAM-01 | — | Pending |
| EXAM-02 | — | Pending |
| EXAM-03 | — | Pending |

**Coverage:**
- v2.0 requirements: 16 total
- Mapped to phases: 0
- Unmapped: 16 ⚠️

---
*Requirements defined: 2026-04-14*
*Last updated: 2026-04-14 after initial definition*
