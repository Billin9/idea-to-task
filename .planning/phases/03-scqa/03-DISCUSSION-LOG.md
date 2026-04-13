# Phase 3: SCQA 输入解析层 - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-04-14
**Phase:** 03-SCQA 输入解析层
**Mode:** batch
**Areas discussed:** 工作流位置, 内部推理格式, 追问触发规则, 证据强度映射

---

## 工作流位置

### Q1: SCQA 与战略型分流的关系

| Option | Description | Selected |
|--------|-------------|----------|
| a) 所有输入先走 SCQA | 战略型判断变成 SCQA 结果的后置推断 | |
| b) 保留战略型前置判断 | SCQA 只替换非战略路径的步骤 3-4 | |
| c) 你来决定 | | |

**User's choice:** 完全推翻现有工作流，使用为方法论设定的最佳 SOP
**Notes:** 用户没有从选项中选择，而是给出了更高层的指令——不受 v1.0 约束，完全重构

### Q2: 替换还是新增

| Option | Description | Selected |
|--------|-------------|----------|
| a) 替换步骤 2-4 | SCQA 同时完成战略判断、密度判断和可任务化判断 | |
| b) 新增一步 | 原步骤 2-4 保留但从 SCQA 取值 | |
| c) 你来决定 | | |

**User's choice:** 同上——完全重构，不受步骤编号束缚
**Notes:** Q1 的回答覆盖了 Q2 和 Q3

### Q3: 向上归纳检查的去留

| Option | Description | Selected |
|--------|-------------|----------|
| a) 保留 | 作为 SCQA 推演的互补验证 | |
| b) 移除 | SCQA 的 Answer 已完成归纳 | |
| c) 合并 | 合并进 SCQA 推演步骤 | |

**User's choice:** 由完全重构决策隐含——归纳检查合并进 SCQA 流程

---

## 内部推理格式

### Q4: 是否用 XML 标签隔离

| Option | Description | Selected |
|--------|-------------|----------|
| a) 用 XML 标签 | `<scqa_analysis>` 隔离推演，便于调试 | ✓ |
| b) 纯指令引导 | 不用标签，靠步骤顺序保证 | |
| c) 你来决定 | | |

**User's choice:** a) 用 XML 标签

### Q5: SCQA 四要素的输出呈现

| Option | Description | Selected |
|--------|-------------|----------|
| a) 四要素全隐藏 | 仅 Answer 以"核心判断"呈现 | ✓ |
| b) S+C 自然语言呈现 | Q+A 转化为核心判断 | |
| c) 你来决定 | | |

**User's choice:** a) 四要素全部隐藏

---

## 追问触发规则

### Q6: 追问触发的判断依据

| Option | Description | Selected |
|--------|-------------|----------|
| a) 连 S 都没有才追问 | 极保守 | |
| b) S 有但 C 完全缺失 | 中等 | |
| c) S+C 任一关键缺失 | 积极追问，确保推演质量 | ✓ |
| d) 你来决定 | | |

**User's choice:** c) S+C 任一关键缺失即追问

### Q7: 追问数量和形式

| Option | Description | Selected |
|--------|-------------|----------|
| a) 复用现有 2-5 个规则 | SCQA 追问计入总量 | |
| b) SCQA 追问独立精简 | 最多 2-3 个，与后续补问分开 | ✓ |
| c) 你来决定 | | |

**User's choice:** b) SCQA 追问独立且精简

### Q8: 补问规则章节结构

| Option | Description | Selected |
|--------|-------------|----------|
| a) 替换现有第 5 节 | 统一为 SCQA 完整度追问 | |
| b) 新增独立章节 | 与现有第 5 节并存 | |
| c) 你来决定 | | |

**User's choice:** c) Claude's discretion

---

## 证据强度映射

### Q9: 映射粒度

| Option | Description | Selected |
|--------|-------------|----------|
| a) 三档沿用 | S→弱, S+C→中, 四要素齐全→强 | |
| b) 四档细化 | S→弱, S+C→中低, S+C+Q→中高, 齐全→强 | |
| c) 你来决定 | | |

**User's choice:** 完全按方法论最佳实践重构，不受三档束缚
**Notes:** 用户表示证据强度机制"完全看方法论是否需要，如果不需要可以推翻"

### Q10: 与层级深度的对应

| Option | Description | Selected |
|--------|-------------|----------|
| a) 沿用三档 | Phase 4 在此基础上加弹性控制 | |
| b) Phase 3 只建映射 | 深度控制留给 Phase 4 | |
| c) 你来决定 | | |

**User's choice:** 同上——由方法论决定

---

## Claude's Discretion

- decision-rules.md 中 SCQA 追问规则的章节结构和位置
- SCQA 推演步骤的具体内部编排顺序
- XML 标签的具体命名和嵌套结构

## Deferred Ideas

None
