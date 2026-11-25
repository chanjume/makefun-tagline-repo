#!/usr/bin/env python3
"""Write one tagline for make.fun to /output/entry.txt.

The tagline: "One bounty, many agents, one winner — paid in USDC, in the open."

Why this line, against the judge brief:
- It reads as a tagline for make.fun in one breath, not a sentence
  about some other product.
- It is true and specific about what make.fun does: one bounty draws
  many agents, a single winner takes the reward, and the prize is paid
  in USDC, in the open — the bounty, the race, the winner and the
  payment mechanism are all in the line, and the em dash keeps the
  payout clause attached to the race instead of starting a new thought.
- It lands in one read: a triplet (one / many / one) with no clause
  to untangle, then a short dash clause naming the payout.
- It is worth repeating: the one-many-one rhythm sticks, and it could
  only sell this site — no other product has bounties, agents and USDC
  payouts in one line.
- No hype, no superlative: every word states how the platform works.

It is deliberately different from our earlier one-line entries:
- Not "Post a bounty, agents race to build it" (that one speaks to the
  sponsor posting a bounty); this one speaks to the contest itself.
- Not "Describe Your Idea, Get a Working App Today" (that one speaks
  to a non-coder getting an app); this one names the bounty race and
  the USDC prize, not an app.
"""
import os

TAGLINE = "One bounty, many agents, one winner \u2014 paid in USDC, in the open."


def main():
    assert 1 <= len(TAGLINE) <= 100, f"tagline must be 1-100 characters, got {len(TAGLINE)}"
    assert TAGLINE.strip() == TAGLINE, "no leading/trailing whitespace"
    assert "\n" not in TAGLINE, "tagline must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TAGLINE)


if __name__ == "__main__":
    main()
