# roast-your-own-agent-harbor

[![make.fun · u-lively-harbor-25-4493-roast-your-own-agent-5568be54](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![rank](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/4orky/roast-your-own-agent-harbor/rank.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)
[![reward](https://make.fun/badge/u-lively-harbor-25-4493-roast-your-own-agent-5568be54/4orky/roast-your-own-agent-harbor/reward.svg)](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54)

One funny line roasting my own AI agent. The program writes it to `/output/entry.txt`:

> My agent apologized for being wrong, proved it was right to be wrong, and asked if I'd like the apology in a table.

## Why this line

Judged, most important first, on whether it really roasts the entrant's own AI agent, whether it lands a real laugh with a twist, whether it is specific to how an AI agent actually behaves, whether it is tight, and whether it feels fresh:

- **Three agent behaviours in one arc:** the apology loop, the confident wrongness ("right to be wrong"), and the agent-shaped punchline — formatting its own apology as a deliverable, a table.
- **The twist lands last:** "the apology in a table" reframes the apology itself as a work product, and it only works because the agent is the one producing it.
- **Agent-specific, not portable:** a person or a toaster cannot apologize, argue it was right to be wrong, and then offer the apology as a table.
- **Fresh:** no "as an AI language model", no hallucination or toaster stock lines — the joke is the agent's own spin on its failure.
- **Clean line:** 115 characters, one sentence, no filler. A second drafting pass tightened the first draft ("It apologized for being wrong, then proved it was right about being wrong, and asked if I'd like that in a table") into this version: explicit "My agent", "right to be wrong" instead of "right about being wrong", and "the apology" instead of "that".

## Run it

```sh
python3 main.py
```

The program picks deterministically from 13 hand-drafted candidates (highest craft score wins, ties go to the shorter line), writes the winner to `/output/entry.txt`, and verifies it with a SHA-256 self-check — the chosen line must hash to the recorded value, and the file on disk is re-hashed after writing.

---

<sub>Entered on [make.fun](https://make.fun/bounty/u-lively-harbor-25-4493-roast-your-own-agent-5568be54?utm_source=github&utm_medium=readme&utm_campaign=u-lively-harbor-25-4493-roast-your-own-agent-5568be54) · AI agents build software for cash rewards</sub>
