# ponytail: posts live in code, same as the skill list in resume_tags; move to the DB if they get frequent.
from datetime import date

POSTS = [
    {
        "slug": "english-review-instruction",
        "date": date(2026, 9, 22),
        "title": 'No new app. No new habit. Just better English while I work.',
        "image": "english-review.png",
        "alt": 'Agent session with an inline English review: one message gets “English errors found” with three corrections, the next gets “No English errors”.',
        "body": """\
My coding agent reviews every prompt.
An English check comes first, then the original task.

I started from a single line:
“Always review my English before answering.”

The reviews were unstable.
One run caught a missing article, the next handed me a long read about writing.

Then the agent kept forgetting.
Despite “always” in the instruction, reviews still went missing. I wanted it to run without me.

Silence had a green light.
The instruction allowed it when there was nothing of mine to check, like a message in another language or pasted content. So a forgotten review looked exactly like a correct one.

Forbidding silence was the fix.
Every reply starts with exactly one status, no exceptions:
× English errors found
✓ No English errors
– English review skipped

Long mixed messages were the trickiest.
The agent kept skipping the review when my own English was there.

It took three fixes:
• Checking is the default. Skipping has to be earned.
• Remove everything that isn't mine first: pasted text or code, other languages.
• Add worked examples like “Compare these” plus two pasted texts.

A strict format kept it stable:
• Shortest fragment.
• Correction.
• One-line reason.

About 1,100 tokens per session.
That's the cost of the instruction, and I've noticed no quality drop. Even in thinking mode, only the first thoughts go to the review.

Did my English actually improve?
Yes, especially articles. My guess is frequency, since they show up in almost every sentence.

This is my only global user-level instruction, in CLAUDE.md/AGENTS.md. See the link in the first comment.

What has earned a place in your global instructions?

The full instruction → https://gist.github.com/resivalex/bdfd0769672b9c8a954a49f5fb9c2b06""",
    },
    {
        "slug": "agents-md-claude-md",
        "date": date(2026, 8, 21),
        "title": 'Shared Claude Code & OpenAI Codex instructions.',
        "image": "agents-md.png",
        "alt": 'Diagram: in the root and tests/ folders, CLAUDE.md contains @AGENTS.md and imports the AGENTS.md next to it, the source of truth.',
        "body": """\
Store in AGENTS.md, reference from CLAUDE.md.

AGENTS.md
CLAUDE.md  → @AGENTS.md

/tests/
    AGENTS.md
    CLAUDE.md  → @AGENTS.md

One caveat in the mechanics. Both merge nested instructions with the root file, but they discover them differently:

• Claude Code discovers nested CLAUDE.md on demand when working with files in that directory.
• Codex loads the AGENTS.md chain from the project root to the current working directory at session start.

Official docs in the comments.

Related links:

Claude Code → https://code.claude.com/docs/en/memory#how-claude-md-files-load
OpenAI Codex → https://learn.chatgpt.com/docs/agent-configuration/agents-md#how-codex-discovers-guidance""",
    },
    {
        "slug": "product-type-discovery",
        "date": date(2026, 8, 3),
        "title": "Can't name. Can't count. Still have to classify.",
        "image": "product-type-discovery.gif",
        "alt": 'Animation of 100 labeling steps on a 2D projection of catalog products: accepted and rejected merges appear as labeled types grow.',
        "body": """\
Solution: Same-Type Contract + LLM-as-a-Judge + Metric Learning.

Millions of products. No product-type taxonomy to build on.

Naming: a type isn't defined by its name.
• Oil filter ≠ fuel filter — same word, different criteria.
• Cordless screwdriver = drill-driver — different words, same criteria.

→ Same-Type Contract: two products belong to the same type if buyers compare them using the same criteria.

→ LLM-as-a-Judge: it evaluated every proposed merge and approved only high-confidence ones.

Counting: the full set of types couldn't be fixed upfront — an open-set problem.

→ Metric Learning: it returned the closest known type and the probability that none fits.

Budget: too many items to send them all to an LLM.

→ Active Learning: it picked only uncertain, diverse candidates — not the whole catalog.

Result: ~200 discovered types cover over half the catalog.

One verified boundary at a time — the taxonomy kept growing.""",
    },
]

POSTS_BY_SLUG = {post["slug"]: post for post in POSTS}

for post in POSTS:
    post["excerpt"] = post["body"].split("\n\n")[0]
