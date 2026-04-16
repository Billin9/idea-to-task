<div align="center">

[简体中文](README.md) · [English](README.en.md)

**idea-to-task: 将碎片想法转化为战略级任务树的 AI 专家指令。**

**它不仅是简单的归纳工具，更是集成「金字塔原理 + SCQA + MECE」的咨询方法论引擎，确保从顶层战略到底层执行的高逻辑一致性。**

[![GSD Powered](https://img.shields.io/badge/GSD-Framework-blueviolet?style=for-the-badge&logo=github)](https://github.com/gsd-build/get-shit-done)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude-Code-black?style=for-the-badge&logo=anthropic)](https://www.anthropic.com/claude)

<br>

*"让老板的碎片想法不仅仅是想法，而是可落地的路线图。"*

<br>

**已被多位 CTO、产品经理和个人开发者用于从 0 到 1 的项目规划与战略拆解。**

[我为什么做这个](#我为什么做这个) · [它是怎么工作的](#它是怎么工作的) · [核心特性](#核心特性) · [快速开始](#快速开始) · [用户指南](docs/USER-GUIDE.md)

</div>

---

## 我为什么做这个

在与老板、创始人或客户沟通时，我们拿到的往往是破碎的语音转文字、随手的会议记录或跳跃的战略构想。

市面上的任务拆解工具往往只是简单的「平铺直叙」——你给它三个想法，它给你三个标题，下面随便挂点子任务。它们缺少对意图的**向上归纳**，也缺少对逻辑缺口的**深度扫描**。

`idea-to-task` v2.0 旨在解决这个问题。通过引入顶级咨询公司的思维模型，它能识别隐藏的包含关系，剔除垃圾信息，并构建出一套符合「金字塔原理」的战略分层任务树。

---

## 它是怎么工作的

`idea-to-task` 是一个通用的 AI Skill，集成支持 Claude Code、Codex、Gemini、Antigravity、OpenCode、OpenClaw 等多种运行时。

### 核心方法论管线

1. **SCQA 内部推演**：AI 自动基于输入推演「情境 (S)、冲突 (C)、问题 (Q)、回答 (A)」，理清业务脉络。信息不足时，会精准追问而非猜测。
2. **证据强度映射**：根据输入来源的确定性，动态调整任务树的深度（2-4 层）。
3. **金字塔分层构建**：从唯一的顶层结论（Center Point）出发，向下分层展开战略支柱和关键任务。
4. **MECE 四维校验**：内部强制执行「相互独立，完全穷尽」校验，防止逻辑重叠或遗漏。
5. **So-what 空洞过滤**：自动剔除诸如「加强协作」、「优化体验」等无意义的描述性空洞，确保每一项任务都是可执行的。

---

## 核心特性

- **六段式结构化输出**：核心判断 → 主题拆分 → 分层任务树 → 执行建议 → 风险与高风险推断 → 下一步动作。
- **中文原生优化**：深度适配中文语境下的隐喻逻辑与表达习惯。
- **严谨的禁词与边界控制**：确保输出专业、冷静、去 AI 化。

---

## 快速开始

### 安装

<!--
方式一：一键安装（推荐）
访问 [skills.sh](https://skills.sh/) 页面，按提示一键安装。
-- 尚未上架 skills.sh，待被索引后再恢复此段 --
-->

方式一：命令行安装（推荐）
```bash
npx skills add https://github.com/Billin9/idea-to-task --skill idea-to-task
```

方式二：手动安装

```bash
# 克隆
git clone https://github.com/Billin9/idea-to-task.git

# 复制到 Claude Code 的 skills 目录
cp -r idea-to-task/skills/idea-to-task ~/.claude/skills/
```

无需额外依赖，开箱即用。

### 使用

在 Claude Code 或者 OpenClaw 中直接调用：

```bash
/idea-to-task 「这是我的一些想法：我们要做一个 AI 带货助手，首先要搞定视频生成，然后是脚本，还要能自动发抖音。对了，目前咱们没钱请模特，得用数字人。」
```

---

## 技术栈

- **指令工程**：高级 Markdown + XML 结构化提示词
- **兼容运行时**：Claude Code、Codex、Gemini、Antigravity、OpenCode、OpenClaw 等 AI 助手（skill 本身为纯 Prompt，无需额外运行时）
- **开发工具链**：Python (uv) 用于 skill 结构校验；Node.js 仅用于本仓库集成的 GSD 工作流脚本，使用者无需安装
- **文案规范**：咨询行业标准 (McKinsey Style)

---

## 许可证

本项目采用 MIT 许可证。详见 [LICENSE](LICENSE) 文件。

---

<div align="center">

**想法本身不值钱，能落地的想法才值钱。**

</div>
