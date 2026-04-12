# Codebase Concerns

**Analysis Date:** 2026-04-12

## Tech Debt

**validate_skill.py 仅覆盖结构校验，无行为测试:**
- Issue: `skills/idea-to-task/scripts/validate_skill.py` 只做静态结构校验（frontmatter 字段、章节存在、引用文件存在），不验证 skill 的实际推理行为是否符合预期。fixture 文件 `tests/fixtures/idea-to-task/` 目前只有期望行为描述（`## 期望行为` 文本），没有任何自动化断言执行它们。
- Files: `skills/idea-to-task/scripts/validate_skill.py`, `tests/fixtures/idea-to-task/01-clear-direction.md`, `tests/fixtures/idea-to-task/02-mixed-topics.md`, `tests/fixtures/idea-to-task/03-high-risk-ambiguity.md`
- Impact: Skill 行为退化无法被自动检测到，只能靠人工运行并主观判断输出。
- Fix approach: 为每个 fixture 添加结构化期望字段（如 `expected_sections`, `expected_path_count`），并扩展 `validate_skill.py` 或新增测试脚本通过 LLM 调用验证输出结构。

**examples.md 内容高度抽象，缺乏真实输出示例:**
- Issue: `skills/idea-to-task/references/examples.md` 只有 4 个案例描述，每个案例仅给出输入类型和处理方式的一句话说明，没有任何真实的完整输出样本。这导致该文件在"校准风格或边界"上实际价值有限。
- Files: `skills/idea-to-task/references/examples.md`
- Impact: 模型调用该文件时得不到足够的行为锚点，风格和输出精度依赖对 SKILL.md 主文档的理解，边界场景行为不稳定。
- Fix approach: 每个案例补充一个完整的真实或合成输出示例，至少覆盖"双路径输出"和"证据不足停在里程碑级"两个场景。

**GSD 框架文件（`.claude/`、`.agent/`）与 skill 业务代码混合在同一仓库:**
- Issue: 项目根目录同时包含 idea-to-task skill 本体（`skills/`）和 GSD 工作流框架（`.claude/get-shit-done/`、`.agent/`、`.codex/`），两者职责完全不同，但没有任何边界文档说明哪些是"本项目核心资产"，哪些是"框架基础设施"。
- Files: `skills/`, `.claude/get-shit-done/`, `.agent/`, `.codex/`
- Impact: 新贡献者难以区分"修改 skill"和"修改 GSD 框架"，错误修改框架文件可能影响所有使用 GSD 的项目。
- Fix approach: 在根目录 README 中明确说明目录职责分层；将 `.agent/` 和 `.codex/` 标注为框架安装目录，避免直接手动修改。

**`.DS_Store` 文件出现在多个目录且已被 `.gitignore` 追踪:**
- Issue: `.gitignore` 已声明忽略 `.DS_Store`，但 `skills/`、`tests/`、`docs/` 子目录内的 `.DS_Store` 文件在初始提交时已经被跟踪进入 git 历史（文件存在于磁盘）。
- Files: `skills/idea-to-task/.DS_Store`, `tests/.DS_Store`, `docs/.DS_Store`
- Impact: 可能导致跨平台协作时出现无意义的 git diff 噪音（若文件已被提交）。
- Fix approach: 运行 `git rm -r --cached "*.DS_Store"` 从 git 追踪中移除，确认 `.gitignore` 全局生效。

## Known Bugs

**validate_skill.py 的 fixture 路径计算依赖脆弱的相对目录结构:**
- Symptoms: `strict` 模式下，fixture 目录通过 `skill_dir.parent.parent / "tests" / "fixtures" / skill_dir.name` 计算，这要求 skill 必须位于 `skills/<skill-name>/` 的两层目录结构中。
- Files: `skills/idea-to-task/scripts/validate_skill.py` (line 75)
- Trigger: 若将 skill 目录移动到 `skills/category/idea-to-task/` 或直接放在根目录，路径计算失败，不会抛出有意义的错误，而是静默判断 fixture 不存在。
- Workaround: 当前 skill 结构符合预期，不触发该问题；但扩展时需注意。

**gsd-validate-commit.sh 只能解析 `-m "..."` 单行消息，无法解析 HEREDOC:**
- Symptoms: commit message 通过 HEREDOC 传入时（如 `git commit -m "$(cat <<'EOF' ... EOF)"`），正则 `[[ "$CMD" =~ -m[[:space:]]+\"([^\"]+)\" ]]` 在 shell 展开后无法匹配多行内容，`MSG` 为空，hook 直接放行而不校验。
- Files: `.claude/hooks/gsd-validate-commit.sh` (lines 27-32)
- Trigger: 使用 HEREDOC 方式提交时，即使消息格式不符合 Conventional Commits 也不会被拦截。
- Workaround: Hook 为 opt-in（需要 `.planning/config.json` 中设置 `hooks.community: true`），当前项目未启用，影响有限。

## Security Considerations

**validate_skill.py 通过 `Path.resolve()` 校验引用文件路径，但未限制路径范围:**
- Risk: `extract_reference_paths` 提取 SKILL.md 内所有相对链接，通过 `(skill_dir / rel_path).resolve()` 转为绝对路径后检查是否存在。若 SKILL.md 中包含类似 `../../../etc/passwd` 的链接，脚本会尝试 `resolve()` 并检查该路径是否存在，但不会读取内容。当前行为仅为文件存在性检查，无信息泄露风险。
- Files: `skills/idea-to-task/scripts/validate_skill.py` (lines 32-37, 65-68)
- Current mitigation: 脚本只做 `target.exists()` 检查，不读取文件内容，风险低。
- Recommendations: 添加路径范围校验，确保所有解析后的引用路径在 skill 目录内，拒绝路径穿越。

**gsd-workflow-guard.js 依赖 `data.tool_input?.is_subagent` 字段判断上下文:**
- Risk: `is_subagent` 字段不是 Claude SDK 的标准字段，实际上该字段在正常工具调用中不存在，因此 guard 在子 agent 场景中无法可靠地跳过检查。
- Files: `.claude/hooks/gsd-workflow-guard.js` (line 35)
- Current mitigation: Hook 为 opt-in（需要 `config.hooks.workflow_guard: true`），当前项目未启用。
- Recommendations: 改用 session 上下文中可靠的标识方式，或移除该检查依赖。

## Performance Bottlenecks

**gsd-read-guard.js 和 gsd-workflow-guard.js 对每次 Write/Edit 都触发同步文件系统访问:**
- Problem: 两个 PreToolUse hook 在每次 Write/Edit 调用前都会同步读取配置文件（`fs.accessSync`、`fs.readFileSync`）和检查文件存在性，在高频编辑场景中累积延迟。
- Files: `.claude/hooks/gsd-read-guard.js` (line 46), `.claude/hooks/gsd-workflow-guard.js` (lines 63-70)
- Cause: 无缓存机制，每次 hook 调用独立进程，无法跨调用共享状态。
- Improvement path: 由于每次 hook 调用是独立进程，优化空间有限；可通过减少不必要的配置文件读取（先检查快速条件再读文件）来降低平均耗时。目前已有 3 秒 stdin timeout 保护，不会无限阻塞。

## Fragile Areas

**SKILL.md 中"何时读取参考文件"章节依赖模型主动判断，无强制触发机制:**
- Files: `skills/idea-to-task/SKILL.md` (lines 63-67)
- Why fragile: 参考文件（`decision-rules.md`、`output-template.md`、`examples.md`）的加载完全依赖模型读取 SKILL.md 后自行决定何时调用 Read 工具。不同模型、不同上下文长度压力下，参考文件可能被跳过，导致输出格式或决策逻辑偏离预期。
- Safe modification: 修改 SKILL.md 时，确保"何时读取"的条件描述足够明确具体，避免模糊触发条件。
- Test coverage: 无自动化验证，完全依赖人工评测。

**output-template.md 与 SKILL.md 的输出结构描述存在轻微冗余，维护时易不同步:**
- Files: `skills/idea-to-task/SKILL.md` (lines 32-33, 55-61), `skills/idea-to-task/references/output-template.md`
- Why fragile: 两个文件都描述了六段式输出结构，若修改其中一个（如增加第七段）而忘记同步另一个，模型可能从两个来源得到矛盾指令。
- Safe modification: 将 SKILL.md 中的输出结构说明改为只引用 `output-template.md`，不重复定义。
- Test coverage: 无。

**openai.yaml 中 `default_prompt` 硬编码了 `$idea-to-task` 调用语法:**
- Files: `skills/idea-to-task/agents/openai.yaml` (line 4)
- Why fragile: 若 skill 名称或调用约定变更，该字段需要手动同步，`validate_skill.py` 不会校验该文件内容的一致性。
- Safe modification: 修改 skill name 时同步更新此文件。
- Test coverage: `validate_skill.py` 在 strict 模式下只检查该文件是否存在，不验证内容。

## Scaling Limits

**Fixture 驱动测试不支持自动化 LLM 回归:**
- Current capacity: 3 个 fixture 文件，纯文档描述，手动验证。
- Limit: 无法在 CI/CD 中自动回归，随着 skill 版本迭代，历史场景行为无法保证。
- Scaling path: 引入结构化 fixture 格式（JSON/YAML），配合 LLM 评估脚本，支持批量回归测试。

**GSD 框架版本（1.34.2）与 skill 版本无显式绑定:**
- Current capacity: `.claude/get-shit-done/VERSION` 记录框架版本，skill 本身无版本字段。
- Limit: 若框架升级引入破坏性变更（如 hook API 变更），无法快速定位 skill 与框架的兼容性边界。
- Scaling path: 在 `skills/idea-to-task/SKILL.md` frontmatter 中增加 `min_gsd_version` 字段，`validate_skill.py` 增加兼容性检查。

## Dependencies at Risk

**pyyaml 版本约束过宽（`pyyaml<7`）:**
- Risk: `validate_skill.py` 的 inline metadata 声明 `pyyaml<7`，没有下界约束，可能拉取到较老版本。
- Files: `skills/idea-to-task/scripts/validate_skill.py` (line 3)
- Impact: pyyaml 旧版本在解析某些 YAML 格式时行为不一致，可能导致 frontmatter 解析结果异常。
- Migration plan: 将约束收紧为 `pyyaml>=6,<7`，锁定主版本。

## Missing Critical Features

**无 CI 流水线:**
- Problem: 项目没有 `.github/workflows/`、`Makefile` 或任何 CI 配置，`validate_skill.py` 只能手动运行。
- Blocks: 无法在 PR 合并时自动校验 skill 结构完整性，结构错误可能直接进入主分支。

**无版本控制策略用于 skill 内容迭代:**
- Problem: SKILL.md、decision-rules.md、output-template.md 无版本号，无 CHANGELOG，无法追踪 skill 行为变更历史。
- Blocks: 多人协作时无法知道哪次修改改变了什么行为，也无法回滚到历史版本行为。

## Test Coverage Gaps

**fixture 文件仅描述期望行为，无断言:**
- What's not tested: 实际 LLM 输出是否包含正确的段落结构、是否触发双路径输出、是否在证据不足时停在里程碑级。
- Files: `tests/fixtures/idea-to-task/01-clear-direction.md`, `tests/fixtures/idea-to-task/02-mixed-topics.md`, `tests/fixtures/idea-to-task/03-high-risk-ambiguity.md`
- Risk: skill 逻辑退化（如对高风险歧义输入不再给出双路径）无法被检测到。
- Priority: High

**validate_skill.py 的路径穿越保护未被测试:**
- What's not tested: 当 SKILL.md 包含 `../` 相对路径链接时，validate_skill.py 的行为。
- Files: `skills/idea-to-task/scripts/validate_skill.py`
- Risk: 路径穿越场景下行为未定义。
- Priority: Low

**gsd-validate-commit.sh 的 HEREDOC 场景未被测试:**
- What's not tested: 多行 commit message 通过 HEREDOC 传入时，hook 是否正确校验格式。
- Files: `.claude/hooks/gsd-validate-commit.sh`
- Risk: 绕过 Conventional Commits 格式校验。
- Priority: Low（功能为 opt-in，当前未启用）

---

*Concerns audit: 2026-04-12*
