---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Martingale"
  - "Def - Filtration"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $S_n=X_1+\cdots+X_n$ ($S_0=0$) be a random walk with i.i.d. steps $X_k$, and $\mathcal{F}_n=\sigma(X_1,\dots,X_n)$.

**(a)** If $\mathbb{E}[X_1]=0$, show $(S_n)$ is a [[Def - Martingale|martingale]].

**(b)** If additionally $\mathrm{Var}(X_1)=\sigma^2<\infty$, show $(S_n^2-n\sigma^2)$ is a martingale.

**(c)** If the steps are $\pm1$ fair, show $M_n=\theta^{S_n}$ for the right $\theta$, and find the exponential martingale $e^{uS_n}/\mathbb{E}[e^{uX_1}]^n$ in general.

**Recall:**

![[Def - Martingale#The Definition]]

---

# Convergent Strategy

**Problem class:** verifying the martingale property — checking $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n$.

**Assumption pattern:** the increment $X_{n+1}$ is *independent of $\mathcal{F}_n$*; $S_n$ is *$\mathcal{F}_n$-measurable*. So one splits the candidate into "$\mathcal{F}_n$-measurable part" (taken out) and "independent increment" (averaged) — the [[Thm - Properties of Conditional Expectation|two conditional rules]].

---

# Legal Operations Used

1. **Split into known $+$ independent**; take out the known, average the independent.
2. **Verify $\mathbb{E}[\text{candidate}_{n+1}\mid\mathcal{F}_n]=\text{candidate}_n$.**

---

# Hints

> [!note]- Hint 1
> $S_{n+1}=S_n+X_{n+1}$; $S_n$ is $\mathcal{F}_n$-measurable, $X_{n+1}$ independent of $\mathcal{F}_n$.

> [!note]- Hint 2
> (b): expand $S_{n+1}^2=(S_n+X_{n+1})^2$; the cross term has conditional mean $2S_n\mathbb{E}[X_{n+1}]=0$.

> [!note]- Hint 3
> (c): $e^{uS_{n+1}}=e^{uS_n}e^{uX_{n+1}}$; condition and use independence — $\mathbb{E}[e^{uX_{n+1}}\mid\mathcal{F}_n]=\mathbb{E}[e^{uX_1}]$.

---

# Solution

The proof breaks into three steps, one per sub-part. Step 1 (part a) verifies $\mathbb{E}[S_{n+1} \mid \mathcal{F}_n] = S_n + \mathbb{E}[X_{n+1}] = S_n$ by splitting into "$\mathcal{F}_n$-measurable + independent increment"; Step 2 (part b) expands $S_{n+1}^2 = (S_n + X_{n+1})^2$, conditions out the known $S_n$, sees the cross-term vanish, and absorbs $\mathbb{E}[X_{n+1}^2] = \sigma^2$ into the predictable compensator $-n\sigma^2$; Step 3 (part c) constructs the exponential martingale $e^{uS_n}/\mathbb{E}[e^{uX_1}]^n$ by the same independence-of-increment computation. The non-obvious move is the choice of normaliser in each case — the constant $\sigma^2$ in Step 2 and the moment-generating function in Step 3 are the *exactly right* compensators that drive the conditional mean back to the current value.

**Step 1 — (a).** $(S_n)$ is adapted and integrable ($\mathbb{E}|S_n|\le n\mathbb{E}|X_1|$). Since $X_{n+1}\perp\mathcal{F}_n$,
$$\mathbb{E}[S_{n+1}\mid\mathcal{F}_n]=\mathbb{E}[S_n+X_{n+1}\mid\mathcal{F}_n]=S_n+\mathbb{E}[X_{n+1}]=S_n+0=S_n.$$
A mean-zero random walk is a martingale.

**Step 2 — (b).** $S_{n+1}^2=(S_n+X_{n+1})^2=S_n^2+2S_nX_{n+1}+X_{n+1}^2$. Conditioning, with $S_n$ [[Thm - Properties of Conditional Expectation|taken out as known]] and $X_{n+1}\perp\mathcal{F}_n$:
$$\mathbb{E}[S_{n+1}^2\mid\mathcal{F}_n]=S_n^2+2S_n\,\mathbb{E}[X_{n+1}]+\mathbb{E}[X_{n+1}^2]=S_n^2+0+\sigma^2.$$
So $\mathbb{E}[S_{n+1}^2-(n+1)\sigma^2\mid\mathcal{F}_n]=S_n^2+\sigma^2-(n+1)\sigma^2=S_n^2-n\sigma^2$ — $(S_n^2-n\sigma^2)$ is a martingale.

**Step 3 — (c).** For $\pm1$ fair steps, $\mathbb{E}[\theta^{X_{n+1}}]=\tfrac12\theta+\tfrac12\theta^{-1}$, which equals $1$ iff $\theta+\theta^{-1}=2$, i.e. $\theta=1$ (trivial). For an *asymmetric* walk $\mathbb{P}(X=1)=p$, $\mathbb{P}(X=-1)=q$, $\mathbb{E}[\theta^X]=p\theta+q\theta^{-1}=1$ has the non-trivial root $\theta=q/p$, and $M_n=(q/p)^{S_n}$ is a martingale. In general, the **exponential martingale**: for any $u$ with $\mathbb{E}[e^{uX_1}]<\infty$,
$$M_n=\frac{e^{uS_n}}{\mathbb{E}[e^{uX_1}]^n},\qquad\mathbb{E}[M_{n+1}\mid\mathcal{F}_n]=M_n\cdot\frac{\mathbb{E}[e^{uX_{n+1}}\mid\mathcal{F}_n]}{\mathbb{E}[e^{uX_1}]}=M_n,$$
using $e^{uS_{n+1}}=e^{uS_n}e^{uX_{n+1}}$, taking out the known $e^{uS_n}$, and $X_{n+1}\perp\mathcal{F}_n$.

> [!note]- Complete formal solution
> (a) $\mathbb{E}[S_{n+1}\mid\mathcal{F}_n]=S_n+\mathbb{E}[X_{n+1}]=S_n$. (b) $\mathbb{E}[S_{n+1}^2\mid\mathcal{F}_n]=S_n^2+\sigma^2$ (cross term $0$, $\mathbb{E}X_{n+1}^2=\sigma^2$), so $S_n^2-n\sigma^2$ is a martingale. (c) $M_n=e^{uS_n}/\mathbb{E}[e^{uX_1}]^n$ is a martingale by independence; for asymmetric $\pm1$ steps $(q/p)^{S_n}$ works. $\blacksquare$

---

# Key Takeaways

**Three martingales accompany every random walk — $S_n$ (mean-zero case), $S_n^2-n\sigma^2$, and the exponential $e^{uS_n}/\mathbb{E}[e^{uX_1}]^n$ — and each is verified by the same split: known part out, independent increment averaged.** The increment $X_{n+1}$ is independent of the past $\mathcal{F}_n$, and the current state is $\mathcal{F}_n$-measurable; conditioning on $\mathcal{F}_n$ therefore *freezes the state and averages the increment*. This is the universal recipe for *checking* the martingale property — and these three martingales are the tools that, via [[Thm - Optional Stopping Theorem|optional stopping]], compute hitting probabilities ($S_n$ or $(q/p)^{S_n}$), expected hitting times ($S_n^2-n\sigma^2$), and exponential / large-deviation estimates (the exponential martingale).

**A martingale and a Markov walk are different structures, but harmonic/space-time functions of the walk are martingales.** $S_n$ itself is a martingale only when centred; $S_n^2$ is *not* a martingale (it is a [[Def - Martingale|submartingale]] — convex function of a martingale) but $S_n^2-n\sigma^2$ is, the "$-n\sigma^2$" being the [[Ex - The Doob decomposition|predictable compensator]] that removes the drift. The exponential martingale is the workhorse of the [[Thm - Cramér's Theorem|change-of-measure]] / tilting method. Recognising "which function of the walk is a martingale" is the move that unlocks optional stopping.
