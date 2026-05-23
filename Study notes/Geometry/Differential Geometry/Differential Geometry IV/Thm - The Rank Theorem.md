---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Map between Manifolds"
  - "Def - The Differential of a Smooth Map"
  - "Def - Rank of a Smooth Map"
  - "Def - Immersion, Submersion, and Embedding"
  - "Thm - The Inverse Function Theorem"
tags: [geometry, differential-geometry]
---

# Notation

$F : M \to N$ is a smooth map between smooth manifolds, $m = \dim M$, $n = \dim N$. The rank of $F$ at $p$ is $\mathrm{rank}\, dF_p = \dim \mathrm{im}\, dF_p$ ([[Def - Rank of a Smooth Map]]). "$F$ has constant rank $r$ on $U$" means $\mathrm{rank}\, dF_p = r$ for every $p \in U$. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

---

# Statement

> **Theorem (Rank Theorem).** Let $M$ and $N$ be smooth manifolds of [[Def - Dimension|dimensions]] $m$ and $n$ respectively, and let $F : M \to N$ be a smooth map with **constant rank** $r$ on a neighbourhood of a point $p \in M$. Then there exist smooth charts $(U, \varphi)$ for $M$ centred at $p$ and $(V, \psi)$ for $N$ centred at $F(p)$ with $F(U) \subseteq V$, such that the coordinate representation $\hat F = \psi \circ F \circ \varphi^{-1}$ has the linear form
> $$\hat F(x^1, \dots, x^r, x^{r+1}, \dots, x^m) \;=\; (x^1, \dots, x^r, 0, \dots, 0).$$

> **Corollary (Submersion form).** If $F$ is a submersion ($r = n$, requires $m \geq n$), the coordinate representation becomes the projection $\hat F(x^1, \dots, x^n, x^{n+1}, \dots, x^m) = (x^1, \dots, x^n)$.

> **Corollary (Immersion form).** If $F$ is an immersion ($r = m$, requires $m \leq n$), the coordinate representation becomes the inclusion $\hat F(x^1, \dots, x^m) = (x^1, \dots, x^m, 0, \dots, 0)$.

> **Corollary (Global Rank Theorem).** If $F : M \to N$ has *constant rank* $r$ on all of $M$ and is:
> - **surjective**, then $F$ is a smooth submersion ($r = n$);
> - **injective**, then $F$ is a smooth immersion ($r = m$);
> - **bijective**, then $F$ is a diffeomorphism ($r = m = n$).

The constant-rank hypothesis is automatic on the open set of maximal-rank points (by lower semicontinuity of rank).

---

# Motivation

This is the **central theorem of the chapter**. Every other result — the local immersion theorem, the local submersion theorem, the regular value theorem on manifolds, the global rank corollary, the structure of smooth quotient maps — is either a direct specialisation or a quick corollary. The theorem unifies them all by saying: the only local invariant of a constant-rank smooth map is its rank, and any constant-rank map can be put into a unique standard form by smooth changes of coordinates on source and target.

The result solves an obvious-once-stated problem: given a smooth map $F : M \to N$, what does it look like near a point? In general the answer can be complicated, but the rank theorem says it is determined by one integer: the rank of the differential. Two constant-rank maps of the same rank are locally indistinguishable — they differ only by a choice of coordinates. This is a sweeping classification result for the local geometry of smooth maps.

The theorem is the manifold-level generalisation of the canonical-form theorem for linear maps in linear algebra: any linear map of rank $r$ between vector spaces of dimensions $m$ and $n$ has, in suitable bases, the matrix $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$. The rank theorem says the same statement holds for nonlinear smooth maps of constant rank, with "suitable bases" replaced by "suitable coordinates" — and the proof is the [[Thm - The Inverse Function Theorem|inverse function theorem]] used to build those coordinates from the linear ones.

Why is it the "central" theorem? Because constant rank is the right hypothesis for a clean local normal form, and *every* smooth map has constant rank on the open set of maximal-rank points (immersion or submersion points). So the rank theorem applies, in the form of one of its corollaries, to almost every interesting smooth map at most points — and it gives an explicit local description in coordinates. Anything you want to know about a constant-rank map near a point can be read off from the normal form: it is linear, it is a projection-inclusion, its fibres are coordinate slices, its image is a coordinate slice, etc.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$F$ has constant rank $r$ on a neighbourhood of $p$". The skill is in recognizing constant rank in disguise.

The first disguised source is **the maximal-rank open set**. Property $B$: $F$ is an immersion (resp. submersion) at $p$. The bridge: by lower semicontinuity of rank, there is an open neighbourhood $U$ of $p$ on which $\mathrm{rank}\, dF_q \geq m$ (resp. $\geq n$); but $\mathrm{rank}\, dF_q \leq m$ (resp. $\leq n$), so $\mathrm{rank}\, dF$ is constantly $m$ (resp. $n$) on $U$. Hence every immersion is automatically constant-rank on a neighbourhood of any one of its immersion points; the same for submersions. The non-obviousness: a *pointwise* maximal-rank assumption gives constant rank in a *neighbourhood* for free. *Example:* every theorem proved for immersions ([[Thm - Local Immersion Theorem]]) is a special case of the rank theorem with this implicit bridge.

The second disguised source is **a smooth fibration / surjective submersion**. Property $B$: $\pi : M \to N$ is a surjective smooth submersion. The bridge: every submersion has constant rank $n = \dim N$ on all of $M$, so the rank theorem applies. The non-obviousness: even when the global structure of a fibration is complicated, every point looks locally like a coordinate projection. *Example:* The Hopf fibration $h : S^3 \to S^2$ ([[Ex - The Hopf Map is a Submersion]]) is locally a projection, so its fibres (great circles) inherit a local product structure that lifts to the global fibre bundle picture.

The third disguised source is **a constant-rank algebraic structure**. Property $B$: $F$ is the multiplication or inversion map of a Lie group, restricted to a neighbourhood. The bridge: these maps have constant rank because of the group structure — left translations $L_g$ are diffeomorphisms, so $dF_p$ at any point is related to $dF_e$ at the identity by composition with $dL_g$, which is an isomorphism; constant rank then follows from the same rank at every point. The non-obviousness: algebraic structure forces constant rank globally. *Example:* the multiplication $\mu : G \times G \to G$ of a Lie group is a constant-rank surjective submersion.

**Targets (Output Amplification)**

The conclusion is "in suitable coordinates, $F$ has the standard projection-inclusion form".

Combine the conclusion with **the local injectivity / surjectivity question.** Property $D$: you want to know whether $F$ is injective or surjective on some neighbourhood. The amplified result $E$: in the normal-form coordinates, $\hat F$ is injective if and only if $r = m$ (it is the inclusion), and surjective onto the cube-image if and only if $r = n$ (it is the projection). So the rank determines the local injectivity / surjectivity profile completely. This is the content of the global rank theorem's parts (b) and (a) — a constant-rank map is globally an immersion iff $r = m$, globally a submersion iff $r = n$.

Combine the conclusion with **the structure of the fibres.** Property $D$: you want to understand the level set $F^{-1}(F(p))$ near $p$. The amplified result $E$: in normal-form coordinates, the level set $\{\hat F = (0, \dots, 0)\}$ is exactly the coordinate slice $\{x^1 = \dots = x^r = 0\}$ — a flat $(m - r)$-dimensional submanifold. So fibres of a constant-rank map are *automatically* embedded submanifolds of dimension $m - r$. This is the manifold-level version of the [[Thm - The Regular Value Theorem|regular value theorem]] for constant-rank maps: every level set is a submanifold of the predicted dimension.

Combine the conclusion with **smooth descent through the map.** Property $D$: you want to define a smooth map $\tilde F$ on the image of $F$. The amplified result $E$: in normal-form coordinates, a function on $F(M)$ depends on $r$ variables; to define it smoothly on $M$, you compose with $F$ and check that the result is "constant on the fibre directions" (depends only on $x^1, \dots, x^r$). This is the characteristic property of smooth submersions (with $r = n$, surjective): smooth descent through a submersion is equivalent to constancy on fibres. The rank theorem provides the coordinate setup for verifying this descent.

---

# Why Is It True

The intuition is direct and the picture is the same as for the [[Thm - The Implicit Function Theorem|implicit function theorem]]: **in well-chosen coordinates, a constant-rank smooth map *is* its linear approximation.**

Linear maps are easy: any linear $L : \mathbb{R}^m \to \mathbb{R}^n$ of rank $r$ can be put into the form $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^r, 0, \dots, 0)$ by choosing bases on $\mathbb{R}^m$ and $\mathbb{R}^n$ — a fact from elementary linear algebra (every rank-$r$ matrix is row-and-column equivalent to $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$). The bases are: on $\mathbb{R}^m$, choose $r$ vectors whose images span $\mathrm{im}\, L$ and extend by a basis for $\ker L$; on $\mathbb{R}^n$, take the images of those $r$ vectors and extend to a basis. With these bases, $L$ is the projection-inclusion.

The rank theorem says the same thing for smooth maps of constant rank, with the change-of-basis transformations replaced by *smooth changes of coordinates*. The key insight is that "rank is constant" is exactly the condition needed to make the linear-algebra construction work *smoothly across a neighbourhood*. If the rank dropped somewhere, the choice of "$r$ independent columns" would have to change, and the construction would fail.

**The bolded one-liner mechanism summary: the rank theorem is the inverse function theorem applied twice — once to build new coordinates on the source by carrying $r$ image-coordinates back as new source-coordinates, and once on the target by using the source-construction to define a remainder-killing diffeomorphism on the target.**

Unpacking this: the proof has two main moves. First, you arrange that the first $r$ columns of $dF_p$'s matrix are linearly independent (by reordering coordinates), so that the map "first $r$ output coordinates of $F$" has injective differential on a complementary [[Def - Subspace|subspace]]. The inverse function theorem applied to "carry forward the first $r$ image coordinates" produces a diffeomorphism of the source taking $(x, y) \mapsto (F^{1\dots r}(x, y), y)$. After this first change of coordinates, the map $F$ has been rewritten as $(x, y) \mapsto (x, R(x, y))$ for some smooth $R$.

Second, the constant-rank hypothesis kicks in. The Jacobian of the rewritten map is $\begin{pmatrix} I_r & 0 \\ \partial R/\partial x & \partial R/\partial y \end{pmatrix}$, which has rank $r$ everywhere (the rank is unchanged by smooth coordinate changes). For the rank to be exactly $r$, the bottom block $\partial R/\partial y$ *must vanish identically* — otherwise the rank would jump up. So $R$ depends only on $x$, not on $y$: $R(x, y) = S(x)$ for some smooth $S$. The map is now $(x, y) \mapsto (x, S(x))$ — a graph over the first $r$ variables.

Third, a coordinate change on the target eliminates the graph: replace $(v, w) \in V$ by $(v, w - S(v))$, which is a smooth diffeomorphism since $S$ is smooth. In the new target coordinates the map $(x, y) \mapsto (x, S(x))$ becomes $(x, y) \mapsto (x, 0)$ — the standard projection-inclusion.

So the proof is exactly: (i) IFT to swap $r$ source-coords for $r$ output-coords; (ii) constant rank forces the remainder to be independent of the "carried-along" coords; (iii) absorb the resulting graph into a target diffeomorphism.

Why is constant rank essential (not just "rank at least $r$")? Step (ii) above uses the rank-equals-$r$ hypothesis to force $\partial R/\partial y = 0$. If the rank could be larger somewhere, this conclusion would fail. The hypothesis is sharp.

The submersion and immersion specialisations are simpler. For an immersion ($r = m$), the entire $y$-block is empty; the construction collapses to step (i) — exactly the local immersion theorem. For a submersion ($r = n$), the same shrinkage happens on the target side. Both are direct applications of the [[Thm - The Inverse Function Theorem|inverse function theorem]] without needing the constant-rank refinement, because the rank is already at its maximum value.

---

# What Makes This Hard

The non-obvious step is recognising that **constant rank** is the *exact* condition needed for the bottom-right block $\partial R / \partial y$ to vanish identically — the proof is otherwise stuck. Students often conflate "constant rank" with "pointwise maximal rank" and miss the subtlety. The most common error is to attempt the proof for a map with maximal rank only at a single point: the construction goes through at that point (the inverse function theorem applies), but extending to a neighbourhood requires either (a) the rank to be maximal on a neighbourhood (which it is, by lower semicontinuity — this is the immersion / submersion case) or (b) the rank to be exactly $r$ on a neighbourhood (the genuine constant-rank case for intermediate $r$). A second slip: forgetting that the "carried-along" coordinates from step (i) must commute with the target's; one has to track the IFT's output domain carefully through the construction.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
By choosing initial charts, reduce to the case where $F$ is a smooth map from an open subset of $\mathbb{R}^m$ to an open subset of $\mathbb{R}^n$ with constant rank $r$ near the origin and $F(0) = 0$. Permute coordinates so that the upper-left $r \times r$ block of $DF(0)$ is invertible. Apply the inverse function theorem to the "carry-along" map $(x, y) \mapsto (F^{1\dots r}(x, y), y)$ to swap the first $r$ source coordinates for the first $r$ image coordinates. Use the constant-rank hypothesis to force the remainder of $F$ to depend only on the new "image" coordinates. Then use a target coordinate change to eliminate the remaining graph dependence.

**Subgoal decomposition:**

1. **Reduce to Euclidean coordinates.** Choose initial smooth charts $(U_0, \varphi_0)$ at $p$ and $(V_0, \psi_0)$ at $F(p)$. Working with the coordinate representation $\hat F = \psi_0 \circ F \circ \varphi_0^{-1}$, the problem becomes a problem about a smooth map between open subsets of Euclidean space with constant rank.
   - *Hint:* Centre the charts so that $p, F(p)$ map to the origin. Translate as needed.
   - *Why needed:* Local statements on manifolds reduce to Euclidean problems via charts; the rank is invariant under chart changes.

2. **Permute coordinates to expose an invertible $r \times r$ block.** Since $D\hat F(0)$ has rank $r$, it has an invertible $r \times r$ submatrix. Reorder source and target coordinates so this is the upper-left block: writing $\mathbb{R}^m = \mathbb{R}^r_x \times \mathbb{R}^{m-r}_y$ and $\mathbb{R}^n = \mathbb{R}^r_v \times \mathbb{R}^{n-r}_w$, write $\hat F(x, y) = (Q(x, y), R(x, y))$ with $Q$ valued in $\mathbb{R}^r$ and $R$ in $\mathbb{R}^{n-r}$, and arrange that $\partial Q / \partial x|_0$ is invertible.
   - *Hint:* Linear permutation of coordinates is a smooth diffeomorphism — it does not change rank.
   - *Why needed:* It positions us to apply the inverse function theorem to the $r$-component upper block.

3. **Apply the inverse function theorem to the carry-along map.** Define $\varphi(x, y) = (Q(x, y), y)$, a smooth map $\mathbb{R}^m \to \mathbb{R}^m$. Show $D\varphi(0)$ is invertible (it has the block-triangular form $\begin{pmatrix} \partial Q/\partial x|_0 & * \\ 0 & I \end{pmatrix}$), so the [[Thm - The Inverse Function Theorem|inverse function theorem]] gives a smooth local inverse $\varphi^{-1}(\tilde x, \tilde y) = (A(\tilde x, \tilde y), \tilde y)$.
   - *Hint:* The bottom-right block is $I$ because $\varphi$ carries $y$ unchanged.
   - *Why needed:* This provides the new source coordinates in which the first $r$ output coordinates of $\hat F$ are simply the first $r$ new source coordinates.

4. **Compute $\hat F \circ \varphi^{-1}$.** By construction, $\hat F \circ \varphi^{-1}(\tilde x, \tilde y) = (\tilde x, \tilde R(\tilde x, \tilde y))$ for some smooth $\tilde R = R \circ \varphi^{-1}$. So in the new source coordinates $\hat F$ has the form "identity on the first $r$, plus a remainder in the last $n - r$".
   - *Hint:* Apply $\hat F$ to $\varphi^{-1}(\tilde x, \tilde y) = (A(\tilde x, \tilde y), \tilde y)$, and use $Q(A(\tilde x, \tilde y), \tilde y) = \tilde x$ (from $\varphi \circ \varphi^{-1} = \mathrm{Id}$).
   - *Why needed:* It puts $\hat F$ into the partial standard form needed for the next step.

5. **Use constant rank to force the remainder to be independent of $\tilde y$.** The Jacobian of $\hat F \circ \varphi^{-1}$ at $(\tilde x, \tilde y)$ is $\begin{pmatrix} I_r & 0 \\ \partial \tilde R / \partial \tilde x & \partial \tilde R / \partial \tilde y \end{pmatrix}$. Since composing with a diffeomorphism preserves rank, this matrix has rank $r$ everywhere. The first $r$ rows are already linearly independent (the identity block); for the total rank to be exactly $r$, the bottom-right block $\partial \tilde R / \partial \tilde y$ must vanish identically. Hence $\tilde R$ depends only on $\tilde x$: $\tilde R(\tilde x, \tilde y) = S(\tilde x)$ for some smooth $S : \mathbb{R}^r \to \mathbb{R}^{n-r}$.
   - *Hint:* If $\partial \tilde R / \partial \tilde y$ had even one nonzero entry, the rank would jump above $r$.
   - *Why needed:* This is the constant-rank-essential step; it eliminates the $\tilde y$-dependence and produces a graph over $\tilde x$.

6. **Eliminate the graph via a target coordinate change.** Define $\psi(v, w) = (v, w - S(v))$ on the target. This is a smooth diffeomorphism (its inverse is $(v, w) \mapsto (v, w + S(v))$). Compute $\psi \circ \hat F \circ \varphi^{-1}(\tilde x, \tilde y) = \psi(\tilde x, S(\tilde x)) = (\tilde x, 0)$. So in the new source coordinates and new target coordinates, $\hat F$ has the standard projection-inclusion form.
   - *Hint:* The diffeomorphism shifts the $w$-coordinate by $-S(v)$ at each point, absorbing the graph.
   - *Why needed:* It produces the final normal form $(\tilde x, \tilde y) \mapsto (\tilde x, 0)$.

7. **Repackage as manifold charts.** Combine $\varphi$ with the initial chart $\varphi_0$ to get a chart $(U, \varphi) = (\varphi_0^{-1}(U_0'), \varphi \circ \varphi_0)$ on $M$; similarly combine $\psi$ with $\psi_0$. These are smooth charts on $M$ and $N$ centred at $p$ and $F(p)$, in which $F$ has the form $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^r, 0, \dots, 0)$.
   - *Hint:* Composition of smooth charts with smooth [[Def - Diffeomorphism|diffeomorphisms]] is again a smooth chart.
   - *Why needed:* It returns from Euclidean coordinates to genuine manifold charts.

---

# Lemma Decomposition

> [!note]- Lemma 1: A constant-rank smooth map with invertible upper-left block has a partial normal form
> **Statement:** Let $\hat F : U \to \mathbb{R}^n$ be smooth on $U \subseteq \mathbb{R}^m$ open, with $\hat F(0) = 0$ and $\partial Q/\partial x|_0$ invertible (where $\hat F = (Q, R)$ with $Q \in \mathbb{R}^r$, $R \in \mathbb{R}^{n-r}$). Then there is a smooth diffeomorphism $\varphi$ of a neighbourhood of $0$ in $\mathbb{R}^m$ such that $\hat F \circ \varphi^{-1}(\tilde x, \tilde y) = (\tilde x, \tilde R(\tilde x, \tilde y))$ for some smooth $\tilde R$.
>
> **Hint:** Define $\varphi(x, y) = (Q(x, y), y)$ and apply the inverse function theorem.
>
> **Why needed:** It produces "partial normal form" — the first $r$ output coordinates become the first $r$ source coordinates — before the constant-rank hypothesis is invoked.
>
> > [!note]- Full proof
> > Define $\varphi : U \to \mathbb{R}^m$ by $\varphi(x, y) = (Q(x, y), y)$. The Jacobian at $0$ is
> > $$D\varphi(0) = \begin{pmatrix} \partial Q/\partial x|_0 & \partial Q/\partial y|_0 \\ 0 & I_{m-r} \end{pmatrix}.$$
> > This is block-upper-triangular with diagonal blocks $\partial Q/\partial x|_0$ (invertible by hypothesis) and $I_{m-r}$ (the identity); its determinant is $\det(\partial Q/\partial x|_0) \neq 0$, so $D\varphi(0)$ is invertible. By the [[Thm - The Inverse Function Theorem|inverse function theorem]], $\varphi$ has a local smooth inverse on a neighbourhood of $0$, of the form $\varphi^{-1}(\tilde x, \tilde y) = (A(\tilde x, \tilde y), \tilde y)$ — since $\varphi$ preserves the second component, so does $\varphi^{-1}$. Now compute
> > $$\hat F \circ \varphi^{-1}(\tilde x, \tilde y) = \hat F(A(\tilde x, \tilde y), \tilde y) = (Q(A(\tilde x, \tilde y), \tilde y),\, R(A(\tilde x, \tilde y), \tilde y)).$$
> > The first component is $Q(A(\tilde x, \tilde y), \tilde y) = \tilde x$, since $\varphi(A(\tilde x, \tilde y), \tilde y) = (\tilde x, \tilde y)$ unpacked says $Q(A, \tilde y) = \tilde x$. So $\hat F \circ \varphi^{-1}(\tilde x, \tilde y) = (\tilde x, \tilde R(\tilde x, \tilde y))$ with $\tilde R(\tilde x, \tilde y) = R(A(\tilde x, \tilde y), \tilde y)$, which is smooth.

> [!note]- Lemma 2: Constant rank forces the remainder to depend on only $r$ variables
> **Statement:** Suppose $\hat G : V \to \mathbb{R}^n$ is a smooth map on $V \subseteq \mathbb{R}^m = \mathbb{R}^r \times \mathbb{R}^{m-r}$ with the form $\hat G(\tilde x, \tilde y) = (\tilde x, \tilde R(\tilde x, \tilde y))$, and $\hat G$ has constant rank $r$ on $V$. Then $\tilde R$ is independent of $\tilde y$ on a connected open neighbourhood of any point: there is a smooth $S : \mathbb{R}^r \to \mathbb{R}^{n-r}$ such that $\tilde R(\tilde x, \tilde y) = S(\tilde x)$.
>
> **Hint:** Compute the Jacobian of $\hat G$ explicitly and use that the rank equals $r$ to force the bottom-right block to vanish.
>
> **Why needed:** This is *the* constant-rank step; without it, the construction cannot reach the standard form. It is the only place the hypothesis "constant rank $r$" (rather than just "rank exactly $r$ at one point") is used.
>
> > [!note]- Full proof
> > The Jacobian of $\hat G(\tilde x, \tilde y) = (\tilde x, \tilde R(\tilde x, \tilde y))$ is
> > $$D\hat G(\tilde x, \tilde y) = \begin{pmatrix} I_r & 0 \\ \partial \tilde R/\partial \tilde x & \partial \tilde R/\partial \tilde y \end{pmatrix}.$$
> > The top $r$ rows are the identity on $\mathbb{R}^r$, so they are linearly independent. For the total rank to be $r$, no additional row can be linearly independent of these — that is, the last $n - r$ rows must all be in the row span of the first $r$. Examining the column structure: the first $r$ columns of the bottom-right block are $\partial \tilde R/\partial \tilde x$, which can be anything; the last $m - r$ columns of the bottom-right block are $\partial \tilde R/\partial \tilde y$, and the rank-$r$ condition forces *these* to vanish, because in the first $r$ rows the last $m - r$ entries are zero, so the only way for the bottom-right block to not add new rank is for it to be zero on the last $m - r$ columns. Hence $\partial \tilde R/\partial \tilde y \equiv 0$ on the connected neighbourhood. Since the neighbourhood is connected, $\tilde R$ is independent of $\tilde y$, i.e., $\tilde R(\tilde x, \tilde y) = S(\tilde x)$ for some smooth $S$.

> [!note]- Lemma 3: A graph over the first $r$ variables is killed by a target diffeomorphism
> **Statement:** Let $S : \mathbb{R}^r \to \mathbb{R}^{n-r}$ be smooth. The map $\psi : \mathbb{R}^r \times \mathbb{R}^{n-r} \to \mathbb{R}^r \times \mathbb{R}^{n-r}$ defined by $\psi(v, w) = (v, w - S(v))$ is a smooth diffeomorphism with inverse $\psi^{-1}(v, w) = (v, w + S(v))$, and $\psi(\tilde x, S(\tilde x)) = (\tilde x, 0)$ for all $\tilde x$.
>
> **Hint:** Write down the inverse and check that the compositions are the identity. Then evaluate $\psi$ on the graph.
>
> **Why needed:** It executes the final coordinate change on the target, mapping the graph $\{(v, S(v))\}$ onto the standard slice $\{(v, 0)\}$.
>
> > [!note]- Full proof
> > The proposed inverse is $\psi^{-1}(v, w) = (v, w + S(v))$. Check: $\psi(\psi^{-1}(v, w)) = \psi(v, w + S(v)) = (v, (w + S(v)) - S(v)) = (v, w)$, and similarly $\psi^{-1}(\psi(v, w)) = (v, w)$. So $\psi$ is a bijection. Both $\psi$ and $\psi^{-1}$ are smooth (they are smooth combinations of smooth functions), so $\psi$ is a smooth diffeomorphism. Finally, $\psi(\tilde x, S(\tilde x)) = (\tilde x, S(\tilde x) - S(\tilde x)) = (\tilde x, 0)$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F : M \to N$ be smooth with constant rank $r$ on a neighbourhood of $p$, and let $m = \dim M$, $n = \dim N$.
>
> **Step 0 (reduction to coordinates).** Choose smooth charts $(U_0, \varphi_0)$ for $M$ centred at $p$ and $(V_0, \psi_0)$ for $N$ centred at $F(p)$, with $F(U_0) \subseteq V_0$. The coordinate representation $\hat F = \psi_0 \circ F \circ \varphi_0^{-1}$ is a smooth map from an open subset of $\mathbb{R}^m$ to $\mathbb{R}^n$, with $\hat F(0) = 0$ and constant rank $r$ near $0$. Local statements about $F$ are equivalent to local statements about $\hat F$.
>
> **Step 1 (permute coordinates).** Since $D\hat F(0)$ has rank $r$, it has an invertible $r \times r$ submatrix. After permuting source and target coordinates (which is a linear, hence smooth, diffeomorphism on both sides), assume this is the upper-left block. Write $\mathbb{R}^m = \mathbb{R}^r_x \times \mathbb{R}^{m-r}_y$, $\mathbb{R}^n = \mathbb{R}^r_v \times \mathbb{R}^{n-r}_w$, and $\hat F(x, y) = (Q(x, y), R(x, y))$ with $\partial Q/\partial x|_0$ invertible.
>
> **Step 2 (partial normal form).** By Lemma 1, define $\varphi(x, y) = (Q(x, y), y)$; the inverse function theorem gives a smooth local inverse $\varphi^{-1}$ of the form $(\tilde x, \tilde y) \mapsto (A(\tilde x, \tilde y), \tilde y)$. Composing,
> $$\hat F \circ \varphi^{-1}(\tilde x, \tilde y) = (\tilde x, \tilde R(\tilde x, \tilde y))$$
> for $\tilde R(\tilde x, \tilde y) = R(A(\tilde x, \tilde y), \tilde y)$.
>
> **Step 3 (constant rank kills the $\tilde y$-dependence).** By Lemma 2, the constant-rank hypothesis forces $\partial \tilde R / \partial \tilde y \equiv 0$ on a connected neighbourhood of $0$, hence $\tilde R(\tilde x, \tilde y) = S(\tilde x)$ for some smooth $S : \mathbb{R}^r \to \mathbb{R}^{n-r}$.
>
> **Step 4 (target diffeomorphism).** By Lemma 3, the map $\psi(v, w) = (v, w - S(v))$ is a smooth diffeomorphism. Compose:
> $$\psi \circ \hat F \circ \varphi^{-1}(\tilde x, \tilde y) = \psi(\tilde x, S(\tilde x)) = (\tilde x, 0).$$
>
> **Step 5 (return to manifold charts).** Define the new chart on $M$ as $(U, \varphi)$ where $U = \varphi_0^{-1}(\text{image of }\varphi^{-1}\text{ shrunk to fit})$ and the chart map is $\varphi \circ \varphi_0|_U$; similarly the new chart on $N$ is $(V, \psi \circ \psi_0|_V)$ for an appropriate $V$. In these charts $F$ has the coordinate representation $(\tilde x, \tilde y) \mapsto (\tilde x, 0)$, i.e., $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^r, 0, \dots, 0)$. $\qquad\blacksquare$
>
> The submersion case ($r = n$): the $w$-block is empty, the "graph" is automatic, and Step 4 is trivial — the result is the projection $(x^1, \dots, x^n, \dots, x^m) \mapsto (x^1, \dots, x^n)$. The immersion case ($r = m$): the $y$-block is empty, Step 3 is vacuous (there is no $\tilde y$ to kill), and the result is the inclusion $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^m, 0, \dots, 0)$.

---

# Cross-Field Exercise Suggestions

**Linear algebra: a non-square matrix's normal form.** The linear-algebra theorem "any rank-$r$ linear map can be brought to $\begin{pmatrix} I_r & 0 \\ 0 & 0 \end{pmatrix}$ by row and column operations" is the rank theorem in its simplest case. The rank theorem says this is *robust under smooth perturbation*: a constant-rank smooth perturbation of a linear map remains in the same coordinate normal form. The application is to checking when a polynomial system has constant rank in some region — this is the basic check before applying the rank theorem to define a smooth subvariety or quotient.

**Control theory: linearisation of nonlinear control systems.** A control system $\dot x = f(x, u)$ near an equilibrium point can be analysed by linearising in $u$: the rank of $\partial f/\partial u$ determines the controllability dimension. The rank theorem says that when this rank is constant near the equilibrium, the system can be put into a canonical normal form by smooth changes of state and control coordinates — this is the **Brunovsky normal form** for controllable systems and its constant-rank generalisations. The application is out-of-distribution because the "smooth map" is the dynamics, not a geometric map between manifolds.

**Catastrophe theory and singularity theory.** Catastrophe theory classifies the *failures* of constant rank — the singularities of smooth maps near critical points. The rank theorem handles the regular case (constant rank), and the classification of catastrophes (fold, cusp, swallowtail, butterfly, ...) handles the next-order corrections when rank drops. The application is to classifying the local behaviour of smooth maps *near* points where rank drops; the rank theorem says that away from such points, the behaviour is trivial.

**Algebraic geometry: smoothness of varieties.** A polynomial map $F : \mathbb{R}^m \to \mathbb{R}^n$ defining a variety $V = F^{-1}(0)$ has $V$ a smooth submanifold near a point $p$ iff $F$ has constant rank $n$ at $p$ — this is the polynomial version of the regular value theorem, and it follows from the rank theorem applied to $F$. The application is in classifying singular points of varieties as exactly the points where the rank theorem fails.

---

# Bridges

- **[[Thm - The Inverse Function Theorem|Inverse Function Theorem]]** — the engine. The rank theorem's proof is the inverse function theorem applied to the carry-along map. Conversely, the rank theorem implies the inverse function theorem in the case $r = m = n$: a map of constant rank $m = n$ is locally a diffeomorphism by the normal form. The two theorems are not just related but mutually equivalent through the rank theorem's specialisations.

- **[[Thm - The Implicit Function Theorem|Implicit Function Theorem]]** — a corollary. The rank theorem specialised to a submersion gives the [[Thm - Local Submersion Theorem|local submersion theorem]], which is the implicit function theorem on manifolds. Conversely, the rank theorem can be proved by carefully iterating the implicit function theorem (carry forward image coordinates one at a time, then apply IFT).

- **[[Thm - Local Immersion Theorem|Local Immersion Theorem]]** — the immersion specialisation. When $r = m$ (the immersion case), the rank theorem reduces to the local immersion theorem: every immersion is locally the standard inclusion $(x^1, \dots, x^m) \mapsto (x^1, \dots, x^m, 0, \dots, 0)$. The "constant rank" condition is automatic from "immersion at a single point" by lower semicontinuity, so this specialisation does not need the strong constant-rank hypothesis explicitly.

- **[[Thm - Local Submersion Theorem|Local Submersion Theorem]]** — the submersion specialisation. When $r = n$, the rank theorem reduces to the local submersion theorem: every submersion is locally the standard projection. Same automatic-from-pointwise-condition observation.

- **[[Thm - Regular Value Theorem on Manifolds|Regular Value Theorem]]** — a downstream consequence. Apply the rank theorem (submersion form) at every point of a regular level set; the level set is locally a coordinate slice in each chart, hence an embedded submanifold. The rank theorem provides the coordinate setup; the level set theorem assembles the local pieces.

- **Global rank theorem** — the global form. A constant-rank smooth map is locally a projection-inclusion at every point, so global behaviour (injectivity, surjectivity, bijection) forces global rank to equal $m$, $n$, or both. This is the content of the global rank theorem corollary above.

---

# Unlocked by This

> [!tip] The Smooth Quotient Manifold Theorem *(from Lie Theory)*
> A surjective smooth submersion $\pi : M \to N$ behaves like a smooth quotient map: $F : N \to P$ is smooth iff $F \circ \pi : M \to P$ is. The rank theorem (submersion form) provides the local sections needed for this descent. When $\pi$ comes from a Lie group action, this becomes the **smooth quotient manifold theorem**: the orbit space of a free, proper action of a Lie group is a smooth manifold with the projection as a submersion. This is the source of homogeneous spaces $G/H$ as manifolds.

> [!tip] Fibre Bundles *(from Algebraic Topology)*
> A surjective submersion with locally trivial fibres is a **fibre bundle**. The rank theorem ensures every submersion is locally a projection (the trivial bundle); a global submersion is a bundle iff the local trivialisations can be patched together consistently. This is how the Hopf fibration, vector bundles, principal bundles, and gauge theory are organised.

> [!tip] The Constant Rank Form of the Regular Value Theorem *(from this topic)*
> Generalising the regular value theorem to *constant-rank* maps (not just submersions): if $F : M \to N$ has constant rank $r$ in a neighbourhood of $F^{-1}(c)$, then $F^{-1}(c)$ is an embedded submanifold of $M$ of codimension $r$. This follows from the rank theorem applied at each point of the level set.

> [!tip] Foliations *(from Differential Geometry / Topology)*
> A constant-rank smooth map $F : M \to N$ partitions $M$ into the level sets $F^{-1}(c)$, all of which are submanifolds of the same dimension. This is the simplest example of a **foliation** — a decomposition of $M$ into submanifolds locally diffeomorphic to a stack of parallel slices. General foliations are governed by the Frobenius theorem ([[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X]]).
