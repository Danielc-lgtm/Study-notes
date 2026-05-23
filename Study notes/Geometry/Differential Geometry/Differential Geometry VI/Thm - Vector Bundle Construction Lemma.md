---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Vector Bundle"
  - "Def - Local Trivialization"
  - "Def - Transition Function of a Vector Bundle"
  - "Def - Smooth Manifold"
tags: [geometry, differential-geometry, bundles, construction]
---

# Notation

$M$ is a smooth manifold of dimension $n$ (possibly with boundary). $\{U_\alpha\}_{\alpha \in A}$ is an open cover of $M$, with $A$ an index set. At each $p \in M$, $E_p$ is a fixed real vector space of dimension $k$ — the **fibre** at $p$. The total space is $E := \bigsqcup_{p \in M} E_p$ (disjoint union of fibres), with the natural projection $\pi : E \to M$ sending each element of $E_p$ to $p$. The bijections $\Phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times \mathbb{R}^k$ are linear on each fibre. The transition functions are $\tau_{\alpha\beta} : U_\alpha \cap U_\beta \to \mathrm{GL}(k, \mathbb{R})$, satisfying the cocycle conditions.

---

# Statement

> **Theorem ([[Def - Vector Bundle|Vector Bundle]] Construction Lemma).** Let $M$ be a smooth manifold (with or without boundary). Suppose that for each $p \in M$ we are given a real vector space $E_p$ of fixed [[Def - Dimension|dimension]] $k$. Let $E := \bigsqcup_{p \in M} E_p$ and let $\pi : E \to M$ send each element of $E_p$ to $p$. Suppose further that we are given:
>
> (i) an open cover $\{U_\alpha\}_{\alpha \in A}$ of $M$,
>
> (ii) for each $\alpha \in A$, a bijection $\Phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times \mathbb{R}^k$ whose restriction to each fibre $E_p$ (for $p \in U_\alpha$) is a linear isomorphism $E_p \to \{p\} \times \mathbb{R}^k \cong \mathbb{R}^k$,
>
> (iii) for each pair $\alpha, \beta \in A$ with $U_\alpha \cap U_\beta \neq \emptyset$, a smooth map $\tau_{\alpha\beta} : U_\alpha \cap U_\beta \to \mathrm{GL}(k, \mathbb{R})$ such that the composition $\Phi_\alpha \circ \Phi_\beta^{-1} : (U_\alpha \cap U_\beta) \times \mathbb{R}^k \to (U_\alpha \cap U_\beta) \times \mathbb{R}^k$ has the form
> $$(\Phi_\alpha \circ \Phi_\beta^{-1})(p, v) = (p, \tau_{\alpha\beta}(p) v),$$
>
> with the cocycle conditions $\tau_{\alpha\alpha} = \mathrm{id}$ and $\tau_{\alpha\gamma} = \tau_{\alpha\beta} \tau_{\beta\gamma}$ on triple overlaps.
>
> Then $E$ has a **unique** topology and smooth structure making it into a smooth rank-$k$ vector bundle over $M$ with projection $\pi$, with the $\Phi_\alpha$ as smooth local trivializations.

---

# Motivation

This lemma is the **workhorse construction tool** of vector-bundle theory. Without it, every new vector bundle would require constructing the total space $E$ as a smooth manifold by hand, building charts on $E$, verifying smooth compatibility — a substantial overhead. The construction lemma does all of this once and for all, packaging the work into a checkable criterion: produce fibres, an open cover, candidate trivializations, and a cocycle of transition functions; the lemma then certifies the existence and uniqueness of the resulting bundle.

The lemma is what makes the menagerie of vector bundles — tensor bundles, exterior bundles, jet bundles, spinor bundles, associated bundles — uniform constructions. Each new bundle is built by identifying its fibres, choosing an open cover from charts of $M$, writing down the transition functions, and applying the lemma. The cotangent bundle $T^*M$, in particular, is constructed exactly this way: fibres are $T_p^*M$, transition functions are inverse-transpose Jacobians, and the lemma assembles the bundle (see [[Thm - The Cotangent Bundle is a Smooth Manifold]] and [[Ex - Constructing the Cotangent Bundle from Transition Functions]]).

The role of the cocycle condition is to certify *consistency* of the gluing data. Without the cocycle condition, the three trivializations on a triple overlap would prescribe inconsistent identifications: combining $\Phi_\alpha \circ \Phi_\beta^{-1}$ with $\Phi_\beta \circ \Phi_\gamma^{-1}$ should give $\Phi_\alpha \circ \Phi_\gamma^{-1}$, and this is precisely what $\tau_{\alpha\gamma} = \tau_{\alpha\beta} \tau_{\beta\gamma}$ enforces. With the cocycle in hand, the local trivializations are coherent and assemble into a global structure; without it, the structure is over-determined and contradictory.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis the construction lemma needs is "a manifold, fibre vector spaces, an open cover, candidate trivializations, and a cocycle of transition functions". The skill is recognising, in a problem that does not yet present a bundle, that this data is implicitly available.

The most common source is **a smoothly varying fibrewise multilinear-algebra construction**. Given a vector bundle $E$ and a functor $F$ on finite-dimensional vector spaces (dual, tensor product, exterior power, symmetric power, Hom), the bundle $F(E)$ exists and has the same base manifold, with fibres $F(E_p)$ and transition functions $F(\tau_{\alpha\beta})$. The cocycle inherits from the cocycle of $E$. This is the source behind every construction of derived bundles: the cotangent bundle ($F = $ dual), tensor bundles ($F = $ tensor product), form bundles ($F = $ exterior power), etc.

A second source is **a smoothly varying family of linear subspaces of constant dimension**. Given $E \to M$ and a smoothly varying subspace $D_p \subseteq E_p$ of constant dimension $m$, with the local-frame criterion satisfied ([[Def - Subbundle]]), the subspaces assemble into a subbundle $D \subseteq E$. The construction lemma applied to the candidate trivializations adapted to $D$ provides the smooth structure on $D$.

A third source is **a smooth map $f : M \to N$ and a bundle $E \to N$**. The **pullback bundle** $f^*E$ over $M$ has fibres $(f^*E)_p = E_{f(p)}$ and transition functions $\tau_{\alpha\beta} \circ f$. The cocycle is inherited from $E$, and the construction lemma assembles $f^*E$ as a bundle over $M$. This is the categorical content of "$f^*$ is a functor": given a bundle on $N$, the lemma produces a bundle on $M$.

A fourth source is **a Čech cocycle in $\mathrm{GL}(k, \mathbb{R})$**. A collection of smooth maps $\tau_{\alpha\beta} : U_\alpha \cap U_\beta \to \mathrm{GL}(k, \mathbb{R})$ satisfying the cocycle condition, with no a priori reference to fibres, *is* a vector bundle by the lemma: take fibres $E_p = \mathbb{R}^k$ (as a model), define $E$ as the appropriate quotient of $\bigsqcup_\alpha U_\alpha \times \mathbb{R}^k$ by the cocycle's gluing, and the lemma produces the bundle. This is the abstract source — the bundle is literally specified by its cocycle.

**Targets (Output Amplification)**

The conclusion the lemma delivers is "a smooth rank-$k$ vector bundle with the specified trivializations". Combined with one further hypothesis, it produces structural conclusions about the bundle.

The most powerful combination is **construction lemma plus fibrewise smooth functor produces a derived bundle**. The cotangent bundle, tensor bundles, exterior bundles, and Hom bundles all arise this way. The fibrewise construction is the smooth functor; the transition functions of the derived bundle are obtained by applying the functor to the transitions of the original; the lemma then certifies the derived bundle is smooth.

A second combination is **construction lemma plus structure-group reduction gives a geometric structure**. If the cocycle takes values in a subgroup $G \subseteq \mathrm{GL}(k, \mathbb{R})$, the bundle inherits a $G$-structure: an inner product (for $G = \mathrm{O}(k)$), orientation (for $G = \mathrm{SO}(k)$), volume form (for $G = \mathrm{SL}(k, \mathbb{R})$), or a complex structure (for $G = \mathrm{GL}(k/2, \mathbb{C}) \subseteq \mathrm{GL}(k, \mathbb{R})$). The lemma produces the bundle; the structure-group restriction supplies the additional structure.

A third combination is **construction lemma plus a smooth map $f : M \to N$ gives the pullback bundle**. Pullback bundles are essential to gauge theory and to relating bundles on different manifolds. The construction lemma is what makes "pullback" a precise operation rather than a heuristic.

A fourth combination is **construction lemma plus an open cover refinement gives bundle-isomorphism-equivalence under coboundary**. Two cocycles relative to refinements of the same cover give isomorphic bundles if they differ by a coboundary. The construction lemma applied to both produces bundles that are then identified by the coboundary's gauge transformation.

---

# Why Is It True

The intuition is straightforward and follows from the manifold chart lemma. The candidate total space $E$ has, via the trivializations $\Phi_\alpha$, charts $(\pi^{-1}(U_\alpha), \tilde\Phi_\alpha)$ where $\tilde\Phi_\alpha$ is the composition $\Phi_\alpha$ followed by a chart of $U_\alpha$ in $M$. The transition between two such charts is computed from $\Phi_\alpha \circ \Phi_\beta^{-1}$ and the chart transitions of $M$ — and the cocycle condition on $\tau_{\alpha\beta}$, combined with smoothness of chart transitions, makes the composite smooth.

**The single one-line mechanism summary: the cocycle condition on $\tau_{\alpha\beta}$ is exactly the consistency condition for the charts on $E$ built from $\Phi_\alpha$ to satisfy the manifold chart lemma's smooth-compatibility requirement.**

The construction is essentially a re-statement of the smooth-manifold chart lemma in bundle language. The fibre structure on $E_p$ is well-defined (independent of which $\Phi_\alpha$ is used, by linearity of $\Phi_\alpha|_{E_p}$); the vector-space operations are smooth (by smoothness of the inversions and the cocycle); and the projection is smooth (because in any trivialization it becomes the first-coordinate projection). The uniqueness follows because the trivializations are required to be [[Def - Diffeomorphism|diffeomorphisms]]; this uniquely determines the smooth structure on $E$, which must include all the charts $\tilde\Phi_\alpha$, and the smooth structure is the maximal atlas containing them.

The deeper reason the lemma is true is that **the manifold structure on a vector bundle is forced by the local-triviality data**. Once the trivializations are specified and the cocycle condition is checked, no further choices are available: the smooth structure on $E$ is uniquely determined. The "construction" is therefore not really a construction but a recognition: the data already specifies a unique bundle.

---

# What Makes This Hard

The substantive difficulty is **verifying smoothness of the bundle structure**, especially the smoothness of the projection $\pi$, the smoothness of fibrewise addition and scalar multiplication, and the smoothness of the trivializations. Each of these requires careful coordinate computations using the cocycle, and the temptation is to wave hands and quote the manifold chart lemma — the actual verification is straightforward but bookkeeping-intensive.

The most common error is to **forget to check the cocycle condition** when constructing a bundle from candidate transition functions. If $\tau_{\alpha\gamma} \neq \tau_{\alpha\beta} \tau_{\beta\gamma}$ on a triple overlap, the lemma does not apply, and the candidate data does not assemble into a bundle. This failure mode shows up most often in physics applications where transition functions are written down ad hoc; one must always verify the cocycle.

A subtler error is to **misidentify the fibre's vector-space structure**. The fibre $E_p$ at $p \in U_\alpha$ inherits its structure from $\Phi_\alpha|_{E_p} : E_p \to \mathbb{R}^k$, and this inheritance must be *independent* of $\alpha$. Independence requires the restriction of $\Phi_\alpha \circ \Phi_\beta^{-1}$ to a fibre to be linear — which is precisely the demand that $\tau_{\alpha\beta}(p) \in \mathrm{GL}(k, \mathbb{R})$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Use the smooth-manifold chart lemma to construct the smooth structure on $E$. For each chart $(V, \varphi)$ of $M$ contained in some $U_\alpha$, the composition $\tilde\varphi := (\varphi \times \mathrm{id}_{\mathbb{R}^k}) \circ \Phi_\alpha|_{\pi^{-1}(V)}$ is a candidate chart on $E$ with values in $\varphi(V) \times \mathbb{R}^k \subseteq \mathbb{R}^{n+k}$. Verify that the collection of these candidate charts satisfies the chart-lemma hypotheses: smooth compatibility on overlaps, Hausdorff and second-countable conditions. The cocycle and the smoothness of chart transitions on $M$ supply the compatibility.

**Subgoal decomposition:**

1. **Construct candidate charts on $E$.** For each chart $(V, \varphi)$ of $M$ with $V \subseteq U_\alpha$, define $\tilde\varphi := (\varphi \times \mathrm{id}_{\mathbb{R}^k}) \circ \Phi_\alpha$ on $\pi^{-1}(V)$.
   - *Hint:* Each $\tilde\varphi$ is a bijection $\pi^{-1}(V) \to \varphi(V) \times \mathbb{R}^k$, the latter an open subset of $\mathbb{R}^{n+k}$.
   - *Why needed:* The chart lemma needs candidate charts to even begin.

2. **Verify smooth compatibility on overlaps.** Compute $\tilde\varphi \circ \tilde\psi^{-1}$ for two such charts and show it is smooth, using the cocycle condition and the smoothness of chart transitions on $M$.
   - *Hint:* The composite is $(\varphi \circ \psi^{-1}) \times $ matrix multiplication by $\tau_{\alpha\beta}$, both smooth.
   - *Why needed:* This is the manifold chart lemma's compatibility hypothesis.

3. **Check Hausdorff and second-countable.** Verify that the topology induced on $E$ by the charts is Hausdorff (two points in $E$ can be separated by disjoint chart neighbourhoods) and second-countable (a countable atlas suffices).
   - *Hint:* For Hausdorff, separate points in the same fibre using a single chart; separate points in different fibres using disjoint chart neighbourhoods of their projections in $M$. Second-countability uses second-countability of $M$ and of $\mathbb{R}^k$.
   - *Why needed:* These are the smooth-manifold axioms.

4. **Verify the $\Phi_\alpha$ are smooth local trivializations of the resulting bundle.** Once the smooth structure on $E$ exists, check $\Phi_\alpha$ is a diffeomorphism by computing its coordinate representation in chart $\tilde\varphi$.
   - *Hint:* In coordinates, $\Phi_\alpha$ is the identity on $\varphi(V) \times \mathbb{R}^k$, manifestly smooth.
   - *Why needed:* This certifies the resulting structure on $E$ has the prescribed trivializations.

5. **Verify uniqueness.** Any other smooth structure on $E$ for which the $\Phi_\alpha$ are smooth must contain the charts $\tilde\varphi$, so it is the maximal atlas containing them — uniquely determined.
   - *Hint:* The maximal smooth atlas containing a given subatlas is unique.
   - *Why needed:* This completes the existence-and-uniqueness statement.

---

# Lemma Decomposition

> [!note]- Lemma 1: Candidate charts on $E$ are bijections onto open subsets of $\mathbb{R}^{n+k}$
> **Statement:** For each chart $(V, \varphi)$ of $M$ with $V \subseteq U_\alpha$, the composition $\tilde\varphi := (\varphi \times \mathrm{id}_{\mathbb{R}^k}) \circ \Phi_\alpha|_{\pi^{-1}(V)}$ is a bijection from $\pi^{-1}(V)$ onto $\varphi(V) \times \mathbb{R}^k \subseteq \mathbb{R}^{n+k}$.
>
> **Hint:** Both $\Phi_\alpha$ and $\varphi \times \mathrm{id}_{\mathbb{R}^k}$ are bijections (the first by hypothesis, the second from $\varphi$ being a chart).
>
> **Why needed:** This produces the candidate atlas on $E$.
>
> > [!note]- Full proof
> > $\Phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times \mathbb{R}^k$ is a bijection by hypothesis. Restriction to $\pi^{-1}(V) \subseteq \pi^{-1}(U_\alpha)$ gives a bijection onto $V \times \mathbb{R}^k$. Postcomposing with $\varphi \times \mathrm{id}_{\mathbb{R}^k}$ (a bijection $V \times \mathbb{R}^k \to \varphi(V) \times \mathbb{R}^k$) gives the bijection $\tilde\varphi : \pi^{-1}(V) \to \varphi(V) \times \mathbb{R}^k$.

> [!note]- Lemma 2: Two candidate charts have smooth transition
> **Statement:** For two charts $(V, \varphi) \subseteq U_\alpha$ and $(W, \psi) \subseteq U_\beta$ with $V \cap W \neq \emptyset$, the transition $\tilde\varphi \circ \tilde\psi^{-1}$ is a smooth map between open subsets of $\mathbb{R}^{n+k}$.
>
> **Hint:** Compute $\tilde\varphi \circ \tilde\psi^{-1}(\psi(p), v) = (\varphi(p), \tau_{\alpha\beta}(p) v)$, using the cocycle.
>
> **Why needed:** This is the chart-lemma compatibility.
>
> > [!note]- Full proof
> > Let $(\psi(p), v) \in \psi(V \cap W) \times \mathbb{R}^k$, with $p \in V \cap W$. Then $\tilde\psi^{-1}(\psi(p), v) = \Phi_\beta^{-1}(p, v) \in \pi^{-1}(V \cap W) \subseteq E$. Applying $\Phi_\alpha$: $\Phi_\alpha(\Phi_\beta^{-1}(p, v)) = (p, \tau_{\alpha\beta}(p) v)$ by the cocycle hypothesis. Then applying $\varphi \times \mathrm{id}$: $\tilde\varphi \circ \tilde\psi^{-1}(\psi(p), v) = (\varphi(p), \tau_{\alpha\beta}(p) v)$. Both components are smooth: $\psi(p) \mapsto \varphi(p)$ is smooth because it is $\varphi \circ \psi^{-1}$, the chart transition on $M$; and $\psi(p) \mapsto \tau_{\alpha\beta}(p) v$ is smooth because $\tau_{\alpha\beta}$ is smooth on $V \cap W$ and matrix-vector multiplication is smooth.

> [!note]- Lemma 3: The atlas on $E$ satisfies the chart lemma hypotheses
> **Statement:** The collection of candidate charts $\{(\pi^{-1}(V), \tilde\varphi)\}$ as $V$ ranges over a chart-cover of $M$ refining $\{U_\alpha\}$ satisfies: (i) chart bijections to open sets in $\mathbb{R}^{n+k}$, (ii) smooth-compatible on overlaps, (iii) countable subcover available, (iv) Hausdorff condition.
>
> **Hint:** (i) and (ii) are Lemmas 1 and 2. (iii) uses second-countability of $M$. (iv) uses Hausdorff of $M$ and the fibre structure.
>
> **Why needed:** This is the input to the smooth-manifold chart lemma.
>
> > [!note]- Full proof
> > (i) and (ii) by Lemmas 1 and 2. (iii) Since $M$ is second-countable, the cover $\{U_\alpha\}$ has a countable refinement by charts. The corresponding $\tilde\varphi$ provide a countable atlas on $E$. (iv) For two points $u_1, u_2 \in E$ with $\pi(u_1) = \pi(u_2) = p$, they lie in a single fibre $E_p$, and a single chart $\tilde\varphi$ contains both — Hausdorff in the chart is Hausdorff in $\mathbb{R}^{n+k}$. For $\pi(u_1) \neq \pi(u_2)$, the Hausdorff condition on $M$ provides disjoint open sets $V_1 \ni \pi(u_1)$ and $V_2 \ni \pi(u_2)$, whose preimages $\pi^{-1}(V_1), \pi^{-1}(V_2)$ are disjoint open sets in $E$ separating $u_1$ from $u_2$.

> [!note]- Lemma 4: $\Phi_\alpha$ is a diffeomorphism in the resulting smooth structure
> **Statement:** Once $E$ is equipped with the smooth structure from the chart lemma, each $\Phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times \mathbb{R}^k$ is a diffeomorphism.
>
> **Hint:** In a chart $\tilde\varphi$ on $E$ and the chart $\varphi \times \mathrm{id}_{\mathbb{R}^k}$ on $U_\alpha \times \mathbb{R}^k$, $\Phi_\alpha$ is the identity map.
>
> **Why needed:** This certifies that the $\Phi_\alpha$ are smooth local trivializations of the resulting bundle.
>
> > [!note]- Full proof
> > Compute the coordinate representation of $\Phi_\alpha$ in the charts $\tilde\varphi$ on the domain and $\varphi \times \mathrm{id}_{\mathbb{R}^k}$ on the codomain. $\tilde\varphi = (\varphi \times \mathrm{id}_{\mathbb{R}^k}) \circ \Phi_\alpha$, so $(\varphi \times \mathrm{id}_{\mathbb{R}^k}) \circ \Phi_\alpha \circ \tilde\varphi^{-1} = (\varphi \times \mathrm{id}_{\mathbb{R}^k}) \circ \Phi_\alpha \circ \Phi_\alpha^{-1} \circ (\varphi \times \mathrm{id}_{\mathbb{R}^k})^{-1} = \mathrm{id}$ on $\varphi(V) \times \mathbb{R}^k$. So $\Phi_\alpha$ has the identity as its coordinate representation in these charts — manifestly smooth, with smooth inverse the identity.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — Well-posedness.** The fibre $E_p$ for $p \in U_\alpha \cap U_\beta$ inherits the same vector-space structure regardless of which trivialization $\Phi_\alpha$ or $\Phi_\beta$ is used: the transition $\Phi_\alpha \circ \Phi_\beta^{-1}$ restricted to the fibre is multiplication by $\tau_{\alpha\beta}(p) \in \mathrm{GL}(k, \mathbb{R})$, a linear isomorphism, so the vector-space structure on $E_p$ is well-defined.
>
> **Step 1 — Candidate charts on $E$.** For each chart $(V, \varphi)$ of $M$ contained in some $U_\alpha$, define $\tilde\varphi : \pi^{-1}(V) \to \varphi(V) \times \mathbb{R}^k$ by $\tilde\varphi(u) := (\varphi(\pi(u)), \pi_2 \Phi_\alpha(u))$, where $\pi_2 : U_\alpha \times \mathbb{R}^k \to \mathbb{R}^k$. By Lemma 1 each $\tilde\varphi$ is a bijection.
>
> **Step 2 — Smooth compatibility.** For two such charts $\tilde\varphi$ (associated to $U_\alpha$) and $\tilde\psi$ (associated to $U_\beta$) with $V \cap W \neq \emptyset$, the transition $\tilde\varphi \circ \tilde\psi^{-1}$ on $\psi(V \cap W) \times \mathbb{R}^k$ is $(\psi(p), v) \mapsto (\varphi(p), \tau_{\alpha\beta}(p) v)$. The first component is the smooth chart transition $\varphi \circ \psi^{-1}$; the second is smooth as a composition of the smooth $\tau_{\alpha\beta}$ and the smooth matrix-vector multiplication. So the transition is smooth.
>
> **Step 3 — Manifold-chart-lemma hypotheses.** The collection of candidate charts is a smooth atlas (by Step 2). $M$ is second-countable, so a countable refinement of $\{U_\alpha\}$ by charts gives a countable atlas on $E$. The Hausdorff condition: for points in the same fibre, use a single chart; for points in different fibres, use disjoint $V_1, V_2$ around their projections in $M$ to get disjoint $\pi^{-1}(V_1), \pi^{-1}(V_2)$ in $E$.
>
> **Step 4 — Apply the chart lemma.** The smooth-manifold chart lemma gives $E$ a unique smooth manifold structure of dimension $n + k$ for which the candidate charts are smooth.
>
> **Step 5 — $\pi$ is smooth.** In a chart $\tilde\varphi$ on $E$ and $\varphi$ on $M$, $\pi$ has coordinate representation $(x, v) \mapsto x$, the first-factor projection — manifestly smooth.
>
> **Step 6 — $\Phi_\alpha$ are diffeomorphisms.** By Lemma 4, each $\Phi_\alpha$ has the identity as its coordinate representation, hence is a diffeomorphism. The compatibility-with-projection ($\pi_1 \circ \Phi_\alpha = \pi$) and linearity-on-fibres are by hypothesis.
>
> **Step 7 — Linear structure on fibres.** The fibrewise vector-space structure is smooth: addition $E_p \times E_p \to E_p$ and scalar multiplication $\mathbb{R} \times E_p \to E_p$ are smooth on $E$, because in a trivialization $\Phi_\alpha$ they become the standard operations on $\mathbb{R}^k$, which are smooth.
>
> **Step 8 — Uniqueness.** Any smooth structure on $E$ for which $\Phi_\alpha$ are smooth local trivializations must include the candidate charts $\tilde\varphi$ in its maximal atlas, and by the chart lemma the maximal atlas containing a given subatlas is unique.
>
> $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Algebraic topology: classification of line bundles.** A real line bundle (rank-$1$ vector bundle) on a manifold $M$ has structure [[Def - Group|group]] $\mathrm{GL}(1, \mathbb{R}) = \mathbb{R}^*$, and isomorphism classes are classified by $H^1(M; \mathbb{Z}/2)$ — specifically, the first Stiefel–Whitney class detects whether the bundle is trivial or "twisted" like the Möbius bundle. Use the construction lemma to build the line bundles corresponding to each element of $H^1(M; \mathbb{Z}/2)$.

**Gauge theory: bundles with prescribed connections.** Given a connection 1-form $A$ on an open cover of $M$ with values in a Lie algebra, the bundle that admits $A$ as a connection is constructed via the lemma applied to the transition functions implied by the gauge transformations of $A$. Yang–Mills theory is the variational principle on the resulting moduli space of connections.

**Algebraic geometry: vector bundles on projective space.** The tautological line bundle on $\mathbb{CP}^n$ and its dual (the hyperplane bundle $\mathcal{O}(1)$) can be constructed explicitly via the construction lemma applied to the standard open cover by affine charts. The transition functions are rational functions, and the bundle structure inherits from the cocycle.

**Physics: spinor bundles on a spin manifold.** A **spin structure** on a Riemannian manifold $M$ is a lift of the orthonormal frame bundle (structure group $\mathrm{SO}(n)$) to a $\mathrm{Spin}(n)$-bundle. The associated spinor bundle has fibre $\mathbb{C}^{2^{n/2}}$ (for even $n$), and is constructed via the lemma applied to the lifted transition functions. The Dirac operator is then a differential operator on this bundle.

---

# Bridges

- **[[Def - Smooth Manifold]] and the smooth-manifold chart lemma** — The construction lemma is the bundle counterpart of the manifold chart lemma. Both convert "local data + smooth-compatibility cocycle" into "global smooth structure". The bundle version is structurally identical, with $\mathrm{GL}(k, \mathbb{R})$ playing the role of the group of smooth changes of coordinates.

- **[[Thm - The Cotangent Bundle is a Smooth Manifold]]** — The cotangent bundle $T^*M$ is constructed by applying the construction lemma to the open cover of $M$ by coordinate charts and the inverse-transpose Jacobian transition functions. This is the canonical first application of the lemma.

- **Principal bundles and associated bundles** *(from gauge theory)* — The construction lemma generalizes to fibre bundles with arbitrary structure group $G$: given an open cover, candidate trivializations of $G$-action, and a cocycle of $G$-valued transition functions, a principal $G$-bundle is constructed. Vector bundles are the case $G = \mathrm{GL}(k, \mathbb{R})$ acting on $\mathbb{R}^k$. The associated bundle construction extends to other $G$-representations.

- **Čech cohomology of $\mathrm{GL}(k, \mathbb{R})$-valued functions** *(from algebraic topology)* — The construction lemma's hypotheses are exactly that of a Čech $1$-cocycle in the sheaf of smooth $\mathrm{GL}(k, \mathbb{R})$-valued functions. The lemma proves cocycles can be realised as bundles; the cohomological classification says isomorphism classes are $H^1(M; \mathrm{GL}(k, \mathbb{R}))$, which factors through the homotopy classes of maps to $B\mathrm{GL}(k, \mathbb{R})$.

---

# Unlocked by This

> [!tip] Construction of Tensor Bundles, Form Bundles, Jet Bundles *(from Differential Geometry VII and VIII)*
> Every multilinear-algebra construction on vector spaces — tensor product, exterior power, symmetric power, Hom, jet — applied fibrewise to $TM$ and/or $T^*M$ produces a new vector bundle, with transition functions obtained by applying the multilinear construction to the transitions of $TM$. The construction lemma assembles each such bundle in one step.

> [!tip] Pullback Bundle and Naturality *(from this topic)*
> The construction lemma gives the existence of the **pullback bundle** $f^*E$ over $M$ for any smooth $f : M \to N$ and bundle $E \to N$. The cocycle of $f^*E$ is the cocycle of $E$ composed with $f$. Pullback bundles are essential in gauge theory and in defining how bundles transform under changes of base.

> [!tip] Associated Bundle Construction *(from Gauge Theory)*
> Given a principal $G$-bundle $P \to M$ and a representation $\rho : G \to \mathrm{GL}(V)$, the associated bundle $P \times_G V$ has the same transition functions as $P$ but acting on $V$ via $\rho$. The construction lemma provides the smooth structure on the associated bundle, generalizing the vector-bundle construction to arbitrary $G$-representations.
