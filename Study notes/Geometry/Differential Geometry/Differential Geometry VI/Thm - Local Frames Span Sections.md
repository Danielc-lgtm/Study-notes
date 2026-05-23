---
type: theorem
subject: differential-geometry
prereqs:
  - "Def - Vector Bundle"
  - "Def - Section of a Vector Bundle"
  - "Def - Local Frame"
  - "Def - Free Module"
tags: [geometry, differential-geometry, sections, frames]
---

# Notation

$\pi : E \to M$ is a smooth rank-$k$ vector bundle. $(\sigma_1, \dots, \sigma_k)$ is a smooth local frame for $E$ over an open set $U \subseteq M$, in the sense of [[Def - Local Frame]]. Every $\tau \in \Gamma(U, E)$ — a smooth local section — has a unique expression $\tau = f^i \sigma_i$ for smooth functions $f^i \in C^\infty(U)$. The space of smooth local sections over $U$, denoted $\Gamma(U, E)$, is a $C^\infty(U)$-module.

---

# Statement

> **Theorem ([[Def - Local Frame|Local Frames]] Span Sections).** Let $\pi : E \to M$ be a smooth vector bundle of rank $k$, and let $(\sigma_1, \dots, \sigma_k)$ be a smooth local frame for $E$ over an open set $U \subseteq M$. Then every smooth local section $\tau \in \Gamma(U, E)$ has a unique expression
> $$\tau = f^i \sigma_i = \sum_{i=1}^{k} f^i \sigma_i$$
> for smooth functions $f^1, \dots, f^k \in C^\infty(U)$, called the **component functions of $\tau$ in the frame** $(\sigma_i)$. Conversely, every $k$-tuple of smooth functions on $U$ defines a smooth local section by this formula. Equivalently, $\Gamma(U, E)$ is a free $C^\infty(U)$-module of rank $k$, with basis $(\sigma_1, \dots, \sigma_k)$.

---

# Motivation

This theorem says, in one sentence: **a local frame realises the space of smooth sections of $E$ over $U$ as a free $C^\infty(U)$-module of rank $k$**. The consequence is that every concrete computation with sections, over a domain where a frame is available, reduces to a computation with $k$-tuples of smooth functions — ordinary multivariable calculus. The theorem is the bridge between the abstract bundle structure and the concrete arithmetic of components.

The theorem is implicit every time one writes a vector field as $X = X^i \partial/\partial x^i$ or a 1-form as $\omega = \omega_i \, dx^i$. The coordinate frame is the local frame; the coefficients $X^i$ or $\omega_i$ are the component functions; their smoothness is exactly what the theorem asserts. Without the theorem, the validity of these coordinate expressions would require proof every time.

The deeper reason the theorem matters is that it makes **sections behave like vectors over the [[Def - Ring|ring]] $C^\infty(U)$**. In linear algebra, a vector in an $n$-dimensional space has unique coordinates in any basis, with smooth functions of the point playing no role. The bundle version replaces "scalars from $\mathbb{R}$" with "scalars from $C^\infty(U)$", and the theorem says the analog of "every vector has unique coordinates" holds. This is the foundation of the **tensoriality criterion** for bundle [[Def - Homomorphism|homomorphisms]] ([[Def - Bundle Homomorphism]]): a map of sections that is $C^\infty(M)$-linear comes from a bundle homomorphism, while a $C^\infty(M)$-nonlinear map (like the Lie derivative) does not.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis is "a smooth local frame on $U$". This data is automatically available whenever a local trivialization is available, which is everywhere in a vector bundle. Sources of frame-availability include:

The most common source is **a local trivialization $\Phi : \pi^{-1}(U) \to U \times \mathbb{R}^k$**. The standard basis $e_1, \dots, e_k$ of $\mathbb{R}^k$ pulls back through $\Phi^{-1}$ to give the local sections $\sigma_i(p) := \Phi^{-1}(p, e_i)$, which form a smooth local frame. Every local trivialization yields a frame, and the theorem then applies. This source is automatic — wherever you have a bundle, you have a frame, and the theorem follows.

A second source is **a chart $(U, x^i)$ on the base $M$ for the tangent or cotangent bundle**. The coordinate frame $(\partial/\partial x^i)$ is a smooth local frame for $TM$ over $U$; the dual coordinate coframe $(dx^j)$ is a smooth local frame for $T^*M$ over $U$. So any computation in a chart automatically invokes the theorem to express vector fields and 1-forms with smooth components.

A third source is **an extension of $k$ pointwise linearly independent vectors at a single point**. Given $v_1, \dots, v_k \in E_p$ linearly independent, the completion lemma ([[Def - Local Frame|completion of partial frames]]) extends these to a smooth local frame in some neighborhood of $p$. The theorem then applies on this neighborhood. This source is useful for constructing frames with prescribed initial data.

A fourth source is **an arbitrary nowhere-vanishing local section on a rank-$1$ bundle**. For a line bundle, a single nowhere-vanishing section is a local frame, and the theorem says every section is a smooth-function multiple. So nowhere-vanishing sections on line bundles give very simple component representations.

**Targets (Output Amplification)**

The conclusion is "every section has unique smooth components in the frame". Combined with one further hypothesis, this gives structural consequences.

The first combination is **theorem plus a bundle homomorphism gives a matrix representation**. Given a bundle homomorphism $F : E \to E'$ over $M$ and local frames $(\sigma_i)$ for $E$, $(\sigma'_j)$ for $E'$, $F$ has a unique matrix representation $F(\sigma_i) = A^j_i \sigma'_j$ for smooth functions $A^j_i \in C^\infty(U)$. So bundle homomorphisms become smooth-matrix-valued functions on the frame's domain, and bundle computations reduce to matrix calculus.

A second combination is **theorem plus a $C^\infty(M)$-linear map on sections gives a bundle homomorphism**. The bundle homomorphism characterization lemma says: a $C^\infty(M)$-linear map $\Gamma(E) \to \Gamma(E')$ that respects smoothness arises from a bundle homomorphism. The proof uses local frames: in a frame, the $C^\infty(M)$-linearity forces a matrix representation, and the matrix-valued function is the local form of the bundle homomorphism.

A third combination is **theorem plus a partition of unity gives global sections from local sections**. Given a smooth section locally over each $U_\alpha$ and a partition of unity $\{\rho_\alpha\}$ subordinate to $\{U_\alpha\}$, the sum $\tau := \sum_\alpha \rho_\alpha \tau_\alpha$ is a smooth global section. The theorem applied to each chart gives the local smoothness; the partition of unity globalizes it.

A fourth combination is **theorem plus the Whitney embedding theorem makes $\Gamma(E)$ finitely generated**. For compact $M$, the Whitney embedding theorem provides a finite cover of $M$ by trivializing opens; the theorem then realises $\Gamma(E)$ as a finitely generated projective $C^\infty(M)$-module. This is the input to the Serre–Swan theorem.

---

# Why Is It True

The intuition is direct: **a frame at every point provides a basis of each fibre, and a smooth section's value at each point has unique coordinates in that basis — the key is that "smooth in $p$" follows from "smooth section" plus "smooth frame", because the coordinates are extracted by a smooth procedure**.

**The one-line mechanism summary: the components $f^i$ of $\tau$ in the frame $(\sigma_i)$ are the pointwise dual-basis evaluations, smooth in $p$ because both the dual basis and the section are smooth in $p$.**

More precisely: at each $p \in U$, the values $\sigma_1(p), \dots, \sigma_k(p)$ form a basis of $E_p$, so the value $\tau(p) \in E_p$ has unique coordinates $f^1(p), \dots, f^k(p) \in \mathbb{R}$ in this basis. Existence and uniqueness of the components *pointwise* is the standard finite-dimensional-linear-algebra fact about bases.

The substantive content is **smoothness of the functions $p \mapsto f^i(p)$**. In a local trivialization $\Phi : \pi^{-1}(U) \to U \times \mathbb{R}^k$, the frame $(\sigma_i)$ corresponds to a smooth $\mathrm{GL}(k, \mathbb{R})$-valued function $A : U \to \mathrm{GL}(k, \mathbb{R})$, namely $\Phi \circ \sigma_i (p) = (p, A(p) e_i)$. The section $\tau$ corresponds to a smooth function $\tilde\tau : U \to \mathbb{R}^k$, namely $\Phi \circ \tau(p) = (p, \tilde\tau(p))$. The components of $\tau$ in the frame are then $f^i(p) = (A(p)^{-1} \tilde\tau(p))^i$ — smooth in $p$ because $A^{-1}$ is smooth (matrix inversion is smooth on $\mathrm{GL}(k, \mathbb{R})$), $\tilde\tau$ is smooth, and the matrix product is smooth.

The converse — every smooth $k$-tuple gives a smooth section — is the easier direction: given $f^i \in C^\infty(U)$, the assignment $p \mapsto f^i(p) \sigma_i(p)$ is smooth because both $f^i$ and $\sigma_i$ are smooth, and the fibrewise linear combination is smooth (linear combination is smooth on $\mathbb{R}^k$).

So the theorem reduces to (a) pointwise basis-coordinates exist uniquely by linear algebra, and (b) the assignment "section ↦ components" is smooth by the smoothness of matrix inversion.

---

# What Makes This Hard

The substantive technical step is **proving smoothness of the components $f^i$**, which requires using a local trivialization and the smoothness of matrix inversion on $\mathrm{GL}(k, \mathbb{R})$. Beginners often write down the unique pointwise components and skip the smoothness step; this is the gap that must be filled. The matrix-inversion-is-smooth fact is the key ingredient, and it is a non-trivial bit of multivariable calculus (Cramer's rule plus the smoothness of the determinant).

A common confusion is between **pointwise linear independence** and **$C^\infty(U)$-module linear independence**. A frame's pointwise linear independence is strictly stronger than its module linear independence, and the theorem genuinely needs the pointwise condition. The non-example in [[Def - Local Frame]] (sections $\sigma_1 = (x, 0)$ and $\sigma_2 = (0, 1)$ on $\mathbb{R}$ with $E = \mathbb{R}^2$) shows that module linear independence can hold without pointwise linear independence, and the theorem would fail in such a case.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Use a local trivialization to convert the abstract bundle into a product $U \times \mathbb{R}^k$. The frame corresponds to a smooth $\mathrm{GL}(k, \mathbb{R})$-valued matrix function on $U$, and the section corresponds to a smooth $\mathbb{R}^k$-valued function. The components are the inverse-matrix-times-vector, smooth by smoothness of matrix inversion.

**Subgoal decomposition:**

1. **Pointwise uniqueness of components.** Show that at each $p \in U$, $\tau(p)$ has unique coordinates in the basis $(\sigma_1(p), \dots, \sigma_k(p))$ of $E_p$.
   - *Hint:* Standard linear algebra: every basis of a finite-dimensional vector space gives unique coordinates.
   - *Why needed:* Establishes the pointwise existence and uniqueness of the components.

2. **Convert to a local trivialization.** Pass to a local trivialization $\Phi : \pi^{-1}(U) \to U \times \mathbb{R}^k$. The frame becomes a smooth $\mathrm{GL}(k, \mathbb{R})$-valued matrix $A(p)$; the section becomes a smooth $\mathbb{R}^k$-valued function $\tilde\tau(p)$.
   - *Hint:* Local trivializations always exist (after possibly shrinking $U$); frame and section both become coordinate-tuples.
   - *Why needed:* This is the bridge to multivariable calculus.

3. **Smoothness of inversion.** Show that the matrix inverse $A(p) \mapsto A(p)^{-1}$ is smooth on $\mathrm{GL}(k, \mathbb{R})$.
   - *Hint:* Cramer's rule: $A^{-1} = \mathrm{adj}(A) / \det(A)$, with adjugate polynomial in entries and determinant polynomial nonzero.
   - *Why needed:* This is what makes the components $f^i$ smooth.

4. **Smoothness of components.** Compute $f^i(p) = (A(p)^{-1} \tilde\tau(p))^i$. Since $A^{-1}$ and $\tilde\tau$ are smooth, the components are smooth.
   - *Hint:* Matrix-vector product of smooth functions is smooth.
   - *Why needed:* This completes the existence side.

5. **Converse: smooth tuples give smooth sections.** Given $f^i \in C^\infty(U)$, the assignment $p \mapsto f^i(p) \sigma_i(p)$ is smooth.
   - *Hint:* In the trivialization, this is $(p, f^i(p) A(p) e_i) = (p, A(p) (f^1, \dots, f^k)^T(p))$ — smooth.
   - *Why needed:* This establishes the bijection between $k$-tuples and sections.

---

# Lemma Decomposition

> [!note]- Lemma 1: Pointwise unique decomposition
> **Statement:** For each $p \in U$, $\tau(p)$ has a unique expression $\tau(p) = f^i(p) \sigma_i(p)$ for scalars $f^i(p) \in \mathbb{R}$.
>
> **Hint:** This is the standard fact that bases of finite-dimensional vector spaces give unique coordinates.
>
> **Why needed:** Pointwise existence and uniqueness of the components.
>
> > [!note]- Full proof
> > By hypothesis $(\sigma_1(p), \dots, \sigma_k(p))$ is a basis of $E_p$. Every element of $E_p$ has a unique expression as a linear combination of the basis elements. Applied to $\tau(p) \in E_p$, this gives unique scalars $f^i(p)$ with $\tau(p) = f^i(p) \sigma_i(p)$.

> [!note]- Lemma 2: Frame as smooth matrix in trivialization
> **Statement:** In a smooth local trivialization $\Phi : \pi^{-1}(U) \to U \times \mathbb{R}^k$ (possibly after shrinking $U$), the frame $(\sigma_i)$ corresponds to a smooth $\mathrm{GL}(k, \mathbb{R})$-valued function $A : U \to \mathrm{GL}(k, \mathbb{R})$.
>
> **Hint:** $\Phi(\sigma_i(p)) = (p, A(p) e_i)$ for the $i$-th column of $A(p)$.
>
> **Why needed:** Converts the frame data to a matrix-valued smooth function.
>
> > [!note]- Full proof
> > For each $i$, $\sigma_i : U \to E$ is smooth, and $\Phi \circ \sigma_i : U \to U \times \mathbb{R}^k$ is smooth; the second component is a smooth $\mathbb{R}^k$-valued function, which we call the $i$-th column of $A : U \to M_{k \times k}(\mathbb{R})$. So $A$ is a smooth matrix-valued function. At each $p$, the columns of $A(p)$ are $\Phi(\sigma_1(p)), \dots, \Phi(\sigma_k(p))$, which are linearly independent (the frame condition transferred through the linear-isomorphism trivialization); so $A(p) \in \mathrm{GL}(k, \mathbb{R})$ at every $p$, and $A : U \to \mathrm{GL}(k, \mathbb{R})$.

> [!note]- Lemma 3: Matrix inversion is smooth on $\mathrm{GL}(k, \mathbb{R})$
> **Statement:** The map $A \mapsto A^{-1}$ from $\mathrm{GL}(k, \mathbb{R})$ to itself is smooth.
>
> **Hint:** Cramer's rule expresses $A^{-1}$ as a polynomial in the entries of $A$ divided by $\det(A)$, which is nonzero on $\mathrm{GL}(k, \mathbb{R})$.
>
> **Why needed:** This is what allows extracting smooth components from a smooth section in a smooth frame.
>
> > [!note]- Full proof
> > By Cramer's rule, $(A^{-1})_{ij} = (-1)^{i+j} M_{ji}(A) / \det(A)$, where $M_{ji}(A)$ is the $(j, i)$-minor (determinant of the matrix obtained by removing row $j$ and column $i$ from $A$). Both $M_{ji}(A)$ and $\det(A)$ are polynomial functions of the entries of $A$, hence smooth. The quotient is smooth where the denominator $\det(A)$ is nonzero, which is exactly on $\mathrm{GL}(k, \mathbb{R})$. So every entry of $A^{-1}$ is a smooth function of the entries of $A$, and the map $A \mapsto A^{-1}$ is smooth.

> [!note]- Lemma 4: Components are smooth
> **Statement:** The component functions $f^i(p)$ of a smooth section $\tau$ in a smooth frame $(\sigma_i)$ are smooth.
>
> **Hint:** In a local trivialization, $\tau$ becomes a smooth $\mathbb{R}^k$-valued function $\tilde\tau$, and $f^i$ are the entries of $A^{-1} \tilde\tau$, smooth by Lemma 3.
>
> **Why needed:** This is the existence side of the theorem.
>
> > [!note]- Full proof
> > In a local trivialization $\Phi$, $\Phi(\tau(p)) = (p, \tilde\tau(p))$ for a smooth $\tilde\tau : U \to \mathbb{R}^k$. The frame is a smooth $A : U \to \mathrm{GL}(k, \mathbb{R})$ by Lemma 2. The equation $\tau(p) = f^i(p) \sigma_i(p)$ transferred through $\Phi$ becomes $\tilde\tau(p) = f^i(p) A(p) e_i = A(p) (f^1(p), \dots, f^k(p))^T$, i.e., $\tilde\tau(p) = A(p) f(p)$. Solving: $f(p) = A(p)^{-1} \tilde\tau(p)$. By Lemma 3, $A^{-1}$ is smooth in $p$; $\tilde\tau$ is smooth; the matrix-vector product is smooth. So each $f^i$ is smooth on $U$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — Pointwise uniqueness.** By Lemma 1, for each $p \in U$ there exist unique scalars $f^i(p) \in \mathbb{R}$ with $\tau(p) = f^i(p) \sigma_i(p)$. This defines functions $f^i : U \to \mathbb{R}$.
>
> **Step 1 — Smoothness via trivialization.** Choose a smooth local trivialization $\Phi$ on a neighborhood $V \subseteq U$ of an arbitrary point $p_0 \in U$ (shrinking $U$ to $V$ if necessary; smoothness is a local property so we may work on $V$). By Lemma 2, the frame becomes a smooth $A : V \to \mathrm{GL}(k, \mathbb{R})$. By smoothness of $\tau$, $\Phi \circ \tau : V \to V \times \mathbb{R}^k$ is smooth with second component a smooth $\tilde\tau : V \to \mathbb{R}^k$.
>
> **Step 2 — Solve for components.** The decomposition $\tau = f^i \sigma_i$ in the trivialization is $\tilde\tau = A f$, where $f = (f^1, \dots, f^k)^T$. By Lemma 3, $A^{-1}$ is smooth, so $f = A^{-1} \tilde\tau$ is smooth on $V$. So each $f^i$ is smooth on $V$.
>
> **Step 3 — Patch to $U$.** Since smoothness is local and $p_0 \in U$ was arbitrary, each $f^i$ is smooth on $U$. By Lemma 4 explicitly: every $f^i \in C^\infty(U)$.
>
> **Step 4 — Converse.** Given $f^1, \dots, f^k \in C^\infty(U)$, define $\tau(p) := f^i(p) \sigma_i(p)$. In a local trivialization, $\Phi(\tau(p)) = (p, A(p) f(p))$, a smooth $V \times \mathbb{R}^k$-valued function. So $\tau$ is a smooth local section.
>
> **Step 5 — Free module of rank $k$.** The map $C^\infty(U)^k \to \Gamma(U, E)$, $(f^1, \dots, f^k) \mapsto f^i \sigma_i$, is bijective by Steps 0–4, and clearly $C^\infty(U)$-linear. So $\Gamma(U, E) \cong C^\infty(U)^k$ as $C^\infty(U)$-[[Def - Module|modules]] — i.e., $\Gamma(U, E)$ is a free $C^\infty(U)$-module of rank $k$ with basis $(\sigma_1, \dots, \sigma_k)$.
>
> $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Module theory: free vs projective modules.** The theorem says $\Gamma(U, E)$ is *free* of rank $k$ on a frame-admitting open $U$. But on a manifold $M$ where the bundle is not globally trivial, the global section module $\Gamma(M, E)$ is *projective* but not free. Use the Serre–Swan theorem to formalize this distinction, and compute $\Gamma(S^2, TS^2)$ as a non-free projective $C^\infty(S^2)$-module.

**Vector calculus: coordinate vector fields and 1-forms.** Apply the theorem to the tangent and cotangent bundles in a chart. Every vector field $X$ on the chart is uniquely $X = X^i \partial/\partial x^i$ for smooth components $X^i$; every 1-form $\omega$ is uniquely $\omega = \omega_j dx^j$ for smooth $\omega_j$. The smoothness of these coordinate expressions is exactly the theorem's content.

**Sheaf theory: locally free sheaves of rank $k$.** The theorem expresses the local triviality of the sheaf $\mathcal{E}(U) := \Gamma(U, E)$: locally on a frame-admitting open, it is $\mathcal{O}_M^k$, the free $\mathcal{O}_M$-module of rank $k$ (where $\mathcal{O}_M = C^\infty(M)$ for smooth manifolds). Locally free sheaves of rank $k$ on a manifold are precisely vector bundles of rank $k$.

**Gauge theory: components in a frame are the "physical" field values.** In gauge theory, sections of an associated vector bundle are fields (matter fields, Higgs fields, etc.). The components in a local frame are the "physical" field values that an observer reports; gauge transformations between frames change these components by smooth matrix actions. The theorem is what makes the component-based description of fields rigorous.

---

# Bridges

- **[[Def - Local Frame]] and [[Def - Local Trivialization]]** — The theorem is the operational consequence of the frame-trivialization equivalence: a frame *is* a trivialization, and the theorem says trivializations identify sections with vector-valued functions. The bridge is exact: $\Gamma(U, E) \cong C^\infty(U)^k$ when a frame (equivalently a trivialization) is available.

- **Serre–Swan theorem** *(from commutative algebra)* — The theorem is the local content of the Serre–Swan theorem, which globalises it: $\Gamma(M, E)$ is a finitely generated projective $C^\infty(M)$-module, locally free of rank $k$. The Serre–Swan theorem is an equivalence between smooth vector bundles over $M$ and projective $C^\infty(M)$-modules.

- **[[Def - Bundle Homomorphism]] and the tensoriality criterion** — A $C^\infty(M)$-linear map $\Gamma(E) \to \Gamma(E')$ comes from a bundle homomorphism over $M$ if and only if it respects the module structure pointwise. The theorem is the key step in the proof: in a local frame, the $C^\infty(M)$-linearity forces a matrix representation, and the matrix-valued function is the local form of the bundle homomorphism.

- **[[Thm - Coordinate Expression for df]]** — A special case of the theorem applied to $T^*M$ and the coordinate coframe $(dx^i)$: every 1-form has a unique expression $\omega = \omega_i \, dx^i$ for smooth $\omega_i$. The differential of a function $df$ is the special case with $\omega_i = \partial f / \partial x^i$.

---

# Unlocked by This

> [!tip] Tensoriality Criterion *(from this topic)*
> A map $\Gamma(E) \to \Gamma(E')$ of sections is **tensorial** — i.e., comes from a bundle homomorphism over $M$ — if and only if it is $C^\infty(M)$-linear. The theorem applied to the local-frame expansion shows that $C^\infty(M)$-linearity in components is equivalent to fibrewise linearity, which is the bundle-homomorphism condition. This is the cleanest criterion for distinguishing "tensors" from "differential operators".

> [!tip] Component Calculus on Manifolds *(from Tensor Calculus)*
> Once the theorem is in hand, every computation with vectors, covectors, tensors, and forms on a manifold reduces to computations with their components in a chosen local frame. The classical "index notation" of tensor calculus — $T^i{}_j$ with upper and lower indices for vector and covector slots — is exactly the component representation in a coordinate frame. This is the bridge from abstract differential geometry to the index-laden physics calculations of general relativity and gauge theory.

> [!tip] Connection Coefficients (Christoffel Symbols) *(from Riemannian Geometry)*
> Given a connection $\nabla$ on a bundle $E$ and a local frame $(\sigma_i)$, the **connection coefficients** $\Gamma^j_i = \omega^j_i$ are 1-forms defined by $\nabla \sigma_i = \omega^j_i \otimes \sigma_j$. The theorem ensures that in any frame, $\nabla$ is determined by the $\omega^j_i$ — smooth 1-forms with values in matrices — and the entire calculus of covariant derivatives reduces to computing with these connection coefficients. For the Levi-Civita connection on $TM$, the connection coefficients are the Christoffel symbols.
