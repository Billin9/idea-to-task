#!/usr/bin/env -S uv run
# /// script
# dependencies = ["pyyaml<7"]
# ///
from __future__ import annotations

import argparse
import re
from pathlib import Path

import yaml

REQUIRED_SECTIONS = [
    "## 适用场景",
    "## 核心原则",
    "## 工作流",
    "## 补问规则",
    "## 输出结构",
]


def read_frontmatter(text: str) -> dict:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    if not match:
        raise ValueError("SKILL.md 缺少合法的 YAML frontmatter")
    data = yaml.safe_load(match.group(1))
    if not isinstance(data, dict):
        raise ValueError("frontmatter 必须是字典")
    return data


def extract_reference_paths(text: str) -> list[str]:
    paths: list[str] = []
    for raw_path in re.findall(r"\[[^\]]+\]\(([^)]+)\)", text):
        if raw_path.startswith(("http://", "https://", "#")):
            continue
        paths.append(raw_path)
    return paths


def validate_skill(skill_dir: Path, strict: bool) -> list[str]:
    errors: list[str] = []
    skill_md = skill_dir / "SKILL.md"
    if not skill_md.exists():
        return ["SKILL.md 不存在"]

    text = skill_md.read_text(encoding="utf-8")

    try:
        frontmatter = read_frontmatter(text)
    except ValueError as exc:
        return [str(exc)]

    name = frontmatter.get("name")
    description = frontmatter.get("description")
    if not isinstance(name, str) or not name.strip():
        errors.append("frontmatter.name 缺失或为空")
    if not isinstance(description, str) or not description.strip():
        errors.append("frontmatter.description 缺失或为空")

    for section in REQUIRED_SECTIONS:
        if section not in text:
            errors.append(f"缺少必需章节：{section}")

    for rel_path in extract_reference_paths(text):
        target = (skill_dir / rel_path).resolve()
        if not target.exists():
            errors.append(f"引用文件不存在：{rel_path}")

    if strict:
        openai_yaml = skill_dir / "agents" / "openai.yaml"
        if not openai_yaml.exists():
            errors.append("strict 模式要求 agents/openai.yaml 存在")

        fixtures_dir = skill_dir.parent.parent / "tests" / "fixtures" / skill_dir.name
        if not fixtures_dir.exists():
            errors.append("strict 模式要求存在 tests/fixtures/<skill-name>/")
        else:
            fixture_count = len(list(fixtures_dir.glob("*.md")))
            if fixture_count < 3:
                errors.append("strict 模式要求至少 3 个 markdown fixtures")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="校验本地 skill 结构")
    parser.add_argument("skill_dir", help="skill 目录路径")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="额外校验 UI 元数据和 smoke fixtures",
    )
    args = parser.parse_args()

    skill_dir = Path(args.skill_dir).resolve()
    errors = validate_skill(skill_dir, strict=args.strict)
    if errors:
        print("校验失败：")
        for item in errors:
            print(f"- {item}")
        return 1

    print("校验通过")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
