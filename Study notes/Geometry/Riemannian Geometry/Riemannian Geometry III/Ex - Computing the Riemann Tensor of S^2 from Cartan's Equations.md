---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Riemann Curvature Tensor"
  - "Def - Sectional Curvature"
  - "Def - Levi-Civita Connection"
tags: [geometry, riemannian-geometry, curvature, sphere]
---

# Problem Statement

Equip the $2$-sphere $S^2$ with the standard round metric $g = d\theta^2 + \sin^2\theta\, d\varphi^2$ in spherical coordinates $(\theta, \varphi)$ with $\theta \in (0, \pi)$ and $\varphi \in [0, 2\pi)$. Using Cartan's structural equations in an orthonormal coframe, compute:

(a) the orthonormal coframe and its exterior differentials;
(b) the connection 1-form $\omega^1_{\;2}$;
(c) the curvature 2-form $\Omega^1_{\;2}$;
(d) the Gauss curvature $K$, and verify $K = 1$ pointwise.

**Recall:**

In an orthonormal coframe $(\sigma^a)$ for a Riemannian manifold, Cartan's structural equations read:
- First structural equation: $d\sigma^a + \omega^a_{\;b}\wedge\sigma^b = 0$ (assuming torsion-free [[Def - Levi-Civita Connection|Levi-Civita]] connection).
- Second structural equation: $\Omega^a_{\;b} = d\omega^a_{\;b} + \omega^a_{\;c}\wedge\omega^c_{\;b} = \tfrac{1}{2}R^a_{\;bcd}\sigma^c\wedge\sigma^d$.

The skew-symmetry of $\omega$ ($\omega^a_{\;b} = -g_{ac}g^{bd}\omega^c_{\;d}$) reduces to $\omega^1_{\;2} = -\omega^2_{\;1}$ in dim $2$.

The [[Def - Sectional Curvature|Gauss curvature]] of a $2$-D Riemannian manifold satisfies $d\omega^1_{\;2} = K\sigma^1\wedge\sigma^2$.

---

# Convergent Strategy

**Problem class:** Curvature computation via Cartan's method on a specific Riemannian manifold ($S^2$). This is the prototypical example of the Cartan-method recipe in dim $2$ with a *non-conformally-flat* metric of the form $g = du^2 + G(u)^2 dv^2$.

**Assumption pattern:** The round metric on $S^2$ has the form $g = d\theta^2 + \sin^2\theta\, d\varphi^2$, which is of the type $g = du^2 + G(u, v)^2 dv^2$ with $G(\theta, \varphi) = \sin\theta$. Frankel §9.5c derived the general formula $K = -G_{uu}/G$ for such metrics; with $G = \sin\theta$, $G_{uu} = -\sin\theta$, so $K = -(-\sin\theta)/\sin\theta = 1$. We will derive this explicitly via Cartan, with the structural equations applied step by step.

**Theorem routing:** (a) First structural equation $d\sigma^a + \omega^a_{\;b}\wedge\sigma^b = 0$ + skew-symmetry $\omega^1_{\;2} = -\omega^2_{\;1}$ uniquely determines $\omega^1_{\;2}$. (b) Second structural equation $\Omega^1_{\;2} = d\omega^1_{\;2}$ (the wedge term vanishes in dim $2$). (c) $K = R^1_{\;212}$ in the orthonormal frame.

**Key decision point:** The choice of orthonormal coframe. The coordinate $1$-forms $d\theta, d\varphi$ are *not* orthonormal — $|d\varphi|^2 = g^{\varphi\varphi} = 1/\sin^2\theta$, so $d\varphi$ has length $1/\sin\theta$. The orthonormal coframe is $\sigma^1 = d\theta$, $\sigma^2 = \sin\theta\, d\varphi$. The non-obvious move is recognising that $d\sigma^2 = \cos\theta\, d\theta\wedge d\varphi$ has a $\cos\theta$ factor that propagates into the connection 1-form $\omega^1_{\;2}$.

---

# Legal Operations Used

1. **Operation 3 from the topic page (Cartan's structural equations).** The whole calculation is an instance of this operation, performed mechanically.

2. **Operation 4 from the topic page (descend from $R$ to $K$).** In dim $2$, $K = R^1_{\;212}$ in an orthonormal frame.

---

# Hints

> [!note]- Hint 1
> Set up the orthonormal coframe. Since $g = d\theta^2 + \sin^2\theta\, d\varphi^2$, the orthonormal coframe is $\sigma^1 = d\theta$ and $\sigma^2 = \sin\theta\, d\varphi$. Check: $\sigma^1\otimes\sigma^1 + \sigma^2\otimes\sigma^2 = d\theta\otimes d\theta + \sin^2\theta\, d\varphi\otimes d\varphi = g$. ✓

> [!note]- Hint 2
> Compute exterior derivatives: $d\sigma^1 = d(d\theta) = 0$. $d\sigma^2 = d(\sin\theta\, d\varphi) = \cos\theta\, d\theta\wedge d\varphi = \cos\theta\cdot\sigma^1\wedge(d\varphi)$. To express in terms of $\sigma^1, \sigma^2$: $d\varphi = \sigma^2/\sin\theta$, so $d\sigma^2 = (\cos\theta/\sin\theta)\sigma^1\wedge\sigma^2 = \cot\theta\,\sigma^1\wedge\sigma^2$.

> [!note]- Hint 3
> First structural equation:
> - $a = 1$: $d\sigma^1 + \omega^1_{\;2}\wedge\sigma^2 = 0$, so $\omega^1_{\;2}\wedge\sigma^2 = 0$, i.e., $\omega^1_{\;2}$ is a multiple of $\sigma^2$.
> - $a = 2$: $d\sigma^2 + \omega^2_{\;1}\wedge\sigma^1 = 0$, i.e., $\cot\theta\,\sigma^1\wedge\sigma^2 = -(-\omega^1_{\;2})\wedge\sigma^1 = \omega^1_{\;2}\wedge\sigma^1$.
> 
> Writing $\omega^1_{\;2} = f\sigma^2$ from the first equation, the second gives $\cot\theta\,\sigma^1\wedge\sigma^2 = f\sigma^2\wedge\sigma^1 = -f\sigma^1\wedge\sigma^2$, so $f = -\cot\theta$ and $\omega^1_{\;2} = -\cot\theta\,\sigma^2 = -\cos\theta\, d\varphi$.

> [!note]- Hint 4
> Compute the curvature 2-form: $\Omega^1_{\;2} = d\omega^1_{\;2}$ (no wedge term in dim 2). $d(-\cos\theta\, d\varphi) = \sin\theta\, d\theta\wedge d\varphi = \sigma^1\wedge(\sin\theta\, d\varphi) = \sigma^1\wedge\sigma^2$. So $\Omega^1_{\;2} = \sigma^1\wedge\sigma^2$.

> [!note]- Hint 5
> Read off the curvature: $\Omega^1_{\;2} = R^1_{\;212}\sigma^1\wedge\sigma^2 = \sigma^1\wedge\sigma^2$, so $R^1_{\;212} = 1$. In dim $2$, $K = R^1_{\;212} = 1$.

---

# Solution

The calculation has four steps. **Step 1** sets up the orthonormal coframe and computes $d\sigma^a$. **Step 2** solves the first structural equation for $\omega^1_{\;2}$. **Step 3** computes the curvature 2-form $\Omega^1_{\;2}$. **Step 4** reads off the Riemann tensor components and the Gauss curvature.

**Step 1: Orthonormal coframe and its differentials.**

> [!note]- Derivation
> The round metric is $g = d\theta^2 + \sin^2\theta\, d\varphi^2$. An orthonormal coframe:
> $$\sigma^1 = d\theta, \qquad \sigma^2 = \sin\theta\, d\varphi.$$
> Verification: $\sum_a \sigma^a \otimes \sigma^a = d\theta^2 + \sin^2\theta\, d\varphi^2 = g$. ✓
>
> Exterior derivatives:
> - $d\sigma^1 = d(d\theta) = 0$.
> - $d\sigma^2 = d(\sin\theta\, d\varphi) = \cos\theta\, d\theta \wedge d\varphi$. To express in $\sigma^a$: $d\theta = \sigma^1$ and $d\varphi = \sigma^2/\sin\theta$, so $d\sigma^2 = \cos\theta \cdot \sigma^1 \wedge (\sigma^2/\sin\theta) = \cot\theta\,\sigma^1 \wedge \sigma^2$.

**Step 2: Connection 1-form $\omega^1_{\;2}$ from the first structural equation.**

> [!note]- Derivation
> In dim $2$, the only independent connection 1-form is $\omega^1_{\;2}$, with $\omega^2_{\;1} = -\omega^1_{\;2}$ (skew-symmetry) and $\omega^1_{\;1} = \omega^2_{\;2} = 0$.
>
> First structural equation $d\sigma^a + \omega^a_{\;b}\wedge\sigma^b = 0$:
> - $a = 1$: $0 + \omega^1_{\;2} \wedge \sigma^2 = 0 \implies \omega^1_{\;2}$ is a multiple of $\sigma^2$.
> - $a = 2$: $\cot\theta\,\sigma^1\wedge\sigma^2 + \omega^2_{\;1}\wedge\sigma^1 = 0$, equivalently $\cot\theta\,\sigma^1\wedge\sigma^2 = -\omega^2_{\;1}\wedge\sigma^1 = \omega^1_{\;2}\wedge\sigma^1$.
>
> Write $\omega^1_{\;2} = f(\theta, \varphi)\sigma^2$ (from $a = 1$). Substitute into $a = 2$: $\cot\theta\,\sigma^1\wedge\sigma^2 = f\sigma^2\wedge\sigma^1 = -f\sigma^1\wedge\sigma^2$, so $f = -\cot\theta$. Therefore
> $$\omega^1_{\;2} = -\cot\theta\,\sigma^2 = -\cot\theta\,(\sin\theta\, d\varphi) = -\cos\theta\, d\varphi.$$

**Step 3: Curvature 2-form $\Omega^1_{\;2}$ from the second structural equation.**

> [!note]- Derivation
> Second structural equation: $\Omega^1_{\;2} = d\omega^1_{\;2} + \omega^1_{\;c}\wedge\omega^c_{\;2}$. The wedge sum vanishes in dim $2$ since the only nonzero $\omega^1_{\;c}$ is $\omega^1_{\;2}$ (for $c = 2$) and $\omega^2_{\;2} = 0$: $\omega^1_{\;2}\wedge\omega^2_{\;2} = 0$. So $\Omega^1_{\;2} = d\omega^1_{\;2}$.
>
> Compute: $d(-\cos\theta\, d\varphi) = -d(\cos\theta)\wedge d\varphi - \cos\theta\, d(d\varphi) = \sin\theta\, d\theta\wedge d\varphi + 0 = \sin\theta\, d\theta\wedge d\varphi$. In $\sigma^a$ form: $\sin\theta\, d\theta\wedge d\varphi = \sigma^1\wedge(\sin\theta\, d\varphi) = \sigma^1\wedge\sigma^2$. So
> $$\Omega^1_{\;2} = \sigma^1\wedge\sigma^2.$$

**Step 4: Read off Riemann components and Gauss curvature.**

> [!note]- Derivation
> Expand $\Omega^1_{\;2} = \tfrac{1}{2}R^1_{\;2cd}\sigma^c\wedge\sigma^d$. By antisymmetry in $(c, d)$, this is $R^1_{\;212}\sigma^1\wedge\sigma^2$. Comparing: $R^1_{\;212} = 1$.
>
> The other component is $R^2_{\;112}$, found from $\Omega^2_{\;1} = -\Omega^1_{\;2} = -\sigma^1\wedge\sigma^2$, so $R^2_{\;112} = -1$. By the algebraic symmetries, this is the same information.
>
> In dim $2$, the Gauss curvature is $K = R^1_{\;212}$ in an orthonormal frame. Therefore $K \equiv 1$ on $S^2$. ∎

> [!note]- Complete formal solution
> Orthonormal coframe: $\sigma^1 = d\theta$, $\sigma^2 = \sin\theta\, d\varphi$. Differentials: $d\sigma^1 = 0$, $d\sigma^2 = \cot\theta\,\sigma^1\wedge\sigma^2$. First structural equation gives $\omega^1_{\;2} = -\cos\theta\, d\varphi$. Curvature 2-form: $\Omega^1_{\;2} = d\omega^1_{\;2} = \sin\theta\, d\theta\wedge d\varphi = \sigma^1\wedge\sigma^2$. Hence $R^1_{\;212} = 1$ and $K \equiv 1$ on $S^2$. The Riemann tensor takes the constant-sectional-curvature-$1$ form $R(X, Y)Z = \langle Y, Z\rangle X - \langle X, Z\rangle Y$.

> [!warning] Sanity check via independent route
> Compare to the Frankel general formula for metrics $g = du^2 + G(u, v)^2 dv^2$: $K = -G_{uu}/G$. Here $G = \sin\theta$, $G_{\theta\theta} = -\sin\theta$, so $K = -(-\sin\theta)/\sin\theta = 1$. ✓ Match.

---

# Key Takeaways

**Cartan's method in dim 2 has a fixed recipe.** For any $2$-D Riemannian metric, the orthonormal coframe → exterior derivatives → first structural equation → connection 1-form → second structural equation → Gauss curvature recipe is mechanical. The only creative move is the choice of orthonormal coframe, which is usually forced by the metric's structure. The advantage over Christoffel symbols: $4$ Christoffel symbols + $3$ Riemann components vs. $1$ connection 1-form + $1$ curvature 2-form. Recognise the trigger: any explicit metric in dim $2$, especially one of the form $g = du^2 + G^2 dv^2$ (which includes spheres, surfaces of revolution, and the hyperbolic plane in geodesic-polar coordinates).

**Surfaces of revolution have $K = -G_{uu}/G$.** The general formula derived in Frankel §9.5c for metrics $g = du^2 + G(u, v)^2 dv^2$ gives the Gauss curvature in one line, no Cartan calculation needed once you've internalised the general formula. For $S^2$: $G = \sin\theta$, $K = 1$. For $H^2$ in geodesic-polar coordinates: $G = \sinh r$, $K = -\cosh r/\sinh r$... wait, $G_{rr} = \sinh r$, so $K = -\sinh r/\sinh r = -1$. ✓ For the flat plane in polar coordinates: $G = r$, $K = 0$. ✓ For the cone with angle deficit $\alpha$: $G = r\sin\alpha$ + delta-function at apex. The formula is *the* one to remember for axisymmetric $2$-D metrics.

**The connection 1-form encodes the *holonomy* of parallel transport along loops.** $\omega^1_{\;2} = -\cos\theta\, d\varphi$ on $S^2$ tells you that parallel transport along a latitude circle of constant $\theta$ rotates the tangent space by an angle $-\cos\theta \cdot 2\pi$ — the holonomy of one trip around. Integrating $\omega^1_{\;2}$ along a closed curve and exponentiating gives the rotation matrix of parallel transport. This is the geometric content of $\omega^1_{\;2}$ as the "infinitesimal generator of parallel transport rotation."

**Comparison: the parallel calculation on $H^2$ (see [[Ex - Sectional Curvature of the Hyperbolic Plane is -1]]) gives $K = -1$ via the same structural equations, with sign-flipped intermediate quantities.** Studying both calculations in parallel reveals the structural symmetry between positive- and negative-curvature 2-D geometry.
