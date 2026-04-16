<div align="center">

[简体中文](README.md) · [English](README.en.md)

**idea-to-task: An AI Expert Instruction for Turning Fragmented Ideas into Strategic Task Trees.**

**Not just a simple summarization tool, but a consulting methodology engine integrating "Pyramid Principle + SCQA + MECE" to ensure high logical consistency from top-level strategy to bottom-level execution.**

[![GSD Powered](https://img.shields.io/badge/GSD-Framework-blueviolet?style=for-the-badge&logo=github)](https://github.com/gsd-build/get-shit-done)
[![License](https://img.shields.io/badge/license-MIT-blue?style=for-the-badge)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude-Code-black?style=for-the-badge&logo=anthropic)](https://www.anthropic.com/claude)

<br>

*"Make the CEO's fragmented ideas more than just ideas, but actionable roadmaps."*

<br>

**Adopted by multiple CTOs, Product Managers, and solo developers for 0-to-1 project planning and strategic decomposition.**

[Why I Built This](#why-i-built-this) · [How It Works](#how-it-works) · [Features](#features) · [Quick Start](#quick-start) · [User Guide](docs/USER-GUIDE.md)

</div>

---

## Why I Built This

When communicating with bosses, founders, or clients, what we get are often fragmented speech-to-text, casual meeting notes, or jumping strategic concepts.

Existing task decomposition tools are often just "flat lists"—you give them three ideas, they give you three headings with some sub-tasks underneath. They lack the **top-down induction** of intent and the **deep scanning** of logic gaps.

`idea-to-task` v2.0 is designed to solve this. By introducing thinking models from top-tier consulting firms, it identifies hidden relationships, removes noise, and builds a strategically layered task tree that follows the "Pyramid Principle."

---

## How It Works

`idea-to-task` is a general AI Skill that supports integration with multiple runtimes including Claude Code, Codex, Antigravity, OpenCode, and OpenClaw.

### Core Methodology Pipeline

1.  **SCQA Inference**: AI automatically deduces "Situation (S), Complication (C), Question (Q), Answer (A)" based on the input to clarify the business context. It asks precise follow-up questions instead of guessing when information is insufficient.
2.  **Evidence Strength Mapping**: Dynamically adjusts the depth of the task tree (2-4 levels) based on the certainty of the input sources.
3.  **Pyramid Layered Construction**: Starting from a single top-level conclusion (Center Point), it expands downwards into strategic pillars and key tasks.
4.  **MECE Quad-Check**: Mandates internal "Mutually Exclusive, Collectively Exhaustive" checks to prevent logical overlaps or omissions.
5.  **So-what Hollow Filtering**: Automatically filters out meaningless descriptive hollows like "strengthen collaboration" or "optimize experience," ensuring every task is actionable.

---

## Features

- **Six-section Structured Output**: Core Judgment → Theme Breakdown → Layered Task Tree → Execution Suggestions → Risk & High-risk Inference → Next Actions.
- **Chinese Native Optimization**: Deeply adapted to metaphorical logic and expression habits in Chinese contexts.
- **Atomic Git Commit Support**: Deeply integrated with GSD, supporting independent commits and tracking for each task item.
- **Strict Prohibition & Boundary Control**: Ensures output is professional, calm, and "anti-AI" styled.

---

## Quick Start

### Installation

<!--
Option 1: One-click install (recommended)
Visit [skills.sh](https://skills.sh/) and follow the prompts.
-- Hidden until this skill is indexed on skills.sh --
-->

Option 1: CLI install (recommended)
```bash
npx skills add https://github.com/Billin9/idea-to-task --skill idea-to-task
```

Option 2: Manual install

```bash
# Clone
git clone https://github.com/Billin9/idea-to-task.git

# Copy to Claude Code skills directory
cp -r idea-to-task/skills/idea-to-task ~/.claude/skills/
```

No extra dependencies — works out of the box.

### Usage

Call it directly in Claude Code or Antigravity:

```text
/idea-to-task "Here are some of my thoughts: We're making an AI live-streaming assistant. First, we need to handle video generation, then scripts, and it should be able to auto-post to TikTok. Oh, and we don't have money for models right now, so we need to use digital humans."
```

---

## Tech Stack

- **Instruction Engineering**: Advanced Markdown + XML structured prompts
- **Compatible Runtimes**: Claude Code, Codex, Gemini, Antigravity, OpenCode, OpenClaw, and other AI assistants (the skill itself is pure prompt — no runtime required)
- **Development Toolchain**: Python (uv) for skill structure validation; Node.js only for the bundled GSD workflow scripts — end users don't need to install it
- **Copywriting Standard**: Consulting industry standard (McKinsey Style)

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

<div align="center">

**Ideas themselves are cheap; ideas that can be implemented are valuable.**

</div>
