---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Lie-Algebra-Valued Differential Form"
  - "Def - Fundamental Vector Field of a Principal Bundle"
  - "Def - Adjoint Representation"
  - "Def - Lie Group"
tags: [geometry, gauge-theory, principal-bundles, connections]
---

# Notation

$P \to M$ is a principal $G$-bundle with right action $R_g : P \to P$, $p \mapsto p \cdot g$. $\mathfrak{g} = T_e G$ is the Lie algebra. For $\xi \in \mathfrak{g}$, $\xi^* \in \mathfrak{X}(P)$ is the [[Def - Fundamental Vector Field of a Principal Bundle|fundamental vector field]]. $\mathrm{Ad} : G \to \mathrm{GL}(\mathfrak{g})$ is the [[Def - Adjoint Representation|adjoint representation]]. We write $\Omega^1(P; \mathfrak{g})$ for the space of [[Def - Lie-Algebra-Valued Differential Form|$\mathfrak{g}$-valued 1-forms]] on $P$.

---

# Axiom Motivation

What is the right way to encode the data of "parallel transport" on a principal bundle? In the [[Riemannian Geometry I — Connections and Covariant Differentiation|vector-bundle setting]], a connection $\nabla$ on $E$ specified, for each vector field $X \in \mathfrak{X}(M)$, the linear operator $\nabla_X : \Gamma(E) \to \Gamma(E)$ — equivalently, an $\mathrm{End}(E)$-valued 1-form on $M$. For a principal bundle this approach is awkward because $P$ does not have a natural "section" picture: $P$ has *fibres* on which $G$ acts, not vector-space fibres. We need a more invariant formulation.

The clean formulation, due to **Ehresmann** (1950): a connection on $P$ is a $G$-equivariant assignment, at each $p \in P$, of a "horizontal" complementary subspace $H_p$ to the canonical vertical subspace $V_p P = \ker(d\pi_p)$. The horizontal subspaces let one *lift* tangent vectors on $M$ uniquely to horizontal tangent vectors on $P$, which integrates to give parallel transport along curves. This is the **geometric** or **distribution** picture of a connection (see [[Def - Horizontal Subspace]]).

The **algebraic** or **1-form** picture, due to Cartan and now standard, packages exactly the same data as a $\mathfrak{g}$-valued 1-form $\omega \in \Omega^1(P; \mathfrak{g})$ on the total space. The bijection: given a horizontal distribution $H$, define $\omega$ to vanish on $H$ and to be the inverse vertical-space isomorphism on $V_p P$. Given $\omega$, define $H_p = \ker\omega_p$. The two pictures are equivalent (see [[Thm - Principal Connection is Equivalent to a Horizontal Distribution]]); the 1-form picture is computationally clean and is what we develop here.

But not every $\mathfrak{g}$-valued 1-form on $P$ is a connection. Two axioms are needed.

**(i) Verticality.** The form must "see" vertical directions correctly: for $\xi \in \mathfrak{g}$, $\omega(\xi^*_p) = \xi$ at every $p \in P$. This says that $\omega$, restricted to $V_p P$, is the inverse of the vertical-space isomorphism $\mathfrak{g} \to V_p P$ — equivalently, $\omega|_{V_p P}$ is the canonical 1-form coming from the principal-bundle structure, with no connection-specific content. Verticality is *automatic* in the sense that it is a normalisation condition: it pins down what $\omega$ does on vertical directions, and the connection content is in what $\omega$ does on horizontal (= non-vertical) directions.

Without verticality, $\omega$ would fail to be related to the canonical vertical structure of the bundle. There would be no canonical way to define parallel transport, no canonical way to extract the gauge potential by pullback. Verticality is the *minimum* needed for $\omega$ to be a connection in any meaningful sense.

**(ii) Equivariance.** The form must transform correctly under the right action: $R_g^*\omega = \mathrm{Ad}_{g^{-1}}\omega$ for every $g \in G$. Pointwise, this means $\omega_p((dR_g)_{R_{g^{-1}}p}X) = \mathrm{Ad}_{g^{-1}}\omega_{R_{g^{-1}}p}(X)$ — pull back a tangent vector by $R_g$, evaluate $\omega$, and you get the adjoint-conjugated answer of what you would have got by evaluating $\omega$ first.

This is the *non-trivial* axiom — the one that distinguishes a *principal* connection from a generic $\mathfrak{g}$-valued 1-form. Geometrically, it says that the horizontal distribution $\ker\omega$ is *$G$-equivariant*: $(R_g)_* H_p = H_{p \cdot g}$. The right action carries horizontal vectors to horizontal vectors. This is what allows parallel transport to be well defined globally on the bundle: if you parallel-transport $p_0$ along $\gamma$ and get $p_1$, then transporting $p_0 \cdot g$ along the same $\gamma$ gives $p_1 \cdot g$ — the same $g$, applied to both endpoints.

Without equivariance, the horizontal distribution would not respect the principal-bundle structure. The local gauge potentials $A_\alpha = s_\alpha^*\omega$ would not transform correctly under change of section, the curvature would not descend to a section of $\mathrm{Ad}\,P$, and the whole formalism would collapse. Equivariance is what makes the connection a *principal* connection — compatible with the $G$-action that defines the bundle.

What if we replaced $\mathrm{Ad}_{g^{-1}}$ with some other action of $G$ on $\mathfrak{g}$? It would have to be a representation (for the cocycle to close up under composition), and it would have to fix vertical vectors correctly (for verticality to be preserved). The adjoint representation is the unique choice that satisfies both — it is forced by the principal-bundle structure.

Why is the connection a 1-form on $P$, not on $M$? Because the data is *globally* a 1-form on $P$ (no choice of section needed) but only *locally* a 1-form on $M$ (different sections give different pullbacks). Working on $P$ is what makes the formalism invariant. The gauge potential $A_\alpha = s_\alpha^*\omega$ on $M$ is a useful *consequence* of $\omega$, but not the fundamental object.

The test of a successful definition is: can we recover the parallel transport, curvature, and gauge transformation laws of physics from these two axioms alone? The answer is yes — every formula in classical gauge theory drops out of (i) and (ii) by direct calculation.

---

# The Definition

Let $P \to M$ be a principal $G$-bundle with right action $R_g(p) = p \cdot g$.

A **connection 1-form** (or **principal connection**) on $P$ is a $\mathfrak{g}$-valued 1-form $\omega \in \Omega^1(P; \mathfrak{g})$ satisfying both of the following axioms:

**(i) Verticality.** For every $\xi \in \mathfrak{g}$ and every $p \in P$,
$$
\omega(\xi^*_p) = \xi,
$$
where $\xi^*$ is the [[Def - Fundamental Vector Field of a Principal Bundle|fundamental vector field]] of $\xi$.

**(ii) Equivariance.** For every $g \in G$,
$$
R_g^*\omega = \mathrm{Ad}_{g^{-1}}\,\omega,
$$
where $R_g^*$ is the pullback under $R_g$ and $\mathrm{Ad}_{g^{-1}} : \mathfrak{g} \to \mathfrak{g}$ is the inverse-adjoint linear map applied to the $\mathfrak{g}$-value pointwise. Pointwise: $\omega_{p \cdot g}((dR_g)_p X) = \mathrm{Ad}_{g^{-1}}(\omega_p(X))$ for $X \in T_p P$.

The kernel
$$
H_p := \ker\omega_p \subseteq T_p P
$$
is the **horizontal subspace** at $p$; the collection $\{H_p\}_{p \in P}$ is the [[Def - Horizontal Subspace|horizontal distribution]] of $\omega$. The pair $(\omega, \{H_p\})$ is two views of the same data: $T_p P = V_p P \oplus H_p$ at every point, with the vertical part identified with $\mathfrak{g}$ via $\omega$.

The set of all connections on $P$ is denoted $\mathcal{A}(P)$. By [[Ex - The Affine Space of Connections on a Principal Bundle]], $\mathcal{A}(P)$ is an **affine space modelled on $\Omega^1(M; \mathrm{Ad}\,P)$**: the difference of two connections is a horizontal equivariant 1-form on $P$, i.e., a 1-form section of the adjoint bundle.

---

# Categorical / Structural Definition

In the framework of **groupoids and Cartan connections**, a connection on a principal $G$-bundle is equivalent to a section of the **first jet bundle** $J^1 P \to P$ that is $G$-equivariant, where $J^1 P$ classifies "infinitesimal section data" at each point of $P$.

Equivalently, in the language of **Ehresmann connections**: a connection on a fibre bundle $\pi : E \to M$ is an $\mathbb{E}$-valued 1-form $\Phi : TE \to VE$ that projects each tangent vector onto its vertical component along a fixed horizontal complement. For a principal bundle, where the vertical bundle is canonically trivialised by fundamental vector fields, this reduces to a $\mathfrak{g}$-valued 1-form — recovering the present definition.

Categorically, the connection forms a section of an affine bundle: the bundle of connections $\mathcal{C}(P) \to M$ has fibre $\mathcal{C}_x = \mathcal{A}(P|_{P_x})$, the affine space of equivariant horizontal distributions in $T_p P$ for $p \in P_x$, modelled on $T_x^*M \otimes \mathfrak{g}$. Connections globally are equivalent to sections of this affine bundle.

In **synthetic differential geometry**, a connection is a functor from the (smooth) groupoid of paths in $M$ to the category of fibres of $P$ — the parallel transport functor. The axioms of the 1-form definition are the infinitesimal version of the functor axioms (composition, identity).

---

# Relate to Other Fields / Compression

A principal connection generalises the vector-bundle connections of [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection|Gauge Theory I]] and [[Riemannian Geometry I — Connections and Covariant Differentiation|Riemannian Geometry I]] in a strong sense: every vector-bundle connection $\nabla$ on $E$ is equivalent to a principal connection on the frame bundle $\mathrm{Fr}(E)$, and the principal connection induces $\nabla$ on $E = \mathrm{Fr}(E) \times_{\mathrm{GL}(K)} \mathbb{R}^K$ via the [[Thm - Principal Connection Induces a Connection on Every Associated Bundle|associated bundle construction]]. So the principal-bundle picture and the vector-bundle picture are two windows on the same geometric object — the principal picture being the more invariant one, the vector picture the more concrete.

For matrix Lie groups, the principal connection is **the global, gauge-invariant version of the Christoffel symbols of differential geometry**. The Christoffel symbols of the Levi-Civita connection on a Riemannian manifold are the local gauge potentials $A_\alpha = s_\alpha^*\omega$ of the principal connection on the orthonormal frame bundle. The "$g^{-1}dg$ inhomogeneous term" in the gauge transformation law is the principal-bundle version of the well-known inhomogeneous transformation of Christoffel symbols under change of chart.

In **physics**, every gauge field is a principal connection. The electromagnetic vector potential $A_\mu$ is the local gauge potential of a $U(1)$-connection; the colour gauge fields $G^a_\mu$ ($a = 1, \ldots, 8$) of QCD are the local gauge potentials of an $SU(3)$-connection; the electroweak gauge fields are local gauge potentials of an $SU(2) \times U(1)$-connection; the spin connection of general relativity is a local gauge potential of an $SO(1,3)$- or $\mathrm{Spin}(1,3)$-connection on the orthonormal frame bundle. All of them satisfy the same structural equation $F = dA + \tfrac{1}{2}[A, A]$ and the same Bianchi identity $d_A F = 0$, differing only in the choice of structure group $G$.

**True name:** the connection 1-form is *the global, $G$-equivariant horizontal distribution on $P$, packaged as the 1-form whose kernel is that distribution and whose restriction to vertical vectors is the canonical inverse of the vertical-space isomorphism*. In matrix-group notation, $\omega = g^{-1}A g + g^{-1}dg$ in a trivialisation given by a section $s : M \to P$, $s(x) = (x, e)$ — that is, the connection is "Maurer-Cartan-like on the fibre direction, plus a base-coupling term $A$ on the horizontal direction". This decomposition is the operational picture.

---

# Examples / Corollaries

**Example (canonical flat connection on a trivial bundle).** For the trivial bundle $P = M \times G$ with the obvious right action $(x, h) \cdot g = (x, hg)$, the canonical connection is $\omega = \mathrm{pr}_G^* \theta_G$, the pullback of the [[Def - The Maurer-Cartan Form|Maurer-Cartan form]] of $G$. Verticality: fundamental vector fields project to $G$ as left-invariant vector fields, on which $\theta_G$ acts as the identity. Equivariance: $R_g^* \theta_G = \mathrm{Ad}_{g^{-1}}\theta_G$ — a property of the Maurer-Cartan form. The canonical section $s : M \to M \times G$, $x \mapsto (x, e)$, has $s^*\omega = 0$, so the gauge potential vanishes in the canonical gauge. This is the *trivial flat connection*; its curvature is zero by the Maurer-Cartan equation.

**Example (Levi-Civita connection on a Riemannian manifold).** For $(M, g)$ Riemannian and $P = F^O(M)$ the orthonormal frame bundle (a principal $O(n)$-bundle), the Levi-Civita connection of [[Riemannian Geometry I — Connections and Covariant Differentiation|Riemannian Geometry I]] is *equivalent* to a principal connection $\omega$ on $F^O(M)$ with values in $\mathfrak{o}(n)$ (antisymmetric matrices). The pullback under any local orthonormal frame gives the matrix of Cartan connection 1-forms $\omega^a{}_b$ of Riemannian geometry. See [[Ex - Connection on the Frame Bundle of a Riemannian Manifold from Levi-Civita]].

**Example (electromagnetic connection on a $U(1)$-bundle).** For a $U(1)$-bundle $P \to M$, a principal connection is a $\mathfrak{u}(1) = i\mathbb{R}$-valued 1-form on $P$. In a local trivialisation, $\omega = i A_\mu\,dx^\mu + i\,d\theta$ where $\theta$ is the fibre coordinate (an angle), and $A_\mu$ is the local gauge potential — the electromagnetic 4-potential. See [[Ex - Local Connection 1-Form of the Electromagnetic Bundle]].

**Is NOT an instance:** an arbitrary $\mathfrak{g}$-valued 1-form on $P$ is generally not a connection. For example, the zero form $\omega = 0$ is not a connection (it fails verticality: $\omega(\xi^*) = 0 \neq \xi$ for nonzero $\xi$). A connection is a *normalised* 1-form, with the verticality axiom pinning down its values on $V_p P$.

**Is NOT an instance:** the pullback $A = s^*\omega$ of a connection along a section is a 1-form on the base $M$, not a 1-form on the total space $P$. It is the [[Def - Local Connection 1-Form (Gauge Potential)|gauge potential]], not the connection. The connection lives on $P$; the gauge potential is its shadow on $M$ after choosing a section.

**Corollary.** For any connection $\omega$ on $P$, the horizontal distribution $H = \ker\omega$ is:
- of rank $n = \dim M$ everywhere (because $\omega : T_p P \to \mathfrak{g}$ is surjective and $\dim T_p P = n + \dim G$);
- $G$-equivariant: $(R_g)_* H_p = H_{p\cdot g}$ (from equivariance of $\omega$);
- transverse to the vertical: $T_p P = V_p P \oplus H_p$ (from verticality, which forces $\omega$ to be an isomorphism $V_p P \to \mathfrak{g}$, so $\ker\omega \cap V_p P = 0$).

**Corollary.** The orthogonal projection $T_p P \to V_p P$ along $H_p$ — that is, the assignment of the vertical part of a tangent vector — is the map $X \mapsto \omega(X)^*_p$. So the connection 1-form encodes the vertical-projection operator at every point.

**Corollary (affine structure).** The difference of two connections $\omega_1 - \omega_2$ vanishes on every fundamental vector field (both connections agree on the vertical part by verticality), so it factors through the horizontal: it is a *horizontal* 1-form on $P$ with values in $\mathfrak{g}$. By equivariance, it is also equivariant: $R_g^*(\omega_1 - \omega_2) = \mathrm{Ad}_{g^{-1}}(\omega_1 - \omega_2)$. A horizontal equivariant $\mathfrak{g}$-valued form on $P$ is exactly a form on $M$ with values in $\mathrm{Ad}\,P$ (the [[Def - Adjoint Bundle|adjoint bundle]]). Conclusion: $\mathcal{A}(P)$ is an affine space modelled on $\Omega^1(M; \mathrm{Ad}\,P)$. See [[Ex - The Affine Space of Connections on a Principal Bundle]].

**Calibration check.** If you have understood the definition, you should be able to: (i) verify the verticality axiom for the canonical connection $\omega = \mathrm{pr}_G^*\theta_G$ on $M \times G$, by computing $\omega(\xi^*)$ for a fundamental vector field; (ii) check that the kernel $\ker\omega$ of any connection is transverse to the vertical, using verticality and the surjectivity of $\omega : T_p P \to \mathfrak{g}$ for vertical vectors; (iii) explain in one sentence why a connection cannot exist as a $\mathfrak{g}$-valued 1-form on $M$ alone — answer: any local pullback $A = s^*\omega$ depends on the section, and there is no canonical global section unless $P$ is trivial; for non-trivial bundles, only the global form on $P$ is well defined.

---

# Unlocked by This

> [!tip] Horizontal Distribution and Parallel Transport *(from Gauge Theory III)*
> A connection 1-form $\omega$ determines a horizontal distribution $H = \ker\omega$, and the **horizontal lift** of a curve $\gamma$ on $M$ — the unique curve $\tilde\gamma$ on $P$ that projects to $\gamma$ and is everywhere horizontal — gives **parallel transport** in the principal bundle. The lift solves a linear ODE; integrating it gives the **holonomy** of the connection around closed loops. See [[Def - Horizontal Subspace]] and [[Thm - Principal Connection is Equivalent to a Horizontal Distribution]].

> [!tip] Curvature and the Cartan Structural Equation *(from Gauge Theory III)*
> The curvature 2-form of $\omega$ is $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega] \in \Omega^2(P; \mathfrak{g})$. This is the **Cartan structural equation**, and the resulting $\Omega$ is horizontal and equivariant, hence descends to a section of $\Lambda^2 T^*M \otimes \mathrm{Ad}\,P$. See [[Thm - Cartan Structural Equation for Principal Connections]] and [[Def - Curvature 2-Form on a Principal Bundle]].

> [!tip] Induced Connections on Associated Bundles *(from Gauge Theory III)*
> A principal connection $\omega$ on $P$ induces a connection on every associated bundle $P \times_\rho V$ via the representation $\rho : G \to \mathrm{GL}(V)$. The induced covariant derivative is $\nabla = d + d\rho(A)$ in any local trivialisation. This is what makes the principal-bundle formalism the *unifying framework* for all matter fields in a gauge theory. See [[Thm - Principal Connection Induces a Connection on Every Associated Bundle]].

> [!tip] Holonomy and Ambrose-Singer *(from Differential Geometry)*
> The **holonomy group** $\mathrm{Hol}(\omega) \subseteq G$ at $p \in P$ is the subgroup obtained by parallel-transporting $p$ around all loops based at $\pi(p)$. The **Ambrose-Singer theorem** states that the Lie algebra of the connected component $\mathrm{Hol}^0(\omega)$ is the span of all curvature values $\Omega(X, Y)$ — the precise statement that "curvature generates holonomy". This is the most refined expression of the slogan "curvature is the obstruction to parallel transport being path-independent" and the geometric input to **flat connections**, which have discrete holonomy classified by representations $\pi_1(M) \to G$.
