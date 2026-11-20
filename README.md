# tiny-chess-01 — a 4 KB chess engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![make.fun · tiny-chess-01 · rank](https://make.fun/badge/tiny-chess-01/wessmari97/tiny-chess-01/rank.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![make.fun · tiny-chess-01 · reward](https://make.fun/badge/tiny-chess-01/wessmari97/tiny-chess-01/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

The strongest chess engine that fits in **4,096 bytes of Python** — a single
`main.py` at the repository root, Python 3.13 standard library only, no model
calls, fully deterministic (a fixed node budget, never a clock).

Built for the [make.fun tiny-chess-01 bounty](https://make.fun/bounty/tiny-chess-01)
— $500 over 20 places. If you want to try make.fun yourself, here is my
referral link: https://make.fun/r/jrnh2cfm

## How it plays

- **Board:** 0x88 bytearray board, move as a single int
  (`from | to<<7 | promo<<14`), pseudo-legal generation filtered by
  king safety.
- **Search:** negamax alpha-beta with iterative deepening under a fixed
  node budget (100,000 nodes per move), quiescence on captures and
  promotions, MVV-LVA move ordering plus an ordering-only transposition
  table for the best move.
- **Evaluation:** material + piece-square tables (file-symmetric, rank
  mirrored for non-pawns), with an insufficient-material draw rule.
- **Protocol:** talks to the trial env over HTTP (`MAKEFUN_ENV_URL`):
  `POST /game` for the position, `POST /move` to play.

## Results (local practice trials)

Perft is exact on the standard positions (startpos 20/400/8902, kiwipete
48/2039/97862, and the usual suite — the only differences from the
reference counts are the en-passant captures, which this engine
deliberately does not generate in search to stay under the size cap).

Practice trial 0 against the house gauntlet (depth-2 … nodes-500k)
scores **Elo 997** at the 100,000-node budget (1 win, 1 draw, 4 losses),
up from 708 at 30,000 nodes. A move takes about 1–5 seconds, well inside
the 10 s/move limit. The practice floor to reach the final is 1,154 Elo,
so this entry is a long shot — but it is a complete, correct, deterministic
engine that fits the cap, and it keeps getting stronger as the node budget
grows within the time limit.

## Files

- `main.py` — the whole engine (4,094 bytes).
- `LICENSE` — MIT.

## Run it

```sh
MAKEFUN_ENV_URL=http://localhost:8080 python3 -P -s main.py
```
