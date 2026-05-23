---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Lie Group"
  - "Def - Lie Subgroup"
  - "Def - Embedded Submanifold"
  - "Def - Exponential Map of a Lie Group"
tags: [geometry, differential-geometry, lie-groups]
---

# Notation

$G$ is a Lie group with Lie algebra $\mathfrak{g}$ and exponential map $\exp : \mathfrak{g} \to G$. $H \leq G$ is a subgroup, assumed closed as a subset of $G$ in the manifold topology. The Lie algebra of $H$, once $H$ is shown to be a Lie subgroup, is $\mathfrak{h} \subseteq \mathfrak{g}$. See [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]] for the full notation registry.

---

# Statement

> **Theorem (Closed Subgroup Theorem; Cartan).** Let $G$ be a Lie group and $H \leq G$ a subgroup that is also a topologically closed subset of $G$ (in the manifold topology of $G$). Then $H$ is an **embedded Lie subgroup** of $G$.
>
> Moreover, the Lie algebra of $H$, regarded as a subspace of $\mathfrak{g}$, is
> $$\mathfrak{h} = \{X \in \mathfrak{g} : \exp(tX) \in H \text{ for all } t \in \mathbb{R}\}.$$

> **Corollary (Lee Cor 20.13).** For any subgroup $H \leq G$, the following are equivalent: (a) $H$ is closed in $G$; (b) $H$ is an embedded submanifold of $G$; (c) $H$ is an embedded Lie subgroup of $G$.

---

# Motivation

The closed subgroup theorem is the most useful structural fact in Lie group theory, and it is the one that converts manifold questions into topological questions. Given a subset $H$ of a Lie group $G$ that one suspects of being a Lie subgroup, one wants to verify some condition that establishes the manifold structure of $H$. The naive guesses — that $H$ is "locally Euclidean", that $H$ admits a smooth atlas, that $H$ is parameterized by a smooth map — are all hard to verify directly. The closed subgroup theorem says: **only two conditions are needed, and they are both elementary** — $H$ must be a subgroup (closed under multiplication and inversion), and $H$ must be closed as a subset of $G$. From these, the manifold structure, the immersion property, the embedding property, and the Lie algebra are all automatic.

This is a deeply non-trivial statement. There is no a priori reason a closed subgroup should be a submanifold: closed subsets of manifolds need not be submanifolds (a Cantor set in $\mathbb{R}$ is closed but not a submanifold). The miracle is that the algebraic condition "subgroup" combined with the topological condition "closed" force the geometric condition "embedded smooth submanifold". The rigidity is what makes the theorem powerful.

In practice, the closed subgroup theorem is what underlies the entire theory of matrix Lie groups. The classical Lie groups — $\mathrm{O}(n)$, $\mathrm{SO}(n)$, $\mathrm{SL}(n)$, $\mathrm{U}(n)$, $\mathrm{SU}(n)$, $\mathrm{Sp}(2n)$ — are defined as the solution sets of polynomial equations in $\mathrm{GL}(n)$. These solution sets are *closed* by continuity, and they are *subgroups* by the algebra of the equations. The closed subgroup theorem then says they are automatically embedded Lie subgroups of $\mathrm{GL}(n)$, with manifold structures and Lie algebras derived from the equations. Without this theorem, each classical group would require its own ad hoc construction of charts and atlases; with it, the construction is uniform.

The Lie algebra characterization $\mathfrak{h} = \{X : \exp(tX) \in H \text{ for all } t\}$ is also useful: it gives a concrete way to compute $\mathfrak{h}$ from $H$ via the exponential map. For matrix groups, $\mathfrak{h} = \{X : \exp(tX) \in H \text{ for all } t\}$ is exactly the set of $X$ whose matrix exponential lies in $H$ for all real $t$, and this is checked by differentiating the defining equations of $H$ at the identity.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis of the theorem is a *closed subgroup* of $G$. The non-obvious sources are situations where a closed subgroup appears without being initially recognized as such.

The first source is **a subgroup defined by polynomial equations**. Property $B$ is "$H = \{g : p_1(g) = 0, \ldots, p_k(g) = 0\}$ for polynomial constraints $p_i$". The bridge is that polynomial functions are continuous, so their zero set is closed, and the level set of polynomial equations is a subgroup precisely because the equations are multiplicatively respected (e.g., $\det(AB) = \det(A) \det(B)$ makes $\{\det = 1\}$ a subgroup, $A^T A = I$ makes $\mathrm{O}(n)$ a subgroup). All classical matrix Lie groups come from this source.

A second source is **the kernel of a continuous group homomorphism**. Property $B$ is "$H = \ker(F)$ for $F : G \to K$ a continuous homomorphism into a topological group $K$". The bridge: $\ker F = F^{-1}(\{e_K\})$ is closed by continuity, and the kernel of a homomorphism is automatically a normal subgroup. So $H$ is a closed normal subgroup, and the theorem gives the embedded Lie subgroup structure. This generalizes [[Def - Lie Group Homomorphism|Lee Prop 7.16]] (smooth-homomorphism kernels are Lie subgroups) to merely continuous homomorphisms.

A third source is **a stabilizer of a smooth group action**. Property $B$ is "$H = G_p$ for the smooth action of $G$ on a manifold $M$ at a point $p$". The bridge: $G_p = \theta(\cdot, p)^{-1}(\{p\})$ is closed by continuity. So the stabilizer of any smooth action is automatically a closed Lie subgroup, which is the technical fact needed for the orbit-stabilizer theorem and the homogeneous-space construction.

A fourth source is **the intersection of two closed Lie subgroups**. Property $B$ is "$H = H_1 \cap H_2$ for closed Lie subgroups $H_i \leq G$". The bridge: intersections of closed sets are closed, intersections of subgroups are subgroups. So $H$ is again a closed subgroup, hence an embedded Lie subgroup by the closed subgroup theorem.

**Targets (Output Amplification)**

The conclusion is "$H$ is an embedded Lie subgroup of $G$, with Lie algebra $\mathfrak{h} = \{X : \exp(tX) \in H \text{ for all } t\}$." Combined with further structure, this amplifies.

The first amplification is **the Lie algebra characterization in concrete cases**. For matrix Lie groups $G \leq \mathrm{GL}(n)$, $\mathfrak{h} = \{A \in \mathfrak{gl}(n) : e^{tA} \in H \text{ for all } t\}$, and this set is computed by differentiating the defining equations of $H$ at $I$. For $\mathrm{O}(n)$: $e^{tA} \in \mathrm{O}(n)$ iff $e^{tA^T} e^{tA} = I$, iff $A^T + A = 0$ (taking $d/dt|_{t=0}$). So $\mathfrak{o}(n) = \{A : A^T = -A\}$. This is the standard one-line computation.

A second amplification is **dimension computation**. Once $H$ is an embedded submanifold, $\dim H = \dim \mathfrak{h}$ by the [[Thm - Left-Invariant Vector Fields Form a Lie Algebra|Lie algebra dimension theorem]]. So computing $\dim \mathfrak{h}$ from the Lie algebra characterization gives $\dim H$ — for instance $\dim \mathrm{O}(n) = \dim \mathfrak{o}(n) = \binom{n}{2}$ (number of free parameters in an antisymmetric matrix).

A third amplification is **the homogeneous-space construction**. Once any closed subgroup is automatically a Lie subgroup, the quotient $G/H$ for any closed $H \leq G$ acquires a smooth manifold structure (Lee Thm 21.17), and $G/H$ is the homogeneous space. This is the foundation of homogeneous-space theory.

A fourth amplification is **classification of normal subgroups**. Closed normal Lie subgroups of $G$ correspond (for connected $G$) to ideals in $\mathfrak{g}$ via $H \leftrightarrow \mathfrak{h}$ (Lee Thm 20.28). The closed subgroup theorem provides the manifold structure on each closed normal subgroup, and the structural classification then proceeds via Lie algebra ideals.

---

# Why Is It True

The proof is one of the more sophisticated in Lee's book, and it has several conceptual ingredients. The central observation is that **the structure of $\mathfrak{h}$ can be determined from $H$ before $H$ is even known to be a manifold**: namely, $\mathfrak{h} := \{X \in \mathfrak{g} : \exp(tX) \in H \text{ for all } t \in \mathbb{R}\}$ makes sense without any manifold assumption on $H$, and the proof shows that this $\mathfrak{h}$ is a linear subspace of $\mathfrak{g}$ that turns out to be the Lie algebra of $H$ once the manifold structure is established.

**The bolded mechanism summary: closure of $H$ + the BCH-leading-order formula $\lim_{n \to \infty} (\exp(X/n) \exp(Y/n))^n = \exp(X + Y)$ force $\mathfrak{h}$ to be a linear subspace; then a slice chart using a complement to $\mathfrak{h}$ in $\mathfrak{g}$ gives $H$ as an embedded submanifold near $e$, and left-translation extends the slice everywhere.**

Step by step:

1. **$\mathfrak{h}$ is closed under scalar multiplication.** If $X \in \mathfrak{h}$ and $s \in \mathbb{R}$, then $\exp(t(sX)) = \exp((ts)X) \in H$ for all $t \in \mathbb{R}$ (by definition of $\mathfrak{h}$). Hence $sX \in \mathfrak{h}$.

2. **$\mathfrak{h}$ is closed under addition.** This is where closedness of $H$ is essential. For $X, Y \in \mathfrak{h}$ and $t \in \mathbb{R}$ fixed, write $\exp(tX/n) \exp(tY/n) \in H$ for each $n$ (since each factor is in $H$ and $H$ is a subgroup). By the BCH-leading-order formula (Lee Cor 20.11),
$$\lim_{n \to \infty} (\exp(tX/n) \exp(tY/n))^n = \exp(t(X + Y)).$$
The sequence on the left is in $H$ (each term is a product of $H$-elements), and the limit is in $H$ by closedness. Hence $\exp(t(X + Y)) \in H$ for all $t$, so $X + Y \in \mathfrak{h}$.

3. **Local slice chart.** Choose a complement $\mathfrak{b} \subseteq \mathfrak{g}$ to $\mathfrak{h}$, so $\mathfrak{g} = \mathfrak{h} \oplus \mathfrak{b}$. By Lee Problem 20-3, the map $\Phi : \mathfrak{h} \oplus \mathfrak{b} \to G$, $(X, Y) \mapsto \exp(X) \exp(Y)$, is a local diffeomorphism near $(0, 0)$. The proof now shows: by shrinking the domain $U \subseteq \mathfrak{g}$ of $\exp|_U : U \to \exp(U)$ a diffeomorphism, we have $\exp(\mathfrak{h} \cap U) = H \cap \exp(U)$ — i.e., $H$ near $e$ is exactly the image of the subspace $\mathfrak{h}$ under $\exp$. This is the slice chart at $e$.

   The proof of this step is the heart of the theorem: suppose, for contradiction, no such $U$ exists. Then for every neighborhood $U_i$ of $0$ in $\mathfrak{g}$, there is $h_i \in (\exp(U_i)) \cap H$ with $h_i \notin \exp(U_i \cap \mathfrak{h})$. Writing $h_i = \Phi(X_i, Y_i)$ with $(X_i, Y_i) \in \mathfrak{h} \oplus \mathfrak{b}$ near $0$, the $Y_i$ component is nonzero. Then $Y_i/|Y_i| \in \mathfrak{b}$ accumulates on the unit sphere in $\mathfrak{b}$, so passing to a subsequence converges to some $Y \in \mathfrak{b}$ with $|Y| = 1$. A careful argument (Lee pp 523–524) then shows $\exp(tY) \in H$ for all $t \in \mathbb{R}$, so $Y \in \mathfrak{h}$. But $Y \in \mathfrak{b}$ and $\mathfrak{h} \cap \mathfrak{b} = \{0\}$, contradicting $|Y| = 1$.

4. **Translation by left-multiplication.** For any $h \in H$, the left-translation $L_h$ is a diffeomorphism of $G$ taking $H$ to $H$ (since $H$ is a subgroup). So the slice chart at $e$ produces a slice chart at $h$ via composition with $L_h$. Hence $H$ is an embedded submanifold of $G$ at every one of its points.

5. **Lie subgroup.** By Proposition 7.11, an embedded subgroup of a Lie group is a Lie subgroup. Hence $H$ is an embedded Lie subgroup.

---

# What Makes This Hard

The slice-chart construction in Step 3 is the genuinely hard part of the proof. Several elements have to come together: the BCH-leading-order formula (which requires closedness of $H$ in an essential way), the local diffeomorphism property of $\Phi$ (from Lee Problem 20-3), and a careful compactness argument extracting a limit from a sequence in $\mathfrak{b}$ and concluding it lies in $\mathfrak{h}$ — contradicting the assumption that no slice chart exists.

The most common error is to underestimate the role of closedness. Without closure of $H$, none of the limit arguments work: a sequence in $H$ may have a limit outside $H$, breaking the argument that $\mathfrak{h}$ is closed under addition. The irrational winding example (immersed but not embedded subgroup of $T^2$) is the standard illustration that without closedness, the theorem fails.

A second subtlety is that **the theorem is automatic for matrix Lie groups in disguise**, since they are obviously closed. But the proof has to handle abstract Lie groups, where no matrix realization is in hand a priori; this is what requires the BCH formula and the slice-chart construction.

---

# Rederivation Scaffold

This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.

**High-level strategy:**
Identify a candidate Lie subalgebra $\mathfrak{h} \subseteq \mathfrak{g}$ from the data of $H$, using the exponential map. Use closure of $H$ and the BCH-leading-order limit formula to show $\mathfrak{h}$ is a linear subspace. Construct a slice chart for $H$ at $e$ via the diffeomorphism $(X, Y) \mapsto \exp(X) \exp(Y)$ with $X \in \mathfrak{h}, Y \in \mathfrak{b}$ (a complement). Extend by left translation to slice charts at every point of $H$.

**Subgoal decomposition:**

1. **Define $\mathfrak{h}$.** Set $\mathfrak{h} := \{X \in \mathfrak{g} : \exp(tX) \in H \text{ for all } t \in \mathbb{R}\}$.
   - *Hint:* This makes sense for any subset $H$ of $G$; no manifold structure needed.

2. **$\mathfrak{h}$ is a linear subspace of $\mathfrak{g}$.** Show closure under scalar multiplication (immediate) and addition (BCH-leading-order limit + closure of $H$).
   - *Hint:* For addition, use $\lim_{n \to \infty}(\exp(X/n) \exp(Y/n))^n = \exp(X + Y)$ (Lee Cor 20.11), with each term in $H$.

3. **Local slice chart at $e$.** Choose a complement $\mathfrak{b}$ to $\mathfrak{h}$, define $\Phi(X, Y) = \exp(X) \exp(Y)$. Show $\Phi$ is a local diffeomorphism near $(0,0)$ (Lee Problem 20-3), and there is a neighborhood $U_0 \subseteq \mathfrak{g}$ of $0$ such that $\exp(\mathfrak{h} \cap U_0) = H \cap \exp(U_0)$.
   - *Hint:* Proof by contradiction using a compactness argument in the complement $\mathfrak{b}$.

4. **Extend by translation.** Use left-translation by $h \in H$ to produce a slice chart at $h$.
   - *Hint:* $L_h$ is a diffeomorphism preserving $H$.

5. **Conclude.** $H$ is an embedded submanifold of $G$ at every point, hence an embedded Lie subgroup (Lee Prop 7.11).

---

# Lemma Decomposition

> [!note]- Lemma 1: $\mathfrak{h}$ is closed under scalar multiplication
> **Statement:** If $X \in \mathfrak{h}$ and $s \in \mathbb{R}$, then $sX \in \mathfrak{h}$.
>
> **Hint:** $\exp(t(sX)) = \exp((ts)X)$, which is in $H$ for all $t$ by definition of $\mathfrak{h}$.
>
> **Why needed:** Half of "$\mathfrak{h}$ is a linear subspace".
>
> > [!note]- Full proof
> > For $t \in \mathbb{R}$, $\exp(t(sX)) = \exp((ts)X) \in H$ by definition of $\mathfrak{h}$ applied with parameter $ts \in \mathbb{R}$. Hence $sX \in \mathfrak{h}$.

> [!note]- Lemma 2 (BCH-leading-order limit): $\lim_n (\exp(X/n) \exp(Y/n))^n = \exp(X + Y)$
> **Statement:** For $X, Y \in \mathfrak{g}$, $\lim_{n \to \infty} (\exp(X/n) \exp(Y/n))^n = \exp(X + Y)$.
>
> **Hint:** Use the formula $\exp(X/n) \exp(Y/n) = \exp((X + Y)/n + (1/n^2) Z(1/n))$ for some smooth $Z$ (Lee Prop 20.10).
>
> **Why needed:** Critical for showing $\mathfrak{h}$ is closed under addition.
>
> > [!note]- Full proof
> > By Lee Prop 20.10, $\exp(tX) \exp(tY) = \exp(t(X+Y) + t^2 Z(t))$ for some smooth $Z$. Substituting $t = 1/n$: $\exp(X/n) \exp(Y/n) = \exp((X+Y)/n + (1/n^2) Z(1/n))$. By Lee Prop 20.8(d), raising to the $n$th power: $(\exp(X/n) \exp(Y/n))^n = \exp(n((X+Y)/n + (1/n^2)Z(1/n))) = \exp(X + Y + (1/n) Z(1/n))$. As $n \to \infty$, $(1/n) Z(1/n) \to 0$, so the right side $\to \exp(X + Y)$ by continuity of $\exp$.

> [!note]- Lemma 3: $\mathfrak{h}$ is closed under addition
> **Statement:** If $X, Y \in \mathfrak{h}$, then $X + Y \in \mathfrak{h}$.
>
> **Hint:** Use Lemma 2 to get a sequence in $H$ converging to $\exp(t(X+Y))$; use closure of $H$.
>
> **Why needed:** Other half of "$\mathfrak{h}$ is a linear subspace".
>
> > [!note]- Full proof
> > Let $X, Y \in \mathfrak{h}$ and $t \in \mathbb{R}$. By Lemma 2 applied to $tX, tY$: $\lim_n (\exp(tX/n) \exp(tY/n))^n = \exp(t(X+Y))$. For each $n$, $\exp(tX/n) \in H$ and $\exp(tY/n) \in H$ (since $X, Y \in \mathfrak{h}$), so their product is in $H$ (subgroup), and any power is in $H$ (subgroup). Hence $(\exp(tX/n) \exp(tY/n))^n \in H$ for all $n$. As $H$ is closed, the limit $\exp(t(X+Y))$ lies in $H$. Since this holds for all $t \in \mathbb{R}$, $X + Y \in \mathfrak{h}$.

> [!note]- Lemma 4: Local slice chart at $e$
> **Statement:** There is a neighborhood $U_0 \subseteq \mathfrak{g}$ of $0$ such that $\exp|_{U_0} : U_0 \to \exp(U_0)$ is a diffeomorphism and $\exp(\mathfrak{h} \cap U_0) = H \cap \exp(U_0)$.
>
> **Hint:** Suppose not; extract a contradiction from a sequence in $\mathfrak{b}$ (a complement to $\mathfrak{h}$) using compactness.
>
> **Why needed:** It is the local slice chart that exhibits $H$ as an embedded submanifold near $e$.
>
> > [!note]- Full proof
> > [Lee pp 523–524, the slice-chart-by-contradiction argument.] Sketch: choose a complement $\mathfrak{b} \subseteq \mathfrak{g}$ to $\mathfrak{h}$, so $\mathfrak{g} = \mathfrak{h} \oplus \mathfrak{b}$. By Lee Problem 20-3, the map $\Phi(X, Y) = \exp(X) \exp(Y)$ is a local diffeomorphism near $(0, 0)$. Suppose no neighborhood $U$ satisfies $\exp(\mathfrak{h} \cap U) = H \cap \exp(U)$. Then for a countable basis $U_i \to 0$, there are $h_i \in H \cap \exp(U_i)$ with $h_i \notin \exp(\mathfrak{h} \cap U_i)$. Writing $h_i = \Phi(X_i, Y_i)$ with $(X_i, Y_i) \in \mathfrak{h} \oplus \mathfrak{b}$ and $Y_i \neq 0$, set $c_i = |Y_i|$. Then $c_i^{-1} Y_i$ lies on the unit sphere in $\mathfrak{b}$; passing to a subsequence, $c_i^{-1} Y_i \to Y \in \mathfrak{b}$ with $|Y| = 1$. The compactness argument then shows $\exp(tY) \in H$ for all $t \in \mathbb{R}$, contradicting $Y \in \mathfrak{b} \setminus \mathfrak{h}$ (since $\mathfrak{h} \cap \mathfrak{b} = \{0\}$).

---

# Formal Proof

> [!note]- Complete formal proof
> Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$ and exponential map $\exp$. Let $H \leq G$ be a closed subgroup. Define
> $$\mathfrak{h} := \{X \in \mathfrak{g} : \exp(tX) \in H \text{ for all } t \in \mathbb{R}\}.$$
>
> **Step 1 ($\mathfrak{h}$ is a linear subspace).** By Lemma 1 it is closed under scalar multiplication. By Lemma 3 it is closed under addition. Hence $\mathfrak{h} \subseteq \mathfrak{g}$ is a linear subspace.
>
> **Step 2 (slice chart at $e$).** By Lemma 4, there is a neighborhood $U_0$ of $0$ in $\mathfrak{g}$ such that $\exp|_{U_0} : U_0 \to \exp(U_0)$ is a diffeomorphism and $\exp(\mathfrak{h} \cap U_0) = H \cap \exp(U_0)$. Define the chart $\varphi := \exp^{-1}|_{\exp(U_0)} : \exp(U_0) \to U_0 \subseteq \mathfrak{g}$, and choose a linear isomorphism $\mathfrak{g} \cong \mathbb{R}^n$ with $\mathfrak{h} \cong \mathbb{R}^k \subseteq \mathbb{R}^n$ ($k = \dim \mathfrak{h}$). Then $\varphi$ is a smooth chart of $G$ at $e$, and $H \cap \exp(U_0)$ corresponds under this chart to $\mathbb{R}^k \cap U_0 \subseteq \mathbb{R}^n$ — a slice.
>
> **Step 3 (slice chart at any $h \in H$).** For $h \in H$, the left translation $L_h$ is a diffeomorphism of $G$ taking $e$ to $h$ and taking $H$ to $H$ (since $H$ is a subgroup). So $\varphi \circ L_{h^{-1}} : L_h(\exp(U_0)) \to U_0$ is a smooth chart of $G$ at $h$, and $H \cap L_h(\exp(U_0)) = L_h(H \cap \exp(U_0))$ corresponds to the slice $\mathbb{R}^k \cap U_0$.
>
> **Step 4 (embedded submanifold).** The collection of slice charts $\{\varphi \circ L_{h^{-1}} : h \in H\}$ exhibits $H$ as an embedded submanifold of $G$ of dimension $k = \dim \mathfrak{h}$.
>
> **Step 5 (Lie subgroup).** An embedded subgroup of a Lie group is automatically a Lie subgroup (Lee Prop 7.11). Hence $H$ is an embedded Lie subgroup.
>
> **Step 6 (Lie algebra equality).** By Step 4, $\dim H = \dim \mathfrak{h}$. By [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]], $\dim \mathrm{Lie}(H) = \dim H = \dim \mathfrak{h}$. Since $\mathrm{Lie}(H) \subseteq \mathfrak{h}$ (a left-invariant vector field on $H$, restricted to $\exp$ of its initial vector, gives an element with $\exp(tX) \in H$ for all $t$), and both have the same finite dimension, they are equal: $\mathrm{Lie}(H) = \mathfrak{h}$.
>
> Hence $H$ is an embedded Lie subgroup of $G$ with Lie algebra $\mathfrak{h} = \{X \in \mathfrak{g} : \exp(tX) \in H \text{ for all } t\}$. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Matrix Lie groups — computing $\mathfrak{h}$ from defining equations.** Every classical matrix Lie group is a closed subgroup of $\mathrm{GL}(n)$, and its Lie algebra is computed by differentiating the defining equations at $I$. Concrete examples: (i) for $\mathrm{O}(n)$ with equation $A^T A = I$, differentiate to $X^T + X = 0$, giving $\mathfrak{o}(n) = \{X : X^T = -X\}$, dimension $\binom{n}{2}$; (ii) for $\mathrm{SL}(n)$ with equation $\det A = 1$, differentiate to $\mathrm{tr} X = 0$, giving $\mathfrak{sl}(n) = \{X : \mathrm{tr} X = 0\}$, dimension $n^2 - 1$; (iii) for $\mathrm{Sp}(2n)$ with equation $A^T J A = J$ for the symplectic form $J$, differentiate to $X^T J + J X = 0$, giving $\mathfrak{sp}(2n) = \{X : X^T J + JX = 0\}$, dimension $n(2n + 1)$.

**Algebraic topology — fundamental group of compact Lie groups via the closed subgroup theorem.** The closed subgroup theorem provides the principal building block for computing $\pi_1$ of compact Lie groups: the centre of $G$ is a closed subgroup (hence a Lie subgroup), and the quotient $G/Z(G)$ is the **adjoint group**, with the same Lie algebra as $G$ but no central extensions. The fundamental group of $G$ relates to the kernel of $G \to G/Z(G) \hookrightarrow \mathrm{GL}(\mathfrak{g})$ via the long exact sequence of homotopy groups for the principal $Z(G)$-bundle $G \to G/Z(G)$.

**General relativity — the Lorentz group as a closed subgroup of $\mathrm{GL}(4, \mathbb{R})$.** The Lorentz group $\mathrm{O}(3, 1) = \{A \in \mathrm{GL}(4, \mathbb{R}) : A^T \eta A = \eta\}$ where $\eta = \mathrm{diag}(-1, 1, 1, 1)$ is the Minkowski metric. By the closed subgroup theorem, $\mathrm{O}(3, 1)$ is a closed embedded Lie subgroup of $\mathrm{GL}(4)$, with Lie algebra $\mathfrak{o}(3, 1) = \{X : X^T \eta + \eta X = 0\}$, dimension $6$. The identity component $\mathrm{SO}^+(3, 1)$ is the proper orthochronous Lorentz group, and its double cover $\mathrm{SL}(2, \mathbb{C}) \to \mathrm{SO}^+(3, 1)$ is the four-dimensional analogue of $\mathrm{SU}(2) \to \mathrm{SO}(3)$. The closed subgroup theorem is what gives the Lorentz group its smooth manifold structure for free.

---

# Bridges

- **The simpler "closed = embedded" for Lie subgroups** (Lee Thm 7.21): a Lie subgroup of $G$ is embedded iff it is closed. The closed subgroup theorem is a strict strengthening: it does not assume any a priori manifold structure on the subgroup. So the closed subgroup theorem says "closed subset that is a subgroup" implies "embedded Lie subgroup", while Lee 7.21 says "Lie subgroup that is closed" implies "embedded Lie subgroup". The closed subgroup theorem is strictly more powerful and is what makes the classical matrix groups (defined by equations, with no a priori manifold structure) into Lie groups for free.

- **[[Thm - Homogeneous Space is a Smooth Manifold]]** (Lee Thm 21.17) — the homogeneous-space construction depends critically on the closed subgroup theorem. For any closed $H \leq G$, the quotient $G/H$ is a manifold; the closed-ness is what ensures $G/H$ is Hausdorff. Combined with the orbit-stabilizer theorem, this gives every homogeneous space the structure of $G/H$ for a closed subgroup.

- **Lie algebra correspondence at the closed-subgroup level** — Lee Theorem 19.26 (proved using Frobenius and the closed subgroup theorem) says: every Lie subalgebra $\mathfrak{h} \subseteq \mathfrak{g}$ of the Lie algebra of $G$ is the Lie algebra of a unique connected immersed Lie subgroup $H \subseteq G$. Whether this $H$ is closed (= embedded) depends on the algebra: subalgebras that are ideals give normal subgroups; arbitrary Lie subalgebras may give non-closed Lie subgroups (the irrational winding being the canonical example).

---

# Unlocked by This

> [!tip] Homogeneous Space Theory *(from this chapter)*
> The closed subgroup theorem combined with the quotient manifold theorem gives smooth manifold structure to $G/H$ for any closed Lie subgroup $H \leq G$. See [[Thm - Homogeneous Space is a Smooth Manifold]] and [[Def - Homogeneous Space]].

> [!tip] Classical Matrix Lie Groups *(from this chapter)*
> All classical Lie groups — $\mathrm{O}(n), \mathrm{SO}(n), \mathrm{U}(n), \mathrm{SU}(n), \mathrm{Sp}(2n), \mathrm{SL}(n)$ — are defined as zero sets of polynomial equations in $\mathrm{GL}(n)$, hence closed by continuity. The closed subgroup theorem gives them all the structure of embedded Lie subgroups for free, and their Lie algebras are computed by differentiating the defining equations at $I$.

> [!tip] Compact Lie Groups and Maximal Tori *(from Lie Groups, Advanced)*
> Every compact Lie group $G$ contains a **maximal torus** $T$ — a maximal connected abelian closed Lie subgroup — and all maximal tori are conjugate. The closed subgroup theorem ensures that the maximal torus has the structure of a Lie group, and its Lie algebra $\mathfrak{t}$ is a Cartan subalgebra of $\mathfrak{g}$. The structure theory of compact Lie groups (Weyl group, root systems, weight lattice) is then read off the maximal torus.

> [!tip] Borel and Parabolic Subgroups *(from Algebraic Groups)*
> In the theory of algebraic groups (linear algebraic groups over $\mathbb{C}$ or $\mathbb{R}$), the closed subgroup theorem has an algebraic-geometric analogue. **Borel subgroups** are maximal connected solvable closed subgroups; **parabolic subgroups** are those containing a Borel. The quotients $G/B$ and $G/P$ are the **flag manifolds**, projective varieties whose geometry is the foundation of the Borel–Weil theorem and the geometric Langlands program.
