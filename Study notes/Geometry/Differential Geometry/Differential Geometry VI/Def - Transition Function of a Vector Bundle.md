---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Vector Bundle"
  - "Def - Local Trivialization"
  - "Def - Smooth Map between Manifolds"
  - "Def - Group"
tags: [geometry, differential-geometry, bundles, structure-group]
---

# Notation

$\pi : E \to M$ is a smooth vector bundle of rank $k$ (see [[Def - Vector Bundle]]). $\{(U_\alpha, \Phi_\alpha)\}_{\alpha \in A}$ is a trivializing atlas: an open cover $\{U_\alpha\}$ of $M$ together with smooth local trivializations $\Phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times \mathbb{R}^k$ (see [[Def - Local Trivialization]]). The transition function is the map $\tau_{\alpha\beta} : U_\alpha \cap U_\beta \to \mathrm{GL}(k, \mathbb{R})$ obtained from the composition $\Phi_\alpha \circ \Phi_\beta^{-1}$. The group $\mathrm{GL}(k, \mathbb{R})$ is the [[Def - Group|group]] of invertible real $k \times k$ matrices under multiplication.

---

# Axiom Motivation

The transition function answers a single question: **when two local trivializations of the same bundle overlap, what changes?** The answer reveals the entire structural data of the bundle, because the trivializations are the only mechanism by which the abstract bundle is seen, and the transition between them encodes everything intrinsic that survives the choice of trivialization.

Begin with the algebraic structure of an overlap. Given two trivializations $\Phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times \mathbb{R}^k$ and $\Phi_\beta : \pi^{-1}(U_\beta) \to U_\beta \times \mathbb{R}^k$ with $U_\alpha \cap U_\beta \neq \emptyset$, the composition $\Phi_\alpha \circ \Phi_\beta^{-1}$ is a self-map of $(U_\alpha \cap U_\beta) \times \mathbb{R}^k$. The two compatibility conditions in [[Def - Local Trivialization|the definition of a local trivialization]] — projection compatibility and linearity on fibres — pin this composition down to a very rigid form. Projection compatibility forces $\Phi_\alpha \circ \Phi_\beta^{-1}$ to preserve the first coordinate, sending $(p, v)$ to $(p, \text{something})$. Linearity on fibres forces the second coordinate to depend on $v$ linearly. Together these say
$$(\Phi_\alpha \circ \Phi_\beta^{-1})(p, v) = (p, \tau_{\alpha\beta}(p) v)$$
for some assignment $p \mapsto \tau_{\alpha\beta}(p)$ of an invertible linear map $\mathbb{R}^k \to \mathbb{R}^k$ — that is, an element of $\mathrm{GL}(k, \mathbb{R})$. The smoothness of $\Phi_\alpha \circ \Phi_\beta^{-1}$ then forces $\tau_{\alpha\beta}$ to be a smooth function $U_\alpha \cap U_\beta \to \mathrm{GL}(k, \mathbb{R})$.

That is the *form* of the transition function. The substantive content is what conditions $\tau_{\alpha\beta}$ must satisfy. There are three, each forced by the consistency of the trivializing atlas.

First, on each set $U_\alpha$ alone, the transition from $\Phi_\alpha$ to itself is the identity: $\tau_{\alpha\alpha}(p) = \mathrm{id}_{\mathbb{R}^k}$. This is purely cosmetic — it follows immediately from the definition — but it is worth noting because it is the "identity" axiom of the cocycle.

Second, on an overlap $U_\alpha \cap U_\beta$, the transition $\Phi_\alpha \circ \Phi_\beta^{-1}$ and the reverse transition $\Phi_\beta \circ \Phi_\alpha^{-1}$ are inverses of each other, so
$$\tau_{\beta\alpha}(p) = \tau_{\alpha\beta}(p)^{-1}.$$
This is the symmetry axiom of the cocycle: reverse the trivializations and you reverse the matrix.

Third, and most importantly, on a triple overlap $U_\alpha \cap U_\beta \cap U_\gamma$, three trivializations are available, and the compositions $\Phi_\alpha \circ \Phi_\gamma^{-1}$ and $\Phi_\alpha \circ \Phi_\beta^{-1} \circ \Phi_\beta \circ \Phi_\gamma^{-1}$ are tautologically equal (the middle pair cancels). Reading off transition functions, this gives the **cocycle condition**
$$\tau_{\alpha\gamma}(p) = \tau_{\alpha\beta}(p) \cdot \tau_{\beta\gamma}(p) \quad \text{for } p \in U_\alpha \cap U_\beta \cap U_\gamma.$$
This is the deep axiom. It says the transitions compose multiplicatively, and it is precisely the consistency condition that lets a collection of local trivializations assemble into a single global bundle. The cocycle condition is non-trivial — it constrains the choices of $\tau_{\alpha\beta}$ — and it is exactly the condition under which the [[Thm - Vector Bundle Construction Lemma|vector-bundle construction lemma]] produces a bundle from the data.

What is forced by demanding $\tau_{\alpha\beta}$ to take values in $\mathrm{GL}(k, \mathbb{R})$ specifically, rather than in a larger [[Def - Group|group]] of [[Def - Diffeomorphism|diffeomorphisms]] of $\mathbb{R}^k$? This is the **linearity on fibres** condition: trivializations are *linear* on each fibre, so their compositions on fibres are linear [[Def - Isomorphism|isomorphisms]] — that is, elements of $\mathrm{GL}(k, \mathbb{R})$. If we allowed arbitrary fibre-diffeomorphisms, the transition functions would take values in $\mathrm{Diff}(\mathbb{R}^k)$ — a much larger group — and the bundle would be a **fibre bundle**, not a vector bundle. The vector-bundle theory is the special case where the structure group is $\mathrm{GL}(k, \mathbb{R})$.

What is forced by demanding **smoothness** of $\tau_{\alpha\beta}$ rather than continuity? The smoothness of the trivializations (as diffeomorphisms) is what supplies $E$ with its smooth structure; smoothness of the transition functions is the manifestation of this on the overlap. A continuous-but-non-smooth transition function would give $E$ only the structure of a topological vector bundle, not a smooth one.

What if we **strengthened** by demanding $\tau_{\alpha\beta}$ take values in a [[Def - Subgroup|subgroup]] of $\mathrm{GL}(k, \mathbb{R})$? Each such strengthening corresponds to extra structure on the bundle. Taking values in $\mathrm{O}(k)$ means there is a Riemannian metric on $E$ (the standard inner product on $\mathbb{R}^k$ is preserved by transitions, so it descends to a well-defined inner product on each fibre). Taking values in $\mathrm{SO}(k)$ means there is both a metric and an orientation. Taking values in $\mathrm{SL}(k, \mathbb{R})$ means there is a volume form. Taking values in the trivial group $\{1\}$ means the bundle is **trivial**. Each reduction of the structure group corresponds to a geometric structure that the bundle carries.

What if we **weakened** by dropping the cocycle condition? Then the local pieces would not fit together: trying to assemble them into a global $E$ would produce a non-Hausdorff or inconsistent space. The cocycle is the consistency condition without which the bundle does not exist.

---

# The Definition

Let $\pi : E \to M$ be a smooth vector bundle of rank $k$, and let $\Phi_\alpha : \pi^{-1}(U_\alpha) \to U_\alpha \times \mathbb{R}^k$ and $\Phi_\beta : \pi^{-1}(U_\beta) \to U_\beta \times \mathbb{R}^k$ be two smooth local trivializations with $U_\alpha \cap U_\beta \neq \emptyset$. The **transition function** $\tau_{\alpha\beta}$ from $\Phi_\beta$ to $\Phi_\alpha$ is the unique smooth map
$$\tau_{\alpha\beta} : U_\alpha \cap U_\beta \to \mathrm{GL}(k, \mathbb{R})$$
such that
$$(\Phi_\alpha \circ \Phi_\beta^{-1})(p, v) = (p, \tau_{\alpha\beta}(p) v) \quad \text{for all } (p, v) \in (U_\alpha \cap U_\beta) \times \mathbb{R}^k.$$
The existence and smoothness of $\tau_{\alpha\beta}$ is forced by the local-triviality conditions: projection compatibility makes $\Phi_\alpha \circ \Phi_\beta^{-1}$ preserve the first coordinate; linearity on fibres makes the second-coordinate dependence on $v$ linear, so it is multiplication by an invertible matrix that varies smoothly with $p$.

For a trivializing atlas $\{(U_\alpha, \Phi_\alpha)\}_{\alpha \in A}$, the collection $\{\tau_{\alpha\beta}\}_{\alpha, \beta \in A}$ satisfies the following three properties, jointly called the **cocycle conditions**:

1. **Identity:** $\tau_{\alpha\alpha}(p) = \mathrm{id}_{\mathbb{R}^k}$ for all $\alpha$ and all $p \in U_\alpha$.
2. **Inverse:** $\tau_{\beta\alpha}(p) = \tau_{\alpha\beta}(p)^{-1}$ for all $\alpha, \beta$ and all $p \in U_\alpha \cap U_\beta$.
3. **Cocycle:** $\tau_{\alpha\gamma}(p) = \tau_{\alpha\beta}(p) \cdot \tau_{\beta\gamma}(p)$ for all $\alpha, \beta, \gamma$ and all $p \in U_\alpha \cap U_\beta \cap U_\gamma$.

The Lie group $\mathrm{GL}(k, \mathbb{R})$ is called the **structure group** of the bundle. A **reduction of structure** is a choice of trivializing atlas whose transition functions take values in a fixed subgroup $G \subseteq \mathrm{GL}(k, \mathbb{R})$; this is equivalent to an extra geometric structure (a metric, orientation, volume form, etc.) on $E$.

---

# Relate to Other Fields / Compression

The transition function is **the gluing data for the vector bundle**, in the same sense that transition maps between charts are the gluing data for a smooth manifold. A smooth manifold is built from open subsets of $\mathbb{R}^n$ via smooth transition maps $\varphi_\beta \circ \varphi_\alpha^{-1} : \varphi_\alpha(U_\alpha \cap U_\beta) \to \varphi_\beta(U_\alpha \cap U_\beta)$; a vector bundle is built from local products $U_\alpha \times \mathbb{R}^k$ via smooth transition functions $\tau_{\alpha\beta} : U_\alpha \cap U_\beta \to \mathrm{GL}(k, \mathbb{R})$. The analogy is exact, and the [[Thm - Vector Bundle Construction Lemma|construction lemma]] is the bundle counterpart of the smooth-manifold chart lemma.

The transition function is also a **Čech 1-cocycle with values in the sheaf of smooth $\mathrm{GL}(k, \mathbb{R})$-valued functions**. Two cocycles differing by a coboundary (refinement of cover, change of trivialization on each $U_\alpha$ by a function $g_\alpha : U_\alpha \to \mathrm{GL}(k, \mathbb{R})$) give isomorphic bundles. So the isomorphism classes of rank-$k$ vector bundles over $M$ are classified by the first Čech cohomology
$$H^1(M; \underline{\mathrm{GL}(k, \mathbb{R})}),$$
where $\underline{\mathrm{GL}(k, \mathbb{R})}$ is the sheaf of smooth $\mathrm{GL}(k, \mathbb{R})$-valued functions. For complex vector bundles one replaces $\mathrm{GL}(k, \mathbb{R})$ by $\mathrm{GL}(k, \mathbb{C})$; for oriented bundles by $\mathrm{GL}^+(k, \mathbb{R})$; and so on.

**True name:** the transition function is "**a smoothly varying change-of-basis matrix between two local choices of basis for the bundle**". Each trivialization corresponds to a local frame; the transition function is the change-of-basis matrix from one frame to the other, evaluated pointwise.

A useful slogan: **the bundle IS its cocycle of transition functions**, up to coboundary equivalence. The total space, the projection, and the fibre structures are all reconstructible from the cocycle via the [[Thm - Vector Bundle Construction Lemma|construction lemma]]. The cocycle is the complete and minimal invariant.

---

# Examples / Corollaries

**Is an instance — transition functions of $TM$ are the Jacobians.** Given two coordinate charts $(U_\alpha, x^i)$ and $(U_\beta, \tilde x^j)$ on $M$, the induced trivializations of $TM$ are $\Phi_\alpha(v^i \partial/\partial x^i|_p) = (p, v^1, \dots, v^n)$ and similarly for $\Phi_\beta$. On the overlap, a tangent vector has two coordinate expressions related by the chain rule: if $v^i \partial/\partial x^i = \tilde v^j \partial/\partial \tilde x^j$, then $\tilde v^j = (\partial \tilde x^j/\partial x^i) v^i$. So the transition function is
$$\tau_{\beta\alpha}(p) = \left( \frac{\partial \tilde x^j}{\partial x^i}(p) \right)_{j,i} \in \mathrm{GL}(n, \mathbb{R}),$$
the Jacobian matrix of the coordinate change $\varphi_\beta \circ \varphi_\alpha^{-1}$.

**Is an instance — transition functions of $T^*M$ are inverse-transpose Jacobians.** Given the same two charts, the dual frames are $(dx^i)$ and $(d\tilde x^j)$. A covector $\omega$ has expressions $\omega = \omega_i \, dx^i = \tilde\omega_j \, d\tilde x^j$, and from $d\tilde x^j = (\partial \tilde x^j/\partial x^i) dx^i$ one finds $\omega_i = (\partial \tilde x^j/\partial x^i) \tilde\omega_j$, so $\tilde\omega_j = (\partial x^i/\partial \tilde x^j) \omega_i$ — the *inverse* Jacobian. As a matrix on covector components, the transition function is the inverse transpose of the tangent-bundle transition function:
$$\tau^{T^*M}_{\beta\alpha}(p) = \left(\tau^{TM}_{\beta\alpha}(p)\right)^{-T}.$$
The "covariant" transformation rule for covectors is precisely this inverse-transpose.

**Is an instance — Möbius bundle transition functions are $\pm 1$.** For the Möbius bundle over $S^1$, with $S^1 = U_1 \cup U_2$ as a union of two open arcs whose overlap has two components, the transition function $\tau_{12} : U_1 \cap U_2 \to \mathrm{GL}(1, \mathbb{R}) = \mathbb{R}^*$ takes the value $+1$ on one component and $-1$ on the other. The sign change is the "twist" of the Möbius band, and it is the obstruction to triviality: if $\tau_{12}$ could be lifted to a constant function, $E$ would be trivial.

**Is an instance — trivial bundle has identity transition functions.** For $M \times \mathbb{R}^k$ with a single global trivialization, the transition function is trivially $\tau \equiv \mathrm{id}$. Conversely, if a bundle has a trivializing atlas with all transition functions equal to the identity, the local trivializations glue to a global one, and the bundle is trivial.

**Is NOT an instance — a smooth $\mathrm{GL}(k, \mathbb{R})$-valued function that fails the cocycle condition.** Take $M = S^1$, an open cover $\{U_1, U_2, U_3\}$ by three arcs each overlapping the next, and propose transition functions $\tau_{12} = +1$, $\tau_{23} = +1$, $\tau_{13} = -1$ on the overlaps. On the triple overlap (if there is one — choose the cover so all three meet), the cocycle condition demands $\tau_{13} = \tau_{12} \tau_{23} = +1$, contradicting $\tau_{13} = -1$. So this is *not* a valid cocycle, and it does not assemble into a bundle.

**Corollary — the cocycle determines the bundle up to isomorphism.** Two cocycles $\{\tau_{\alpha\beta}\}$ and $\{\tau'_{\alpha\beta}\}$ relative to (possibly different refinements of) the same cover yield isomorphic bundles if and only if there exist smooth functions $g_\alpha : U_\alpha \to \mathrm{GL}(k, \mathbb{R})$ such that $\tau'_{\alpha\beta} = g_\alpha \tau_{\alpha\beta} g_\beta^{-1}$. The maps $g_\alpha$ are the change-of-trivialization within each chart.

**Corollary — reduction of structure group corresponds to extra structure.** If a trivializing atlas can be chosen so that all $\tau_{\alpha\beta}$ take values in a subgroup $G \subseteq \mathrm{GL}(k, \mathbb{R})$, then any structure on $\mathbb{R}^k$ that is invariant under $G$ descends to a well-defined structure on each fibre $E_p$. For $G = \mathrm{O}(k)$, the invariant structure is the inner product; for $G = \mathrm{SO}(k)$, the inner product and orientation; for $G = \mathrm{Sp}(2n, \mathbb{R})$, a symplectic form; for $G = \{1\}$, a trivialization (so all of these are obstructed equally by the topology of the bundle).

**Calibration check.** Verify the cocycle condition $\tau_{\alpha\gamma} = \tau_{\alpha\beta} \tau_{\beta\gamma}$ by expanding $(\Phi_\alpha \circ \Phi_\beta^{-1}) \circ (\Phi_\beta \circ \Phi_\gamma^{-1}) = \Phi_\alpha \circ \Phi_\gamma^{-1}$. Compute the transition functions of $TS^2$ for the two-chart stereographic atlas and confirm they are smooth $\mathrm{GL}(2, \mathbb{R})$-valued functions on the overlap (which is $S^2$ minus two points). Verify that the inverse-transpose relationship between $TM$ and $T^*M$ transitions follows from the duality of bases.

---

# Unlocked by This

> [!tip] Principal Bundle and Associated Bundle *(from Gauge Theory)*
> Forgetting the fibre $\mathbb{R}^k$ and remembering only the cocycle $\{\tau_{\alpha\beta}\}$ with values in a Lie group $G = \mathrm{GL}(k, \mathbb{R})$ gives a **principal $G$-bundle** $P \to M$. The original vector bundle is then the **associated bundle** $E = P \times_G \mathbb{R}^k$. This separation of structural data (the $G$-bundle $P$) from fibre data ($\mathbb{R}^k$ with the standard $G$-action) is the foundation of gauge theory: replacing $G$ by other Lie groups ($U(1)$, $\mathrm{SU}(n)$, etc.) and replacing $\mathbb{R}^k$ by other representations of $G$ produces the panoply of fibre bundles used in physics.

> [!tip] Characteristic Classes *(from Algebraic Topology)*
> A cocycle of transition functions in $\mathrm{GL}(k, \mathbb{R})$ has cohomological obstructions to being a coboundary — these obstructions are the **characteristic classes** of the bundle. The first Stiefel–Whitney class $w_1(E)$ measures whether the structure group reduces to $\mathrm{GL}^+(k, \mathbb{R})$ (orientability of $E$); the Euler class $e(E)$ measures the obstruction to a nowhere-vanishing global section; the Pontryagin and Chern classes are higher-dimensional analogues. The cocycle perspective is what makes the cohomological classification of bundles possible.

> [!tip] Classifying Space and BG-Theory *(from Algebraic Topology)*
> Rank-$k$ real vector bundles over $M$ are classified by homotopy classes of maps $M \to BO(k)$ (or $M \to B\mathrm{GL}(k, \mathbb{R})$), where $B\mathrm{GL}(k, \mathbb{R})$ is the **classifying space** of $\mathrm{GL}(k, \mathbb{R})$. The universal bundle on $B\mathrm{GL}(k, \mathbb{R})$ pulls back to any rank-$k$ bundle via the classifying map, and the universal characteristic classes pull back to the classes of the specific bundle. This is one of the most powerful structural results of algebraic topology: bundle classification reduces to homotopy classification of maps into a single universal space.
