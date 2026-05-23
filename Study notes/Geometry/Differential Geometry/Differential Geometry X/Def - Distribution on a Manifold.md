---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - The Tangent Bundle"
  - "Def - Vector Bundle"
  - "Def - Subbundle"
  - "Def - Vector Field on a Manifold"
tags: [geometry, differential-geometry, frobenius]
---

# Notation

$M$ is a smooth $n$-manifold; $TM$ is its [[Def - The Tangent Bundle|tangent bundle]], with $T_pM$ the tangent space at $p$. A **rank-$k$ distribution** on $M$ is denoted $D$; its fiber at $p$ is $D_p \subseteq T_pM$, a $k$-dimensional subspace. The space of smooth (local or global) sections of $D$ — vector fields whose values at every point lie in $D$ — is denoted $\Gamma(D)$ or $\mathfrak{X}(D)$. The full notation registry is on [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius]].

The term "distribution" is overloaded — in functional analysis it refers to generalized functions, in geometry to plane fields. The two are unrelated; we always mean the geometric notion here. When precision matters one writes "tangent distribution," "$k$-plane field," or "tangent subbundle."

---

# Axiom Motivation

What we want to invent is a notion of "smoothly varying $k$-plane field on $M$" — the higher-rank generalization of a smooth nowhere-vanishing vector field. The motivating problem is: we know what an integral *curve* of a vector field is, and we know they always exist by [[Thm - Existence and Uniqueness of Integral Curves|ODE theory]]; we want to ask whether there are higher-dimensional analogues — *integral submanifolds* of [[Def - Dimension|dimension]] $k$ tangent to a chosen $k$-plane field at every point.

A first-pass definition: assign to each $p \in M$ a $k$-dimensional subspace $D_p \subseteq T_pM$. This is a *set-theoretic* assignment; it has no smoothness. To make sense of "smooth $k$-plane field" we need to add a regularity condition.

The desiderata are: (i) $D$ should be a $k$-dimensional object globally, like a vector bundle would be — so that one can talk about its sections, frames, and dual; (ii) smoothness should be inherited from the smoothness of the ambient $TM$, so we can use calculus; (iii) the definition should be local — checkable in coordinate charts — but well-defined globally; (iv) we want flexibility to define $D$ either by spanning vector fields (a "frame approach") or by annihilating $1$-forms (a "constraint approach"), and these two should be equivalent.

These force the definition: $D$ is a [[Def - Subbundle|smooth subbundle]] of $TM$. Here is why. A **vector bundle** is by definition a locally trivial family of vector spaces, and a smooth [[Def - Subbundle|subbundle]] $D \subseteq TM$ inherits the local-triviality property: in a neighborhood of every $p$ there is a smooth local frame $X_1, \dots, X_k$ for $D$ — smooth vector fields on a neighborhood whose values $X_1|_q, \dots, X_k|_q$ are a basis for $D_q$ at every nearby $q$. This is exactly desideratum (i). The smoothness of the frame is desideratum (ii). The local-frame description is checkable in coordinates: $D$ is smooth iff such a local frame exists in a chart around each point — desideratum (iii). And the equivalence between "frame description" and "constraint description" — that there exist annihilating $1$-forms $\omega^1, \dots, \omega^{n-k}$ with $D_q = \bigcap_i \ker \omega^i_q$ — is a consequence of the local-frame criterion applied to the dual bundle (desideratum iv).

A weaker definition — "for each $p$, a $k$-dimensional subspace, with no smoothness requirement" — would let pathological examples in (a distribution that jumps abruptly between charts, say). A stronger definition — "$D$ is the kernel of a globally defined surjection $TM \to E$" — would exclude useful examples (a distribution on $S^2$ that is locally the kernel of a $1$-form but admits no global annihilating $1$-form, by the hairy ball theorem applied to its complement). The [[Def - Subbundle|subbundle]] definition is the Goldilocks: smooth and locally-trivializable, but possibly only globally describable via patched local data.

Why does the rank have to be constant? Because we want $D$ to be a vector bundle, and vector bundles by definition have constant rank. If we wanted to allow rank to vary — singular distributions, as appearing in the theory of singular [[Def - Foliation|foliations]] — we would need a more delicate definition, but generic problems and the Frobenius theorem live in the constant-rank world. The natural extension to singular cases is a *generalized distribution* (a $C^\infty(M)$-[[Def - Submodule|submodule]] of $\mathfrak{X}(M)$ rather than a subbundle), but we postpone this.

The choice to demand smoothness rather than continuity or measurability matters for two reasons. First, we want to use the Lie bracket of vector fields, which requires their components to have one derivative. Second, the Frobenius theorem we are heading toward is a *smooth* theorem; weaker regularity would require different (and harder) techniques.

---

# The Definition

Let $M$ be a smooth $n$-manifold. A **distribution of rank $k$** on $M$ (or **tangent distribution**, **$k$-plane field**, **tangent subbundle**) is a rank-$k$ smooth [[Def - Subbundle|subbundle]] $D$ of $TM$.

Equivalently, $D$ is described by either of the following equivalent local-data presentations:

**(Frame description.)** Each point $p \in M$ has a neighborhood $U$ on which there are smooth vector fields $X_1, \dots, X_k : U \to TM$ whose values $X_1|_q, \dots, X_k|_q$ form a basis for $D_q$ at every $q \in U$. The tuple $(X_1, \dots, X_k)$ is called a **local frame** for $D$ on $U$, and $D$ is locally **spanned** by the frame.

**(Constraint description.)** Each point $p \in M$ has a neighborhood $U$ on which there are smooth $1$-forms $\omega^1, \dots, \omega^{n-k} : U \to T^*M$, pointwise linearly independent, such that

$$D_q = \bigcap_{i=1}^{n-k} \ker \omega^i_q \subseteq T_qM \qquad \text{for every } q \in U.$$

The tuple $(\omega^1, \dots, \omega^{n-k})$ is called a system of **local defining forms** or **annihilating $1$-forms** for $D$ on $U$, and $D$ is locally the **null space** of the defining forms.

A **section** of $D$ is a [[Def - Vector Field on a Manifold|vector field]] $X$ on $M$ (or on an open subset) such that $X_p \in D_p$ for every $p$. The space of smooth sections is denoted $\Gamma(D)$; it is a $C^\infty(M)$-[[Def - Submodule|submodule]] of the space of all smooth vector fields.

---

# Categorical / Structural Definition

A distribution is a *subobject in the category of smooth vector bundles over $M$*. To make this precise: the category of smooth vector bundles over $M$ has, as objects, smooth vector bundles $E \to M$, and as morphisms, smooth bundle [[Def - Homomorphism|homomorphisms]] covering the identity on $M$. A **subbundle** of $TM$ is an injective morphism $E \to TM$ whose image is a smoothly varying family of [[Def - Subspace|subspaces]] of constant rank — equivalently, a rank-$k$ smooth subbundle $D \subseteq TM$.

The structural alternatives, both equivalent to the subbundle definition:

**As a finitely-generated locally-free submodule of $\mathfrak{X}(M)$.** The $C^\infty(M)$-[[Def - Module|module]] of smooth sections $\Gamma(D)$ is a submodule of the module $\mathfrak{X}(M)$ of all smooth vector fields. The condition "locally free of rank $k$" — that every point has a neighborhood on which $\Gamma(D)$ is free over $C^\infty$ on $k$ generators — is exactly the local-frame condition. So a distribution is a *locally-free $C^\infty(M)$-submodule of $\mathfrak{X}(M)$ of rank $k$*. This is the algebraic-geometric viewpoint, where vector bundles are sheaves of locally free [[Def - Module|modules]].

**As a smooth section of the Grassmann bundle.** The **Grassmann bundle** $\mathrm{Gr}_k(TM)$ is a fiber bundle whose fiber at $p$ is the Grassmannian $\mathrm{Gr}_k(T_pM)$ of $k$-planes in $T_pM$. A distribution of rank $k$ is *exactly* a smooth section of $\mathrm{Gr}_k(TM)$. This viewpoint clarifies why distributions are a "geometric" rather than "algebraic" object: they are *fields* of planes, and the space of such fields has all the topology of a section space over the Grassmann bundle.

---

# Relate to Other Fields / Compression

**True name:** A distribution is *infinitesimal data for a desired family of submanifolds*. The operational reading is: $D$ is the answer to the question "what is the tangent space of the $k$-dimensional submanifold I hope to construct, at every point?" The natural follow-up question — "does such a submanifold exist?" — is the integrability question, answered by the [[Thm - The Frobenius Theorem|Frobenius theorem]]: yes iff $D$ is closed under Lie brackets.

**Compression to linear algebra at each point.** Pointwise, a distribution is just a choice of $k$-dimensional subspace of an $n$-dimensional vector space — an element of the Grassmannian $\mathrm{Gr}(k, n) \cong \mathrm{Gr}(k, T_pM)$. So a distribution is a smooth field of Grassmannian-valued data, varying along $M$. The local-frame and constraint descriptions are the two standard ways to specify a $k$-plane in linear algebra — by spanning vectors, or by linear equations.

**Compression to physics / mechanics.** In classical mechanics, the configuration space $Q$ of a system is a manifold, and a distribution $D \subseteq TQ$ encodes a **velocity constraint** — a restriction on which velocities $\dot{q} \in T_qQ$ the system can have at each configuration $q$. If $D = \ker \omega^1 \cap \cdots \cap \ker \omega^{n-k}$ (constraint description), then the constraint reads "$\omega^i(\dot{q}) = 0$" for each $i$ — exactly the form classical mechanics uses for nonholonomic constraints (rolling without slipping, skating on ice). The frame description "$\dot{q}$ is a linear combination of $X_1, \dots, X_k$" corresponds to specifying the *allowed* directions of motion.

**Compression to PDE.** An overdetermined system of first-order PDEs $\partial u/\partial x^i = \alpha^i(x, u)$ defines a distribution $D \subseteq T(\mathbb{R}^n \times \mathbb{R})$ spanned by the vector fields $X_i = \partial_{x^i} + \alpha^i \partial_u$. The graph of any solution $u$ is an integral submanifold of $D$. So solving the PDE = constructing an integral submanifold = applying the [[Thm - The Frobenius Theorem|Frobenius theorem]] to $D$.

---

# Examples / Corollaries

**Is an instance: a nowhere-vanishing vector field defines a rank-$1$ distribution.** Let $V$ be a smooth vector field with $V_p \neq 0$ everywhere; define $D_p = \mathrm{span}(V_p)$. This $D$ is a rank-$1$ smooth subbundle (the frame is just $V$ itself). Conversely, locally every rank-$1$ distribution is of this form (the local frame is a single nowhere-vanishing vector field), but globally a rank-$1$ distribution may not admit a global frame — the tangent line field of a Möbius strip's core circle is a rank-$1$ distribution that has no global nowhere-vanishing spanning vector field.

**Is an instance: coordinate planes in $\mathbb{R}^n$.** On $\mathbb{R}^n$, the rank-$k$ distribution spanned by $\partial/\partial x^1, \dots, \partial/\partial x^k$ has, at every point, the same $k$-plane (parallel to the first $k$ axes). Its integral manifolds are the affine [[Def - Subspace|subspaces]] $\{x^{k+1} = c^{k+1}, \dots, x^n = c^n\}$ — a [[Def - Foliation|foliation]] of $\mathbb{R}^n$ by parallel $k$-planes. The annihilating $1$-forms are $dx^{k+1}, \dots, dx^n$.

**Is an instance: the standard contact distribution on $\mathbb{R}^3$.** Let $\alpha = dz - y\,dx$ on $\mathbb{R}^3$; the rank-$2$ distribution $D = \ker \alpha$ is the **standard contact distribution**. At $(x, y, z)$, $D$ is the $2$-plane spanned by $\partial_y$ and $\partial_x + y\partial_z$. This is the prototype example of a *non-involutive* distribution — see [[Ex - A Non-Integrable Distribution on R^3 from the Standard Contact Form]]. The picture: as you move in the $x$-direction, the $2$-plane twists like a helical screw, preventing the existence of any tangent surface.

**Is an instance: the kernel of a submersion.** Let $F : M \to N$ be a smooth submersion. The fibers $F^{-1}(q)$ are submanifolds of $M$, and their tangent spaces $T_p F^{-1}(F(p)) = \ker dF_p$ form a smooth distribution of rank $\dim M - \dim N$. This distribution is *automatically integrable*, with integral manifolds the fibers themselves; the Frobenius theorem's "involutivity iff integrability" is trivially satisfied here.

**Is an instance: the kernel of a Lie algebra action.** Let a Lie [[Def - Group|group]] $G$ act smoothly on $M$; the action defines a Lie algebra homomorphism $\mathfrak{g} \to \mathfrak{X}(M)$, and the image $D_p = \{X_p^* : X \in \mathfrak{g}\}$ (where $X^*$ is the fundamental vector field associated to $X$) is a distribution. When the action is locally free, $D$ has constant rank $\dim G$; involutivity follows from the Lie algebra homomorphism property, and the integral manifolds are the orbits.

**Is NOT an instance: the union of all radial lines through $0$ in $\mathbb{R}^n$.** Each radial line through $0$ is a $1$-dimensional subspace of $\mathbb{R}^n$, but these subspaces are *not* a distribution on $\mathbb{R}^n$: at $0$, the "radial line" is not well-defined (all directions are radial), so the rank fails to be constant. This non-example probes the constant-rank requirement; the radial structure is a distribution only on $\mathbb{R}^n \setminus \{0\}$, where the rank is genuinely $1$.

**Is NOT an instance: the set $D_p = T_pM$ if $p \in $ open set, $\{0\}$ otherwise.** This is a "distribution that jumps in rank" — rank $n$ on an open piece, rank $0$ elsewhere. It fails the constant-rank requirement and is not a (vector-bundle) distribution. The correct framework for such examples is the *generalized distributions* of Sussmann–Stefan.

**Corollary (frame and constraint descriptions are dual).** If $(X_1, \dots, X_k)$ is a local frame and $(\omega^1, \dots, \omega^{n-k})$ are local defining $1$-forms for the same distribution $D$, they are *dual* in the sense that $\omega^i(X_j) = 0$ for all $i, j$ — the constraint forms annihilate the spanning fields. Extending $(X_1, \dots, X_k)$ to a full local frame $(X_1, \dots, X_n)$ for $TM$ and dualizing yields a coframe $(\eta^1, \dots, \eta^n)$ with $\eta^i(X_j) = \delta^i_j$; the constraint forms are then $\omega^i = \eta^{k+i}$ for $i = 1, \dots, n-k$.

**Corollary (sections are a $C^\infty(M)$-module).** $\Gamma(D)$ is closed under addition of vector fields and under multiplication by smooth functions: if $X, Y \in \Gamma(D)$ and $f, g \in C^\infty(M)$, then $fX + gY \in \Gamma(D)$ because $D_p$ is a linear subspace. So $\Gamma(D)$ is a submodule of $\mathfrak{X}(M)$ over $C^\infty(M)$.

**Calibration check.** If you have understood the definition you should be able to (i) verify that the standard contact distribution $\ker(dz - y\,dx)$ on $\mathbb{R}^3$ is a smooth rank-$2$ distribution by exhibiting an explicit local frame, (ii) explain why the constant-rank requirement is essential (give an example of what fails without it), and (iii) state the dual frame/coframe relationship between spanning fields and annihilating $1$-forms.

---

# Unlocked by This

> [!tip] **The Frobenius theorem** *(from this same topic)*
> Once you have distributions, you can ask whether they admit *integral submanifolds* — submanifolds tangent to $D$ at every point. The [[Thm - The Frobenius Theorem|Frobenius theorem]] is the precise criterion: integrable iff involutive (closed under Lie brackets). This is the central theorem of the section.

> [!tip] **Contact manifold** *(from Symplectic and Contact Geometry)*
> A **contact manifold** is a smooth $(2n+1)$-manifold equipped with a rank-$2n$ distribution $D$ that is *maximally non-involutive* — locally $D = \ker \alpha$ where $\alpha \wedge (d\alpha)^n \neq 0$ everywhere. This is the opposite extreme from an integrable distribution: instead of having maximally integral submanifolds (full foliation), the distribution has *no* integral submanifolds at all. Contact manifolds are the natural setting for geometric optics, geometric thermodynamics, and the cosphere bundle of a Riemannian manifold.

> [!tip] **Foliation** *(from this same topic)*
> A **foliation** is the global structure produced by an involutive distribution: a partition of $M$ into immersed submanifolds (leaves) that "fit together" via flat charts. Foliations are the moduli space of "smooth structure on the quotient $M/\sim$" where $\sim$ is the equivalence relation of "being on the same integral submanifold."

> [!tip] **Principal bundle** *(from Gauge Theory and Differential Geometry)*
> A **principal $G$-bundle** carries a canonical *vertical* distribution — the kernel of the projection — and the choice of a complementary *horizontal* distribution is exactly a **connection** on the bundle. The curvature of the connection is the obstruction to involutivity of the horizontal distribution — i.e. the Lie bracket $[X, Y]$ of two horizontal fields has a vertical part, and that vertical part is the curvature. Gauge theories are about distributions on principal bundles and the topology of their curvature.

> [!tip] **Cartan distribution** *(from PDE and Exterior Differential Systems)*
> In the **jet bundle** approach to PDE, the partial differential equation $F(x, u, \partial u, \partial^2 u, \dots) = 0$ defines a submanifold of the jet space, and the natural distribution on this submanifold — the **Cartan distribution** — has integral submanifolds corresponding to solutions of the PDE. The whole Cartan–Kähler theory of overdetermined systems is the systematic study of distributions and their integrability via differential ideals, generalizing Frobenius's theorem.
