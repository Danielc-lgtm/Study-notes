---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Smooth Action of a Lie Group"
  - "Def - Fibre Bundle"
tags: [geometry, gauge-theory, associated-bundles]
---

# Notation

For a principal $G$-bundle $\pi : P \to M$ and a smooth left $G$-action on a manifold $F$, the **associated bundle** is written $P \times_G F$ or $P \times^G F$. A point of $P \times_G F$ is an equivalence class $[u, y]$ with $u \in P$, $y \in F$, modulo $(u, y) \sim (u \cdot g, g^{-1} \cdot y)$ for all $g \in G$. The projection $P \times_G F \to M$ sends $[u, y]$ to $\pi_P(u)$. For a representation $\rho : G \to \mathrm{GL}(V)$, the associated vector bundle is $P \times_\rho V = P \times_G V$ with the corresponding action. See [[Gauge Theory II — Principal Bundles, Representations, and Bundle Classification]] for the full registry.

---

# Axiom Motivation

The associated-bundle construction is the **universal recipe for building every fibre bundle with structure group $G$ from a single principal $G$-bundle**. Given a principal $G$-bundle $P \to M$ (the "frame" data, with structure group $G$ acting), every fibre bundle with the same structure group $G$ is recovered by specifying the *typical fibre* $F$ and the *action* $G \times F \to F$. This is the unifying frame of the chapter: a principal bundle is the universal object, and associated bundles are the *derived* bundles obtained by combining the principal bundle with a $G$-space.

Why **quotient by the diagonal action** $(u, y) \cdot g = (u \cdot g, g^{-1} \cdot y)$? The point is to take the data $(u, y)$ — "a frame $u$ and a point $y$ in the fibre" — and identify it with the data $(u \cdot g, g^{-1} \cdot y)$ — "the rotated frame $u \cdot g$ and the inverse-rotated point $g^{-1} \cdot y$". Why this particular identification? Because in any local trivialization of $P$, a frame $u$ corresponds to a basis of $E_p$, and a point $y \in F$ corresponds to the *components* of the fibre point with respect to that basis. Changing the frame ($u \to u \cdot g$) must be balanced by changing the components ($y \to g^{-1} \cdot y$) to keep the underlying geometric object the same. The diagonal-quotient construction enforces this invariance.

Why is the quotient **smooth**? The diagonal action of $G$ on $P \times F$ is free (because the action on $P$ is free) and proper (because $P \to M$ is proper as a fibre bundle and the action on $F$ is by diffeomorphisms), so the quotient manifold theorem gives a smooth structure on $P \times_G F$ such that the quotient map $P \times F \to P \times_G F$ is a surjective submersion. Without freeness/properness we would not get a manifold.

Why **fibre $F$**? Over each $p \in M$, the fibre $(P \times_G F)_p$ is $\pi^{-1}(p) \times F / G$. Since $\pi^{-1}(p) \cong G$ (after choosing a basepoint $u_0$), the fibre is $G \times F / G$ where $G$ acts by $(g, y) \mapsto (gh, h^{-1} y)$; choosing $u_0$ to map to $g = e$, the fibre is identified with $F$ itself via $[u_0, y] \mapsto y$. So the associated bundle has typical fibre $F$, with the structure group $G$ acting on $F$ as specified.

What goes wrong if we **omit the inverse** in the diagonal action — i.e., use $(u, y) \cdot g = (u \cdot g, g \cdot y)$? The quotient does not have the right fibre structure: in the local trivialization the "components" $y$ would transform the *same* way as the frame, not the opposite way, and the construction would not recover the original bundle from its frame bundle. Concretely, for the tangent bundle: under a change of basis $e \to eg$, a vector $v = e^\alpha v_\alpha$ has components transforming as $v_\alpha \to g^{-1} v_\alpha$ (inverse) so that the vector itself stays fixed. The inverse is what makes the geometric object invariant.

What goes wrong if we **drop the local trivialization condition** — i.e., just take the quotient set-theoretically? The quotient might fail to be locally trivial, hence not a fibre bundle in our sense. The smoothness and local triviality of the associated bundle are *theorems* (see [[Thm - Associated-Bundle Construction Yields a Bundle]]), not parts of the definition; they follow from the bundle structure of $P$.

---

# The Definition

Let $\pi_P : P \to M$ be a principal $G$-bundle, and let $G$ act smoothly from the left on a smooth manifold $F$ via $G \times F \to F$, $(g, y) \mapsto g \cdot y$. The **associated bundle** $P \times_G F \to M$ is defined as follows:

- **Total space:** $P \times_G F = (P \times F) / G$, where $G$ acts on $P \times F$ on the right by
$$(u, y) \cdot g = (u \cdot g, g^{-1} \cdot y).$$
Equivalence classes are denoted $[u, y]$.

- **Projection:** $P \times_G F \to M$ sends $[u, y] \mapsto \pi_P(u)$. (Well-defined because $\pi_P(u \cdot g) = \pi_P(u)$.)

- **Fibre:** The fibre over $p \in M$ is diffeomorphic to $F$ via $[u_0, y] \mapsto y$ for any chosen $u_0 \in \pi_P^{-1}(p)$.

- **Local trivializations:** Inherited from local trivializations of $P$. If $\Phi_P : \pi_P^{-1}(U) \to U \times G$ is a trivialization of $P$, the induced trivialization of $P \times_G F$ over $U$ is $[u, y] \mapsto (\pi_P(u), \mathrm{pr}_2(\Phi_P(u)) \cdot y)$.

- **Transition functions:** The transition functions of $P \times_G F$ are obtained from those of $P$ by composing with the action: $c^{F}_{\alpha\beta}(p) = (y \mapsto c^P_{\alpha\beta}(p) \cdot y)$, valued in $\mathrm{Diff}(F)$ (and inside the image of $G \to \mathrm{Diff}(F)$).

The associated bundle is a smooth fibre bundle over $M$ with typical fibre $F$ and structure group $G$ acting on $F$ as specified. See [[Thm - Associated-Bundle Construction Yields a Bundle]] for the verification.

**Special cases:**

- **Associated vector bundle**: $F = V$ a vector space, $G \to \mathrm{GL}(V)$ a representation. Then $P \times_G V$ is a vector bundle.
- **Associated sphere bundle**: $F = S^{k-1}$ with the orthogonal action when $G \leq \mathrm{O}(k)$.
- **Adjoint bundle**: $F = \mathfrak{g}$ (Lie algebra of $G$), action by adjoint representation. Then $\mathrm{Ad}(P) = P \times_G \mathfrak{g}$. Sections are the infinitesimal gauge transformations.

---

# Categorical Definition

The associated-bundle construction is a **functor** from the category of $G$-spaces (smooth manifolds with smooth left $G$-action and $G$-equivariant maps) to the category of fibre bundles over $M$ with structure group $G$:
$$P \times_G - : G\text{-Mfd} \to \text{Bun}(M, G), \qquad F \mapsto P \times_G F.$$
This functor is the *base change* along the principal bundle $P$. It has the following universal property: a smooth section of $P \times_G F$ is the same data as a $G$-equivariant smooth map $P \to F$:
$$\Gamma(P \times_G F) = \mathrm{Map}_G(P, F).$$
The equivalence sends a section $s : M \to P \times_G F$ to the equivariant map $\tilde s : P \to F$, $u \mapsto y$ where $s(\pi(u)) = [u, y]$. Equivariance: $\tilde s(u \cdot g) = g^{-1} \tilde s(u)$.

For vector bundles, this categorical viewpoint is especially clean: the category of representations of $G$ is the category of vector bundles associated to a fixed principal $G$-bundle $P$, and the construction is the **induction functor** from $\mathrm{Rep}(G)$ to vector bundles. Tensor products of representations correspond to tensor products of associated bundles, direct sums to direct sums, dual representations to dual bundles. This is the algebraic-categorical reason that all tensor / dual / symmetric / exterior power constructions on vector bundles can be done at the level of representations of $\mathrm{GL}(k)$.

---

# Relate to Other Fields / Compression

The associated-bundle construction is **the same as the induced representation in group theory, geometrized**. Given a subgroup $H \leq G$ and an $H$-representation $V$, the induced representation $\mathrm{Ind}_H^G V$ on $G \times_H V$ is the algebraic shadow of the associated bundle of the principal $H$-bundle $H \to G \to G/H$: it produces a vector bundle over $G/H$ whose fibre is $V$, by exactly the diagonal-quotient recipe.

The associated-bundle construction is the **fundamental example of a quotient construction in the category of $G$-spaces**: given a $G$-space $X$ with a free $G$-action and a $G$-space $Y$, the quotient $X \times_G Y$ is the geometric realization of "$X$ in families parametrized by $X/G$, with fibre $Y$ at each parameter, and the original $G$-symmetry quotiented out". This pattern recurs throughout equivariant geometry: in algebraic geometry, $X \times_G Y$ shows up as the GIT quotient with character; in symplectic geometry, as the symplectic reduction. The associated-bundle is the simplest instance.

**True name:** the associated bundle is **the bundle of $G$-equivariant fields on the principal bundle**. Operationally: to specify an element of $P \times_G F$, give a $G$-equivariant map $\tilde s : P \to F$, with the section property automatic. This converts the bundle theory of $P \times_G F$ into the equivariant theory on $P$, where everything is globally defined.

---

# Examples / Corollaries

**Is an instance: the original vector bundle $E$ from its frame bundle.** $E = \mathrm{Fr}(E) \times_{\mathrm{GL}(k, \mathbb{R})} \mathbb{R}^k$ with $\mathrm{GL}(k)$ acting on $\mathbb{R}^k$ by matrix multiplication. This is the prototype example and the source of the universal-object characterization.

**Is an instance: the dual vector bundle $E^*$ from $\mathrm{Fr}(E)$.** $E^* = \mathrm{Fr}(E) \times_{\mathrm{GL}(k, \mathbb{R})} (\mathbb{R}^k)^*$ with $\mathrm{GL}(k)$ acting on $(\mathbb{R}^k)^*$ by $g \cdot \xi = \xi \circ g^{-1}$ (the contragredient/inverse-transpose representation). This is why covectors transform "oppositely" to vectors.

**Is an instance: the tensor bundle $\otimes^r E \otimes \otimes^s E^*$.** From $\mathrm{Fr}(E)$ with the tensor representation. All tensor bundles, including the bundles of $p$-forms and symmetric tensors, are built this way.

**Is an instance: the unit sphere bundle $T_0 M$ as $\mathrm{Fr}^{\mathrm{SO}}(TM) \times_{\mathrm{SO}(n)} S^{n-1}$.** With $\mathrm{SO}(n)$ acting on $S^{n-1} \subset \mathbb{R}^n$ as a subset of the linear action.

**Is an instance: the adjoint bundle $\mathrm{Ad}(P) = P \times_G \mathfrak{g}$.** With $G$ acting on $\mathfrak{g}$ via the adjoint representation $\mathrm{Ad}$. Sections of $\mathrm{Ad}(P)$ are infinitesimal gauge transformations; the gauge group $\mathcal{G}$ is the corresponding $G$-bundle $P \times_G G$ with conjugation action.

**Is an instance: the Möbius bundle as an associated bundle of the double cover.** The connected double cover $S^1 \to S^1$ is a principal $\mathbb{Z}/2$-bundle; $\mathbb{Z}/2$ acts on $\mathbb{R}$ by sign, and the associated bundle is the Möbius line bundle $S^1 \times_{\mathbb{Z}/2} \mathbb{R}$. See [[Ex - The Möbius Strip as an Associated Bundle to a Double Cover]].

**Is NOT an instance: a bundle without a structure-group action on its fibre.** Strictly speaking, every fibre bundle is *some* associated bundle (with the structure group acting), but if the action of the structure group on the fibre is trivial, the associated bundle reduces to the product $M \times F$ — not a useful construction in that case.

**Corollary (sections of $P \times_G F$ correspond bijectively to $G$-equivariant maps $P \to F$).** $s : M \to P \times_G F \leftrightarrow \tilde s : P \to F$ with $\tilde s(u \cdot g) = g^{-1} \tilde s(u)$. Operationally: do all computations with sections on the principal bundle as equivariant maps; everything else descends.

**Corollary (the bundle $P \times_G F$ inherits a connection from any connection on $P$).** A principal connection on $P$ — a $\mathfrak{g}$-valued 1-form $\omega$ on $P$ — induces a covariant derivative on $P \times_G F$ via the equivariant-map identification. This is the unifying mechanism by which connection theory descends from the principal bundle to all associated bundles. Developed in [[Gauge Theory III — Connections in Principal and Associated Bundles]].

**Corollary (associated-bundle is functorial in $F$).** A $G$-equivariant map $F \to F'$ induces a bundle map $P \times_G F \to P \times_G F'$ over $M$.

**Calibration check.** Verify (i) $E \cong \mathrm{Fr}(E) \times_{\mathrm{GL}(k)} \mathbb{R}^k$ by writing down the explicit isomorphism (frame + components $\leftrightarrow$ vector); (ii) the diagonal-quotient identification with the inverse $(u \cdot g, g^{-1} \cdot y)$ is needed to make the construction well-defined; (iii) the section of $P \times_G F$ corresponding to a global frame of $P$ and a constant $y_0 \in F^G$ is the constant section $y_0$.

---

# Unlocked by This

> [!tip] Functor from Representations to Bundles *(from Geometric Representation Theory)*
> For a fixed principal $G$-bundle $P$, the associated-bundle construction is a functor $\mathrm{Rep}(G) \to \text{VectBun}(M)$, $V \mapsto P \times_G V$, which is exact and intertwines tensor product, direct sum, dual, symmetric/exterior power. This is the bridge between Lie-group representation theory and vector-bundle geometry: every representation-theoretic operation has a bundle-theoretic counterpart. In gauge theory, the matter fields are sections of $P \times_G V$ for various representations $V$ of the gauge group $G$.

> [!tip] Induced Connection on Associated Bundles *(from Gauge Theory III)*
> Every principal connection on $P$ induces a covariant derivative $\nabla$ on every associated bundle $P \times_G F$, compatible with the inclusion-of-$G$-actions. For vector bundles this gives the familiar $\nabla$; for the adjoint bundle, $\nabla^{\mathrm{ad}}$ is what acts on infinitesimal gauge transformations. The systematic theory of induced connections is the bridge between principal-bundle and vector-bundle gauge theory.

> [!tip] Adjoint Bundle and the Gauge Algebra *(from Yang–Mills Theory)*
> The adjoint bundle $\mathrm{Ad}(P) = P \times_G \mathfrak{g}$ has Lie-algebra-valued fibres, and the space of sections $\Gamma(\mathrm{Ad}\, P)$ is the **Lie algebra of the gauge group $\mathcal{G}$**. Infinitesimal gauge transformations are sections of $\mathrm{Ad}\,P$, and the Yang–Mills equations $d_A \star F = 0$ have $F \in \Omega^2(M; \mathrm{Ad}\,P)$, with the covariant derivative $d_A$ acting on adjoint-valued forms. See [[Gauge Theory IV — Yang–Mills Fields and Instantons]].
