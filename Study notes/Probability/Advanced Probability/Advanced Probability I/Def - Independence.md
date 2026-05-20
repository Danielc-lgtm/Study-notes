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

**$\pi$-system criterion.** Independence of $\sigma$-algebras need only be checked for $A_i$ ranging over generating [[Thm - Dynkin's π-λ Theorem|π-systems]] (e.g. the rays for random variables).

---

# Categorical Definition

Independence is a **categorical property of sub-objects in the probabilistic setting**: a family of sub-σ-algebras $(\mathcal{A}_i)_{i \in I}$ of $(\Omega, \mathcal{F}, \mathbb{P})$ is independent if and only if **the joint law on the product is the product of the marginals**. This is the categorical statement that the natural map into a product splits the probability into independent coordinates.

The vocabulary. Recall from [[Def - Probability Space#Categorical Definition|the categorical view of probability spaces]] that the category $\mathbf{Meas}$ has measurable spaces as objects and [[Def - Measurable Function|measurable maps]] as arrows, that it has products (the product σ-algebra), and that probability measures pushforward along arrows. A *sub-σ-algebra* $\mathcal{G} \subseteq \mathcal{F}$ corresponds categorically to a sub-quotient: the identity map $\mathrm{id} : (\Omega, \mathcal{F}) \to (\Omega, \mathcal{G})$ is a measurable surjection, and $\mathcal{G}$-measurable functions $\Omega \to \mathbb{R}$ are exactly those factoring through this map. The category $\mathbf{Prob}$ inherits products from $\mathbf{Meas}$ together with the product measure construction: if $(\Omega_1, \mathcal{F}_1, \mathbb{P}_1)$ and $(\Omega_2, \mathcal{F}_2, \mathbb{P}_2)$ are probability spaces, the product space has $(\mathbb{P}_1 \otimes \mathbb{P}_2)(A_1 \times A_2) = \mathbb{P}_1(A_1)\mathbb{P}_2(A_2)$ as the unique measure satisfying the rectangle rule.

Now the categorical reformulation of independence. Given sub-σ-algebras $\mathcal{A}_1, \dots, \mathcal{A}_n \subseteq \mathcal{F}$, there is a canonical map
$$\Phi : (\Omega, \mathcal{F}) \to (\Omega, \mathcal{A}_1) \times \cdots \times (\Omega, \mathcal{A}_n), \qquad \omega \mapsto (\omega, \dots, \omega),$$
the diagonal-like map sending $\omega$ to itself in each factor (each copy of $\Omega$ now equipped only with $\mathcal{A}_i$). This is measurable because each projection $\omega \mapsto \omega \in (\Omega, \mathcal{A}_i)$ is measurable. Pushing $\mathbb{P}$ forward through $\Phi$ produces a joint law $\Phi_* \mathbb{P}$ on the product, and the **marginals** of this joint law are exactly the restrictions $\mathbb{P}|_{\mathcal{A}_i}$ — the law $\mathbb{P}$ viewed on each sub-σ-algebra alone. The family $(\mathcal{A}_i)$ is **independent** if and only if
$$\Phi_* \mathbb{P} = \mathbb{P}|_{\mathcal{A}_1} \otimes \cdots \otimes \mathbb{P}|_{\mathcal{A}_n}$$
— the joint pushforward equals the product of the marginal pushforwards. This is exactly the statement that the diagonal map factors the probability into the categorical product of its restrictions.

For random variables $(X_i)$ valued in measurable spaces $(E_i, \mathcal{E}_i)$, the same formulation reads: $(X_i)$ are independent iff the joint random variable $(X_1, \dots, X_n) : \Omega \to E_1 \times \cdots \times E_n$ has pushforward $\mu_{(X_1, \dots, X_n)} = \mu_{X_1} \otimes \cdots \otimes \mu_{X_n}$. The deep categorical compression is therefore: *independent means the joint law factors through the categorical product*. The non-categorical product-rule definition $\mathbb{P}(A_1 \cap \dots \cap A_n) = \prod \mathbb{P}(A_i)$ is the rectangle-test for this factorisation, and Dynkin's π-λ theorem is the categorical statement that the factorisation is determined by its values on a generating π-system.

From this viewpoint, the [[Def - Probability Space#Categorical Definition|Giry monad]] $\mathcal{G}$ on $\mathbf{Meas}$ makes the independence statement still sharper: in the Kleisli category of $\mathcal{G}$ (whose arrows are Markov kernels), independence corresponds to a *parallel composition* of channels — independent random variables are channels that share no input wire. This is the bridge to information theory, where mutual information $I(X; Y) = 0$ is the quantitative measure of how far the joint distribution lies from the product.

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
