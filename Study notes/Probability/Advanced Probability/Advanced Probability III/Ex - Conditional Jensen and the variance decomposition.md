---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Thm - Properties of Conditional Expectation"
  - "Thm - Conditional Expectation as L2 Projection"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $X\in L^2(\Omega,\mathcal{F},\mathbb{P})$ and $\mathcal{G}\subseteq\mathcal{F}$.

**(a)** Use [[Thm - Properties of Conditional Expectation|conditional Jensen]] to show $\mathbb{E}[X\mid\mathcal{G}]^2\le\mathbb{E}[X^2\mid\mathcal{G}]$, hence the **$L^2$-contraction** $\|\mathbb{E}[X\mid\mathcal{G}]\|_2\le\|X\|_2$.

**(b)** Prove the **law of total variance**:
$$\mathrm{Var}(X)=\underbrace{\mathrm{Var}\big(\mathbb{E}[X\mid\mathcal{G}]\big)}_{\text{explained}}+\underbrace{\mathbb{E}\big[\mathrm{Var}(X\mid\mathcal{G})\big]}_{\text{unexplained}}.$$

**(c)** Interpret: conditioning *reduces* variance, and the reduction is the "explained" part.

**Recall:**

[[Thm - Properties of Conditional Expectation|Conditional Jensen]]; $\mathrm{Var}(X\mid\mathcal{G})=\mathbb{E}[X^2\mid\mathcal{G}]-\mathbb{E}[X\mid\mathcal{G}]^2$. [[Thm - Conditional Expectation as L2 Projection|Conditional expectation is L²-projection]].

---

# Convergent Strategy

**Problem class:** deriving the variance decomposition from the tower property and conditional Jensen.

**Assumption pattern:** $X\in L^2$; conditional Jensen with $\varphi(x)=x^2$ gives the pointwise inequality, the tower property converts conditional identities into unconditional ones by taking $\mathbb{E}$.

---

# Legal Operations Used

1. **Conditional Jensen** with $\varphi(x)=x^2$.
2. **Tower property** $\mathbb{E}[\mathbb{E}[\cdot\mid\mathcal{G}]]=\mathbb{E}[\cdot]$.
3. **Expand and recombine** conditional second moments.

---

# Hints

> [!note]- Hint 1
> Conditional Jensen with $\varphi(x)=x^2$: $\mathbb{E}[X^2\mid\mathcal{G}]\ge\mathbb{E}[X\mid\mathcal{G}]^2$. Take $\mathbb{E}$ and use the tower property.

> [!note]- Hint 2
> $\mathrm{Var}(X)=\mathbb{E}[X^2]-(\mathbb{E}X)^2$. Write $\mathbb{E}[X^2]=\mathbb{E}[\mathbb{E}[X^2\mid\mathcal{G}]]$ and split.

> [!note]- Hint 3
> $\mathbb{E}[X^2\mid\mathcal{G}]=\mathrm{Var}(X\mid\mathcal{G})+\mathbb{E}[X\mid\mathcal{G}]^2$ — rearrange the definition of conditional variance.

---

# Solution

The proof breaks into three steps, one per sub-part. Step 1 (part a) applies conditional Jensen with $\varphi(x) = x^2$ to get $\mathbb{E}[X^2 \mid \mathcal{G}] \geq \mathbb{E}[X \mid \mathcal{G}]^2$, then takes unconditional expectations using the tower property to read off the $L^2$-contraction; Step 2 (part b) rearranges the conditional variance identity $\mathbb{E}[X^2\mid\mathcal{G}] = \mathrm{Var}(X\mid\mathcal{G}) + \mathbb{E}[X\mid\mathcal{G}]^2$, takes $\mathbb{E}$, and subtracts $(\mathbb{E}X)^2$ to extract the total variance decomposition; Step 3 (part c) interprets the result as the Pythagorean split into explained and unexplained variance. The non-obvious move is the tower-property bridge — turning every conditional statement into an unconditional one is the only way to convert "Jensen at a.s." into a global norm inequality.

**Step 1 — (a) $L^2$-contraction.** [[Thm - Properties of Conditional Expectation|Conditional Jensen]] with the convex $\varphi(x)=x^2$:
$$\mathbb{E}[X^2\mid\mathcal{G}]\ge\big(\mathbb{E}[X\mid\mathcal{G}]\big)^2\quad\text{a.s.}$$
Take unconditional expectations and apply the [[Thm - Properties of Conditional Expectation|tower property]] to the left side:
$$\mathbb{E}[X^2]=\mathbb{E}\big[\mathbb{E}[X^2\mid\mathcal{G}]\big]\ge\mathbb{E}\big[\mathbb{E}[X\mid\mathcal{G}]^2\big]=\big\|\mathbb{E}[X\mid\mathcal{G}]\big\|_2^2.$$
So $\|\mathbb{E}[X\mid\mathcal{G}]\|_2\le\|X\|_2$ — conditional expectation is an $L^2$-contraction. (Geometrically, [[Thm - Conditional Expectation as L2 Projection|this is "an orthogonal projection does not increase the norm"]].)

**Step 2 — (b) Law of total variance.** By definition $\mathrm{Var}(X\mid\mathcal{G})=\mathbb{E}[X^2\mid\mathcal{G}]-\mathbb{E}[X\mid\mathcal{G}]^2$, so
$$\mathbb{E}[X^2\mid\mathcal{G}]=\mathrm{Var}(X\mid\mathcal{G})+\mathbb{E}[X\mid\mathcal{G}]^2.$$
Take $\mathbb{E}$ and use the [[Thm - Properties of Conditional Expectation|tower property]] $\mathbb{E}[\mathbb{E}[X^2\mid\mathcal{G}]]=\mathbb{E}[X^2]$:
$$\mathbb{E}[X^2]=\mathbb{E}[\mathrm{Var}(X\mid\mathcal{G})]+\mathbb{E}\big[\mathbb{E}[X\mid\mathcal{G}]^2\big].$$
Now subtract $(\mathbb{E}X)^2$. Since $\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]]=\mathbb{E}[X]$ (tower property again), $(\mathbb{E}X)^2=(\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]])^2$, and so $\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]^2]-(\mathbb{E}X)^2=\mathrm{Var}(\mathbb{E}[X\mid\mathcal{G}])$. Hence
$$\mathrm{Var}(X)=\mathbb{E}[X^2]-(\mathbb{E}X)^2=\mathbb{E}[\mathrm{Var}(X\mid\mathcal{G})]+\mathrm{Var}\big(\mathbb{E}[X\mid\mathcal{G}]\big).$$

**Step 3 — (c) Interpretation.** Both terms are non-negative, so $\mathrm{Var}(\mathbb{E}[X\mid\mathcal{G}])\le\mathrm{Var}(X)$ — **conditioning (then averaging) never increases variance**; predicting $X$ by $\mathbb{E}[X\mid\mathcal{G}]$ removes the variance $\mathbb{E}[\mathrm{Var}(X\mid\mathcal{G})]$, the *unexplained / residual* part, leaving $\mathrm{Var}(\mathbb{E}[X\mid\mathcal{G}])$, the *explained* part. This is the Pythagorean variance split of [[Thm - Conditional Expectation as L2 Projection|L²-projection]] — total $=$ explained $+$ residual — and the basis of ANOVA, the coefficient of determination $R^2$, and Rao–Blackwell estimator improvement.

> [!note]- Complete formal solution
> (a) Conditional Jensen ($\varphi=x^2$): $\mathbb{E}[X^2\mid\mathcal{G}]\ge\mathbb{E}[X\mid\mathcal{G}]^2$; take $\mathbb{E}$, tower property $\Rightarrow\mathbb{E}[X^2]\ge\|\mathbb{E}[X\mid\mathcal{G}]\|_2^2$. (b) $\mathbb{E}[X^2\mid\mathcal{G}]=\mathrm{Var}(X\mid\mathcal{G})+\mathbb{E}[X\mid\mathcal{G}]^2$; take $\mathbb{E}$, subtract $(\mathbb{E}X)^2$, use the tower property to get $\mathrm{Var}(X)=\mathbb{E}[\mathrm{Var}(X\mid\mathcal{G})]+\mathrm{Var}(\mathbb{E}[X\mid\mathcal{G}])$. (c) Both terms $\ge0$, so conditioning reduces variance by the explained part. $\blacksquare$

---

# Key Takeaways

**The law of total variance — $\mathrm{Var}(X)=\mathrm{Var}(\mathbb{E}[X\mid\mathcal{G}])+\mathbb{E}[\mathrm{Var}(X\mid\mathcal{G})]$ — is the Pythagorean theorem for [[Thm - Conditional Expectation as L2 Projection|conditional expectation as projection]].** It splits total variability into an *explained* part (the variance of the prediction) and an *unexplained* part (the mean residual variance), and it is derived in two lines from the *tower property* (the only tool that turns conditional identities into unconditional ones) plus the algebra of conditional variance. It is the foundation of analysis of variance, of $R^2$, and of Rao–Blackwellisation — conditioning on a sufficient statistic strictly improves an estimator's variance.

**Conditioning never increases variance — and more generally conditional expectation is an $L^p$-contraction — because it is an orthogonal projection.** [[Thm - Properties of Conditional Expectation|Conditional Jensen]] applied to $\varphi=|\cdot|^p$, followed by the tower property, gives $\|\mathbb{E}[X\mid\mathcal{G}]\|_p\le\|X\|_p$; geometrically this is just "projecting onto a [[Def - Subspace|subspace]] shortens vectors." This contraction is what makes the family $\{\mathbb{E}[X\mid\mathcal{G}]\}$ [[Def - Uniform Integrability|uniformly integrable]] (for fixed $X\in L^1$), the fact behind the $L^1$-convergence of [[Def - Martingale|martingales]] — and it confirms that taking a conditional expectation is always a *smoothing*, never a sharpening, operation.
