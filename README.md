# contextbudget-kit

Estimate LLM cost of a file before you send it

Built for my own use; public in case it helps someone.

## Examples

```bash
python cost.py prompt.txt --model gpt-4o-mini --expect-out 500
```

## Install

```bash
# stdlib only
```

## Highlights

- Reports input/output tokens and USD estimate
- Heuristic token estimate (~4 chars/token)
- Per-model pricing table in JSON
- Zero dependencies

## Project structure

```text
├── .github/
│   └── workflows/
│       └── ci.yml
├── docs/
│   ├── development.md
│   ├── faq.md
│   ├── roadmap.md
│   └── usage.md
├── examples/
│   └── quickstart.md
├── tests/
│   └── test_smoke.py
├── .gitignore
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── cost.py
└── pricing.json
```

## 说明

个人练习项目, 谨慎用于生产环境。
