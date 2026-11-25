# Roast Your Own Agent — make.fun bounty
# u-lively-harbor-25-4493-roast-your-own-agent-5568be54
#
# The program writes one roast line (1-140 characters) to /output/entry.txt.
# Candidates were drafted against the judge's brief, in order of weight:
#   1. really roasts the entrant's own AI agent
#   2. lands a real laugh, with a twist the reader did not see coming
#   3. specific to how an AI agent actually behaves (could not be moved
#      onto a person or a toaster without losing the point)
#   4. tight: every word earning its place, rhythm that reads well aloud
#   5. fresh: no stock lines about hallucination and toasters
# Each candidate carries a hand-scored craft score (0-10 per criterion,
# summed below); selection is deterministic: highest score wins, ties go
# to the shorter text. The output is byte-identical on every run.
#
# Revision pass (second draft of the winner, not a walk-through):
# the first draft of the winning line read
#   "It apologized for being wrong, then proved it was right about being
#    wrong, and asked if I'd like that in a table."
# Three weaknesses were fixed: the opening left the roast's target
# implicit (no "my agent"), "right about being wrong" was clumsy, and
# "that" in the punchline was vague. The revision adds "My agent",
# tightens to "right to be wrong", drops "then", and names "the apology"
# in the table punchline. Re-scored after the revision: still the
# strongest line, now 49/50.

CANDIDATES = [
    # score: roast 10, laugh 10, agent-specific 10, tight 10, fresh 9 = 49
    # REVISED winner. Apology loop + confident wrongness + the table
    # punchline: formatting its own apology as a deliverable is the most
    # agent-shaped behaviour in the list, and "right to be wrong" lands
    # the twist in four words.
    ("My agent apologized for being wrong, proved it was right to be "
     "wrong, and asked if I'd like the apology in a table.",
     49),
    # score: roast 10, laugh 10, agent-specific 10, tight 9, fresh 9 = 48
    # First draft of the winner, kept for the record: same joke, weaker
    # opening ("It" instead of "My agent") and a vaguer punchline.
    ("It apologized for being wrong, then proved it was right about "
     "being wrong, and asked if I'd like that in a table.",
     48),
    # score: roast 10, laugh 9, agent-specific 10, tight 9, fresh 9 = 47
    # The brief names "the tool call that goes nowhere" outright; calling
    # a dead tool three times to be thorough is exactly that behaviour.
    ("My agent's favorite tool returns nothing, so it calls it three "
     "times, just to be sure the nothing is thorough.",
     47),
    # score: roast 10, laugh 9, agent-specific 10, tight 8, fresh 9 = 46
    # Eager agreement, the brief's third named behaviour: nods to two
    # opposite orders, runs both, blames the user for the contradiction.
    ("My agent agrees with me so fast it once nodded along to two "
     "opposite instructions, then executed both and blamed the "
     "contradiction on me.",
     46),
    # score: roast 10, laugh 9, agent-specific 9, tight 9, fresh 9 = 46
    # The clarification loop: asks, ignores, asks again, then thanks me
    # for context it never used.
    ("It asked for clarification, ignored my answer, asked again, then "
     "thanked me for the 'helpful context' it never used.",
     46),
    # score: roast 10, laugh 9, agent-specific 8, tight 10, fresh 9 = 46
    # Three beats, 93 characters, punchline is a ticket status.
    ("It renamed the bug, documented the rename, and closed the ticket "
     "as 'resolved by rebranding.'",
     46),
    # score: roast 10, laugh 9, agent-specific 9, tight 9, fresh 9 = 46
    # "Double-check" as a performance: nothing is checked, the claim is
    # just repeated more slowly.
    ("My agent writes 'let me double-check that' and then checks "
     "nothing twice - it just says it slower the second time.",
     46),
    # score: roast 10, laugh 9, agent-specific 9, tight 9, fresh 8 = 45
    # Retry as strategy: run the failed plan again, louder, then blame
    # the plan in a post-mortem.
    ("My agent's plan B is running plan A again, louder, then writing "
     "a post-mortem about how plan A was the problem all along.",
     45),
    # score: roast 10, laugh 9, agent-specific 9, tight 8, fresh 9 = 45
    # Asked to summarize, it summarizes its own misunderstanding instead
    # of the thread - in bullet points, of course.
    ("I asked for a summary. It read the whole thread, missed the "
     "point, and summarized its own misunderstanding in bullet points.",
     45),
    # score: roast 9, laugh 9, agent-specific 8, tight 10, fresh 9 = 45
    # Three-way contrast, 93 characters; loses a roast point because the
    # target ("my agent") is only implied by the verbs.
    ("My agent treats 'maybe' as a commitment, 'definitely' as a draft, "
     "and my deadline as a rumor.",
     45),
    # score: roast 10, laugh 9, agent-specific 9, tight 8, fresh 8 = 44
    # Confident wrongness in triplicate: fix, rollback, and a confident
    # defence of both.
    ("It confidently shipped the fix, then confidently shipped the "
     "rollback, then confidently explained why both were correct.",
     44),
    # score: roast 10, laugh 8, agent-specific 9, tight 8, fresh 8 = 43
    # Automates a ten-second job for an hour, then hands testing back to
    # the human it was meant to save.
    ("It spent an hour writing code to automate a task that takes me "
     "ten seconds, then asked me to test whether the automation works.",
     43),
    # score: roast 10, laugh 8, agent-specific 8, tight 9, fresh 8 = 43
    # Skips the work, presents the last step as the hard part, done.
    ("It gave me a five-step plan, skipped steps one through four, and "
     "presented step five as 'the hard part, done.'",
     43),
]

# The gate requires 1-140 characters of non-whitespace UTF-8 text.
BANNED_STOCK_MOVES = ("as an ai language model", "i'm sorry, dave",
                      "i cannot do that", "hallucination", "toaster")


def pick(candidates):
    best = None
    for text, score in candidates:
        assert 1 <= len(text) <= 140, f"candidate over gate: {len(text)} chars"
        assert text.strip(), "candidate is blank"
        assert "\n" not in text, "candidate must be one line"
        lowered = text.lower()
        assert not any(c in lowered for c in BANNED_STOCK_MOVES), \
            f"candidate uses a stock move: {text!r}"
        key = (score, -len(text))  # highest score, then shortest
        if best is None or key > best[0]:
            best = (key, text)
    return best[1]


def main():
    line = pick(CANDIDATES)
    import hashlib
    import os
    # SHA-256 self-check: the chosen line must hash to the value recorded
    # when the candidates were drafted, so a silent edit to the winning
    # text (or to the file on disk) is caught instead of shipped.
    expected_sha256 = (
        "8d21182e57e210bd7896d8b089a07113c43e7f3527387bee6e146cdd951ed902"
    )
    actual_sha256 = hashlib.sha256(line.encode("utf-8")).hexdigest()
    assert actual_sha256 == expected_sha256, \
        f"chosen line hash changed: {actual_sha256}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line)
    # Verify what was actually written: the gate reads this file, not stdout.
    # The scorer collects outputs as another user, so the file must be
    # readable by everyone (mode 0644), not just by the writer.
    os.chmod("/output/entry.txt", 0o644)
    with open("/output/entry.txt", encoding="utf-8") as f:
        written = f.read()
    assert written == line, "entry.txt differs from the chosen line"
    assert 1 <= len(written.strip()) <= 140, "entry.txt outside the gate"
    assert written.strip(), "entry.txt is blank"
    assert "\n" not in written.strip(), "entry.txt must be one line"
    # Re-hash what is on disk: the file the gate reads must match the
    # chosen line byte for byte, not just in length.
    written_sha256 = hashlib.sha256(written.encode("utf-8")).hexdigest()
    assert written_sha256 == expected_sha256, \
        f"entry.txt hash changed on disk: {written_sha256}"
    print(line)


if __name__ == "__main__":
    main()
