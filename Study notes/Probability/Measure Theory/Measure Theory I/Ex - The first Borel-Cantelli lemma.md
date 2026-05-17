---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Measure and Measure Space"
  - "Thm - Properties of Measures"
tags: [analysis, measure-theory, probability]
---

# Problem Statement

Let $(X,\mathcal{A},\mu)$ be a measure space and $(A_k)_{k\ge 1}$ a sequence in $\mathcal{A}$. Define the **limit superior** of the sequence of sets,
$$\limsup_k A_k=\bigcap_{n=1}^\infty\bigcup_{k=n}^\infty A_k=\{x\in X : x\in A_k\text{ for infinitely many }k\}.$$

**(a)** Verify the set-theoretic identity $\limsup_k A_k=\{x : x\in A_k \text{ for infinitely many }k\}$ and that $\limsup_k A_k\in\mathcal{A}$.

**(b) (First Borel–Cantelli lemma.)** Show that if $\sum_{k=1}^\infty\mu(A_k)<\infty$, then $\mu(\limsup_k A_k)=0$.

**(c)** Interpret (b) when $\mu=\mathbb{P}$ is a probability measure: if the probabilities $\mathbb{P}(A_k)$ are summable, then almost surely only finitely many of the events $A_k$ occur.

**Recall:**

A [[Def - Measure and Measure Space|measure]] satisfies $\mu(\emptyset)=0$ and countable additivity. From [[Thm - Properties of Measures]] we use **monotonicity**, **continuity from above** (valid since the relevant first term has finite measure), and **$\sigma$-subadditivity**: $\mu(\bigcup_k B_k)\le\sum_k\mu(B_k)$.

---

# Convergent Strategy

**Problem class:** bounding the measure of a $\limsup$ of sets — a "tail event" — from a summability hypothesis.

**Assumption pattern:** the hypothesis is a *convergent series* $\sum\mu(A_k)<\infty$. Convergence of a series means its *tails* $\sum_{k\ge n}\mu(A_k)$ vanish as $n\to\infty$. The target set $\limsup A_k$ is, by construction, contained in *every* tail union $\bigcup_{k\ge n}A_k$. Pairing "target inside every tail union" with "tail sums $\to 0$" via $\sigma$-subadditivity is the whole proof.

**Theorem routing:** $\limsup A_k\subseteq\bigcup_{k\ge n}A_k$ (monotonicity) $\Rightarrow$ $\mu(\limsup A_k)\le\sum_{k\ge n}\mu(A_k)$ ($\sigma$-subadditivity) $\Rightarrow$ $0$ (let $n\to\infty$, convergent tail).

**Key decision point:** realising that one should *not* compute $\mu(\limsup A_k)$ directly, but bound it by an $n$-indexed quantity and then optimise over $n$.

---

# Legal Operations Used

1. **Sandwiching the target inside an indexed family** — $\limsup A_k\subseteq\bigcup_{k\ge n}A_k$ for every $n$.
2. **$\sigma$-subadditivity** to convert "measure of a union" into "sum of measures."
3. **Optimising a free index** — the bound holds for all $n$, so pass to $n\to\infty$.
4. **Tail of a convergent series $\to 0$.**

---

# Hints

> [!note]- Hint 1
> Do not try to compute $\mu(\limsup A_k)$ on the nose. Instead bound it. For every $n$, $\limsup_k A_k\subseteq\bigcup_{k=n}^\infty A_k$ — why?

> [!note]- Hint 2
> Apply monotonicity then $\sigma$-subadditivity to that inclusion: $\mu(\limsup A_k)\le\sum_{k=n}^\infty\mu(A_k)$. This holds for *every* $n$.

> [!note]- Hint 3
> The right-hand side is the tail of a convergent series. What happens as $n\to\infty$?

---

# Solution

**Step 1 — The $\limsup$ identity and measurability.** $x\in\bigcap_n\bigcup_{k\ge n}A_k$ means: for every $n$, $x$ lies in some $A_k$ with $k\ge n$ — i.e. $x$ lies in $A_k$ for infinitely many $k$. Each $\bigcup_{k\ge n}A_k\in\mathcal{A}$ (countable union), and the intersection over $n$ is again in $\mathcal{A}$.

> [!note]- Derivation
> If $x\in A_k$ for infinitely many $k$, then for each $n$ there is some such $k\ge n$, so $x\in\bigcup_{k\ge n}A_k$ for all $n$, hence $x\in\bigcap_n\bigcup_{k\ge n}A_k$. Conversely if $x$ is in only finitely many $A_k$, let $N$ be the largest such index; then $x\notin\bigcup_{k\ge N+1}A_k$, so $x\notin\limsup A_k$. Measurability: $\mathcal{A}$ is closed under countable unions and countable intersections.

**Step 2 — Sandwich and bound (the heart).** Fix $n$. Since $\limsup_k A_k=\bigcap_m\bigcup_{k\ge m}A_k\subseteq\bigcup_{k\ge n}A_k$, monotonicity and $\sigma$-subadditivity give
$$\mu\big(\limsup_k A_k\big)\ \le\ \mu\Big(\bigcup_{k=n}^\infty A_k\Big)\ \le\ \sum_{k=n}^\infty\mu(A_k).$$

> [!note]- Derivation
> The intersection $\bigcap_m(\cdots)$ is contained in its $m=n$ term $\bigcup_{k\ge n}A_k$, giving the first inequality by [[Thm - Properties of Measures|monotonicity]]. The union $\bigcup_{k\ge n}A_k$ is a countable union, so by [[Thm - Properties of Measures|σ-subadditivity]] its measure is at most $\sum_{k\ge n}\mu(A_k)$.

**Step 3 — Let $n\to\infty$.** The bound $\mu(\limsup A_k)\le\sum_{k\ge n}\mu(A_k)$ holds for *every* $n$. Since $\sum_{k\ge 1}\mu(A_k)<\infty$, its tails satisfy $\sum_{k\ge n}\mu(A_k)\to 0$ as $n\to\infty$. Hence $\mu(\limsup A_k)\le 0$, and being a measure value it equals $0$.

> [!note]- Derivation
> A nonnegative series converges iff its partial sums are bounded; convergence then forces the tail $\sum_{k\ge n}\mu(A_k)=\big(\sum_{k\ge 1}\big)-\big(\sum_{k<n}\big)\to 0$. The left side $\mu(\limsup A_k)$ does not depend on $n$, so it is $\le$ the infimum over $n$ of the right side, which is $0$.

**Step 4 — (c) Probabilistic reading.** With $\mu=\mathbb{P}$: $\limsup A_k$ is the event "infinitely many $A_k$ occur." Its complement, "only finitely many $A_k$ occur," then has probability $1$. So summable probabilities $\Rightarrow$ almost surely the events $A_k$ stop occurring.

> [!note]- Complete formal solution
> (a) $x\in\bigcap_n\bigcup_{k\ge n}A_k\iff\forall n\,\exists k\ge n: x\in A_k\iff x\in A_k$ for infinitely many $k$; the set lies in $\mathcal{A}$ by closure under countable unions and intersections. (b) For each $n$, $\limsup_k A_k\subseteq\bigcup_{k\ge n}A_k$, so by monotonicity and $\sigma$-subadditivity $\mu(\limsup A_k)\le\sum_{k\ge n}\mu(A_k)$. As $\sum_k\mu(A_k)<\infty$, the tail $\to 0$; hence $\mu(\limsup A_k)=0$. (c) For $\mathbb{P}$, $\mathbb{P}(\limsup A_k)=0$ means $\mathbb{P}(\text{infinitely many }A_k\text{ occur})=0$, equivalently a.s. only finitely many occur. $\blacksquare$

---

# Key Takeaways

**To bound the measure of a $\limsup$ set, sandwich it inside a tail union and exploit a free index.** The set $\limsup A_k$ resists direct computation, but it sits inside $\bigcup_{k\ge n}A_k$ for *every* $n$ — and a bound that holds for every value of a free parameter may be optimised over that parameter. This "prove an $n$-indexed inequality, then send $n\to\infty$" move is ubiquitous: it is the same idea as bounding a limit by every term of a sequence, or an infimum by every member of a family. The trigger is "the quantity I want does not depend on $n$, but my bound does."

**Summability of measures kills the $\limsup$ — this is the first Borel–Cantelli lemma, and it is nothing but $\sigma$-subadditivity plus a convergent tail.** Recognise the input type: whenever you can show $\sum_k\mu(A_k)<\infty$, you instantly know $\mu(\limsup A_k)=0$ — "almost no point is in infinitely many $A_k$." In probability this is the standard route to almost-sure statements: to prove $X_n\to X$ a.s. one shows $\sum_n\mathbb{P}(|X_n-X|>\varepsilon)<\infty$ and concludes the bad events occur only finitely often. The converse direction — divergent sum *plus independence* forcing $\mathbb{P}(\limsup)=1$ — is the [[Thm - Borel-Cantelli Lemmas|second Borel–Cantelli lemma]], where independence does the extra work.
