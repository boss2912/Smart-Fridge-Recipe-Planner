# AGENTS.md — read this first

Group project for course 310-2309 Database Systems: a smart fridge & recipe planner.
Deliverables are a database design + SQL; a Flask web app (Nginx · frontend · backend) is built alongside.
Docs are in Thai. Answer the user in the language they write in.

## Current status — one place only

- **`docs/ROADMAP.md` is the single source of status** (4 stages, 9-round calendar, decided items).
- Do not trust it blindly: check freshness with `git log -1 --format=%cs -- docs/ROADMAP.md`
  and compare with `git log --oneline -10 origin/develop` and `gh issue list --state open`.
  If they disagree, tell the user before acting.
- When a task finishes a ROADMAP item, update the checkbox in `docs/ROADMAP.md` in the same PR.
  Do not add status tables anywhere else.

## Read only what the task needs

| Task | Read |
|---|---|
| Anything graded / "what does the teacher want" | `docs/COURSE_REQUIREMENTS.md` (has slide page numbers) |
| ER / schema / normalization | `design/README.md`, `design/business-rules.md` |
| SQL | `database/README.md`, then the relevant rules in `design/business-rules.md` |
| Web app | `README.md` section "แต่ละส่วนต้องมีอะไร", then `nginx/` `frontend/` `backend/` README |
| Install / run | `INSTALL.md` |
| Who owns what | `docs/TEAM_AND_WORKFLOW.md` |
| Before changing anything that looks odd | `docs/DECISIONS.md` |

Large files — do not read whole:

- `docs/DECISIONS.md` (~44 KB, 18+ ADRs): read the table of contents (`## สารบัญ`), then only the ADR you need.
- `design/er-diagram.drawio` (~63 KB XML) and `design/er-diagram.drawio.png` (~217 KB): open only when the task is about the ER diagram itself.

## Rules (from `CONTRIBUTING.md`)

- `main` and `develop` are protected. Never push to them directly, never force-push.
- Branch from `origin/develop`, named `<issue number>-<topic>`. PR base must be `develop` (GitHub defaults to `main`).
- Merge with **merge commit**, not squash. One approval from someone other than the PR author.
- Commit format: `<type>(<scope>): <summary>` — type `feat|fix|docs|chore`, scope `proposal|design|db|report|nginx|frontend|backend`.
- Never commit member emails (repo is public, ADR-007) or `.db` / `.sqlite` files.
- A decision others might revert → add a new ADR in `docs/DECISIONS.md`; never delete old ADRs, mark them 🔁.
- Each folder's `README.md` must be updated when its contents change.
- Do not edit folders owned by other members without saying so (owners in `docs/TEAM_AND_WORKFLOW.md`).
- DBMS is PostgreSQL (ADR-005). Web stack is Python + Flask (ADR-009).
