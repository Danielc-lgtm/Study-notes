---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Gauss-Bonnet for Closed Surfaces (Chern's Proof)"
  - "Def - Riemannian Metric"
  - "Def - Riemannian Volume Form"
tags: [geometry, gauge-theory, gauss-bonnet]
---

# Problem Statement

Verify the Gauss-Bonnet theorem for the 2-torus $T^2 = S^1 \times S^1$ in two ways:

**(a) The flat torus.** Equip $T^2$ with the flat metric inherited from $\mathbb{R}^2/(\mathbb{Z}^2)$. Compute the Gauss curvature $K$ directly, show $K \equiv 0$, and verify $\frac{1}{2\pi}\int_{T^2} K\,dA = 0 = \chi(T^2)$.

**(b) The donut torus in $\mathbb{R}^3$.** Embed $T^2 \subset \mathbb{R}^3$ as the donut surface
$$X(u, v) = ((R + r\cos v)\cos u, (R + r\cos v)\sin u, r\sin v),$$
with $0 < r < R$. Compute the Gauss curvature $K(u, v)$ from the first and second fundamental forms, integrate $\int_{T^2} K\,dA$, and verify it equals $0 = 2\pi\chi(T^2) = 0$. Exhibit both positive curvature regions (outer rim) and negative curvature regions (inner) where they cancel.

**Recall:**

For a Riemannian surface $(M^2, g)$, the **Gauss curvature** $K(p)$ at $p \in M$ is the unique scalar invariant of the metric at $p$ such that for an oriented orthonormal frame $(e_1, e_2)$ on a neighborhood of $p$, the curvature 2-form $\Omega \in \Omega^2(M; \mathfrak{so}(2))$ satisfies $\Omega^1{}_2 = -K\,\sigma^1\wedge\sigma^2$, where $\sigma^1, \sigma^2$ is the dual coframe.

For an embedded surface $M \subset \mathbb{R}^3$, $K = \det(\mathrm{II})/\det(\mathrm{I})$, where $\mathrm{I}$ is the first fundamental form (matrix $g_{ij} = X_i \cdot X_j$ in surface parameters) and $\mathrm{II}$ is the second fundamental form (matrix $h_{ij} = -X_i \cdot \hat n_j$, with $\hat n$ the outward unit normal).

![[Thm - Gauss-Bonnet for Closed Surfaces (Chern's Proof)#Statement]]

---

# Convergent Strategy

**Problem class:** A *verification* problem for Gauss-Bonnet on a specific manifold with $\chi = 0$. The topic-page strategy is to compute the curvature integral directly and verify equality with $\chi$.

**Assumption pattern:** Part (a) uses the *intrinsic flat metric*: the torus has a flat Riemannian structure (inherited from $\mathbb{R}^2$ by quotient), so $K \equiv 0$. Part (b) uses an *extrinsic embedded metric*: the donut in $\mathbb{R}^3$ has varying curvature, but the *integral* must still vanish, hence positive and negative contributions cancel.

**Theorem routing:** [[Thm - Gauss-Bonnet for Closed Surfaces (Chern's Proof)]] gives the prediction $\frac{1}{2\pi}\int K\,dA = \chi(T^2) = 0$ in both cases. The computation in each case verifies the integral directly.

**Key decision point:** Recognizing that the torus has $\chi = 0$ in the first place — this follows from the standard CW-decomposition (1 vertex, 2 edges, 1 face, giving $\chi = 1 - 2 + 1 = 0$). For the donut surface, the non-obvious step is computing the integral via explicit fundamental forms.

---

# Legal Operations Used

1. **Operation 7 from the topic page (Compute Kronecker indices of zeros).** $\chi(T^2) = 0$ can be verified independently: the standard vector field $\partial/\partial\theta_1$ on $T^2$ (the "horizontal" vector field of the product structure) is nowhere zero, giving $\sum j_v(p_\alpha) = 0 = \chi(T^2)$. This confirms our prediction.

2. **Operation 4 from the topic page (Use Pfaffian / invariant polynomial of curvature).** For the donut surface, compute $\mathrm{Pf}(\Omega) = K\,dA$ directly via the second fundamental form and integrate.

---

# Hints

> [!note]- Hint 1
> For (a), the flat metric on $T^2 = \mathbb{R}^2/\mathbb{Z}^2$ has Riemann curvature tensor identically zero (inherits from the flat metric on $\mathbb{R}^2$), so $K \equiv 0$.

> [!note]- Hint 2
> For (b), compute $g_{ij} = X_i \cdot X_j$ from $X(u, v) = ((R + r\cos v)\cos u, (R + r\cos v)\sin u, r\sin v)$. Result: $g_{uu} = (R + r\cos v)^2$, $g_{vv} = r^2$, $g_{uv} = 0$. So $dA = (R + r\cos v) \cdot r \, du\,dv$.

> [!note]- Hint 3
> For (b), the unit normal is $\hat n = (\cos u\cos v, \sin u\cos v, \sin v)$ (outward). Compute $h_{ij} = -X_i \cdot \hat n_j$, and $K = (h_{uu}h_{vv} - h_{uv}^2)/(g_{uu}g_{vv} - g_{uv}^2)$.

> [!note]- Hint 4
> For (b), the answer simplifies to $K = \cos v/(r(R + r\cos v))$. Integrate: $\int_0^{2\pi}\int_0^{2\pi} K \cdot (R + r\cos v)\cdot r\,du\,dv = \int_0^{2\pi}\int_0^{2\pi}\cos v\,du\,dv = 0$.

---

# Solution

The proof has two distinct computations corresponding to parts (a) and (b). Part (a) is essentially trivial — flat metric, zero curvature, zero integral. Part (b) requires the full machinery of fundamental forms for embedded surfaces and exhibits the cancellation of positive and negative curvature contributions that makes the integral vanish.

**Part (a): Flat torus.**

The flat torus $T^2 = \mathbb{R}^2/\mathbb{Z}^2$ inherits the Euclidean metric from $\mathbb{R}^2$.

> [!note]- Derivation
> The quotient map $\mathbb{R}^2 \to T^2$ is a local isometry (in fact, a local diffeomorphism), so the Riemannian curvature tensor of $T^2$ at every point equals that of $\mathbb{R}^2$ — which is zero everywhere. In particular, the Gauss curvature $K \equiv 0$.
>
> Therefore $\frac{1}{2\pi}\int_{T^2}K\,dA = 0$.
>
> Comparing with $\chi(T^2) = 0$ (the standard CW-decomposition with 1 vertex, 2 edges, 1 face gives $\chi = 0$, or equivalently the parallelizability of $T^2$ gives $\chi = 0$ via Poincaré-Hopf): $\frac{1}{2\pi}\int K\,dA = 0 = \chi(T^2)$. ✓

**Part (b): Donut surface in $\mathbb{R}^3$.**

Parameterize $T^2 \subset \mathbb{R}^3$ by $X : [0, 2\pi]^2 \to \mathbb{R}^3$ with $X(u, v) = ((R + r\cos v)\cos u, (R + r\cos v)\sin u, r\sin v)$.

> [!note]- Derivation: First fundamental form
> $X_u = \partial X/\partial u = (-(R+r\cos v)\sin u, (R+r\cos v)\cos u, 0)$. $X_v = \partial X/\partial v = (-r\sin v\cos u, -r\sin v\sin u, r\cos v)$. Then:
> - $g_{uu} = X_u \cdot X_u = (R + r\cos v)^2$;
> - $g_{vv} = X_v \cdot X_v = r^2\sin^2 v + r^2\cos^2 v = r^2$;
> - $g_{uv} = X_u \cdot X_v = 0$.
>
> So $dA = \sqrt{\det g}\,du\,dv = (R + r\cos v) \cdot r\,du\,dv$.

> [!note]- Derivation: Unit normal and second fundamental form
> $\hat n = X_u \times X_v / \|X_u \times X_v\|$. Cross product:
> $$X_u \times X_v = (R+r\cos v) \cdot r \cdot (\cos u\cos v, \sin u\cos v, \sin v),$$
> with magnitude $(R + r\cos v) \cdot r$. So $\hat n = (\cos u\cos v, \sin u\cos v, \sin v)$, the outward unit normal.
>
> $\hat n_u = (-\sin u\cos v, \cos u\cos v, 0)$, $\hat n_v = (-\cos u\sin v, -\sin u\sin v, \cos v)$. Then:
> - $h_{uu} = -X_u \cdot \hat n_u = -[-(R+r\cos v)\sin u \cdot (-\sin u\cos v) + (R+r\cos v)\cos u \cdot \cos u\cos v + 0] = -[(R+r\cos v)\sin^2 u\cos v + (R+r\cos v)\cos^2 u \cos v] = -(R + r\cos v)\cos v$;
> - $h_{vv} = -X_v \cdot \hat n_v = -[(-r\sin v\cos u)(-\cos u\sin v) + (-r\sin v\sin u)(-\sin u\sin v) + r\cos v \cdot \cos v] = -[r\sin^2 v\cos^2 u + r\sin^2 v\sin^2 u + r\cos^2 v] = -r[\sin^2 v + \cos^2 v] = -r$;
> - $h_{uv} = -X_u \cdot \hat n_v = -[(-(R+r\cos v)\sin u)(-\cos u\sin v) + (R+r\cos v)\cos u(-\sin u\sin v) + 0] = -(R+r\cos v)\sin v\cos u\sin u + (R+r\cos v)\sin v\cos u\sin u = 0$.

> [!note]- Derivation: Gauss curvature
> By the formula $K = \det\mathrm{II}/\det\mathrm{I}$ for embedded surfaces:
> $$K = \frac{h_{uu}h_{vv} - h_{uv}^2}{g_{uu}g_{vv} - g_{uv}^2} = \frac{[-(R+r\cos v)\cos v] \cdot [-r] - 0^2}{(R+r\cos v)^2 \cdot r^2 - 0^2} = \frac{(R+r\cos v) \cdot r\cos v}{(R+r\cos v)^2 \cdot r^2} = \frac{\cos v}{r(R + r\cos v)}.$$

> [!note]- Derivation: Integration
> $$\int_{T^2}K\,dA = \int_0^{2\pi}\!\int_0^{2\pi} K \cdot (R + r\cos v)\cdot r\,du\,dv = \int_0^{2\pi}\!\int_0^{2\pi} \frac{\cos v}{r(R + r\cos v)} \cdot (R + r\cos v) \cdot r \, du\,dv = \int_0^{2\pi}\!\int_0^{2\pi}\cos v\,du\,dv.$$
> The $u$-integration gives $2\pi$; the $v$-integration $\int_0^{2\pi}\cos v\,dv = 0$.
>
> So $\int_{T^2}K\,dA = 2\pi \cdot 0 = 0$. ✓
>
> Therefore $\frac{1}{2\pi}\int_{T^2}K\,dA = 0 = \chi(T^2)$, matching the Gauss-Bonnet prediction.

> [!note]- Derivation: Cancellation of positive and negative curvature
> $K = \cos v/(r(R+r\cos v)) > 0$ when $\cos v > 0$ (i.e., $v \in (-\pi/2, \pi/2)$, the outer rim of the donut) and $K < 0$ when $\cos v < 0$ (i.e., $v \in (\pi/2, 3\pi/2)$, the inner rim). The integral cancels because $\int\cos v\,dv = 0$ over a full period — the positive contribution on the outer rim exactly cancels the negative contribution on the inner rim, and the area weighting $(R + r\cos v) \cdot r$ is exactly what gives this cancellation.

> [!note]- Complete formal solution
> **Part (a):** Flat torus inherits flat metric from $\mathbb{R}^2$; curvature tensor identically zero; hence $K \equiv 0$ and $\int K\,dA = 0$. $\chi(T^2) = 0$ by CW-decomposition or by parallelizability. Equality holds.
>
> **Part (b):** Compute first fundamental form $g_{uu} = (R+r\cos v)^2$, $g_{vv} = r^2$, $g_{uv} = 0$; unit normal $\hat n = (\cos u\cos v, \sin u\cos v, \sin v)$; second fundamental form $h_{uu} = -(R+r\cos v)\cos v$, $h_{vv} = -r$, $h_{uv} = 0$. Gauss curvature $K = \cos v/(r(R + r\cos v))$, varying in sign with $\cos v$. Area form $dA = (R+r\cos v)r\,du\,dv$. Integral: $\int K\,dA = \int\!\int\cos v\,du\,dv = 0$. Equality $\frac{1}{2\pi}\int K\,dA = 0 = \chi(T^2)$ holds. ∎

> [!warning] Sanity-check via independent route
> Since $T^2$ is parallelizable (admits a global frame: $\partial/\partial\theta_1, \partial/\partial\theta_2$), the tangent bundle is trivial, so its Euler class is zero, so $\chi(T^2) = 0$. This confirms $\frac{1}{2\pi}\int K\,dA = 0$ on the donut without doing any calculus — purely from the parallelizability of the abstract torus.

---

# Key Takeaways

**Flat metric gives zero curvature integral automatically.** Any closed surface admitting a flat metric must have $\chi = 0$. By the uniformization theorem, the closed surfaces admitting flat metrics are exactly the torus (genus 1) and the Klein bottle (non-orientable). The trigger-reaction pattern: "is this surface flat-metrizable?" → "compute $\chi$; if nonzero, no." This is a global topological obstruction to flat-metrizability, a major application of Gauss-Bonnet.

**Curvature cancellation on the donut is structural.** The positive curvature on the outer rim and negative curvature on the inner rim of the donut exactly cancel because $T^2$ has $\chi = 0$ — there is no "net curvature" to be carried by the embedded geometry. The same cancellation holds for any embedded torus in $\mathbb{R}^3$: the integral always vanishes, regardless of the size parameters $R, r$. More generally, *any* metric on $T^2$ (not just embedded ones) has $\int K\,dA = 0$ — this is the topological content of Gauss-Bonnet. This is the geometric meaning of "$\chi$ is a topological invariant" in the present setting.

**Verification via parallelizability bypasses the integral computation.** $T^n$ is parallelizable for all $n$ (admits a global frame from the product structure), so the tangent bundle is trivial, so the Euler class vanishes, so $\chi(T^n) = 0$ — no curvature integral needed. The trigger: "is this manifold a product of circles (or, more generally, a parallelizable manifold)?" → "$\chi = 0$ automatically." Parallelizable manifolds with $\chi \neq 0$ don't exist (this is a consequence of Gauss-Bonnet-Chern).

This exercise parallels the higher-dimensional cases addressed by [[Thm - Gauss-Bonnet-Chern Theorem]] and the line-bundle quantization analogue in [[Thm - First Chern Class of the Hopf Bundle is One]]. The general pattern — topological invariants computable as curvature integrals — is what makes characteristic classes so powerful.
