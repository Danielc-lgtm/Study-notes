---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Smooth Map between Manifolds"
  - "Def - Regular and Critical Points"
  - "Def - Set of Measure Zero on a Manifold"
tags: [geometry, differential-geometry]
---

# Notation

$F : M \to N$ is a smooth map between smooth manifolds, $m = \dim M$, $n = \dim N$. A point $p \in M$ is a **critical point** of $F$ if $dF_p$ fails to be surjective; the **critical set** $C \subseteq M$ is the set of all critical points. A value $c \in N$ is a **critical value** if $c \in F(C)$ — equivalently, if at least one point of $F^{-1}(c)$ is a critical point. The **set of critical values** is $F(C) \subseteq N$. A subset of $N$ has **measure zero** in the sense of [[Def - Set of Measure Zero on a Manifold]]. The full notation registry lives on [[Differential Geometry IV — Submersions, Immersions, Embeddings, and Submanifolds]].

---

# Statement

> **Theorem (Sard's Theorem).** Let $F : M \to N$ be a smooth map between smooth manifolds. The set of critical values of $F$ has measure zero in $N$.

> **Corollary (Almost every value is regular).** The set of regular values of $F$ is dense in $N$ (and has full measure in any chart of $N$).

> **Corollary (Image of a low-dimensional manifold has measure zero).** If $\dim M < \dim N$, then $F(M)$ has measure zero in $N$.

---

# Motivation

This is the technical theorem that makes the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] usable in practice. The regular value theorem says regular level sets are submanifolds, but says nothing about whether regular values *exist*. Sard's theorem fills the gap: critical values are exceptional — they form a measure-zero set — so almost every value is regular, and the regular value theorem applies to almost every level set.

The result is the **density-of-regular-values theorem**. It is what allows differential topology to operate with confidence: when a construction requires picking a regular value (a transversal map, a Morse function, an embedding direction), Sard guarantees one exists. The non-constructive nature of the argument is essential — Sard does not tell you *which* values are regular, but tells you that "regular" is the generic case.

The downstream consequences are sweeping. **Whitney's embedding theorem** (every $n$-manifold embeds in $\mathbb{R}^{2n+1}$) is proved by iteratively projecting an embedding into successively smaller Euclidean spaces, using Sard at each step to find a projection direction that preserves injectivity and immersion. **Morse theory** rests on the genericity of Morse functions, which is a Sard-style argument. **Transversality theorems** (transverse maps form an open dense set) generalise Sard. **Mapping degree** is well-defined as a signed count of preimages of *any* regular value (and Sard guarantees regular values exist). **Cobordism theory** (the Pontryagin–Thom construction) uses regular values of maps to spheres to define cobordism classes.

The theorem is technically nontrivial but conceptually clean: the proof reduces (by chart-by-chart application) to the Euclidean case, and there proceeds by induction on the dimension of the source, with a clever subdivision argument bounding the volume of cubes containing critical points.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$F$ is a smooth map between smooth manifolds". This is essentially as broad as one can make it.

The first disguised source is **a transverse parametrised family**. Given $H:M\times\Lambda\to N$ and a submanifold $S\subseteq N$, assume the joint map $H$ is transverse to $S$. Applying Sard to the projection $H^{-1}(S)\to\Lambda$ shows that for almost every parameter $\lambda$, the slice $H_\lambda$ is transverse to $S$. The transversality hypothesis on the joint map is essential; Sard applied to an arbitrary $H$ does not by itself make its slices regular.

The second disguised source is **a family of conserved quantities in dynamics**. For a smooth first integral $H:M\to\mathbb R$, Sard says almost every energy $E$ is regular; the corresponding energy surface $H^{-1}(E)$ is then a hypersurface by the regular value theorem. Critical energies are precisely where topology or qualitative dynamics can change, so Sard separates the generic energy levels from the exceptional bifurcation levels.

The third disguised source is **height functions on submanifolds**. If $S\subseteq\mathbb R^n$ is a smooth submanifold and $h:S\to\mathbb R$ is a coordinate projection, Sard makes almost every height a regular value, so almost every horizontal slice is a smooth submanifold of dimension $\dim S-1$. Nondegeneracy of the exceptional critical points is a separate jet-transversality condition; it is not a consequence of Sard for one fixed height function.

**Targets (Output Amplification)**

The conclusion is "the critical values of $F$ form a measure-zero set in $N$". Combining with various $D$:

Combine with **the regular value theorem.** Property $D$: $\Phi^{-1}(c)$ is a submanifold whenever $c$ is regular. The amplified result $E$: *almost every* level set of $\Phi$ is a smooth submanifold of $M$ (the regular level sets), so "submanifold structure" is generic in the family of all level sets. This is the bridge that makes the regular value theorem applicable in practice.

Combine with **partial-rank reductions of the Whitney embedding theorem.** Property $D$: $M$ embeds in $\mathbb{R}^N$ for some large $N$. The amplified result $E$: $M$ embeds in $\mathbb{R}^{2n+1}$, by iterative projection — at each step, applying Sard to the directions that fail injectivity or immersion shows the bad set has measure zero, hence good directions are dense, hence a good projection exists. The repeated application converts an embedding in any ambient Euclidean space into an embedding in $\mathbb{R}^{2n+1}$. See [[Thm - Whitney Embedding Theorem]].

Combine with **the existence of Morse functions.** Property $D$: a Morse function exists. The amplified result $E$: in fact Morse functions are open dense in the space of smooth functions, by a Sard-style argument on the second-jet space. This makes Morse theory's hypothesis "pick a Morse function" essentially costless.

Combine with **the well-definedness of mapping degree.** Property $D$: $f : M \to N$ is a smooth map between compact oriented $n$-manifolds. The amplified result $E$: Sard guarantees regular values of $f$ exist; the signed count of preimages at any regular value gives the **mapping degree**, an integer invariant of $f$. The result is independent of the regular value chosen (by an additional argument using the connectedness of the regular-value set), and is a smooth-homotopy invariant.

---

# Why Is It True

The intuition has two parts: **why critical values are "few"** (the measure-theoretic content), and **why this is the right way to count "few"** (the [[Def - Diffeomorphism|diffeomorphism]]-invariance content).

**The bolded one-liner mechanism summary: the critical set is locally controlled by the failure of the differential's rank, and the failure of rank propagates into a sub-Euclidean image — packing arguments at successive orders of vanishing show the image's volume can be made arbitrarily small.**

Why are critical values rare? Two main mechanisms.

**Mechanism 1: dimension reduction.** When $\dim M < \dim N$, *every* point of $M$ is critical (the differential cannot be surjective), but the image $F(M)$ is at most $\dim M$-dimensional inside a $\dim N$-dimensional manifold. A smooth map between Euclidean spaces is locally Lipschitz, and the image of a Lipschitz map from $\mathbb{R}^m$ into $\mathbb{R}^n$ with $m < n$ has measure zero (it's a Lipschitz image of an $m$-dimensional set, hence covered by countably many balls whose volumes shrink in $n$-dimensional measure). So strictly low-dimensional images are automatically negligible. This is the easy case of Sard.

**Mechanism 2: rank-drop on a sub-manifold-of-positive-codimension.** When $\dim M \geq \dim N$, the critical set $C$ is the set of points where the rank of $dF$ is strictly less than $n$. Generically this set has positive codimension in $M$ — it is cut out by the vanishing of $n \times n$ subdeterminants of the Jacobian. So $C$ is at most $(m - 1)$-dimensional, and by mechanism 1 (recursively), $F(C)$ has measure zero. This is the substantive case of Sard, and the proof requires the careful packing argument to bound the image volume of *higher-order* critical points (where multiple derivatives of $F$ vanish, not just the first).

The proof is by induction on $m = \dim M$ (the source dimension). The base case $m = 0$ is trivial (a $0$-manifold is a countable disjoint union of points, and a countable set has measure zero in any positive-dimensional manifold). The inductive step subdivides the critical set $C$ into a nested sequence $C \supseteq C_1 \supseteq C_2 \supseteq \cdots$, where $C_k$ is the set of points where the *first $k$ partial derivatives* of $F$ vanish. The image of $C \setminus C_1$ has measure zero by the simple-rank-drop argument; the image of $C_k \setminus C_{k+1}$ has measure zero by induction on a lower-dimensional source (a level set of a partial derivative); the image of $C_k$ for $k$ sufficiently large has measure zero by a direct packing argument using Taylor's theorem (the image volume in each cube is $O(R^{n(k+1)})$, where $R$ is the cube side, and summing over $K^m$ cubes of side $R/K$ gives total volume $K^{m - n(k+1)} \cdot R^{n(k+1)}$, which vanishes as $K \to \infty$ when $k+1 > m/n$).

Why is "measure zero" the right notion? Because it is **diffeomorphism-invariant**: a smooth map between manifolds of the same dimension sends measure-zero sets to measure-zero sets (locally a Lipschitz map, which preserves Lebesgue measure zero with at most a multiplicative constant). So measure zero is a property of subsets of a manifold that does not depend on a chart. This is what makes the statement "critical values have measure zero in $N$" well-posed without additional structure on $N$ (no metric, no volume form).

The corollary "almost every value is regular" is just "the complement of a measure-zero set is dense". And the corollary "image of low-dimensional source has measure zero" is the case where *every* point of $M$ is critical: when $\dim M < \dim N$, every point fails the rank condition, so the entire image is the critical-value set, which is measure-zero.

---

# What Makes This Hard

The non-obvious step is the **higher-order packing argument** for the deeply-degenerate critical points (the set $C_k$ for $k > m/n - 1$). The first two reductions — $F(C \setminus C_1)$ has measure zero by elementary Lipschitz-image arguments; $F(C_k \setminus C_{k+1})$ has measure zero by induction — are intuitive. But the *innermost* set $C_k$ (where many derivatives vanish) requires a careful covering-by-cubes argument with Taylor's theorem providing the volume bound. The most common error is to skip directly to "measure-zero" without verifying the packing constants are uniform on compact sets, or to apply the elementary argument at all levels and miss the higher-order case. A second pitfall: applying Sard with hypotheses too weak (continuous instead of smooth) — the theorem genuinely requires smoothness (or at least sufficiently high regularity, depending on the [[Def - Dimension|dimensions]]; see Lee's remarks).

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof structure.**

**High-level strategy:**
Reduce to the case $F : U \to \mathbb{R}^n$ on $U \subseteq \mathbb{R}^m$ open by chart-by-chart application; "measure zero" is preserved through this reduction. Induct on $m$. Subdivide the critical set $C$ into a chain $C \supseteq C_1 \supseteq C_2 \supseteq \cdots$ by orders of vanishing. Bound the image of each layer separately: the difference $C \setminus C_1$ via the simple rank-drop argument using Lipschitz estimates; the difference $C_k \setminus C_{k+1}$ by inducting on a hypersurface in $M$; the innermost layer $C_k$ for $k$ large via the cube-packing argument using Taylor's theorem. The union of all these measure-zero sets is measure zero, so $F(C)$ has measure zero.

**Subgoal decomposition:**

1. **Reduce to Euclidean coordinates.** By taking countably many smooth charts covering $M$, reduce to: $F : U \to \mathbb{R}^n$ smooth on $U \subseteq \mathbb{R}^m$ open. The conclusion "image of critical points has measure zero" transports through charts because smooth maps preserve measure zero.
   - *Hint:* Lemma 6.6 in Lee: a measure-zero set checked in one cover of charts is measure-zero in all.

2. **Induct on $m$.** Base case $m = 0$: trivial (the critical set is countable, hence its image is). Inductive step: assume the theorem for sources of dimension $< m$, prove for dimension $m$.
   - *Hint:* The induction parameter is the source dimension, not the codimension.

3. **Define the nested critical sets.** $C \supseteq C_1 \supseteq C_2 \supseteq \cdots$ where $C_k = \{p \in C :$ all derivatives of $F$ up to order $k$ vanish at $p\}$. Each $C_k$ is closed.
   - *Hint:* $C_1$ requires all *first* partial derivatives to vanish (so $dF = 0$); $C_2$ adds vanishing of all second partials; etc.

4. **Bound $F(C \setminus C_1)$.** This is the simple-rank-drop case. At a point $p \in C \setminus C_1$, some first partial of $F$ is nonzero. Use this to define new coordinates near $p$ in which one of the original coordinates becomes $F^1$ (a partial-IFT change). Then apply the inductive hypothesis to slice maps $F_c$ defined on hyperplanes $\{x^1 = c\}$, and use Fubini-style integration to conclude.
   - *Hint:* The slicing reduces to lower-dimensional source.

5. **Bound $F(C_k \setminus C_{k+1})$ for $k \geq 1$.** At such a point, some $k$-th partial of $F$ is nonzero but all lower partials vanish. Let $y =$ that partial; its zero set near $p$ is a smooth hypersurface. The set $C_k$ lies in this hypersurface, so the image of $C_k \setminus C_{k+1}$ near $p$ is bounded by the image of a critical set on a lower-dimensional manifold. Apply the inductive hypothesis.
   - *Hint:* Restrict $F$ to the hypersurface and apply Sard inductively.

6. **Bound $F(C_k)$ for $k > m/n - 1$.** This is the packing argument. Cover the closure of $C_k$ in a compact subset by cubes of side $R/K$. By Taylor's theorem with the constant-on-$C_k$ derivatives, $F$ restricted to a cube intersecting $C_k$ has image contained in a ball of radius $A(R/K)^{k+1}$. Summing over $K^m$ cubes, the total volume is bounded by $K^m \cdot (A(R/K)^{k+1})^n = A^n R^{n(k+1)} K^{m - n(k+1)}$, which goes to $0$ as $K \to \infty$ when $m - n(k+1) < 0$, i.e., $k + 1 > m/n$.
   - *Hint:* Taylor's theorem gives uniform control on $F$'s deviation in cubes near $C_k$.

7. **Conclude.** $F(C)$ is the union of $F(C \setminus C_1)$, $F(C_1 \setminus C_2)$, $\dots$, $F(C_{k_0 - 1} \setminus C_{k_0})$, and $F(C_{k_0})$ for $k_0 > m/n - 1$. Each piece has measure zero, and a finite union of measure-zero sets has measure zero. (Strictly speaking, also need to verify the construction across the countably many charts of $M$ that were chosen in Step 1 — but this is handled by countable union closure.)
   - *Hint:* Countable union of measure-zero sets is measure-zero.

---

# Lemma Decomposition

> [!note]- Lemma 1: Image of measure-zero set under smooth map (same dimension)
> **Statement:** Let $F : U \to V$ be a smooth map between open subsets of $\mathbb{R}^n$ (same dimension), and let $A \subseteq U$ have Lebesgue measure zero. Then $F(A) \subseteq V$ has Lebesgue measure zero.
>
> **Hint:** Cover $A$ by small open balls of total volume $< \delta$; use the Lipschitz bound for $F$ on a compact neighbourhood to bound the image volume.
>
> **Why needed:** It is the diffeomorphism-invariance of "measure zero", essential for transporting Sard's conclusion through charts.
>
> > [!note]- Full proof
> > Cover $A$ by countably many precompact open balls $B_i$ in $U$. For each $B_i$, the closure $\bar B_i$ is compact and contained in $U$, so $\sup_{x \in \bar B_i} |DF(x)| \leq C_i$ for some $C_i < \infty$. By the mean value inequality (Lipschitz estimate for smooth functions), $|F(x) - F(y)| \leq C_i |x - y|$ for $x, y \in \bar B_i$.
> >
> > Given $\delta > 0$, cover $A \cap \bar B_i$ by countably many balls $\{B^{(i,j)}\}_j$ with $\sum_j \mathrm{Vol}(B^{(i,j)}) < \delta / 2^i C_i^n$. Then $F(A \cap \bar B_i)$ is covered by balls $\{B^{(i,j)\prime}\}_j$ of radius at most $C_i$ times the radius of $B^{(i,j)}$, so volume at most $C_i^n$ times. The total volume is bounded by $C_i^n \sum_j \mathrm{Vol}(B^{(i,j)}) < \delta / 2^i$. Summing over $i$: $\sum_i \delta / 2^i = \delta$.
> >
> > Since $\delta$ was arbitrary, $F(A)$ has measure zero.

> [!note]- Lemma 2: A submersion in low dimension has measure-zero image
> **Statement:** Let $F : U \to \mathbb{R}^n$ be smooth on $U \subseteq \mathbb{R}^m$ open, with $m < n$. Then $F(U)$ has measure zero in $\mathbb{R}^n$.
>
> **Hint:** Extend $F$ to a map $\tilde F : U \times \mathbb{R}^{n-m} \to \mathbb{R}^n$ by ignoring the extra coordinates. The image of $U \times \{0\}$ is $F(U)$; since $U \times \{0\}$ has measure zero in $U \times \mathbb{R}^{n-m} \cong \mathbb{R}^n$, and $\tilde F$ is smooth, by Lemma 1 the image has measure zero.
>
> **Why needed:** It handles the easy case of Sard when $\dim M < \dim N$, where every point is automatically critical.
>
> > [!note]- Full proof
> > Define $\tilde F : U \times \mathbb{R}^{n-m} \to \mathbb{R}^n$ by $\tilde F(x, y) = F(x)$, ignoring $y$. This is a smooth map between same-dimensional open subsets ($U \times \mathbb{R}^{n-m}$ has dimension $n$, target $\mathbb{R}^n$). The set $A = U \times \{0\}$ has Lebesgue measure zero in $\mathbb{R}^n$ (it is a hyperplane $\{y = 0\}$ intersected with $U \times \mathbb{R}^{n-m}$, which is contained in a hyperplane, which has measure zero). By Lemma 1, $\tilde F(A) = F(U)$ has measure zero.

---

# Formal Proof

> [!note]- Formal proof, with the Euclidean null-set lemmas isolated
>
> The proof uses two Euclidean analytic inputs at the points where they are named: the Fubini slice lemma in Step 2 and the Taylor flatness estimate proved in Step 4. The differential-topological reductions are written out rather than hidden under the label “proof sketch.”
>
> **Step 0 (reduction to Euclidean).** By covering $M$ and $N$ with countably many smooth charts, reduce to: $F : U \to \mathbb{R}^n$ smooth on $U \subseteq \mathbb{R}^m$ open. By Lemma 1, "measure zero" transports through these charts.
>
> If $n=0$, the differential to the zero-dimensional target is always surjective, so there are no critical points. Hence assume $n\geq1$.
>
> **Step 1 (induction on $m$).** Base case $m = 0$: a second-countable zero-manifold is countable, so its image in $\mathbb R^n$ has measure zero.
>
> **Inductive step.** Assume the theorem for source dimensions $<m$. Let $C$ be the critical set and define
> $$C_k=\{x\in U:D^\alpha F^j(x)=0\text{ for every }j\text{ and every }\alpha\text{ with }1\le |\alpha|\le k\},\qquad k\ge1.$$
> Thus $C_1=\{dF=0\}\subseteq C$. Notice that $C$ is not being identified with a zeroth-order vanishing set.
>
> **Step 2 ($F(C \setminus C_1)$ has measure zero).** At $p \in C \setminus C_1$, some first partial $\partial F^1 / \partial x^1$, say, is nonzero. By the inverse function theorem applied to the carry-along map $(x^1, x^2, \dots, x^m) \mapsto (F^1(x), x^2, \dots, x^m)$, change coordinates so that $F^1(x) = x^1$. Then $F(x^1, \dots, x^m) = (x^1, F^2_{x^1}(x^2, \dots, x^m), \dots, F^n_{x^1}(x^2, \dots, x^m))$, and the critical set of $F$ in the new coordinates restricted to $\{x^1 = c\}$ is exactly the critical set of $F_c = (F^2_c, \dots, F^n_c) : \{x^1 = c\} \to \mathbb{R}^{n-1}$. By the inductive hypothesis (source dim $m - 1$), $F_c(\text{critical set of } F_c)$ has measure zero in $\mathbb{R}^{n-1}$ for each $c$. By Lemma 6.2 of Lee (a Fubini-style lemma), $F(C \setminus C_1) \cap U$ has measure zero in $\mathbb{R}^n$.
>
> **Step 3 ($F(C_k \setminus C_{k+1})$ has measure zero for $k \geq 1$).** For $p\in C_k\setminus C_{k+1}$, choose a component $F^j$ and a multi-index $\alpha$ of length $k$ such that some first derivative of $g=D^\alpha F^j$ is nonzero at $p$. Because $p\in C_k$, $g(p)=0$, while $dg_p\ne0$. After shrinking around $p$, the regular value theorem makes $Y=g^{-1}(0)$ a smooth hypersurface containing $C_k$ locally. Every $q\in C_k\cap Y$ satisfies $dF_q=0$, so $q$ is a critical point of $F|_Y:Y\to\mathbb R^n$. The induction hypothesis gives that $F(C_k\cap Y)$ is null. A countable collection of these neighbourhoods covers $C_k\setminus C_{k+1}$, so its image is null.
>
> **Step 4 ($F(C_k)$ has measure zero for $k > m/n - 1$).** Cover the closure of $C_k$ in a compact set by a cube $E$ of side $R$. Let $A$ bound the $(k+1)$-st derivatives of $F$ on $E$. Subdivide $E$ into $K^m$ subcubes of side $R/K$. By Taylor's theorem, if a subcube $E_i$ contains a point of $C_k$, then for all $x \in E_i$, $|F(x) - F(\text{point of }C_k\text{ in }E_i)| \leq A' (R/K)^{k+1}$ for some $A'$ depending only on $A, k, m$. So $F(E_i \cap C_k)$ is contained in a ball of radius $A'(R/K)^{k+1}$, volume $C \cdot (R/K)^{n(k+1)}$ for some $C$. Summing over $K^m$ subcubes: total volume $\leq C \cdot K^m \cdot (R/K)^{n(k+1)} = C \cdot R^{n(k+1)} \cdot K^{m - n(k+1)}$. For $m - n(k+1) < 0$, this $\to 0$ as $K \to \infty$. So $F(C_k \cap E)$ has measure zero.
>
> **Step 5 (assemble).** For any integer $k_0>m/n-1$,
> $$C=(C\setminus C_1)\cup(C_1\setminus C_2)\cup\cdots\cup(C_{k_0-1}\setminus C_{k_0})\cup C_{k_0}.$$
> Steps 2–4 show that the image of every term is null. This is a finite union, so $F(C)$ has measure zero.
>
> $\qquad\blacksquare$
>
> Corollary 6.11 of Lee follows: if $\dim M < \dim N$, every point is critical, so $F(M)$ has measure zero by Sard (or directly by Lemma 2 above).
>
> Corollary 6.12 of Lee follows: an immersed submanifold of dimension less than the ambient has measure zero (apply Corollary 6.11 to the inclusion).

---

# Cross-Field Exercise Suggestions

**The fundamental theorem of algebra via degree theory.** Consider a polynomial $p(z) \in \mathbb{C}[z]$ of degree $n \geq 1$. It defines a smooth map $p : \mathbb{C} \to \mathbb{C}$, extending to a smooth map $\bar p : \mathbb{CP}^1 \to \mathbb{CP}^1$ between compact $2$-manifolds. By Sard, regular values of $\bar p$ exist; by counting signs at preimages of a regular value, the **mapping degree** of $\bar p$ is computed and shown to be $n$. Since $\deg \bar p \neq 0$, $\bar p$ must be surjective — in particular hits $0$, so $p$ has a root. This is a smooth-category proof of the fundamental theorem of algebra; Sard is essential for the well-definedness of degree.

**Brouwer's fixed-point theorem.** Brouwer's theorem says every continuous map $f : D^n \to D^n$ from the closed disk to itself has a fixed point. The smooth-category proof uses a retraction argument: if there is no fixed point, define a smooth retraction $r : D^n \to S^{n-1}$, and use Sard to find a regular value $y$; the preimage $r^{-1}(y)$ is a $1$-dimensional submanifold of $D^n$ with boundary on $S^{n-1}$, but this contradicts a degree calculation. Sard ensures the regular value $y$ exists.

**The hairy ball theorem.** Every continuous tangent vector field on $S^2$ vanishes at some point. The smooth-category proof shows that a never-vanishing vector field would give a smooth map $S^2 \to S^2$ of degree $1$ that is also homotopic to the antipodal map (degree $-1$), a contradiction. Sard's theorem is used in computing the degree by counting preimages of a regular value.

**Whitney's embedding theorem (the engine).** The proof of the [[Thm - Whitney Embedding Theorem|weak Whitney embedding theorem]] (every $n$-manifold embeds in $\mathbb{R}^{2n+1}$) is a textbook application of Sard. Starting from an embedding in some $\mathbb{R}^N$, the proof projects to $\mathbb{R}^{N-1}$ along a direction $v$, and shows that "bad" directions $v$ (those for which the projection fails to be injective or an immersion) form a set of measure zero, so good directions are dense. Iterating reduces $N$ until $N = 2n + 1$.

---

# Bridges

- **[[Thm - Regular Value Theorem on Manifolds|Regular Value Theorem]]** — the companion. Sard says regular values are dense; the regular value theorem says regular values give submanifolds. Together: almost every level set is a submanifold. This is the genericity statement at the heart of differential topology.

- **[[Thm - Whitney Embedding Theorem|Whitney Embedding Theorem]]** — Sard's most famous consequence. The weak Whitney theorem (embedding into $\mathbb{R}^{2n+1}$) is proved by iterated projection, using Sard at each step to find a projection direction that preserves the embedding properties.

- **[[Def - Set of Measure Zero on a Manifold|Set of Measure Zero on a Manifold]]** — the natural setting. Sard's conclusion lives in the diffeomorphism-invariant world of measure zero on a manifold, which is precisely the structure needed to state the result without reference to a metric or volume form.

- **Morse theory** — the application. A **Morse function** is a smooth $f : M \to \mathbb{R}$ whose critical points are all non-degenerate. The existence of Morse functions is a Sard-type genericity result: in the space of smooth functions, Morse functions are generic. Morse theory then uses the Morse function's critical-point data to reconstruct the topology of $M$.

- **Transversality theorems** — the generalisation. Sard generalises to: in any reasonable space of smooth maps, the maps satisfying a given transversality condition form an open dense set. This is the formal version of "perturb to general position", the workhorse behind intersection theory, the Pontryagin–Thom construction, and Smale's $h$-cobordism.

- **Mapping degree** — the application. For a smooth map $f : M \to N$ between compact oriented $n$-manifolds, $\deg(f)$ is defined as the signed count of preimages of a regular value. Sard ensures regular values exist; the count's independence of the regular value comes from a separate connectedness argument.

---

# Unlocked by This

> [!tip] Whitney Embedding Theorem *(from this topic)*
> [[Thm - Whitney Embedding Theorem|Whitney's embedding theorem]] says every $n$-manifold embeds smoothly in $\mathbb{R}^{2n+1}$. The proof is a Sard-style argument: iterated projection from a large Euclidean space, using Sard at each step to show good projection directions are dense.

> [!tip] Morse Theory *(from Differential Topology)*
> **Morse functions** — smooth functions with only non-degenerate critical points — are generic by a Sard-type argument. **Morse theory** reconstructs the topology of a manifold from the critical-point data of a Morse function: critical points of index $k$ contribute $k$-cells to a CW-decomposition; the number of critical points of each index bounds the Betti numbers; the moduli space of gradient flow lines encodes the differentials.

> [!tip] Mapping Degree and Topological Invariants *(from Algebraic Topology)*
> For a smooth map $f : M \to N$ between compact oriented manifolds of the same dimension, the **mapping degree** $\deg(f)$ is the signed count of preimages of a regular value of $f$. Sard guarantees regular values exist; the degree is independent of the choice of regular value and is a smooth-homotopy invariant. Degree theory yields the Brouwer fixed-point theorem, the hairy ball theorem, the fundamental theorem of algebra, and the Poincaré–Hopf theorem.

> [!tip] Transversality Theorems *(from Differential Topology)*
> The **transversality density theorem**: in the space of smooth maps $M \to N$, the maps transverse to a given submanifold $S \subseteq N$ form an open dense set. This generalises Sard (which is the case $S$ is a point), and it is the foundation of intersection theory, $h$-cobordism, and Smale's classification of simply connected high-dimensional manifolds.

> [!tip] Cobordism Theory *(from Algebraic Topology)*
> Two compact $n$-manifolds are **cobordant** if their disjoint union is the boundary of a compact $(n+1)$-manifold. The **Pontryagin–Thom construction** realises cobordism classes as preimages of regular values of maps from $S^N$ to the Thom space of a universal bundle. Sard's theorem provides the regular values and hence the manifold structure of the cobordism.

> [!tip] Generic Position and Density Arguments *(across geometry)*
> Sard's theorem is the prototype of "generic position" arguments: almost every choice of parameter, projection, or perturbation produces a "good" object. This pattern recurs throughout geometry (in moduli space arguments), topology (in transversality), algebraic geometry (in Bertini-type theorems), and analysis (in $C^k$-density of regular maps).
