---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - The Tangent Bundle"
  - "Def - Smooth Manifold"
  - "Def - The Tangent Space"
  - "Def - Coordinate Tangent Vectors"
  - "Def - Smooth Atlas and Smooth Structure"
tags: [geometry, differential-geometry]
---

# Notation

$M$ is a smooth $n$-manifold. The tangent bundle is $TM = \bigsqcup_{p \in M} T_{p}M$ with projection $\pi : TM \to M$, $(p, v) \mapsto p$, see [[Def - The Tangent Bundle]]. For a chart $(U, \varphi)$ on $M$ with coordinates $x^{1}, \dots, x^{n}$, we define the **natural chart** $(\pi^{-1}(U), \tilde\varphi)$ on $TM$, with $\tilde\varphi : \pi^{-1}(U) \to \varphi(U) \times \mathbb{R}^{n}$ sending $(p, v)$ to $(\varphi(p), v^{1}, \dots, v^{n})$ where $v = v^{i}\,\partial/\partial x^{i}|_{p}$. The full notation registry is on [[Differential Geometry III — Tangent Vectors and the Differential]].

---

# Statement

> **Theorem ([[Def - The Tangent Bundle|The Tangent Bundle]] is a [[Def - Smooth Manifold|Smooth Manifold]]).** Let $M$ be a smooth $n$-manifold. The disjoint-union set $TM = \bigsqcup_{p \in M} T_{p}M$ admits a unique topology and smooth structure such that:
> 1. $TM$ is a smooth manifold of [[Def - Dimension|dimension]] $2n$;
> 2. The natural charts $\tilde\varphi : \pi^{-1}(U) \to \varphi(U) \times \mathbb{R}^{n}$ induced by smooth charts $(U, \varphi)$ on $M$ are smoothly compatible and form a [[Def - Smooth Atlas and Smooth Structure|smooth atlas]];
> 3. The projection $\pi : TM \to M$ is a smooth submersion;
> 4. For any smooth map $F : M \to N$, the global differential $dF : TM \to TN$ is smooth.
>
> If $M$ has [[Def - Dimension|dimension]] $n$, then $TM$ has dimension $2n$. If $M$ has a smooth structure as a manifold with boundary, then $TM$ has a smooth structure as a manifold with boundary.

> **Corollary (Global functoriality).** The assignment $M \mapsto TM$, $F \mapsto dF$ is a covariant functor from the category $\mathrm{Diff}$ of smooth manifolds to itself: $d(\mathrm{id}_{M}) = \mathrm{id}_{TM}$ and $d(G \circ F) = dG \circ dF$ as smooth maps.

---

# Motivation

The motivation is to give the disjoint union $TM = \bigsqcup_{p} T_{p}M$ a coherent geometric structure — making it a smooth manifold in its own right, not just a set. Without this structure, fundamental notions like "smooth vector field" or "smooth dependence of velocity on a curve parameter" cannot be stated.

The need is forced by three uses we want to make of $TM$:
- **Vector fields** should be smooth assignments of tangent vectors. This requires $TM$ to be a smooth manifold so that the smoothness of a section $X : M \to TM$ is meaningful.
- **Velocities of smooth curves** should be smooth in the parameter. For $\gamma : J \to M$ smooth, the map $J \to TM$, $t \mapsto \gamma'(t)$, should be smooth.
- **The global differential** $dF : TM \to TN$ should be smooth. This is the only way to make the tangent-space construction a functor on the category of smooth manifolds.

All three uses require the bundle structure. The theorem provides exactly the structure needed.

The construction is canonical: there is only one topology and one smooth structure on $TM$ making the natural charts smooth. Different charts produce *different* natural charts, but they are smoothly compatible (the change-of-chart formula on $TM$ involves the original chart-transition plus its Jacobian, both smooth), so they all extend to the same maximal smooth structure.

---

# Sources and Targets

**Sources (Input Broadening).**

The precondition is "$M$ is a smooth manifold". This is the standing assumption.

The first source is **a smooth atlas on $M$**. By the definition of smooth manifold, $M$ has a smooth atlas — a countable collection of smoothly-compatible charts. The construction transports this to a smooth atlas on $TM$: each chart $(U, \varphi)$ of $M$ gives a natural chart $(\pi^{-1}(U), \tilde\varphi)$ of $TM$, and pairwise smooth compatibility on $M$ implies pairwise smooth compatibility on $TM$. The bridge is: "smooth atlas on $M$" $\implies$ "smooth atlas on $TM$" via the natural-chart construction.

The second source is **a single coordinate computation on $M$**. The transition formula on $TM$ — $(x, v) \mapsto (\widetilde{\varphi \circ \tilde\varphi^{-1}}(x), D(\varphi \circ \tilde\varphi^{-1})_{x} \cdot v)$ — is determined by a single Jacobian computation on $M$. Once you know the chart transitions on $M$ are smooth, you get the chart transitions on $TM$ smooth for free, because matrix multiplication and partial differentiation preserve smoothness.

The third source is **Hausdorff and second-countability of $M$**. These topological properties propagate from $M$ to $TM$. Hausdorff: any two distinct points $(p, v), (q, w)$ in $TM$ are separated by disjoint open sets — either via the projection $\pi$ if $p \neq q$, or within a single fibre if $p = q$. Second-countable: a countable atlas on $M$ produces a countable atlas on $TM$. So $TM$ is a topological manifold once the natural-chart structure is in place.

**Targets (Output Amplification).**

The conclusion is "$TM$ is a smooth $2n$-manifold, with smooth projection and natural charts". Combined with various structures it amplifies.

Target 1: **combined with the differential's coordinate formula, the conclusion makes the global differential $dF : TM \to TN$ smooth**. In natural coordinates, $dF$ acts on a tangent vector $(x, v) \in TM$ by $(x, v) \mapsto (\hat{F}(x), D\hat{F}_{x} \cdot v)$, where $\hat{F}$ is the coordinate representative. Both pieces are smooth in $(x, v)$, so $dF$ is smooth on each chart $\pi^{-1}(U)$, hence smooth globally. This is the categorical statement that $T$ is a functor on smooth manifolds.

Target 2: **combined with the structure-group $\mathrm{GL}(n, \mathbb{R})$, the conclusion places $TM$ in the framework of vector bundles**. The transition functions between natural charts involve Jacobian matrices, which are elements of $\mathrm{GL}(n, \mathbb{R})$ acting linearly on the fibre — exactly the data of a rank-$n$ vector bundle. So $TM$ is the prototypical vector bundle, and the broader theory of bundles begins here. See [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]].

Target 3: **combined with the existence of smooth sections, the conclusion gives the space of vector fields a manifold-level meaning**. A vector field $X$ on $M$ is a smooth map $X : M \to TM$ with $\pi \circ X = \mathrm{id}_{M}$. Smoothness of $X$ is now meaningful (it is smoothness of a map between smooth manifolds), and the space $\Gamma(TM)$ of vector fields becomes a $C^{\infty}(M)$-module. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]].

Target 4: **combined with topological obstructions, the conclusion exposes the non-triviality of $TM$**. The natural charts make $TM$ *locally* a product, but globally $TM$ need not be diffeomorphic to $M \times \mathbb{R}^{n}$. Failure of triviality is measured by characteristic classes (Euler class, Pontryagin classes). The hairy ball theorem is the simplest example: $TS^{2} \not\cong S^{2} \times \mathbb{R}^{2}$.

---

# Why Is It True

The reason is structural: **the tangent bundle's smooth structure is *manufactured* from the manifold's smooth structure by doubling the coordinates and using the Jacobian to glue the fibre coordinates**. The construction is mechanical, and the only check is that the gluing is smooth — which is the chain rule.

**The bolded one-liner mechanism summary: $TM$ is a smooth $2n$-manifold because each chart on $M$ produces a natural chart on $TM$ with $2n$ coordinates, and transitions between these natural charts are smooth because the transition on $M$ is smooth and its Jacobian (the matrix of $dF$ acting on fibre coordinates) is smooth in $(x, v)$.**

Here is the construction in detail. Given a chart $(U, \varphi)$ on $M$ with $\varphi : U \to \hat{U} \subseteq \mathbb{R}^{n}$, define $\tilde\varphi : \pi^{-1}(U) \to \hat{U} \times \mathbb{R}^{n}$ by
$$\tilde\varphi(p, v) = (\varphi(p), v^{1}, \dots, v^{n})$$
where $v = v^{i}\,\partial/\partial x^{i}|_{p}$ — that is, $(v^{1}, \dots, v^{n})$ are the components of $v$ in the coordinate basis. This is a bijection onto $\hat{U} \times \mathbb{R}^{n}$, with inverse $\tilde\varphi^{-1}(x, v) = (\varphi^{-1}(x), v^{i}\,\partial/\partial x^{i}|_{\varphi^{-1}(x)})$.

The image $\hat{U} \times \mathbb{R}^{n}$ is an open subset of $\mathbb{R}^{2n}$. So $\tilde\varphi$ provides a candidate chart for $TM$, with $2n$ coordinates $(x^{1}, \dots, x^{n}, v^{1}, \dots, v^{n})$.

Now check **smooth compatibility**. For two charts $(U, \varphi)$ and $(V, \psi)$ on $M$ with overlap, the transition map $\psi \circ \varphi^{-1} : \varphi(U \cap V) \to \psi(U \cap V)$ is smooth. The transition between the natural charts is computed as follows. Suppose $(p, v) \in \pi^{-1}(U \cap V)$ has $\varphi$-coordinates $(x, v^{1}, \dots, v^{n})$ in the $\tilde\varphi$ chart. In the $\tilde\psi$ chart, the position part is $\psi(p) = (\psi \circ \varphi^{-1})(x)$, and the velocity components are
$$\tilde v^{j} = (\partial \tilde x^{j}/\partial x^{i})(x) \cdot v^{i},$$
where $\tilde x^{j} = (\psi \circ \varphi^{-1})^{j}$ are the components of the transition map. This is the change-of-chart formula from [[Def - Coordinate Tangent Vectors]] — the Jacobian rule.

So the transition $\tilde\psi \circ \tilde\varphi^{-1} : \hat{U} \times \mathbb{R}^{n} \to \hat{V} \times \mathbb{R}^{n}$ is given by
$$(x, v) \mapsto (\psi \circ \varphi^{-1}(x),\; D(\psi \circ \varphi^{-1})_{x} \cdot v).$$
The first component is the original transition map, smooth in $x$ by assumption. The second component is *linear* in $v$ (matrix-vector product), with the coefficients being entries of a Jacobian matrix, which are smooth functions of $x$. So the second component is smooth in $(x, v)$. Combined, the transition is smooth.

This is the only non-trivial check. Once it is in place, $TM$ inherits the topology and smooth structure from the smooth atlas of natural charts. Hausdorff and second-countability follow from the corresponding properties of $M$ and the fact that the natural-chart construction respects them.

Smoothness of $\pi$ in natural coordinates is $(x, v) \mapsto x$ — projection onto the first $n$ coordinates, manifestly smooth and submersive.

Smoothness of $dF$ in natural coordinates is $(x, v) \mapsto (\hat{F}(x), D\hat{F}_{x} \cdot v)$, where $\hat{F}$ is the coordinate representative of $F$. Both pieces are smooth, so $dF$ is smooth.

---

# What Makes This Hard

The conceptual difficulty is **recognizing that the transition formula on $TM$ has both a position part *and* a velocity part, with the velocity part being linear (Jacobian) in $v$**. People often write transition formulas for $M$ alone and forget that on $TM$ each chart's velocity coordinates depend on the choice of position chart — so the transition is not just "transition on $M$", but "transition on $M$ plus Jacobian acting on velocities".

The technical subtlety is verifying **smoothness of the Jacobian as a function of $x$**. The transition formula's velocity part is $(D(\psi \circ \varphi^{-1})_{x})^{j}_{i}\,v^{i}$, where the Jacobian entries $(D \cdot)^{j}_{i}(x)$ are smooth functions of $x$ — this is the statement that smooth maps have smooth partial derivatives, a foundational fact of multivariate analysis.

A secondary subtlety is the **Hausdorff condition on $TM$**. Two points $(p, v), (q, w) \in TM$ in different fibres are separated using disjoint charts on $M$; two points in the same fibre are separated using a single natural chart's $\mathbb{R}^{n}$ component. This is straightforward but needs to be checked carefully.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Define the natural charts $\tilde\varphi : \pi^{-1}(U) \to \varphi(U) \times \mathbb{R}^{n}$. Verify smoothness of transitions between natural charts (the position part is the original transition; the velocity part is the Jacobian acting on velocities, both smooth). Use the smooth-manifold-chart-lemma (Lee Lemma 1.35) to assemble these charts into a smooth structure. Check Hausdorff and second-countability.

**Subgoal decomposition:**

1. **Define the natural chart.** For a chart $(U, \varphi)$ on $M$, define $\tilde\varphi : \pi^{-1}(U) \to \varphi(U) \times \mathbb{R}^{n}$ by $\tilde\varphi(p, v) = (\varphi(p), v^{1}, \dots, v^{n})$ where $v = v^{i}\,\partial/\partial x^{i}|_{p}$.
   - *Hint:* This is a bijection because every $v \in T_{p}M$ has unique components in the coordinate basis.
   - *Why needed:* Sets up the chart structure on $TM$.

2. **Compute the transition between two natural charts.** For charts $(U, \varphi)$ and $(V, \psi)$ on $M$ with overlap, $\tilde\psi \circ \tilde\varphi^{-1}(x, v) = (\psi \circ \varphi^{-1}(x),\; D(\psi \circ \varphi^{-1})_{x} \cdot v)$.
   - *Hint:* The position part follows from $\tilde\varphi(p, v) = (\varphi(p), v^{i})$ and $\tilde\psi(p, v) = (\psi(p), \tilde v^{j})$. The velocity part is the chart-change formula $\tilde v^{j} = (\partial \tilde x^{j}/\partial x^{i})\,v^{i}$.
   - *Why needed:* This is the formula whose smoothness needs to be verified.

3. **Verify smoothness of the transition.** Both the position part ($\psi \circ \varphi^{-1}$ smooth) and the velocity part ($D(\psi \circ \varphi^{-1})_{x} \cdot v$ smooth in $(x, v)$, with smooth Jacobian entries) are smooth on the overlap.
   - *Hint:* The position part is smooth by the manifold structure of $M$. The velocity part is linear in $v$ (matrix-vector product), with smooth coefficients.
   - *Why needed:* This is the heart of the proof.

4. **Apply the smooth-manifold chart lemma to assemble the structure.** The countably many natural charts from a countable atlas on $M$ cover $TM$, are smoothly compatible, and satisfy the topological conditions of Lee's Lemma 1.35, so $TM$ becomes a smooth manifold.
   - *Hint:* Use the cover of $TM$ by $\pi^{-1}(U_{i})$ where $\{U_{i}\}$ is a countable atlas on $M$.
   - *Why needed:* Lifts the natural charts to a full smooth manifold structure.

5. **Verify Hausdorff and second-countability.** Two distinct points of $TM$ in different fibres are separated by $\pi^{-1}(U), \pi^{-1}(V)$ for disjoint charts $U, V$; two points in the same fibre are separated within a single natural chart. Countability of the atlas comes from countability of $\{U_{i}\}$.
   - *Hint:* Same as $M$, with the natural charts providing the open sets.
   - *Why needed:* Required by the definition of a topological manifold.

6. **Smoothness of $\pi$.** In natural coordinates, $\pi(x, v) = x$, projection onto the first $n$ coordinates, manifestly smooth and submersive.
   - *Hint:* Read off directly.
   - *Why needed:* Property 3 of the theorem.

7. **Smoothness of $dF$.** In natural coordinates, $dF(x, v) = (\hat{F}(x), D\hat{F}_{x} \cdot v)$, both pieces smooth.
   - *Hint:* Same calculation as the transition, with $\hat{F}$ in place of the transition function.
   - *Why needed:* Property 4 of the theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: The natural chart $\tilde\varphi$ is a bijection
> **Statement:** For a chart $(U, \varphi)$ on $M$, the map $\tilde\varphi : \pi^{-1}(U) \to \varphi(U) \times \mathbb{R}^{n}$, $\tilde\varphi(p, v) = (\varphi(p), v^{1}, \dots, v^{n})$ where $v^{i}$ are the components of $v$ in the coordinate basis $\partial/\partial x^{i}|_{p}$, is a bijection.
>
> **Hint:** Surjectivity by direct construction; injectivity by uniqueness of components.
>
> **Why needed:** Establishes that $\tilde\varphi$ is a chart in the topological sense.
>
> > [!note]- Full proof
> > *Surjective:* given $(x, v) \in \varphi(U) \times \mathbb{R}^{n}$, define $p = \varphi^{-1}(x) \in U$ and $v = v^{i}\,\partial/\partial x^{i}|_{p} \in T_{p}M$. Then $(p, v) \in \pi^{-1}(U)$ and $\tilde\varphi(p, v) = (x, v)$.
> >
> > *Injective:* suppose $\tilde\varphi(p, v) = \tilde\varphi(q, w)$. Then $\varphi(p) = \varphi(q)$, so $p = q$ (since $\varphi$ is a chart). And the components of $v$ and $w$ in the coordinate basis at $p$ agree, so by uniqueness of components $v = w$.

> [!note]- Lemma 2: Smoothness of the transition between natural charts
> **Statement:** For charts $(U, \varphi)$ and $(V, \psi)$ on $M$ with overlap, the transition $\tilde\psi \circ \tilde\varphi^{-1}$ between the natural charts on $TM$ is smooth on $\tilde\varphi(\pi^{-1}(U \cap V)) = \varphi(U \cap V) \times \mathbb{R}^{n}$.
>
> **Hint:** Compute the transition explicitly: position part is $\psi \circ \varphi^{-1}$, velocity part is $D(\psi \circ \varphi^{-1})_{x} \cdot v$. Both are smooth in $(x, v)$.
>
> **Why needed:** This is the smooth-compatibility condition for the natural-chart atlas on $TM$, the heart of the theorem.
>
> > [!note]- Full proof
> > Let $(p, v) \in \pi^{-1}(U \cap V)$ have $\tilde\varphi$-coordinates $(x, v^{1}, \dots, v^{n})$ with $v = v^{i}\,\partial/\partial x^{i}|_{p}$. We compute $\tilde\psi(p, v) = (\psi(p), \tilde v^{1}, \dots, \tilde v^{n})$.
> >
> > Position part: $\psi(p) = \psi(\varphi^{-1}(x)) = (\psi \circ \varphi^{-1})(x)$, which is smooth in $x$ by the manifold structure on $M$.
> >
> > Velocity part: from [[Def - Coordinate Tangent Vectors|Def - Coordinate Tangent Vectors]], $\tilde v^{j} = (\partial \tilde x^{j}/\partial x^{i})(x)\,v^{i}$ where $\tilde x^{j} = (\psi \circ \varphi^{-1})^{j}$. This is the matrix-vector product $D(\psi \circ \varphi^{-1})_{x} \cdot v$. The entries $\partial \tilde x^{j}/\partial x^{i}$ are smooth functions of $x$ (partial derivatives of a smooth map), and the matrix-vector product is linear and hence smooth in $v$. So the velocity part is smooth in $(x, v)$.
> >
> > Combined: $\tilde\psi \circ \tilde\varphi^{-1}(x, v) = (\psi \circ \varphi^{-1}(x),\; D(\psi \circ \varphi^{-1})_{x} \cdot v)$ is smooth.

> [!note]- Lemma 3: Hausdorff and second-countability of $TM$
> **Statement:** $TM$ is Hausdorff and second-countable.
>
> **Hint:** Use the natural charts. Distinct points in different fibres are separated by chart preimages; distinct points in the same fibre are separated within one natural chart.
>
> **Why needed:** These topological properties are required for $TM$ to be a topological (hence smooth) manifold.
>
> > [!note]- Full proof
> > *Hausdorff:* Let $(p, v) \neq (q, w) \in TM$. If $p \neq q$, then since $M$ is Hausdorff, there exist disjoint open sets $U, V \subseteq M$ with $p \in U, q \in V$, and after refining we can take both to be chart domains. Then $\pi^{-1}(U), \pi^{-1}(V)$ are disjoint open sets in $TM$ containing the two points. If $p = q$ and $v \neq w$, both lie in $\pi^{-1}(U)$ for some chart $U$ around $p$; their $\tilde\varphi$ images are $(\varphi(p), v^{i})$ and $(\varphi(p), w^{i})$, which are distinct in $\varphi(U) \times \mathbb{R}^{n}$, hence separated by disjoint open sets there.
> >
> > *Second-countable:* $M$ has a countable smooth atlas $\{(U_{i}, \varphi_{i})\}$. Then $\{\pi^{-1}(U_{i})\}$ is a countable open cover of $TM$, each $\pi^{-1}(U_{i})$ being homeomorphic to $\varphi_{i}(U_{i}) \times \mathbb{R}^{n}$ (which is second-countable). A countable union of second-countable spaces is second-countable.

> [!note]- Lemma 4: Smoothness of $\pi$ and $dF$
> **Statement:** The projection $\pi : TM \to M$ is a smooth submersion. For any smooth map $F : M \to N$, the global differential $dF : TM \to TN$ is smooth.
>
> **Hint:** Compute both maps in natural coordinates. They are smooth.
>
> **Why needed:** Properties 3 and 4 of the theorem.
>
> > [!note]- Full proof
> > *$\pi$ is a smooth submersion:* in natural coordinates, $\pi$ is $(x, v) \mapsto x$, projection onto the first $n$ coordinates of $\varphi(U) \times \mathbb{R}^{n}$. This is smooth (linear) and has surjective Jacobian (the first $n$ standard basis vectors), so $\pi$ is a smooth submersion.
> >
> > *$dF$ is smooth:* in natural coordinates, $dF$ takes a chart $(\pi^{-1}(U), \tilde\varphi)$ on $TM$ and a chart $(\pi^{-1}(V), \tilde\psi)$ on $TN$ (with $F(U) \subseteq V$ assumed by shrinking $U$), and acts on coordinates by $(x, v) \mapsto (\hat{F}(x), D\hat{F}_{x} \cdot v)$ where $\hat{F} = \psi \circ F \circ \varphi^{-1}$ is the coordinate representative of $F$. Both pieces are smooth in $(x, v)$ — the first by smoothness of $\hat{F}$, the second by smoothness of its Jacobian entries times linearity in $v$. So $dF$ is smooth.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** The disjoint union $TM = \bigsqcup_{p \in M} T_{p}M$ has a unique smooth structure of dimension $2n$ making the natural charts smoothly compatible, the projection $\pi$ a smooth submersion, and every global differential $dF$ smooth.
>
> *Proof.* By Lemma 1, the natural chart $\tilde\varphi$ associated to a chart $(U, \varphi)$ on $M$ is a bijection $\pi^{-1}(U) \to \varphi(U) \times \mathbb{R}^{n}$, with $\varphi(U) \times \mathbb{R}^{n}$ open in $\mathbb{R}^{2n}$.
>
> By Lemma 2, the transition between two natural charts is smooth on the overlap. So the natural charts form a smoothly compatible collection.
>
> By Lemma 3, the natural-chart structure on $TM$ is Hausdorff and second-countable, satisfying the topological-manifold axioms.
>
> Applying the smooth manifold chart lemma (Lee Lemma 1.35), the natural charts assemble into a smooth atlas on $TM$, defining the smooth structure. The dimension is $\dim(\varphi(U) \times \mathbb{R}^{n}) = n + n = 2n$.
>
> Smoothness of $\pi$ and of $dF$ follow from Lemma 4.
>
> Uniqueness: any other topology/smooth structure making the natural charts smoothly compatible would have to agree with this one on each natural-chart neighborhood, hence agree everywhere.
>
> *Proof of Corollary (Global functoriality).* Both functor axioms follow from the pointwise versions: $d(\mathrm{id})_{p} = \mathrm{id}$ (Lemma 1 of [[Thm - Chain Rule for the Differential]]) and $d(G \circ F)_{p} = dG_{F(p)} \circ dF_{p}$ (the chain rule). Both lift to smooth maps on the tangent bundles by Lemma 4 (smoothness of $dF$). So $d(\mathrm{id}_{M}) = \mathrm{id}_{TM}$ and $d(G \circ F) = dG \circ dF$ as smooth maps. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Algebraic topology — the Euler class of $TS^{2}$.** The tangent bundle of $S^{2}$ is a non-trivial rank-2 vector bundle. Its **Euler class** $e(TS^{2}) \in H^{2}(S^{2}, \mathbb{Z}) \cong \mathbb{Z}$ has the value $\chi(S^{2}) = 2$, the Euler characteristic of $S^{2}$. The non-vanishing of this class is the quantitative form of the hairy ball theorem. The construction of $TS^{2}$ as a smooth manifold (this theorem) is the prerequisite for even posing the question of characteristic classes.

**Classical mechanics — the state space of a Lagrangian system.** For a mechanical system with configuration manifold $Q$, the tangent bundle $TQ$ is the state space, equipped with a smooth structure making the Lagrangian $L : TQ \to \mathbb{R}$ a smooth function. The Euler–Lagrange equations are a smooth ODE on $TQ$ — and "smooth ODE" requires the smooth structure of $TQ$ produced by this theorem.

**Gauge theory — principal bundles and connections.** The tangent bundle $TM$ is associated to the **principal frame bundle** $FM$, whose fibre at $p$ is the set of ordered bases of $T_{p}M$. The smooth structure on $TM$ given by this theorem extends to a smooth structure on $FM$; both are smooth principal $\mathrm{GL}(n)$-bundles. The whole machinery of connections, curvature, and Yang–Mills theory rests on these smooth structures.

**Information geometry — the tangent bundle of a statistical model.** A parametric statistical model is a smooth submanifold of the space of probability measures, with the Fisher information defining a Riemannian metric. The tangent bundle of the model is a smooth manifold whose fibres carry the Fisher metric, used in maximum-likelihood estimation, natural-gradient optimization, and information-geometric methods in machine learning.

---

# Bridges

- **The Lemma 1.35 chart-by-chart construction is the canonical way to build smooth manifolds from atlases.** The smooth-manifold chart lemma (Lee's Lemma 1.35) takes a collection of bijections from open subsets to $\mathbb{R}^{n}$ (each candidate to be a chart) with smooth pairwise transitions and Hausdorff/second-countable separation properties, and produces a smooth manifold. The construction of $TM$ is one of the cleanest applications. The same construction underlies the cotangent bundle, tensor bundles, and frame bundles. See [[Differential Geometry I — Smooth Manifolds and Atlases]].

- **The Jacobian as a section of $\mathrm{Hom}(TM, TN)$ or $T^{*}M \otimes TN$.** For a smooth map $F : M \to N$, the family $\{dF_{p}\}_{p \in M}$ assembles into a smooth section of the bundle $\mathrm{Hom}(TM, F^{*}TN) \to M$ (or, dually, a smooth section of $T^{*}M \otimes F^{*}TN$). This is the geometric viewpoint of "the Jacobian as a tensor field" — it requires the smooth structure on the relevant bundles, which this theorem provides for $TM$. See [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]] and [[Differential Geometry VII — Tensors and Tensor Fields]].

- **The tangent bundle is a $\mathrm{GL}(n)$-bundle.** The transition functions of $TM$ between natural charts are Jacobian matrices, elements of $\mathrm{GL}(n, \mathbb{R})$. This places $TM$ in the framework of **structure group** for fibre bundles: the structure group of $TM$ is $\mathrm{GL}(n, \mathbb{R})$, and reducing this structure group to a subgroup gives additional geometric structure on $M$ (orientation, Riemannian metric, almost complex structure). See [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds]].

- **Local triviality and global non-triviality.** The natural charts provide local diffeomorphisms $\pi^{-1}(U) \cong U \times \mathbb{R}^{n}$. The failure of these local trivializations to extend globally is the **non-triviality of the bundle**, measured by characteristic classes. The tangent bundle of $\mathbb{R}^{n}$ or any Lie group is globally trivial; the tangent bundle of $S^{2}$ is not. This is the first geometric content of the difference between a manifold and its tangent bundle.

---

# Unlocked by This

> [!tip] Vector Bundles in General *(from Differential Geometry)*
> The tangent bundle is the prototype for the **vector bundle** concept. A rank-$k$ vector bundle on $M$ is a smooth manifold $E$ with smooth surjection $\pi : E \to M$, vector-space fibres, and locally-trivial structure. Sections, transition functions, structure groups — all the tools developed for $TM$ apply. The cotangent bundle, tensor bundles, frame bundles, and exterior-power bundles are all examples. See [[Differential Geometry VI — Vector Bundles and the Cotangent Bundle]].

> [!tip] Vector Fields as Smooth Sections *(from Differential Geometry)*
> A **vector field** on $M$ is a smooth section $X : M \to TM$ of $\pi$, i.e., a smooth map with $\pi \circ X = \mathrm{id}_{M}$. Smoothness of $X$ is now a meaningful condition (smoothness of a map between smooth manifolds). The space $\Gamma(TM)$ of vector fields is a module over $C^{\infty}(M)$. See [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]].

> [!tip] Characteristic Classes *(from Algebraic Topology)*
> The non-triviality of $TM$ — its failure to be diffeomorphic to $M \times \mathbb{R}^{n}$ — is measured by **characteristic classes** in the cohomology of $M$: the Euler class, the Pontryagin classes, the Stiefel-Whitney classes. The Euler class of $TS^{2}$ is $\chi(S^{2}) = 2$, encoding the hairy ball theorem.

> [!tip] Lagrangian Mechanics *(from Classical Mechanics)*
> A **Lagrangian** $L : TQ \to \mathbb{R}$ is a smooth function on the tangent bundle of the configuration manifold. The Euler–Lagrange equations are a second-order smooth ODE on $TQ$, with solutions the dynamical trajectories. The smooth-manifold structure of $TQ$ given by this theorem is what makes the variational formulation rigorous.
