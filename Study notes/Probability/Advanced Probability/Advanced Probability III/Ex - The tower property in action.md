---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Thm - Properties of Conditional Expectation"
  - "Def - Conditional Expectation"
tags: [probability, advanced-probability]
---

# Problem Statement

**(a)** Compute $\mathbb{E}[X]$ for $X$ a random sum $X=\sum_{k=1}^N Y_k$, where $N$ is a random variable taking values in $\mathbb{N}$, the $Y_k$ are i.i.d. with mean $m$, and $N$ is independent of $(Y_k)$. (**Wald's identity**.)

**(b)** Identify where the [[Thm - Properties of Conditional Expectation|tower property]] and *taking out what is known* are used.

**(c)** State the general principle: to compute $\mathbb{E}[X]$, *condition on an auxiliary variable, compute the inner expectation, then average* — $\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid Z]]$.

**Recall:**

[[Thm - Properties of Conditional Expectation|Tower property]]: $\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]]=\mathbb{E}[X]$. *Taking out what is known*: $\mathcal{G}$-measurable factors pass through $\mathbb{E}[\cdot\mid\mathcal{G}]$.

---

# Convergent Strategy

**Problem class:** computing an expectation by *conditioning on an auxiliary variable* — the tower property as a computational device.

**Assumption pattern:** $X$ is hard to average directly (the *number* of summands is itself random), but *given $N=n$* it is a plain sum of $n$ i.i.d. variables, trivial to average. So condition on $N$, compute the inner expectation, then average over $N$.

**Theorem routing:** $\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid N]]$ (tower); $\mathbb{E}[X\mid N]=Nm$ (inner computation).

---

# Legal Operations Used

1. **Condition on an auxiliary variable**; apply the tower property.
2. **Compute the inner conditional expectation** in the now-deterministic count.
3. **Average the result.**

---

# Hints

> [!note]- Hint 1
> $\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid N]]$ by the tower property. Compute the inner $\mathbb{E}[X\mid N]$ first.

> [!note]- Hint 2
> Given $N=n$, $X=\sum_{k=1}^n Y_k$ — a fixed number of summands. Use independence of $N$ from $(Y_k)$.

> [!note]- Hint 3
> $\mathbb{E}[X\mid N]=N\cdot m$. Then average: $\mathbb{E}[X]=\mathbb{E}[Nm]=m\,\mathbb{E}[N]$.

---

# Solution

**Step 1 — (a),(b) Wald's identity.** By the [[Thm - Properties of Conditional Expectation|tower property]],
$$\mathbb{E}[X]=\mathbb{E}\big[\mathbb{E}[X\mid N]\big].$$
Compute the inner conditional expectation. On $\{N=n\}$, $X=\sum_{k=1}^n Y_k$; since $N$ is independent of $(Y_k)$,
$$\mathbb{E}[X\mid N]=\mathbb{E}\Big[\sum_{k=1}^N Y_k\,\Big|\,N\Big]=\sum_{k=1}^N\mathbb{E}[Y_k\mid N]=\sum_{k=1}^N\mathbb{E}[Y_k]=N\,m.$$

> [!note]- Derivation
> Two properties are used. The number of summands $N$ is $\sigma(N)$-measurable, so it is *taken out as known* — the sum "$\sum_{k=1}^N$" is, given $N$, a deterministic finite sum, and linearity of conditional expectation applies term by term. And $\mathbb{E}[Y_k\mid N]=\mathbb{E}[Y_k]=m$ because $Y_k$ is *independent of $N$* ([[Thm - Properties of Conditional Expectation|independence property]]). Hence $\mathbb{E}[X\mid N]=Nm$.
> Now the *outer* expectation (the tower property's second half): $\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid N]]=\mathbb{E}[Nm]=m\,\mathbb{E}[N]$. This is **Wald's identity**: the mean of a random sum is (mean of one term) $\times$ (mean number of terms).

**Step 2 — (c) The principle.** The computation exemplifies a universal device: when $X$ is hard to average directly but becomes simple *once an auxiliary variable $Z$ is fixed*, write $\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid Z]]$ — condition on $Z$, compute the inner expectation (now a deterministic-structure problem), then average over $Z$. The tower property is what licenses this two-stage computation.

> [!note]- Complete formal solution
> By the tower property $\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid N]]$. Given $N$, $X=\sum_{k\le N}Y_k$ with $N$ taken out as known; $\mathbb{E}[Y_k\mid N]=m$ by independence; so $\mathbb{E}[X\mid N]=Nm$. Averaging, $\mathbb{E}[X]=m\,\mathbb{E}[N]$ — Wald's identity. The general principle: $\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid Z]]$, condition–compute–average. $\blacksquare$

---

# Key Takeaways

**The tower property is a *computational engine*: to find a hard expectation, condition on an auxiliary variable, compute the easy inner expectation, then average.** $\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid Z]]$ splits a difficult averaging into two manageable stages — and the art is choosing $Z$ so that "$X$ given $Z$" has *deterministic structure*. Wald's identity is the prototype: a *random* number of summands becomes a *fixed* number once $N$ is conditioned on. This "condition–compute–average" is one of the most-used techniques in all of probability — first-step analysis of Markov chains, branching-process means, and recursive expectations all run on it.

**Two conditional-expectation rules do the work, and recognising them is the skill: *taking out what is known* and the *independence property*.** The conditioning variable $N$, being $\sigma(N)$-measurable, is "frozen" — pulled out of the conditional expectation as a constant; and any summand *independent* of $N$ has conditional mean equal to its unconditional mean. Together they collapse $\mathbb{E}[\sum_{k\le N}Y_k\mid N]$ to $Nm$. Whenever a quantity depends on "an amount" and "a count" with one independent of the other, this pairing — take out the count, average the amount — is the move.
