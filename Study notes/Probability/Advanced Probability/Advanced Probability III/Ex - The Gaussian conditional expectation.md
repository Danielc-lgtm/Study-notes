---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Conditional Expectation"
  - "Thm - Conditional Expectation as L2 Projection"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $(X,W)$ be jointly Gaussian, mean zero, with $\mathrm{Var}(W)>0$.

**(a)** Show that $\mathbb{E}[X\mid W]$ is a *linear* function of $W$: $\mathbb{E}[X\mid W]=aW$ with $a=\mathrm{Cov}(X,W)/\mathrm{Var}(W)$.

**(b)** Show the residual $X-\mathbb{E}[X\mid W]$ is *independent* of $W$ (not merely uncorrelated).

**(c)** Conclude that for jointly Gaussian variables, "best predictor" $=$ "best *linear* predictor," and conditioning preserves Gaussianity.

**Recall:**

[[Thm - Conditional Expectation as L2 Projection|Conditional expectation is $L^2$-projection]]. For Gaussians, *uncorrelated $\Rightarrow$ independent*.

---

# Convergent Strategy

**Problem class:** computing a conditional expectation by *guessing the form* (linear) and pinning the coefficient by orthogonality.

**Assumption pattern:** $(X,W)$ Gaussian. The decisive Gaussian fact: a linear combination of jointly Gaussian variables is Gaussian, and *uncorrelated jointly Gaussian variables are independent*. So if a linear $aW$ makes the residual *uncorrelated* with $W$, the residual is in fact *independent*, hence the conditioning is fully resolved.

**Theorem routing:** propose $Y=aW$; choose $a$ so $X-aW\perp W$ ($L^2$-orthogonality); Gaussianity upgrades orthogonality to independence; verify $Y$ is the conditional expectation.

---

# Legal Operations Used

1. **Propose a linear candidate**, pin the coefficient by orthogonality.
2. **Gaussian uncorrelated $\Rightarrow$ independent.**
3. **Verify the two characterising properties.**

---

# Hints

> [!note]- Hint 1
> Try $Y=aW$. Choose $a$ so $\mathrm{Cov}(X-aW,W)=0$, i.e. $a=\mathrm{Cov}(X,W)/\mathrm{Var}(W)$.

> [!note]- Hint 2
> $X-aW$ and $W$ are jointly Gaussian (linear images of $(X,W)$) and uncorrelated — so *independent*.

> [!note]- Hint 3
> Independence of $X-aW$ from $W$ gives $\mathbb{E}[(X-aW)\mathbf{1}_A]=0$ for $A\in\sigma(W)$ — the averaging identity.

---

# Solution

**Step 1 — (a),(b).** Set $a=\mathrm{Cov}(X,W)/\mathrm{Var}(W)$ and $R=X-aW$. Then
$$\mathrm{Cov}(R,W)=\mathrm{Cov}(X,W)-a\,\mathrm{Var}(W)=\mathrm{Cov}(X,W)-\mathrm{Cov}(X,W)=0,$$
so $R$ and $W$ are *uncorrelated*. Crucially, $R$ and $W$ are jointly Gaussian — both are linear combinations of the jointly Gaussian pair $(X,W)$ — and **for jointly Gaussian variables, uncorrelated implies independent**. So $R=X-\mathbb{E}[X\mid W]$ is *independent* of $W$, the conclusion of (b).

> [!note]- Derivation
> Now verify $Y=aW$ is the conditional expectation. $Y$ is $\sigma(W)$-measurable. For $A\in\sigma(W)$, $\mathbf{1}_A$ is a function of $W$, hence independent of $R$, so $\mathbb{E}[R\mathbf{1}_A]=\mathbb{E}[R]\mathbb{E}[\mathbf{1}_A]=0$ (using $\mathbb{E}[R]=\mathbb{E}X-a\mathbb{E}W=0$). Therefore $\mathbb{E}[X\mathbf{1}_A]=\mathbb{E}[(aW+R)\mathbf{1}_A]=\mathbb{E}[aW\mathbf{1}_A]=\mathbb{E}[Y\mathbf{1}_A]$ — the averaging identity. By [[Thm - Existence and Uniqueness of Conditional Expectation|uniqueness]], $\mathbb{E}[X\mid W]=aW$ with $a=\mathrm{Cov}(X,W)/\mathrm{Var}(W)$.

**Step 2 — (c).** Several conclusions. The conditional expectation is *linear in $W$* — so for jointly Gaussian variables the **best mean-square predictor coincides with the best *linear* predictor** (the linear regression line). The residual is not just uncorrelated but *independent* of $W$, so the conditional law of $X$ given $W$ is the law of $aW+R$ with $R\perp W$ Gaussian — a Gaussian with mean $aW$ and *variance not depending on $W$*. **Conditioning a Gaussian on a Gaussian yields a Gaussian** — the family is closed under conditioning, the fact behind the Kalman filter.

> [!note]- Complete formal solution
> (a),(b) With $a=\mathrm{Cov}(X,W)/\mathrm{Var}(W)$, $R=X-aW$ has $\mathrm{Cov}(R,W)=0$; $R,W$ jointly Gaussian and uncorrelated $\Rightarrow$ independent. Then $aW$ is $\sigma(W)$-measurable and $\mathbb{E}[X\mathbf{1}_A]=\mathbb{E}[aW\mathbf{1}_A]$ for $A\in\sigma(W)$ (as $\mathbb{E}[R\mathbf{1}_A]=0$ by independence); uniqueness gives $\mathbb{E}[X\mid W]=aW$. (c) Linear best predictor; conditional law Gaussian with $W$-independent variance. $\blacksquare$

---

# Key Takeaways

**For jointly Gaussian variables, conditional expectation is *linear* — the best predictor equals the best *linear* predictor.** This is the Gaussian world's defining simplification: $\mathbb{E}[X\mid W]=\frac{\mathrm{Cov}(X,W)}{\mathrm{Var}(W)}W$, the regression line, with the coefficient pinned by orthogonality ([[Thm - Conditional Expectation as L2 Projection|$L^2$-projection]]). In general, conditional expectation is some complicated nonlinear function of the conditioning variable; Gaussianity collapses it to a line. This is why Gaussian models — linear regression, the Kalman filter, Gaussian processes — are so tractable: projection onto *all* $\sigma(W)$-measurable functions gives the same answer as projection onto the *linear* span of $W$.

**The engine is "jointly Gaussian $+$ uncorrelated $\Rightarrow$ independent" — a property unique to the Gaussian family.** Choosing the coefficient to make the residual *uncorrelated* with $W$ is just $L^2$-orthogonality, available for any $X,W$; but for Gaussians that orthogonality *upgrades to full independence*, which is what makes the conditional law itself Gaussian with a $W$-independent variance. For non-Gaussian variables, orthogonality of the residual does *not* give independence, and the conditional expectation need not be linear. Whenever a problem says "jointly Gaussian," reach for "uncorrelated $=$ independent" and expect everything to linearise.
