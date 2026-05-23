---
type: definition
subject: riemannian-geometry
prereqs:
  - "Def - Ricci Tensor"
  - "Def - Sectional Curvature"
tags: [geometry, riemannian-geometry, curvature]
---

# Notation

$(M, g)$ is a Riemannian manifold of dimension $n$ with [[Def - Ricci Tensor|Ricci tensor]] $\mathrm{Ric}$. The metric components are $g_{ab}$ with inverse $g^{ab}$ (so $g^{ab}g_{bc} = \delta^a_c$). Sectional curvature of the $2$-plane spanned by $e_a, e_b$ in an orthonormal frame is $K(e_a \wedge e_b)$. Einstein summation is used throughout.

---

# Axiom Motivation

We have descended one trace from the Riemann tensor to the Ricci tensor. The Ricci tensor is symmetric $(0, 2)$, much smaller than $R$ but still matrix-valued. The natural next move is to take *another* trace, paring down to a single function on the manifold — a scalar. This is the **scalar curvature**.

The definition is forced: there is only one nonzero way to trace a symmetric $(0, 2)$-tensor against the metric, namely $S = g^{ab}\mathrm{Ric}_{ab}$. The desideratum is that this scalar carry interpretable geometric information; specifically, it should be the sum of all sectional curvatures in a sense that generalises the surface case (where $S = 2K$).

This works out: in an orthonormal frame $(e_1, \ldots, e_n)$ at $p$,

$$S(p) = \sum_a \mathrm{Ric}(e_a, e_a) = \sum_a \sum_{b \neq a} K(e_a \wedge e_b) = \sum_{a \neq b} K(e_a \wedge e_b) = 2 \sum_{a < b} K(e_a \wedge e_b).$$

So **the scalar curvature is twice the sum of the sectional curvatures over all unordered pairs of orthonormal basis directions.** For a surface ($n = 2$, one pair), this is $S = 2K$; for the unit $n$-sphere ($\binom{n}{2}$ pairs, each with $K = 1$), this is $S = n(n-1)$.

Why not normalise by dividing by the number of pairs, $\binom{n}{2}$? The unnormalised sum is what appears in the **Einstein–Hilbert action** of general relativity,

$$S_{\mathrm{EH}}[g] = \int_M S\, dV_g,$$

whose Euler–Lagrange equations are the **vacuum Einstein equations** $\mathrm{Ric} = 0$ (in dimension $\ge 3$; in dimension $2$ the action is topological by Gauss–Bonnet). The lack of a normalisation factor is what makes the variational structure clean — adding a normalisation would introduce dimension-dependent constants. The unnormalised $S$ is also what appears in the **Bochner formula** and in scaling identities for the Yamabe problem.

What is lost in passing from Ricci to scalar curvature? Quite a lot. The Bonnet–Myers diameter bound, the sphere theorem, and most comparison theorems require Ricci or sectional bounds, not scalar bounds. The scalar curvature controls a small but important class of theorems: the **Yamabe problem** (find a conformal metric of constant scalar curvature; solved by Schoen–Trudinger–Yamabe–Aubin), the **positive mass theorem** of general relativity (Schoen–Yau, using a nonnegative scalar curvature spinor identity), and the **Gauss–Bonnet theorem** in dimension $2$ (where $S = 2K$ and $\int S\, dV = 4\pi\chi(M)$).

What if we tried to define scalar curvature without first defining Ricci? You could: $S = g^{ac}g^{bd}R_{abcd}$, contracting the full Riemann tensor with two factors of the inverse metric. The result is the same; this is just the double trace, $g^{ab}\mathrm{Ric}_{ab}$, written out. The Ricci tensor is the intermediate object, but you can skip it if you only care about $S$.

---

# The Definition

> **Definition (Scalar curvature).** Let $(M, g)$ be a Riemannian manifold with Ricci tensor $\mathrm{Ric}$. The **scalar curvature** is the smooth function
>
> $$S := g^{ab}\mathrm{Ric}_{ab} = \mathrm{tr}_g \mathrm{Ric}.$$
>
> Equivalently, in an orthonormal frame, $S(p) = \sum_a \mathrm{Ric}(e_a, e_a) = 2\sum_{a < b} K(e_a \wedge e_b)$.

The scalar curvature is sometimes denoted $R$ in physics texts (where it never gets confused with the full Riemann tensor by context), or $\mathrm{Scal}$ in differential-geometry texts.

---

# Relate to Other Fields / Compression

In **general relativity**, the scalar curvature appears in the Einstein tensor $G_{ab} = \mathrm{Ric}_{ab} - \tfrac{1}{2}g_{ab}S$ and in the Einstein–Hilbert action $\int S\, dV$. Varying the Einstein–Hilbert action with respect to $g$ produces the vacuum Einstein equations $G_{ab} = 0$, equivalently $\mathrm{Ric} = 0$ in $n \geq 3$.

In **conformal geometry**, scalar curvature transforms under conformal changes $\tilde g = e^{2f}g$ in a specific way that is the heart of the **Yamabe problem**: find a conformal rescaling making the scalar curvature constant. The problem reduces to an elliptic PDE for $f$ (the **Yamabe equation**), and the existence question was settled by Schoen ($1984$) completing earlier work of Trudinger, Yamabe, and Aubin.

In **mathematical physics**, the **positive mass theorem** (Schoen–Yau, $1979$; Witten's spinor proof, $1981$) says that a complete asymptotically-flat $3$-manifold with nonnegative scalar curvature has nonnegative ADM mass, with equality iff the manifold is Euclidean. This connects scalar curvature to a global asymptotic invariant.

**True name:** *Scalar curvature at $p$ is twice the sum of sectional curvatures over all $\binom{n}{2}$ unordered pairs of orthonormal basis directions at $p$.* Equivalently, the leading-order coefficient in the small-radius expansion of the volume of geodesic balls,

$$\mathrm{vol}(B_r(p)) = \omega_n r^n\left(1 - \frac{S(p)}{6(n+2)}r^2 + O(r^4)\right),$$

where $\omega_n$ is the volume of the unit Euclidean ball. Positive scalar curvature means small geodesic balls have *less* volume than in flat space; negative scalar curvature, more.

---

# Examples / Corollaries

**Example 1 (constant sectional curvature).** If $K \equiv K_0$, then $\mathrm{Ric} = (n-1)K_0\, g$ and $S = n(n-1)K_0$. For the unit $n$-sphere, $S = n(n-1)$; for the unit $n$-hyperbolic space, $S = -n(n-1)$. For $\mathbb{R}^n$, $S = 0$.

**Example 2 (surface).** On a $2$-manifold $(M, g)$, $S = 2K$ where $K$ is the Gauss curvature. Both are functions on $M$. The Gauss–Bonnet theorem reads $\int_M K\, dV = 2\pi\chi(M)$, equivalently $\tfrac{1}{2}\int_M S\, dV = 2\pi\chi(M)$ — the scalar curvature integral computes the Euler characteristic times $4\pi$. This is the prototype of all higher-dimensional integral-curvature-equals-topology results.

**Example 3 (Calabi–Yau).** A **Calabi–Yau manifold** has $\mathrm{Ric} = 0$, hence $S = 0$. The scalar curvature is zero but the Riemann tensor and even the sectional curvatures need not vanish.

**Example 4 (constant scalar curvature on a sphere).** The standard round $S^n$ has constant scalar curvature $n(n-1)$. The Yamabe problem asks whether every conformal class on a compact manifold contains a metric of constant scalar curvature. The sphere case is part of the **Yamabe constant** of $S^n$ and feeds into the resolution.

**Non-example.** $S > 0$ does **not** imply $\mathrm{Ric} > 0$. The product $S^2 \times H^2$ with the standard product metric has $S = 2 - 2 = 0$ in the simplest case (and can be made positive or negative depending on radii) but $\mathrm{Ric}$ has eigenvalues $+1$ on the $S^2$ factor and $-1$ on the $H^2$ factor — never positive-definite.

**Non-example.** The scalar curvature alone does not control diameter, fundamental group, or topology in the strong ways that Ricci does. There is no Bonnet–Myers analogue for scalar curvature. The theorems that *do* work with scalar curvature (Yamabe, positive mass) require either a topological hypothesis or a global structure (asymptotic flatness).

**Calibration check.** If you have understood the definition correctly you should be able to: (a) compute $S = n(n-1)K_0$ on a constant-curvature-$K_0$ manifold; (b) verify $S = 2K$ on a $2$-manifold; (c) write down the Einstein tensor $G_{ab} = \mathrm{Ric}_{ab} - \tfrac{1}{2}g_{ab}S$ and recognise this as the divergence-free combination from Bianchi.

---

# Unlocked by This

> [!tip] Einstein–Hilbert Action *(from General Relativity)*
> In general relativity, the scalar curvature is the **Lagrangian density of gravity**: the Einstein–Hilbert action $S_{\mathrm{EH}}[g] = (16\pi G)^{-1}\int_M S\, dV_g$ has the vacuum Einstein equations as its Euler–Lagrange equations. Coupling to matter via $S_{\mathrm{matter}}[g, \psi]$ and varying gives the full Einstein equations $G_{ab} = 8\pi T_{ab}$. See [[General Relativity I — Einstein's Equations and Schwarzschild]].

> [!tip] Yamabe Problem *(from Geometric Analysis)*
> Given a compact Riemannian manifold $(M, g_0)$, the **Yamabe problem** asks for a conformal rescaling $g = e^{2f}g_0$ with constant scalar curvature. This reduces to an elliptic PDE for $f$, the **Yamabe equation**, and was solved through the combined work of Yamabe, Trudinger, Aubin, and **Schoen** (the latter handling the most delicate critical exponent cases in dimensions $3, 4, 5$). The Yamabe constant of a conformal class is a fundamental conformal invariant.

> [!tip] Positive Mass Theorem *(from General Relativity)*
> The **positive mass theorem** of **Schoen–Yau** (1979) and **Witten** (1981, spinor proof) says: a complete asymptotically-flat $3$-manifold with nonnegative scalar curvature has nonnegative ADM mass. This is one of the deepest connections between scalar curvature and global asymptotic geometry; it underpins much of mathematical general relativity.

> [!tip] Gauss–Bonnet Theorem *(from Riemannian Geometry IV)*
> On a closed orientable $2$-manifold, $\int_M K\, dV = 2\pi\chi(M)$, equivalently $\tfrac{1}{2}\int_M S\, dV = 2\pi\chi(M)$. This is the simplest **characteristic class** integral-curvature identity; the higher-dimensional **Chern–Gauss–Bonnet** generalisation integrates a curvature polynomial (the Pfaffian of $R$) to compute $\chi(M)$.
