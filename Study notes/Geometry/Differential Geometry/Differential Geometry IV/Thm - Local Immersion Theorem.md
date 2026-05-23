---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Map between Manifolds"
  - "Def - The Differential of a Smooth Map"
  - "Def - Immersion, Submersion, and Embedding"
  - "Thm - The Rank Theorem"
  - "Thm - The Inverse Function Theorem"
tags: [geometry, differential-geometry]
---

# Notation

$F : M \to N$ is a smooth map between smooth manifolds with $\dim M = m \leq n = \dim N$. The differential at $p$ is $dF_p : T_p M \to T_{F(p)} N$. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

---

# Statement

> **Theorem (Local Immersion Theorem).** Let $F : M \to N$ be a smooth map. The following are equivalent at a point $p \in M$:
> 1. $F$ is an immersion at $p$ — that is, $dF_p$ is injective ($\mathrm{rank}\, dF_p = m$);
> 2. There exist smooth charts $(U, \varphi)$ for $M$ centred at $p$ and $(V, \psi)$ for $N$ centred at $F(p)$ with $F(U) \subseteq V$, such that the coordinate representation has the form
> $$\psi \circ F \circ \varphi^{-1}(x^1, \dots, x^m) = (x^1, \dots, x^m, 0, \dots, 0).$$

> **Corollary (Local Embedding).** If $F$ is an immersion at $p$, then there is a neighbourhood $U$ of $p$ in $M$ such that $F|_U : U \to N$ is a smooth embedding.

---

# Motivation

This theorem is the **immersion specialisation of [[Thm - The Rank Theorem|the rank theorem]]**. It says that *any* smooth immersion at a point looks, in suitable local coordinates, like the standard inclusion of $\mathbb{R}^m$ into $\mathbb{R}^n$ as the first $m$ coordinates. The rank theorem's hypothesis of "constant rank in a neighbourhood" is automatic for immersions, because the maximal rank $m$ is preserved on an open neighbourhood by lower semicontinuity ([[Def - Rank of a Smooth Map]]).

The result is the local version of the question "what does an immersion look like?", and the answer is "the simplest possible thing — a coordinate inclusion". This makes immersions the local-injectivity-respecting smooth maps: every immersion is locally a smooth embedding (its image is locally a flat coordinate slice). The "local" qualifier is essential — globally, an immersion can fail to be an embedding (figure-eight, dense torus line), because global injectivity or the [[Def - Homeomorphism|homeomorphism]] condition may fail. But near each point, an immersion is as nice as possible.

The corollary about local embedding is the bridge from the linear-algebraic immersion condition to the topological-embedding condition: every immersion is *locally* an embedding, by restricting to a sufficiently small neighbourhood. This is why immersions are sometimes called "local embeddings" — locally they are always embeddings, even when globally they fail to be.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$dF_p$ is injective". Recognising this in disguise:

The first disguised source is **a parametrisation by an open subset of $\mathbb{R}^m$**. Property $B$: $F : U \to N$ where $U \subseteq \mathbb{R}^m$ is open, and the columns of the Jacobian matrix $DF(p)$ are linearly independent at $p$. The bridge: linear independence of columns *is* injectivity of the linear map represented by the matrix. So *any* parametrisation with linearly independent partial-derivative vectors at a point is locally an immersion there. *Example:* the graph parametrisation $G(x) = (x, g(x))$ has $DG(x) = \begin{pmatrix} I \\ Dg(x) \end{pmatrix}$ with the top block the identity, so the columns are always linearly independent — graph parametrisations are immersions.

The second disguised source is **a curve with nonzero velocity**. Property $B$: $\gamma : J \to N$ is a smooth curve with $\gamma'(t) \neq 0$ for all $t \in J$. The bridge: $d\gamma_t : T_t \mathbb{R} \to T_{\gamma(t)} N$ is the linear map $a \mapsto a \gamma'(t)$, which is injective iff $\gamma'(t) \neq 0$. So *any* smooth curve with nonvanishing velocity is an immersion. *Example:* a regular curve in $\mathbb{R}^3$ — one parametrised by arc length, say — is automatically an immersion of $\mathbb{R}$ into $\mathbb{R}^3$.

The third disguised source is **a smooth section of a submersion**. Property $B$: $\sigma : N \to M$ is a smooth map and there is a smooth submersion $F : M \to N$ with $F \circ \sigma = \mathrm{id}_N$. The bridge: differentiating $F \circ \sigma = \mathrm{id}_N$ at any point gives $dF_{\sigma(p)} \circ d\sigma_p = \mathrm{id}_{T_p N}$, which forces $d\sigma_p$ to be injective (a left-invertible linear map is injective). So *every smooth section of a submersion is an immersion*. *Example:* the zero section of a vector bundle is an immersion of the base into the total space.

**Targets (Output Amplification)**

The conclusion is "in suitable coordinates, $F$ is the standard inclusion $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^m, 0, \dots, 0)$".

Combine the conclusion with **the question of local injectivity.** Property $D$: you want to know whether $F$ is injective on some neighbourhood of $p$. The amplified result $E$: in the normal-form coordinates, $F$ *is* the standard inclusion of $\mathbb{R}^m$ into $\mathbb{R}^n$, which is patently injective. So $F$ is automatically injective on the chart's domain — every immersion is locally injective. The combination is the local-embedding corollary.

Combine the conclusion with **compactness of the domain.** Property $D$: $M$ is compact. The amplified result $E$: a *globally injective* immersion from a compact $M$ to $N$ is automatically a smooth embedding ([[Def - Immersion, Submersion, and Embedding|Proposition 4.22(c) of Lee]]). This is because the closed map lemma plus injectivity plus continuity makes the map a homeomorphism onto its image. So the global injectivity assumption — which the local immersion theorem does not give — is bridged by compactness.

Combine the conclusion with **the question of image structure.** Property $D$: you want to understand what $F(U)$ looks like as a subset of $N$. The amplified result $E$: in the normal-form coordinates, $F(U)$ is the coordinate slice $\{y^{m+1} = \dots = y^n = 0\}$ — a flat $m$-dimensional embedded submanifold of $V \subseteq N$. So the image of any immersion is *locally* an embedded submanifold of $N$ of dimension $\dim M$. This connects the immersion theorem to the submanifold theory: immersions produce submanifolds (locally, and globally when injective and the topology works out).

---

# Why Is It True

The intuition is the rank theorem's intuition in the special case of maximal injective rank, and it has a clean direct proof using the [[Thm - The Inverse Function Theorem|inverse function theorem]].

**The bolded one-liner mechanism summary: the immersion's image is, by injectivity of the differential, transversal to a complementary [[Def - Subspace|subspace]]; completing $F$ by carrying along a basis of the complement produces a local diffeomorphism, which then provides the coordinate normal form.**

Here is the construction. In local coordinates around $p$ and $F(p)$, $F$ is represented by a smooth map $\hat F : U \to \mathbb{R}^n$ with $\hat F(0) = 0$ and $D\hat F(0)$ injective. By a permutation of target coordinates, assume the upper $m \times m$ block of $D\hat F(0)$ is invertible — write $\hat F(x) = (F^1(x), \dots, F^n(x))$ and let $\Pi = (F^1, \dots, F^m)$ be the first $m$ components; then $D\Pi(0)$ is the upper $m \times m$ block of $D\hat F(0)$, invertible.

Now extend $\hat F$ to a square map by completing with the last $n - m$ target coordinates as new source coordinates. Define $G : U \times \mathbb{R}^{n-m} \to \mathbb{R}^n$ by
$$G(x, t) = \hat F(x) + (0, \dots, 0, t^1, \dots, t^{n-m}) = (F^1(x), \dots, F^m(x), F^{m+1}(x) + t^1, \dots, F^n(x) + t^{n-m}).$$
This is a smooth map from an open subset of $\mathbb{R}^n$ to $\mathbb{R}^n$, with $G(0, 0) = 0$. Its Jacobian at $(0, 0)$ is
$$DG(0,0) = \begin{pmatrix} D\Pi(0) & 0 \\ * & I_{n-m} \end{pmatrix},$$
which is block-lower-triangular with invertible diagonal blocks — hence invertible. By the [[Thm - The Inverse Function Theorem|inverse function theorem]], $G$ is a local diffeomorphism near $(0,0)$.

This gives the new target coordinates. Let $\psi = G^{-1}$; this is a smooth diffeomorphism from a neighbourhood of $0$ in $\mathbb{R}^n$ (target) to a neighbourhood of $(0,0)$ in $\mathbb{R}^m \times \mathbb{R}^{n-m} = \mathbb{R}^n$. The composition $\psi \circ \hat F$ takes a point $x \in U$ to $\psi(\hat F(x)) = G^{-1}(\hat F(x))$, and we want to verify this equals $(x, 0)$. Well, $G(x, 0) = \hat F(x)$ by construction (the $t$-block contributes nothing when $t = 0$), so $G^{-1}(\hat F(x)) = (x, 0)$. Hence
$$\psi \circ \hat F(x) = (x, 0) = (x^1, \dots, x^m, 0, \dots, 0)$$
— the standard inclusion. The source coordinates are unchanged; only the target chart was rebuilt.

So the construction is: complete $\hat F$ to a square map by carrying along the last $n - m$ target coordinates as new source coordinates; the square map is invertible (its Jacobian is block-triangular with invertible blocks), so by IFT a target coordinate change exists in which $\hat F$ becomes the standard inclusion.

Why does injectivity of $dF_p$ correspond to invertibility of the square completion? Because injectivity at the differential level means the columns of $D\hat F(0)$ are linearly independent, hence span an $m$-dimensional subspace of $\mathbb{R}^n$. The square completion's extra columns are the standard basis vectors $e_{m+1}, \dots, e_n$ in the target (with zero contribution to the source coordinates). Together these span all of $\mathbb{R}^n$ iff they together are linearly independent, iff the original $m$ columns are linearly independent from $e_{m+1}, \dots, e_n$, iff (after the coordinate permutation) the upper $m \times m$ block of $D\hat F(0)$ is invertible. So the geometric meaning is "the immersion's image is transversal to the carried-along subspace, by injectivity".

The local-embedding corollary follows immediately: in the normal-form coordinates, $F$ is the standard inclusion of $\varphi(U) \subseteq \mathbb{R}^m$ into $\psi(V) \subseteq \mathbb{R}^n$, which is a smooth embedding (it is a smooth immersion and a topological embedding — it is a homeomorphism onto its image in the subspace topology, because both are equipped with their Euclidean topologies and the inclusion is the identity on the first $m$ coordinates).

---

# What Makes This Hard

The non-obvious step is the **square completion construction** — choosing how to extend $\hat F$ to a square map. Students often try to complete on the *source* side (by adding $n - m$ extra source coordinates), but the natural completion is on the *target* side: carry $n - m$ target coordinates back as new source coordinates with the identity dependence. This is symmetric to the [[Thm - The Implicit Function Theorem|implicit function theorem]]'s carry-along construction (which carries source coordinates forward); for immersions, you carry *target* coordinates *backward*. The most common error is forgetting that the inverse function theorem requires invertibility of the *full* Jacobian — students sometimes write down a partial completion that does not square out properly.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Reduce to Euclidean coordinates via initial charts. Permute target coordinates so the upper $m \times m$ block of the Jacobian is invertible. Construct an auxiliary square map $G : \mathbb{R}^n \to \mathbb{R}^n$ that completes $\hat F$ by "carrying along" the last $n - m$ target coordinates as new source coordinates. The Jacobian of $G$ is block-triangular with invertible diagonal blocks, hence invertible; apply the inverse function theorem to invert it. The inverse provides the target diffeomorphism that turns $\hat F$ into the standard inclusion.

**Subgoal decomposition:**

1. **Reduce to Euclidean coordinates.** Choose initial smooth charts $(U_0, \varphi_0)$ centred at $p$ and $(V_0, \psi_0)$ centred at $F(p)$. Work with $\hat F = \psi_0 \circ F \circ \varphi_0^{-1}$, a smooth map from an open neighbourhood of $0$ in $\mathbb{R}^m$ to $\mathbb{R}^n$, with $\hat F(0) = 0$ and $D\hat F(0)$ injective.
   - *Hint:* Center the charts; injectivity is invariant under chart changes.
   - *Why needed:* Local statements about $F$ reduce to local statements about $\hat F$.

2. **Permute target coordinates to expose an invertible upper block.** Since $D\hat F(0)$ has rank $m$, it has an invertible $m \times m$ submatrix. By permuting target coordinates, arrange that this is the upper block.
   - *Hint:* Permuting target coordinates is a linear diffeomorphism on the target side.
   - *Why needed:* It positions us to construct an invertible square completion.

3. **Construct the square completion.** Define $G : U \times \mathbb{R}^{n-m} \to \mathbb{R}^n$ by
   $$G(x, t) = (\hat F^1(x), \dots, \hat F^m(x),\, \hat F^{m+1}(x) + t^1, \dots, \hat F^n(x) + t^{n-m}).$$
   - *Hint:* The first $m$ output coordinates depend only on $x$; the last $n - m$ output coordinates carry $t$ in addition to $\hat F$.
   - *Why needed:* It builds a smooth map between equal-dimensional spaces that "extends" $\hat F$.

4. **Verify $DG(0, 0)$ is invertible.** Compute the Jacobian and check the block-triangular structure with invertible diagonal blocks.
   - *Hint:* $DG(0,0) = \begin{pmatrix} D\Pi(0) & 0 \\ * & I_{n-m} \end{pmatrix}$ where $D\Pi(0)$ is the upper $m \times m$ block, invertible by Step 2.
   - *Why needed:* It activates the inverse function theorem.

5. **Apply the inverse function theorem to $G$.** The [[Thm - The Inverse Function Theorem|inverse function theorem]] gives a smooth local inverse $\psi = G^{-1}$ defined near $0 \in \mathbb{R}^n$ (target side), with values in a neighbourhood of $(0,0) \in U \times \mathbb{R}^{n-m}$.
   - *Hint:* $G(0,0) = 0$, so the IFT gives an inverse on a neighbourhood of $0$.
   - *Why needed:* $\psi$ is the new target chart that turns $\hat F$ into the standard inclusion.

6. **Verify $\psi \circ \hat F$ is the standard inclusion.** Since $G(x, 0) = \hat F(x)$ for all $x$ near $0$, we have $\psi(\hat F(x)) = G^{-1}(\hat F(x)) = (x, 0)$. So $\psi \circ \hat F(x) = (x^1, \dots, x^m, 0, \dots, 0)$.
   - *Hint:* Substitute $t = 0$ into the definition of $G$.
   - *Why needed:* It verifies the standard form.

7. **Return to manifold charts.** Combine $\psi$ with the initial target chart $\psi_0$ to get the new target chart on $N$; the source chart can remain $\varphi_0$ (no change of source coordinates was needed).
   - *Hint:* Composition of smooth charts with smooth [[Def - Diffeomorphism|diffeomorphisms]] gives smooth charts.
   - *Why needed:* It returns from Euclidean coordinates to manifold charts.

---

# Lemma Decomposition

> [!note]- Lemma 1: The square completion of an immersion is locally a diffeomorphism
> **Statement:** Let $\hat F : U \to \mathbb{R}^n$ be smooth on $U \subseteq \mathbb{R}^m$ open, with $\hat F(0) = 0$ and the upper $m \times m$ block of $D\hat F(0)$ invertible. Define $G : U \times \mathbb{R}^{n-m} \to \mathbb{R}^n$ by $G(x, t) = (\hat F^1(x), \dots, \hat F^m(x), \hat F^{m+1}(x) + t^1, \dots, \hat F^n(x) + t^{n-m})$. Then $G$ is a smooth local diffeomorphism near $(0, 0)$.
>
> **Hint:** Compute $DG(0,0)$ and check it is invertible via block-triangular determinant.
>
> **Why needed:** It is the auxiliary square map whose inverse provides the target diffeomorphism for the normal form.
>
> > [!note]- Full proof
> > The Jacobian of $G$ at $(0,0)$ has the block structure
> > $$DG(0, 0) = \begin{pmatrix} \partial \hat F^i / \partial x^j(0)_{1 \leq i, j \leq m} & 0_{m \times (n-m)} \\ \partial \hat F^i / \partial x^j(0)_{m < i \leq n,\, 1 \leq j \leq m} & I_{n-m} \end{pmatrix}.$$
> > The top-right block is $0$ because $\hat F^i$ does not depend on $t$ for $i \leq m$; the bottom-right block is $I_{n-m}$ because $\hat F^i + t^{i-m}$ has $\partial/\partial t^j = \delta^{i-m}_j$. This is block-lower-triangular with diagonal blocks $D\Pi(0)$ (the upper $m \times m$ block of $D\hat F(0)$, invertible by hypothesis) and $I_{n-m}$. Its determinant is the product of the diagonal blocks' [[Def - Determinant|determinants]], $\det D\Pi(0) \cdot 1 \neq 0$. So $DG(0,0)$ is invertible, and by the [[Thm - The Inverse Function Theorem|inverse function theorem]] $G$ is a local diffeomorphism near $(0,0)$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F : M \to N$ be smooth with $dF_p$ injective. We show the existence of coordinate charts producing the standard inclusion form.
>
> **Step 0 (reduction).** Choose smooth charts $(U_0, \varphi_0)$ for $M$ centred at $p$ and $(V_0, \psi_0)$ for $N$ centred at $F(p)$ with $F(U_0) \subseteq V_0$. The coordinate representation $\hat F = \psi_0 \circ F \circ \varphi_0^{-1}$ is a smooth map from an open neighbourhood of $0$ in $\mathbb{R}^m$ to $\mathbb{R}^n$, $\hat F(0) = 0$, $D\hat F(0)$ injective.
>
> **Step 1 (permute target coordinates).** $D\hat F(0)$ has rank $m$, so it has $m$ linearly independent rows. After permuting target coordinates, assume the first $m$ rows are linearly independent, i.e., the upper $m \times m$ block of $D\hat F(0)$ is invertible.
>
> **Step 2 (square completion).** By Lemma 1, the map $G(x, t) = (\hat F^1(x), \dots, \hat F^m(x), \hat F^{m+1}(x) + t^1, \dots, \hat F^n(x) + t^{n-m})$ from $U_0 \times \mathbb{R}^{n-m}$ to $\mathbb{R}^n$ is a smooth local diffeomorphism near $(0, 0)$. The [[Thm - The Inverse Function Theorem|inverse function theorem]] gives a smooth local inverse $\psi = G^{-1}$ defined on a neighbourhood of $0$ in $\mathbb{R}^n$ (target).
>
> **Step 3 (verify normal form).** For $x$ in a neighbourhood of $0$, $G(x, 0) = \hat F(x)$ (the $t$-terms vanish when $t = 0$). Hence $\psi(\hat F(x)) = G^{-1}(\hat F(x)) = (x, 0)$, i.e., $\psi \circ \hat F(x) = (x^1, \dots, x^m, 0, \dots, 0)$.
>
> **Step 4 (manifold charts).** Define the new target chart on $N$ as $(V, \tilde\psi)$ where $V$ is a suitable open subset of $V_0$ and $\tilde\psi = \psi \circ \psi_0|_V$. With the source chart $\varphi_0$ unchanged and the target chart $\tilde\psi$, the coordinate representation of $F$ is the standard inclusion $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^m, 0, \dots, 0)$.
>
> The corollary (local embedding) follows: in these coordinates $F|_U$ is the inclusion of an open subset of $\mathbb{R}^m$ into $\mathbb{R}^n$, which is a smooth embedding (it is a homeomorphism onto its image — the slice $\{(x, 0) : x \in \varphi(U)\}$ — in the subspace topology, and a smooth immersion). Hence $F|_U$ is a smooth embedding.
>
> $\qquad\blacksquare$
>
> The converse (2 ⟹ 1) is trivial: if $F$ has coordinate representation the standard inclusion, its differential is the standard inclusion's linear map $(v^1, \dots, v^m) \mapsto (v^1, \dots, v^m, 0, \dots, 0)$, which is injective. So 1 and 2 are equivalent.

---

# Cross-Field Exercise Suggestions

**Parametrised surfaces in $\mathbb{R}^3$.** A smooth map $X : U \to \mathbb{R}^3$ from an open $U \subseteq \mathbb{R}^2$ with linearly independent partials $\partial X/\partial u, \partial X/\partial v$ is an immersion. The local immersion theorem says that locally the parametrised surface is the standard inclusion $\mathbb{R}^2 \hookrightarrow \mathbb{R}^3$ — that is, locally a flat plane in suitable coordinates. The application is to surface theory: many results about smooth surfaces (first fundamental form, Gauss map, curvature) are local and reduce to the standard plane via the immersion theorem.

**Smooth knot theory.** A smooth knot is a smooth embedding $S^1 \hookrightarrow \mathbb{R}^3$ — and equivalently a smooth injective immersion from $S^1$ (which is compact, so injective immersion = embedding automatically). The local immersion theorem says any smooth knot is, near each point, the standard inclusion of an arc into $\mathbb{R}^3$ — locally trivial. The interesting knot theory is in the *global* topology of the embedding, not the local structure.

**Smooth sections of vector bundles.** Given a smooth vector bundle $\pi : E \to M$, a smooth section is a smooth map $s : M \to E$ with $\pi \circ s = \mathrm{id}_M$. Differentiating, $d\pi_{s(p)} \circ ds_p = \mathrm{id}_{T_p M}$, which forces $ds_p$ to be injective — so every smooth section of a vector bundle is an immersion. The image $s(M)$ is locally embedded by the local immersion theorem (and globally embedded if $s$ is sufficiently nice).

**Submanifold reconstructions in geometric measure theory.** Smooth approximations of irregular sets often start with a smooth immersion from a regularised parameter domain. The local immersion theorem ensures the image is locally a smooth embedded submanifold — providing a local smoothness baseline against which the regularity of the approximation is measured.

---

# Bridges

- **[[Thm - The Rank Theorem|Rank Theorem]]** — the parent. The local immersion theorem is the rank theorem with $r = m$ (the immersion case). The general rank theorem reduces to this when "the map is constant-rank maximal-injective"; the immersion case has no constant-rank issue because the rank is automatically maximal on a neighbourhood.

- **[[Thm - The Inverse Function Theorem|Inverse Function Theorem]]** — the engine. The proof's only nontrivial step is applying the IFT to the square completion of $\hat F$. The two are mutually equivalent at this level: IFT implies local immersion theorem (above proof); local immersion theorem implies IFT (in the case $m = n$, the standard inclusion form $(x^1, \dots, x^n) \mapsto (x^1, \dots, x^n)$ *is* the identity).

- **[[Thm - The Implicit Function Theorem|Implicit Function Theorem]]** — the dual on the target side. The IFT carries source coordinates *forward* to the target via the carry-along construction; the local immersion theorem carries target coordinates *backward* to the source. The two are duals.

- **[[Thm - Local Submersion Theorem|Local Submersion Theorem]]** — the rank-theoretic dual. The submersion case ($r = n$) is the local submersion theorem; the immersion case ($r = m$) is the local immersion theorem. They are the two extreme rank specialisations of the rank theorem.

- **[[Def - Embedded Submanifold|Embedded Submanifold]]** — the downstream consequence. By the corollary (local embedding), the image of an immersion is locally an embedded submanifold of dimension $\dim M$. So immersions produce locally embedded submanifolds; this is the parametric representation in the equivalences of [[Def - Embedded Submanifold]].

- **[[Ex - The Figure-Eight Immersion]]** — the canonical example of "local but not global". The figure-eight is locally an embedding (at every point in the domain), but globally fails because the image's subspace topology disagrees with the domain's topology.

---

# Unlocked by This

> [!tip] Smooth Submanifolds via Parametrisation *(from this topic)*
> The local immersion theorem is the engine behind the parametric representation of embedded submanifolds (representation 3 in [[Def - Submanifold of Euclidean Space]]). Whenever a candidate submanifold is presented as the image of an immersion, the local immersion theorem says it is locally embedded; combined with compactness or properness, it becomes globally embedded.

> [!tip] Knot Theory and Topological Embeddings *(from Topology / Geometry)*
> A smooth knot is a smooth embedding $S^1 \to \mathbb{R}^3$. The local immersion theorem says every smooth knot is locally trivial; the interesting structure is global — linking, crossing number, knot polynomials. Smooth knot theory rests on the foundation that smooth knots exist as embeddings.

> [!tip] The Whitney Immersion Theorem *(from Differential Topology)*
> Every smooth $n$-manifold admits a smooth immersion into $\mathbb{R}^{2n}$ (the Whitney immersion theorem). This is one dimension less than the Whitney embedding theorem requires, and it is the foundation of immersion-vs-embedding gap analyses in differential topology.

> [!tip] Riemannian Submanifold Geometry *(from Riemannian Geometry)*
> Given an immersion $F : M \to (N, g)$ with $N$ Riemannian, $M$ inherits a Riemannian metric $F^* g$ (the **first fundamental form**), and one can develop the second fundamental form, the Gauss equation, and the theory of submanifold curvature — all based on the local-embedding picture provided by the local immersion theorem.
