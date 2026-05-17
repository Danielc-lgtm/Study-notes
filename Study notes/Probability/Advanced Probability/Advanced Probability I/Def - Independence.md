---
type: definition
subject: advanced-probability
prereqs:
  - "Def - Probability Space"
  - "Def - Random Variable"
  - "Def - Product σ-Algebra"
tags: [probability, advanced-probability]
---

# Notation

$(\Omega,\mathcal{F},\mathbb{P})$ a [[Def - Probability Space|probability space]]; $A_i$ events, $\mathcal{A}_i$ sub-$\sigma$-algebras, $X_i$ [[Def - Random Variable|random variables]].

---

# Axiom Motivation

Independence is *the* concept that distinguishes probability theory from measure theory — without it, probability would be a sub-branch of integration. Intuitively, two events are independent if knowing one occurred tells you nothing about the other. The quantitative form is the **product rule**: $\mathbb{P}(A\cap B)=\mathbb{P}(A)\mathbb{P}(B)$.

Why a *product*? Because "knowing $A$" rescales probability to the conditional measure $\mathbb{P}(\cdot\mid A)=\mathbb{P}(\cdot\cap A)/\mathbb{P}(A)$, and "tells you nothing about $B$" means $\mathbb{P}(B\mid A)=\mathbb{P}(B)$ — which rearranges to the product rule. The product rule is the symmetric, division-free form.

Three subtleties the definition must get right. (i) **Mutual, not pairwise.** Independence of a family demands the product rule for *every finite sub-collection* — pairwise independence is strictly weaker ([[Ex - Pairwise versus mutual independence|Bernstein's example]]). (ii) **The right level of generality is $\sigma$-algebras.** Independence of random variables means independence of the $\sigma$-algebras $\sigma(X_i)$ they generate — the information they carry; this automatically makes $f(X_1)$ and $g(X_2)$ independent. (iii) **Checkable on $\pi$-systems.** By [[Thm - Dynkin's π-λ Theorem|Dynkin's theorem]], independence of $\sigma$-algebras need only be verified on generating $\pi$-systems — for real variables, on the events $\{X_i\le t_i\}$. This makes independence equivalent to "the joint [[Def - Random Variable|law]] is the [[Thm - Product Measure|product]] of the marginal laws."

That last equivalence is the deep one: **independence is the product structure**. Independent variables are coordinates of a product measure, and [[Thm - Fubini-Tonelli Theorem|Fubini]] is what computes with them.

---

# The Definition

Let $(\Omega,\mathcal{F},\mathbb{P})$ be a probability space.

**Events.** A family $(A_i)_{i\in I}$ is **(mutually) independent** if for every finite $J\subseteq I$,
$$\mathbb{P}\Big(\bigcap_{i\in J}A_i\Big)=\prod_{i\in J}\mathbb{P}(A_i).$$

**$\sigma$-algebras.** Sub-$\sigma$-algebras $(\mathcal{A}_i)_{i\in I}$ of $\mathcal{F}$ are **independent** if, for every finite $J$ and every choice $A_i\in\mathcal{A}_i$, the events $(A_i)_{i\in J}$ satisfy the product rule.

**Random variables.** $(X_i)_{i\in I}$ are **independent** if the $\sigma$-algebras $(\sigma(X_i))_{i\in I}$ are independent — equivalently, for all $t_i$ and finite $J$, $\mathbb{P}(X_i\le t_i,\,i\in J)=\prod_{i\in J}\mathbb{P}(X_i\le t_i)$ — equivalently, the joint law $\mu_{(X_i)_{i\in J}}$ is the [[Thm - Product Measure|product]] $\bigotimes_{i\in J}\mu_{X_i}$.

**$\pi$-system criterion.** Independence of $\sigma$-algebras need only be checked for $A_i$ ranging over generating [[Thm - Dynkin's π-λ Theorem|$\pi$-systems]] (e.g. the rays for random variables).

---

# Relate to Other Fields / Compression

Independence is precisely the [[Thm - Product Measure|product-measure]] structure: independent variables are the coordinate projections of a product probability space, and their joint law factors. This is why [[Thm - Fubini-Tonelli Theorem|Fubini–Tonelli]] is the computational engine for independent variables ($\mathbb{E}[XY]=\mathbb{E}X\,\mathbb{E}Y$, the law of a sum is a convolution). In information theory, independence is *zero mutual information*. The infinite-product / [[Thm - Product Measure|Kolmogorov extension]] construction places an entire independent sequence on one space.

---

# Examples / Corollaries

Successive fair coin tosses are independent; the digits of a uniform $[0,1]$ variable are independent and uniform on $\{0,\dots,9\}$. For independent $X,Y$: $\mathbb{E}[XY]=\mathbb{E}X\,\mathbb{E}Y$ (so $\mathrm{Cov}=0$), $\mathrm{Var}(X+Y)=\mathrm{Var}X+\mathrm{Var}Y$, and $f(X),g(Y)$ are independent for any Borel $f,g$.

**Independence is strictly stronger than uncorrelatedness:** $\mathrm{Cov}(X,Y)=0$ does not imply independence (take $X$ symmetric, $Y=X^2$). **Pairwise is strictly weaker than mutual** ([[Ex - Pairwise versus mutual independence|Bernstein]]).

Calibration: (i) Are disjoint events independent? Almost never — $\mathbb{P}(A\cap B)=0\neq\mathbb{P}(A)\mathbb{P}(B)$ unless one is null. (ii) Is $X$ independent of itself? Only if $X$ is a.s. constant. (iii) Does $\mathrm{Cov}(X,Y)=0$ give independence? No.

---

# Unlocked by This

> [!tip] Borel–Cantelli, the 0–1 law, and the limit theorems
> Independence powers the [[Thm - Borel-Cantelli Lemmas|second Borel–Cantelli lemma]], the [[Thm - Kolmogorov 0-1 Law|Kolmogorov 0–1 law]] (tail events are trivial), and — for i.i.d. sequences — the [[Thm - Strong Law of Large Numbers|law of large numbers]] and the [[Thm - Central Limit Theorem|central limit theorem]].
