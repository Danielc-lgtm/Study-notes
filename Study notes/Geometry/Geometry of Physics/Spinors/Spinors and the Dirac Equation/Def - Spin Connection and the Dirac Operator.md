---
type: definition
subject: spinors
prereqs:
  - "Def - Spin Structure on a Manifold"
  - "Def - Dirac Gamma Matrices"
  - "Def - Riemannian Manifold"
tags: [geometry, spinors, differential-geometry]
---

# Notation

Let $M$ be an oriented Riemannian (or pseudo-Riemannian) spin manifold of dimension $n$. The spinor bundle is $SM \to M$. An **orthonormal frame** is a local section $e = (e_1, \ldots, e_n)$ of the frame bundle $P_{SO}$, with dual coframe $\theta^a$ satisfying $\theta^a(e_b) = \delta^a_b$. We use **Latin indices** $a, b, c, \ldots$ for frame components and **Greek indices** $\mu, \nu, \ldots$ for coordinate components. The Levi-Civita connection 1-form is $\omega^a_{\;b}$, antisymmetric in the orthonormal frame: $\omega^a_{\;b} = -\omega^b_{\;a}$. Cliifford generators on the spinor bundle: $\gamma_a$ for $a = 1, \ldots, n$ satisfying $\{\gamma_a, \gamma_b\} = 2g_{ab} I = 2\eta_{ab} I$. The covariant derivative on spinors is $\nabla^S$; the Dirac operator is $\not D$.

This is a compound page: it defines two interlocking notions — the **spin connection** $\nabla^S$ and the **Dirac operator** $\not D$ — because the Dirac operator is by definition Clifford contraction of the spin connection, and neither is fully usable without the other.

---

# Axiom Motivation

On flat Minkowski space we had the Dirac operator $\not\partial = \gamma^\mu\partial_\mu$, a first-order linear differential operator on $\mathbb{C}^4$-valued functions, whose square was the d'Alembertian. To define an analogous operator on a curved spin manifold $M$, we need to address two issues:

1. **The derivative $\partial_\mu$ depends on coordinates.** On a manifold, the partial derivative of a vector-valued function transforms badly under change of coordinates; we need a **covariant derivative** to fix this. The natural choice is to use the Levi-Civita connection — but it acts on $TM$ (vectors), not on $SM$ (spinors).

2. **The gamma matrices $\gamma^\mu$ must be defined with respect to an orthonormal frame.** On flat space we used the standard frame globally; on a manifold there is no global orthonormal frame in general (unless $M$ is parallelizable). We need to choose a frame patch-by-patch and ensure the Dirac operator is well-defined.

The construction proceeds in two steps. **Step 1**: lift the Levi-Civita connection $\nabla^{LC}$ on $TM$ (or equivalently on $P_{SO}$) to a connection $\nabla^S$ on $SM$ (the spinor bundle). The natural method: the connection on $P_{SO}$ is described by a 1-form $\omega^a_{\;b}$ with values in $\mathfrak{so}(n)$ (the Lie algebra of $SO(n)$); since $\mathfrak{spin}(n) \cong \mathfrak{so}(n)$ as Lie algebras (the covering map is an iso on Lie algebras), the *same* 1-form gives a connection on $P_{\mathrm{Spin}}$, and hence by associated-bundle construction a connection on $SM = P_{\mathrm{Spin}} \times_\rho \mathbb{C}^N$. The explicit formula uses the Clifford bivector $\tfrac{1}{4}[\gamma_a, \gamma_b] = \tfrac{1}{2}\gamma_a\gamma_b$ (for $a \neq b$) as the spinor generator of an infinitesimal rotation:
$$\nabla^S_X \psi = X(\psi) + \tfrac{1}{4}\omega^{ab}(X)\gamma_a\gamma_b\psi.$$
This is the **spin connection**: it is the unique connection on $SM$ that is compatible with the Clifford multiplication and reduces to the Levi-Civita connection on the vector representation.

**Step 2**: define the Dirac operator as the Clifford-contraction of $\nabla^S$:
$$\not D \psi = \gamma^a e_a^\mu \nabla^S_\mu \psi = \gamma^a \nabla^S_{e_a}\psi.$$
This is the natural first-order linear operator on spinor sections that is *frame-independent*: under a change of orthonormal frame $e_a \mapsto e_a' = \Lambda^b_{\;a} e_b$ for $\Lambda \in SO(n)$ (varying smoothly with point), both $\gamma^a$ and $\nabla^S_{e_a}$ transform, and the Clifford contraction is invariant.

Why is the bivector $\tfrac{1}{4}\gamma_a\gamma_b$ the right generator? Because under the spin representation, an infinitesimal rotation in the $a$-$b$ plane (generator $E_{ab} \in \mathfrak{so}(n)$) lifts to the spinor-space infinitesimal action $\tfrac{1}{4}[\gamma_a, \gamma_b] = \tfrac{1}{2}\gamma_a\gamma_b$ (for $a \neq b$, where the commutator equals twice the product). The Lie-algebra isomorphism $\mathfrak{so}(n) \to \mathfrak{spin}(n) \subset \mathrm{Cl}(n)$ sends $E_{ab} \to \tfrac{1}{2}\gamma_a\gamma_b$, and so a *vector-bundle* connection $\omega^a_{\;b}E_a^{\;b}$ becomes a *spinor-bundle* connection via $\nabla^S - d = \tfrac{1}{4}\omega^{ab}\gamma_a\gamma_b$.

What if we used the matrix commutator $\tfrac{1}{2}[\gamma_a, \gamma_b]$ directly? This gives the right answer for $a \neq b$, since $\tfrac{1}{2}[\gamma_a, \gamma_b] = \gamma_a\gamma_b$ when $\{\gamma_a, \gamma_b\} = 0$. The factor of $\tfrac{1}{4}$ in the standard convention $\nabla^S = d + \tfrac{1}{4}\omega^{ab}\gamma_a\gamma_b$ (summing over all $a, b$, *not* just $a < b$) accounts for the double-counting in summing over all pairs; equivalently, $\nabla^S = d + \tfrac{1}{2}\omega^{ab}\gamma_a\gamma_b$ if you sum over $a < b$ only.

The Dirac operator satisfies a **square formula** — the Lichnerowicz formula $\not D^2 = -\nabla^{S*}\nabla^S + R/4$ — which is the curved analog of $\not\partial^2 = \Box$ on flat space, with the additional scalar-curvature term being a "geometric correction". See [[Thm - Lichnerowicz Formula]].

---

# The Definition

Let $M$ be an oriented Riemannian (or pseudo-Riemannian) spin manifold of dimension $n$, with a chosen [[Def - Spin Structure on a Manifold|spin structure]] and associated spinor bundle $SM \to M$. Let $e = (e_1, \ldots, e_n)$ be a local orthonormal frame on $M$ with Levi-Civita connection 1-forms $\omega^a_{\;b}$ (so $\nabla^{LC}_X e_b = \omega^a_{\;b}(X) e_a$, with $\omega^a_{\;b} = -\omega^b_{\;a}$ in the orthonormal frame). Let $\gamma_a$ be the Clifford generators acting on the spinor bundle, satisfying $\{\gamma_a, \gamma_b\} = 2g_{ab} \cdot \mathrm{id}_{SM}$.

The **spin connection** $\nabla^S$ on $SM$ is defined by
$$\nabla^S_X \psi = X(\psi) + \tfrac{1}{4}\omega^{ab}(X)\gamma_a\gamma_b\psi,$$
where the sum is over all pairs $a, b = 1, \ldots, n$ (with antisymmetry of $\omega^{ab}$ ensuring the term is well-defined), and $\omega^{ab} = g^{ac}\omega^b_{\;c}$. Equivalently, summing only over $a < b$ with double-coefficient:
$$\nabla^S_X \psi = X(\psi) + \tfrac{1}{2}\sum_{a < b}\omega^{ab}(X)\gamma_a\gamma_b\psi.$$

The **Dirac operator** on $SM$ is the Clifford-contraction of $\nabla^S$:
$$\not D \psi := \gamma^a \nabla^S_{e_a}\psi = \gamma^a e_a^\mu \nabla^S_\mu \psi.$$
Equivalently, in coordinate form using $\gamma^\mu = \gamma^a e_a^\mu$:
$$\not D\psi = \gamma^\mu \nabla^S_\mu \psi = \gamma^\mu(\partial_\mu + \tfrac{1}{4}\omega^{ab}_{\mu}\gamma_a\gamma_b)\psi.$$

The Dirac operator is a **first-order linear differential operator** on sections of $SM$. In Riemannian signature it is **elliptic**; in Lorentzian signature it is **hyperbolic**.

**Properties:**

1. **Frame-independence:** Under a change of orthonormal frame $e \mapsto e' = e \cdot \Lambda$ for $\Lambda: U \to SO(n)$ a smooth map, both the connection 1-form and the gamma matrices transform, but the operator $\not D$ is unchanged.

2. **Self-adjointness (Riemannian):** On a closed Riemannian spin manifold, $\not D$ is formally self-adjoint with respect to the natural Hermitian inner product on spinors: $\langle\not D\psi, \phi\rangle = \langle\psi, \not D\phi\rangle$.

3. **Chirality in even dimensions:** When $n = 2k$, the Dirac operator anticommutes with the chirality $\gamma^{n+1} = \gamma^5$ (the volume element times $i$ for the right sign), so $\not D$ splits as $\not D = \begin{pmatrix} 0 & \not D^- \\ \not D^+ & 0\end{pmatrix}$ with $\not D^\pm: \Gamma(S^\pm) \to \Gamma(S^\mp)$ — Dirac operator maps positive chirality to negative and vice versa.

4. **Square (Lichnerowicz formula):** On a closed Riemannian spin manifold, $\not D^2 = -\nabla^{S*}\nabla^S + R/4$ where $\nabla^{S*}\nabla^S$ is the connection Laplacian and $R$ is the scalar curvature. See [[Thm - Lichnerowicz Formula]].

---

# Categorical / Structural Definition

The spin connection is the **unique connection on the spinor bundle that is compatible with the Levi-Civita connection on the tangent bundle via the Clifford action**: more precisely, the unique $\nabla^S$ on $SM$ such that the Clifford multiplication $c: TM \otimes SM \to SM$ satisfies the **Leibniz rule**
$$\nabla^S_X(c(Y, \psi)) = c(\nabla^{LC}_X Y, \psi) + c(Y, \nabla^S_X \psi).$$
This is the natural compatibility condition between the two bundles' connections; the spin connection is what makes the Clifford bundle a *parallel object* in the relevant sense.

Categorically, the spin connection arises as the **lift of the Levi-Civita connection along the double cover** $\mathrm{Spin}(n) \to SO(n)$: the Levi-Civita connection is a connection 1-form $\omega$ on $P_{SO}$ with values in $\mathfrak{so}(n)$; pulled back to $P_{\mathrm{Spin}}$ via the cover (and using $\mathfrak{spin}(n) \cong \mathfrak{so}(n)$), it gives a connection on $P_{\mathrm{Spin}}$, which by associated-bundle construction gives a connection on $SM$. This lift is *unique* because the cover is $2:1$ on the group but the *identity* on Lie algebras.

The Dirac operator $\not D = c \circ \nabla^S$ is the composition of the spin covariant derivative with the Clifford multiplication, viewed as a map $\Gamma(SM) \to \Gamma(SM)$ (the Clifford-multiplication step contracts the $T^*M$ index from $\nabla^S\psi \in \Gamma(T^*M \otimes SM)$ with the $TM$-valued index in the Clifford action). It is the **canonical first-order linear differential operator on $SM$**, just as $d$ is canonical on $\Lambda^* M$.

---

# Relate to Other Fields / Compression

**True name (spin connection):** The spin connection is *the Levi-Civita connection lifted to the spinor bundle via the Clifford bivector lift of the Lie algebra*. Operationally, the formula $\nabla^S_X = X + \tfrac{1}{4}\omega^{ab}(X)\gamma_a\gamma_b$ is the explicit recipe.

**True name (Dirac operator):** $\not D$ is the *Clifford-contracted spin covariant derivative*, equivalently the *natural first-order elliptic (in Riemannian signature) operator on the spinor bundle*, which on flat space reduces to $\gamma^\mu\partial_\mu$. It is the **square root of the Laplacian** (with a curvature correction), and is the fundamental object of spin geometry.

Connections:

- **Hodge theory.** The Dirac operator on the spinor bundle is the spin-geometric analog of the **Hodge–de Rham operator** $d + d^*$ acting on forms (see [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]]). Both square to Laplacian-like operators; both have finite-dimensional kernels on closed manifolds (giving rise to topological invariants); both fit into index-theoretic frameworks (the de Rham Laplacian gives the Euler characteristic, the Dirac operator gives the $\hat A$-genus).
- **Yang–Mills / gauge theory.** Twisting the spinor bundle by a vector bundle $E$ with connection $A$ gives the twisted Dirac operator $\not D_E$, central to the Seiberg–Witten equations and to the Atiyah–Singer index theorem in its general form. See [[Gauge Theory IV — Yang–Mills Fields and Instantons]].
- **General relativity.** On a curved Lorentzian spacetime with a chosen spin structure, the Dirac equation $\not D\psi = m\psi$ describes spin-$\tfrac{1}{2}$ matter in a gravitational field. The curvature correction $R/4$ in the Lichnerowicz formula tells us that scalar curvature *directly* affects the Dirac spectrum — a fact used by Witten in his proof of the **positive mass theorem**.

---

# Examples / Corollaries

**Example 1: Flat space.** On $\mathbb{R}^n$ (or $\mathbb{R}^{1,3}$) with the standard frame, the Levi-Civita connection 1-form is zero ($\omega^{ab} = 0$), so $\nabla^S = d$ and $\not D = \gamma^a \partial_a = \gamma^\mu\partial_\mu = \not\partial$ — the flat-space Dirac operator we started with.

**Example 2: Sphere $S^n$.** Use the round metric and standard orthonormal frame; the Levi-Civita connection 1-form has the symmetric, totally-antisymmetric structure dictated by constant positive curvature. The Dirac operator on $S^n$ has explicitly computable spectrum (Friedrich, 1980s): the eigenvalues are $\pm(k + n/2)$ for $k = 0, 1, 2, \ldots$, with multiplicities related to spherical harmonics. The Lichnerowicz formula gives a lower bound on these eigenvalues from the scalar curvature; the spherical metric saturates the bound (the **Friedrich inequality** $\lambda^2 \geq (n/(4(n-1)))R$).

**Example 3: Torus $T^n$ with flat metric.** The Levi-Civita connection is flat ($\omega = 0$ in standard coordinates), so $\not D = \gamma^a\partial_a$. The spectrum is computed by Fourier series; the spectrum (including whether $0$ is an eigenvalue) depends on the *choice of spin structure* — different spin structures correspond to periodic vs antiperiodic boundary conditions, giving different sets of allowed momenta.

**Example 4: Lichnerowicz operator on Berger spheres.** The **Berger sphere** is a $1$-parameter family of metrics on $S^3$ deforming the round metric by squashing along the Hopf fibers. The scalar curvature varies along the deformation, and the Dirac spectrum changes correspondingly; this is a tractable explicit example of the Lichnerowicz formula in action.

**Non-example: a "Dirac operator" on a non-spin manifold.** On $\mathbb{CP}^2$ (which has $w_2 \neq 0$, so no spin structure), one cannot define a global spinor bundle — the construction of the spin connection runs into the obstruction of $w_2$. The fix is to use a $\mathrm{Spin}^c$ structure instead, which gives a $\mathrm{Spin}^c$ Dirac operator. The Seiberg–Witten equations exploit exactly this.

**Non-example: an "improper" connection on $SM$.** The "naive" choice $\nabla^S_X\psi = X(\psi)$ — i.e., the flat coordinate derivative — is *not* well-defined globally, because the spinor field $\psi$ has components in a basis that itself varies from point to point (the spin frame), and ignoring this dependence leads to a non-covariant operator. The $\tfrac{1}{4}\omega^{ab}\gamma_a\gamma_b$ correction is exactly what fixes this.

**Calibration check.** A reader should verify: (i) explicit calculation: $\nabla^S_X(\gamma_a) = -\omega^b_{\;a}(X)\gamma_b$, the same as the Levi-Civita derivative of $e_a$ — showing the spin connection respects Clifford structure; (ii) on flat space $\nabla^S = d$ and $\not D = \not\partial$; (iii) under a frame rotation $e \mapsto e \cdot \Lambda$, the spin connection 1-form transforms as $\omega \mapsto \Lambda^{-1}\omega\Lambda + \Lambda^{-1}d\Lambda$ (standard gauge transformation law).

---

# Unlocked by This

> [!tip] Lichnerowicz Formula and Positive Scalar Curvature
> The **Lichnerowicz formula** $\not D^2 = \nabla^{S*}\nabla^S + R/4$ (see [[Thm - Lichnerowicz Formula]]) is the central identity of Dirac-operator analysis on curved manifolds. Its most immediate consequence is the **Lichnerowicz vanishing theorem**: on a closed Riemannian spin manifold with strictly positive scalar curvature, $\ker \not D = 0$ (no nontrivial harmonic spinors). Combined with the Atiyah–Singer index theorem, this gives the topological obstruction $\hat A(M) = 0$ to admitting positive-scalar-curvature metrics on a spin manifold — a deep constraint discovered by Hitchin (1974) for K3 surfaces and generalized widely.

> [!tip] Index of the Dirac Operator
> On a closed Riemannian spin manifold $M^{2k}$, the chirality decomposition $SM = S^+ \oplus S^-$ splits the Dirac operator into $\not D^\pm: \Gamma(S^\pm) \to \Gamma(S^\mp)$. The **index** is
> $$\mathrm{ind}\,\not D^+ = \dim\ker\not D^+ - \dim\ker\not D^-,$$
> a Fredholm-theoretic invariant. The **Atiyah–Singer index theorem** computes this analytical index as a topological one:
> $$\mathrm{ind}\,\not D^+ = \int_M \hat A(M),$$
> where $\hat A(M)$ is the $\hat A$-genus. This is the foundational instance of index theory in spin geometry, and is the source of many specific results: the Atiyah–Singer-Hirzebruch signature theorem (twisting by an appropriate bundle), Riemann–Roch (in the Kähler case), and the Gauss–Bonnet–Chern theorem (via the Euler operator).

> [!tip] Twisted Dirac Operator and Gauge Coupling
> When the Dirac operator is **twisted** by a vector bundle $E \to M$ with connection $A$, one obtains the **twisted Dirac operator** $\not D_E: \Gamma(SM \otimes E) \to \Gamma(SM \otimes E)$ defined using both the spin connection and the gauge connection. The twisted Lichnerowicz formula reads
> $$\not D_E^2 = -\nabla^*\nabla + R/4 + \tfrac{1}{2}\sum_{a < b}\gamma_a\gamma_b F_E(e_a, e_b),$$
> where $F_E$ is the curvature of $A$. This twisted version is central to physics: in the Standard Model, the Dirac operator coupling fermions to gauge fields is exactly $\not D_E$ with $E$ the appropriate gauge representation. Its index counts chiral zero modes in instanton backgrounds — the basis of the chiral anomaly and of the Seiberg–Witten invariants.
