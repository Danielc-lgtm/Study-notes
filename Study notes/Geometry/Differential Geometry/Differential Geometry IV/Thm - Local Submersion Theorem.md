---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Map between Manifolds"
  - "Def - The Differential of a Smooth Map"
  - "Def - Immersion, Submersion, and Embedding"
  - "Thm - The Rank Theorem"
  - "Thm - The Implicit Function Theorem"
tags: [geometry, differential-geometry]
---

# Notation

$F : M \to N$ is a smooth map between smooth manifolds with $\dim M = m \geq n = \dim N$. A **local section** of $F$ at $q \in N$ is a smooth map $\sigma : V \to M$ defined on a neighbourhood $V$ of $q$ in $N$, satisfying $F \circ \sigma = \mathrm{id}_V$. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

---

# Statement

> **Theorem (Local Submersion Theorem).** Let $F : M \to N$ be a smooth map. The following are equivalent at a point $p \in M$:
> 1. $F$ is a submersion at $p$ — that is, $dF_p$ is surjective ($\mathrm{rank}\, dF_p = n$);
> 2. There exist smooth charts $(U, \varphi)$ for $M$ centred at $p$ and $(V, \psi)$ for $N$ centred at $F(p)$ with $F(U) \subseteq V$, such that the coordinate representation has the form
> $$\psi \circ F \circ \varphi^{-1}(x^1, \dots, x^n, x^{n+1}, \dots, x^m) = (x^1, \dots, x^n).$$

> **Corollary (Local Section Theorem).** $F$ is a submersion at $p$ if and only if there exists an open neighbourhood $V$ of $F(p)$ in $N$ and a smooth local section $\sigma : V \to M$ with $\sigma(F(p)) = p$.

---

# Motivation

This theorem is the **submersion specialisation of [[Thm - The Rank Theorem|the rank theorem]]**, and it is the manifold-level upgrade of the [[Thm - The Implicit Function Theorem|implicit function theorem]]. It says that any smooth submersion at a point looks, in suitable local coordinates, like the standard projection of $\mathbb{R}^m$ onto its first $n$ coordinates. The rank theorem's "constant rank in a neighbourhood" hypothesis is automatic because the maximal surjective rank is preserved on an open neighbourhood ([[Def - Rank of a Smooth Map]]).

The local section corollary is the *operational* content of the theorem. It says submersions admit smooth right-inverses locally — through every point of the source, there is a smooth section of the submersion in a neighbourhood of the image point. This is the property that makes submersions behave like "quotient maps" in the smooth category: smooth functions on the base lift smoothly to the source via the section, and conversely, smooth functions on the source that are constant on fibres push forward smoothly to the base.

The local section property is the single most important consequence of "submersion" in differential geometry. It is what gives the [[Thm - Submersions are Open Maps|open map theorem for submersions]] (the image of a neighbourhood contains the image of the local section's domain, an open set). It is what makes the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] work (regular level sets are slice-described in coordinates). And it is the foundation of the smooth quotient theorem and the structure of fibre bundles.

The relationship to the [[Thm - The Implicit Function Theorem|implicit function theorem]] is exact: the implicit function theorem says, in Euclidean coordinates, that an equation $f(x, y) = 0$ can be solved for $y$ as $y = g(x)$ when the partial Jacobian $\partial f/\partial y$ is invertible. The local submersion theorem on manifolds is the same statement in chart-independent form: the fibre $F^{-1}(q)$ is locally a graph over the "vertical" coordinates, and the "graph" is exactly the local section.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$dF_p$ is surjective". Recognising this in disguise:

The first disguised source is **a smooth surjection between manifolds of equal dimension that is also a local diffeomorphism**. Property $B$: $F$ is a local diffeomorphism. The bridge: a local diffeomorphism has $dF_p$ a linear isomorphism, in particular surjective — so every local diffeomorphism is a submersion. *Example:* covering maps. The $1$-dimensional covering $\mathbb{R} \to S^1$, $t \mapsto e^{2\pi i t}$, is a submersion (and local diffeomorphism), so it admits local sections — namely, local logarithms.

The second disguised source is **a projection of a product manifold**. Property $B$: $F = \pi_N : M = N \times P \to N$ is the projection onto the first factor. The bridge: the differential of a projection is the projection on tangent spaces, which is patently surjective. *Example:* the projection $TM \to M$ from the tangent bundle is a submersion; local trivialisations $TM|_U \cong U \times \mathbb{R}^n$ make this explicit.

The third disguised source is **a smooth fibration / vector bundle projection**. Property $B$: $\pi : E \to B$ is the projection of a smooth fibre bundle. The bridge: bundle projections are submersions by definition (they have local trivialisations $\pi^{-1}(U) \cong U \times F$, in which the projection is the first-coordinate map and hence a submersion). *Example:* the tangent bundle $TM \to M$, the cotangent bundle $T^*M \to M$, any vector bundle projection.

The fourth disguised source is **a quotient by a free, proper Lie group action**. Property $B$: $\pi : M \to M/G$ is the quotient by a smooth, free, proper action of a Lie group. The bridge: by the smooth quotient theorem, $\pi$ is a smooth submersion (this is one of its defining properties). *Example:* the quotient map $\mathrm{O}(n+1) \to S^n = \mathrm{O}(n+1)/\mathrm{O}(n)$ exhibiting the sphere as a homogeneous space.

**Targets (Output Amplification)**

The conclusion is "in suitable coordinates, $F$ is the standard projection $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^n)$", and equivalently "smooth local sections exist".

Combine the conclusion with **a smooth function on the target whose pullback is wanted.** Property $D$: you have $f \in C^\infty(N)$ and want to lift to a smooth function on $M$. The amplified result $E$: composing with $F$ gives $F^* f = f \circ F \in C^\infty(M)$, a smooth function on $M$ that is *constant on the fibres of $F$* (since $F$-equivalent points have the same image, hence the same $f$-value). Combined with the *Characteristic property of submersions*: $g : M \to P$ is smooth iff it descends through $F$, *iff* $g$ is constant on the fibres of $F$. So submersions characterise their fibre-wise-constant lifts. This is the foundation of the smooth quotient theorem.

Combine the conclusion with **a curve in the target.** Property $D$: $\gamma : J \to N$ is a smooth curve passing through $F(p) = q$. The amplified result $E$: the curve lifts smoothly to $M$ via the local section — define $\tilde\gamma = \sigma \circ \gamma$ on a sub-interval where $\gamma$ lies in the section's domain. This lifted curve is the smooth lift of $\gamma$ through $p$. The application is to lifting paths and homotopies through fibrations — the foundation of the long exact sequence of homotopy groups for a fibration.

Combine the conclusion with **the fibres of $F$.** Property $D$: you ask about the structure of $F^{-1}(q)$ near $p$. The amplified result $E$: in the normal-form coordinates, $F^{-1}(q)$ is the coordinate slice $\{x^1 = \dots = x^n = 0\}$ — a flat $(m - n)$-dimensional smooth submanifold of $U \subseteq M$. So the fibres of any submersion are *automatically* embedded submanifolds of $M$ of dimension $\dim M - \dim N$. This is the level set side of the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] applied at every value.

---

# Why Is It True

The intuition is the rank theorem's intuition in the surjection case, and the proof is a direct application of the [[Thm - The Implicit Function Theorem|implicit function theorem]] via the auxiliary square map trick.

**The bolded one-liner mechanism summary: a submersion's differential is surjective, so it has an $n$-dimensional right-inverse [[Def - Subspace|subspace]] in the source; carrying that subspace's coordinates forward as new source coordinates makes $F$ literally a coordinate projection.**

Here is the construction. In local coordinates around $p$ and $F(p)$, $F$ is represented by a smooth map $\hat F : U \to \mathbb{R}^n$ with $\hat F(0) = 0$ and $D\hat F(0)$ surjective. By permuting source coordinates, assume the *first* $n$ columns of $D\hat F(0)$ are linearly independent — write the source as $\mathbb{R}^n_x \times \mathbb{R}^{m-n}_y$, and the columns of $D\hat F(0)$ in the $x$-block are linearly independent. So the partial Jacobian $\partial \hat F / \partial x|_0$ is an invertible $n \times n$ matrix.

Now build the source coordinate change. Define $\varphi : U \to \mathbb{R}^n \times \mathbb{R}^{m-n}$ by
$$\varphi(x, y) = (\hat F(x, y), y) = (\hat F^1(x, y), \dots, \hat F^n(x, y), y^1, \dots, y^{m-n}).$$
This is a smooth map between open subsets of $\mathbb{R}^m$, with $\varphi(0, 0) = (0, 0)$. Its Jacobian at $(0,0)$ is
$$D\varphi(0, 0) = \begin{pmatrix} \partial \hat F/\partial x|_0 & \partial \hat F/\partial y|_0 \\ 0 & I_{m-n} \end{pmatrix},$$
which is block-upper-triangular with diagonal blocks invertible ($\partial \hat F/\partial x|_0$ by hypothesis, $I_{m-n}$ trivially). Hence $D\varphi(0,0)$ is invertible.

By the [[Thm - The Inverse Function Theorem|inverse function theorem]], $\varphi$ is a local [[Def - Diffeomorphism|diffeomorphism]] near $(0,0)$. So $\varphi$ provides a new system of source coordinates, in which the *first $n$ source coordinates are the components of $\hat F$* and the *last $m - n$ source coordinates are the original $y$ coordinates carried unchanged*.

In these new source coordinates, $\hat F$ becomes the standard projection. Indeed, $(\tilde x,\tilde y)=\varphi(x,y)=(\hat F(x,y),y)$ implies directly that
$$\hat F \circ \varphi^{-1}(\tilde x, \tilde y) = \tilde x = (\tilde x^1, \dots, \tilde x^n)$$
— the standard projection. The target chart can remain unchanged.

The normal form gives a coordinate section $\widehat\sigma(\tilde x)=\varphi^{-1}(\tilde x,0)$. Returning through the original charts yields $\sigma=\varphi_0^{-1}\circ\widehat\sigma\circ\psi_0$ on a neighbourhood of $F(p)$. The coordinate identity $\hat F\circ\widehat\sigma=\mathrm{id}$ implies $F\circ\sigma=\mathrm{id}$, and $\sigma(F(p))=p$.

Why does surjectivity of $dF_p$ correspond to invertibility of $\varphi$'s Jacobian? Surjectivity means the columns of $D\hat F(0)$ span $\mathbb{R}^n$ — equivalently, after permutation, the first $n$ columns are linearly independent, equivalently $\partial \hat F/\partial x|_0$ is invertible. The carry-along construction adds the identity $I_{m-n}$ in the bottom-right of $\varphi$'s Jacobian, giving the block-triangular structure with invertible blocks. So surjectivity of the differential is exactly what makes the carry-along construction work — and the construction's invertibility produces the new source coordinates.

---

# What Makes This Hard

The non-obvious step is the **carry-along source coordinate construction** — defining $\varphi(x, y) = (\hat F(x, y), y)$ and recognising that this is the natural way to convert "$\hat F$ is a submersion" into "$\hat F$ is a coordinate projection". Students often expect a *target* coordinate change (parallel to the immersion theorem), but for submersions the natural construction is on the *source* side: carry the source coordinates whose differential block is invertible (the first $n$) forward by replacing them with $\hat F$ itself, and carry the rest along unchanged. The most common error is permuting both source and target when only source-side permutation is needed; the second is forgetting to check that $D\varphi(0)$ is invertible (which is automatic from surjectivity of $D\hat F(0)$ via the block-triangular structure).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Reduce to Euclidean coordinates. Permute source coordinates so the first $n$ columns of the Jacobian are linearly independent. Build a source coordinate change by carrying the first $n$ output values of $\hat F$ forward as new source coordinates and the remaining $m - n$ source coordinates unchanged. The inverse function theorem makes this a local diffeomorphism. In the new source coordinates, $\hat F$ is the standard projection onto the first $n$ coordinates. The local section is read off by setting the last $m - n$ coordinates to $0$.

**Subgoal decomposition:**

1. **Reduce to Euclidean coordinates.** Choose initial smooth charts centred at $p$ and $F(p)$. Work with the coordinate representation $\hat F : U \to \mathbb{R}^n$, $\hat F(0) = 0$, $D\hat F(0)$ surjective.
   - *Hint:* Center the charts; surjectivity is invariant under chart changes.
   - *Why needed:* Reduces to a Euclidean problem.

2. **Permute source coordinates to expose an invertible $n \times n$ block.** Since $D\hat F(0)$ has rank $n$, it has $n$ linearly independent columns. After permuting source coordinates, assume these are the first $n$ columns: write $\mathbb{R}^m = \mathbb{R}^n_x \times \mathbb{R}^{m-n}_y$ with $\partial\hat F/\partial x|_0$ invertible.
   - *Hint:* Permuting source coordinates is a linear diffeomorphism on the source.
   - *Why needed:* Positions for the carry-along construction.

3. **Build the source coordinate change.** Define $\varphi(x, y) = (\hat F(x, y), y)$ from $U$ to $\mathbb{R}^n \times \mathbb{R}^{m-n}$. Compute the Jacobian:
   $$D\varphi(0, 0) = \begin{pmatrix} \partial\hat F/\partial x|_0 & \partial\hat F/\partial y|_0 \\ 0 & I_{m-n} \end{pmatrix}.$$
   - *Hint:* The bottom-right block is $I_{m-n}$ because $y$ is carried unchanged.
   - *Why needed:* Provides the new source coordinates.

4. **Verify $D\varphi(0,0)$ is invertible.** Block-triangular with invertible diagonal blocks; determinant is the product of diagonal [[Def - Determinant|determinants]].
   - *Hint:* Use the block-triangular determinant formula.
   - *Why needed:* Activates the inverse function theorem.

5. **Apply the inverse function theorem.** The [[Thm - The Inverse Function Theorem|inverse function theorem]] gives a smooth local inverse $\varphi^{-1}$ near $(0,0)$.
   - *Hint:* $\varphi(0,0) = (0,0)$, so the IFT inverse exists near the origin.
   - *Why needed:* Provides the new source chart.

6. **Verify $\hat F \circ \varphi^{-1}$ is the standard projection.** By construction, $\hat F \circ \varphi^{-1}(\tilde x, \tilde y) = \tilde x$ — the first $n$ output coordinates of $\hat F$ have been "carried forward" as the new first $n$ source coordinates.
   - *Hint:* Substitute the explicit form of $\varphi^{-1}$ into the definition.
   - *Why needed:* Yields the normal form.

7. **Construct the local section.** Define $\sigma(\tilde x) = \varphi^{-1}(\tilde x, 0)$ on a neighbourhood of $0$. Then $\hat F(\sigma(\tilde x)) = \hat F(\varphi^{-1}(\tilde x, 0)) = \tilde x$, so $\sigma$ is a smooth local section of $\hat F$.
   - *Hint:* The local section is the "$\tilde y = 0$" slice in the new source coordinates.
   - *Why needed:* Proves the local section corollary.

---

# Lemma Decomposition

> [!note]- Lemma 1: The carry-along source map of a submersion is locally a diffeomorphism
> **Statement:** Let $\hat F : U \to \mathbb{R}^n$ be smooth on $U \subseteq \mathbb{R}^m$ open, with $\hat F(0) = 0$ and $\partial\hat F/\partial x|_0$ invertible (where $U \subseteq \mathbb{R}^n_x \times \mathbb{R}^{m-n}_y$). Then the map $\varphi(x, y) = (\hat F(x, y), y)$ is a smooth local diffeomorphism near $(0, 0)$.
>
> **Hint:** Compute $D\varphi(0,0)$ and verify the block-triangular structure has invertible determinant.
>
> **Why needed:** It is the new source chart producing the normal form.
>
> > [!note]- Full proof
> > The Jacobian is
> > $$D\varphi(0, 0) = \begin{pmatrix} \partial\hat F/\partial x|_0 & \partial\hat F/\partial y|_0 \\ 0 & I_{m-n} \end{pmatrix},$$
> > with the top-right block $\partial\hat F/\partial y|_0$ unimportant and the bottom-right block $I_{m-n}$ because $\varphi(x, y)$'s last $m - n$ coordinates are just $y$. This is block-upper-triangular with diagonal blocks $\partial\hat F/\partial x|_0$ (invertible by hypothesis) and $I_{m-n}$. The determinant of a block-triangular matrix is the product of diagonal-block determinants, so $\det D\varphi(0,0) = \det(\partial\hat F/\partial x|_0) \neq 0$. By the [[Thm - The Inverse Function Theorem|inverse function theorem]], $\varphi$ is a local diffeomorphism near $(0,0)$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F : M \to N$ be smooth with $dF_p$ surjective. We show the existence of charts producing the standard projection form, and the existence of a smooth local section.
>
> **Step 0 (reduction).** Choose smooth charts $(U_0, \varphi_0)$ for $M$ centred at $p$ and $(V_0, \psi_0)$ for $N$ centred at $F(p)$ with $F(U_0) \subseteq V_0$. Work with $\hat F = \psi_0 \circ F \circ \varphi_0^{-1}$, smooth from a neighbourhood of $0$ in $\mathbb{R}^m$ to $\mathbb{R}^n$, $\hat F(0) = 0$, $D\hat F(0)$ surjective.
>
> **Step 1 (permute source).** $D\hat F(0)$ has rank $n$, so it has $n$ linearly independent columns. After permuting source coordinates, assume these are the first $n$: write source as $\mathbb{R}^n_x \times \mathbb{R}^{m-n}_y$, $\partial\hat F/\partial x|_0$ invertible.
>
> **Step 2 (carry-along construction).** On the open coordinate domain $\Omega=\varphi_0(U_0)$ define $H(x,y)=(\hat F(x,y),y)$. Lemma 1 shows that $DH_{(0,0)}$ is invertible. Hence the inverse function theorem gives open neighbourhoods $A\subseteq\Omega$ and $B\subseteq\mathbb R^m$ of the origin such that $H|_A:A\to B$ is a diffeomorphism. Write $K:B\to A$ for its smooth inverse.
>
> **Step 3 (verify normal form).** For $(\tilde x,\tilde y)\in B$, the identity $H(K(\tilde x,\tilde y))=(\tilde x,\tilde y)$ reads
> $$(\hat F(K(\tilde x,\tilde y)),K(\tilde x,\tilde y)_2)=(\tilde x,\tilde y),$$
> so equating the first $n$ components gives
> $$\hat F\circ K(\tilde x,\tilde y)=\tilde x.$$
>
> **Step 4 (manifold charts).** Let $U=\varphi_0^{-1}(A)$ and use the source chart $\widetilde\varphi=H\circ\varphi_0:U\to B$. After shrinking $U$ so that $F(U)\subseteq V_0$, keep the target chart $\psi_0$. Its coordinate representative is $\hat F\circ K$, which Step 3 identifies with the standard projection.
>
> **Step 5 (local section).** Because $B$ is open and contains $(0,0)$, choose a neighbourhood $W$ of $0\in\mathbb R^n$ with $W\times\{0\}\subseteq B$. Define $\hat\sigma(\tilde x)=K(\tilde x,0)$. Then $\hat F(\hat\sigma(\tilde x))=\tilde x$ by Step 3. On the target neighbourhood $\psi_0^{-1}(W)$, the map $\sigma=\varphi_0^{-1}\circ\hat\sigma\circ\psi_0$ is smooth, satisfies $F\circ\sigma=\mathrm{id}$, and sends $F(p)$ to $p$.
>
> $\qquad\blacksquare$
>
> Conversely, the differential of the coordinate projection is surjective, and conjugating it by the two chart differentials preserves surjectivity. If a local section through $p$ exists, differentiating $F\circ\sigma=\mathrm{id}$ at $F(p)$ gives $dF_p\circ d\sigma_{F(p)}=\mathrm{id}_{T_{F(p)}N}$, so $dF_p$ is surjective; Step 5 proves the reverse implication.

---

# Cross-Field Exercise Suggestions

**Fibre bundles in physics.** A principal-bundle projection $P\to M$ is a smooth surjective submersion, so this theorem supplies local sections through chosen points. The principal action then upgrades a section $s:U\to P$ to the equivariant trivialization $(x,g)\mapsto s(x)g$ of $P|_U$. The submersion theorem alone gives ordinary product coordinates with a Euclidean fibre; the group-compatible trivialization uses the principal action as additional structure.

**The smooth quotient theorem.** A free, proper smooth action of a Lie [[Def - Group|group]] $G$ on $M$ produces a smooth manifold structure on the orbit space $M/G$ such that the projection $M \to M/G$ is a smooth submersion. This is the manifold-level version of the topological quotient construction, and the local submersion theorem is the technical foundation: locally, the quotient map is a coordinate projection.

**Implicit function theorem applications in PDEs.** A nonlinear PDE $F(u, \lambda) = 0$ on a Banach space, depending on a parameter $\lambda$, has solutions $u(\lambda)$ that depend smoothly on $\lambda$ whenever the linearised operator $F_u$ is invertible (in the appropriate Banach-space sense). This is the implicit function theorem in infinite [[Def - Dimension|dimensions]], and at the level of finite-dimensional approximations it is the local submersion theorem applied to the map $F : E \times \Lambda \to E$.

**Path lifting in covering spaces.** A smooth covering map $\pi:\widetilde M\to M$ is a local diffeomorphism and hence a submersion. Its path-lifting property is stronger than the local-section conclusion here: evenly covered neighbourhoods provide disjoint inverse branches, and the chosen initial point selects a unique branch on successive subintervals. Arbitrary local sections of a general submersion need not paste uniquely and do not imply path lifting.

---

# Bridges

- **[[Thm - The Rank Theorem|Rank Theorem]]** — the parent. The local submersion theorem is the rank theorem specialised to maximal surjective rank ($r = n$). The general rank theorem reduces to this when the rank is $n$.

- **[[Thm - The Implicit Function Theorem|Implicit Function Theorem]]** — the engine and the analogue. The proof's main step is the carry-along source construction $\varphi(x, y) = (\hat F(x, y), y)$, exactly the auxiliary square map of the implicit function theorem. The two theorems are duals: the implicit function theorem solves $\hat F(x, y) = 0$ for $y$ as a function of $x$ (the fibre is a graph over $x$); the local submersion theorem writes $\hat F$ as the projection onto $\tilde x$ in the new coordinates. The relationship is exact.

- **[[Thm - The Inverse Function Theorem|Inverse Function Theorem]]** — the workhorse. The proof's only nontrivial step is applying the IFT to the carry-along map. The two theorems are mutually equivalent: IFT implies local submersion theorem (above proof); the local submersion theorem with $m = n$ reduces to a local diffeomorphism statement, equivalent to IFT.

- **[[Thm - Local Immersion Theorem|Local Immersion Theorem]]** — the rank-theoretic dual. Immersions and submersions are the two extreme rank specialisations of the rank theorem.

- **[[Thm - Submersions are Open Maps|Submersions are Open Maps]]** — the direct consequence. A submersion's local section theorem says the image of any neighbourhood contains the image of a section's domain, an open set; so the image of any open set is open.

- **[[Thm - Regular Value Theorem on Manifolds|Regular Value Theorem]]** — the level-set consequence. Applying the local submersion theorem at every point of a level set produces a slice chart of $M$ in which the level set is a flat coordinate slice, hence (by [[Def - Embedded Submanifold]]) an embedded submanifold. The regular value theorem assembles these slice charts into the global submanifold structure.

- **[[Ex - The Hopf Map is a Submersion]]** — a concrete example. The Hopf map $S^3 \to S^2$ is a submersion, so it admits local sections (great-circle local sections of the Hopf fibration), and the local-submersion-theorem normal form holds.

---

# Unlocked by This

> [!tip] Characteristic Property of Submersions *(from this topic)*
> A surjective smooth submersion $\pi : M \to N$ has the universal property: for any smooth manifold $P$, a map $F : N \to P$ is smooth if and only if $F \circ \pi$ is smooth. This makes submersions the smooth-category analogue of topological quotient maps. The local section theorem is what proves the "if" direction.

> [!tip] Smooth Fibre Bundles *(from Algebraic Topology / Geometry)*
> A **fibre bundle** is a surjective submersion with locally trivial fibres: $\pi : E \to B$ such that around each point of $B$ there is a neighbourhood $U$ with $\pi^{-1}(U) \cong U \times F$, the local trivialisation. The local submersion theorem is the *local* part of this — every submersion looks locally like a projection. The global structure (transition functions, structure group) is the additional bundle data.

> [!tip] Smooth Quotient Manifold Theorem *(from Lie Theory)*
> The **smooth quotient theorem**: a free, proper smooth action of a Lie group $G$ on a manifold $M$ produces a smooth manifold structure on $M/G$ such that the projection $\pi : M \to M/G$ is a smooth submersion. The local submersion theorem is used in the construction of the charts of $M/G$ from the local-section structure of $\pi$.

> [!tip] Connections on Principal Bundles *(from Gauge Theory)*
> A **connection** on a principal bundle $P \to M$ is a smooth choice, at each point of $P$, of a "horizontal" complement to the vertical (fibre tangent) subspace — equivalently, a smooth retraction of $TP$ onto the vertical bundle. The local submersion theorem ensures the vertical bundle is a well-defined sub-bundle (it is the kernel of the projection's differential), making the choice of horizontal complement meaningful.
