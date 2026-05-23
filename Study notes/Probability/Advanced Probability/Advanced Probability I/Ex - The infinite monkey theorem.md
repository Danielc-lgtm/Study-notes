---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Thm - Borel-Cantelli Lemmas"
  - "Def - Independence"
  - "Thm - Kolmogorov 0-1 Law"
tags: [probability, advanced-probability]
---

# Problem Statement

A monkey types an infinite i.i.d. sequence of characters, each uniform on a $K$-letter alphabet.

**(a)** Fix a target string $w$ of length $L$. Show that, almost surely, $w$ appears (as a contiguous block) infinitely often in the sequence.

**(b)** Identify where the [[Thm - Borel-Cantelli Lemmas|second Borel–Cantelli lemma]] is used and why independence is essential.

**(c)** Explain how the [[Thm - Kolmogorov 0-1 Law|Kolmogorov 0–1 law]] tells us, *before any computation*, that $\mathbb{P}(w\text{ appears infinitely often})\in\{0,1\}$.

**Recall:**

[[Thm - Borel-Cantelli Lemmas|Second Borel–Cantelli]]: independent events with $\sum\mathbb{P}(A_n)=\infty$ have $\mathbb{P}(A_n\text{ i.o.})=1$.

---

# Convergent Strategy

**Problem class:** proving an almost-sure occurrence via the divergent-sum half of Borel–Cantelli.

**Assumption pattern:** the sequence is i.i.d. To apply the *second* lemma one needs *independent* events $A_n$ — so partition the sequence into **disjoint blocks** of length $L$; the events "block $n$ equals $w$" are then independent, each of probability $K^{-L}>0$.

**Theorem routing:** disjoint blocks $\Rightarrow$ independent events, each probability $K^{-L}$ $\Rightarrow\sum\mathbb{P}(A_n)=\infty\Rightarrow$ second Borel–Cantelli.

**Key decision point:** using *disjoint, non-overlapping* blocks to manufacture genuine independence — overlapping windows are *not* independent.

---

# Legal Operations Used

1. **Partition into disjoint blocks** to obtain independent events.
2. **Second Borel–Cantelli lemma.**
3. **0–1 law** for an a priori dichotomy.

---

# Hints

> [!note]- Hint 1
> Overlapping length-$L$ windows share letters — *not* independent. Use disjoint blocks: positions $[(n-1)L+1,\,nL]$.

> [!note]- Hint 2
> $A_n=\{$block $n$ equals $w\}$. By i.i.d.-ness, $\mathbb{P}(A_n)=K^{-L}$, and the $A_n$ (disjoint blocks) are independent.

> [!note]- Hint 3
> $\sum_n K^{-L}=\infty$. Apply the second lemma.

---

# Solution

**Step 1 — (a),(b).** Cut the infinite sequence into consecutive **disjoint blocks** of length $L$: block $n$ is positions $(n-1)L+1,\dots,nL$. Let
$$A_n=\{\text{block }n\text{ equals }w\}.$$

> [!note]- Derivation
> Since the characters are i.i.d. uniform on $K$ letters, the probability that the $L$ characters of block $n$ spell $w$ exactly is $\mathbb{P}(A_n)=K^{-L}$ — the same for every $n$. Crucially, distinct blocks use *disjoint* sets of characters, and the characters are independent, so the events $(A_n)_{n\ge1}$ are mutually independent. (Had we used *overlapping* windows, they would share characters and independence would fail — this is exactly why disjoint blocks are chosen.)
> Now $\sum_{n\ge1}\mathbb{P}(A_n)=\sum_n K^{-L}=\infty$. By the [[Thm - Borel-Cantelli Lemmas|second Borel–Cantelli lemma]] — divergent sum *plus independence* — $\mathbb{P}(A_n\text{ infinitely often})=1$. So a.s. infinitely many blocks equal $w$; in particular $w$ appears infinitely often in the sequence.

The second lemma is used at the last step, and its independence hypothesis is supplied by the disjoint-block construction — without independence, a divergent sum gives *nothing* (the first lemma needs convergence; only the second exploits divergence, and only for independent events).

**Step 2 — (c) The 0–1 law.** The event $E=\{w\text{ appears infinitely often}\}$ is a [[Thm - Kolmogorov 0-1 Law|tail event]]: changing any *finite* number of typed characters cannot affect whether $w$ appears *infinitely* often (only finitely many occurrences are touched). Since the characters are independent, the [[Thm - Kolmogorov 0-1 Law|Kolmogorov 0–1 law]] gives $\mathbb{P}(E)\in\{0,1\}$ — *before* any estimation. The Borel–Cantelli computation then resolves the dichotomy in favour of $1$.

> [!note]- Complete formal solution
> (a),(b) Disjoint length-$L$ blocks give independent events $A_n=\{$block $n=w\}$ with $\mathbb{P}(A_n)=K^{-L}$; $\sum\mathbb{P}(A_n)=\infty$, so the second Borel–Cantelli lemma gives $\mathbb{P}(A_n\text{ i.o.})=1$ — $w$ appears infinitely often a.s. (c) $\{w\text{ i.o.}\}$ is a tail event (insensitive to finitely many characters); independence + the 0–1 law force its probability into $\{0,1\}$ a priori. $\blacksquare$

---

# Key Takeaways

**To apply the second Borel–Cantelli lemma, manufacture *independent* events — typically by partitioning into disjoint blocks.** The lemma's divergent-sum conclusion ("infinitely often, almost surely") is *only* available for independent events, so the modelling work is engineering independence. Overlapping windows are correlated and useless here; disjoint blocks share no randomness and are genuinely independent. This block trick recurs everywhere — in proving recurrence of random walks, the existence of long runs, percolation occurrences.

**The [[Thm - Kolmogorov 0-1 Law|0–1 law]] and Borel–Cantelli divide the labour: the 0–1 law says the answer is $0$ *or* $1$; Borel–Cantelli says *which*.** Any tail event of an independent sequence — "$w$ infinitely often," "the series converges," "$\limsup X_n=\infty$" — has probability $0$ or $1$ by the 0–1 law, with *no computation*. That structural certainty turns the remaining question into a binary one, and the appropriate Borel–Cantelli lemma (convergent sum → $0$; divergent sum + independence → $1$) selects the value. Recognising "this is a tail event" first, then computing $\sum\mathbb{P}(A_n)$, is the standard two-step.
