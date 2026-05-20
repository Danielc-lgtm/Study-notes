---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Curve and C1 Curve"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ open; $f : U \to \mathbb{C}$ continuous; $\gamma : [a, b] \to U$ a piecewise $C^1$ curve. The contour integral is written $\int_\gamma f\,dz$ or $\int_\gamma f(z)\,dz$. The length is $L(\gamma) = \int_a^b |\gamma'(t)|\,dt$. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Axiom Motivation

Real analysis has a notion of integration along an interval: $\int_a^b g(x)\,dx$ for $g$ continuous. To do complex analysis, we need an integration concept that lives on *curves* in $\mathbb{C}$ rather than intervals in $\mathbb{R}$. The definition must satisfy: (a) for *real* integrals along the real axis, it should reduce to the standard real integral; (b) it should be parametrization-invariant up to orientation; (c) it should support a *fundamental theorem* relating it to antiderivatives.

The standard definition meeting all three: for $\gamma : [a, b] \to U$ piecewise $C^1$ and $f$ continuous on the trace,
$$\int_\gamma f\,dz := \int_a^b f(\gamma(t)) \gamma'(t)\,dt.$$
The right-hand side is an integral *over an interval* — and the integrand is a complex-valued continuous function of a real parameter, integrated component-wise. So the contour integral is reduced to two standard real integrals.

Why multiply by $\gamma'(t)$? Because the "infinitesimal contribution" of $f$ to the integral, traveling along the curve at time $t$, is $f(\gamma(t)) \cdot$ (the infinitesimal displacement) $= f(\gamma(t)) \cdot \gamma'(t)\,dt$. The $\gamma'(t)$ factor accounts for both the speed of traversal and its direction. Without it, the integral would not be parametrization-invariant.

Parametrization invariance: if $\phi : [c, d] \to [a, b]$ is an increasing $C^1$ bijection, then $\delta = \gamma \circ \phi$ has $\delta'(s) = \gamma'(\phi(s))\phi'(s)$, and the integral $\int_c^d f(\delta(s))\delta'(s)\,ds = \int_c^d f(\gamma(\phi(s)))\gamma'(\phi(s))\phi'(s)\,ds = \int_a^b f(\gamma(t))\gamma'(t)\,dt$ (via substitution $t = \phi(s)$). Reversing orientation negates: if $-\gamma$ traverses the curve in reverse, $\int_{-\gamma} f\,dz = -\int_\gamma f\,dz$.

The notation $dz$ is more than mnemonic: it encodes the differential form interpretation. The 1-form $f(z)\,dz$ on $\mathbb{C}$ pulls back via $\gamma$ to the form $f(\gamma(t))\gamma'(t)\,dt$ on $[a, b]$, which is what we integrate. The contour integral is the integral of the pulled-back 1-form. This perspective unifies contour integration with integration of differential forms on manifolds.

Why require *continuous* $f$ on the trace, not just measurable or bounded? Because (a) we need $f(\gamma(t))$ to be Riemann-integrable as a function of $t$, and continuity suffices; (b) most theorems of complex analysis assume $f$ continuous (or stronger, holomorphic). The cleanest theory is for continuous integrands. Generalizations (Lebesgue, distributional) exist but are not needed at the introductory level.

The piecewise $C^1$ regularity of $\gamma$ is essential: it ensures $\gamma'(t)$ exists almost everywhere with continuous pieces, so the integral makes sense as a sum of Riemann integrals on each smooth piece.

---

# The Definition

Let $U \subseteq \mathbb{C}$ be open, $f : U \to \mathbb{C}$ continuous, and $\gamma : [a, b] \to U$ a piecewise $C^1$ curve.

**Contour integral.** The **contour integral** of $f$ along $\gamma$ is
$$\int_\gamma f\,dz := \int_a^b f(\gamma(t))\, \gamma'(t)\,dt.$$
The right-hand side is a Riemann integral of a complex-valued continuous function of a real variable. For piecewise $C^1$ curves, the integral is interpreted piece by piece and summed.

**Basic properties.**

(i) **Linearity.** $\int_\gamma (c_1 f_1 + c_2 f_2)\,dz = c_1 \int_\gamma f_1\,dz + c_2 \int_\gamma f_2\,dz$ for $c_1, c_2 \in \mathbb{C}$.

(ii) **Additivity over concatenation.** If $\gamma = \gamma_1 + \gamma_2$ (concatenation), then $\int_\gamma f\,dz = \int_{\gamma_1} f\,dz + \int_{\gamma_2} f\,dz$.

(iii) **Reversal.** If $-\gamma$ is $\gamma$ traversed in reverse, $\int_{-\gamma} f\,dz = -\int_\gamma f\,dz$.

(iv) **Parametrization invariance** (under increasing $C^1$ reparametrizations).

**Length of the curve.** $L(\gamma) := \int_a^b |\gamma'(t)|\,dt$, the arc length of $\gamma$ (independent of parametrization).

---

# Relate to Other Fields / Compression

In **multivariable calculus**, the contour integral is the *complex* analog of the line integral $\int_\gamma \vec F \cdot d\vec r = \int_a^b \vec F(\gamma(t)) \cdot \gamma'(t)\,dt$ for a vector field $\vec F : \mathbb{R}^2 \to \mathbb{R}^2$. Writing $f(z) = P + iQ$ and $dz = dx + idy$: $f\,dz = (P + iQ)(dx + idy) = (P\,dx - Q\,dy) + i(Q\,dx + P\,dy)$. So $\int_\gamma f\,dz$ decomposes into two real line integrals of related vector fields.

In **differential geometry**, $f(z)\,dz$ is a complex 1-form on $\mathbb{C}$, and $\int_\gamma f\,dz$ is the integration of a 1-form along a 1-manifold (the curve). Stokes' theorem applies: if $f\,dz$ is closed ($d(f\,dz) = 0$, equivalent to $f$ holomorphic), then the integral over the boundary of a 2-region equals the integral of the exterior derivative on the region — which is $0$. This is Cauchy's theorem in disguise.

In **measure theory**, the contour integral can be viewed as integration against the *complex measure* $\gamma'(t)\,dt$ on $[a, b]$ (or against the line-element measure on the trace $\gamma^*$, weighted by direction).

---

# Examples / Corollaries

**Is an instance — $\int_\gamma z^n\,dz$ for $\gamma(t) = e^{it}, t \in [0, 2\pi]$.** Compute: $\gamma'(t) = ie^{it}$, $f(\gamma(t)) = e^{int}$. So $\int_\gamma z^n\,dz = \int_0^{2\pi} e^{int} \cdot ie^{it}\,dt = i\int_0^{2\pi} e^{i(n+1)t}\,dt$. For $n \neq -1$: $\int_0^{2\pi} e^{i(n+1)t}\,dt = 0$. For $n = -1$: $i \int_0^{2\pi} 1\,dt = 2\pi i$. See [[Ex - Computing zn dz on a circle]].

**Is an instance — line segment from $0$ to $1 + i$.** Parametrize $\gamma(t) = t(1 + i), t \in [0, 1]$, so $\gamma'(t) = 1 + i$. For $f(z) = z$: $\int_\gamma z\,dz = \int_0^1 t(1+i)(1+i)\,dt = (1+i)^2 \int_0^1 t\,dt = (1+i)^2/2 = (2i)/2 = i$.

**Is NOT an instance — integral along a non-rectifiable curve.** A "curve" that is continuous but not piecewise $C^1$ may have infinite length (think: fractal). The contour integral is not defined for such curves (in the elementary theory).

**Corollary — the integral depends on orientation.** Reversing the path negates the integral. So $\int_\gamma$ is not a property of the trace alone, but of the trace *with orientation*.

**Corollary — additivity makes "closing" a contour meaningful.** If $\gamma$ is closed ($\gamma(a) = \gamma(b)$), the integral $\oint_\gamma f\,dz$ has special status as the "circulation" of $f$ around the closed loop. The fundamental theorem will say this integral is $0$ when $f$ has a primitive.

**Calibration check.** Compute $\int_\gamma \bar z\,dz$ for $\gamma$ the unit circle: $\bar z = e^{-it}$ on $\gamma$, so $\int_0^{2\pi} e^{-it} \cdot ie^{it}\,dt = i\int_0^{2\pi} 1\,dt = 2\pi i$. (This integral is nonzero, which is consistent with $\bar z$ being non-holomorphic.) Compare to $\int_\gamma z\,dz = \int_0^{2\pi} e^{it} \cdot ie^{it}\,dt = \int_0^{2\pi} ie^{2it}\,dt = 0$ — zero because $z$ is holomorphic (has primitive $z^2/2$).

---

# Unlocked by This

> [!tip] Fundamental Theorem of Contour Integration *(from this topic)*
> When $f$ has a primitive $F$, the contour integral is given by the endpoint difference: $\int_\gamma f\,dz = F(\gamma(b)) - F(\gamma(a))$. See [[Thm - Fundamental Theorem of Contour Integration]].

> [!tip] Cauchy's Theorem *(from this topic)*
> For $f$ holomorphic on a star-shaped (or simply connected) domain, the integral around any closed curve is zero. See [[Thm - Cauchy's Theorem for a Star-Shaped Domain]].

> [!tip] Residue Theorem *(from CA III)*
> For $f$ holomorphic except at isolated singularities, the contour integral around an enclosing curve is $2\pi i$ times the sum of residues. The **residue theorem** is the universal formula for contour integrals around singularities.
