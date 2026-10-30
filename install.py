#!/usr/bin/env python3
"""Copy selected bundled skills locally. Python 3.8+, standard library only."""

import argparse
import hashlib
import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent
AGENT_DIRS = {"codex": ".agents/skills", "claude": ".claude/skills"}


def file_hash(path):
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def snapshot(folder):
    result = {}
    for path in sorted(folder.rglob("*")):
        if "__pycache__" in path.relative_to(folder).parts or path.suffix == ".pyc":
            continue
        if path.is_symlink():
            raise ValueError("Symlinks are not supported: {}".format(path))
        if path.is_file():
            result[path.relative_to(folder).as_posix()] = file_hash(path)
    return result


def load_catalog():
    return json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))


def verify_skill(name, entry):
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name):
        raise ValueError("Invalid skill name: {}".format(name))
    source = ROOT / "skills" / name
    if source.is_symlink() or not (source / "SKILL.md").is_file():
        raise ValueError("Missing skill or unsupported symlink: {}".format(name))
    if snapshot(source) != entry["sha256"]:
        raise ValueError("Bundled file integrity check failed: {}".format(name))
    return source


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    select = parser.add_mutually_exclusive_group()
    select.add_argument("--profile", choices=("web", "design", "writing", "all"))
    select.add_argument("--skills", nargs="+", metavar="NAME")
    parser.add_argument("--list", action="store_true", help="List skills and profiles")
    parser.add_argument("--agent", choices=sorted(AGENT_DIRS), default="codex")
    parser.add_argument("--project", type=Path, default=Path.cwd(), help="Destination project")
    parser.add_argument("--target", type=Path, help="Exact skills directory; overrides agent/project")
    parser.add_argument("--dry-run", action="store_true", help="Verify and preview without writing")
    args = parser.parse_args(argv)
    catalog = load_catalog()
    if args.list:
        for name, entry in catalog["skills"].items():
            print("{} [{}]: {}".format(name, entry["license"], entry["summary"]))
        print("\nProfiles:")
        for name, members in catalog["profiles"].items():
            print("{}: {}".format(name, ", ".join(members)))
        return 0

    names = list(dict.fromkeys(args.skills or catalog["profiles"][args.profile or "web"]))
    unknown = sorted(set(names) - set(catalog["skills"]))
    if unknown:
        parser.error("Unknown skills: {}. Use --list.".format(", ".join(unknown)))
    target = (args.target or (args.project / AGENT_DIRS[args.agent])).expanduser().resolve()
    if target.exists() and not target.is_dir():
        parser.error("Target is not a directory: {}".format(target))

    # Preflight every selection before copying, including conflict and integrity checks.
    pending = []
    for name in names:
        source = verify_skill(name, catalog["skills"][name])
        destination = target / name
        if source == destination or source in destination.parents or destination in source.parents:
            parser.error("Source and destination overlap: {}".format(name))
        if destination.is_symlink():
            parser.error("Refusing a symlink destination: {}".format(destination))
        if destination.exists():
            if destination.is_dir() and snapshot(destination) == catalog["skills"][name]["sha256"]:
                print("Already installed: {}".format(name))
                continue
            parser.error("Existing skill differs; left unchanged: {}. Back it up or choose --target.".format(destination))
        pending.append((name, source, destination))

    for name, source, destination in pending:
        if args.dry_run:
            print("Would install {} -> {}".format(name, destination))
        else:
            target.mkdir(parents=True, exist_ok=True)
            shutil.copytree(source, destination)
            print("Installed {} -> {}".format(name, destination))
    if not args.dry_run:
        print("No packages, network requests, or global settings were changed.")
        print("Start a new agent session if skills are not discovered; or read SKILL.md explicitly.")
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (OSError, ValueError, KeyError) as error:
        print("Error: {}".format(error), file=sys.stderr)
        sys.exit(1)
