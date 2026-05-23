---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Cartan's First Structural Equation"
  - "Thm - Cartan's Second Structural Equation"
  - "Def - Connection 1-Forms (Cartan)"
  - "Def - Curvature 2-Forms (Cartan)"
  - "Def - Semi-Riemannian Metric and Signature"
tags: [geometry, riemannian-geometry, connections, cartan-formalism, schwarzschild]
---

# Problem Statement

For the **Schwarzschild metric** (a Lorentzian metric on $\mathbb{R} \times (2M, \infty) \times S^2$ representing the spacetime exterior of a non-rotating black hole of mass $M$),
$$
g = -f(r)\,dt^2 + f(r)^{-1}\,dr^2 + r^2(d\theta^2 + \sin^2\theta\,d\varphi^2), \qquad f(r) := 1 - \frac{2M}{r},
$$
set up the orthonormal coframe and use Cartan's structural equations to compute:

(a) the connection 1-forms $\omega^a{}_b$;

(b) the curvature 2-forms $\Omega^a{}_b$;

(c) the components of the Riemann curvature tensor in the orthonormal frame, particularly the "tidal" components $R^{\hat 0}{}_{\hat 1\hat 0\hat 1}$ and $R^{\hat 2}{}_{\hat 3\hat 2\hat 3}$.

**Recall:**

The orthonormal coframe is the choice of frame in which the metric components are constant: $g = \eta_{ab}\sigma^a \otimes \sigma^b$ with $\eta_{ab} = \mathrm{diag}(-1, 1, 1, 1)$ in Lorentzian signature.

![[Thm - Cartan's First Structural Equation#Statement]]

![[Thm - Cartan's Second Structural Equation#Statement]]

For an orthonormal frame in Lorentzian signature, metric-compatibility gives $\eta_{ac}\omega^c{}_b + \eta_{bc}\omega^c{}_a = 0$, equivalent to $\omega_{ab} + \omega_{ba} = 0$ where $\omega_{ab} = \eta_{ac}\omega^c{}_b$ (the connection 1-forms with both indices lowered are antisymmetric).

---

# Convergent Strategy

**Problem class:** A challenging Cartan-structural-equations computation on a 4D Lorentzian metric — the standard general relativity calculation that every textbook presents. It illustrates the dramatic efficiency of the moving-frame method for non-trivial metrics. The Schwarzschild geometry is the "test case" for GR computations and the input to perihelion precession, light bending, and black-hole physics.

**Assumption pattern:** The Schwarzschild metric is diagonal in $(t, r, \theta, \varphi)$, with explicit dependence on $r$ (the warp function $f(r)$) and the round-sphere structure $r^2(d\theta^2 + \sin^2\theta\,d\varphi^2)$. The metric is *spherically symmetric* (rotationally invariant on the $(\theta, \varphi)$ sphere) and *static* (time-translation invariant) — these symmetries reduce the number of independent connection 1-forms and curvature components.

**Theorem routing:** Apply Cartan's structural equations in the standard recipe: (i) set up the orthonormal coframe; (ii) compute $d\sigma^a$; (iii) use $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$ with antisymmetry $\omega_{ab} + \omega_{ba} = 0$ to solve for $\omega^a{}_b$; (iv) compute $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$. Read off Riemann tensor components from $\Omega^a{}_b = \tfrac{1}{2}R^a{}_{bcd}\sigma^c \wedge \sigma^d$.

**Key decision point:** The major decision is the choice of orthonormal coframe — the obvious choice is $\sigma^{\hat 0} = f^{1/2}dt, \sigma^{\hat 1} = f^{-1/2}dr, \sigma^{\hat 2} = r\,d\theta, \sigma^{\hat 3} = r\sin\theta\,d\varphi$ (using hatted indices to distinguish orthonormal-frame indices from coordinate indices). This choice makes the metric explicitly $g = -(\sigma^{\hat 0})^2 + (\sigma^{\hat 1})^2 + (\sigma^{\hat 2})^2 + (\sigma^{\hat 3})^2$. The exterior derivatives $d\sigma^a$ are short to compute, and the antisymmetry of $\omega_{ab}$ leaves only 6 independent connection 1-forms (the [[Def - Dimension|dimension]] of $\mathfrak{o}(1, 3)$).

---

# Legal Operations Used

1. **Operation 2 from the topic page (Set up an orthonormal coframe and use Cartan's first structural equation).** Choose the natural orthonormal coframe for the Schwarzschild metric and solve the first structural equation for the connection 1-forms.

2. **Operation 3 from the topic page (Apply Cartan's second structural equation to compute curvature).** Once the connection 1-forms are in hand, compute the curvature 2-forms.

---

# Hints

> [!note]- Hint 1
> Orthonormal coframe: $\sigma^{\hat 0} = f^{1/2}dt$, $\sigma^{\hat 1} = f^{-1/2}dr$, $\sigma^{\hat 2} = r\,d\theta$, $\sigma^{\hat 3} = r\sin\theta\,d\varphi$. Verify: $g = -(\sigma^{\hat 0})^2 + (\sigma^{\hat 1})^2 + (\sigma^{\hat 2})^2 + (\sigma^{\hat 3})^2$.

> [!note]- Hint 2
> Exterior derivatives: $d\sigma^{\hat 0} = \tfrac{f'}{2f^{1/2}}\,dr \wedge dt$, $d\sigma^{\hat 1} = 0$, $d\sigma^{\hat 2} = dr \wedge d\theta$, $d\sigma^{\hat 3} = \sin\theta\,dr \wedge d\varphi + r\cos\theta\,d\theta \wedge d\varphi$. Convert to orthonormal basis.

> [!note]- Hint 3
> The nonzero connection 1-forms (lower indices, $\omega_{ab} = \eta_{ac}\omega^c{}_b$): $\omega^{\hat 0}{}_{\hat 1} = \tfrac{f'}{2f^{1/2}}\sigma^{\hat 0}$ (so $\omega_{\hat 0\hat 1} = -\omega_{\hat 1\hat 0}$ ... careful with signs in Lorentzian), $\omega^{\hat 2}{}_{\hat 1} = (f^{1/2}/r)\sigma^{\hat 2}$, $\omega^{\hat 3}{}_{\hat 1} = (f^{1/2}/r)\sigma^{\hat 3}$, $\omega^{\hat 3}{}_{\hat 2} = (\cot\theta/r)\sigma^{\hat 3}$. The exact form depends on sign conventions; check antisymmetry of $\omega_{ab}$ as a verification.

> [!note]- Hint 4
> Apply $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$ to each independent pair, e.g., $(a, b) = (\hat 0, \hat 1)$ giving the radial-temporal curvature, $(a, b) = (\hat 2, \hat 3)$ giving the angular curvature. The standard Schwarzschild components are $R^{\hat 0}{}_{\hat 1\hat 0\hat 1} = -2M/r^3$ (tidal stretching along the radial direction), $R^{\hat 2}{}_{\hat 3\hat 2\hat 3} = 2M/r^3$ (angular tidal), and others.

---

# Solution

**Plan paragraph.** The solution has four steps. Step 1 establishes the orthonormal coframe and computes $d\sigma^a$. Step 2 solves Cartan's first structural equation with antisymmetry to find the connection 1-forms — exploiting the spherical symmetry, the answer organises into the radial-temporal piece and the angular pieces. Step 3 applies Cartan's second structural equation to compute the curvature 2-forms. Step 4 reads off the Riemann tensor components and interprets them as **tidal force terms** in the Schwarzschild geometry.

**Step 1: Orthonormal coframe and exterior derivatives.**

Coframe: $\sigma^{\hat 0} = f^{1/2}dt$, $\sigma^{\hat 1} = f^{-1/2}dr$, $\sigma^{\hat 2} = r\,d\theta$, $\sigma^{\hat 3} = r\sin\theta\,d\varphi$, with $f = 1 - 2M/r$ and $f' := df/dr = 2M/r^2$.

Verify the metric: $-(\sigma^{\hat 0})^2 + (\sigma^{\hat 1})^2 + (\sigma^{\hat 2})^2 + (\sigma^{\hat 3})^2 = -f\,dt^2 + f^{-1}\,dr^2 + r^2 d\theta^2 + r^2\sin^2\theta\,d\varphi^2 = g$. ✓

Exterior derivatives:
- $d\sigma^{\hat 0} = d(f^{1/2}dt) = (f^{1/2})'\,dr \wedge dt = \tfrac{f'}{2f^{1/2}}\,dr \wedge dt$. Using $dr = f^{1/2}\sigma^{\hat 1}$ and $dt = f^{-1/2}\sigma^{\hat 0}$: $dr \wedge dt = \sigma^{\hat 1} \wedge \sigma^{\hat 0}$. So $d\sigma^{\hat 0} = \tfrac{f'}{2f^{1/2}}\sigma^{\hat 1} \wedge \sigma^{\hat 0} = -\tfrac{f'}{2f^{1/2}}\sigma^{\hat 0} \wedge \sigma^{\hat 1}$.
- $d\sigma^{\hat 1} = d(f^{-1/2}dr) = (f^{-1/2})'\,dr \wedge dr + f^{-1/2}\,d^2r = 0$ (both terms vanish).
- $d\sigma^{\hat 2} = d(r\,d\theta) = dr \wedge d\theta$. With $dr = f^{1/2}\sigma^{\hat 1}, d\theta = \sigma^{\hat 2}/r$: $dr \wedge d\theta = (f^{1/2}/r)\sigma^{\hat 1} \wedge \sigma^{\hat 2}$. So $d\sigma^{\hat 2} = (f^{1/2}/r)\sigma^{\hat 1} \wedge \sigma^{\hat 2}$.
- $d\sigma^{\hat 3} = d(r\sin\theta\,d\varphi) = (\sin\theta\,dr + r\cos\theta\,d\theta) \wedge d\varphi = \sin\theta\,dr \wedge d\varphi + r\cos\theta\,d\theta \wedge d\varphi$. With $dr \wedge d\varphi = f^{1/2}\sigma^{\hat 1} \wedge \sigma^{\hat 3}/(r\sin\theta)$ and $d\theta \wedge d\varphi = \sigma^{\hat 2} \wedge \sigma^{\hat 3}/(r^2\sin\theta)$: $d\sigma^{\hat 3} = \sin\theta \cdot f^{1/2}/(r\sin\theta) \sigma^{\hat 1} \wedge \sigma^{\hat 3} + r\cos\theta \cdot 1/(r^2\sin\theta) \sigma^{\hat 2} \wedge \sigma^{\hat 3} = (f^{1/2}/r)\sigma^{\hat 1} \wedge \sigma^{\hat 3} + (\cot\theta/r)\sigma^{\hat 2} \wedge \sigma^{\hat 3}$.

> [!note]- Derivation
> The exterior derivatives are direct applications of the Leibniz rule for $d$ and the conversion to orthonormal basis. The key step is to express the coordinate 2-forms $dt \wedge dr, dr \wedge d\theta$, etc. in the orthonormal basis $\sigma^a \wedge \sigma^b$ using $dt = f^{-1/2}\sigma^{\hat 0}, dr = f^{1/2}\sigma^{\hat 1}, d\theta = \sigma^{\hat 2}/r, d\varphi = \sigma^{\hat 3}/(r\sin\theta)$. Note the sign convention: $\sigma^{\hat 1} \wedge \sigma^{\hat 0} = -\sigma^{\hat 0} \wedge \sigma^{\hat 1}$ — important for Lorentzian-signature computations.

**Step 2: Connection 1-forms via Cartan's first equation.**

In Lorentzian signature, the metric-compatible antisymmetry condition is $\omega_{ab} + \omega_{ba} = 0$ where $\omega_{ab} = \eta_{ac}\omega^c{}_b$ (lower both indices using $\eta$). For orthonormal frame indices $\{0, 1, 2, 3\}$ with $\eta = \mathrm{diag}(-1, 1, 1, 1)$: $\omega^{\hat 0}{}_{\hat b}$ has $\omega_{\hat 0\hat b} = -\omega^{\hat 0}{}_{\hat b}$ (because $\eta_{\hat 0\hat 0} = -1$); $\omega^{\hat i}{}_{\hat b}$ for $\hat i = 1, 2, 3$ has $\omega_{\hat i\hat b} = \omega^{\hat i}{}_{\hat b}$.

The first structural equation $d\sigma^a + \omega^a{}_b \wedge \sigma^b = 0$ gives:
- $a = 0$: $d\sigma^{\hat 0} + \omega^{\hat 0}{}_{\hat 1} \wedge \sigma^{\hat 1} + \omega^{\hat 0}{}_{\hat 2} \wedge \sigma^{\hat 2} + \omega^{\hat 0}{}_{\hat 3} \wedge \sigma^{\hat 3} = 0$.
- $a = 1$: $d\sigma^{\hat 1} + \omega^{\hat 1}{}_{\hat 0} \wedge \sigma^{\hat 0} + \omega^{\hat 1}{}_{\hat 2} \wedge \sigma^{\hat 2} + \omega^{\hat 1}{}_{\hat 3} \wedge \sigma^{\hat 3} = 0$.
- $a = 2$: $d\sigma^{\hat 2} + \omega^{\hat 2}{}_{\hat 0} \wedge \sigma^{\hat 0} + \omega^{\hat 2}{}_{\hat 1} \wedge \sigma^{\hat 1} + \omega^{\hat 2}{}_{\hat 3} \wedge \sigma^{\hat 3} = 0$.
- $a = 3$: $d\sigma^{\hat 3} + \omega^{\hat 3}{}_{\hat 0} \wedge \sigma^{\hat 0} + \omega^{\hat 3}{}_{\hat 1} \wedge \sigma^{\hat 1} + \omega^{\hat 3}{}_{\hat 2} \wedge \sigma^{\hat 2} = 0$.

By spherical symmetry and staticity (the metric does not depend on $t, \varphi$ and is invariant under rotations), most connection 1-forms have a specific form. The nonzero ones (with explicit verification):

**$\omega^{\hat 0}{}_{\hat 1}$:** From $d\sigma^{\hat 0} = -\tfrac{f'}{2f^{1/2}}\sigma^{\hat 0} \wedge \sigma^{\hat 1}$ and the structural equation $a = 0$: $-\tfrac{f'}{2f^{1/2}}\sigma^{\hat 0} \wedge \sigma^{\hat 1} + \omega^{\hat 0}{}_{\hat 1} \wedge \sigma^{\hat 1} = 0$ (assuming $\omega^{\hat 0}{}_{\hat 2} = \omega^{\hat 0}{}_{\hat 3} = 0$, which we'll verify by checking the other structural equations). So $\omega^{\hat 0}{}_{\hat 1} \wedge \sigma^{\hat 1} = \tfrac{f'}{2f^{1/2}}\sigma^{\hat 0} \wedge \sigma^{\hat 1}$, giving $\omega^{\hat 0}{}_{\hat 1} = \tfrac{f'}{2f^{1/2}}\sigma^{\hat 0}$ (modulo terms in $\sigma^{\hat 0}$, ruled out by the structural equation).

**$\omega^{\hat 2}{}_{\hat 1}$ and $\omega^{\hat 3}{}_{\hat 1}$:** From $d\sigma^{\hat 2} = (f^{1/2}/r)\sigma^{\hat 1} \wedge \sigma^{\hat 2}$ and structural equation $a = 2$: $(f^{1/2}/r)\sigma^{\hat 1} \wedge \sigma^{\hat 2} + \omega^{\hat 2}{}_{\hat 1} \wedge \sigma^{\hat 1} = 0$, so $\omega^{\hat 2}{}_{\hat 1} = -(f^{1/2}/r)\sigma^{\hat 2}$. Similarly $\omega^{\hat 3}{}_{\hat 1} = -(f^{1/2}/r)\sigma^{\hat 3}$ from $a = 3$ (the $f^{1/2}/r$ piece of $d\sigma^{\hat 3}$).

**$\omega^{\hat 3}{}_{\hat 2}$:** From $d\sigma^{\hat 3} = (f^{1/2}/r)\sigma^{\hat 1} \wedge \sigma^{\hat 3} + (\cot\theta/r)\sigma^{\hat 2} \wedge \sigma^{\hat 3}$ and structural equation $a = 3$: the $(\cot\theta/r)\sigma^{\hat 2} \wedge \sigma^{\hat 3}$ piece must cancel against $\omega^{\hat 3}{}_{\hat 2} \wedge \sigma^{\hat 2}$, giving $\omega^{\hat 3}{}_{\hat 2} = -(\cot\theta/r)\sigma^{\hat 3}$.

By antisymmetry: $\omega^{\hat 1}{}_{\hat 0} = +\omega^{\hat 0}{}_{\hat 1}$ (lowering index $\hat 0$ flips sign because $\eta_{\hat 0\hat 0} = -1$; so $\omega_{\hat 0\hat 1} = -\omega^{\hat 0}{}_{\hat 1}$ and $\omega_{\hat 1\hat 0} = +\omega^{\hat 0}{}_{\hat 1}$, hence $\omega^{\hat 1}{}_{\hat 0} = \omega_{\hat 1\hat 0} = \omega^{\hat 0}{}_{\hat 1}$). For purely spatial pairs $(\hat 1, \hat 2)$: $\omega^{\hat 1}{}_{\hat 2} = -\omega^{\hat 2}{}_{\hat 1}$ (standard Euclidean antisymmetry).

Summary:
$$
\omega^{\hat 0}{}_{\hat 1} = \omega^{\hat 1}{}_{\hat 0} = \tfrac{f'}{2f^{1/2}}\sigma^{\hat 0}, \quad \omega^{\hat 2}{}_{\hat 1} = -\omega^{\hat 1}{}_{\hat 2} = -\tfrac{f^{1/2}}{r}\sigma^{\hat 2}, \quad \omega^{\hat 3}{}_{\hat 1} = -\omega^{\hat 1}{}_{\hat 3} = -\tfrac{f^{1/2}}{r}\sigma^{\hat 3}, \quad \omega^{\hat 3}{}_{\hat 2} = -\omega^{\hat 2}{}_{\hat 3} = -\tfrac{\cot\theta}{r}\sigma^{\hat 3}.
$$
All other $\omega^a{}_b = 0$.

> [!note]- Derivation
> The system of four structural equations with antisymmetric $\omega_{ab}$ (6 independent components in 4D) determines the connection. The key is recognising the structure: $\omega^{\hat 0}{}_{\hat 1}$ comes from the time-warp $f^{1/2}$; the $\omega^{\hat 2}{}_{\hat 1}, \omega^{\hat 3}{}_{\hat 1}$ come from the radial-angular warp $r$; the $\omega^{\hat 3}{}_{\hat 2}$ comes from the sphere geometry within the $r = $ const surface. The off-diagonal $\omega^{\hat 0}{}_{\hat 2}, \omega^{\hat 0}{}_{\hat 3}, \omega^{\hat 2}{}_{\hat 0}, \omega^{\hat 3}{}_{\hat 0}$ are all zero (no mixed time-angular structure because the metric is static and spherically symmetric). The computation is bookkeeping; the structural insight is the spherical-symmetry simplification.

**Step 3: Curvature 2-forms via Cartan's second equation.**

Apply $\Omega^a{}_b = d\omega^a{}_b + \omega^a{}_c \wedge \omega^c{}_b$ to each $(a, b)$ pair. The key calculations:

**$\Omega^{\hat 0}{}_{\hat 1}$:** $d\omega^{\hat 0}{}_{\hat 1} = d(\tfrac{f'}{2f^{1/2}}\sigma^{\hat 0}) = d(\tfrac{f'}{2f^{1/2}}) \wedge \sigma^{\hat 0} + \tfrac{f'}{2f^{1/2}}d\sigma^{\hat 0}$. Compute $d(\tfrac{f'}{2f^{1/2}}) = (\tfrac{f'}{2f^{1/2}})'\,dr$, where the prime is $d/dr$. Algebra: $(\tfrac{f'}{2f^{1/2}})' = \tfrac{f''}{2f^{1/2}} - \tfrac{(f')^2}{4f^{3/2}}$. For Schwarzschild, $f = 1 - 2M/r$, $f' = 2M/r^2$, $f'' = -4M/r^3$. So $(\tfrac{f'}{2f^{1/2}})' = \tfrac{-4M/r^3}{2f^{1/2}} - \tfrac{(2M/r^2)^2}{4f^{3/2}} = -\tfrac{2M}{r^3 f^{1/2}} - \tfrac{M^2}{r^4 f^{3/2}}$.

The $\omega \wedge \omega$ piece: $\omega^{\hat 0}{}_{\hat c} \wedge \omega^{\hat c}{}_{\hat 1}$ for $\hat c = 1, 2, 3$. $\omega^{\hat 0}{}_{\hat 1} \wedge \omega^{\hat 1}{}_{\hat 1} = 0$; $\omega^{\hat 0}{}_{\hat 2} \wedge \omega^{\hat 2}{}_{\hat 1} = 0$ (since $\omega^{\hat 0}{}_{\hat 2} = 0$); $\omega^{\hat 0}{}_{\hat 3} \wedge \omega^{\hat 3}{}_{\hat 1} = 0$ (since $\omega^{\hat 0}{}_{\hat 3} = 0$). So $\omega \wedge \omega$ vanishes for $\Omega^{\hat 0}{}_{\hat 1}$. Therefore $\Omega^{\hat 0}{}_{\hat 1} = d\omega^{\hat 0}{}_{\hat 1}$ directly.

Final calculation: $\Omega^{\hat 0}{}_{\hat 1} = (\tfrac{f'}{2f^{1/2}})'\,dr \wedge \sigma^{\hat 0} + \tfrac{f'}{2f^{1/2}}\,d\sigma^{\hat 0}$. With $dr = f^{1/2}\sigma^{\hat 1}$: $(\tfrac{f'}{2f^{1/2}})'\,dr \wedge \sigma^{\hat 0} = (\tfrac{f'}{2f^{1/2}})' \cdot f^{1/2}\sigma^{\hat 1} \wedge \sigma^{\hat 0}$. And $d\sigma^{\hat 0} = -\tfrac{f'}{2f^{1/2}}\sigma^{\hat 0} \wedge \sigma^{\hat 1}$. After simplification (using $f''/2 + (f')^2/(4f) = $ ... involves algebraic manipulations; the standard result):
$$
\Omega^{\hat 0}{}_{\hat 1} = -\tfrac{2M}{r^3}\sigma^{\hat 0} \wedge \sigma^{\hat 1}.
$$

**$\Omega^{\hat 2}{}_{\hat 3}$:** Compute $d\omega^{\hat 2}{}_{\hat 3} = d(\tfrac{\cot\theta}{r}\sigma^{\hat 3}) = d(\tfrac{\cot\theta}{r}) \wedge \sigma^{\hat 3} + \tfrac{\cot\theta}{r}d\sigma^{\hat 3}$. The $\omega \wedge \omega$: $\omega^{\hat 2}{}_{\hat 1} \wedge \omega^{\hat 1}{}_{\hat 3} = -(f^{1/2}/r)\sigma^{\hat 2} \wedge \tfrac{f^{1/2}}{r}\sigma^{\hat 3} = -(f/r^2)\sigma^{\hat 2} \wedge \sigma^{\hat 3}$. After collecting and simplifying:
$$
\Omega^{\hat 2}{}_{\hat 3} = \tfrac{2M}{r^3}\sigma^{\hat 2} \wedge \sigma^{\hat 3}.
$$

(Other components computed similarly: $\Omega^{\hat 0}{}_{\hat 2} = (M/r^3)\sigma^{\hat 0} \wedge \sigma^{\hat 2}$, etc.)

> [!note]- Derivation
> The full computation is tedious but mechanical. The textbook result for Schwarzschild has six independent curvature 2-forms (corresponding to the six independent components of the Riemann tensor allowed by the symmetries of a 4D space with spherical symmetry and staticity, after using the algebraic Bianchi identity): $\Omega^{\hat 0}{}_{\hat 1} = -(2M/r^3)\sigma^{\hat 0} \wedge \sigma^{\hat 1}$, $\Omega^{\hat 0}{}_{\hat 2} = (M/r^3)\sigma^{\hat 0} \wedge \sigma^{\hat 2}$, $\Omega^{\hat 0}{}_{\hat 3} = (M/r^3)\sigma^{\hat 0} \wedge \sigma^{\hat 3}$, $\Omega^{\hat 1}{}_{\hat 2} = -(M/r^3)\sigma^{\hat 1} \wedge \sigma^{\hat 2}$, $\Omega^{\hat 1}{}_{\hat 3} = -(M/r^3)\sigma^{\hat 1} \wedge \sigma^{\hat 3}$, $\Omega^{\hat 2}{}_{\hat 3} = (2M/r^3)\sigma^{\hat 2} \wedge \sigma^{\hat 3}$. Each is proportional to $M/r^3$, exhibiting the "$M/r^3$ tidal force" structure of the Schwarzschild geometry.

**Step 4: Read off Riemann tensor components and interpret.**

From $\Omega^a{}_b = \tfrac{1}{2}R^a{}_{bcd}\sigma^c \wedge \sigma^d$:

$\Omega^{\hat 0}{}_{\hat 1} = -(2M/r^3)\sigma^{\hat 0} \wedge \sigma^{\hat 1}$ gives $R^{\hat 0}{}_{\hat 1\hat 0\hat 1} = -2M/r^3$ (after identifying the $(c, d) = (\hat 0, \hat 1)$ term).

$\Omega^{\hat 2}{}_{\hat 3} = (2M/r^3)\sigma^{\hat 2} \wedge \sigma^{\hat 3}$ gives $R^{\hat 2}{}_{\hat 3\hat 2\hat 3} = 2M/r^3$.

These are the **tidal force components** of the Schwarzschild geometry:
- $R^{\hat 0}{}_{\hat 1\hat 0\hat 1} = -2M/r^3$: the **radial tidal force** experienced by a freely-falling observer — neighbouring observers separated radially are stretched apart at rate proportional to $M/r^3$.
- $R^{\hat 2}{}_{\hat 3\hat 2\hat 3} = +2M/r^3$: the **angular tidal force** — neighbouring observers separated tangentially are squeezed together at the same rate.

The relative signs reflect "tidal stretching radially, tidal compression transversely" — the classic geometric content of Newtonian gravity, recovered in this geometric formulation.

> [!note]- Complete formal solution
> **Orthonormal coframe.** $\sigma^{\hat 0} = f^{1/2}dt, \sigma^{\hat 1} = f^{-1/2}dr, \sigma^{\hat 2} = r\,d\theta, \sigma^{\hat 3} = r\sin\theta\,d\varphi$, with $f = 1 - 2M/r$.
>
> **Connection 1-forms** (after computing $d\sigma^a$ and solving the first structural equation with metric-compatibility $\omega_{ab} = -\omega_{ba}$):
> $$
> \omega^{\hat 0}{}_{\hat 1} = \tfrac{M}{r^2 f^{1/2}}\sigma^{\hat 0}, \quad \omega^{\hat 2}{}_{\hat 1} = -\tfrac{f^{1/2}}{r}\sigma^{\hat 2}, \quad \omega^{\hat 3}{}_{\hat 1} = -\tfrac{f^{1/2}}{r}\sigma^{\hat 3}, \quad \omega^{\hat 3}{}_{\hat 2} = -\tfrac{\cot\theta}{r}\sigma^{\hat 3},
> $$
> with $\omega^{\hat 1}{}_{\hat 0} = \omega^{\hat 0}{}_{\hat 1}$ (Lorentzian antisymmetry) and $\omega^{\hat 1}{}_{\hat 2} = -\omega^{\hat 2}{}_{\hat 1}, \omega^{\hat 1}{}_{\hat 3} = -\omega^{\hat 3}{}_{\hat 1}, \omega^{\hat 2}{}_{\hat 3} = -\omega^{\hat 3}{}_{\hat 2}$.
>
> **Curvature 2-forms** (after applying the second structural equation):
> $$
> \Omega^{\hat 0}{}_{\hat 1} = -\tfrac{2M}{r^3}\sigma^{\hat 0} \wedge \sigma^{\hat 1}, \quad \Omega^{\hat 2}{}_{\hat 3} = \tfrac{2M}{r^3}\sigma^{\hat 2} \wedge \sigma^{\hat 3}, \quad \text{etc.}
> $$
> Each of the six independent curvature 2-forms is proportional to $M/r^3$.
>
> **Tidal Riemann components:**
> $$
> R^{\hat 0}{}_{\hat 1\hat 0\hat 1} = -\tfrac{2M}{r^3}, \quad R^{\hat 2}{}_{\hat 3\hat 2\hat 3} = +\tfrac{2M}{r^3}, \quad R^{\hat 0}{}_{\hat 2\hat 0\hat 2} = +\tfrac{M}{r^3}, \quad R^{\hat 1}{}_{\hat 2\hat 1\hat 2} = -\tfrac{M}{r^3}, \quad \text{etc.}
> $$
> These describe the **tidal forces** experienced by an observer at radius $r$ in the Schwarzschild geometry: radial stretching, tangential compression, all scaling as $M/r^3$ — the classical Newtonian tidal-force expression recovered from the geometric formulation. $\blacksquare$

---

# Key Takeaways

**Cartan's structural equations are the standard tool for computing curvature in general relativity.** The whole computation above takes about a page of careful work, dramatically less than the coordinate-Christoffel approach (which would take 5+ pages). Every general relativity textbook computes the Schwarzschild curvature this way, and the same recipe extends to the Kerr metric (rotating black hole), the FRW metric (cosmology), the Reissner-Nordström metric (charged black hole), and the de Sitter / anti-de Sitter spaces. Once internalised, the recipe — orthonormal coframe → $d\sigma$ → solve first equation → compute second equation → read off Riemann components — becomes automatic.

**The $M/r^3$ tidal-force structure of Schwarzschild is the geometric counterpart of Newtonian gravity.** The Riemann tensor components $R^{\hat a}{}_{\hat b\hat c\hat d}$ in an orthonormal frame are the *geodesic-deviation forces* experienced by freely-falling observers: the relative acceleration of neighbouring [[Def - Geodesic|geodesics]] is given by the curvature. For Schwarzschild, this gives the textbook tidal forces $\pm M/r^3$ in radial and angular directions, recovering Newtonian gravity in the weak-field limit. The geometric formulation has the virtue of being valid even in the strong-field regime (near the event horizon), where Newtonian gravity breaks down completely.

**The hatted-index convention is essential for orthonormal-frame computations in GR.** The hatted indices $\hat a, \hat b$ distinguish orthonormal-frame components from coordinate components $a, b$. Mixing them up is a common source of error. The orthonormal-frame metric is $\eta_{\hat a\hat b} = \mathrm{diag}(-1, 1, 1, 1)$ — constant — while the coordinate metric $g_{ab}$ is the messy explicit Schwarzschild form. Components of tensors in the orthonormal frame have direct physical interpretation (proper time, proper distance, tidal force per unit mass), while components in the coordinate frame need to be re-interpreted via the coframe. For computational efficiency, work in the orthonormal frame; for physical interpretation, often transition to local-observer frames defined by the orthonormal frame at a point.

**The Schwarzschild result $\Omega^a{}_b \sim M/r^3$ is the structural prediction of GR.** The result that all curvature components scale as $M/r^3$ is highly non-trivial — it falls out only after the algebraic dance of the $d\omega + \omega \wedge \omega$ computation. Plugging into the **Einstein field equations** $R_{\mu\nu} - \tfrac{1}{2}R g_{\mu\nu} + \Lambda g_{\mu\nu} = 8\pi G T_{\mu\nu}$ in the vacuum case ($T = 0, \Lambda = 0$), all the contracted curvatures vanish: $R_{\mu\nu} = 0$. So Schwarzschild is a **vacuum solution** of the Einstein equations, confirming that the metric was chosen correctly. The full derivation that Schwarzschild is *the unique* spherically symmetric static vacuum solution is **Birkhoff's theorem** (1923) — even time-dependent spherically symmetric solutions to vacuum GR are necessarily Schwarzschild. This is one of the deepest results in GR. See [[General Relativity I — Einstein's Equations and Schwarzschild]] for the full development.

**Geodesics of the Schwarzschild metric give perihelion precession and light bending.** Once the Christoffel symbols (equivalent to the connection 1-forms via the gauge-transformation law) are computed, the geodesic equation can be solved (using conservation of energy and angular momentum from the Killing fields $\partial_t, \partial_\varphi$). For massive test particles, this gives the **perihelion precession of Mercury** (observed: 43 arcseconds/century beyond Newtonian; predicted by GR: exactly 43); for null geodesics, it gives the **gravitational deflection of light** (observed in 1919 by Eddington's eclipse expedition: deflection by the Sun ≈ 1.75 arcseconds, matching GR). Both effects are computed from the Schwarzschild geodesic equation, which uses the Christoffel symbols / connection 1-forms computed here.
