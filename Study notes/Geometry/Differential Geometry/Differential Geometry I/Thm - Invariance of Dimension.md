---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Topological Manifold"
  - "Def - Homeomorphism"
  - "Def - Continuous Map"
tags: [geometry, differential-geometry, topology]
---

# Notation

We write $\mathbb{R}^n$ with its standard topology; open subsets of $\mathbb{R}^n$ are denoted $U, V \subseteq \mathbb{R}^n$. A [[Def - Homeomorphism|homeomorphism]] is a bijective continuous map with continuous inverse. For the full notation registry see [[Differential Geometry I — Smooth Manifolds and Atlases]].

---

# Statement

> **Theorem (Topological Invariance of Dimension; Lee Theorem 1.2 / Brouwer 1911).** Let $n, m \geq 0$. If $U \subseteq \mathbb{R}^n$ and $V \subseteq \mathbb{R}^m$ are nonempty open subsets, then $U$ and $V$ are homeomorphic only if $n = m$.

> **Corollary (Topological Invariance of Dimension for Manifolds).** Let $M$ and $N$ be nonempty [[Def - Topological Manifold|topological manifolds]] of dimensions $n$ and $m$ respectively. If $M$ and $N$ are homeomorphic, then $n = m$. In particular, every nonempty topological manifold has a well-defined dimension.

The proof of the theorem requires algebraic topology (singular homology, de Rham cohomology, or the Brouwer fixed-point theorem); we state it here and use it as a black box. A *smooth* version (where the homeomorphism is required to be a diffeomorphism) follows from elementary calculus and is Lee Theorem 2.17.

---

# Motivation

The notion of "dimension" appears explicitly in the [[Def - Topological Manifold|definition of a topological manifold]] — a topological $n$-manifold is one whose every point has a chart to an open subset of $\mathbb{R}^n$. But this is potentially ambiguous: what if the same point also has a chart to $\mathbb{R}^m$ for some $m \neq n$? Could the same point be "$n$-dimensional" from one chart and "$m$-dimensional" from another? Could the same topological space be a 1-manifold *and* a 2-manifold?

Intuitively, of course not. A line is 1-dimensional, a plane is 2-dimensional, they are visibly different objects. But the formal statement is delicate: it says that an open subset of $\mathbb{R}^n$ — which need not be all of $\mathbb{R}^n$, may be highly contorted — cannot be homeomorphic to an open subset of $\mathbb{R}^m$ for $n \neq m$. This is a *topological* statement: continuity alone — not smoothness, not differentiability — already forces the dimensions to match.

This is genuinely surprising, because at first glance, *continuity* should be a very weak condition. Cantor showed in 1878 that there is a bijection between $\mathbb{R}$ and $\mathbb{R}^2$ — these sets have the same cardinality — and that one might hope continuity alone preserves so little structure that "dimension" would not be a topological invariant. The bijection Cantor exhibited is *not* continuous, of course; but the existence of a set-theoretic bijection raises the question of whether some clever continuous bijection might exist.

Peano (1890) made the situation worse by constructing a *space-filling curve* — a continuous surjection $[0, 1] \to [0, 1]^2$ from a 1-dimensional interval onto a 2-dimensional square. So continuity alone does not preserve dimension. The remarkable fact, eventually proved by Brouwer in 1911, is that *the combination of continuity and bijectivity-with-continuous-inverse* (homeomorphism) *does* preserve dimension. A topological manifold has a well-defined dimension precisely because the chart-defining homeomorphisms are required to be homeomorphisms, not just continuous maps.

Without invariance of dimension, "the dimension of a topological manifold" would not be a well-defined phrase, and the entire definition of topological manifold would be incoherent. Theorems like "$S^n$ is an $n$-manifold" would have to be stated carefully — *which* $n$? Sources differ on convention, and the theorem is the bedrock that lets us write "dim $S^n = n$" without scare-quotes.

The proof requires genuine topological machinery. There are several routes:

- **Via singular homology:** $H_k(\mathbb{R}^n, \mathbb{R}^n \setminus 0; \mathbb{Z})$ is nonzero exactly for $k = n$. A homeomorphism $\mathbb{R}^n \to \mathbb{R}^m$ taking the origin to the origin would induce an isomorphism on these homology groups, forcing $n = m$.

- **Via de Rham cohomology:** $H^k_{dR}(\mathbb{R}^n \setminus 0)$ is nonzero exactly for $k = 0, n-1$. (For $\mathbb{R}^n \setminus 0 \simeq S^{n-1}$, and the de Rham cohomology of $S^{n-1}$ is computed in [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]].) This gives a *smooth* invariance, requiring extension to smooth maps and arguments to extend to topological setting.

- **Via the Brouwer fixed-point theorem and degree theory:** $\mathbb{R}^n$ can be distinguished from $\mathbb{R}^m$ via the degree of self-maps of spheres of different dimensions.

The argument is *intrinsically topological* — local Euclidean structure plus the topology is what determines dimension, no derivative information is needed. Lee notes (chapter 17) that the proof using de Rham cohomology is technically convenient because it builds the necessary machinery in the smooth category and then uses approximation theorems to extend.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "two nonempty homeomorphic open subsets of Euclidean spaces". The skill is recognizing situations where this hypothesis is in play but not obvious.

The first source is **two manifolds claimed to be diffeomorphic or homeomorphic**. The implication is that any chart on one corresponds to a chart on the other, and the chart dimensions must match. If we conjecture $S^3$ is homeomorphic to $\mathbb{RP}^3$ (a true statement — see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map|DG XI]], where $\mathbb{RP}^3 \cong \mathrm{SO}(3)$ is shown not to be $S^3$), the dimensions must agree (both are 3). Invariance of dimension is the *necessary condition* for homeomorphism.

The second source is **a continuous bijection from $\mathbb{R}^n$ to $\mathbb{R}^m$**. Even though Cantor showed $|\mathbb{R}| = |\mathbb{R}^2|$ as sets, no homeomorphism exists. The contrapositive: a *continuous bijection* $\mathbb{R}^n \to \mathbb{R}^m$ with $n \neq m$, if one exists, cannot have continuous inverse. (In fact, by invariance of domain — a stronger theorem of Brouwer — no such continuous bijection exists between *open* subsets of unequal-dimensional Euclidean spaces.)

The third source is **a manifold defined by a construction whose "dimension" is naively ambiguous**. For instance, the configuration space of a system can sometimes be described by different numbers of parameters in different regions (e.g., a particle constrained to a curve in $\mathbb{R}^3$ is 1-dimensional; in different parametrizations one might use 3 coordinates with 2 constraints, or 1 coordinate intrinsically — invariance of dimension says the intrinsic answer is unique). The theorem ensures the dimension is well-defined regardless of presentation.

**Targets (Output Amplification)**

The first target: **dimension is a topological invariant**, hence a *necessary* condition for homeomorphism. To show $M \not\cong N$ as topological spaces, it suffices to show $\dim M \neq \dim N$. This eliminates many pairs of manifolds from any homeomorphism question.

The second target: **the dimension of a topological manifold is well-defined**, allowing us to write $\dim M = n$ as if $n$ is a function of $M$, not of any chart. This is the foundation of every later definition (codimension of a submanifold, degree of a map between equidimensional manifolds, Euler characteristic).

The third target: **invariance-of-dimension arguments are local — every chart sees the same dimension**. If a topological manifold $M$ has charts $\varphi_\alpha : U_\alpha \to \mathbb{R}^{n_\alpha}$, then for any two overlapping charts the transition function is a homeomorphism between open subsets of $\mathbb{R}^{n_\alpha}$ and $\mathbb{R}^{n_\beta}$, forcing $n_\alpha = n_\beta$ on the overlap. If $M$ is *connected*, this forces a single dimension globally. (Without connectedness, the dimensions could differ between components — but our convention is that a "topological manifold" has a fixed dimension, so we either restrict to connected components or impose dimension as a global hypothesis.)

The fourth target: **invariance of domain (a stronger theorem)** — a continuous injective map $f : U \to \mathbb{R}^n$ from an open $U \subseteq \mathbb{R}^n$ is automatically open (its image is open in $\mathbb{R}^n$, and $f$ is a homeomorphism onto its image). This is *strictly stronger* than invariance of dimension; the proof uses the same algebraic-topology machinery. Invariance of domain is essential in submanifold theory ([[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]]) and in the proof of the topological-invariance-of-the-boundary theorem (Lee Theorem 1.37, used in [[Def - Smooth Manifold with Boundary]]).

The fifth target: **invariance of the boundary**. The topological-invariance-of-boundary theorem (Lee 1.37) — that a point of a manifold-with-boundary is either an interior point or a boundary point with respect to every chart — is a corollary of invariance of domain, hence ultimately of invariance of dimension. Without invariance of dimension, $\partial M$ would not be a well-defined set.

---

# Why Is It True

The intuition is that the *topology* near a point of $\mathbb{R}^n$ encodes its dimension: roughly speaking, removing a point from $\mathbb{R}^n$ leaves a space that is "$(n-1)$-connected but not $n$-connected" — i.e., loops, surfaces, and so on up to dimension $n-1$ can be contracted, but not the sphere $S^{n-1}$. A homeomorphism preserves all these connectedness properties, so the dimensions must match.

More precisely (in the homology formulation): for any point $p \in \mathbb{R}^n$, the local homology $H_k(\mathbb{R}^n, \mathbb{R}^n \setminus \{p\}; \mathbb{Z})$ is $\mathbb{Z}$ for $k = n$ and $0$ otherwise. This is the *local* dimension at $p$, computed by relative homology of the pair "neighbourhood of $p$ vs. that neighbourhood minus $p$". A homeomorphism $\mathbb{R}^n \to \mathbb{R}^m$ taking a point to a point would induce an isomorphism on these local homology groups — and they are concentrated in different degrees for $n \neq m$, so no such isomorphism exists.

**The one-liner mechanism: an open subset of $\mathbb{R}^n$ has nontrivial local homology in degree $n$, and a homeomorphism induces an isomorphism on local homology — so the degrees must match.**

The Brouwer-fixed-point approach gives a more concrete picture. Identify $S^n$ with the one-point compactification of $\mathbb{R}^n$, and observe that a homeomorphism $\mathbb{R}^n \to \mathbb{R}^m$ extends (under one-point compactification) to a homeomorphism $S^n \to S^m$. But the degree of the identity map of $S^n$ is $1$, and there is no degree-$\pm 1$ self-map of $S^n$ that factors through $S^m$ for $m < n$ (such a factorization would force the identity of $S^n$ to be null-homotopic, contradicting the nontriviality of $\pi_n(S^n) = \mathbb{Z}$).

For the smooth version (a homeomorphism between open subsets that happens to be smooth in both directions), the proof is much easier and entirely calculus-based: a diffeomorphism has an invertible Jacobian, and the Jacobian is a linear isomorphism between $\mathbb{R}^n$ and $\mathbb{R}^m$, forcing $n = m$. The genuinely deep content of the theorem is that *topological* homeomorphisms — without smoothness — also preserve dimension.

---

# What Makes This Hard

The theorem is folklore-easy to state, but the proof is famously delicate — Brouwer (1911) was the first to give a correct proof, after several attempts by others (including a famous error by Cantor's contemporaries who thought continuity alone might be enough). The non-obvious step is: continuity is not enough — Peano's space-filling curve shows a continuous surjection $\mathbb{R} \to \mathbb{R}^2$ exists. The crucial extra ingredient is that the *inverse* must also be continuous. Without this, no dimension invariance.

The most common error in attempted elementary proofs is to argue from the *cardinality* of $\mathbb{R}^n$ — but cardinality alone is no obstruction, since $|\mathbb{R}^n| = |\mathbb{R}|$ for all $n \geq 1$. Cardinality is not a topological invariant. The right notion is some homotopy/homology invariant of $\mathbb{R}^n$ near a point, which detects the local dimension.

The other source of confusion: the theorem applies to *open subsets* of $\mathbb{R}^n$, not arbitrary subsets. For instance, the Cantor set $C \subseteq \mathbb{R}$ is homeomorphic to $C \times C \subseteq \mathbb{R}^2$ — but $C$ and $C \times C$ are not open subsets of any Euclidean space, so the theorem does not apply. Generally, totally disconnected sets, lower-dimensional submanifolds, and fractals can have unexpected topological equivalences across "dimensions" of ambient space; the theorem applies specifically to *open subsets*.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the proof at the algebraic-topology level.**

**High-level strategy:** Find a topological invariant that distinguishes $\mathbb{R}^n$ from $\mathbb{R}^m$ for $n \neq m$. The standard choices are local homology, the homotopy type of $\mathbb{R}^n \setminus \{0\}$, or the topological degree of self-maps of compactifications.

**Subgoal decomposition:**

1. **Compute the local homology of $\mathbb{R}^n$ at a point.** Show that $H_k(\mathbb{R}^n, \mathbb{R}^n \setminus \{0\}; \mathbb{Z})$ is $\mathbb{Z}$ for $k = n$ and $0$ otherwise.
   - *Hint:* Use the long exact sequence of the pair $(\mathbb{R}^n, \mathbb{R}^n \setminus \{0\})$, and the contractibility of $\mathbb{R}^n$ together with the homotopy equivalence $\mathbb{R}^n \setminus \{0\} \simeq S^{n-1}$.
   - *Why needed:* This is the dimension-detecting invariant; the proof is essentially a transcription of it through a homeomorphism.

2. **Verify functoriality of local homology under homeomorphism.** A homeomorphism $f : U \to V$ with $U \subseteq \mathbb{R}^n$, $V \subseteq \mathbb{R}^m$ open, taking $p \in U$ to $q \in V$, induces an isomorphism $H_k(U, U \setminus \{p\}) \cong H_k(V, V \setminus \{q\})$.
   - *Hint:* Homeomorphisms induce isomorphisms on singular homology, and on pairs.
   - *Why needed:* This is what transfers the local-homology computation across the homeomorphism.

3. **Identify the local homology of an open subset of $\mathbb{R}^n$ with the local homology of $\mathbb{R}^n$.** Excision: the local homology of $U$ at $p$ equals the local homology of $\mathbb{R}^n$ at $p$, namely $\mathbb{Z}$ in degree $n$.
   - *Hint:* Apply the excision theorem to the pair $(\mathbb{R}^n, \mathbb{R}^n \setminus \{p\})$ and a small neighbourhood of $p$.
   - *Why needed:* Reduces the question about open subsets to the question about all of $\mathbb{R}^n$.

4. **Conclude $n = m$.** From the isomorphism of step 2 and the computation of step 3, both $H_n(\mathbb{R}^n)$ and $H_m(\mathbb{R}^m)$ must agree with each other up to the homeomorphism, forcing the nontrivial degree to coincide — hence $n = m$.
   - *Hint:* Compare the degree where the local homology is nonzero.
   - *Why needed:* Closes the argument.

---

# Lemma Decomposition

> [!note]- Lemma 1: Local homology of $\mathbb{R}^n$ at the origin
> **Statement:** $H_k(\mathbb{R}^n, \mathbb{R}^n \setminus \{0\}; \mathbb{Z}) \cong \mathbb{Z}$ for $k = n$ and $0$ for $k \neq n$.
>
> **Hint:** Use the long exact sequence of the pair and the homotopy equivalence $\mathbb{R}^n \setminus \{0\} \simeq S^{n-1}$.
>
> **Why needed:** This is the *dimension detector* — a topological invariant of $\mathbb{R}^n$ that vanishes outside degree $n$.
>
> > [!note]- Full proof
> > The long exact sequence of the pair $(\mathbb{R}^n, \mathbb{R}^n \setminus \{0\})$ gives
> > $$\cdots \to H_k(\mathbb{R}^n \setminus \{0\}) \to H_k(\mathbb{R}^n) \to H_k(\mathbb{R}^n, \mathbb{R}^n \setminus \{0\}) \to H_{k-1}(\mathbb{R}^n \setminus \{0\}) \to \cdots.$$
> > $\mathbb{R}^n$ is contractible, so $H_k(\mathbb{R}^n) = 0$ for $k > 0$ and $H_0(\mathbb{R}^n) = \mathbb{Z}$. The space $\mathbb{R}^n \setminus \{0\}$ deformation retracts onto $S^{n-1}$ via $x \mapsto x/|x|$, so $H_k(\mathbb{R}^n \setminus \{0\}) \cong H_k(S^{n-1})$, which is $\mathbb{Z}$ for $k = 0$ or $k = n-1$ (assuming $n \geq 1$), and $0$ otherwise. Plugging into the long exact sequence and simplifying:
> > - For $k > n$: $0 \to 0 \to H_k \to 0$, so $H_k = 0$.
> > - For $k = n$: $0 \to 0 \to H_n \to H_{n-1}(S^{n-1}) = \mathbb{Z} \to H_{n-1}(\mathbb{R}^n) = 0$, so $H_n \cong \mathbb{Z}$.
> > - For $0 < k < n$: $H_k(S^{n-1}) = 0 \to H_k(\mathbb{R}^n) = 0 \to H_k \to H_{k-1}(S^{n-1})$. For $1 \leq k \leq n - 1$, $H_{k-1}(S^{n-1})$ is $\mathbb{Z}$ if $k = 1$ and $0$ otherwise; similarly $H_k(S^{n-1})$ is $\mathbb{Z}$ if $k = n-1$ and $0$ otherwise. A small case analysis yields $H_k = 0$ in this range.

> [!note]- Lemma 2: Homeomorphisms induce isomorphisms on local homology
> **Statement:** Let $f : U \to V$ be a homeomorphism between open subsets of Euclidean spaces, with $f(p) = q$. Then $f$ induces an isomorphism $f_* : H_k(U, U \setminus \{p\}) \to H_k(V, V \setminus \{q\})$ for all $k$.
>
> **Hint:** Singular homology is functorial under continuous maps, and a homeomorphism is a continuous bijection with continuous inverse, hence induces an isomorphism.
>
> **Why needed:** Transports the local homology computation across the hypothesized homeomorphism.
>
> > [!note]- Full proof
> > Singular homology $H_k(-)$ is a functor from topological pairs to abelian groups. A homeomorphism $f : (U, U \setminus \{p\}) \to (V, V \setminus \{q\})$ is an isomorphism in the homotopy category of pairs, hence induces an isomorphism on $H_k$.

> [!note]- Lemma 3: Excision identifies the local homology of an open set with the local homology of $\mathbb{R}^n$
> **Statement:** Let $U \subseteq \mathbb{R}^n$ be open with $p \in U$. Then $H_k(U, U \setminus \{p\}) \cong H_k(\mathbb{R}^n, \mathbb{R}^n \setminus \{p\})$ for all $k$.
>
> **Hint:** Apply excision: the inclusion of pairs $(U, U \setminus \{p\}) \hookrightarrow (\mathbb{R}^n, \mathbb{R}^n \setminus \{p\})$ excises the complement of $U$ from $\mathbb{R}^n$.
>
> **Why needed:** Reduces the question about open subsets to the question about all of $\mathbb{R}^n$, which Lemma 1 has answered.
>
> > [!note]- Full proof
> > The complement $\mathbb{R}^n \setminus U$ is closed in $\mathbb{R}^n$ and disjoint from a small open ball $B$ around $p$ contained in $U$. The excision theorem says: removing the closed set $\mathbb{R}^n \setminus U$ from both members of the pair $(\mathbb{R}^n, \mathbb{R}^n \setminus \{p\})$ does not change the homology, provided the closed set lies in the interior of the complement of the smaller set $\{p\}$ — which holds since $p \in U$. Hence $H_k(\mathbb{R}^n, \mathbb{R}^n \setminus \{p\}) \cong H_k(U, U \setminus \{p\})$.

---

# Formal Proof

> [!note]- Complete formal proof (algebraic topology version)
> **Theorem.** If $U \subseteq \mathbb{R}^n$ and $V \subseteq \mathbb{R}^m$ are nonempty homeomorphic open subsets, then $n = m$.
>
> *Proof.* Let $f : U \to V$ be a homeomorphism, $p \in U$, $q = f(p) \in V$. By Lemma 3 and Lemma 1,
> $$H_k(U, U \setminus \{p\}; \mathbb{Z}) \cong H_k(\mathbb{R}^n, \mathbb{R}^n \setminus \{p\}; \mathbb{Z}) \cong \begin{cases} \mathbb{Z} & k = n, \\ 0 & k \neq n. \end{cases}$$
> Similarly,
> $$H_k(V, V \setminus \{q\}; \mathbb{Z}) \cong \begin{cases} \mathbb{Z} & k = m, \\ 0 & k \neq m. \end{cases}$$
> By Lemma 2, $f$ induces an isomorphism $H_k(U, U \setminus \{p\}) \cong H_k(V, V \setminus \{q\})$ for every $k$. Comparing degrees, both groups are nonzero only in a single degree, which must coincide. Hence $n = m$. $\blacksquare$
>
> *Proof of the manifold corollary.* Suppose $M$ is a connected topological $n$-manifold and $N$ is a connected topological $m$-manifold and they are homeomorphic via $F : M \to N$. Pick a smooth chart $(U, \varphi)$ on $M$ with image $\widehat{U} \subseteq \mathbb{R}^n$ open, and a chart $(V, \psi)$ on $N$ with image $\widehat{V} \subseteq \mathbb{R}^m$ open and $F(U) \subseteq V$ (possible by continuity and shrinking $U$). Then $\psi \circ F \circ \varphi^{-1} : \widehat{U} \to \widehat{V}$ is a continuous injective map between open subsets of $\mathbb{R}^n$ and $\mathbb{R}^m$. Restricting to a smaller chart $(U_0, \varphi_0)$ containing a point and a chart $(V_0, \psi_0)$ containing its image — and ensuring the restriction is still a homeomorphism (which follows from $F$ being a homeomorphism of the manifolds) — gives a homeomorphism between nonempty open subsets of $\mathbb{R}^n$ and $\mathbb{R}^m$. By the theorem, $n = m$. $\blacksquare$
>
> *Note on the smooth case (Lee Theorem 2.17).* If $F : M \to N$ is a diffeomorphism between smooth manifolds, the proof is much simpler: in the coordinate representation $\psi \circ F \circ \varphi^{-1}$, the Jacobian is a linear isomorphism $\mathbb{R}^n \to \mathbb{R}^m$, forcing $n = m$. This smooth version is part of multivariable calculus and requires no algebraic topology.

---

# Cross-Field Exercise Suggestions

**Algebraic topology — local homology as a dimension detector.** The proof above can be turned into an exercise: compute $H_k(\mathbb{R}^n, \mathbb{R}^n \setminus \{0\})$ from the long exact sequence and deformation retraction, then verify the dimension-detection property. This is the prototype of "use a topological invariant to distinguish spaces".

**Linear algebra — invariance of dimension for vector spaces.** The vector-space analogue: the dimension of a finite-dimensional vector space $V$ is well-defined — any two bases have the same cardinality, by the *exchange lemma*. The argument is purely linear-algebraic and much easier than the topological version; in fact, for *smooth* manifolds, invariance of dimension reduces to this linear-algebra fact via the chain rule.

**Brouwer fixed-point theorem.** Brouwer's theorem (every continuous map $D^n \to D^n$ has a fixed point) is closely related: both are consequences of the nontriviality of the top homology of $S^n$, and both were proved by Brouwer using similar arguments. The proof of invariance of dimension via Brouwer fixed-point goes: a homeomorphism $\mathbb{R}^n \to \mathbb{R}^m$ extends to a homeomorphism of one-point compactifications $S^n \to S^m$, which is impossible for $n \neq m$ because the identity map of $S^n$ cannot factor through $S^m$ (the degree would not match).

**Cantor's space-filling phenomena — the necessity of continuous inverses.** Cantor's bijection $\mathbb{R} \to \mathbb{R}^2$ and Peano's continuous surjection $[0,1] \to [0,1]^2$ show that continuity alone is too weak. The theorem requires *both* continuity and continuous inverse. This is a useful diagnostic: if a "dimension-changing" map exists, it is either not continuous (Cantor) or its inverse is not continuous (Peano).

---

# Bridges

- **Brouwer's invariance of domain** — a strictly stronger theorem: a continuous *injective* map $f : U \to \mathbb{R}^n$ from an open $U \subseteq \mathbb{R}^n$ is automatically an open map onto its image (in particular, the image is open in $\mathbb{R}^n$ and $f$ is a homeomorphism onto its image). This is essential for smooth manifold theory because it ensures that the image of an injective immersion is locally a graph (see [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]] and Lee Theorem 1.46 on smooth invariance of the boundary).

- **Topological invariance of the boundary** (Lee Theorem 1.37) — a corollary of invariance of domain. A point $p$ of a topological manifold-with-boundary $M$ is either a boundary point or an interior point with respect to *every* chart; the partition $M = \operatorname{Int} M \sqcup \partial M$ is well-defined. Without this theorem, the [[Def - Smooth Manifold with Boundary|definition of the boundary ∂M]] would be incoherent. Lee defers the proof to Chapter 17 (which uses de Rham cohomology, hence requires the apparatus of [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]]).

- **Smooth invariance of dimension** (Lee Theorem 2.17) — the *smooth* version, where the homeomorphism is required to be a diffeomorphism, is much easier: a diffeomorphism has a linear isomorphism as Jacobian, and a linear isomorphism between $\mathbb{R}^n$ and $\mathbb{R}^m$ exists iff $n = m$. The topological version (the present theorem) is genuinely deeper.

- **Sard's theorem** ([[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds|DG IV]]) — for any smooth map $f : M^n \to N^m$ with $n < m$, the image $f(M)$ has measure zero in $N$. This is the *smooth* analogue of "low-dimensional cannot fill high-dimensional", and is much stronger than invariance of dimension: it says low-dimensional sources cannot even *cover* high-dimensional targets, much less be homeomorphic to them. For smooth maps, dimension cannot be "raised by continuity" in any useful sense.

---

# Unlocked by This

> [!tip] Dimension as a Well-Defined Manifold Invariant *(used throughout the rest of the subject)*
> Every later definition that uses dimension — codimension of a submanifold, degree of a map, Euler characteristic, top form on an oriented manifold — depends on dimension being a well-defined invariant. This theorem is the foundation.

> [!tip] Topological vs. Smooth Manifold Classification *(from Differential Topology)*
> In dimension $\leq 3$, the topological and smooth classifications of manifolds coincide (every topological manifold of dimension $\leq 3$ admits a unique smooth structure). In dimensions $\geq 5$, they typically differ (exotic smooth structures on spheres). In dimension 4, the divergence is extreme — Donaldson's exotic $\mathbb{R}^4$'s. Understanding the topological-vs-smooth divide is one of the deepest projects of modern geometry.

> [!tip] Invariance of Domain *(from Algebraic Topology)*
> The strictly stronger result — every continuous injection between open subsets of $\mathbb{R}^n$ is open — is the workhorse of submanifold theory. Without it, the image of an embedding could fail to be a topological subspace in the expected sense.

> [!tip] Manifolds with Boundary and the Boundary Invariance Theorem *(from this chapter, §1.4)*
> The companion theorem (Lee 1.37) — that the boundary $\partial M$ of a manifold-with-boundary is well-defined — is a direct consequence of invariance of domain. Without it, [[Def - Smooth Manifold with Boundary|smooth manifolds with boundary]] would not have a well-defined boundary.
