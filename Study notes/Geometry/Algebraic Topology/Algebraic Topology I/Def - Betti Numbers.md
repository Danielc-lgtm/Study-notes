---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Singular Homology"
tags: [geometry, algebraic-topology, invariants]
---

# Notation

$M$ is a topological space (typically a compact manifold). $H_p(M; \mathbb{R})$ is the [[Def - Singular Homology|singular homology]] with real coefficients. $\dim_\mathbb{R}$ denotes the dimension of a real vector space.

$b_p(M) \in \{0, 1, 2, \dots\} \cup \{\infty\}$ — the $p$-th Betti number. We write $b_p$ when $M$ is clear from context.

$P_M(t) = \sum_p b_p(M) t^p$ — the **Poincaré polynomial** of $M$, a generating function packaging all the Betti numbers.

---

# Axiom Motivation

The Betti numbers are the single most-used numerical invariants of a topological space — they count the "$p$-dimensional holes" for each $p$. We want to extract from the rich algebraic structure of homology a small list of numbers that captures the essential topological information.

Why use $\mathbb{R}$ coefficients to define them? Three reasons.

**Real coefficients kill torsion.** Over a field of characteristic zero, the universal coefficient theorem simplifies: $H_p(M; \mathbb{R}) = H_p(M; \mathbb{Z}) \otimes_\mathbb{Z} \mathbb{R}$, which is a real vector space whose dimension equals the *free rank* of $H_p(M; \mathbb{Z})$. The torsion part of $H_p(M; \mathbb{Z})$ — finite cyclic factors $\mathbb{Z}/n\mathbb{Z}$ — dies after tensoring with $\mathbb{R}$ (because $\mathbb{Z}/n\mathbb{Z} \otimes_\mathbb{Z} \mathbb{R} = 0$). So the Betti number $b_p = \dim_\mathbb{R} H_p(M; \mathbb{R})$ counts only the free part, the "essential" rank that survives in any coefficient field.

**Real vector spaces have dimensions.** Working over $\mathbb{R}$ ensures the homology groups are vector spaces, so we can speak of dimensions in a clean linear-algebraic sense. The dimension is a well-defined non-negative integer (or $\infty$), making the Betti number a numerical invariant in the most rigorous sense. Working over $\mathbb{Z}$ instead would give us "ranks of finitely generated abelian groups," which is the same number but conceptually less direct.

**Real coefficients are the natural arena for the de Rham theorem.** The de Rham cohomology $H^p_{dR}(M)$ is a real vector space (since differential forms have real coefficients), and the de Rham theorem identifies $H^p(M; \mathbb{R}) \cong H^p_{dR}(M)$. The dimension of either side is the Betti number. So Betti numbers are simultaneously the dimensions of de Rham cohomology and the ranks of integer homology — two completely different definitions that coincide by deep theorems.

Why is the Betti number a good invariant? Three properties.

**Homotopy invariance.** Since homology is a homotopy invariant ([[Thm - Homotopy Invariance of Singular Homology]]), Betti numbers are homotopy invariants: $b_p(M) = b_p(N)$ whenever $M \simeq N$. They capture only the homotopy type of $M$, not the smooth or even topological structure beyond that.

**Numerical computability.** Betti numbers are non-negative integers (or $\infty$), so they are easy to compute, compare, and tabulate. The Betti numbers of all the standard spaces — spheres, tori, projective spaces, Grassmannians — are explicitly known and form the basic data of algebraic topology.

**Refinement via Poincaré polynomial.** Packaging all Betti numbers into the generating function $P_M(t) = \sum b_p t^p$ gives a polynomial (when $M$ is a compact manifold, all Betti numbers are finite and only finitely many are non-zero) whose specific values at $t = 1, -1, \pm 1, \dots$ recover important invariants: $P_M(1) = \sum b_p$ is the total Betti sum, $P_M(-1) = \sum (-1)^p b_p = \chi(M)$ is the [[Def - Euler Characteristic|Euler characteristic]]. So the Poincaré polynomial is a master invariant from which many derived invariants are obtained.

What information do Betti numbers *lose*? They lose torsion (real coefficients kill it). They lose ring structure (no cup product). They lose ordering (the Poincaré polynomial loses the geometric meaning of which generator lives where). But they retain the most fundamental property: the count of independent "$p$-dimensional cycles up to bounding" for each $p$.

---

# The Definition

Let $M$ be a topological space and $p \geq 0$ an integer. The **$p$-th Betti number** of $M$ is
$$
b_p(M) \;=\; \dim_\mathbb{R} H_p(M; \mathbb{R}),
$$
the dimension of the $p$-th real singular homology as a real vector space. By the universal coefficient theorem,
$$
b_p(M) \;=\; \mathrm{rank}_\mathbb{Z} H_p(M; \mathbb{Z}),
$$
the free rank of the integer singular homology. By the [[Thm - The de Rham Theorem (Full Proof)|de Rham theorem]] (when $M$ is a smooth manifold),
$$
b_p(M) \;=\; \dim_\mathbb{R} H^p_{dR}(M),
$$
the dimension of the $p$-th de Rham cohomology. All three definitions give the same answer.

The **Poincaré polynomial** of $M$ is the formal generating function
$$
P_M(t) \;=\; \sum_{p \geq 0} b_p(M)\, t^p \;\in\; \mathbb{Z}[[t]].
$$
When $M$ is a finite CW complex (or compact manifold), only finitely many $b_p$ are non-zero, so $P_M(t)$ is a polynomial.

The **total Betti number** is $b(M) = \sum_p b_p(M) = P_M(1)$, the sum of all Betti numbers. The **Euler characteristic** is $\chi(M) = \sum_p (-1)^p b_p(M) = P_M(-1)$.

---

# Relate to Other Fields / Compression

The Betti numbers are the **dimensions of homology over a field** — the simplest numerical invariants extractable from singular homology. They are the topological analogue of the "rank" of a finitely generated module: a single non-negative integer that captures the size of the free part.

In differential geometry, by the de Rham theorem the Betti numbers are the **maximal numbers of independent closed $p$-forms modulo exact**: $b_p(M) = \dim H^p_{dR}(M)$. So Betti numbers are computable two ways — topologically (from cycles) and smoothly (from forms) — and the two answers must match.

In algebraic geometry (specifically complex projective varieties), the Betti numbers refine into the **Hodge numbers** $h^{p,q}$ with $b_k = \sum_{p+q=k} h^{p,q}$. The Hodge numbers carry strictly more information than the Betti numbers (they distinguish complex structure within a fixed topological type), and the Hodge decomposition is the way to access them.

In statistical mechanics and dynamical systems, the Betti numbers appear in the **Morse inequalities**: the number of critical points of index $p$ of a Morse function on $M$ is at least $b_p(M)$. So Betti numbers give lower bounds on the complexity of any Morse function — equivalently, on the number of critical points of any smooth function with non-degenerate critical points.

In topological data analysis (TDA), Betti numbers are the **persistent homology** of a filtration of a finite metric space, used as features for classifying shapes in machine learning. The persistence diagram tracks how Betti numbers change as a scale parameter varies, and the resulting "Betti curves" are robust features for shape classification.

**True name:** the $p$-th Betti number is the **number of independent $p$-dimensional holes in $M$**, where "hole" means "$p$-cycle that is not a boundary" and "independent" means "linearly independent over $\mathbb{R}$ in the homology vector space." For $b_0$ this is the number of path components; for $b_1$ the number of independent loops; for $b_2$ the number of independent voids (sphere-like cavities); and so on.

---

# Examples / Corollaries

**$b_*(S^n)$.** The $n$-sphere has Betti numbers $b_0 = 1$, $b_n = 1$, all others zero. Poincaré polynomial $P_{S^n}(t) = 1 + t^n$. Total Betti number $b(S^n) = 2$. Euler characteristic $\chi(S^n) = 1 + (-1)^n$.

**$b_*(T^n)$.** The $n$-torus has $b_k(T^n) = \binom{n}{k}$ for $0 \leq k \leq n$. Poincaré polynomial $P_{T^n}(t) = (1 + t)^n$ (binomial expansion). Total Betti number $b(T^n) = 2^n$. Euler characteristic $\chi(T^n) = (1 - 1)^n = 0$ for $n \geq 1$.

**$b_*(\mathbb{CP}^n)$.** Complex projective space has $b_{2k}(\mathbb{CP}^n) = 1$ for $0 \leq k \leq n$, all odd Betti numbers zero. Poincaré polynomial $P_{\mathbb{CP}^n}(t) = 1 + t^2 + t^4 + \cdots + t^{2n} = (1 - t^{2(n+1)})/(1 - t^2)$. Total Betti number $b(\mathbb{CP}^n) = n + 1$. Euler characteristic $\chi(\mathbb{CP}^n) = n + 1$ (the alternating sum of $n + 1$ ones with all signs positive, since the non-zero Betti numbers are in even degrees).

**$b_*(\mathbb{RP}^n)$.** With $\mathbb{R}$ coefficients, $\mathbb{RP}^n$ has $b_0 = 1$ always, $b_n = 1$ if $n$ is odd (when $\mathbb{RP}^n$ is orientable), zero otherwise. So $b_*(\mathbb{RP}^n) = (1, 0, \dots, 0)$ for even $n$ (Betti numbers same as a point) and $(1, 0, \dots, 0, 1)$ for odd $n$ (Betti numbers same as $S^n$). The torsion in integer homology is invisible to Betti numbers.

**$b_*(\Sigma_g)$.** A closed orientable surface of genus $g$ has $b_0 = 1$, $b_1 = 2g$, $b_2 = 1$. Poincaré polynomial $P_{\Sigma_g}(t) = 1 + 2gt + t^2$. Euler characteristic $\chi(\Sigma_g) = 1 - 2g + 1 = 2 - 2g$.

**Is NOT an instance: an arbitrary integer.** Not every non-negative integer is a Betti number of *some* manifold of a fixed dimension. For instance, no closed $2$-manifold has $b_1 = 5$ (orientable surfaces have $b_1 = 2g$, so $b_1$ is always even). The achievable Betti numbers are constrained by Poincaré duality, the existence of a fundamental class, and other topological restrictions.

**Corollary ($b_0$ = number of path components).** For any space $M$, $b_0(M)$ equals the number of path components. A path component contributes a generator to $H_0$ (any point in the component), and different components contribute independent generators.

**Corollary (Betti numbers vanish above the dimension).** For an $n$-dimensional CW complex (or topological $n$-manifold), $b_p(M) = 0$ for $p > n$. Reason: no cells of dimension higher than $n$, so the chain complex (cellular or simplicial) is zero in those degrees.

**Corollary (Poincaré duality of Betti numbers).** For a closed oriented $n$-manifold $M$,
$$
b_p(M) = b_{n-p}(M)
$$
for all $p$. This is the **palindrome property** of the Poincaré polynomial: $P_M(t) = t^n P_M(1/t)$. Visible in the Betti polynomials of $S^n$ ($1, 0, \dots, 0, 1$), $T^n$ ($\binom{n}{k}$ symmetric around $n/2$), $\mathbb{CP}^n$ ($1, 0, 1, 0, \dots, 1$ in even degrees only).

**Corollary (Betti numbers determine Euler characteristic).** $\chi(M) = \sum_p (-1)^p b_p(M) = P_M(-1)$. So computing the Euler characteristic is one substitution of $t \to -1$ in the Poincaré polynomial.

**Corollary (Künneth formula for Betti numbers).** For a product of spaces $X \times Y$ with finite Betti numbers, $b_n(X \times Y) = \sum_{p+q=n} b_p(X)\, b_q(Y)$. Equivalently, $P_{X \times Y}(t) = P_X(t) \cdot P_Y(t)$. This makes computation of $b_*(T^n)$ from $b_*(S^1) = (1, 1)$ a one-line application: $P_{T^n}(t) = (1 + t)^n$.

**Calibration check.** If you understand the definition you should be able to: (1) verify by computation that $\chi(\Sigma_g) = 2 - 2g$ for the genus-$g$ surface using the Betti numbers; (2) write down the Poincaré polynomial of $\mathbb{CP}^2 \times \mathbb{CP}^2$ and compute its Euler characteristic; (3) explain why the Betti numbers of $\mathbb{RP}^2$ and a single point coincide (despite $\mathbb{RP}^2$ being a non-trivial surface), and identify what information this loss reveals about the importance of integer coefficients.

---

# Unlocked by This

> [!tip] Euler Characteristic *(from Algebraic Topology — this same topic)*
> The alternating sum $\chi(M) = \sum_p (-1)^p b_p(M)$ is the **Euler characteristic**, the most-used single-number invariant of $M$. See [[Def - Euler Characteristic]] and [[Thm - Euler Characteristic via Alternating Betti Numbers]]. The Euler characteristic appears in Gauss–Bonnet ($\chi = (1/2\pi) \int K\, dA$ for surfaces), Poincaré–Hopf ($\chi$ = sum of indices of zeros of a vector field), and the Lefschetz fixed-point formula.

> [!tip] Hodge Numbers *(from Complex Algebraic Geometry)*
> For a compact Kähler manifold, the Betti numbers refine into the **Hodge numbers** $h^{p,q}$ with $b_k = \sum_{p+q=k} h^{p,q}$. The Hodge numbers satisfy Hodge symmetry $h^{p,q} = h^{q,p}$ and Serre duality $h^{p,q} = h^{n-p,n-q}$, and they distinguish complex structures within a fixed topological type. The collection $\{h^{p,q}\}$ is the **Hodge diamond** of the variety.

> [!tip] Morse Inequalities *(from Differential Topology)*
> A Morse function $f : M \to \mathbb{R}$ on a closed manifold has at least $b_p(M)$ critical points of index $p$ — the **Morse inequalities**. The strong form: $\sum_p (-1)^p m_p \geq \sum_p (-1)^p b_p = \chi(M)$, where $m_p$ is the number of index-$p$ critical points, with equality when the function is "perfect" (e.g. for a generic Morse function on a Kähler manifold). Morse theory uses the Betti numbers as a topological lower bound on the complexity of any smooth function.

> [!tip] **Persistent Homology** *(from Topological Data Analysis)*
> For a finite metric space (a point cloud), one can build a filtration of simplicial complexes parameterised by a scale $\varepsilon$ — the **Vietoris–Rips complex** — and track how the Betti numbers $b_p(\varepsilon)$ change with $\varepsilon$. The persistence diagram records the birth-and-death pairs of each homology class as $\varepsilon$ varies. **Persistent homology** has become a standard tool in shape classification, neural network interpretability, and biology.
