---
type: lemma
subject: hyperbolic-geometry
prereqs:
  - "Def - Hyperbolic Plane"
  - "Def - Closed Geodesics, Conjugacy Classes, and Translation Length"
  - "Def - Heat Kernel and Heat Semigroup"
tags: [paper, brownian-loops, hyperbolic-geometry, heat-kernel]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Lemma 3.4"
---

# Notation

- $\mathbb{H}^2$ — upper-half-plane $\{z = x+iy : y > 0\}$ with hyperbolic metric $ds^2 = (dx^2+dy^2)/y^2$; hyperbolic distance $d_{\mathbb{H}^2}(z,w)$; area measure $d\rho_{\mathbb{H}^2}(z) = dx\,dy/y^2$.
- $p_{\mathbb{H}^2}(s, z, w)$ — the standard Brownian heat kernel on $\mathbb{H}^2$; a function of $s>0$ and the hyperbolic distance $r = d_{\mathbb{H}^2}(z,w)$ alone (rotation-and-translation invariance of $\mathbb{H}^2$).
- $\tau : z\mapsto e^L z$ — a hyperbolic isometry of $\mathbb{H}^2$ with axis the imaginary half-line and translation length $L>0$; here $L := m\ell_\gamma$ with $m\ge 1$ and $\ell_\gamma$ the length of a primitive closed geodesic.
- $\mathcal{F}_\tau = \{z\in\mathbb{H}^2 : 1\le\mathrm{Im}\,z < e^L\}$ — the fundamental strip of $\langle\tau\rangle$.

> [!recall]- Hyperbolic plane $\mathbb{H}^2$, distance, and area
> **Formally:** $\mathbb{H}^2 = \{z=x+iy \in \mathbb{C} : y>0\}$ with $ds^2 = (dx^2+dy^2)/y^2$; hyperbolic distance $d(z,w) = \operatorname{arcosh}(1 + |z-w|^2/(2\,\mathrm{Im}\,z\,\mathrm{Im}\,w))$; area $d\rho_{\mathbb{H}^2}(x,y) = dx\,dy/y^2$; isometry group $\mathrm{PSL}(2,\mathbb{R})$.
> **In words:** the upper half-plane with a rescaled ruler that puts an infinite-distance wall at $y=0$; distances on curves at the same height $y_0$ are stretched by a factor $1/y_0$ compared with Euclidean.
> **Concretely:** the distance from $i$ to $2i$ is $\int_1^2 dy/y = \log 2$; the distance from $i$ to $e^L i$ is $L$ (the definition of the translation length of $\tau : z\mapsto e^L z$, whose axis is the imaginary half-line). Full detail: [[Def - Hyperbolic Plane]].

> [!recall]- Fundamental strip $\mathcal{F}_\tau$
> **Formally:** for $\tau : z\mapsto e^L z$ (with $L>0$), $\mathcal{F}_\tau = \{z\in\mathbb{H}^2 : 1\le\mathrm{Im}\,z < e^L\}$; this is a fundamental region for the cyclic subgroup $\langle\tau\rangle$, meeting every $\langle\tau\rangle$-orbit in exactly one point.
> **In words:** $\tau$ rescales $\mathrm{Im}\,z$ by $e^L$; the strip is one period of that rescaling. Quotienting $\mathbb{H}^2$ by $\langle\tau\rangle$ gives a hyperbolic *cylinder* (or *funnel*) obtained by gluing the top edge $\mathrm{Im}\,z = e^L$ to the bottom $\mathrm{Im}\,z = 1$ via $z\mapsto z/e^L$.
> **Concretely:** if $L = \log 2$, the strip is $\{1 \le \mathrm{Im}\,z < 2\}$; the orbit of $1+i$ inside the strip is the single point $1+i$; the orbit of $3+3i$ has strip-representative $\tau^{-1}(3+3i) = 1.5 + 1.5i$.

> [!recall]- Brownian heat kernel on $\mathbb{H}^2$
> **Formally:** the transition density $p_{\mathbb{H}^2}(s,z,w)$ of Brownian motion (semigroup $e^{-s\Delta_{\mathbb{H}^2}}$, with $\Delta_{\mathbb{H}^2}$ the positive Laplacian) has a closed form depending only on $r = d_{\mathbb{H}^2}(z,w)$:
> $$p_{\mathbb{H}^2}(s, r) \;=\; \frac{\sqrt{2}\,e^{-s/4}}{(4\pi s)^{3/2}}\int_r^\infty \frac{u\,e^{-u^2/(4s)}}{\sqrt{\cosh u - \cosh r}}\,du.$$
> The prefactor $e^{-s/4}$ reflects the spectral bottom $\lambda_0 = 1/4 = (\frac12)^2$ of $\Delta_{\mathbb{H}^2}$ on $L^2(\mathbb{H}^2)$.
> **In words:** the return-probability density for hyperbolic Brownian motion. Depends only on how far apart the two points are (not on their location), because $\mathbb{H}^2$ is homogeneous and isotropic. The factor $e^{-s/4}$ is the correction from negative curvature (it makes the heat decay faster than on $\mathbb{R}^2$, because Brownian paths spread out exponentially faster).
> **Concretely:** at short times $s\ll 1$ and small distances $r\ll 1$, $p_{\mathbb{H}^2}(s,r) \sim (4\pi s)^{-1}e^{-r^2/(4s)}$ — the flat-plane Gaussian, because hyperbolic and Euclidean geometry agree at small scales. At long times $s\gg 1$, $p_{\mathbb{H}^2}(s,r) \sim (4\pi)^{-1}e^{-s/4}\cdot(\text{polynomial in }r,s)$ — exponential decay set by the spectral gap. Full detail: [[Def - Heat Kernel and Heat Semigroup]].

> [!recall]- Translation length $L$ and $d_{\mathbb{H}^2}(z, e^L z)$
> **Formally:** $\tau : z\mapsto e^L z$ has axis the imaginary half-line $\{iy : y>0\}$ and moves each axis point by hyperbolic distance $L$. For a general $z = x+iy$, the distance $d_{\mathbb{H}^2}(z, e^L z)$ depends on how far $z$ is from the axis; the *minimum* value $L$ is attained on the axis, and the distance grows for off-axis points.
> **In words:** every hyperbolic isometry has a preferred geodesic (its *axis*) along which it translates by a fixed distance; off the axis, points move further because they follow curves that swing around the axis.
> **Concretely:** with $L = \log 2$ and $\tau : z\mapsto 2z$: on the axis, $d(i, 2i) = \log 2$; off-axis at $z = 1+i$, $d(1+i, 2+2i) = \operatorname{arcosh}(1 + |1+i - 2 - 2i|^2/(2\cdot 1\cdot 2)) = \operatorname{arcosh}(1 + 2/4) = \operatorname{arcosh}(3/2) \approx 0.962 > \log 2 \approx 0.693$. So off-axis paths are strictly longer than the axis translation.

---

# Statement

> **Lemma (Wang–Xue strip integral; Belyaev–Huseynli 3.4, after Wang–Xue [WX25]).** For the Brownian heat kernel $p_{\mathbb{H}^2}$ on $\mathbb{H}^2$, every $s > 0$, every $L > 0$, and $\tau : z\mapsto e^L z$,
> $$\int_{\mathcal{F}_\tau} p_{\mathbb{H}^2}\big(s, z, e^L z\big)\,d\rho_{\mathbb{H}^2}(z) \;=\; \frac{L\cdot(1/L)\cdot\ell_\gamma}{\ldots}\quad\text{i.e.}\quad \int_{\mathcal{F}_\tau} p_{\mathbb{H}^2}(s, z, \tau z)\,d\rho_{\mathbb{H}^2}(z) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}},$$
> where $L = m\ell_\gamma$ (so the "single winding around the axis by translation length $L$" corresponds to $\tau^m$ acting on the strip $\mathcal{F}_\tau$ built from $\ell_\gamma$). Equivalently, writing $\tau^m : z\mapsto e^{L}z$ directly and $\mathcal{F}_\tau$ for the strip of the primitive $\tau$:
> $$\boxed{\;\int_{\mathcal{F}_\tau} p_{\mathbb{H}^2}\big(s, z, \tau^m z\big)\,d\rho_{\mathbb{H}^2}(z) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}\;}\qquad(L = m\ell_\gamma).$$

---

# In One Line

For an $\mathbb{H}^2$-hyperbolic isometry $\tau^m$ with translation length $L$, the integral of the Brownian heat kernel from $z$ to $\tau^m z$ over the primitive fundamental strip has an explicit product-form: a *geometric* factor $\ell_\gamma/[2\sinh(L/2)]$ measuring the strip's hyperbolic width times a *1-D-Gaussian* factor $e^{-s/4}e^{-L^2/(4s)}/(2\sqrt{\pi s})$ carrying the heat cost of translating by hyperbolic distance $L$.

---

# Why It's True

**Mechanism (one sentence).** *Choose Fermi (distance-along-axis, distance-across-axis) coordinates on the strip; the axis contributes the Gaussian $e^{-L^2/(4s)}/(2\sqrt{\pi s})$ (a 1-D heat kernel in the axis direction), the cross-axis integral produces $\ell_\gamma/[2\sinh(L/2)]$ (a geometric width from the sinh volume form of $\mathbb{H}^2$), and the curvature correction $e^{-s/4}$ is the spectral-bottom factor of the $\mathbb{H}^2$ heat kernel.*

There are two ways to see the identity: (i) direct computation with the explicit $\mathbb{H}^2$ heat kernel; (ii) exploiting the fact that $\langle\tau^m\rangle\backslash\mathbb{H}^2$ is a hyperbolic cylinder of core-geodesic length $L$ and computing its heat kernel by unfolding.

**Approach (i) — Fermi coordinates.** The strip $\mathcal{F}_\tau$ mod-out $\langle\tau^m\rangle$ becomes a cylinder around a core geodesic of length $L$ (the projection of the axis of $\tau^m$). In *Fermi coordinates* $(t, r)$ — $t\in[0,L)$ arc-length along the core geodesic, $r\in\mathbb{R}$ signed hyperbolic distance to it — the metric on this cylinder is $ds^2 = \cosh^2(r)\,dt^2 + dr^2$ and the area element is $\cosh(r)\,dt\,dr$; the heat kernel from a point $(t_0, r)$ to its $\tau^m$-image $(t_0 + L, r)$ depends only on $r$ (the "cost" of going once around the cylinder). Integrating over the cylinder ($t_0\in[0,L)$ gives length $L$, then $r\in\mathbb{R}$ integrates the $r$-dependence) reproduces the stated closed form. The $\sinh(L/2)$ in the denominator arises from the sinh Jacobian of $\mathbb{H}^2$-radial integration and expresses the effective "width" of the cylinder relative to its core.

**Approach (ii) — spectral / unfolding.** The heat kernel on the hyperbolic cylinder $\langle\tau^m\rangle\backslash\mathbb{H}^2$ decomposes into Fourier modes along the $S^1$-factor (period $L$); the projection onto the trivial ("radial") mode carries the "shift by one period" term, and evaluating it against the $\mathbb{H}^2$ heat kernel gives the boxed formula.

Both approaches are executed in Wang–Xue [WX25]; the paper cites the result. Below is the input as a self-contained callout for a reader who wants to see the *statement typed and its provenance*, without the full derivation.

---

# Proof

> [!cite]- External input — the Wang–Xue derivation
> **Statement (typed).** With notation as above, for every $s > 0$, $L > 0$, and $m\ge 1$ (with $L = m\ell_\gamma$):
> $$\int_{\mathcal{F}_\tau}p_{\mathbb{H}^2}(s, z, \tau^m z)\,d\rho_{\mathbb{H}^2}(z) \;=\; \frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}.$$
> **Type check.** The left-hand side is a function of $s, L$; both sides are positive; the right factors into a geometric part $\ell_\gamma/[2\sinh(L/2)]$ (dimensionless in the hyperbolic units, depending on the primitive length $\ell_\gamma$ and the winding $m$ via $L$) and an analytic part $e^{-s/4}e^{-L^2/(4s)}/(2\sqrt{\pi s})$ (the 1-D heat kernel from $0$ to $L$ at Euclidean time $s$, times the $\mathbb{H}^2$-spectral-bottom correction $e^{-s/4}$).
> **Why it's true (intuition).** The heat kernel on $\mathbb{H}^2$ depends only on distance. Along the axis of $\tau^m$, $d(z, \tau^m z) = L$ (the translation length); off the axis, the distance grows. The Gaussian $e^{-L^2/(4s)}/(2\sqrt{\pi s})$ is the leading heat cost of the on-axis translation (the 1-D Brownian bridge factor for a translation by $L$ in Euclidean time $s$); $e^{-s/4}$ is the curvature/spectral-gap correction ($1/4 = (\frac12)^2$ is the bottom of the $L^2$-spectrum of $\Delta_{\mathbb{H}^2}$); $\ell_\gamma/[2\sinh(L/2)]$ is the geometric width of the strip's cross-section after the $\cosh r$ Jacobian of the hyperbolic area is integrated out (the $2\sinh(L/2)$ factor comes from the elementary identity $e^L - 1 = 2\sinh(L/2)e^{L/2}$, which lets the Gaussian pair up with the strip's period cleanly).
> **Source.** Wang–Xue [WX25, Lemma 3.2] — proved there by (i) reducing to Fermi coordinates on the cylinder $\langle\tau^m\rangle\backslash\mathbb{H}^2$, (ii) writing the $\mathbb{H}^2$ heat kernel as an $S^1$-Fourier series and picking off the "shift by $L$" mode. The result is standard in the literature on heat kernels on hyperbolic cylinders and appears (in equivalent form) in Buser's *Geometry and Spectra of Compact Riemann Surfaces* and Sarnak's determinant-formula papers.
> **Take on faith with the stated form.** A reader who wants the derivation may consult Wang–Xue directly; the identity is *elementary* modulo the closed form of the $\mathbb{H}^2$ heat kernel (which is itself a classical computation, e.g. Chavel, *Eigenvalues in Riemannian Geometry*).

The formula is the sole geometric input of §3.1: with it, [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] specialised to a subordinate process reduces to a purely 1-D integral in the subordination variable, evaluated in closed form for each concrete process in [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] and its four cases.

---

# Where the paper uses this

Used to prove [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]]: after subordination, the spatial integral over the strip is precisely this integral (with the subordinator's kernel replacing $s$); the identity turns the double $(t,s)$-integral into a single 1-D integral against the weighted potential measure $V_\phi$. Also used, in the special case $\phi = \lambda$, to recover the Wang–Xue closed form $\mu_X(C_X(\gamma^m)) = \frac{1}{m(e^L-1)}$ (§3.1.1). Read in context: [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3]].
