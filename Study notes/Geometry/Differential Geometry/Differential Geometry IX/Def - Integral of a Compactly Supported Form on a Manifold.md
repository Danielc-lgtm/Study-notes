---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Orientation of a Smooth Manifold"
  - "Def - Differential k-Form on a Manifold"
  - "Def - Pullback of a Differential Form on a Manifold"
  - "Def - Partition of Unity on a Manifold"
  - "Def - Support of a Function"
tags: [geometry, differential-geometry, integration]
---

# Notation

Throughout, $(M, \mathcal{O})$ is an oriented smooth $n$-manifold, possibly with boundary. $\Omega^n_c(M)$ denotes compactly-supported smooth $n$-forms on $M$. A chart $(U, \varphi)$ is **positively oriented** if its coordinate frame $(\partial_1, \ldots, \partial_n)$ is positively oriented at every point of $U$; **negatively oriented** otherwise. For a form $\omega$ supported in a chart, $(\varphi^{-1})^*\omega$ is its pushforward to $\varphi(U) \subseteq \mathbb{R}^n$. The full notation registry for the topic is at [[Differential Geometry IX — Orientation, Integration, and Stokes' Theorem]].

---

# Axiom Motivation

We have a smooth oriented manifold and a compactly supported top-degree form, and we want to define an integral $\int_M\omega \in \mathbb{R}$ that *(a)* generalizes the usual multiple Riemann integral on $\mathbb{R}^n$, *(b)* is chart-independent, *(c)* is linear, and *(d)* changes sign when the orientation is reversed.

The recipe is the only one that could possibly work, and it has two stages.

**Stage 1: a single positively oriented chart.** If $\omega$ is supported in a chart $(U, \varphi)$, we can push it down to $\varphi(U) \subseteq \mathbb{R}^n$ via $(\varphi^{-1})^*\omega$, getting a compactly supported $n$-form on an open subset of $\mathbb{R}^n$. Any such form is $A(x)\,dx^1\wedge\cdots\wedge dx^n$ for a continuous compactly supported $A : \varphi(U) \to \mathbb{R}$, and we define
$$\int_M\omega := \int_{\varphi(U)} A(x)\,dx^1\cdots dx^n,$$
the ordinary multiple Riemann (or Lebesgue) integral.

The chart-independence question is: if a different positively-oriented chart $(\widetilde U, \widetilde\varphi)$ also contains $\mathrm{supp}\,\omega$, does the same definition give the same answer? The transition map $\widetilde\varphi \circ \varphi^{-1}$ is an orientation-preserving [[Def - Diffeomorphism|diffeomorphism]] of open subsets of $\mathbb{R}^n$ (positive Jacobian by oriented atlas). The form transforms by $(\widetilde\varphi\circ\varphi^{-1})^*$, which contributes a factor of $\det D(\widetilde\varphi\circ\varphi^{-1})$ to the coefficient. The multiple integral transforms by the change-of-variables formula, which contributes $|\det D(\widetilde\varphi\circ\varphi^{-1})|$. These two factors *agree* exactly when the Jacobian is positive — which is the defining condition of an oriented atlas. So Stage 1 is well-defined precisely because orientation was demanded.

This is the key insight of the entire definition: **integration of a top-degree form on a manifold is well-defined iff the manifold is oriented, because that is the exact condition under which the form's $\det DF$ transformation rule matches the multiple integral's $|\det DF|$ rule**. Without orientation, the chart-by-chart definitions disagree, and the integral is ill-defined.

**Stage 2: partition of unity for general $\omega$.** A general compactly supported $\omega$ may not be supported in a single chart, so we glue. Cover $\mathrm{supp}\,\omega$ by finitely many positively-oriented charts $\{U_i\}_{i=1}^N$ (possible by compactness), take a smooth partition of unity $\{\psi_i\}$ subordinate to this cover, and write $\omega = \sum_i\psi_i\omega$. Each $\psi_i\omega$ is supported in $U_i$, so Stage 1 applies, and we define
$$\int_M\omega := \sum_{i=1}^N\int_M\psi_i\omega.$$

The well-definedness of this sum — independence of the choice of cover and partition of unity — is the content of [[Thm - Integration is Well-Defined on Oriented Manifolds]]. The proof uses a "refinement" argument: if $\{V_j, \chi_j\}$ is another such choice, the sum $\sum_{i,j}\int_M\psi_i\chi_j\omega$ equals both $\sum_i\int_M\psi_i\omega$ (since $\sum_j\chi_j = 1$ on the support) and $\sum_j\int_M\chi_j\omega$. Stage 1's chart-independence handles each $\psi_i\chi_j\omega$ term.

**Why allow negatively oriented charts in the partition?** Because boundary charts on a 1-dimensional manifold sometimes cannot be made positively oriented within the constraints of the boundary convention. Lee handles this by allowing negatively oriented charts and inserting a $-$ sign for each. This is a technical detail; the substance is the positively-oriented case.

**Why compactly supported?** Without compact support, the partition-of-unity sum has infinitely many terms (possibly all nonzero), and convergence is not automatic. The case of $M$ compact is automatic (every smooth $\omega$ on a compact manifold has compact support). For non-compact $M$ and non-compactly-supported $\omega$, the integral can be defined as an improper Riemann integral but requires convergence to be checked separately.

---

# The Definition

Let $(M, \mathcal{O})$ be an oriented smooth $n$-manifold ($n \geq 1$), possibly with boundary.

**Stage 1: Integral of a form supported in a single chart.** Suppose $\omega \in \Omega^n_c(M)$ is supported in the domain of a positively oriented chart $(U, \varphi)$. Then $(\varphi^{-1})^*\omega$ is a compactly supported $n$-form on $\varphi(U) \subseteq \mathbb{R}^n$ (or $\mathbb{H}^n$ for a boundary chart), of the form $A(x)\,dx^1\wedge\cdots\wedge dx^n$ for a unique compactly-supported continuous function $A$. Define
$$\int_M\omega := \int_{\varphi(U)} A(x)\,dV(x) = \int_{\varphi(U)} A(x)\,dx^1\cdots dx^n,$$
the right-hand side being the ordinary multiple Riemann (or Lebesgue) integral.

If $\omega$ is supported in a *negatively* oriented chart $(U, \varphi)$, define instead
$$\int_M\omega := -\int_{\varphi(U)} A(x)\,dV(x).$$

**Stage 2: Integral of a general compactly supported form.** For arbitrary $\omega \in \Omega^n_c(M)$, choose a finite cover $\{U_i\}_{i=1}^N$ of $\mathrm{supp}\,\omega$ by domains of positively or negatively oriented smooth charts, and choose a smooth partition of unity $\{\psi_i\}_{i=1}^N$ subordinate to this cover (with $\sum_i\psi_i = 1$ on $\mathrm{supp}\,\omega$). Define
$$\int_M\omega := \sum_{i=1}^N\int_M\psi_i\omega,$$
where each summand is defined by Stage 1.

**Well-definedness ([[Thm - Integration is Well-Defined on Oriented Manifolds|theorem]]).** The integral $\int_M\omega$ is independent of the choice of cover and partition of unity, and (in Stage 1) independent of the choice of chart from the maximal oriented atlas.

**Integral over the empty manifold.** If $M = \emptyset$, set $\int_M\omega := 0$.

**0-dimensional case.** If $M^0$ is an oriented 0-manifold (a discrete set of points each labeled $+1$ or $-1$) and $f : M \to \mathbb{R}$ is compactly supported (so $f$ is nonzero at only finitely many points), define
$$\int_M f := \sum_{p \in M} \mathrm{sgn}(p)\,f(p).$$

**Integral over an oriented submanifold.** If $S \subseteq M$ is an oriented immersed $k$-submanifold with inclusion $\iota : S \hookrightarrow M$, and $\omega \in \Omega^k(M)$ has compactly-supported pullback to $S$, define $\int_S\omega := \int_S \iota^*\omega$ — the integral of the pulled-back $k$-form on $S$. In particular, if $M$ is oriented with boundary, $\int_{\partial M}\omega$ for $\omega \in \Omega^{n-1}_c(M)$ means the integral of $\iota^*\omega$ over $\partial M$ with the induced orientation.

---

# Properties

The integral satisfies the standard properties (see [[Thm - Integration is Well-Defined on Oriented Manifolds]] for proofs):

- **Linearity.** $\int_M(a\omega + b\eta) = a\int_M\omega + b\int_M\eta$ for $a, b \in \mathbb{R}$, $\omega, \eta \in \Omega^n_c(M)$.
- **Orientation reversal.** $\int_{-M}\omega = -\int_M\omega$, where $-M$ denotes $M$ with the opposite orientation.
- **Positivity.** If $\omega$ is a positively-oriented volume form (in particular nowhere-vanishing and consistent with the orientation), then $\int_M\omega > 0$ provided $\omega$ is not identically zero on a set of positive measure.
- **[[Def - Diffeomorphism|Diffeomorphism]] invariance / change of variables.** For an orientation-preserving diffeomorphism $F : N \to M$, $\int_M\omega = \int_N F^*\omega$. For orientation-reversing $F$, $\int_M\omega = -\int_N F^*\omega$ (see [[Thm - Change of Variables for Integration on Manifolds]]).
- **Integration over parametrizations.** If domains of integration $D_1, \ldots, D_k \subseteq \mathbb{R}^n$ have orientation-preserving smooth diffeomorphism maps $F_i : D_i \to W_i \subseteq M$ with disjoint $W_i$ covering $\mathrm{supp}\,\omega$ up to measure zero, then $\int_M\omega = \sum_i\int_{D_i}F_i^*\omega$ — the practical computational formula.

---

# Relate to Other Fields / Compression

The integral of a top-form is the **only chart-independent integral** available on a bare smooth manifold (without a metric). The integral of a *function* is not chart-independent — it depends on the Jacobian $|\det DF|$, which has no canonical value across charts. A function can be integrated only after multiplication by a top-form: on a Riemannian manifold, that top-form is canonically the Riemannian volume form $\omega_g$, recovering the usual notion of integration of functions.

The compression: **integration on a manifold = integration of $n$-forms on an oriented $n$-manifold**, with the signed-Jacobian transformation rule of forms matching the absolute-value-Jacobian rule of Riemann integration *exactly* when the manifold is oriented. Everything else (integration of functions, integration on non-orientable manifolds, integration in measure-theoretic terms) is built from this base by adding extra structure.

**True name:** The integral of a compactly supported top-form is the partition-of-unity sum of pullbacks of Riemann integrals, the unique chart-independent linear functional $\Omega^n_c(M) \to \mathbb{R}$ that agrees with the multiple Riemann integral on each chart. This is the operational form; the partition-of-unity machinery is the *only* part that needs care.

---

# Examples / Corollaries

**Example — integral over $\mathbb{R}^n$.** For $\omega = f(x)\,dx^1\wedge\cdots\wedge dx^n$ with $f$ compactly supported,
$$\int_{\mathbb{R}^n}\omega = \int_{\mathbb{R}^n}f(x)\,dV.$$
The identity chart gives the formula directly. No partition of unity is needed.

**Example — integral over $S^2$ of the area form.** With $\omega = x\,dy\wedge dz + y\,dz\wedge dx + z\,dx\wedge dy$ and spherical parametrization $F(\varphi, \theta) = (\sin\varphi\cos\theta, \sin\varphi\sin\theta, \cos\varphi)$ on $(0,\pi) \times (0, 2\pi)$, computation gives $F^*\omega = \sin\varphi\,d\varphi\wedge d\theta$, so
$$\int_{S^2}\omega = \int_0^{2\pi}\int_0^\pi \sin\varphi\,d\varphi\,d\theta = 4\pi.$$
This is [[Ex - Computing the Integral of a 2-Form on the Sphere|the standard exercise]].

**Example — integral of $d\theta$ over $S^1$.** The angular 1-form $d\theta$ on $S^1$ satisfies $\int_{S^1}d\theta = 2\pi$. Note that $\theta$ is not a globally defined function (only locally), so $d\theta$ is *closed but not exact*; the nonzero integral is a topological invariant — the generator of $H^1_{dR}(S^1) = \mathbb{R}$.

**Example — integral of an exact form on a closed manifold.** If $M$ is compact without boundary and $\omega = d\eta$ for some $\eta \in \Omega^{n-1}(M)$, then by [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]], $\int_M\omega = \int_M d\eta = \int_{\partial M}\eta = 0$. So *exact top-forms integrate to zero on closed manifolds* — the engine behind much of de Rham cohomology.

**Non-example — integral on the Möbius strip.** The Möbius strip is non-orientable, so the integral of a top-form is not defined. One can instead integrate *densities*; see [[Def - Density on a Manifold]].

**Non-example — integral without compact support.** $\int_{\mathbb{R}^n}dx^1\wedge\cdots\wedge dx^n$ is not defined: it would have to equal the volume of $\mathbb{R}^n$, which is infinite. Compact support is essential; otherwise convergence must be addressed separately (improper Riemann integrals).

**Non-example — integral of a function.** $\int_{S^2}1 = ?$ has no canonical value without choosing a top-form / volume form / Riemannian metric. With the round metric, $\int_{S^2}1\cdot\omega_g = \mathrm{Area}(S^2) = 4\pi$; with a different choice the answer would be different.

**Corollary — fundamental theorem of calculus in disguise.** On the oriented 1-manifold $M = [a, b]$ with $\partial M = \{a, b\}$ (orientations: $a$ negative, $b$ positive), for $f \in C^1([a, b])$,
$$\int_{[a, b]}df = \int_{\partial[a, b]}f = f(b) - f(a).$$
This is the Fundamental Theorem of Calculus, recovered as the $n = 1$ case of [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]]. The integral on the left is the manifold integral defined here; the right side uses the 0-dimensional definition.

**Corollary — diffeomorphism invariance.** If $F : N \to M$ is an orientation-preserving diffeomorphism and $\omega \in \Omega^n_c(M)$, then $\int_M\omega = \int_N F^*\omega$. This is what makes manifold integration *intrinsic* — independent of how $M$ is embedded or parametrized.

**Calibration check.** Verify the computation $\int_{S^2}\omega = 4\pi$ for the area form; verify the angular form gives $\int_{S^1}d\theta = 2\pi$; check that reversing the orientation of $[a, b]$ negates the FTC value; and verify that the integral of an exact form on a sphere (no boundary) is zero. If you can also explain why the integral of a top-form on $\mathbb{R}^n$ is the usual multiple integral, with no extra Jacobian factor (because the identity chart is positively oriented), you have understood the definition.

---

# Unlocked by This

> [!tip] Stokes's Theorem *(continued in this topic)*
> Once the manifold integral is defined, the central theorem of the topic is [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] $\int_M d\omega = \int_{\partial M}\omega$, which links the integral to the exterior derivative. The proof uses this definition heavily — pulling back to half-space charts.

> [!tip] de Rham Cohomology *(from Algebraic Topology)*
> Because (by Stokes) $\int_M$ kills exact forms on closed manifolds, integration descends to a pairing $H^k_{dR}(M) \times H_k(M) \to \mathbb{R}$ between de Rham cohomology and singular homology. **De Rham's theorem** identifies the two as canonically isomorphic via this pairing.

> [!tip] Riemannian Integration and Lebesgue Measure *(from Measure Theory)*
> On an oriented Riemannian manifold, the volume form $\omega_g = \sqrt{\det g}\,dx^1\wedge\cdots\wedge dx^n$ gives a canonical way to integrate functions: $\int_M f := \int_M f\omega_g$. This induces a Borel measure $\mu_g$ on $M$, related to [[Def - Lebesgue Measure|Lebesgue measure]] in any chart by the Radon–Nikodým factor $\sqrt{\det g}$.

> [!tip] Spectral Theory on Manifolds *(from Differential Geometry / Mathematical Physics)*
> The integral defined here is the building block of $L^p$ spaces on a Riemannian manifold, of the spectral theory of the Laplace–Beltrami operator $\Delta_g$, and of all elliptic/parabolic/hyperbolic PDE theory on manifolds. The spectral theorem for $\Delta_g$ on a compact manifold rests on the inner product $\langle f, h\rangle = \int_M fh\,\omega_g$ — defined exactly by this construction.
