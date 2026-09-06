---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection 1-Form on a Principal Bundle"
  - "Def - Bracket of g-Valued Forms"
  - "Def - Lie-Algebra-Valued Differential Form"
  - "Def - Adjoint Bundle"
tags: [geometry, gauge-theory, principal-bundles, curvature]
---

# Notation

$P \to M$ is a principal $G$-bundle, $\omega \in \Omega^1(P; \mathfrak{g})$ a [[Def - Connection 1-Form on a Principal Bundle|connection 1-form]]. The Lie bracket on $\mathfrak{g}$ extends to a [[Def - Bracket of g-Valued Forms|bracket of \mathfrak{g}-valued forms]] by $[\alpha \otimes \xi, \beta \otimes \eta] = \alpha \wedge \beta \otimes [\xi, \eta]$. The curvature 2-form is denoted $\Omega \in \Omega^2(P; \mathfrak{g})$ (Frankel's notation; some authors write $F$ or $\Theta$). For matrix groups, $\tfrac{1}{2}[\omega, \omega] = \omega \wedge \omega$ where the right-hand side is the matrix wedge.

---

# Axiom Motivation

What is curvature? Geometrically, the curvature of a connection is the obstruction to the horizontal distribution being involutive — equivalently, the obstruction to parallel transport being path-independent — equivalently, the obstruction to the connection being locally trivial. We need a *formula* that captures this obstruction, and that formula is the Cartan structural equation.

The motivation is forced by analogy with the [[Def - The Maurer-Cartan Form|Maurer-Cartan form]] on a Lie group $G$. The Maurer-Cartan form $\theta_G$ is the canonical flat connection on the trivial bundle $G \to *$, and it satisfies $d\theta_G + \tfrac{1}{2}[\theta_G, \theta_G] = 0$ — the [[Thm - Maurer-Cartan Equation|Maurer-Cartan equation]]. The vanishing of the right-hand side is the statement of flatness: there is no curvature. For a general connection $\omega$ on a general principal bundle, the *same combination* $d\omega + \tfrac{1}{2}[\omega, \omega]$ need not vanish — and *whatever it equals* is the curvature.

This is the **Cartan structural equation**:
$$
\Omega := d\omega + \tfrac{1}{2}[\omega, \omega].
$$
The motivation in one sentence: curvature is the *deformation* of the Maurer-Cartan equation. A flat connection satisfies Maurer-Cartan; a curved connection has $\Omega \neq 0$ measuring the deviation.

Why this exact formula? Three reasons.

**(i) Compatibility with the matrix case.** For matrix groups, $\tfrac{1}{2}[\omega, \omega] = \omega \wedge \omega$ (the matrix wedge of a 1-form with itself, which is nonzero because matrix entries do not commute under wedge). So $\Omega = d\omega + \omega \wedge \omega$ — the formula physicists use in matrix-group form. The two notations agree.

**(ii) Compatibility with the vector-bundle structural equation.** The Cartan structural equation specialises to the structural equation $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$ of [[Riemannian Geometry I — Connections and Covariant Differentiation|Riemannian Geometry I §1.3]] via the associated bundle construction. The matrix indices $(a, b)$ are the basis indices of the defining representation of $\mathrm{GL}(n)$, and the wedge product is the entry-wise matrix wedge. This is the consistency check: principal-bundle curvature and vector-bundle curvature are the same object, viewed in different formalisms.

**(iii) Horizontality and equivariance.** The defining property of a useful curvature is that it descends to a globally defined object on $M$ — specifically, a 2-form section of the [[Def - Adjoint Bundle|adjoint bundle]] $\mathrm{Ad}\,P$. This requires $\Omega$ to be (a) horizontal — vanishing on vertical tangent vectors — and (b) equivariant — transforming under the adjoint representation. The Cartan structural equation produces exactly such a form, as proved in [[Thm - Cartan Structural Equation for Principal Connections]]. If we tried any other formula (e.g., $d\omega$ alone, or $d\omega + [\omega, \omega]$), we would not get a horizontal equivariant form.

What if we dropped the $\tfrac{1}{2}[\omega, \omega]$ term? Then $\Omega = d\omega$, the abelian formula. For abelian $G$, this is correct (since the bracket vanishes). For non-abelian $G$, $d\omega$ is not horizontal — it has a vertical part proportional to $\tfrac{1}{2}[\omega, \omega]$ (essentially the structure constants of $\mathfrak{g}$ via the verticality axiom). Adding $\tfrac{1}{2}[\omega, \omega]$ cancels this vertical part exactly, producing a horizontal form. The bracket term is *not optional* — it is forced by the requirement of horizontality.

What does "horizontal" mean for a 2-form? A 2-form $\Omega$ on $P$ is **horizontal** if $\Omega(X, Y) = 0$ whenever either $X$ or $Y$ is vertical (i.e., a fundamental vector field). This is equivalent to saying $\Omega$ is the pullback $\pi^* F$ of a 2-form $F$ on $M$ (in the trivial case) — but for non-trivial bundles, "horizontal + equivariant" is weaker than "$\pi$-projectable" and the right descent is to a section of $\Lambda^2 T^*M \otimes \mathrm{Ad}\,P$.

In components for a matrix group, the curvature reads
$$
F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + f^a{}_{bc}\,A^b_\mu A^c_\nu,
$$
where $f^a{}_{bc}$ are the structure constants of $\mathfrak{g}$. The first two terms are the abelian field strength; the third is the **non-abelian self-coupling** that makes gauge theory self-interacting. Physically, this term gives the three-gluon and four-gluon vertices in QCD, the $W^+W^-Z$ vertex in electroweak theory, and so on. There are no analogous self-couplings in electromagnetism because $U(1)$ is abelian.

The naming "curvature" extends the Riemannian-geometry usage: in Riemannian geometry, the Riemann tensor $R^a{}_{bcd}$ is the curvature of the Levi-Civita connection on $TM$. In gauge theory, the field strength $F^a_{\mu\nu}$ is the curvature of the gauge connection on $P$. The two are special cases of the same construction, and the name "curvature" is universal.

---

# The Definition

Let $P \to M$ be a principal $G$-bundle and $\omega \in \Omega^1(P; \mathfrak{g})$ a connection 1-form.

The **curvature 2-form** of $\omega$ is the $\mathfrak{g}$-valued 2-form on $P$
$$
\Omega := d\omega + \tfrac{1}{2}[\omega, \omega] \in \Omega^2(P; \mathfrak{g}).
$$
This is the **Cartan structural equation**. For matrix groups (when $\mathfrak{g}$ is a matrix Lie algebra and we identify $\mathfrak{g}$-valued forms with matrices of forms), the equation reads
$$
\Omega = d\omega + \omega \wedge \omega,
$$
since $\tfrac{1}{2}[\omega, \omega] = \omega \wedge \omega$ for matrix-valued 1-forms.

**Properties** (proved in [[Thm - Cartan Structural Equation for Principal Connections]]):

1. **Horizontality.** $\Omega(X, Y) = 0$ whenever $X$ or $Y$ is vertical (a fundamental vector field).
2. **Equivariance.** $R_g^*\Omega = \mathrm{Ad}_{g^{-1}}\,\Omega$ for every $g \in G$.
3. **Descent.** By horizontality and equivariance, $\Omega$ descends to a 2-form section of the [[Def - Adjoint Bundle|adjoint bundle]]:
$$
F \in \Omega^2(M; \mathrm{Ad}\,P).
$$
The descent is canonical: for a local section $s_\alpha : U_\alpha \to P$, $F|_{U_\alpha} = s_\alpha^*\Omega$ in the local trivialisation of $\mathrm{Ad}\,P$ via $s_\alpha$.

**Local form.** For a local section $s : U \to P$ with [[Def - Local Connection 1-Form (Gauge Potential)|gauge potential]] $A = s^*\omega$:
$$
F = s^*\Omega = dA + \tfrac{1}{2}[A, A] = dA + A \wedge A \text{ (matrix groups)}.
$$
In components for matrix groups, $F = \tfrac{1}{2}F^a_{\mu\nu}\,T_a\,dx^\mu \wedge dx^\nu$ with
$$
F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + f^a{}_{bc}\,A^b_\mu A^c_\nu,
$$
where $T_a$ are basis generators of $\mathfrak{g}$ and $f^a{}_{bc}$ are the structure constants ($[T_a, T_b] = f^c{}_{ab}\,T_c$, with appropriate sign conventions).

**Bianchi identity** (proved in [[Thm - Bianchi Identity for Principal Connections]]): $d_\omega\Omega = d\Omega + [\omega, \Omega] = 0$. Equivalently, $d_\nabla F = 0$ as a 3-form section of $\mathrm{Ad}\,P$, where $\nabla$ is the induced connection on $\mathrm{Ad}\,P$.

---

# Relate to Other Fields / Compression

In **electromagnetism**, the curvature of a $U(1)$-connection is the electromagnetic field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, the antisymmetric matrix encoding the electric field $\mathbf{E}$ and magnetic field $\mathbf{B}$. The non-abelian term $f^a{}_{bc}A^b A^c$ vanishes identically ($U(1)$ is abelian), so the abelian formula $F = dA$ holds. Bianchi $dF = 0$ gives Faraday's law $\nabla \times \mathbf{E} + \partial_t \mathbf{B} = 0$ and Gauss's law for magnetism $\nabla \cdot \mathbf{B} = 0$ — the *geometric* half of Maxwell. The *dynamical* half ($d \star F = j$) is the Yang-Mills equation.

In **Yang-Mills theory** with structure group $SU(N)$, the curvature is the field strength $F^a_{\mu\nu}$ of the $SU(N)$-gauge field, with $a = 1, \ldots, N^2 - 1$. The non-abelian term $f^a{}_{bc}A^b A^c$ produces gluon-gluon interactions (in QCD: the three-gluon and four-gluon vertices). The classical Yang-Mills action is $-\tfrac{1}{4}\int F^a_{\mu\nu}F^{a\,\mu\nu}\,d^4x$, manifestly gauge-invariant because $F$ transforms in the adjoint.

In **Riemannian geometry**, the curvature of the Levi-Civita connection on the orthonormal frame bundle is the [[Riemannian Geometry I — Connections and Covariant Differentiation|matrix of curvature 2-forms]] $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$, with values in $\mathfrak{o}(n)$ (antisymmetric matrices). The components $R^a{}_{b\mu\nu}$ are exactly the Riemann tensor components in an orthonormal frame.

**True name:** the curvature is *the obstruction to the horizontal distribution being involutive*. By the explicit formula $\Omega(X, Y) = -\omega([\tilde X, \tilde Y]^V)$ for horizontal lifts $\tilde X, \tilde Y$ of base vector fields (where $[\,\cdot\,]^V$ is the vertical projection), curvature measures the failure of the Lie bracket of horizontal vectors to remain horizontal — equivalently, the failure of parallel transport to be path-independent for infinitesimal closed loops. This is the precise geometric content of "curvature is the second-order effect of holonomy around an infinitesimal loop".

---

# Examples / Corollaries

**Example (flat connection on $G \to *$).** For the trivial bundle $G \to \{*\}$ with the canonical connection $\omega = \theta_G$ (Maurer-Cartan form), the curvature is $\Omega = d\theta_G + \tfrac{1}{2}[\theta_G, \theta_G] = 0$ by the Maurer-Cartan equation. So the Maurer-Cartan form is *the* canonical flat connection: curvature zero by construction.

**Example (electromagnetism in Cartesian coordinates).** For the $U(1)$-connection on a $U(1)$-bundle over Minkowski space with $A = A_\mu\,dx^\mu$ (locally), the curvature is $F = dA = \tfrac{1}{2}(\partial_\mu A_\nu - \partial_\nu A_\mu)\,dx^\mu \wedge dx^\nu$, with components $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. The electric field is $E^i = F^{0i}$ and the magnetic field is $B^k = \tfrac{1}{2}\varepsilon^{ijk}F_{ij}$.

**Example ($SU(2)$ Yang-Mills in 4D).** For an $SU(2)$-connection with $A = i\sigma_a A^a_\mu\,dx^\mu/2$ (Pauli matrices basis), the curvature is
$$
F = dA + A \wedge A = \tfrac{i}{2}\sigma_a\,(F^a_{\mu\nu}/2)\,dx^\mu \wedge dx^\nu,
$$
with $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + \varepsilon^a{}_{bc}A^b_\mu A^c_\nu$. The non-abelian term $\varepsilon^a{}_{bc}A^b A^c$ is responsible for the **instantons** of [[Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons|Gauge Theory IV]] — without this term, the BPST solution would not exist.

**Example (Hopf bundle).** For the Hopf bundle $S^3 \to S^2$ with the standard $U(1)$-connection, the curvature is $F = -\tfrac{i}{2}\sin\theta\,d\theta \wedge d\varphi$ in spherical coordinates on $S^2$ — proportional to the area form $\omega_{S^2}$. The integral $\int_{S^2} F = -2\pi i$ (or $2\pi$ after dividing out the $i$), reflecting the non-trivial Chern class of the Hopf bundle.

**Is NOT an instance:** the exterior derivative $d\omega$ alone is *not* the curvature for non-abelian $G$ — it lacks the $\tfrac{1}{2}[\omega, \omega]$ term and is not horizontal. The bracket term is essential.

**Is NOT an instance:** the gauge potential $A$ is *not* the curvature — they are different geometric objects of different form-degrees. $A$ is a 1-form on $M$ (gauge-variant); $F$ is a 2-form section of $\mathrm{Ad}\,P$ (gauge-covariant in the adjoint representation).

**Corollary (transformation under gauge).** Under a gauge transformation $A \mapsto A' = g^{-1}Ag + g^{-1}dg$, the curvature transforms in the adjoint representation:
$$
F' = g^{-1}F g = \mathrm{Ad}_{g^{-1}}F.
$$
The inhomogeneous term in the gauge transformation of $A$ cancels in the curvature computation. Verification: $F' = dA' + A' \wedge A' = d(g^{-1}Ag + g^{-1}dg) + (g^{-1}Ag + g^{-1}dg) \wedge (g^{-1}Ag + g^{-1}dg)$ expands to give $g^{-1}Fg$ after cancellations.

**Corollary (abelian case).** For abelian $G$, $[\omega, \omega] = 0$ identically, so $\Omega = d\omega$ and $F = dA$. The curvature is *exact* locally, and $dF = 0$ automatically — the Bianchi identity reduces to a trivial identity. This is why electromagnetism is "much simpler" than non-abelian gauge theory.

**Corollary (Chern-Weil).** For any $\mathrm{Ad}$-invariant polynomial $p$ on $\mathfrak{g}$, the form $p(F) \in \Omega^{2k}(M; \mathbb{R})$ (where $p$ has degree $k$ in $F$) is closed ($d\,p(F) = 0$, by Bianchi and $\mathrm{Ad}$-invariance) and represents a de Rham cohomology class independent of the choice of connection. For $U(n)$, taking $p = \mathrm{tr}(F^k)$ gives the **Chern classes** $c_k \in H^{2k}(M; \mathbb{Z})$; for $O(n)$, traces of even powers give the **Pontryagin classes**. These are the topological invariants of the bundle.

**Calibration check.** If you have understood the definition, you should be able to: (i) write down the curvature formula $F = dA + \tfrac{1}{2}[A, A]$ from memory and verify it in matrix-group form as $F = dA + A \wedge A$; (ii) compute the curvature in components for an $SU(2)$-connection $A^a_\mu$, obtaining $F^a_{\mu\nu} = \partial_\mu A^a_\nu - \partial_\nu A^a_\mu + \varepsilon^a{}_{bc}A^b_\mu A^c_\nu$; (iii) explain why the non-abelian term $A \wedge A$ vanishes for $U(1)$ but not for $SU(2)$ — answer: $U(1)$ is abelian so the bracket vanishes; for $SU(2)$ the bracket is the cross-product-like $\varepsilon^a{}_{bc}$ which is nonzero.

---

# Unlocked by This

> [!tip] Cartan Structural Equation Theorem *(from Gauge Theory III)*
> The defining formula $\Omega = d\omega + \tfrac{1}{2}[\omega, \omega]$ is the content of the Cartan structural equation. The theorem [[Thm - Cartan Structural Equation for Principal Connections]] proves that this $\Omega$ is horizontal and equivariant, hence descends to a 2-form section $F \in \Omega^2(M; \mathrm{Ad}\,P)$ of the adjoint bundle.

> [!tip] Bianchi Identity *(from Gauge Theory III)*
> The curvature satisfies $d_\omega\Omega = 0$, equivalently $dF + [A, F] = 0$ for the local field strength — the [[Thm - Bianchi Identity for Principal Connections|Bianchi identity]]. It is a *geometric identity*, true for every connection, not a dynamical equation.

> [!tip] Yang-Mills Equations *(from Yang-Mills Theory)*
> Together with the Bianchi identity $d_\omega F = 0$, the Yang-Mills equation $d_\omega \star F = 0$ (derived from extremising the Yang-Mills action) gives the gauge-field dynamics. For self-dual connections in four dimensions ($F = \star F$), Bianchi implies Yang-Mills automatically — this is the **instanton equation** of [[Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons|Gauge Theory IV]].

> [!tip] Chern-Weil Theory and Characteristic Classes *(from Algebraic Topology)*
> Invariant polynomials of the curvature form $F$ produce de Rham representatives of the characteristic classes of the principal bundle — Chern classes for $U(n)$, Pontryagin and Euler classes for $O(n)$ and $SO(n)$. These are topological invariants of the bundle (independent of the connection) and obstruct triviality of $P$. The integrals $\int_M c_k$ give topological invariants like the **instanton number** for $SU(2)$-bundles over $S^4$. See [[Algebraic Topology III — Higher Homotopy and Chern Forms]].

> [!tip] Curvature and Holonomy: Ambrose-Singer *(from Differential Geometry)*
> The **Ambrose-Singer theorem** states that the Lie algebra of the connected component of the holonomy group $\mathrm{Hol}^0(\omega)$ at a point $p \in P$ is the linear span of $\{\Omega_q(X, Y) : q \in P, X, Y \in T_q P\}$, where parallel transport identifies $\mathfrak{g}$ at different points. This is the precise sense in which "curvature generates holonomy" — the curvature *exhausts* the infinitesimal holonomy, modulo conjugation.
