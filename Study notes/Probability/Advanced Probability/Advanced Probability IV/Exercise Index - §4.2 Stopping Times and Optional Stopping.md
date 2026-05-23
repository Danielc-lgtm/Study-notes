---
type: exercise-index
subject: advanced-probability
section: "4.2"
tags: [probability, advanced-probability]
---

## §4.2 Stopping Times and Optional Stopping — Exercises

The exercises of §4.2 drill the optional stopping theorem and its computational use. Each exercise applies optional stopping to a specific [[Def - Martingale|martingale]] at a specific exit time: $S_n$ and $S_n^2 - n$ for fair-walk gambler's ruin (giving $k/N$ and $k(N-k)$); $(q/p)^{S_n}$ for biased hitting probabilities; and the first-passage time on the unbounded line as the counterexample that exposes the necessity of boundedness or uniform integrability. The unifying lesson: "you cannot beat a fair game with bounded resources."

- [[Ex - Gambler's ruin via optional stopping]] (⭐⭐) — hitting probability $k/N$ and expected duration $k(N-k)$ ([[Thm - Optional Stopping Theorem]], [[Ex - Martingales of the random walk]])
- [[Ex - Optional stopping fails for unbounded times]] (⭐⭐) — a fair walk's first hitting of $1$ breaks $\mathbb{E}[X_T]=\mathbb{E}[X_0]$; the boundedness/UI hypothesis is necessary ([[Thm - Optional Stopping Theorem]], [[Def - Uniform Integrability]])
- [[Ex - Hitting probabilities of a biased random walk]] (⭐⭐) — the exponential martingale $(q/p)^{S_n}$; biased hitting probabilities ([[Thm - Optional Stopping Theorem]], [[Ex - Martingales of the random walk]])
