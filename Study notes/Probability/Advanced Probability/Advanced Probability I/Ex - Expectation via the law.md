---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Random Variable"
  - "Def - Expectation and Moments"
  - "Thm - Monotone Convergence Theorem"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $X$ be a [[Def - Random Variable|random variable]] on $(\Omega,\mathcal{F},\mathbb{P})$ with [[Def - Random Variable|law]] $\mu_X$, and $h:\mathbb{R}\to\mathbb{R}$ Borel.

**(a)** Prove the **change-of-variables / law formula**: for $h\ge0$,
$$\mathbb{E}[h(X)]=\int_\Omega h(X)\,d\mathbb{P}=\int_\mathbb{R}h(x)\,d\mu_X(x),$$
and the same for $h$ with $h(X)\in L^1$.

**(b)** Deduce that $\mathbb{E}[X^k]$, $\mathrm{Var}(X)$, and $\mathbb{P}(X\in B)$ depend only on $\mu_X$ — hence two random variables with the same law have the same moments.

**(c)** Conclude that one may always replace the abstract space by $(\mathbb{R},\mathcal{B}(\mathbb{R}),\mu_X)$ with $X=\mathrm{id}$.

**Recall:**

The [[Def - Random Variable|law]] is $\mu_X(B)=\mathbb{P}(X\in B)$. [[Thm - Monotone Convergence Theorem|MCT]] and the [[Thm - Approximation by Simple Functions|standard machine]].

---

# Convergent Strategy

**Problem class:** proving an integral identity — the standard machine (indicators → simple → MCT).

**Assumption pattern:** $\mu_X$ is the *pushforward* of $\mathbb{P}$ under $X$; the identity $\mathbb{E}[h(X)]=\int h\,d\mu_X$ is the abstract change-of-variables for a pushforward measure, proved by the four-step ladder.

**Theorem routing:** indicators ($h=\mathbf{1}_B$: both sides $=\mu_X(B)$), linearity (simple $h$), [[Thm - Monotone Convergence Theorem|MCT]] ($h\ge0$), $h=h^+-h^-$ (signed).

---

# Legal Operations Used

1. **The standard machine** — indicators, simple, MCT, signed.
2. **Pushforward identity** $\mu_X=X_*\mathbb{P}$.

---

# Hints

> [!note]- Hint 1
> For $h=\mathbf{1}_B$: $h(X)=\mathbf{1}_{\{X\in B\}}$, so $\mathbb{E}[h(X)]=\mathbb{P}(X\in B)=\mu_X(B)=\int\mathbf{1}_B\,d\mu_X$.

> [!note]- Hint 2
> Extend by linearity to simple $h$, then by MCT to $h\ge0$ (simple $h_n\uparrow h$), then split $h=h^+-h^-$.

---

# Solution

**Step 1 — (a).** Run the standard machine.

> [!note]- Derivation
> *Indicators.* For $h=\mathbf{1}_B$, $B$ Borel: $h(X)=\mathbf{1}_{\{X\in B\}}$, so $\mathbb{E}[h(X)]=\mathbb{P}(X\in B)=\mu_X(B)=\int_\mathbb{R}\mathbf{1}_B\,d\mu_X$. The identity holds.
> *Simple.* For $h=\sum_i\alpha_i\mathbf{1}_{B_i}$, [[Thm - Properties of the Integral|linearity]] of both integrals gives the identity.
> *Non-negative.* For $h\ge0$ Borel, take simple $h_n\uparrow h$ ([[Thm - Approximation by Simple Functions]]). Then $h_n(X)\uparrow h(X)$, and [[Thm - Monotone Convergence Theorem|MCT]] applied on $\Omega$ and on $\mathbb{R}$ gives $\mathbb{E}[h(X)]=\lim\mathbb{E}[h_n(X)]=\lim\int h_n\,d\mu_X=\int h\,d\mu_X$.
> *Signed.* For $h(X)\in L^1$, split $h=h^+-h^-$; both parts are non-negative with finite integral, subtract.

**Step 2 — (b).** Taking $h(x)=x^k$ gives $\mathbb{E}[X^k]=\int x^k\,d\mu_X$ — the $k$-th moment is an integral against $\mu_X$ alone. $\mathrm{Var}(X)=\int x^2\,d\mu_X-(\int x\,d\mu_X)^2$, again only $\mu_X$. And $\mathbb{P}(X\in B)=\mu_X(B)$ by definition. So if $\mu_X=\mu_Y$ then $X$ and $Y$ have identical moments, variance, and tail probabilities.

**Step 3 — (c).** Since every probabilistic quantity attached to $X$ alone is an integral against $\mu_X$, nothing is lost by working on the **canonical space** $(\mathbb{R},\mathcal{B}(\mathbb{R}),\mu_X)$ with the random variable $\mathrm{id}:\mathbb{R}\to\mathbb{R}$ — it has law $\mu_X$ and reproduces every such quantity.

> [!note]- Complete formal solution
> (a) Standard machine: the identity holds for indicators ($\mathbb{E}[\mathbf{1}_B(X)]=\mu_X(B)$), extends by linearity to simple $h$, by MCT to $h\ge0$, by $h=h^+-h^-$ to integrable $h$. (b) $\mathbb{E}[X^k]=\int x^k d\mu_X$, $\mathrm{Var}(X)$, $\mathbb{P}(X\in B)$ are all integrals against $\mu_X$. (c) Hence $(\mathbb{R},\mathcal{B},\mu_X,\mathrm{id})$ reproduces everything. $\blacksquare$

---

# Key Takeaways

**Everything about a random variable in isolation is encoded in its law — the abstract probability space is scaffolding that can always be discarded.** The change-of-variables formula $\mathbb{E}[h(X)]=\int h\,d\mu_X$ converts every expectation, moment, and tail probability into an integral on $\mathbb{R}$ against the law. This is why probabilists compute with densities and distribution functions and never mention $\Omega$: by (c) one may *take* $\Omega=\mathbb{R}$, $\mathbb{P}=\mu_X$, $X=\mathrm{id}$. Two variables with the same law are probabilistically identical even on different spaces.

**The proof is the standard machine — and recognising "this is a pushforward identity" tells you the machine will work.** Indicators, simple functions, [[Thm - Monotone Convergence Theorem|MCT]], signed split: the same four steps that prove [[Thm - Fubini-Tonelli Theorem|Fubini]] and linearity. Whenever an identity relates an integral on one space to an integral on another via a measurable map, the pushforward/change-of-variables formula is the statement, and the standard machine is the proof.
