---
type: definition
subject: hodge-theory
prereqs:
  - "Def - Exterior Derivative on a Manifold"
  - "Def - The Codifferential"
  - "Def - The L2 Inner Product on Differential Forms"
  - "Def - Riemannian Manifold"
tags: [geometry, hodge-theory, differential-forms, elliptic-operators]
---

# Notation

$(M, g)$ is a smooth oriented (pseudo-)Riemannian $n$-manifold; the closed Riemannian case is the default. The exterior derivative is $d : \Omega^k(M) \to \Omega^{k+1}(M)$ (see [[Def - Exterior Derivative on a Manifold]]); the codifferential is $\delta : \Omega^k(M) \to \Omega^{k-1}(M)$ (see [[Def - The Codifferential]]). The Hodge Laplacian (also called **Laplace–de Rham operator** or simply the **form Laplacian**) is $\Delta : \Omega^k(M) \to \Omega^k(M)$, given by $\Delta = d\delta + \delta d$. We sometimes write $\nabla^2 := -\Delta$ to recover the negative-of-Hodge convention familiar from Euclidean PDE; on functions, $\nabla^2 f$ is then the usual Laplace–Beltrami operator.

> [!warning] Convention: sign of $\Delta$ vs $\nabla^2$
> The Hodge Laplacian $\Delta = d\delta + \delta d$ is *nonnegative*: $\langle\Delta\omega,\omega\rangle = \|d\omega\|^2 + \|\delta\omega\|^2 \geq 0$. The Euclidean Laplacian $\nabla^2 = \sum\partial_i^2$ is *nonpositive*: $\langle\nabla^2 f, f\rangle = -\int|\nabla f|^2 \leq 0$. So $\Delta = -\nabla^2$ on Euclidean functions, with the sign flip ensuring $\Delta \geq 0$. This is the *standard* Hodge-theoretic convention and is the source of much sign-confusion when switching between conventions; see the warning callout in [[Hodge Theory I — Harmonic Forms and the Hodge Decomposition]].

---

# Axiom Motivation

The Hodge Laplacian is the canonical second-order differential operator on $\Omega^k(M)$ that combines $d$ and $\delta$ symmetrically. Four structural pressures force the definition.

**Why combine $d$ and $\delta$?** The exterior derivative $d : \Omega^k \to \Omega^{k+1}$ raises degree by $1$; the codifferential $\delta : \Omega^k \to \Omega^{k-1}$ lowers degree by $1$. On their own, neither preserves the space $\Omega^k$. To get a self-map of $\Omega^k$ from first-order operators, we must combine them: $d\delta : \Omega^k \to \Omega^{k+1} \to \Omega^{k+2}$? No, $\delta$ first lowers to $\Omega^{k-1}$ then $d$ raises to $\Omega^k$. Wait: $d\delta\beta = d(\delta\beta)$ for $\beta \in \Omega^k$: $\delta\beta \in \Omega^{k-1}$, $d\delta\beta \in \Omega^k$. Yes — $d\delta : \Omega^k \to \Omega^k$. Similarly $\delta d : \Omega^k \to \Omega^k$ via $\delta d\beta = \delta(d\beta) \in \Omega^k$. Adding them gives $\Delta = d\delta + \delta d : \Omega^k \to \Omega^k$, a self-map.

**Why the sum, not just one of them?** Each summand alone has a "trivial direction": $d\delta\beta = 0$ if $\delta\beta = 0$ (i.e., $\beta$ coclosed); $\delta d\beta = 0$ if $d\beta = 0$ (i.e., $\beta$ closed). The sum $\Delta\beta = 0$ requires *both* $d\delta\beta = 0$ and $\delta d\beta = 0$ — and on a closed Riemannian manifold, this is equivalent to $d\beta = 0$ and $\delta\beta = 0$ (the harmonic condition). Using just $d\delta$ or just $\delta d$ would give an operator whose kernel is too large; the *sum* singles out exactly the harmonic forms.

**Why a Laplacian-like name?** On $0$-forms (functions), $d\delta f = d \cdot 0 = 0$ (since $\delta f = 0$), and $\delta d f = \delta(df) = -\nabla^2 f$ (negative Laplace–Beltrami; see [[Def - The Codifferential]]). So $\Delta f = -\nabla^2 f$ on functions — it agrees up to sign with the standard Riemannian Laplacian on scalars. The Hodge Laplacian on functions *is* the Laplace–Beltrami operator (up to sign), justifying the name. On higher forms it generalizes the Laplacian to act on differential forms of any degree.

**Why $\Delta = (d + \delta)^2$?** A beautiful structural fact: $(d + \delta)^2 = d^2 + d\delta + \delta d + \delta^2 = d\delta + \delta d = \Delta$ (since $d^2 = 0$ and $\delta^2 = 0$). So the Hodge Laplacian is the *square* of the first-order self-adjoint operator $D = d + \delta$ on the total form space $\Omega^\bullet(M)$. This is the form-analogue of "the Laplacian is the square of the Dirac operator," and is the foundation of the heat-kernel and supersymmetric proofs of index theorems. The operator $D$ does not preserve degree (it shifts by $\pm 1$), but $D^2 = \Delta$ does.

**Why ellipticity?** On a Riemannian manifold, $\Delta = d\delta + \delta d$ is a second-order operator with *positive-definite principal symbol* — it is elliptic. The principal symbol of $\Delta$ at a covector $\xi$ is $|\xi|_g^2 \cdot \mathrm{id}_{\Lambda^k T_p^*M}$ (a scalar times the identity), which is invertible whenever $\xi \neq 0$. Ellipticity has dramatic consequences: solutions of $\Delta\omega = 0$ are automatically smooth (elliptic regularity); the kernel of $\Delta$ on a closed manifold is finite-dimensional; the Fredholm alternative holds. All the content of the Hodge theorem is downstream of ellipticity. In Lorentzian signature, the principal symbol becomes $g^{ij}\xi_i\xi_j$, which is *indefinite* — the operator is hyperbolic, not elliptic, and the kernel can be infinite-dimensional. This is why the closed Riemannian setting is critical.

**Why self-adjoint?** $\Delta$ is formally self-adjoint with respect to the $L^2$ inner product: $\langle\Delta\alpha, \beta\rangle = \langle\alpha, \Delta\beta\rangle$. Proof: $\langle\Delta\alpha, \beta\rangle = \langle d\delta\alpha + \delta d\alpha, \beta\rangle = \langle d\delta\alpha, \beta\rangle + \langle\delta d\alpha, \beta\rangle = \langle\delta\alpha, \delta\beta\rangle + \langle d\alpha, d\beta\rangle$. By symmetry, $\langle\alpha, \Delta\beta\rangle = \langle\alpha, d\delta\beta\rangle + \langle\alpha, \delta d\beta\rangle = \langle\delta\alpha, \delta\beta\rangle + \langle d\alpha, d\beta\rangle$. The two expressions agree. The self-adjointness, combined with ellipticity, gives a complete spectral theory: $\Delta$ has discrete real eigenvalues with finite-dimensional eigenspaces on a closed manifold.

**Why nonnegative?** From the calculation above, $\langle\Delta\omega, \omega\rangle = \|d\omega\|^2 + \|\delta\omega\|^2 \geq 0$ on a closed Riemannian manifold. So $\Delta$ has only nonnegative eigenvalues — and the kernel $\mathcal{H}^k(M) = \ker\Delta$ is exactly the harmonic forms, the eigenvalue-$0$ eigenspace. Nonnegativity is essential for the Hodge decomposition: it lets us argue that the orthogonal complement to the kernel is in the image of $\Delta$, giving the splitting $\Omega^k = \mathcal{H}^k \oplus \operatorname{im}\Delta$. (Plus elliptic regularity to make the smooth-versus-$L^2$ versions agree.)

---

# The Definition

Let $(M, g)$ be a smooth oriented (pseudo-)Riemannian $n$-manifold. The **Hodge Laplacian** (or **Laplace–de Rham operator**) is the operator
$$\Delta = d\delta + \delta d : \Omega^k(M) \to \Omega^k(M)$$
on $k$-forms, for each $k = 0, 1, \dots, n$.

**Equivalent form.** $\Delta = (d + \delta)^2$, where $D = d + \delta : \Omega^\bullet(M) \to \Omega^\bullet(M)$ acts on the total form space; the equality uses $d^2 = 0 = \delta^2$.

**On functions.** For $f \in C^\infty(M) = \Omega^0(M)$, $\delta f = 0$ (no negative degrees), so $\Delta f = \delta d f$. Expanding, $\Delta f = -\nabla^2 f = -\frac{1}{\sqrt{|g|}}\partial_i(\sqrt{|g|}\,g^{ij}\partial_j f)$, the negative of the Laplace–Beltrami operator. The sign convention makes $\Delta$ nonnegative.

**Properties on a closed oriented Riemannian manifold:**
- **Self-adjoint**: $\langle\Delta\alpha, \beta\rangle_{L^2} = \langle\alpha, \Delta\beta\rangle_{L^2}$.
- **Nonnegative**: $\langle\Delta\omega, \omega\rangle_{L^2} = \|d\omega\|^2_{L^2} + \|\delta\omega\|^2_{L^2} \geq 0$.
- **Elliptic**: principal symbol at $\xi \neq 0$ is $|\xi|_g^2\mathrm{id}$, invertible.
- **Commutes with $d$, $\delta$, $\star$**: $[\Delta, d] = 0$, $[\Delta, \delta] = 0$, $[\Delta, \star] = 0$ (the last requires orientation-preserving isometry of the metric for $\star$ to commute).
- **Finite-dimensional kernel** $\mathcal{H}^k(M) = \ker(\Delta : \Omega^k \to \Omega^k)$, the space of [[Def - Harmonic Form|harmonic k-forms]].

In Lorentzian or pseudo-Riemannian signature, the same formula defines $\Delta$ but it is *not* elliptic; on Lorentzian $4$D and functions, $\Delta f = -\square f$ where $\square$ is the d'Alembertian (wave operator).

---

# Categorical / Structural Definition

The Hodge Laplacian is the **square of the Dirac–de Rham operator** $D = d + \delta$. The operator $D$ acts on the total form bundle $\Lambda^\bullet T^*M = \bigoplus_k \Lambda^k T^*M$, shifting degree by $\pm 1$ via the two summands, and is the formal $L^2$-self-adjoint operator
$$D = d + \delta : \Omega^\bullet(M) \to \Omega^\bullet(M).$$
The Clifford-algebra structure on $\Lambda^\bullet T^*M$ makes $D$ a **Dirac operator** in the sense of Atiyah–Singer: a first-order, formally self-adjoint, $\mathbb{Z}/2$-graded (even/odd) operator whose principal symbol at $\xi$ is Clifford multiplication by $\xi$.

In this language, the Hodge Laplacian is $D^2 = \Delta_\bullet$, and the splitting $\Lambda^\bullet = \Lambda^{\text{even}} \oplus \Lambda^{\text{odd}}$ gives $D$ as an operator
$$D : \Omega^{\text{even}}(M) \to \Omega^{\text{odd}}(M)$$
(with the formal adjoint going the other way). The **signature operator** is this $D$ restricted to half-degrees — the index of $D$ is the topological signature of $M$ (when $\dim M \equiv 0 \pmod 4$), an integer-valued topological invariant that is computable from the curvature via the Atiyah–Singer index theorem.

This categorical perspective places the Hodge Laplacian inside the framework of generalized Dirac operators on Clifford modules, and is the gateway to spin geometry, index theory, and supersymmetric quantum mechanics on manifolds (Witten's Morse theory).

---

# Relate to Other Fields / Compression

**On functions, $\Delta$ is the negative Laplace–Beltrami.** $\Delta f = -\nabla^2 f$ where $\nabla^2$ is the standard Riemannian Laplacian. The negative sign is the *Hodge convention*: it makes $\Delta$ nonnegative-definite, matching the convention that the eigenvalues of a Laplacian are positive (e.g., on the round sphere $S^n$, the eigenvalues of $\Delta$ on functions are $\lambda_k = k(k+n-1)$ for $k = 0, 1, 2, \dots$).

**On $\mathbb{R}^3$ vector fields, $\Delta$ recovers $\operatorname{curl}\operatorname{curl} - \operatorname{grad}\operatorname{div}$.** For a vector field $\vec A$ with $1$-form dual $\alpha = a_i dx^i$, $\Delta\alpha = -\partial^j\partial_j a_i dx^i + (\partial_i\partial^j a_j) dx^i$, which is the form-dual to $-\nabla^2 \vec A + \nabla(\nabla\cdot\vec A)$. By the vector calculus identity $\operatorname{curl}\operatorname{curl}\vec A = \nabla(\nabla\cdot \vec A) - \nabla^2 \vec A$, we get $\Delta\alpha = $ (the $1$-form dual of) $\operatorname{curl}\operatorname{curl}\vec A - \operatorname{grad}\operatorname{div}\vec A$. So the Hodge Laplacian on $1$-forms in $\mathbb{R}^3$ is the standard "vector Laplacian" of physics, which famously is *not* just the componentwise Euclidean Laplacian unless one is working in Cartesian coordinates (where the Christoffel symbols vanish).

**True name:** the Hodge Laplacian is the *unique* nonnegative self-adjoint elliptic second-order operator $\Omega^k(M) \to \Omega^k(M)$ on a closed oriented Riemannian manifold that commutes with $d$, $\delta$, and $\star$, and that agrees with the negative Laplace–Beltrami on functions. The kernel $\mathcal{H}^k$ is the space of harmonic forms; ellipticity guarantees this kernel is finite-dimensional and consists of smooth forms.

The deeper "true name" is *the square of the Dirac–de Rham operator $d + \delta$*. The factorization $\Delta = D^2$ is the algebraic reason for all of Hodge theory: the kernel of $D$ is the kernel of $\Delta$ (both are the harmonic forms), and the index theory of $D$ encodes the Euler characteristic and signature of $M$.

---

# Examples / Corollaries

**Is an instance: $\Delta$ on a torus.** On the flat $n$-torus $T^n = \mathbb{R}^n/\mathbb{Z}^n$ with the standard flat metric, the Hodge Laplacian on a function $f(x^1, \dots, x^n)$ is $\Delta f = -\sum_i\partial_i^2 f$. The eigenfunctions are $e^{2\pi i k\cdot x}$ for $k \in \mathbb{Z}^n$, with eigenvalues $(2\pi)^2|k|^2$. The kernel ($\lambda = 0$) is exactly the constants, so $\mathcal{H}^0(T^n) = \mathbb{R}$, $b_0(T^n) = 1$.

**Is an instance: $\Delta$ on $1$-forms of a torus.** On $T^n$, the Hodge Laplacian on a $1$-form $\alpha = \sum_i a_i(x)\,dx^i$ (with $a_i$ periodic functions) is $\Delta\alpha = -\sum_i(\nabla^2 a_i)\,dx^i$ (the flat metric has no Christoffel correction). The kernel consists of $1$-forms with $\nabla^2 a_i = 0$ for each $i$ — periodic harmonic functions are constants, so $a_i = c_i$ constants. So $\mathcal{H}^1(T^n) = \{c_i dx^i : c_i \in \mathbb{R}\} \cong \mathbb{R}^n$, $b_1(T^n) = n$.

**Is an instance: $\Delta$ on the round $S^n$.** On the round $n$-sphere, the eigenvalues of $\Delta$ on functions are $\lambda_k = k(k + n - 1)$ for $k = 0, 1, 2, \dots$, with eigenspace the spherical harmonics of degree $k$ (dimension $\binom{n+k}{k} - \binom{n+k-2}{k-2}$). The kernel ($k = 0$) is the constants, $\mathcal{H}^0(S^n) = \mathbb{R}$. On higher-degree forms, computation via the symmetry group $\mathrm{SO}(n+1)$ shows $\mathcal{H}^k(S^n) = 0$ for $0 < k < n$ (these would be $\mathrm{SO}(n+1)$-invariant forms, which by representation theory exist only in degree $0$ and $n$), and $\mathcal{H}^n(S^n) = \mathbb{R}\cdot\operatorname{vol}_{S^n}$.

**Is NOT an instance: $\Delta$ on Minkowski space is hyperbolic, not elliptic.** On Lorentzian $\mathbb{R}^{3,1}$ with $g = -dt^2 + dx^2 + dy^2 + dz^2$, the Hodge Laplacian on a function is $\Delta f = -\square f$ where $\square = -\partial_t^2 + \nabla^2_{\text{spatial}}$ is the wave operator. The principal symbol is $-\xi_0^2 + |\vec\xi|^2$, which is *indefinite* — null vectors $\xi_0^2 = |\vec\xi|^2$ make it vanish, so the operator is not elliptic. The wave equation $\square f = 0$ has an infinite-dimensional kernel (every traveling wave $f(x - ct)$ is a solution), so the standard Hodge theorem fails.

**Corollary (closed and coclosed on a closed manifold).** $\Delta\omega = 0$ iff $d\omega = 0$ and $\delta\omega = 0$, on a closed Riemannian manifold. Proof: one direction is trivial ($d\omega = \delta\omega = 0 \Rightarrow \Delta\omega = d\delta\omega + \delta d\omega = 0$). The other: $0 = \langle\Delta\omega, \omega\rangle = \|d\omega\|^2 + \|\delta\omega\|^2$, both nonnegative, so both vanish.

**Corollary (kernel is finite-dimensional on a closed manifold).** The space $\mathcal{H}^k(M) = \ker(\Delta : \Omega^k \to \Omega^k)$ is finite-dimensional. This is a deep elliptic-operator result: the elliptic Laplacian on a closed manifold has a finite-dimensional kernel by the Fredholm property.

**Corollary ($\Delta$ commutes with isometries).** For any orientation-preserving isometry $F : (M, g) \to (M, g)$, $F^*\Delta = \Delta F^*$. So $\Delta$-eigenspaces are isometry-invariant, and on a homogeneous manifold the kernel is exactly the invariant subspace.

**Corollary (Weitzenböck formula on $1$-forms).** On a Riemannian manifold, $\Delta\omega = \nabla^*\nabla\omega + \operatorname{Ric}(\omega^\sharp, \cdot)$ for a $1$-form $\omega$, where $\nabla^*\nabla$ is the rough Laplacian (negative trace of the Hessian) and $\operatorname{Ric}$ is the Ricci tensor. The proof is a calculation using the commutator $[\nabla_i, \nabla_j]$ on forms, which produces the Riemann tensor contracted to give Ricci. This is the foundational identity for the Bochner technique (see [[Thm - Bochner's Theorem]]).

**Calibration check.** If you can verify (i) $\Delta f = -\nabla^2 f$ on a function (negative Laplace–Beltrami), (ii) $\Delta = (d + \delta)^2$ from $d^2 = \delta^2 = 0$, and (iii) $\Delta\omega = 0 \iff d\omega = 0 = \delta\omega$ on a closed manifold, you have understood the operator correctly.

---

# Unlocked by This

> [!tip] Heat Equation on Forms *(from Geometric Analysis)*
> The Hodge Laplacian generates a **heat semigroup** $e^{-t\Delta}$ on $\Omega^k(M)$: for an initial form $\omega_0$, the solution to $\partial_t\omega = -\Delta\omega$ with $\omega(0) = \omega_0$ is $\omega(t) = e^{-t\Delta}\omega_0$. On a closed Riemannian manifold this is well-defined for all $t > 0$ and is smoothing (the solution becomes smooth even if $\omega_0$ is only $L^2$). As $t \to \infty$, $e^{-t\Delta}\omega_0$ converges in $L^2$ to the **harmonic projection** of $\omega_0$. The heat semigroup is the analytic backbone of the heat-kernel proof of the index theorem, and provides explicit small-time asymptotic expansions (the **Minakshisundaram–Pleijel formula**) that compute topological invariants from local geometric data.

> [!tip] Spectral Geometry *(from Geometric Analysis)*
> The eigenvalues of the Hodge Laplacian on a closed Riemannian manifold form a discrete spectrum $0 \leq \lambda_1 \leq \lambda_2 \leq \cdots \to \infty$, and the multiplicities and eigenfunctions are geometric invariants of $(M, g)$. Famous questions: **"Can you hear the shape of a drum?"** (Kac) asks whether the spectrum determines the metric — answered in the negative by Milnor's isospectral $16$-tori. **Weyl's law** gives the asymptotic $\lambda_k \sim C\cdot k^{2/n}$, with $C$ involving only $\dim M$ and $\mathrm{vol}(M)$. The Hodge Laplacian's spectrum on forms refines this with multiplicities by degree, and packages all topological invariants of $M$ into spectral data.

> [!tip] Witten Deformation and Morse Theory *(from Differential Topology and Mathematical Physics)*
> For a Morse function $f$ on a closed Riemannian manifold, **Witten's deformation** twists the de Rham complex by $e^{tf}$: $d_t = e^{-tf}\,d\,e^{tf}$. The deformed Hodge Laplacian $\Delta_t = (d_t + d_t^*)^2$ concentrates its eigenforms near the critical points of $f$ as $t \to \infty$, and the small-eigenvalue eigenspace becomes the Morse–Smale chain complex generated by the critical points. This gives an analytic proof of the **Morse inequalities** $b_k(M) \leq c_k(f)$ (Betti number bounded by the count of index-$k$ critical points), and is the foundational construction in **supersymmetric quantum mechanics on a manifold**, with Witten's $d_t$ as the supercharge and $\Delta_t$ as the Hamiltonian.

> [!tip] The Atiyah–Singer Index Theorem *(from Index Theory and Topology)*
> The Dirac–de Rham operator $D = d + \delta$ acting between even and odd forms has **index** $\mathrm{ind}(D) = \dim\ker D - \dim\mathrm{coker}\,D$. By Hodge theory $\ker D = \mathcal{H}^{\text{even}}$ and $\mathrm{coker}\,D \cong \mathcal{H}^{\text{odd}}$, so $\mathrm{ind}(D) = \sum_k(-1)^k\dim\mathcal{H}^k = \sum_k(-1)^k b_k = \chi(M)$, the **Euler characteristic**. The Atiyah–Singer index theorem computes this analytic index purely topologically, as the integral over $M$ of the Euler class — this is the **Gauss–Bonnet–Chern theorem** as a special case of Atiyah–Singer. The same machinery applied to other elliptic operators ($\bar\partial$ on a complex manifold, the Dirac operator on a spin manifold) gives the Riemann–Roch theorem, the index theorem for Dirac, and many further geometric invariants.
