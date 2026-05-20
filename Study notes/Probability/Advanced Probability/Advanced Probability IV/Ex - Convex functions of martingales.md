---
type: exercise
subject: advanced-probability
difficulty: "⭐"
prereqs:
  - "Def - Martingale"
  - "Thm - Properties of Conditional Expectation"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $(M_n)$ be a [[Def - Martingale|martingale]] and $\varphi:\mathbb{R}\to\mathbb{R}$ convex with $\varphi(M_n)\in L^1$ for all $n$.

**(a)** Show $(\varphi(M_n))$ is a **submartingale**. In particular $(|M_n|)$ and $(M_n^2)$ are submartingales.

**(b)** Show that if $(M_n)$ is merely a *submartingale* and $\varphi$ is convex *and non-decreasing*, then $(\varphi(M_n))$ is still a submartingale.

**(c)** Explain why this is the source of [[Thm - Doob's Maximal Inequality|Doob's Lᵖ inequality]].

**Recall:**

[[Thm - Properties of Conditional Expectation|Conditional Jensen]]: $\mathbb{E}[\varphi(X)\mid\mathcal{G}]\ge\varphi(\mathbb{E}[X\mid\mathcal{G}])$ for convex $\varphi$.

---

# Convergent Strategy

**Problem class:** establishing the submartingale property by combining the martingale identity with [[Thm - Properties of Conditional Expectation|conditional Jensen]].

**Assumption pattern:** $(M_n)$ a martingale means $\mathbb{E}[M_{n+1}\mid\mathcal{F}_n]=M_n$ *exactly*; conditional Jensen turns "$\varphi$ of a conditional expectation" into "conditional expectation of $\varphi$" — combining them gives a one-sided inequality.

---

# Legal Operations Used

1. **Conditional Jensen**, then the **martingale identity**.
2. **Monotonicity of $\varphi$** to handle the submartingale case.

---

# Hints

> [!note]- Hint 1
> $\mathbb{E}[\varphi(M_{n+1})\mid\mathcal{F}_n]\ge\varphi(\mathbb{E}[M_{n+1}\mid\mathcal{F}_n])$ — conditional Jensen.

> [!note]- Hint 2
> For a martingale $\mathbb{E}[M_{n+1}\mid\mathcal{F}_n]=M_n$; substitute.

> [!note]- Hint 3
> For (b), a submartingale has $\mathbb{E}[M_{n+1}\mid\mathcal{F}_n]\ge M_n$; apply the *non-decreasing* $\varphi$ to both sides.

---

# Solution

The proof breaks into three steps, one per sub-part. Step 1 (part a) combines conditional Jensen $\mathbb{E}[\varphi(M_{n+1}) \mid \mathcal{F}_n] \geq \varphi(\mathbb{E}[M_{n+1} \mid \mathcal{F}_n])$ with the martingale identity $\mathbb{E}[M_{n+1} \mid \mathcal{F}_n] = M_n$ to read off the submartingale property; Step 2 (part b) handles the submartingale case by additionally invoking monotonicity of $\varphi$ to chain $\varphi(\mathbb{E}[M_{n+1} \mid \mathcal{F}_n]) \geq \varphi(M_n)$; Step 3 (part c) explains why this is the bridge that lets Doob's inequalities (stated for non-negative submartingales) apply to martingales via $\varphi(x) = |x|^p$. The non-obvious move in Step 2 is the role of monotonicity — without it, applying $\varphi$ to the submartingale inequality could flip it.

**Step 1 — (a).** $\varphi(M_n)$ is adapted and integrable by hypothesis. By [[Thm - Properties of Conditional Expectation|conditional Jensen]] and the martingale identity,
$$\mathbb{E}[\varphi(M_{n+1})\mid\mathcal{F}_n]\ \ge\ \varphi\big(\mathbb{E}[M_{n+1}\mid\mathcal{F}_n]\big)\ =\ \varphi(M_n).$$
So $(\varphi(M_n))$ is a submartingale. Taking $\varphi(x)=|x|$ and $\varphi(x)=x^2$: $(|M_n|)$ and $(M_n^2)$ are submartingales.

**Step 2 — (b).** For a submartingale, $\mathbb{E}[M_{n+1}\mid\mathcal{F}_n]\ge M_n$. Conditional Jensen still gives $\mathbb{E}[\varphi(M_{n+1})\mid\mathcal{F}_n]\ge\varphi(\mathbb{E}[M_{n+1}\mid\mathcal{F}_n])$; now apply the *non-decreasing* $\varphi$ to the submartingale inequality $\mathbb{E}[M_{n+1}\mid\mathcal{F}_n]\ge M_n$ to get $\varphi(\mathbb{E}[M_{n+1}\mid\mathcal{F}_n])\ge\varphi(M_n)$. Chaining, $\mathbb{E}[\varphi(M_{n+1})\mid\mathcal{F}_n]\ge\varphi(M_n)$. (Monotonicity of $\varphi$ is essential here — without it, applying $\varphi$ could reverse the submartingale inequality.)

**Step 3 — (c).** [[Thm - Doob's Maximal Inequality|Doob's inequalities]] are stated for *non-negative submartingales*. Given a martingale $(M_n)$, part (a) with $\varphi(x)=|x|^p$ ($p\ge1$, convex) makes $(|M_n|^p)$ a non-negative submartingale — *exactly the object Doob's maximal and $L^p$ inequalities require*. So this exercise is the bridge: it is what lets the maximal inequality, naturally a submartingale statement, be applied to *martingales*.

> [!note]- Complete formal solution
> (a) Conditional Jensen $+$ martingale identity: $\mathbb{E}[\varphi(M_{n+1})\mid\mathcal{F}_n]\ge\varphi(\mathbb{E}[M_{n+1}\mid\mathcal{F}_n])=\varphi(M_n)$. (b) For a submartingale, conditional Jensen gives $\ge\varphi(\mathbb{E}[M_{n+1}\mid\mathcal{F}_n])$, and non-decreasing $\varphi$ gives $\varphi(\mathbb{E}[M_{n+1}\mid\mathcal{F}_n])\ge\varphi(M_n)$. (c) $\varphi=|\cdot|^p$ makes $|M_n|^p$ a non-negative submartingale, the input to Doob's inequalities. $\blacksquare$

---

# Key Takeaways

**A convex function of a martingale is a submartingale — conditional Jensen plus the martingale identity, one line.** This is the most-used structural fact about martingales after the definition itself: $|M_n|$, $M_n^2$, $|M_n|^p$, $e^{uM_n}$ are all submartingales. The mechanism — [[Thm - Properties of Conditional Expectation|conditional Jensen]] produces "$\ge\varphi(\mathbb{E}[M_{n+1}\mid\mathcal{F}_n])$", the martingale identity collapses the inner term to $M_n$ — is worth internalising as a single move. For a *submartingale* base the same works *if $\varphi$ is also non-decreasing*, the monotonicity preventing the submartingale inequality from flipping.

**This is the lemma that lets submartingale theorems be applied to martingales — most importantly [[Thm - Doob's Maximal Inequality|Doob's Lᵖ inequality]].** Doob's maximal and $L^p$ inequalities are naturally about non-negative submartingales; $\varphi(x)=|x|^p$ converts a martingale into exactly such an object, so the inequalities reach all martingales. The same construction makes the [[Thm - Almost Sure Martingale Convergence|convergence theory]] and the analysis of $\mathbb{E}[|M_n|^p]$ possible. Convexity is the bridge between the martingale property (an equality) and the submartingale inequalities that carry the hard analysis.
