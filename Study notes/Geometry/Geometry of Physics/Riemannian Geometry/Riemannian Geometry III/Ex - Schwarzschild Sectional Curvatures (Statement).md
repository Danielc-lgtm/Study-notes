---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Sectional Curvature"
  - "Def - Ricci Tensor"
  - "Def - Riemann Curvature Tensor"
tags: [geometry, riemannian-geometry, general-relativity, schwarzschild]
---

# Problem Statement

The **Schwarzschild metric** on $M = \mathbb{R} \times (2M, \infty) \times S^2$ is
$$g = -\left(1 - \frac{2M}{r}\right)dt^2 + \left(1 - \frac{2M}{r}\right)^{-1}dr^2 + r^2(d\theta^2 + \sin^2\theta\, d\varphi^2),$$
where $M > 0$ is the **Schwarzschild mass parameter** and we use units with $c = G = 1$. (Note: although Schwarzschild is Lorentzian, the curvature analysis below treats the orthonormal-frame components, which extracts essentially the Riemannian information up to sign conventions.)

(a) Compute the orthonormal coframe components of the [[Def - Riemann Curvature Tensor|Riemann tensor]] $R^a_{\;bcd}$ in the natural orthonormal coframe.

(b) Compute the orthonormal-frame sectional curvatures $K(\sigma)$ for the six standard $2$-planes spanned by pairs of orthonormal frame vectors $(\hat{t}, \hat{r}, \hat\theta, \hat\varphi)$.

(c) Verify the Ricci tensor vanishes: $\mathrm{Ric} = 0$ — i.e., Schwarzschild is a **vacuum solution** of Einstein's equations.

(d) Conclude that Schwarzschild is a **non-flat Ricci-flat** Lorentzian manifold: the Riemann tensor is nonzero (with components proportional to $M/r^3$, the **tidal forces** near a black hole), but its trace vanishes.

**Recall:**

The Schwarzschild metric is the unique (up to isometry) spherically symmetric vacuum solution of Einstein's field equations $G_{\mu\nu} = 0$ (equivalently $\mathrm{Ric} = 0$ in dim $\ge 3$). It describes the gravitational field outside a non-rotating, uncharged spherical mass of mass $M$. The coordinate $r$ is the **areal radius**: the area of the sphere $\{t = \mathrm{const}, r = \mathrm{const}\}$ is $4\pi r^2$. The hypersurface $\{r = 2M\}$ is the **event horizon** (the metric component $g_{tt}$ vanishes and $g_{rr}$ diverges in these Schwarzschild coordinates, but the geometry is regular — these are coordinate singularities).

The natural orthonormal coframe:
$$\hat{\sigma}^0 = \sqrt{1 - 2M/r}\,dt, \quad \hat{\sigma}^1 = (1 - 2M/r)^{-1/2}dr, \quad \hat{\sigma}^2 = r\,d\theta, \quad \hat{\sigma}^3 = r\sin\theta\, d\varphi.$$

---

# Convergent Strategy

**Problem class:** Curvature computation on a specific physically-motivated Riemannian (here Lorentzian, but same machinery) manifold. The metric has spherical symmetry plus a specific radial-$t$ structure that makes the orthonormal-frame computation tractable. The size of the computation is non-trivial (24 independent connection 1-form components, 6 independent curvature 2-form components in dim 4), so this exercise is rated **⭐⭐⭐** — a serious computational engagement.

**Assumption pattern:** Spherical symmetry + static (no $t$-dependence in the metric) means the curvature components depend only on $r$. The off-block-diagonal nature of the metric (no $dt\,dr$ or $dt\,d\Omega$ terms) means many off-diagonal curvature components vanish. The Ricci-flatness ($\mathrm{Ric} = 0$) is a consequence of the metric being a *vacuum* solution; verifying it is the main content of part (c).

**Theorem routing:** Cartan's structural equations in the orthonormal coframe. Compute $d\hat\sigma^a$; solve $d\hat\sigma^a + \omega^a_{\;b}\wedge\hat\sigma^b = 0$ for the connection 1-forms $\omega^a_{\;b}$; compute the curvature 2-forms $\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c}\wedge\omega^c_{\;b}$; read off $R^a_{\;bcd}$ and contract to $\mathrm{Ric}$.

**Key decision point:** The choice of orthonormal coframe is forced by the diagonal structure of the metric. The remaining work is bookkeeping: $24$ connection components, $20$ Riemann components (after antisymmetries), $10$ Ricci components, $1$ scalar curvature. The non-trivial step is the verification that Ricci vanishes — this requires careful tracking of cancellations that occur exactly because the metric is a vacuum solution.

---

# Legal Operations Used

1. **Operation 3 from the topic page (Cartan's structural equations).** The whole calculation is an application; in dimension $4$ this is substantial but mechanical.

2. **Operation 4 from the topic page (trace Riemann to get Ricci).** Part (c) verifies that $\sum_a R^a_{\;bac} = 0$ for all $(b, c)$.

---

# Hints

> [!note]- Hint 1
> Set up the orthonormal coframe and compute $d\hat\sigma^a$. Let $f(r) := \sqrt{1 - 2M/r}$ for brevity. Then $\hat\sigma^0 = f\, dt$, $\hat\sigma^1 = f^{-1}\, dr$, $\hat\sigma^2 = r\, d\theta$, $\hat\sigma^3 = r\sin\theta\, d\varphi$.

> [!note]- Hint 2
> Compute (with $f' = df/dr$, $f'/f = M/(r^2(1 - 2M/r)) \cdot 1/f = ...$):
> - $d\hat\sigma^0 = f'\, dr\wedge dt = f'(f^{-1}\hat\sigma^1)\wedge(f^{-1}\hat\sigma^0) = (f'/f^2)\hat\sigma^1 \wedge \hat\sigma^0$.
> - $d\hat\sigma^1 = -f^{-2}f'\, dr\wedge dr = 0$.
> - $d\hat\sigma^2 = dr\wedge d\theta = (f\hat\sigma^1)\wedge(\hat\sigma^2/r)\cdot (1/1)$... need to convert: $d\hat\sigma^2 = dr \wedge d\theta = f\hat\sigma^1\wedge(\hat\sigma^2/r) = (f/r)\hat\sigma^1\wedge\hat\sigma^2$.
> - $d\hat\sigma^3 = (\sin\theta\, dr + r\cos\theta\, d\theta)\wedge d\varphi = (f/r)\sin\theta\,\hat\sigma^1\wedge d\varphi + \cos\theta\,\hat\sigma^2\wedge d\varphi$; after converting $d\varphi = \hat\sigma^3/(r\sin\theta)$, this becomes $(f/r)\hat\sigma^1\wedge\hat\sigma^3 + (\cot\theta/r)\hat\sigma^2\wedge\hat\sigma^3$.

> [!note]- Hint 3
> Solve the first structural equation $d\hat\sigma^a + \omega^a_{\;b}\wedge\hat\sigma^b = 0$ using the skew-symmetry $\omega_{ab} = -\omega_{ba}$ (with the Lorentzian signature flipping the sign for the $0$-index). The connection 1-forms come out to:
> $\omega^0_{\;1} = (f'/f)\hat\sigma^0 = (M/(r^2 f^2))\hat\sigma^0$ (after substitution $f' = M/(r^2 f)$)
> $\omega^2_{\;1} = -(f/r)\hat\sigma^2$, $\omega^3_{\;1} = -(f/r)\hat\sigma^3$, $\omega^3_{\;2} = -(\cot\theta/r)\hat\sigma^3$. All others vanish or are determined by skew-symmetry.

> [!note]- Hint 4
> Compute curvature 2-forms $\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c}\wedge\omega^c_{\;b}$. After the (long) calculation, the *six* independent components (organised as orthonormal sectional curvatures) are:
> $$K(\hat t \wedge \hat r) = -2M/r^3, \quad K(\hat t \wedge \hat\theta) = K(\hat t \wedge \hat\varphi) = M/r^3,$$
> $$K(\hat r \wedge \hat\theta) = K(\hat r \wedge \hat\varphi) = M/r^3, \quad K(\hat\theta \wedge \hat\varphi) = -2M/r^3.$$
> (With Lorentzian signs: the radial-time and angular-angular sectional curvatures have opposite sign from the radial-angular and time-angular ones — the **Kepler tidal pattern**.)

> [!note]- Hint 5
> Verify Ricci vanishes: $\mathrm{Ric}(\hat t, \hat t) = -K(\hat t \wedge \hat r) - K(\hat t \wedge \hat\theta) - K(\hat t \wedge \hat\varphi) = -(-2M/r^3) - M/r^3 - M/r^3 = 2M/r^3 - 2M/r^3 = 0$. ✓ Similarly for the other diagonal components. The off-diagonal Ricci components vanish by the symmetries of the metric. Hence $\mathrm{Ric} = 0$: Schwarzschild is **vacuum**.

---

# Solution

The calculation is long; we summarise it in stages and verify the key conclusions. The full bookkeeping is in any standard GR textbook (Wald §6, Carroll §5).

**Plan:** Set up the orthonormal coframe; compute the four $d\hat\sigma^a$; solve the first structural equation for the six independent connection 1-forms $\omega^a_{\;b}$; compute the six independent curvature 2-forms $\Omega^a_{\;b}$ via the second structural equation; read off the Riemann tensor components, sectional curvatures, and verify $\mathrm{Ric} = 0$.

**Step 1: Orthonormal coframe and $d\hat\sigma^a$.**

> [!note]- Derivation
> Let $f(r) = \sqrt{1 - 2M/r}$. Coframe: $\hat\sigma^0 = f\,dt$, $\hat\sigma^1 = f^{-1}\,dr$, $\hat\sigma^2 = r\,d\theta$, $\hat\sigma^3 = r\sin\theta\,d\varphi$. Verification: $g = -\hat\sigma^0\otimes\hat\sigma^0 + \hat\sigma^1\otimes\hat\sigma^1 + \hat\sigma^2\otimes\hat\sigma^2 + \hat\sigma^3\otimes\hat\sigma^3$ matches the given metric.
>
> Compute exterior derivatives:
> - $d\hat\sigma^0 = f'\,dr\wedge dt = f'(f^{-1}\hat\sigma^1)\wedge(f^{-1}\hat\sigma^0) = (f'/f^2)\hat\sigma^1\wedge\hat\sigma^0$. Using $f' = M/(r^2 f)$ (chain rule on $f = (1-2M/r)^{1/2}$), $f'/f^2 = M/(r^2 f^3)$. So $d\hat\sigma^0 = (M/(r^2 f^3))\hat\sigma^1\wedge\hat\sigma^0$.
> - $d\hat\sigma^1 = d(f^{-1}\,dr) = -f^{-2}f'\,dr\wedge dr = 0$.
> - $d\hat\sigma^2 = dr\wedge d\theta = (f\hat\sigma^1)\wedge(\hat\sigma^2/r) = (f/r)\hat\sigma^1\wedge\hat\sigma^2$.
> - $d\hat\sigma^3 = (\sin\theta\,dr + r\cos\theta\,d\theta)\wedge d\varphi = (f/r)\hat\sigma^1\wedge\hat\sigma^3 + (\cot\theta/r)\hat\sigma^2\wedge\hat\sigma^3$.

**Step 2: Connection 1-forms from the first structural equation.**

> [!note]- Derivation
> Lorentzian skew-symmetry: $\omega_{ab} = -\omega_{ba}$ with the Lorentzian metric raising/lowering indices, giving $\omega^a_{\;b}$ such that $\omega^0_{\;1} = \omega^1_{\;0}$ (note: $+$ sign because of $g^{00} = -1$). Working through:
> - $\omega^0_{\;1} = (M/(r^2 f^2))\hat\sigma^0 = $ proportional to $dt$, capturing time-dilation effects.
> - $\omega^2_{\;1} = -(f/r)\hat\sigma^2 = -f\,d\theta$.
> - $\omega^3_{\;1} = -(f/r)\hat\sigma^3 = -f\sin\theta\,d\varphi$.
> - $\omega^3_{\;2} = -(\cot\theta/r)\hat\sigma^3 = -\cos\theta\,d\varphi$.
> 
> (The remaining $\omega^a_{\;b}$ are determined by skew-symmetry and the absence of off-diagonal metric components.)

**Step 3: Curvature 2-forms and sectional curvatures.**

> [!note]- Derivation
> Compute $\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c}\wedge\omega^c_{\;b}$ for each pair. The (rather long) calculation gives:
> - $\Omega^0_{\;1} = (-2M/r^3)\hat\sigma^0\wedge\hat\sigma^1$
> - $\Omega^0_{\;2} = (M/r^3)\hat\sigma^0\wedge\hat\sigma^2$
> - $\Omega^0_{\;3} = (M/r^3)\hat\sigma^0\wedge\hat\sigma^3$
> - $\Omega^1_{\;2} = (M/r^3)\hat\sigma^1\wedge\hat\sigma^2$
> - $\Omega^1_{\;3} = (M/r^3)\hat\sigma^1\wedge\hat\sigma^3$
> - $\Omega^2_{\;3} = (-2M/r^3)\hat\sigma^2\wedge\hat\sigma^3$
>
> Sectional curvatures (with Lorentzian signs):
> $$K(\hat t \wedge \hat r) = -\frac{2M}{r^3}, \quad K(\hat t \wedge \hat\theta) = K(\hat t \wedge \hat\varphi) = \frac{M}{r^3},$$
> $$K(\hat r \wedge \hat\theta) = K(\hat r \wedge \hat\varphi) = \frac{M}{r^3}, \quad K(\hat\theta \wedge \hat\varphi) = -\frac{2M}{r^3}.$$
>
> The **tidal pattern**: time-radial and angular-angular planes have "stretching" ($K = -2M/r^3$), while the cross-mixed planes have "compression" ($K = M/r^3$). This is the classical **Newtonian tidal pattern** of a $1/r^3$ stretching along the radial direction and $1/r^3$ compression in the transverse directions, recovered exactly from GR.

**Step 4: Verify $\mathrm{Ric} = 0$.**

> [!note]- Derivation
> $\mathrm{Ric}(\hat t, \hat t) = \sum_{j \ne 0}K(\hat t \wedge \hat e_j) = K(\hat t \wedge \hat r) + K(\hat t \wedge \hat\theta) + K(\hat t \wedge \hat\varphi) = -2M/r^3 + M/r^3 + M/r^3 = 0$. ✓
>
> (Wait: in Lorentzian signature, the Ricci-curvature formula involves signs; the **right formula** in Lorentzian signature with our convention $K(\hat e_i, \hat e_j) = \epsilon_i\epsilon_j\langle R(e_i, e_j)e_j, e_i\rangle$ where $\epsilon_0 = -1, \epsilon_\alpha = +1$ gives the formula above. The cleanest way is to compute $\mathrm{Ric}^a_{\;b} = R^c_{\;acb}$ directly in components.)
>
> Similarly: $\mathrm{Ric}(\hat r, \hat r) = K(\hat r \wedge \hat t) + K(\hat r \wedge \hat\theta) + K(\hat r \wedge \hat\varphi) = -2M/r^3 + M/r^3 + M/r^3 = 0$. ✓ ($K(\hat r \wedge \hat t) = K(\hat t \wedge \hat r)$ by symmetry of unsigned $2$-plane.)
>
> $\mathrm{Ric}(\hat\theta, \hat\theta) = K(\hat\theta \wedge \hat t) + K(\hat\theta \wedge \hat r) + K(\hat\theta \wedge \hat\varphi) = M/r^3 + M/r^3 + (-2M/r^3) = 0$. ✓
>
> Similarly $\mathrm{Ric}(\hat\varphi, \hat\varphi) = 0$.
>
> Off-diagonal: by the diagonal structure of the metric and the symmetries of $R$, all off-diagonal Ricci components vanish.
>
> Conclusion: $\mathrm{Ric} = 0$ everywhere on the Schwarzschild manifold (for $r > 2M$). Schwarzschild is a **vacuum solution** of Einstein's equations $\mathrm{Ric} = 0$.

> [!note]- Complete formal solution
> Orthonormal coframe: $\hat\sigma^0 = f\,dt$, $\hat\sigma^1 = f^{-1}\,dr$, $\hat\sigma^2 = r\,d\theta$, $\hat\sigma^3 = r\sin\theta\,d\varphi$, with $f = \sqrt{1 - 2M/r}$. Cartan's structural equations yield connection 1-forms and curvature 2-forms with sectional curvatures
> $$K(\hat t \wedge \hat r) = K(\hat\theta \wedge \hat\varphi) = -\frac{2M}{r^3}, \quad K(\text{other planes}) = +\frac{M}{r^3}.$$
> The trace $\mathrm{Ric}(\hat e_a, \hat e_a) = \sum_{b \ne a}K(\hat e_a \wedge \hat e_b)$ gives $0$ for each $a$ — Schwarzschild is **Ricci-flat**, hence a vacuum solution of Einstein's equations. The Riemann tensor itself is *not* zero (with all sectional curvatures of order $M/r^3$), so spacetime is curved — these are the tidal forces felt near a black hole.

> [!warning] Illegal but tempting alternative route
> One might attempt to compute Christoffel symbols $\Gamma^a_{\;bc}$ from the metric and then the Riemann tensor as $R^a_{\;bcd} = \partial_c\Gamma^a_{\;bd} - \partial_d\Gamma^a_{\;bc} + \Gamma^a_{\;ce}\Gamma^e_{\;bd} - \Gamma^a_{\;de}\Gamma^e_{\;bc}$ in coordinates. This requires computing $\sim 20$ Christoffel symbols and then $\sim 256$ Riemann components, of which the algebraic symmetries reduce most to zero. The Cartan method is dramatically faster: $6$ connection 1-forms, $6$ curvature 2-forms. **Repair:** always use Cartan's method when an orthonormal coframe is available.

---

# Key Takeaways

**The Schwarzschild tidal pattern $K \propto M/r^3$ is the GR generalisation of Newton's $1/r^3$ tidal force.** In Newtonian gravity, a test cloud of particles falling in a $-GM/r^2$ field is stretched radially at rate $2GM/r^3$ and compressed transversely at rate $GM/r^3$ — the **tidal pattern**. The exact same pattern emerges as the sectional curvatures of the Schwarzschild geometry, with the GR sectional curvature of the radial-time plane being $-2M/r^3$ and the transverse planes $+M/r^3$. This is one of the most beautiful Newtonian-to-GR correspondences: the GR curvature *is* the Newtonian tidal field, derived from first principles.

**Ricci-flat ≠ flat. Schwarzschild is the prototype.** Schwarzschild has $\mathrm{Ric} = 0$ but $R \ne 0$ — the Riemann tensor has components of order $M/r^3$ that diverge as $r \to 0$ (the **true** Schwarzschild singularity). The vacuum Einstein equations $\mathrm{Ric} = 0$ are a system of $10$ second-order PDEs in $4$ dimensions; they have a huge solution space, including Schwarzschild, Kerr (rotating black hole), all gravitational-wave solutions, and the various **Petrov classification** types. The conditions "Ricci-flat" and "flat" coincide only in dim $\le 3$ (since the Riemann tensor in those dimensions is determined by Ricci).

**Schwarzschild is the simplest "non-trivial" vacuum solution of GR.** By **Birkhoff's theorem**, every spherically symmetric vacuum solution of Einstein's equations is locally isometric to Schwarzschild. So Schwarzschild is the *unique* spherically symmetric vacuum geometry — any GR exterior of a non-rotating spherically symmetric mass distribution is Schwarzschild (regardless of the matter's pulsations, contractions, etc., as long as the symmetry is preserved). This is the GR analogue of Newton's theorem that the gravitational field outside a spherical mass shell is that of a point mass.

**Companion cross-references:** the [[Thm - First and Second Bianchi Identities|second Bianchi identity]] ensures the consistency of $\mathrm{Ric} = 0$ as a complete vacuum-equation system (no over-determination). For the cosmological implications and the full structure of Einstein's equations, see [[General Relativity I — Einstein's Equations and Schwarzschild]] where the full geometric content of $G_{\mu\nu} = 8\pi T_{\mu\nu}$ is developed.
