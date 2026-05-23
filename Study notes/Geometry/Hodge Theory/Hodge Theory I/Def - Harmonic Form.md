---
type: definition
subject: hodge-theory
prereqs:
  - "Def - Hodge Laplacian"
  - "Def - Exterior Derivative on a Manifold"
  - "Def - The Codifferential"
  - "Def - Closed and Exact Forms"
tags: [geometry, hodge-theory, differential-forms]
---

# Notation

$(M, g)$ is a smooth oriented Riemannian $n$-manifold (closed unless stated). The Hodge Laplacian on $k$-forms is $\Delta = d\delta + \delta d$ (see [[Def - Hodge Laplacian]]). The space of harmonic $k$-forms is $\mathcal{H}^k(M) = \ker(\Delta : \Omega^k(M) \to \Omega^k(M))$; we sometimes write $\mathcal{H}^k(M; g)$ to emphasize the metric dependence. A form satisfying both $d\omega = 0$ and $\delta\omega = 0$ is called a **harmonic field** (Frankel's terminology, useful for distinguishing from $\Delta\omega = 0$ on noncompact manifolds). On a closed Riemannian manifold the two notions coincide.

---

# Axiom Motivation

A harmonic form is defined as a form $\omega$ satisfying $\Delta\omega = 0$. The definition seems abstract — why this particular PDE? The motivation comes from three directions: variational, structural, and analogical.

**Variational motivation: harmonic forms are $L^2$-minima in their cohomology classes.** Consider the problem: among all forms $\omega$ in a fixed de Rham cohomology class $[\omega_0]$, which has the smallest $L^2$ norm? The class consists of $\omega_0 + d\eta$ for arbitrary $\eta \in \Omega^{k-1}(M)$, an infinite-dimensional affine subspace. The squared $L^2$ norm $\|\omega_0 + d\eta\|^2$ is a convex functional on $\eta$, so it has a unique minimum. Setting the first variation to zero: $0 = \frac{d}{dt}|_{t=0}\|\omega_0 + d(\eta + t\zeta)\|^2 = 2\langle\omega_0 + d\eta, d\zeta\rangle = 2\langle\delta(\omega_0 + d\eta), \zeta\rangle$ for all $\zeta$. So the minimizer $\omega := \omega_0 + d\eta$ satisfies $\delta\omega = 0$. It also satisfies $d\omega = d\omega_0 = 0$ since $[\omega] = [\omega_0]$ is a closed class. So the minimizer is *closed and coclosed*. The PDE $\Delta\omega = 0$ is exactly the Euler–Lagrange equation for this constrained minimization. The harmonic form is the *Dirichlet principle* minimizer, the canonical representative of the cohomology class.

**Structural motivation: harmonic forms are orthogonal to exact and coexact forms.** A form $\omega$ satisfies $\Delta\omega = 0$ on a closed Riemannian manifold iff $\omega$ is orthogonal in $L^2$ to both exact forms ($d\eta$ for $\eta \in \Omega^{k-1}$) and coexact forms ($\delta\gamma$ for $\gamma \in \Omega^{k+1}$). Proof: $\langle\omega, d\eta\rangle = \langle\delta\omega, \eta\rangle$, so $\omega \perp d\Omega^{k-1}$ iff $\delta\omega = 0$. Symmetrically, $\langle\omega, \delta\gamma\rangle = \langle d\omega, \gamma\rangle$, so $\omega \perp \delta\Omega^{k+1}$ iff $d\omega = 0$. Combining, $\omega$ is closed and coclosed iff $\omega \perp d\Omega^{k-1}$ and $\omega \perp \delta\Omega^{k+1}$. The space of harmonic forms is the orthogonal complement (in $L^2$) of the sum $d\Omega^{k-1} + \delta\Omega^{k+1}$.

**Analogical motivation: harmonic forms generalize harmonic functions.** On Euclidean $\mathbb{R}^n$ or on a Riemannian manifold, a **harmonic function** is one satisfying $\nabla^2 f = 0$, equivalently (in the Hodge convention) $\Delta f = 0$. Harmonic functions are critical: they minimize the Dirichlet energy $\int|\nabla f|^2$ for fixed boundary values; they enjoy the mean-value property and maximum principle; they are smooth (real-analytic, even). The Hodge Laplacian on $k$-forms extends this notion to higher-degree forms: a harmonic form satisfies a second-order elliptic PDE with the same structural properties (smoothness, mean-value, regularity), and its kernel on a closed manifold computes the cohomology of $M$.

**Why the equivalence "harmonic = closed and coclosed" requires closedness of $M$.** On a closed Riemannian manifold, $\Delta\omega = 0 \iff d\omega = 0 = \delta\omega$. Proof: $0 = \langle\Delta\omega, \omega\rangle = \|d\omega\|^2 + \|\delta\omega\|^2$, both nonnegative, both must vanish. On a noncompact manifold this equivalence breaks: the function $f(x, y) = e^x\cos y$ on $\mathbb{R}^2$ satisfies $\nabla^2 f = 0$ so $\Delta f = 0$, but $f$ is not constant — it is not a "trivial" element of the kernel of $\Delta$ in any cohomological sense. The infinite-dimensional kernel of $\Delta$ on $\mathbb{R}^n$ shows that on a noncompact manifold, "harmonic" is a much weaker condition than "represents a cohomology class". This is why Frankel reserves the term **harmonic field** for forms satisfying both $d\omega = 0$ and $\delta\omega = 0$ — the cohomologically meaningful condition — and distinguishes it from solutions of $\Delta\omega = 0$. On a closed manifold the two are identical.

**What if we strengthen — demand pointwise vanishing?** Then we get only the zero form, since $\omega \equiv 0$ is the only form with $\omega_p = 0$ pointwise. The harmonic condition is *much* weaker — it is an integral condition (or equivalent to a PDE), allowing $\omega$ to be nonzero pointwise but in a balanced way that integrates against test forms to zero. This is what makes harmonic forms an interesting class: they are nonzero, but each one is a critical point of an energy functional, like a quantum-mechanical ground state.

**What if we drop the Riemannian hypothesis?** Without a metric, $\delta$ does not exist, so $\Delta$ does not exist either, and "harmonic form" has no meaning. Harmonic forms are a *metric-dependent* concept — the same de Rham cohomology class can have different harmonic representatives for different metrics. The cohomology dimension $b_k(M)$ is metric-independent (topological), but the representatives are metric-dependent (geometric). This is the structural reason Hodge theory is a metric enrichment of de Rham theory.

---

# The Definition

Let $(M, g)$ be a smooth oriented Riemannian $n$-manifold. A differential $k$-form $\omega \in \Omega^k(M)$ is **harmonic** if
$$\Delta\omega = 0,$$
where $\Delta = d\delta + \delta d$ is the [[Def - Hodge Laplacian|Hodge Laplacian]].

The space of harmonic $k$-forms is
$$\mathcal{H}^k(M) := \{\omega \in \Omega^k(M) : \Delta\omega = 0\} = \ker(\Delta : \Omega^k(M) \to \Omega^k(M)).$$

**Closed-manifold characterization.** On a closed (compact, without boundary) oriented Riemannian manifold $M$,
$$\Delta\omega = 0 \iff d\omega = 0 \text{ and } \delta\omega = 0.$$
That is, harmonic = closed and coclosed simultaneously.

**Harmonic field.** On a general (possibly noncompact, possibly with boundary) Riemannian manifold, Frankel reserves the term **harmonic field** for a form satisfying $d\omega = 0$ and $\delta\omega = 0$ — the cohomologically meaningful condition — distinguishing it from solutions of $\Delta\omega = 0$ (which need not be closed or coclosed on a noncompact manifold).

---

# Relate to Other Fields / Compression

**On functions: harmonic = harmonic in the classical sense (with the Hodge sign).** For $f \in C^\infty(M)$, $\Delta f = -\nabla^2 f$ where $\nabla^2$ is the standard Laplace–Beltrami operator. So $\Delta f = 0 \iff \nabla^2 f = 0$, the classical harmonic-function condition. On a closed manifold, harmonic functions are *constant* (by the maximum principle, or by $\int|\nabla f|^2 = -\int f\nabla^2 f = 0$). So $\mathcal{H}^0(M) = \mathbb{R}^c$ where $c$ is the number of connected components.

**On $1$-forms in $\mathbb{R}^3$: harmonic = "Helmholtz harmonic" vector field.** A $1$-form $\alpha = a_i dx^i$ is harmonic iff its dual vector field $\vec A$ satisfies $\nabla\cdot\vec A = 0$ (divergence-free, i.e., $\delta\alpha = 0$) and $\nabla\times\vec A = 0$ (curl-free, i.e., $d\alpha = 0$). On compact $3$D Riemannian manifolds, harmonic $1$-forms are the **harmonic vector fields** of vector calculus — vector fields with both vanishing divergence and curl. The classical **Helmholtz decomposition** of a vector field $\vec F = \nabla\phi + \nabla\times\vec A + \vec H$ has $\vec H$ as the harmonic part, completing the Hodge decomposition $\Omega^1 = d\Omega^0 + \delta\Omega^2 + \mathcal{H}^1$ in dimension $3$.

**True name:** a harmonic form is the *unique $L^2$-minimum representative* of its de Rham cohomology class on a closed Riemannian manifold. The PDE characterization $\Delta\omega = 0$ is the Euler–Lagrange equation for this variational principle; the algebraic characterization "closed and coclosed" is the orthogonality characterization derived from the variational principle.

A second-deeper "true name" comes from the heat semigroup: a harmonic form is the *long-time limit* of the heat-flow on forms, $\omega_\infty = \lim_{t\to\infty}e^{-t\Delta}\omega_0$ in $L^2$. Every initial form decays to its harmonic projection under the heat flow, and harmonic forms are the equilibria — the stationary points of the form-heat-equation $\partial_t\omega = -\Delta\omega$.

---

# Examples / Corollaries

**Is an instance: constant forms on a torus.** On the flat $n$-torus $T^n = \mathbb{R}^n/\mathbb{Z}^n$ with the flat metric, the constant-coefficient $k$-forms $\sum c_I dx^I$ are harmonic for any constants $c_I \in \mathbb{R}$. Verification: $d(c_I dx^I) = 0$ (closed, since coefficients are constants), and $\delta(c_I dx^I)$ involves derivatives of $c_I$, which vanish. So both $d\omega = 0$ and $\delta\omega = 0$. Conversely, every harmonic $k$-form on the flat torus is constant-coefficient (by Fourier analysis: nonzero modes have positive eigenvalue). Hence $\dim\mathcal{H}^k(T^n) = \binom{n}{k}$, matching the Betti numbers $b_k(T^n) = \binom{n}{k}$.

**Is an instance: the volume form on a closed orientable $n$-manifold.** $\operatorname{vol}_g \in \Omega^n(M)$ is closed ($d$ of any top-degree form is zero, since $\Omega^{n+1} = 0$) and coclosed ($\delta\operatorname{vol}_g$ is a $-1$-form, which doesn't exist, but the calculation $\delta\operatorname{vol}_g = \pm\star d\star\operatorname{vol}_g = \pm\star d 1 = 0$ confirms it). So $\operatorname{vol}_g \in \mathcal{H}^n(M)$. This is the unique (up to scalar) harmonic $n$-form on a closed connected orientable manifold, generating $H^n(M; \mathbb{R}) \cong \mathbb{R}$.

**Is an instance: harmonic $1$-forms on a closed Riemann surface.** A compact Riemann surface $\Sigma_g$ of genus $g$ has $\dim\mathcal{H}^1(\Sigma_g) = 2g = b_1(\Sigma_g)$. Geometrically, these are realized as the real and imaginary parts of the $g$ holomorphic $1$-forms on $\Sigma_g$ — the "abelian differentials" of classical Riemann-surface theory. The fact that harmonic $1$-forms are paired with holomorphic differentials is the start of complex Hodge theory.

**Is NOT an instance: $e^x\cos y$ on $\mathbb{R}^2$.** The function $f(x, y) = e^x\cos y$ satisfies $\nabla^2 f = 0$ (Cauchy–Riemann), so $\Delta f = 0$. But $f$ is not in $L^2$ — it grows exponentially. And $f$ is not constant — so it is not a "trivial" element of $\mathcal{H}^0(\mathbb{R}^2)$. On $\mathbb{R}^2$, the kernel of $\Delta$ (as a differential operator) is the entire space of harmonic functions, which is infinite-dimensional. The cohomologically meaningful kernel — the $L^2$ harmonic forms — is *zero*, because $\mathbb{R}^2$ has $b_0 = 1$ but the constants are not in $L^2$ on $\mathbb{R}^2$. This non-example illustrates that **on a noncompact manifold, the kernel of $\Delta$ is much larger than $\mathcal{H}^k$ in the cohomological sense.**

**Is NOT an instance: a closed non-coclosed form on a closed manifold.** If $\omega$ is closed but not coclosed, $\Delta\omega \neq 0$ and so $\omega \notin \mathcal{H}^k$. Concretely: on the flat $T^2$ with coordinates $(x, y)$, the $1$-form $\omega = \sin(x)\,dy$ is closed ($d\omega = \cos(x)\,dx\wedge dy - 0 = \cos(x)\,dx\wedge dy \neq 0$ — wait, $d(\sin(x)\,dy) = \cos(x)\,dx\wedge dy$). So actually $\omega = \sin(x)dy$ is not closed. A better example: $\omega = \cos(x)\,dy$, then $d\omega = -\sin(x)\,dx\wedge dy \neq 0$, also not closed. The form $\omega = dx$ is closed and coclosed (constant coefficient), hence harmonic. Trying to break this: $\omega = f(x, y)\,dx$ is closed iff $\partial_y f = 0$ (so $f = f(x)$), and coclosed iff $\delta\omega = -\partial_x f = 0$, i.e., $f$ is constant. So on the torus, the closed-not-coclosed $1$-forms don't exist nontrivially in this basis — for the example, take $\omega = \sin(2\pi x)\,dy + \cos(2\pi y)\,dx$, which is *not* closed; the closed cohomologous form is the Hodge harmonic representative, which is the constant-coefficient projection.

**Corollary (smoothness of harmonic forms).** On a closed Riemannian manifold, every harmonic $k$-form is smooth (in fact real-analytic). This is **elliptic regularity** for the Hodge Laplacian. Even if one starts with an $L^2$ form satisfying $\Delta\omega = 0$ weakly, the regularity theory of elliptic operators (Sobolev embedding, bootstrapping) forces $\omega$ to be smooth. This is what makes the smooth and $L^2$ versions of Hodge theory agree.

**Corollary (mean-value property for harmonic functions).** On a Riemannian manifold, harmonic functions enjoy a mean-value property over geodesic balls: $f(p) = \frac{1}{\mathrm{vol}(B_r(p))}\int_{B_r(p)} f\,\operatorname{vol}_g$ for small $r$, with an error of order $r^2\cdot\mathrm{scalar\ curvature}$. The classical Euclidean mean-value property is the $\mathbb{R}^n$ case. The generalization to harmonic forms involves more subtle integration over higher-dimensional spheres, but a version of the mean-value property holds.

**Calibration check.** If you can verify (i) constant functions on a closed manifold are harmonic (and they are the only harmonic functions, by the maximum principle), (ii) constant-coefficient forms on a flat torus are harmonic, and (iii) $e^x\cos y$ on $\mathbb{R}^2$ satisfies $\Delta f = 0$ as a differential equation but is not "harmonic" in the cohomological sense, you have understood the definition and its scope correctly.

---

# Unlocked by This

> [!tip] Hodge Decomposition Theorem *(from Hodge Theory)*
> The space $\mathcal{H}^k(M)$ of harmonic $k$-forms is one of the three orthogonal summands in the **Hodge decomposition** $\Omega^k(M) = \mathcal{H}^k(M) \oplus d\Omega^{k-1}(M) \oplus \delta\Omega^{k+1}(M)$ on a closed oriented Riemannian manifold. The harmonic summand is finite-dimensional, equal in dimension to the $k$-th Betti number, and gives a canonical representative for each de Rham cohomology class. See [[Thm - Hodge Decomposition Theorem]].

> [!tip] Harmonic Maps Between Manifolds *(from Geometric Analysis)*
> The notion of "harmonic" generalizes beyond forms to **harmonic maps**: a smooth map $\varphi : (M, g) \to (N, h)$ between Riemannian manifolds is harmonic if it is a critical point of the **Dirichlet energy** $E(\varphi) = \frac{1}{2}\int_M |d\varphi|^2 \operatorname{vol}_g$. The Euler–Lagrange equation is a nonlinear PDE — the **harmonic map equation** $\tau(\varphi) = 0$ where $\tau$ is the "tension field" — which reduces to the linear Laplace equation when the target is Euclidean. Harmonic maps unify many examples: harmonic functions ($N = \mathbb{R}$), geodesics ($M = \mathbb{R}$), holomorphic maps between Kähler manifolds. **Eells–Sampson** proved existence of harmonic maps from any compact Riemannian manifold to a target with nonpositive sectional curvature, by the heat flow method.

> [!tip] Quantum Mechanics on Manifolds *(from Mathematical Physics)*
> Harmonic forms have a quantum-mechanical interpretation: on a Riemannian manifold $M$ viewed as a configuration space, the Hodge Laplacian $\Delta$ on forms is a Hamiltonian for a supersymmetric quantum-mechanical system. The harmonic forms are the **ground states** of this Hamiltonian (zero-energy eigenstates), and the dimensions $\dim\mathcal{H}^k(M) = b_k(M)$ are the **Witten indices**, counting supersymmetric vacua graded by **fermion number** (= form degree). Witten's analytic proof of the Morse inequalities is the deformation of this quantum system by a Morse function, with the small-energy spectrum localizing at the critical points. This is the gateway to the supersymmetric viewpoint on topology and to **Floer homology** in infinite-dimensional settings.
