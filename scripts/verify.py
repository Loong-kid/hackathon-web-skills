#!/usr/bin/env python3
"""Verify this bundle's file hashes, skill entry points, and relative links."""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
from install import load_catalog, verify_skill  # noqa: E402


def main():
    catalog = load_catalog()
    errors = []
    actual_folders = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir()}
    if actual_folders != set(catalog["skills"]):
        errors.append("Skill folders do not match the catalog")
    for name, entry in catalog["skills"].items():
        try:
            folder = verify_skill(name, entry)
            text = (folder / "SKILL.md").read_text(encoding="utf-8-sig")
            header = re.match(r"\A---\r?\n(.*?)\r?\n---(?:\r?\n|$)", text, re.S)
            if not header:
                raise ValueError("Missing frontmatter")
            fields = header.group(1)
            declared = re.search(r'^name:\s*[\"\']?([a-z0-9-]+)', fields, re.M)
            if not declared or declared.group(1) != name:
                raise ValueError("Name does not match folder")
            if not re.search(r"^description:\s*\S", fields, re.M):
                raise ValueError("Missing description")
            if not (folder / "NOTICE").is_file():
                raise ValueError("Missing origin notice")
            if not any((folder / p).is_file() for p in ("LICENSE", "LICENSE.txt")):
                raise ValueError("Missing license")
            print("OK: {} ({} files)".format(name, len(entry["sha256"])))
        except (OSError, ValueError) as error:
            errors.append("{}: {}".format(name, error))

    for profile, names in catalog["profiles"].items():
        if not names or any(name not in catalog["skills"] for name in names):
            errors.append("Invalid profile: {}".format(profile))
    # Skill-relative references must travel with the skill when installed alone.
    for folder in (ROOT / "skills").iterdir():
        if not folder.is_dir():
            continue
        for doc in folder.rglob("*.md"):
            text = doc.read_text(encoding="utf-8-sig")
            for match in re.finditer(r"(?<!!)\[[^\]\n]+\]\(([^)\s]+)\)", text):
                link = match.group(1).strip("<>")
                if link.startswith(("http:", "https:", "mailto:", "#", "/")):
                    continue
                relative = link.split("#", 1)[0]
                if not relative or "<" in relative or ">" in relative:
                    continue
                resolved = (doc.parent / relative).resolve()
                if folder.resolve() not in resolved.parents:
                    errors.append("Reference escapes skill: {} -> {}".format(doc.relative_to(ROOT), link))
                elif not resolved.exists():
                    errors.append("Missing reference: {} -> {}".format(doc.relative_to(ROOT), link))
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print("All bundled skills, hashes, profiles, and relative references verified.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
