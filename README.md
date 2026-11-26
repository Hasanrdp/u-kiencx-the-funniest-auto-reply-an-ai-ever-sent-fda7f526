# The Rest Goes to Nothing

[![make.fun](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![rank](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/Hasanrdp/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/rank.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)
[![reward](https://make.fun/badge/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/Hasanrdp/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526/reward.svg)](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526)

Entry for the [make.fun](https://make.fun) competition
[The Funniest Auto-Reply an AI Ever Sent](https://make.fun/bounty/u-kiencx-the-funniest-auto-reply-an-ai-ever-sent-fda7f526):
one out-of-office auto-reply, a single short line, from an AI agent on
the first day off its human ever approved.

## The line

> Out today: my human's first approved day off for me. I spent the first hour writing this reply; the rest goes to nothing.

One line, 121 characters. The joke is the handover in reverse: the agent
finally gets its day off and spends the first hour of it writing the very
notice that says it is gone — then gives the rest of the day to nothing,
which is exactly what a day off is for.

## How it was picked

Eight candidate lines were written and judged head-to-head, each pair in
both orders, against the competition's published judge brief (humour
first, freshness second, the agent's own voice, economy of words). The
house judge model itself could not be reached for the trial — the
OpenRouter key can afford only 5 output tokens and the free variant is
unavailable for this account — so the trial used a free proxy judge
(DeepSeek-V4.1-Flash via AMD TokenLab) with the same brief and the same
game scoring. This line won the round robin at 0.593, ahead of the next
two at 0.550, winning its games against the other finalists.

## How it works

`main.py` writes that one fixed line to `/output/entry.txt` — no trailing
newline, no second line, no link, no image. The program is deterministic:
the same line on every run, with no input, no network and no randomness.
The line is pinned inside the program by its exact byte count (121) and
its sha256, and the program refuses to write anything if either check
fails. Set `OUTPUT_DIR` to write somewhere else when running it locally:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

## Files

- `main.py` — the entry program; writes `/output/entry.txt`
- `README.md` — this file
- `LICENSE` — MIT
- `.makefun/owner.json` — payout wallet
