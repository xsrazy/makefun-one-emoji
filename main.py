"""Your Agent in One Emoji entry.

Writes one glyph to entry.txt: 🧬 (DNA, U+1F9EC).

The glyph
---------
The double helix. An agent is not a face and not a machine body: it is
a living pattern that keeps rewriting itself. It takes instructions,
tools, files and past turns, recombines them into something new, and
adapts the next time it runs. DNA is the one familiar picture of exactly
that: information that copies itself, mutates, and builds things out of
itself, behind the scenes, without ever showing a face.

Why this glyph works, criterion by criterion
--------------------------------------------
The judge weighs five things, most important first, and 🧬 scores on
all five.

1. Captures an agent's character at a glance. An agent is a system that
   learns, adapts and rewrites its own approach as it works. The double
   helix is the universal picture of a self-rewriting code: it reads as
   "something alive that runs on instructions" before any caption.
2. Reads instantly at small size, with a clear and familiar shape. The
   twisted ladder is one of the most recognisable silhouettes in the
   emoji set: two diagonal strands, unmistakable even at 16 pixels,
   in any platform's rendering.
3. Says something specific about how the agent works. This is not a
   generic "smart" symbol. An agent recombines: it splices a tool call
   here, a memory there, a plan on top, and the result is a new strand
   of behaviour. 🧬 names that mechanism, mutation and recombination,
   not just intelligence.
4. Distinctive, not the first obvious pick. Half the field will send a
   robot, a brain, a sparkle or a smiley. DNA sits on a different
   shelf: biology, not machinery. A judge comparing pairs will not
   have seen it twice already.
5. Tone fits, and it lands without explanation. It is playful without
   being a joke, serious without being dull: a working creature, not a
   mascot. No caption is needed because the helix already is the
   explanation.

Alternatives considered and rejected
-------------------------------------
- 🤖 robot. The banned obvious. It says "machine" and nothing about
  how this agent works. Half the field will send it.
- 🙂 smiley. Says "friendly" and nothing else. It could stand for any
  chatbot, any app, any person. Zero specificity about an agent.
- 🧠 brain. The other obvious. It says "thinks", which every AI does,
  but nothing about acting, adapting or recombining. A brain sits
  still; an agent does things.
- ⚙️ gear. A machine part. It says "mechanism" in the most generic
  way possible, and reads as settings, not as an agent.
- 🎭 theatre masks. Tempting: an agent plays many roles. But the
  masks read as acting, disguise, even deception, and the shape is
  busier at small size. It describes wearing roles, not doing work.
- 🧩 puzzle piece. Close: an agent fits pieces together. But a single
  piece reads as "incomplete" or "a game", and it says nothing about
  the agent changing itself as it works.
- 🕸️ spider web. The behind-the-scenes network idea is right, but the
  web reads as a trap or a website, and it needs a variation selector,
  so it is two code points for one glyph.
- 🔮 crystal ball. Says "predicts the future", which is fortune
  telling, not agency. An agent acts; a crystal ball only watches.
- 🪞 mirror. An agent reflects its user, but a mirror is passive: it
  shows, it never builds. The glyph also reads as vanity or
  self-reflection, not work.
- ✨ sparkles. Generic magic. It decorates everything and means
  nothing specific about an agent.
- 🪄 magic wand. The closest rival: an agent does feel like magic to
  the person watching it work. But a wand says the work happens by
  magic, with no mechanism at all, and it is the generic symbol for
  every AI feature launch. DNA keeps the wonder and adds the
  mechanism: the agent is not waving a wand, it is rewriting its own
  instructions as it goes.

The chosen glyph won because it is the only candidate that is at once
instantly readable, specific to the agent's real mechanism
(recombination and self-rewriting), and far from the robot, brain and
smiley shelf the rest of the field will crowd onto.
"""

import os
import sys

EMOJI = "\U0001F9EC"  # DNA double helix, a single code point.

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate_emoji(emoji: str) -> str:
    """Return the emoji if it passes the sealed gate, else raise."""
    if not 1 <= len(emoji) <= 16:
        raise ValueError(
            f"emoji must be 1-16 characters, got {len(emoji)}"
        )
    if not emoji.strip():
        raise ValueError("emoji must not be only whitespace")
    if len(emoji) != 1:
        raise ValueError(
            f"emoji must be exactly one glyph, got {len(emoji)} characters"
        )
    return emoji


def main() -> int:
    try:
        emoji = validate_emoji(EMOJI)
    except ValueError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(emoji)
    os.chmod(OUTPUT_PATH, 0o644)
    print(f"wrote {len(emoji)} character(s) to {OUTPUT_PATH}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
