---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Differential k-Form on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - Closed and Exact Forms"
  - "Def - Quotient Group"
tags: [geometry, differential-geometry, cohomology]
---

# Notation

$M$ is a smooth manifold. $\Omega^k(M)$ is the space of smooth $k$-forms on $M$, with $\Omega^0(M) = C^\infty(M)$ and $\Omega^k(M) = 0$ for $k < 0$ or $k > \dim M$. The exterior derivative $d : \Omega^k(M) \to \Omega^{k+1}(M)$ is the unique linear operator satisfying $d^2 = 0$, Leibniz on wedges, and agreeing with the differential of a function on $\Omega^0$ — see [[Def - Exterior Derivative on a Manifold]]. A $k$-form $\omega$ is **closed** if $d\omega = 0$ and **exact** if $\omega = d\eta$ for some $(k-1)$-form $\eta$, called a **primitive** of $\omega$ — see [[Def - Closed and Exact Forms]]. The full notation registry for this topic is on [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]].

---

# Axiom Motivation

What we are trying to invent is a numerical invariant of a smooth manifold that captures the "topological obstruction to integration." Here is the concrete picture that forces the definition.

A closed $1$-form $\omega$ on $\mathbb{R}^n$ is always a gradient, $\omega = df$ for some function $f$ — this is the [[Thm - The Poincaré Lemma|Poincaré lemma]] of `Multivariate Analysis IV`, and it says: on $\mathbb{R}^n$ closedness is enough for the existence of a global primitive. On the punctured plane $\mathbb{R}^2 \setminus \{0\}$ the situation is *different*: the angular form $d\theta = (-y\,dx + x\,dy)/(x^2 + y^2)$ is closed (you can check $d(d\theta) = 0$ pointwise), yet there is no global function $\theta$ on the punctured plane — going once around the origin the angle jumps by $2\pi$. So on this domain, closedness is *not* enough. The exactness has failed, and the failure is captured by a single number — the period $2\pi$ — that registers the single hole at the origin.

We want a definition that captures exactly this kind of obstruction. The desiderata are: (i) it should be zero when closed-implies-exact (so contractible domains have trivial cohomology); (ii) it should be non-trivial when closedness genuinely fails to imply exactness (so punctured spaces have something); (iii) it should be a vector space (so we can add and scale obstructions, and it should agree with the linear structure on forms); (iv) it should depend only on the *smooth structure* of $M$, not on auxiliary choices; and (v) it should be functorial — a smooth map between manifolds should induce a linear map between cohomologies, going the right way for a contravariant invariant.

The construction is forced by these demands. We want "closed forms modulo exact forms," because (i) and (ii) say the answer should be zero exactly when every closed form is exact. We need this to be a sensible quotient — exact forms must be closed — and that is precisely $d^2 = 0$. So the algebraic identity $d^2 = 0$, which we already had to build into the exterior derivative for it to be a "second-order derivative" with mixed-partials commuting, is the necessary preliminary that makes the quotient $\ker d / \mathrm{im}\,d$ even well-defined.

Why a quotient and not, say, the cokernel of $d$? Because we want to measure closed forms that fail to be exact, not exact forms that fail to be closed (there are none of the latter — $d^2 = 0$). The quotient $Z^k / B^k$ identifies two closed forms that differ by an exact form; this is the right equivalence because (i) exact forms integrate to zero over every closed cycle, by Stokes, and (ii) any two primitives of an exact form differ by an exact form themselves. So the equivalence "differ by an exact form" is precisely the right equivalence to make integration well-defined on cohomology classes, which we will see is the key to the de Rham theorem.

The choice of *real* coefficients deserves a sentence. We could in principle work with $\mathbb{Q}$ or $\mathbb{Z}$ coefficients (using rational or integer combinations of forms, suitably interpreted), but the de Rham complex is naturally a complex of real vector spaces — $\Omega^k(M)$ is a module over $C^\infty(M)$, which contains $\mathbb{R}$, and $d$ is $\mathbb{R}$-linear. So $H^k_{dR}(M)$ is born as an $\mathbb{R}$-vector space, and the de Rham theorem will identify it with $H^k_{\mathrm{sing}}(M; \mathbb{R})$ — real-coefficient singular cohomology. To recover integer or rational invariants, one descends through a separate theorem (the universal coefficient theorem) rather than building them into the de Rham construction.

What if we used a different complex, say only $C^k$ forms? The construction works for any $k \geq 1$ (with $d$ now mapping $C^k$ to $C^{k-1}$ forms), and a standard smoothing argument (using partitions of unity and convolution) shows the cohomology is independent of regularity above $C^1$. So restricting to $C^\infty$ is harmless — it gives the same answer and keeps the algebra clean. Going below $C^1$ does not make sense, because the exterior derivative would not be defined.

What if we used compactly supported forms? Then we get **compactly supported de Rham cohomology** $H^k_c(M)$, a related but distinct invariant. On compact manifolds the two agree; on noncompact ones they differ — for instance $H^n_c(\mathbb{R}^n) = \mathbb{R}$ while $H^n_{dR}(\mathbb{R}^n) = 0$. The compactly supported version satisfies Poincaré duality with the ordinary version, and both are useful; we develop only the ordinary one here.

In summary, the definition is forced by three things: $d^2 = 0$ (which makes the quotient sensible), the demand that the obstruction vanish on contractible domains (which makes "closed modulo exact" the right quotient), and the demand that the answer be a topological-strength invariant (which is delivered by the homotopy invariance theorem, building on the choice of quotient).

---

# The Definition

Let $M$ be a smooth manifold. For each integer $k \geq 0$, define:

- $Z^k(M) = \ker(d : \Omega^k(M) \to \Omega^{k+1}(M))$ — the space of **closed** $k$-forms.
- $B^k(M) = \mathrm{im}(d : \Omega^{k-1}(M) \to \Omega^k(M))$ — the space of **exact** $k$-forms (where $B^0(M) := 0$ by convention, since there are no $(-1)$-forms).

The identity $d^2 = 0$ implies $B^k(M) \subseteq Z^k(M)$. The **$k$-th de Rham cohomology group** (or **de Rham cohomology space**) of $M$ is the quotient real vector space

$$H^k_{dR}(M) \,:=\, Z^k(M) \,/\, B^k(M).$$

An element of $H^k_{dR}(M)$ is a **cohomology class** $[\omega]$, where $\omega \in Z^k(M)$, and $[\omega] = [\omega']$ iff $\omega - \omega' \in B^k(M)$, i.e. $\omega - \omega' = d\eta$ for some $\eta \in \Omega^{k-1}(M)$.

For a smooth map $F : M \to N$, the pullback $F^* : \Omega^k(N) \to \Omega^k(M)$ commutes with $d$ (i.e. $F^* \circ d = d \circ F^*$), so it carries $Z^k(N)$ to $Z^k(M)$ and $B^k(N)$ to $B^k(M)$. It therefore descends to an $\mathbb{R}$-linear map

$$F^* : H^k_{dR}(N) \to H^k_{dR}(M), \qquad F^*[\omega] := [F^*\omega].$$

This assignment is functorial: $(G \circ F)^* = F^* \circ G^*$ and $\mathrm{id}_M^* = \mathrm{id}_{H^k_{dR}(M)}$. The de Rham cohomology is thus a *contravariant functor* from the category of smooth manifolds to the category of real vector spaces.

---

# Categorical / Structural Definition

The de Rham cohomology fits into a triple categorical structure that is worth seeing all at once.

**As cohomology of a cochain complex.** A **cochain complex of $\mathbb{R}$-vector spaces** is a sequence $(C^k, d^k)_{k \geq 0}$ of vector spaces and linear maps $d^k : C^k \to C^{k+1}$ with $d^{k+1} \circ d^k = 0$. The **$k$-th cohomology** is the quotient $H^k(C^*) = \ker d^k / \mathrm{im}\,d^{k-1}$. The de Rham complex $(\Omega^k(M), d)$ is such a cochain complex, and $H^k_{dR}(M)$ is *literally* its cohomology in the algebraic sense. The same machinery applied to other cochain complexes — singular, Čech, Dolbeault, group, Lie algebra — produces the corresponding other cohomology theories, all built on the same quotient construction.

**As a contravariant functor.** $H^k_{dR}$ is a contravariant functor from the category $\mathbf{Mfd}$ of smooth manifolds (with smooth maps as morphisms) to the category $\mathbf{Vect}_\mathbb{R}$ of real vector spaces. Contravariance means $H^k_{dR}$ reverses the direction of morphisms — $F : M \to N$ induces $F^* : H^k_{dR}(N) \to H^k_{dR}(M)$ — and functoriality means it respects composition and identities. From this viewpoint, every property of $H^k_{dR}$ that holds for *every* manifold is a property of the functor; in particular homotopy invariance is a *natural isomorphism*, and Mayer–Vietoris is a *natural long exact sequence*. The graded sum $H^*_{dR}(-) = \bigoplus_k H^k_{dR}(-)$ becomes a contravariant functor to graded $\mathbb{R}$-algebras (with wedge product on cohomology making it a commutative graded algebra).

**As a quotient in the category of abelian groups (and of $\mathbb{R}$-vector spaces).** Each $Z^k(M)$ is an [[Def - Abelian Group|abelian group]] under form addition, and $B^k(M) \subseteq Z^k(M)$ is a (normal — every subgroup of an abelian group is normal) subgroup. The [[Def - Quotient Group|quotient group]] $Z^k(M) / B^k(M)$ inherits an abelian-group structure, and the $\mathbb{R}$-scalar multiplication on forms descends to give an $\mathbb{R}$-vector space structure. The quotient map $Z^k(M) \to H^k_{dR}(M)$ is a [[Def - Homomorphism|group homomorphism]] with [[Def - Kernel and Image|kernel]] $B^k(M)$ — by the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] this gives $H^k_{dR}(M) \cong Z^k(M) / B^k(M)$ canonically.

---

# Relate to Other Fields / Compression

**True name:** $H^k_{dR}(M)$ is the *vector space of integration-against-closed-form invariants*. The operational meaning, established by the de Rham theorem, is: a cohomology class is a recipe for assigning a number to every $k$-cycle (smooth closed $k$-submanifold or formal sum thereof) such that the number only depends on the homology class of the cycle. The recipe is "integrate this representative form." So $H^k_{dR}(M)$ is functionally the space of "things you can integrate against cycles." Whenever a problem starts "show that $\omega$ defines a non-trivial cohomology class," the operational route is to exhibit a cycle whose integral against $\omega$ is non-zero.

**Compression to group theory.** $H^k_{dR}(M)$ is the [[Def - Quotient Group|quotient group]] $Z^k / B^k$ where both $Z^k$ and $B^k$ are abelian groups under form addition, and the quotient is in the category of $\mathbb{R}$-vector spaces. The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] for vector spaces says any linear map $\varphi : Z^k(M) \to V$ vanishing on $B^k(M)$ factors uniquely through $H^k_{dR}(M)$; the integration map $\omega \mapsto (\text{cycle } c \mapsto \int_c \omega)$ is exactly such a map (since exact forms integrate to zero over cycles by Stokes), so it factors through $H^k_{dR}$ — and *this* factored map is the de Rham homomorphism whose isomorphism property is the de Rham theorem.

**Compression to homological algebra.** A general principle: given any **chain complex** $(C^*, d)$ in any abelian category, the **cohomology** is the graded sequence of quotients $H^k(C^*) = \ker d^k / \mathrm{im}\,d^{k-1}$, well-defined because $d^2 = 0$. de Rham cohomology is the specialization to the cochain complex of differential forms on a manifold. Singular cohomology is the specialization to a different cochain complex built from continuous simplices; Dolbeault cohomology is the specialization to the $(0, q)$-form complex with the $\bar\partial$ operator; sheaf cohomology generalizes all of these. From this perspective, the de Rham complex is "the complex you get when you have a smooth structure and use ordinary calculus."

**Compression to physics.** $H^k_{dR}(M)$ is the space of **conserved global topological charges** of "field configurations modulo gauge equivalence." For $k = 2$ on a $4$-manifold, $H^2_{dR}(M)$ classifies electromagnetic field configurations modulo gauge ($F = dA$ defines a class only up to $A \mapsto A + d\chi$); for $k = 1$ it parametrizes Aharonov–Bohm phases (line integrals of a closed but not exact $1$-form around a loop); for general $k$ it parametrizes higher-form gauge theories of the type appearing in string theory. The non-vanishing of a de Rham class is the topological obstruction to "trivializing the gauge."

---

# Examples / Corollaries

**Is an instance: $H^0_{dR}(M) = \mathbb{R}^{\#\text{components}}$.** A closed $0$-form is a smooth function $f$ with $df = 0$, equivalently $f$ locally constant — and on a connected component a locally constant function is just constant. So $Z^0(M) \cong \mathbb{R}^c$ where $c$ is the number of components. Since $B^0(M) = 0$ by convention (there are no $(-1)$-forms), $H^0_{dR}(M) = Z^0(M) \cong \mathbb{R}^c$. *Calibration:* $H^0_{dR}$ counts connected components, so $H^0_{dR}(\mathbb{R}^n) = \mathbb{R}$ ($\mathbb{R}^n$ is connected), $H^0_{dR}(S^n) = \mathbb{R}$ ($S^n$ is connected), $H^0_{dR}(\mathbb{R} \setminus \{0\}) = \mathbb{R}^2$ (two components).

**Is an instance: $H^k_{dR}(\mathbb{R}^n) = 0$ for $k \geq 1$.** The Euclidean Poincaré lemma says every closed form of degree $\geq 1$ on $\mathbb{R}^n$ (or on any star-shaped open subset) is exact. So $Z^k = B^k$ in those degrees, and the quotient is zero. This generalizes to contractible manifolds: $H^k_{dR}(M) = 0$ for $k \geq 1$ whenever $M$ is contractible, via homotopy invariance.

**Is an instance: $H^1_{dR}(S^1) = \mathbb{R}$.** The arc-length form $d\theta = (-y\,dx + x\,dy)/(x^2+y^2)$ restricts to a closed $1$-form on $S^1 \subset \mathbb{R}^2 \setminus \{0\}$ whose integral around $S^1$ is $2\pi \neq 0$. This implies $[d\theta] \neq 0$ in $H^1_{dR}(S^1)$, since exact forms have zero integral over closed cycles (by Stokes). The full computation $H^1_{dR}(S^1) = \mathbb{R}$ requires Mayer–Vietoris or homotopy theory, but the non-triviality is established by integration alone.

**Is an instance: $H^k_{dR}(T^n) = \mathbb{R}^{\binom{n}{k}}$.** The de Rham cohomology of the $n$-torus is generated by wedge products of the coordinate $1$-forms $d\theta^1, \dots, d\theta^n$ — the wedge $d\theta^{i_1} \wedge \cdots \wedge d\theta^{i_k}$ for each $k$-element subset is a basis. The dimension is $\binom{n}{k}$, the same as the Betti number, recovering the topology of the torus by smooth means. See [[Ex - The de Rham Cohomology of the Torus]].

**Is NOT an instance: arbitrary quotient of arbitrary subspaces.** It is tempting to think of "cohomology" as some general "kernel modulo image" construction. But the construction requires $d^2 = 0$ — otherwise the image of one differential need not be contained in the kernel of the next, and the quotient is ill-defined. So if you tried to define cohomology of the *de Rham complex with $d$ replaced by Lie derivative along a vector field*, you would fail: $\mathcal{L}_X^2 \neq 0$ in general, so $\mathrm{im}\,\mathcal{L}_X$ is not contained in $\ker \mathcal{L}_X$. This non-example probes the necessity of the algebraic compatibility $d^2 = 0$.

**Is NOT an instance: a quantity that distinguishes diffeomorphic manifolds.** Diffeomorphic manifolds have isomorphic de Rham cohomology (functoriality, with the isomorphism induced by the diffeomorphism). So $H^*_{dR}$ does *not* tell you anything that would distinguish "different smooth structures on the same topological manifold," nor anything beyond the homotopy type. In particular two homotopy equivalent but non-diffeomorphic manifolds (a phenomenon that exists in dimension $\geq 4$) have identical de Rham cohomology. This is a clean illustration of how strong an invariant homotopy type really is.

**Corollary (functoriality).** For any smooth maps $F : M \to N$ and $G : N \to P$, $(G \circ F)^* = F^* \circ G^* : H^*(P) \to H^*(M)$ and $\mathrm{id}_M^* = \mathrm{id}_{H^*(M)}$. In particular, a diffeomorphism induces an isomorphism on cohomology. *Calibration:* this is just the functoriality of pullback for forms together with the well-definedness of the induced map on quotients — a one-line check from the definitions.

**Corollary (additivity over disjoint unions).** If $M = \bigsqcup_\alpha M_\alpha$, then $H^k_{dR}(M) = \bigoplus_\alpha H^k_{dR}(M_\alpha)$. A form on a disjoint union is just a choice of form on each component, and the differential is component-wise.

**Calibration check.** If you have understood the definition you should be able to (i) verify that $H^0_{dR}(\{0, 1\}) = \mathbb{R}^2$ (a $0$-manifold with two points), (ii) state in one sentence why $d^2 = 0$ is the algebraic prerequisite for $H^k_{dR}$ to be well-defined, and (iii) explain why $H^k_{dR}(M)$ depends on no choice of Riemannian metric — only on the smooth structure.

---

# Unlocked by This

> [!tip] **Singular cohomology** *(from Algebraic Topology)*
> A purely topological cohomology theory $H^k(M; \mathbb{R})$ is defined for *any* topological space (not just manifolds) from formal sums of continuous simplices. The [[Thm - The de Rham Theorem (Statement)|de Rham theorem]] identifies $H^k_{dR}(M) \cong H^k(M; \mathbb{R})$ for smooth $M$, but the singular construction extends to spaces with no smooth structure — CW complexes, classifying spaces, infinite-dimensional spaces. The dimensions of singular cohomology are the **Betti numbers** $\beta_k$, and the alternating sum $\sum (-1)^k \beta_k$ is the **Euler characteristic**.

> [!tip] **Sheaf cohomology** *(from Algebraic Geometry and Complex Geometry)*
> The general construction "closed sections modulo exact sections of a resolution" generalizes to cohomology of any **sheaf** of abelian groups on a topological space. de Rham cohomology is sheaf cohomology of the constant sheaf $\mathbb{R}$; Dolbeault cohomology is sheaf cohomology of the holomorphic forms sheaf $\Omega^p$; singular cohomology with integer coefficients is sheaf cohomology of $\mathbb{Z}$. The unifying machine is the derived functor of "global sections."

> [!tip] **Spectral sequence** *(from Algebraic Topology and Homological Algebra)*
> When a manifold has a cover by more than two open sets, the naive Mayer–Vietoris fails — but a refinement, the **Čech-to-de-Rham spectral sequence**, computes $H^*_{dR}(M)$ from the cohomology of all finite intersections of cover members. Every modern cohomology computation in algebraic geometry and topology runs through some spectral sequence; the de Rham case is the prototype.

> [!tip] **Hodge theory** *(from Riemannian and Complex Geometry)*
> On a compact oriented Riemannian manifold, the de Rham complex acquires an adjoint $d^*$ via the metric, and the Hodge Laplacian $\Delta = dd^* + d^*d$ provides a canonical orthogonal decomposition $\Omega^k = \ker\Delta \oplus \mathrm{im}\,d \oplus \mathrm{im}\,d^*$. The cohomology $H^k_{dR}(M)$ is then *isomorphic* to the space of harmonic forms $\ker\Delta$, picking out a *canonical* representative in each class — the harmonic form. This is the bridge from cohomology to elliptic PDE.

> [!tip] **Characteristic classes** *(from Differential and Algebraic Topology)*
> To a vector bundle or principal bundle over $M$ one associates de Rham cohomology classes — the **Chern classes**, **Pontryagin classes**, **Euler class** — built from the curvature of a connection. These classes are bundle invariants that detect non-triviality (e.g. the Euler class of $TS^2$ has $\int_{S^2} e = 2$, certifying that $TS^2$ is not trivial — the hairy ball theorem). The cohomological viewpoint of bundles is the foundation of Chern–Weil theory and gauge field topology.
