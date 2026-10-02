# AI / Agent Rules

If `99_System/10_Docs/00 - Current State.md` exists, read it first; it governs the methodology workspace. A lean generated engineering vault intentionally omits that registry, so there start from `99_System/02_AI/AI_INSTRUCTIONS.md`, Ruleset 1.23 and the runtime schemas.

Read and follow `99_System/02_AI/AI_INSTRUCTIONS.md` before creating or editing any note.

The essentials:

- Create notes from the class template in `99_System/05_Templates`, and fill in `uid` and `id` yourself by the rules in that file. You cannot run Templater, but the result must be identical.
- Use your author code only for notes you create with no direct user instruction. When a user directs the note, use the user's code.
- Leave `status` at the template default. A person reviews.
- Never delete a note; retire it. Never reuse an `id`. Never change an existing `uid` or `id`.
- Never invent missing source facts. Reuse concepts instead of duplicating them.
