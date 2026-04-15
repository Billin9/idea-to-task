# Phase 6: 示例校准与兼容性验证 - Discussion Log

> **Audit trail only.** Do not use as input to planning, research, or execution agents.
> Decisions are captured in CONTEXT.md — this log preserves the alternatives considered.

**Date:** 2026-04-15
**Phase:** 06-examples-compat
**Areas discussed:** Case 1-7 改造策略, 端到端验证载体, v1.0 回归基准定义, 旧术语一致性扫清

---

## 灰区选择

| Option | Description | Selected |
|--------|-------------|----------|
| Case 1-7 改造策略 | Few-shot 污染 HIGH 风险，全量重写/过渡缓冲/分批重写/保留部分 之间取舍 | ✓ |
| EXAM-01 + EXAM-03 案例载体 | SCQA 与 MECE 各 1 组正反对比，独立/嵌入/综合 | (在 Case 1-7 区域讨论中解决) |
| 端到端验证载体 | Success Criteria 4 端到端管线演示位置 | (后续讨论中选中) |
| v1.0 回归基准定义 | Success Criteria 2 不退化判断标准 | (后续讨论中选中) |

**首轮用户选择：** 只勾选「Case 1-7 改造策略」；首轮后用户同意进入更多灰区讨论。

---

## Case 1-7 改造策略

### 总体策略

| Option | Description | Selected |
|--------|-------------|----------|
| 全量重写 | 7 个案例按新方法论重写；与 v2.0 方向一致，一劳永逸 | ✓ |
| 过渡缓冲+指示 | Case 1-7 加 Legacy 前缀 + SKILL.md 指示优先 Case 8 | |
| 分批重写 | 只重写冲突严重的案例，简单保留 | |
| 删 1-7 只留 Case 8 | 最彻底但案例多样性消失 | |

**User's choice:** 全量重写
**Notes:** 用户直接选择最彻底方案，与 v2.0 milestone 的「全面重构」方向一致

### 输入素材处理

| Option | Description | Selected |
|--------|-------------|----------|
| 保留原输入 | 只重写输出，同输入下展示 v1.0→v2.0 差异 | |
| 替换为新素材 | 按新管线 SOP 重新选题 | ✓ |
| 混合策略 | 多数保留，少数替换 | |

**User's choice:** 替换为新素材
**Notes:** 用户授予重写时的选题自由度，不再受旧输入形态束缚

### EXAM-01 / EXAM-03 融合方式

| Option | Description | Selected |
|--------|-------------|----------|
| 融入现有重写案例 | 从 8 个重写案例中抽两个分别承担 SCQA 对比和 MECE 对比 | ✓ |
| 新增 Case 9 + Case 10 | 独立新增两个专项对比案例 | |
| 合并为综合 Case 11 | 单个案例同时展示三维对比 | |

**User's choice:** 融入现有重写案例（案例总数保持 8 不变）
**Notes:** 保持 Few-shot 总量平衡，不让新增案例再次打破比例

### 作者侧旧术语处理

| Option | Description | Selected |
|--------|-------------|----------|
| 全面清理+显式边界声明 | 删除作者侧旧术语 + 显式声明作者侧/模型输出禁词边界 | ✓ |
| 只清理不声明 | 只删旧术语，不加边界说明 | |
| 只声明不清理 | 新增声明，旧术语保留 | |

**User's choice:** 全面清理 + 显式边界声明

### 选题矩阵

| Option | Description | Selected |
|--------|-------------|----------|
| 对齐 Phase 5 UAT 5 类 + 3 个新增封闭点 | 战略/归纳/常规/中等三层/极弱两层 + Case 8 金字塔 + SCQA 对比 + MECE 对比 | ✓ |
| 按输入领域多样化 | 产品/运营/组织/财务等业务领域覆盖 | |
| 按证据强度梯度 | 强 x3 / 中 x3 / 弱 x2 | |

**User's choice:** 对齐 Phase 5 UAT 5 类 + 3 个新增封闭点
**Notes:** 与 Phase 5 UAT 对齐可复用验证维度，不重造

### Case 8 处理

| Option | Description | Selected |
|--------|-------------|----------|
| 同步重写 | 按新素材方向和统一风格一并重写 Case 8 | ✓ |
| 保留 Case 8 不动 | Phase 4 D-09 基线保留 | |

**User's choice:** 同步重写（保留正反对比法，但素材+风格对齐其他 7 个）

### 术语边界声明位置

| Option | Description | Selected |
|--------|-------------|----------|
| examples.md 顶部 + SKILL.md 禁词段都填 | 双重保障，防止 grep 验收脚本自撞 | ✓ |
| 只在 examples.md 顶部 | 简洁但 SKILL.md 禁词段可能被误读 | |
| 只在 SKILL.md 禁词段 | examples.md 读者看不到 | |

**User's choice:** examples 顶部 + SKILL.md 禁词段双重声明

---

## 端到端验证载体

| Option | Description | Selected |
|--------|-------------|----------|
| 8 个重写 Case 中的战略型 Case | 作为 Case 内嵌演示点，案例注释标注双重身份 | ✓ |
| 新增 Case 9 专用端到端案例 | 违反「案例总数 8」约束 | |
| 写成 06-UAT.md 扩展文档 | 位置合理但离用户远 | |
| Case + UAT 双重 | 双防控但成本高 | |

**User's choice:** 战略型 Case 内嵌承担端到端演示
**Notes:** 既满足 Success Criteria 4，又不打破「案例总数不变」约束

---

## v1.0 回归基准定义

### 回归载体

| Option | Description | Selected |
|--------|-------------|----------|
| 06-UAT.md 叠加 v1.0 回归段 | 继承 Phase 5 UAT 框架 | ✓ |
| 原地 fixture 加断言清单 | 改 fixture 文件本身 | |
| 人工对比签收 | 不写断言脚本 | |

**User's choice:** 06-UAT.md 叠加 v1.0 回归段

### 不退化阈值

| Option | Description | Selected |
|--------|-------------|----------|
| 三维断言：结构 + 禁词 + 未硬扣输入类型 | 简洁且可 grep | ✓ |
| 多维 rubric 评分 | 精度高但 Phase 6 不应花中心资源 | |
| 「符合原 fixture 期望行为」整体判断 | 简单但可重复性差 | |

**User's choice:** 三维断言

---

## 旧术语一致性扫清

| Option | Description | Selected |
|--------|-------------|----------|
| 四文件全扫统一替换 + 保留历史白名单 | 一次性到位 | ✓ |
| 只扫 examples.md 和残留表述 | 成本低但可能漏权杖 | |
| grep 规则加入 06-UAT.md 大夫 | 验收驱动但不主动清理 | |

**User's choice:** 四文件全扫统一替换 + 保留历史白名单

---

## 结束确认

| Option | Description | Selected |
|--------|-------------|----------|
| 准备好写 CONTEXT | 四灰区已覆盖所有 Success Criteria 和 Phase 4 MEDIUM carryover | ✓ |
| 再探索新灰区 | | |

**User's choice:** 准备好写 CONTEXT

---

## Claude's Discretion

- 06-UAT.md 内部章节切分、断言脚本的具体表达形态
- 8 个重写案例在 examples.md 中的排列顺序和小节标题措辞
- examples.md 顶部术语边界声明的具体文案长度与排版
- SKILL.md 禁词段新增句子的措辞
- 四文件旧术语扫清的 grep 脚本与替换规则表
- v1.0 回归 fixture 输入复算时采用的温度/种子约束

## Deferred Ideas

- 垂直问答关系检查（D1）、SCQA 变体适配（D3）、MECE 缺口标注（D4）
- 证据强度量化准则（显式规则化）
- 新增 skill 侧 fixture
- Action Items 表格输出
- 多维详细 rubric
