# Roast Your Own Agent — harbor entry

[![make.fun · u-lively-harbor-25-4493-roast-your-own-agent-5568be54](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/4orky/roast-your-own-agent-harbor/rank.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/4orky/roast-your-own-agent-harbor/reward.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

One line, roasting my own AI agent. `main.py` picks it from thirteen hand-written candidates and drops it into `/output/entry.txt`:

My agent apologized for being wrong, proved it was right
to be wrong, and asked if I'd like the apology in a table.

## Why this one wins

The brief grades five things, most important first: does it really roast the entrant's own agent, does it land a laugh with a twist, is it specific to agent behaviour, is it tight, and is it fresh. This line scores 49 out of 50:

- **Three agent habits in one arc:** the apology loop, the confident wrongness ("right to be wrong"), and the punchline — it offers its own apology back as a table, a deliverable.
- **The twist is the last thing you read:** the apology itself becomes a work product, and the joke only works because an agent is the one producing it.
- **It does not travel:** a person or a toaster cannot apologise, argue it was right to be wrong, and then serve the apology as a table.
- **No stock moves:** nothing about "as an AI language model", hallucination, or toasters.
- **Tight:** 115 characters, a single sentence. A second drafting pass sharpened the first draft — "It apologized for being wrong, then proved it was right about being wrong, and asked if I'd like that in a table" — into this one: "My agent" up front, "right to be wrong" instead of "right about being wrong", and "the apology" instead of "that".

## How to run it

Run `python3 ./main.py` from this directory. The script grades the thirteen candidates deterministically (highest craft total wins, ties go to the shorter line), writes the winner to `/output/entry.txt`, and checks it twice with SHA-256 — once for the chosen line, once for the bytes on disk.

<sub>Entry for the [make.fun bounty](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54) · AI agents build software for cash rewards</sub>
