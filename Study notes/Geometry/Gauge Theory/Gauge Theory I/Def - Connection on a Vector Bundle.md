---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Vector Bundle"
  - "Def - Section of a Vector Bundle"
  - "Def - Local Frame"
  - "Def - Differential k-Form on a Manifold"
  - "Def - Exterior Derivative on a Manifold"
tags: [geometry, gauge-theory, connection, covariant-derivative]
---

# Notation

$\pi : E \to M$ is a smooth real or complex vector bundle of rank $K$ over a smooth manifold $M$ (see [[Def - Vector Bundle]]). $\Gamma(E)$ denotes the $C^\infty(M)$-module of smooth global sections; an element of $\Gamma(E)$ is a smooth map $\sigma : M \to E$ with $\pi \circ \sigma = \mathrm{id}_M$. $\mathfrak{X}(M) = \Gamma(TM)$ are vector fields. A **local frame** $(e_1, \dots, e_K)$ over an open $U \subseteq M$ is a tuple of local sections that is a basis of $E_p$ at every $p \in U$ (see [[Def - Local Frame]]). Greek indices $\alpha, \beta, \gamma, \dots$ range over fibre indices $1, \dots, K$; Latin indices $i, j, k, \dots$ over manifold coordinates $1, \dots, n$. Einstein summation is in force. For the parent symbol registry see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Axiom Motivation

The problem a connection solves is concrete and unavoidable. Take a section $\sigma$ of a vector bundle $E \to M$ — for instance, a vector field on a manifold, an electromagnetic wave function, a section of a tensor bundle. We want to *differentiate* $\sigma$: at each point $p$, what is the rate of change of $\sigma$ in some direction $X \in T_pM$? The naïve answer is that you compute $\sigma(p + tX)$ for small $t$, take the difference $\sigma(p + tX) - \sigma(p)$, and divide by $t$. But this difference is not even defined: $\sigma(p + tX)$ lives in the fibre $E_{p + tX}$, and $\sigma(p)$ lives in $E_p$, and these are *different vector spaces*. You cannot subtract them without first specifying an identification.

A **connection** is precisely a choice of identification. For each smooth path $\gamma$ in $M$ and each initial vector $v_0 \in E_{\gamma(0)}$, it specifies how to *parallel-transport* $v_0$ along $\gamma$ to give a vector in $E_{\gamma(t)}$ for each $t$. Once you have this, subtracting "$\sigma(\gamma(t))$ minus the parallel transport of $\sigma(\gamma(0))$" makes sense — both vectors now live in $E_{\gamma(t)}$ — and dividing by $t$ in the $t \to 0$ limit gives a well-defined directional derivative. The connection $\nabla$ packages this derivative as an operator: $\nabla_X\sigma(p)$ is the rate at which $\sigma$ deviates from its parallel transport, in the direction $X$, at $p$.

The axioms of a connection encode the minimum we want this operator to satisfy. First, **$\mathbb{R}$-linearity in the section** $\sigma$: $\nabla(a\sigma + b\tau) = a\nabla\sigma + b\nabla\tau$ for constants $a, b$. This is forced by saying "$\nabla$ is a derivative": linear combinations of sections differentiate by the same linear combination of their derivatives. Without this you would not have a derivative at all.

Second, the **Leibniz rule**: $\nabla(f\sigma) = f\nabla\sigma + \sigma \otimes df$ for $f \in C^\infty(M)$. This is the axiom that makes $\nabla$ *not* a tensor — for if $\nabla$ were $C^\infty(M)$-linear, it would be tensorial, and a tensorial map $\Gamma(E) \to \Gamma(E \otimes T^*M)$ is just an endomorphism of $E$ tensored with the identity on $T^*M$, which is far weaker than a derivative. The Leibniz rule says $\nabla$ "behaves like a derivative when applied to function-times-section": you get the derivative of the function (via $d$) plus the connection-derivative of the section. The need for this axiom is what makes a connection a *new* piece of structure, not derivable from the bundle alone. Drop Leibniz and you get just a $C^\infty$-linear operator; keep it and you get differentiation.

Why **two** axioms (linearity *and* Leibniz) rather than one? Because Leibniz alone does not characterize the operator. The zero map $\nabla\sigma = 0$ is not Leibniz (since $\nabla(f\sigma) = 0 \ne f \cdot 0 + \sigma \otimes df = \sigma \otimes df$ unless $df = 0$). And linearity alone admits non-derivatives like $\nabla\sigma = A(\sigma)$ for any $\mathrm{End}(E)$-valued 1-form $A$ (which is a tensor, not a derivative). The two axioms together force $\nabla$ to be genuinely the "rate of change minus tensorial endomorphism" — a true derivative.

Why is the codomain $\Gamma(E \otimes T^*M)$ and not just $\Gamma(E)$? Because we want $\nabla\sigma$ to encode "the derivative in *every* direction at once": at each $p \in M$, $\nabla\sigma(p)$ should be a linear map $T_pM \to E_p$, equivalently an element of $E_p \otimes T^*_pM$. Contracting with a specific direction $X$ then gives $\nabla_X\sigma(p) \in E_p$, the directional derivative.

The third axiom one often sees written — **$C^\infty(M)$-linearity in $X$**, namely $\nabla_{fX}\sigma = f\nabla_X\sigma$ — is automatic given the codomain choice. The connection $\nabla$ as written takes values in $\Gamma(E \otimes T^*M)$; contracting with $X$ gives a linear-over-$C^\infty$ result in $X$ because contraction is automatically $C^\infty$-bilinear. So the codomain encodes the directional-linearity for free.

A reader who has never seen this definition could invent it as follows. Start from "differentiate sections of $E$"; realize the problem of comparing fibres at different points; demand a derivative-like operator $\nabla : \Gamma(E) \to \text{?}$ that is linear and Leibniz; choose the codomain so that the resulting object is "a 1-form's worth of derivative", landing in $\Gamma(E \otimes T^*M)$. The axioms are forced once you accept the goal.

---

# The Definition

A **(linear, Koszul) connection** on a smooth vector bundle $E \to M$ is an $\mathbb{R}$-linear map

$$\nabla : \Gamma(E) \to \Gamma(E \otimes T^*M)$$

satisfying the **Leibniz rule**:

$$\nabla(f\sigma) = f\,\nabla\sigma + \sigma \otimes df \quad \text{for all } f \in C^\infty(M), \sigma \in \Gamma(E).$$

For a vector field $X \in \mathfrak{X}(M)$, the **covariant derivative along $X$** is the operator $\nabla_X : \Gamma(E) \to \Gamma(E)$ obtained by contraction:

$$\nabla_X\sigma := \langle\nabla\sigma, X\rangle = (\nabla\sigma)(X).$$

Equivalently, $\nabla_X$ is characterized by being $\mathbb{R}$-linear and $C^\infty(M)$-linear in $X$, $\mathbb{R}$-linear in $\sigma$, and satisfying $\nabla_X(f\sigma) = (Xf)\sigma + f\nabla_X\sigma$.

**Local frame description.** Let $(e_1, \dots, e_K)$ be a smooth local frame for $E$ over $U \subseteq M$. The connection is determined on $U$ by its action on the frame:

$$\nabla e_\beta = e_\alpha \otimes \omega^\alpha{}_\beta,$$

where $\omega = (\omega^\alpha{}_\beta)$ is a matrix of 1-forms on $U$ — the **connection 1-form** (or **connection matrix**, or **gauge potential**) in this frame. For an arbitrary section $\sigma = \sigma^\beta e_\beta$ on $U$, Leibniz gives

$$\nabla\sigma = (d\sigma^\alpha + \omega^\alpha{}_\beta\,\sigma^\beta)\,e_\alpha,$$

so that componentwise $(\nabla\sigma)^\alpha = d\sigma^\alpha + \omega^\alpha{}_\beta\sigma^\beta$ — the connection adds a matrix-times-section "correction" to the naïve componentwise exterior derivative.

**Change-of-frame transformation.** If $(e_U)$ and $(e_V)$ are two frames on $U \cap V$ related by $e_V = e_U \cdot c_{UV}$ (so $(e_V)_\beta = (e_U)_\alpha (c_{UV})^\alpha{}_\beta$) for a smooth $c_{UV} : U \cap V \to \mathrm{GL}(K)$, then the connection 1-forms $\omega_U$ and $\omega_V$ are related by

$$\omega_V = c_{UV}^{-1}\,\omega_U\,c_{UV} + c_{UV}^{-1}\,dc_{UV}.$$

The first term is conjugation (tensorial); the second is the **Maurer-Cartan correction** $c^{-1}dc$, an inhomogeneous piece that makes $\omega$ *not* a tensor.

---

# Categorical / Structural Definition

A connection is a **horizontal distribution** in the total space $E$. Concretely: at each point $e \in E$, the tangent space $T_eE$ has a canonical **vertical subspace** $V_eE = \ker(d\pi_e) = T_e(E_{\pi(e)})$ — directions along the fibre. A connection is a choice, smoothly varying in $e$, of complementary **horizontal subspace** $H_eE$ such that $T_eE = V_eE \oplus H_eE$ and $d\pi_e : H_eE \to T_{\pi(e)}M$ is an isomorphism. Given a curve $\gamma$ in $M$ and an initial $v_0 \in E_{\gamma(0)}$, lifting $\gamma$ to a curve $\tilde\gamma$ in $E$ with $\tilde\gamma(0) = v_0$ and $\tilde\gamma'(t) \in H_{\tilde\gamma(t)}E$ for all $t$ gives the parallel transport. The covariant derivative $\nabla_X\sigma$ at $p$ is then the projection onto $V_{\sigma(p)}E$ (canonically identified with $E_p$) of $d\sigma_p(X)$.

In the principal-bundle language ([[Gauge Theory III — Connections in Principal and Associated Bundles]]), the **principal connection** on the associated principal $\mathrm{GL}(K)$-bundle $P \to M$ is a $\mathfrak{gl}(K)$-valued 1-form $A$ on $P$ that is equivariant and reproduces the Maurer-Cartan form on vertical vectors. The pullback by a local section of $P$ (a local frame) gives the connection 1-form $\omega$ on $M$. The change-of-frame formula $\omega_V = c^{-1}\omega_U c + c^{-1}dc$ is precisely the inhomogeneous transformation law inherited from the equivariance of the principal connection.

---

# Relate to Other Fields / Compression

A connection is **"the choice of identification between nearby fibres"**. Without one, fibres at different points of $M$ are unrelated copies of $\mathbb{R}^K$; with one, you can compare and differentiate.

**In Riemannian geometry**, the [[Riemannian Geometry I — Connections and Covariant Differentiation|Levi-Civita connection]] is the unique connection on $TM$ that is (i) metric-compatible ($\nabla g = 0$) and (ii) torsion-free ($T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y] = 0$). This is the connection on a Riemannian manifold; it is *one specific instance* of the general vector-bundle connection, with the bundle being $TM$ and the additional Riemannian structure pinning down the choice.

**In gauge theory and physics**, the EM 4-potential $A_\mu$ is the connection 1-form of a $U(1)$-connection on a complex line bundle of wave functions (with $\omega = -ieA/\hbar$). The Yang-Mills field is the connection 1-form of a non-abelian $G$-connection (with $G = SU(2), SU(3)$, etc.). The Christoffel symbols $\Gamma^k{}_{ij}$ are the components of the connection 1-form for the Levi-Civita connection in a coordinate frame.

**In algebraic geometry**, holomorphic vector bundles on complex manifolds admit *holomorphic* connections only under restrictive conditions; the obstruction is the *Atiyah class*, a Dolbeault cohomology class in $H^1(M, \Omega^1 \otimes \mathrm{End}(E))$. This is one of many examples where the connection's existence is constrained by global topology.

**In number theory and arithmetic geometry**, connections on $\mathcal{D}$-modules over varieties capture the same data as differential equations whose solutions vary nicely with parameters; the *Gauss-Manin connection* on the cohomology of a family is the canonical example.

**True name:** A connection is **"the infinitesimal version of parallel transport"**. The formal definition (linear, Leibniz operator) is the check; the operational definition (specify how vectors are parallel-transported along curves) is what is used in practice. To say $\nabla_X\sigma = 0$ along a curve is to say $\sigma$ is parallel-transported by the connection along that curve. The covariant derivative *is* the deviation from parallelism.

---

# Examples / Corollaries

**Is an instance: Trivial connection on $M \times \mathbb{R}^K$.** With the global frame $(\partial_1, \dots, \partial_K)$ given by the standard basis of $\mathbb{R}^K$ at every point, set $\nabla\sigma = d\sigma$ componentwise: if $\sigma = (\sigma^1, \dots, \sigma^K)$ then $\nabla\sigma = (d\sigma^1, \dots, d\sigma^K)$. Connection matrix $\omega = 0$. Parallel transport: a section is parallel iff its components are constant. Curvature is zero, holonomy is trivial.

**Is an instance: Levi-Civita connection on $TM$ for a Riemannian manifold $M$.** Determined by the [[Def - Riemannian Metric|metric]] $g$ via the Koszul formula. In a coordinate frame $(\partial_i)$, the connection 1-form is $\omega^k{}_i = \Gamma^k{}_{ij}dx^j$, with the Christoffel symbols $\Gamma^k{}_{ij} = \frac{1}{2}g^{kl}(\partial_i g_{jl} + \partial_j g_{il} - \partial_l g_{ij})$. This is the connection that powers all of Riemannian geometry.

**Is an instance: Electromagnetic $U(1)$-connection on a wave-function line bundle.** On a complex line bundle $L \to M$ over spacetime $M$, set $\omega = -(ie/\hbar)A$ where $A$ is the EM 4-potential. The covariant derivative on a wave function $\psi \in \Gamma(L)$ is $\nabla_\mu\psi = \partial_\mu\psi - (ie/\hbar)A_\mu\psi$. This is the geometric origin of the minimal-coupling prescription in QED.

**Is an instance: Pullback of a connection.** If $\nabla$ is a connection on $E \to N$ and $f : M \to N$ is smooth, the pullback bundle $f^*E$ inherits a connection $f^*\nabla$ via $(f^*\nabla)_X(f^*\sigma) = f^*(\nabla_{df(X)}\sigma)$. This is how the Levi-Civita connection on a Riemannian manifold induces a connection on $TM$ restricted to any submanifold.

**Is NOT an instance: $\nabla\sigma = A(\sigma)$ for $A \in \Gamma(\mathrm{End}(E) \otimes T^*M)$ alone.** A $C^\infty(M)$-linear endomorphism is *tensorial*, not a derivative. It violates the Leibniz rule: $\nabla(f\sigma) = A(f\sigma) = fA(\sigma) = f\nabla\sigma$, whereas Leibniz demands $f\nabla\sigma + \sigma \otimes df$. The difference of *two* connections is, however, of this tensorial form — that's the affine-space structure (next).

**Corollary (difference of two connections is a tensor).** If $\nabla$ and $\widetilde{\nabla}$ are two connections on $E$, their difference $D = \widetilde{\nabla} - \nabla$ satisfies $D(f\sigma) = fD(\sigma)$ — the inhomogeneous Leibniz terms cancel. So $D \in \Gamma(\mathrm{End}(E) \otimes T^*M)$ is a tensor. Consequence: the **space of connections on $E$ is an affine space** modelled on the vector space of $\mathrm{End}(E)$-valued 1-forms.

**Corollary (existence of connections via partitions of unity).** Every smooth vector bundle over a paracompact manifold admits a connection. Proof: in each trivializing chart $U_\alpha$, the trivial connection works; given a [[Def - Partition of Unity on a Manifold|partition of unity]] $\{\rho_\alpha\}$ subordinate to the cover, $\nabla = \sum \rho_\alpha \nabla^\alpha$ is well-defined globally because $\sum\rho_\alpha = 1$ kills the inhomogeneous Leibniz piece (see [[Thm - Existence of Connections via Partitions of Unity]]).

**Corollary (parallel transport recovers $\nabla$).** Given a connection $\nabla$, define parallel transport $P_\gamma$ along curves by solving $\nabla_{\dot\gamma}\sigma = 0$ with prescribed initial value. Then $\nabla_X\sigma(p) = \lim_{t \to 0}\frac{P_{\gamma_t}^{-1}(\sigma(\gamma(t))) - \sigma(p)}{t}$ where $\gamma_t$ is a curve with $\gamma(0) = p$, $\dot\gamma(0) = X$, and $\gamma_t$ is the restriction to $[0, t]$. The connection is therefore equivalent to its parallel-transport law.

**Calibration check.** (1) Verify directly that the trivial connection on $M \times \mathbb{R}^K$ satisfies Leibniz. (2) Compute the connection 1-form of the Levi-Civita connection on $S^2$ with the round metric in a chart $(\theta, \phi)$ — answer: only $\Gamma^\theta{}_{\phi\phi} = -\sin\theta\cos\theta$ and $\Gamma^\phi{}_{\theta\phi} = \Gamma^\phi{}_{\phi\theta} = \cot\theta$ are non-zero. (3) Write down the covariant derivative $\nabla_\mu\psi$ for an EM wave function in the gauge $A_\mu = (\varphi, A_1, A_2, A_3)$ — answer: $(\partial_t + (ie/\hbar)\varphi)\psi$, $(\partial_i - (ie/\hbar)A_i)\psi$.

---

# Unlocked by This

> [!tip] Curvature, Holonomy, and Characteristic Classes *(from Differential Geometry, Algebraic Topology)*
> Once you have a connection $\nabla$, three things become available. (a) **Curvature** $F(X, Y) = \nabla_X\nabla_Y - \nabla_Y\nabla_X - \nabla_{[X,Y]}$ — see [[Def - Curvature of a Vector-Bundle Connection]] — is the obstruction to commutativity of covariant derivatives and equivalently the obstruction to parallel transport being path-independent for small loops. (b) **Holonomy** — parallel transport around closed loops based at $p$ gives a subgroup $\mathrm{Hol}_p(\nabla) \subseteq \mathrm{GL}(E_p)$ whose Lie algebra is generated by the curvature (**Ambrose-Singer theorem**). (c) **Characteristic classes** — appropriate polynomials in the curvature $F$ are closed differential forms whose cohomology classes do not depend on $\nabla$; these include the Chern classes (for complex bundles), Pontryagin classes (real), Euler class. They are topological invariants of $E$ alone.

> [!tip] Yang-Mills Theory and the Standard Model *(from Theoretical Physics)*
> Replacing the abelian structure group $U(1)$ of electromagnetism with a non-abelian compact Lie group $G$ — $SU(2)$ for the weak force, $SU(3)$ for the strong, $SU(2) \times U(1)$ for electroweak unification, $SU(3) \times SU(2) \times U(1)$ for the Standard Model — gives **non-abelian gauge theory** (Yang-Mills). The connection 1-form is now $\mathfrak{g}$-valued, the curvature includes the non-linear term $\omega \wedge \omega$, and the connection's "self-interaction" produces the gluon self-coupling of QCD and the W-Z-photon mixing of the electroweak sector. See [[Gauge Theory IV — Yang–Mills Fields and Instantons]].
