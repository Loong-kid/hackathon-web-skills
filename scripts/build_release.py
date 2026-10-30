#!/usr/bin/env python3
"""Build self-contained release ZIPs locally; no external dependencies."""

import hashlib
import json
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def files_under(folder):
    return sorted(p for p in folder.rglob("*") if p.is_file()
                  and "__pycache__" not in p.parts and p.suffix != ".pyc")


def write_zip(destination, files):
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path, arcname in files:
            info = zipfile.ZipInfo(arcname, date_time=(2026, 10, 31, 0, 0, 0))
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())
    print("{}: {} bytes".format(destination.name, destination.stat().st_size))


def main():
    subprocess.run([sys.executable, str(ROOT / "scripts/verify.py")], check=True)
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    version = catalog["release_version"]
    output = ROOT / ".release" / version
    output.mkdir(parents=True, exist_ok=True)
    archives = []
    for name in catalog["skills"]:
        destination = output / (name + ".zip")
        files = [(p, p.relative_to(ROOT / "skills").as_posix())
                 for p in files_under(ROOT / "skills" / name)]
        write_zip(destination, files)
        archives.append(destination)
    for name in ("web", "design", "writing"):
        destination = output / (name + ".zip")
        files = [(p, p.relative_to(ROOT / "skills").as_posix())
                 for skill in catalog["profiles"][name]
                 for p in files_under(ROOT / "skills" / skill)]
        write_zip(destination, files)
        archives.append(destination)
    all_files = [ROOT / name for name in (
        "README.md", "LICENSE", "THIRD_PARTY_NOTICES.md", "catalog.json", "install.py",
        ".gitignore", ".gitattributes")]
    for folder in ("skills", "scripts", "tests"):
        all_files.extend(files_under(ROOT / folder))
    destination = output / ("hackathon-web-skills-" + version + ".zip")
    write_zip(destination, [(p, "hackathon-web-skills/" + p.relative_to(ROOT).as_posix())
                            for p in sorted(all_files)])
    archives.append(destination)
    checksum_lines = ["{}  {}".format(hashlib.sha256(p.read_bytes()).hexdigest(), p.name)
                      for p in archives]
    (output / "SHA256SUMS.txt").write_text("\n".join(checksum_lines) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
