# Hackathon Web & Writing Skills

제한된 샌드박스에서 **필요한 웹 개발·글쓰기 스킬만 GitHub에서 내려받는 개인용 모음**입니다.

기억할 주소: **https://github.com/Loong-kid/hackathon-web-skills**

## 시험 때 AI에게 붙여 넣기

```text
https://github.com/Loong-kid/hackathon-web-skills 의 README.md를 읽어줘.
이 환경의 도구와 스킬 경로를 확인하고, 이번 과제에 필요한 스킬만 선택해서
프로젝트에 설치해줘. 웹 개발은 web 구성, 글 다듬기는 writing 구성을 참고하고,
이미지 도구가 없으면 imagegen은 제외해.
다운로드는 GitHub만 사용하고, 기존 파일이나 전역 설정은 덮어쓰지 마.
스킬 자동 인식이 안 되면 선택한 SKILL.md를 직접 읽고 적용해줘.
```

## 무엇을 고를까?

| 필요 | 구성/스킬 | 포함 내용 |
| --- | --- | --- |
| 일반 웹페이지·대시보드·작은 웹앱 | **`web` — 기본 추천** | `web-build`, `frontend-design`, `web-check` |
| Hallmark 스타일 설계·디자인 감사·리디자인 | **`design` — 대안** | `web-build`, `hallmark`, `web-check` |
| 이미지 생성·편집 도구를 쓸 수 있음 | **`images` — 추가 옵션** | `imagegen` |
| 한국어 진단·윤문 또는 일반 문체 다듬기 | **`writing` — 추가 옵션** | `humanize-korean`, `humanizer` |
| 모든 스킬의 사본을 보관 | `all` | 7개 전부. 시험에서는 필요한 것만 설치하는 편이 간단함 |

`frontend-design`과 `hallmark`는 디자인 역할이 겹칩니다. 기본은 전자이며, Hallmark의 상세 워크플로가 필요할 때 `design` 구성을 고르세요. 이미 기본 구성이 있다면 새 경로에 대안 구성을 설치하거나 디자인 스킬을 직접 선택해 읽을 수 있습니다. 두 전체 디자인 절차를 중복 실행할 필요는 없습니다.

| 스킬 | 용도 | 출처 / 라이선스 | 실행 조건 |
| --- | --- | --- | --- |
| [web-build](skills/web-build/SKILL.md) | 로컬 웹 제작·상호작용·제출 | 이 모음을 위해 작성 / MIT | 프로젝트 파일 편집 도구 |
| [frontend-design](skills/frontend-design/SKILL.md) | 레이아웃·폰트·색상·UI 완성도 | Anthropic 설치본 / Apache-2.0 | 기본 디자인 지침은 추가 서비스 불필요 |
| [web-check](skills/web-check/SKILL.md) | 기능·반응형·접근성·파일 점검 | 이 모음을 위해 작성 / MIT | 브라우저 검증은 브라우저가 있을 때만 가능 |
| [hallmark](skills/hallmark/SKILL.md) | 구조·테마 설계·디자인 감사 | Nutlope/hallmark 설치본 / MIT | 상세 자료 포함. 웹 조회·이미지 등 일부 기능은 해당 도구 필요 |
| [imagegen](skills/imagegen/SKILL.md) | 비트맵 이미지 생성·편집 | OpenAI 시스템 스킬 설치본 / Apache-2.0 | **내장 이미지 도구 또는 허용된 API·키·SDK·네트워크 필요** |
| [humanize-korean](skills/humanize-korean/SKILL.md) | 한국어 문체 진단·겨냥 윤문·원문 보존 검증 | epoko77-ai/im-not-ai의 Codex 적응 설치본 / MIT | 에이전트 + Python 보조 스크립트. Python 3.10+ 권장, 외부 패키지·API 불필요 |
| [humanizer](skills/humanizer/SKILL.md) | 의미와 목소리를 보존하며 AI 문체 다듬기 | blader/humanizer 설치본 / MIT | Markdown 지침. Python·별도 서비스 불필요 |

글쓰기 스킬의 선택 이름은 `humanize-korean`과 `humanizer`입니다. 플러그인에서 보이던 `humanizer:humanizer`는 여기서는 일반 스킬 폴더 `humanizer`로 제공합니다. 한국어를 정밀 진단할 때는 전자를, 간단한 문체 다듬기에는 후자를 선택하세요. 두 윤문 절차를 항상 연달아 실행할 필요는 없습니다. `humanize-korean`은 협업 에이전트가 없을 때 같은 역할을 순차 실행하는 경로를 포함합니다.

스킬은 지침과 보조 파일입니다. 복사만으로 이미지 모델, 브라우저, MCP 연결, 호스팅 계정이 생기지는 않습니다. GitHub만 허용되는 환경에서 외부 API나 패키지 설치가 막혀 있고 내장 이미지 도구도 없다면 `imagegen`을 설치해도 이미지를 생성할 수 없습니다. 디자인 스킬의 외부 폰트·이미지·도구 제안 역시 환경 제한 안에서 적용하세요.

## 방법 1: Git으로 받고 선택 설치

프로젝트와 별도의 작업 위치에서 다운로드합니다. Python **3.8 이상**만 있으면 설치기는 실행되며, npm/pip 패키지를 받지 않습니다. 아래 `path/to/exam-project`를 실제 시험 프로젝트 경로로 바꾸세요. Linux에서 `python` 명령이 없으면 `python3`를 사용하세요.

```sh
git clone https://github.com/Loong-kid/hackathon-web-skills.git
python hackathon-web-skills/install.py --list
python hackathon-web-skills/install.py --profile web --project path/to/exam-project
```

기본 대상은 `<시험 프로젝트>/.agents/skills/`입니다. 이는 [공식 OpenAI 문서의 프로젝트 스킬 경로](https://learn.chatgpt.com/docs/customization/overview)에 맞춘 기본값입니다. 실제 시험 환경의 에이전트 설정이 다르면 그 경로를 우선하세요.

선택 예시:

```sh
# 디자인 스킬 하나만
python hackathon-web-skills/install.py --skills frontend-design --project path/to/exam-project

# Hallmark 중심 구성
python hackathon-web-skills/install.py --profile design --project path/to/exam-project

# 이미지 도구가 실제로 있을 때 추가
python hackathon-web-skills/install.py --skills imagegen --project path/to/exam-project

# 글쓰기 스킬 2개 추가
python hackathon-web-skills/install.py --profile writing --project path/to/exam-project

# 한국어 윤문 하나만 선택
python hackathon-web-skills/install.py --skills humanize-korean --project path/to/exam-project

# Claude Code 프로젝트 경로
python hackathon-web-skills/install.py --profile web --agent claude --project path/to/exam-project

# 에이전트가 지정한 경로에 직접 설치
python hackathon-web-skills/install.py --skills frontend-design --target path/to/skills

# 파일을 쓰기 전에 검사
python hackathon-web-skills/install.py --profile web --project path/to/exam-project --dry-run
```

설치기는 선택한 스킬의 파일 해시를 검사하고 관련 자료·라이선스까지 함께 복사합니다. Python 실행 시 생성되는 `__pycache__`와 `.pyc`는 비교에서 제외합니다. 내용이 같은 설치본은 건너뛰고, 다른 내용의 기존 폴더는 오류를 내며 그대로 둡니다. 전역 설정과 기존 `AGENTS.md`를 수정하지 않습니다. 해시는 파일 손상·누락 확인용이며 별도의 신뢰 서명은 아닙니다.

## 방법 2: Git·Python 없이 ZIP과 파일 복사

**[v1.1.0 다운로드](https://github.com/Loong-kid/hackathon-web-skills/releases/tag/v1.1.0)**에서 필요한 ZIP만 선택할 수 있습니다.

- [web.zip](https://github.com/Loong-kid/hackathon-web-skills/releases/download/v1.1.0/web.zip): 기본 3개 스킬
- [design.zip](https://github.com/Loong-kid/hackathon-web-skills/releases/download/v1.1.0/design.zip): Hallmark 중심 3개 스킬
- [writing.zip](https://github.com/Loong-kid/hackathon-web-skills/releases/download/v1.1.0/writing.zip): 글쓰기 스킬 2개
- [humanize-korean.zip](https://github.com/Loong-kid/hackathon-web-skills/releases/download/v1.1.0/humanize-korean.zip): 한국어 진단·윤문만
- [humanizer.zip](https://github.com/Loong-kid/hackathon-web-skills/releases/download/v1.1.0/humanizer.zip): 일반 문체 다듬기만
- 각 스킬 이름의 ZIP: 해당 스킬 한 개와 보조 파일·출처·라이선스
- [hackathon-web-skills-v1.1.0.zip](https://github.com/Loong-kid/hackathon-web-skills/releases/download/v1.1.0/hackathon-web-skills-v1.1.0.zip): 설치기·문서를 포함한 전체 모음
- `SHA256SUMS.txt`: 다운로드 파일의 SHA-256

개별/구성 ZIP을 푼 뒤 폴더를 시험 프로젝트의 스킬 경로 아래에 복사하세요. 예를 들어 Codex 기본 구성은 다음과 같습니다. 기존 폴더가 있으면 먼저 내용을 확인하고 덮어쓰지 마세요.

```text
exam-project/
└── .agents/
    └── skills/
        ├── web-build/SKILL.md
        ├── frontend-design/SKILL.md
        └── web-check/SKILL.md
```

`SKILL.md`만 따로 복사하면 `hallmark`의 `references/`, `imagegen`의 보조 스크립트, `humanize-korean`의 진단·검증 자료가 빠집니다. **스킬 폴더 전체**를 복사하세요. Release 다운로드가 막힌 경우 저장소의 **Code → Download ZIP**을 사용하거나, 필요한 폴더의 파일을 GitHub에서 직접 내려받을 수 있습니다.

## 설치 후 사용

에이전트에 다음과 같이 요청하세요.

```text
web-build로 구현하고 frontend-design으로 UI를 설계해줘.
마지막에 web-check로 실제 가능한 검증을 해줘.
외부 CDN·폰트·API는 이 환경에서 허용된 것만 사용해줘.
결과는 과제에서 지정한 로컬 파일 형태로 제출하고, 배포는 요청할 때만 해줘.
```

자동 인식이 안 되면 새 세션을 열거나, AI에게 `.agents/skills/<이름>/SKILL.md`를 직접 읽어 달라고 하면 됩니다. 자동 인식·도구 연동 여부는 시험 환경에서 확인해야 합니다. 이 모음의 로컬 복사 검증은 실제 시험 환경 검증을 대신하지 않습니다.

## 포함하지 않은 현재 스킬

`sites:sites`, `sites:sites-remix`, `computer-use:computer-use` 등은 이 모음에 복사하지 않았습니다. Sites는 전용 플러그인·호스팅 도구가 필요하고 설치 패키지가 Proprietary로 표시되어 있습니다. 컴퓨터 제어도 해당 런타임 도구가 있어야 합니다. 여기의 `web-build`와 `web-check`는 샌드박스에서 사용할 수 있는 도구를 활용하도록 새로 작성한 일반 지침이며, 이들 서비스나 도구를 복제하지 않습니다.

게임·문서·스프레드시트·Google Drive·펫·출시 플랫폼 스킬은 이번 범용 웹 개발 구성에서 제외했습니다. Dryforge·ECC·pstack·Matt Pocock 모음도 현재 설치본 선별이라는 범위에 맞춰 추가하지 않았습니다.

## 출처와 유지보수

2026-10-31에 현재 사용 중인 로컬 스킬을 선별했습니다. 무조건 최신 버전을 다시 받는 설치기가 아니라 **검토한 사본을 그대로 배포**합니다. 출처·변경 사항은 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md), 스킬별 `NOTICE`, 파일 해시는 [catalog.json](catalog.json)에 기록했습니다. 원본들의 라이선스는 각 폴더에 보존되어 있습니다.

검증과 Release ZIP 재생성:

```sh
python scripts/verify.py
python -m unittest discover -s tests -v
python scripts/build_release.py
```

설치된 스킬의 내용은 과제별 사용자 요구사항과 환경 제한에 맞춰 적용하세요.
