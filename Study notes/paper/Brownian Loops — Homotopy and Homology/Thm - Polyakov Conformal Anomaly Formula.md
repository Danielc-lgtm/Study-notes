---
type: theorem
subject: spectral-geometry
prereqs:
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure"
tags: [paper, brownian-loops, spectral-geometry, external-input]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Theorem 5.3"
---

# Notation

- $X$ — a **closed** (compact, no boundary) smooth surface of genus $g$; from the paper's setting, later specialised to a hyperbolic surface $X = \Gamma\backslash\mathbb H^2$.
- $g_0$ — a smooth Riemannian metric on $X$ (a symmetric positive-definite bilinear form on each tangent space, varying smoothly).
- $\sigma : X \to \mathbb R$ — a smooth real function on $X$, the **conformal factor**.
- $g = e^{2\sigma} g_0$ — the metric obtained by pointwise rescaling $g_0$ by $e^{2\sigma}$. Two metrics related this way are **conformally equivalent**; they define the same angles at every point but different lengths.
- $\Delta_{g}$, $\Delta_{g_0}$ — the positive Laplace–Beltrami operators of the two metrics (Rule 3: positive convention $\Delta = -\operatorname{div}\operatorname{grad}$, spectrum in $[0, \infty)$).
- $K_0 : X \to \mathbb R$ — the **Gauss curvature** of $g_0$.
- $\operatorname{vol}_{g_0}$, $\operatorname{vol}_g$ — the Riemannian volume (area, since $\dim X = 2$) measures of the two metrics.
- $|\nabla_{g_0}\sigma|^2 = g_0^{ij}\partial_i\sigma\,\partial_j\sigma$ — the squared gradient of $\sigma$ computed with respect to $g_0$.
- $\det_\zeta \Delta_g$, $\det_\zeta \Delta_{g_0}$ — the zeta-regularised determinants of the two Laplacians (zero eigenvalue excluded).

> [!recall]- Zeta-regularised determinant of the Laplacian
> **Formally:** for a closed surface with Laplace eigenvalues $0=\lambda_0<\lambda_1\le\lambda_2\le\cdots\to\infty$, the **spectral zeta function** is $\zeta_X(s):=\sum_{j\ge1}\lambda_j^{-s}$ (convergent for $\operatorname{Re}s>1$). It equals the Mellin transform $\Gamma(s)^{-1}\int_0^\infty t^{s-1}(\operatorname{Tr}e^{-t\Delta_X}-1)\,dt$, from which $\zeta_X$ meromorphically continues to all of $\mathbb C$ and is regular at $s=0$. Then $\log\det_\zeta\Delta_X:=-\zeta_X'(0)$.
> **In words:** you want the "product of all Laplace eigenvalues" $\prod_{j\ge1}\lambda_j$, but this product is infinite (there are infinitely many $\lambda_j$ growing to infinity). The zeta-regularised determinant is a finite, canonical stand-in for that divergent product. The trick: use $\log\prod_j\lambda_j=\sum_j\log\lambda_j$; note that formally $\sum_j\log\lambda_j=-\frac{d}{ds}\big|_{s=0}\sum_j\lambda_j^{-s}=-\zeta_X'(0)$; and *this* right-hand side, thanks to meromorphic continuation, is finite. Define $\det_\zeta\Delta:=e^{-\zeta_X'(0)}$ by fiat.
> **Concretely:** if $\Delta$ has only three eigenvalues $\lambda_1=1,\lambda_2=2,\lambda_3=3$, then $\zeta(s)=1+2^{-s}+3^{-s}$; $\zeta'(0)=-\log 2-\log 3=-\log 6$; so $\det_\zeta=e^{\log 6}=6=1\cdot 2\cdot 3$, the ordinary product. On the flat torus $T^2=\mathbb R^2/(2\pi\mathbb Z)^2$, $\det_\zeta\Delta$ evaluates to a finite Jacobi-theta-product expression. See [[Def - Zeta-Regularised Determinant of the Laplacian]].

> [!recall]- Conformally equivalent metrics $g = e^{2\sigma} g_0$
> **Formally:** two Riemannian metrics $g_0, g$ on the same smooth manifold are **conformally equivalent** if there is a smooth function $\sigma : X \to \mathbb R$ with $g_p = e^{2\sigma(p)} (g_0)_p$ for every point $p$. Equivalently, at each point $g$ is a scalar positive multiple of $g_0$, with the scale varying smoothly across $X$.
> **In words:** the two metrics measure lengths differently (a segment that has $g_0$-length $L$ has $g$-length $e^{\sigma(p)} L$ at $p$), but they measure **angles the same**: the angle between two tangent vectors is unchanged by pointwise rescaling. So conformal equivalence preserves shape/orientation locally and only stretches or compresses distances. The conformal factor $e^{2\sigma}$ is what "reshapes" $g_0$ into $g$.
> **Concretely:** on $\mathbb R^2$ with $g_0$ the standard Euclidean metric, take $\sigma(x, y) = -\log(1 + x^2 + y^2)$: then $g = e^{2\sigma} g_0 = (1 + x^2 + y^2)^{-2}(dx^2 + dy^2)$ is (up to a factor) the round metric on $S^2$ pulled back by stereographic projection. The angles between tangent lines are the same in the two metrics; the metric $g$ shrinks rapidly at infinity so that the total area is finite (the sphere) instead of infinite (the plane).

> [!recall]- Gauss curvature $K$ of a Riemannian surface
> **Formally:** for a smooth Riemannian $2$-manifold $(X, g_0)$, the **Gauss curvature** $K_0 : X \to \mathbb R$ is the sectional curvature of the (unique) 2-plane $T_p X$; intrinsically $K_0 = \frac{R_{1212}}{\det g_0}$ where $R_{1212}$ is a component of the Riemann curvature tensor in any orthonormal frame. It transforms under a conformal change $g = e^{2\sigma} g_0$ by $K_g = e^{-2\sigma}(K_0 - \Delta_{g_0}\sigma)$.
> **In words:** a single number at each point that measures how much the surface curves away from being flat: positive $K$ means the surface bulges outward (like a sphere), negative $K$ means it saddles (like a Pringle chip), zero means it is locally like a piece of paper. It is intrinsic — a bug walking on the surface can measure it by comparing the angles of a small triangle to $\pi$: the excess/deficit divided by triangle area gives $K$.
> **Concretely:** on the round sphere $S^2$ of radius $R$, $K \equiv 1/R^2$ (constant positive). On the Euclidean plane, $K \equiv 0$. On the hyperbolic plane $\mathbb H^2$ with metric $ds^2 = (dx^2+dy^2)/y^2$, $K \equiv -1$ (constant negative). Gauss–Bonnet: $\int_X K\,d\!\operatorname{vol} = 2\pi\chi(X)$, so on a closed hyperbolic surface of genus $g \ge 2$ with $K \equiv -1$, $\operatorname{Area}(X) = 2\pi(2g-2) = 4\pi(g-1)$.

---

# Statement

> **Theorem (Polyakov's conformal anomaly formula; Belyaev–Huseynli Theorem 5.3, external input).** Let $X$ be a closed smooth surface, $g_0$ a smooth Riemannian metric on $X$, $\sigma : X \to \mathbb R$ a smooth real function, and $g = e^{2\sigma} g_0$. Write $K_0$ for the Gauss curvature of $g_0$, and $\Delta_g$, $\Delta_{g_0}$ for the positive Laplace–Beltrami operators with the zero mode excluded. Then
> $$\log\det_\zeta\Delta_g \;=\; -\frac{1}{12\pi}\int_X |\nabla_{g_0}\sigma|^2\,d\!\operatorname{vol}_{g_0} \;-\; \frac{1}{6\pi}\int_X K_0\,\sigma\,d\!\operatorname{vol}_{g_0} \;+\; \log\frac{\operatorname{vol}_g(X)}{\operatorname{vol}_{g_0}(X)} \;+\; \log\det_\zeta\Delta_{g_0}.$$
> The three integrals on the right are the **conformal anomaly**: the difference of zeta-determinants between two conformally equivalent metrics is a local functional of the conformal factor and the reference curvature, plus a volume-ratio term.

---

# In One Line

The zeta-regularised determinant of the Laplacian is not conformally invariant on a surface; its change under a conformal rescaling is given by an *explicit* local integral in the conformal factor $\sigma$ — this is the "conformal anomaly" of the 2-D scalar determinant.

---

# Why It's True (intuition)

**Mechanism (one sentence).** *Differentiate $\log\det_\zeta\Delta_{g_t}$ along a one-parameter family $g_t = e^{2t\sigma}g_0$ of conformal rescalings; the derivative is a local integral (the "conformal variation of $\log\det$"), which integrates in $t$ to give Polyakov's formula.*

Zeta-determinants of Laplacians on **odd**-dimensional manifolds happen to be conformally invariant; on **even**-dimensional manifolds (including our surface case, $\dim X = 2$) they are not — the failure is the **conformal anomaly**, a purely local expression in $\sigma$ and the curvature of the reference metric. Heuristically, when you rescale $g_0 \mapsto e^{2\sigma}g_0$ pointwise, each eigenvalue of $\Delta$ shifts, and adding up "$\log\lambda_j$ after rescaling minus $\log\lambda_j$ before" — regularised — is what the integral on the right-hand side computes.

**Physical picture (heat-kernel side).** The short-time heat-kernel expansion $\operatorname{Tr}(e^{-t\Delta_g}) \sim \frac{\operatorname{vol}_g(X)}{4\pi t} + \frac{\chi(X)}{6} + O(t)$ on a surface has a *conformally invariant* constant term ($\chi(X)/6$), controlled by Gauss–Bonnet, but a non-invariant leading term. That mismatch — visible already in the zeta-value at $s = 0$, $\zeta_X(0) = \chi(X)/6 - 1$ (a topological quantity) versus the derivative $\zeta_X'(0)$ (not topological) — is what powers the anomaly.

**Physical picture (string-theory side).** The prefactor $-\frac{1}{12\pi}$ is exactly the central-charge normalisation of one free scalar boson: Polyakov derived this formula in the context of the bosonic string partition function, where $\log\det_\zeta\Delta_g$ appears as the one-loop effective action and $-\frac{1}{12\pi}\int|\nabla\sigma|^2\,d\!\operatorname{vol}$ is the Liouville action controlling the coupling of the string worldsheet to its conformal factor. The factor $c = 1$ (central charge of the boson) is smuggled inside that constant.

*This intuition is not a proof.* The identity is a nontrivial calculation on the heat-kernel side; see the sources below for a complete derivation.

---

# Proof

> [!cite]- External input — Polyakov's conformal anomaly formula
> **Statement (typed):** as above.
> **Why it's true (intuition):** on a family of conformally-equivalent metrics $g_t = e^{2t\sigma}g_0$, the conformal variation of the log-determinant $\frac{d}{dt}\log\det_\zeta\Delta_{g_t}$ is computable as a local integral in $\sigma$ and $K_0$ (via the small-time heat-kernel coefficients); Polyakov's formula is the integration of this variational identity from $t = 0$ to $t = 1$.
> **Source.** A. M. Polyakov, *Quantum geometry of bosonic strings*, Phys. Lett. B **103** (1981), 207–210, is the original physics derivation; the rigorous mathematical proof (in the surface case, with the constants exactly as above) is Osgood–Phillips–Sarnak, *Extremals of determinants of Laplacians*, J. Funct. Anal. **80** (1988), 148–211 (see also their compendium *Compact isospectral sets of surfaces*, J. Funct. Anal. **80** (1988), 212–234). See also Sarnak, *Determinants of Laplacians*, Comm. Math. Phys. **110** (1987), 113–120. **Take on faith** with the exact statement above; the proof lies well above the paper-notes floor and beyond what the Belyaev–Huseynli paper itself proves.

---

# Where the paper uses this

The paper cites Polyakov's formula as Theorem 5.3 in [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5.1.1]] and combines it with [[Thm - Determinant as Renormalised Loop Mass|Theorem 5.1]] to obtain [[Cor - Polyakov Formula via Brownian Loop Measure|Corollary 5.4]]: an expression for $\log\det_\zeta\Delta_g$ on *any* smooth metric $g$ in the conformal class of the hyperbolic metric $g_{\mathrm{hyp}}$ as (loop-measure content on the hyperbolic representative) $+$ (explicit local Polyakov correction).

---

# Verified against

Polyakov (1981), *Quantum geometry of bosonic strings* — original physics derivation; Osgood–Phillips–Sarnak (1988), *Extremals of determinants of Laplacians* — rigorous statement and proof in the closed-surface case, with the constants $-1/(12\pi)$ and $-1/(6\pi)$ as here. Sarnak, *Determinants of Laplacians* (1987) — surface case. The formula is standard in spectral geometry and string theory. Statement matches Belyaev–Huseynli §5.1.1 exactly.
