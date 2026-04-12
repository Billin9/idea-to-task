# Requirements: idea-to-task 输出质量优化

**Defined:** 2026-04-12
**Core Value:** 输出必须先归纳出统一顶层意图，再向下展开子任务线

## v1 Requirements

### 判断逻辑

- [ ] **JUDGE-01**: 在主题拆分前新增「向上归纳」判断步骤 — 检测所有识别出的意图是否能收敛为一个统一顶层意图，如果能则收敛为单主题
- [ ] **JUDGE-02**: 核心判断必须先输出 CEO 真正想做的那一件事（顶层意图），再展开子线，不再直接列出多条并列主线

### 输出结构

- [ ] **OUT-01**: 核心判断模板改为「一句话顶层意图 + 子线展开」结构
- [ ] **OUT-02**: 主题拆分支持「单顶层主题 + 子任务线」模式 — 当检测到包含关系时，不拆成并列主题
- [ ] **OUT-03**: 任务树模板增加归纳路径 — 被包含的子主题降级为顶层主题下的里程碑或子任务线

### 示例校准

- [ ] **EX-01**: 补充正反对比案例 — 同一输入分别展示「平铺输出」（错误）和「归纳输出」（正确），让模型对齐期望行为

## v2 Requirements

(无)

## Out of Scope

| Feature | Reason |
|---------|--------|
| 新增输入类型支持 | 本次只改输出质量，不扩展输入能力 |
| 交互式追问流程改造 | 不在本次范围 |
| 与其他工具联动集成 | 不在本次范围 |
| skill 触发条件/描述优化 | 不在本次范围 |

## Traceability

| Requirement | Phase | Status |
|-------------|-------|--------|
| JUDGE-01 | TBD | Pending |
| JUDGE-02 | TBD | Pending |
| OUT-01 | TBD | Pending |
| OUT-02 | TBD | Pending |
| OUT-03 | TBD | Pending |
| EX-01 | TBD | Pending |

**Coverage:**
- v1 requirements: 6 total
- Mapped to phases: 0
- Unmapped: 6 ⚠️

---
*Requirements defined: 2026-04-12*
*Last updated: 2026-04-12 after initial definition*
