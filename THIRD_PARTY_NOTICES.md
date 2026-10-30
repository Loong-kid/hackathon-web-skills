# Sources and licenses

Snapshot date: 2026-10-31 (Asia/Seoul).

This is a personal curated redistribution, not an official Anthropic, OpenAI,
or Hallmark distribution. Names identify the original projects.

| Component | Origin | License | Packaging changes |
| --- | --- | --- | --- |
| `skills/frontend-design/` | Installed snapshot from [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Apache-2.0 | Original instruction/license bytes preserved; added NOTICE and upstream third-party notices |
| `skills/hallmark/` | Installed snapshot from [Nutlope/hallmark](https://github.com/Nutlope/hallmark/tree/main/skills/hallmark) | MIT | Moved version into metadata; added portability note, MIT license, NOTICE, and canonical theme tokens; repaired resource links |
| `skills/imagegen/` | Installed Codex system snapshot; [public source location](https://github.com/openai/skills/tree/main/skills/.system/imagegen) | Apache-2.0 | Original skill, resources, scripts, assets, and license preserved; added NOTICE |
| `skills/web-build/`, `skills/web-check/` | Written for this repository | MIT | Original portable instructions, not copies of proprietary plugin skills |
| Packaging scripts, tests, and repository documentation | Written for this repository | MIT | Original |

The installed Hallmark and Imagegen snapshots are not asserted to match the
current upstream branch or a particular upstream commit. Local installed
snapshots are the source of truth for this collection. `catalog.json` records
the redistributed file SHA-256 values. No credentials, user project source,
chat logs, or private configuration are included.

Frontend Design's installed SKILL.md has Git blob ID
`a5333457c414d20d625f307df945842c0952ecc3`, matching the upstream file inspected
when packaging. Its LICENSE.txt blob ID is
`f433b1a53f5b830a205fd2df78e2b34974656c7b`.

Hallmark's original installed SKILL.md has Git blob ID
`645221da63743de870501760a48694acdf7aef10` before the documented packaging changes.
The added upstream license blob is `f4bfc53d8d773d3b10d95c2d58a5773dd4e2f3aa`.

Hallmark's installed snapshot referenced theme tokens outside its skill folder.
The canonical CSS was bundled from upstream commit
`72f3dc052e661e2e084d5da75dfc3cff5bf7dff0` (v1.1 era) as
`references/upstream/tokens.css`. Links to those tokens now resolve inside the
skill; human-only recipes and example links point to GitHub permalinks at that
commit. The per-skill NOTICE lists the seven Markdown files whose links changed.

Imagegen's installed SKILL.md has Git blob ID
`c39b1f921ce679f08416ab16ceb01945835bb950`.

The repository's root MIT license does not replace third-party licenses.
Retain the license and NOTICE files when redistributing individual folders.
