---
type: theorem
subject: advanced-probability
prereqs:
  - "Def - Conditional Expectation"
  - "Thm - Completeness of Lp Spaces"
  - "Ex - The Cauchy-Schwarz inequality and L2 geometry"
tags: [probability, advanced-probability]
---

# Notation

$X\in L^2(\Omega,\mathcal{F},\mathbb{P})$; $\mathcal{G}\subseteq\mathcal{F}$ a sub-$\sigma$-algebra; $L^2(\mathcal{G})=L^2(\Omega,\mathcal{G},\mathbb{P})$.

---

# Motivation

[[Def - Conditional Expectation|Conditional expectation]] for $X\in L^2$ has a purely *geometric* meaning: it is the **orthogonal projection** of $X$ onto the [[Def - Subspace|subspace]] of $\mathcal{G}$-measurable square-integrable functions — the **best $\mathcal{G}$-measurable approximation of $X$ in mean square**. This identification is illuminating in two directions: it gives the cleanest *construction* of conditional expectation ($L^2$ first, then extend), and it gives the *interpretation* — $\mathbb{E}[X\mid\mathcal{G}]$ is the optimal *prediction* of $X$ using only $\mathcal{G}$-information, the **regression function** of statistics and the basis of least-squares estimation, the Kalman filter, and projection-based prediction.

---

# Sources and Targets

**Sources.** Hypothesis: $X\in L^2$. The $L^2$ restriction is essential for the *geometry* (an inner product is needed) — for general $X\in L^1$ one extends by monotone limits, but the projection picture is the $L^2$ statement.

**Targets.** "$\mathbb{E}[X\mid\mathcal{G}]=$ projection" gives: the **best-predictor / minimum-mean-square-error** characterisation $\mathbb{E}[(X-\mathbb{E}[X\mid\mathcal{G}])^2]\le\mathbb{E}[(X-W)^2]$ for all $\mathcal{G}$-measurable $W$; the **Pythagorean variance decomposition** $\mathrm{Var}(X)=\mathrm{Var}(\mathbb{E}[X\mid\mathcal{G}])+\mathbb{E}[\mathrm{Var}(X\mid\mathcal{G})]$ ("explained $+$ unexplained variance"); and the contraction $\|\mathbb{E}[X\mid\mathcal{G}]\|_2\le\|X\|_2$.

---

# Statement

Let $X\in L^2(\Omega,\mathcal{F},\mathbb{P})$. Then $L^2(\mathcal{G})$ is a **closed subspace** of the Hilbert space $L^2(\mathcal{F})$, and the [[Def - Conditional Expectation|conditional expectation]] $\mathbb{E}[X\mid\mathcal{G}]$ is the **orthogonal projection** of $X$ onto $L^2(\mathcal{G})$:
$$\mathbb{E}[X\mid\mathcal{G}]=\operatorname*{arg\,min}_{W\in L^2(\mathcal{G})}\ \mathbb{E}\big[(X-W)^2\big].$$
Equivalently, $\mathbb{E}[X\mid\mathcal{G}]$ is the unique $W\in L^2(\mathcal{G})$ with $X-W\perp L^2(\mathcal{G})$, i.e. $\mathbb{E}[(X-W)Z]=0$ for all $Z\in L^2(\mathcal{G})$.

**Variance decomposition.** $\mathrm{Var}(X)=\mathrm{Var}\big(\mathbb{E}[X\mid\mathcal{G}]\big)+\mathbb{E}\big[\mathrm{Var}(X\mid\mathcal{G})\big]$, where $\mathrm{Var}(X\mid\mathcal{G})=\mathbb{E}[X^2\mid\mathcal{G}]-\mathbb{E}[X\mid\mathcal{G}]^2$.

---

# Why Is It True

**$L^2(\mathcal{G})$ is a closed subspace.** It is a linear subspace of $L^2(\mathcal{F})$; closed because [[Thm - Completeness of Lp Spaces|L² is complete]] and an $L^2$-limit of $\mathcal{G}$-measurable functions is $\mathcal{G}$-measurable (an $L^2$-limit has an a.s.-convergent subsequence, and a.s. limits of $\mathcal{G}$-measurable functions are $\mathcal{G}$-measurable).

**The projection exists and is characterised by orthogonality.** In a [[Ex - The Cauchy-Schwarz inequality and L2 geometry|Hilbert space]], every closed subspace $V$ admits a unique orthogonal projection: for each $X$ there is a unique $W\in V$ minimising $\|X-W\|$, characterised by $X-W\perp V$. (Proof: a minimising sequence is Cauchy by the parallelogram law, converges by completeness, the limit lies in $V$ since $V$ is closed; orthogonality is the first-order optimality condition.)

**The projection *is* conditional expectation.** Let $W=P_{L^2(\mathcal{G})}X$. Then $W$ is $\mathcal{G}$-measurable, and orthogonality $X-W\perp L^2(\mathcal{G})$ gives $\mathbb{E}[(X-W)Z]=0$ for every $Z\in L^2(\mathcal{G})$; taking $Z=\mathbf{1}_A$ ($A\in\mathcal{G}$) yields $\mathbb{E}[W\mathbf{1}_A]=\mathbb{E}[X\mathbf{1}_A]$ — exactly the [[Def - Conditional Expectation|two characterising properties]] of $\mathbb{E}[X\mid\mathcal{G}]$. By [[Thm - Existence and Uniqueness of Conditional Expectation|uniqueness]], $W=\mathbb{E}[X\mid\mathcal{G}]$.

The slogan: **the orthogonality condition "the error $X-\mathbb{E}[X\mid\mathcal{G}]$ is orthogonal to everything $\mathcal{G}$-measurable" is *verbatim* the averaging identity of conditional expectation** — geometry and the measure-theoretic definition are the same statement. The best-predictor property is then the definition of orthogonal projection (nearest point), and the **variance decomposition is the Pythagorean theorem**: $X=\mathbb{E}[X\mid\mathcal{G}]+(X-\mathbb{E}[X\mid\mathcal{G}])$ is an orthogonal decomposition (after centring), so the squared norms add — total variance $=$ variance of the projection ("explained") $+$ mean squared residual ("unexplained").

---

# What Makes This Hard

The leap is *seeing* that the abstract averaging identity is a geometric orthogonality relation — that "$\mathbb{E}[(X-W)\mathbf{1}_A]=0$ for all $A\in\mathcal{G}$" *means* "$X-W$ is orthogonal to $L^2(\mathcal{G})$." Once that is internalised the theorem is the Hilbert-space projection theorem. The two genuine technical points: $L^2(\mathcal{G})$ must be shown *closed* (needs completeness, plus that a.s.-limits preserve $\mathcal{G}$-measurability), and the picture is intrinsically $L^2$ — the geometry has no analogue in $L^1$, where one falls back on the order/monotone-limit constructions.

---

# Rederivation Scaffold

**High-level strategy.** Show $L^2(\mathcal{G})$ is a closed subspace of the Hilbert space $L^2(\mathcal{F})$; project $X$ onto it; verify the projection satisfies the two characterising properties of $\mathbb{E}[X\mid\mathcal{G}]$; read off best-predictor and the Pythagorean variance decomposition.

**Subgoal decomposition.**

1. **Closed subspace.** $L^2(\mathcal{G})$ linear; closed by completeness $+$ "$L^2$-limit of $\mathcal{G}$-measurable is $\mathcal{G}$-measurable."
2. **Projection.** Hilbert-space projection theorem: unique nearest $W\in L^2(\mathcal{G})$, with $X-W\perp L^2(\mathcal{G})$.
3. **Identify.** Orthogonality with $Z=\mathbf{1}_A$ gives the averaging identity; $W$ is $\mathcal{G}$-measurable; uniqueness $\Rightarrow W=\mathbb{E}[X\mid\mathcal{G}]$.
4. **Decompose.** Pythagoras on $X=\mathbb{E}[X\mid\mathcal{G}]+\text{residual}$ (centred) gives the variance identity.

---

# Lemma Decomposition

> [!note]- Lemma 1: $L^2(\mathcal{G})$ is a closed subspace
> **Statement:** $L^2(\Omega,\mathcal{G},\mathbb{P})$ is a closed linear subspace of $L^2(\Omega,\mathcal{F},\mathbb{P})$.
>
> **Hint:** $L^2$-convergence has an a.s.-convergent subsequence (the standard $L^p$-to-a.s. extraction), and an a.s. limit of $\mathcal{G}$-measurable functions is $\mathcal{G}$-measurable.
>
> **Why needed:** Closedness is the precondition for the Hilbert-space projection theorem to apply — without it, the orthogonal projection $P_{L^2(\mathcal{G})}$ does not exist, and the construction of conditional expectation as a projection is illegal.
>
> > [!note]- Full proof
> > It is a linear subspace. If $W_n\in L^2(\mathcal{G})$ and $W_n\to W$ in $L^2(\mathcal{F})$, then ([[Ex - Lp convergence and almost-everywhere subsequences|L²-convergence gives an a.s.-convergent subsequence]]) $W_{n_k}\to W$ a.s.; each $W_{n_k}$ is $\mathcal{G}$-measurable, and an a.s.-limit of $\mathcal{G}$-measurable functions is $\mathcal{G}$-measurable (in the completed $\mathcal{G}$). So $W\in L^2(\mathcal{G})$ — the subspace is closed. $\square$

> [!note]- Lemma 2: The projection is the conditional expectation
> **Statement:** The orthogonal projection $W=P_{L^2(\mathcal{G})}X$ equals $\mathbb{E}[X\mid\mathcal{G}]$.
>
> **Hint:** The defining condition $X-W\perp L^2(\mathcal{G})$ tested against indicators $\mathbf{1}_A$ for $A\in\mathcal{G}$ gives $\mathbb{E}[W\mathbf{1}_A]=\mathbb{E}[X\mathbf{1}_A]$, which is exactly the averaging characterisation of conditional expectation.
>
> **Why needed:** This is the actual identification — the Hilbert-space projection is not just *some* good $\mathcal{G}$-measurable approximation to $X$, it is literally $\mathbb{E}[X\mid\mathcal{G}]$. From this identification flow the variance decomposition, the contraction property, and the geometric intuition for all conditional-expectation manipulations.
>
> > [!note]- Full proof
> > By the Hilbert-space [[Ex - The Cauchy-Schwarz inequality and L2 geometry|projection theorem]] (Lemma 1 gives the closed subspace), $W\in L^2(\mathcal{G})$ exists with $X-W\perp L^2(\mathcal{G})$. For $A\in\mathcal{G}$, $\mathbf{1}_A\in L^2(\mathcal{G})$, so $\mathbb{E}[(X-W)\mathbf{1}_A]=0$, i.e. $\mathbb{E}[W\mathbf{1}_A]=\mathbb{E}[X\mathbf{1}_A]$. With $W$ $\mathcal{G}$-measurable and integrable, $W$ satisfies the [[Def - Conditional Expectation|characterisation]] of $\mathbb{E}[X\mid\mathcal{G}]$; [[Thm - Existence and Uniqueness of Conditional Expectation|uniqueness]] gives $W=\mathbb{E}[X\mid\mathcal{G}]$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1: $L^2(\mathcal{G})$ is a closed subspace. Lemma 2: its orthogonal projection of $X$ is $\mathbb{E}[X\mid\mathcal{G}]$, which is therefore the unique $L^2(\mathcal{G})$-minimiser of $\mathbb{E}[(X-W)^2]$. Variance decomposition: centre $X$; $X-\mathbb{E}X=(\mathbb{E}[X\mid\mathcal{G}]-\mathbb{E}X)+(X-\mathbb{E}[X\mid\mathcal{G}])$ is an orthogonal sum (the residual is $\perp L^2(\mathcal{G})$, the first term is in $L^2(\mathcal{G})$), so by Pythagoras $\mathrm{Var}(X)=\mathrm{Var}(\mathbb{E}[X\mid\mathcal{G}])+\mathbb{E}[(X-\mathbb{E}[X\mid\mathcal{G}])^2]$, and the residual term equals $\mathbb{E}[\mathrm{Var}(X\mid\mathcal{G})]$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The projection picture *is* **linear regression** when $\mathcal{G}=\sigma(\text{predictors})$ — $\mathbb{E}[Y\mid X]$ is the minimum-mean-square-error predictor of $Y$, and restricting to *linear* functions of $X$ gives ordinary least squares. The variance decomposition is the **ANOVA / law of total variance** ("explained $+$ unexplained"). Iterated, the projection viewpoint underlies the **Kalman filter** (recursive projection onto the growing information of a [[Def - Filtration|filtration]]).

---

# Bridges

- **[[Ex - The Cauchy-Schwarz inequality and L2 geometry]]** — supplies the Hilbert-space projection theorem this rests on.
- **[[Thm - Existence and Uniqueness of Conditional Expectation]]** — the projection construction is one of the two existence proofs; uniqueness identifies the projection with $\mathbb{E}[X\mid\mathcal{G}]$.
- **[[Thm - Properties of Conditional Expectation]]** — the $L^2$-contraction and the tower property are, geometrically, "projections shrink norms" and "projecting onto a subspace of a subspace."
