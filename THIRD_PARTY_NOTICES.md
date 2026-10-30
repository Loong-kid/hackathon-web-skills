# Sources and licenses

Snapshot date: 2026-10-31 (Asia/Seoul).

This is a personal curated redistribution. Names identify the original projects.

| Component | Origin | License | Packaging changes |
| --- | --- | --- | --- |
| `skills/frontend-design/` | Installed snapshot from [anthropics/skills](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Apache-2.0 | Original instruction/license bytes preserved; added NOTICE and upstream third-party notices |
| `skills/hallmark/` | Installed snapshot from [Nutlope/hallmark](https://github.com/Nutlope/hallmark/tree/main/skills/hallmark) | MIT | Moved version into metadata; added portability note, MIT license, NOTICE, and canonical theme tokens; repaired resource links |
| `skills/humanize-korean/` | Installed Codex-adapted snapshot of [epoko77-ai/im-not-ai](https://github.com/epoko77-ai/im-not-ai/tree/main/skills/humanize-korean) | MIT, copyright 2026 epoko77-ai | Original instructions, references, scripts, and UI metadata preserved; excluded generated caches; added NOTICE |
| `skills/humanizer/` | Installed snapshot of [blader/humanizer](https://github.com/blader/humanizer) | MIT, copyright 2025 Siqi Chen | Original SKILL.md, LICENSE, and UI metadata preserved; added NOTICE; upstream development and plugin packaging files omitted |
| Packaging scripts, tests, and repository documentation | Written for this repository | MIT | Original |

The installed Hallmark snapshot is not asserted to match the
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

The repository's root MIT license does not replace third-party licenses.
Retain the license and NOTICE files when redistributing individual folders.

The writing skills were added in v1.1.0 on the snapshot date above. Humanizer's
SKILL.md matches the public upstream blob
`19fc634208e8cc6ae55d4ff287152583216fd244` inspected when packaging.
Humanize Korean's baseline.json matches the public upstream blob
`8565b1e5efc3c336d956851aad7e1aace1900e63`; its historical corpus labels and
calibration values are upstream reference data, not private inputs from this
workspace. Its installed Codex adaptations are retained without asserting an
exact upstream commit match. No prior rewriting runs, drafts, or Python caches
are included.
