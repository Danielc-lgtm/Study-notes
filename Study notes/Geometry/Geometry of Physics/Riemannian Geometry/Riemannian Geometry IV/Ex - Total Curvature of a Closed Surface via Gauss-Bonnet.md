---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Thm - Gauss-Bonnet Theorem for Surfaces"
  - "Def - Gauss Curvature and Mean Curvature"
tags: [geometry, riemannian-geometry, surfaces, gauss-bonnet, topology, euler-characteristic]
---

# Problem Statement

Use the [[Thm - Gauss-Bonnet Theorem for Surfaces|Gauss–Bonnet theorem]] to compute the total Gauss curvature $\int_M K\, dA$ for each of the following closed oriented surfaces:

(a) The sphere $S^2$ ($g = 0$, $\chi = 2$).

(b) The torus $T^2$ ($g = 1$, $\chi = 0$).

(c) The genus-$2$ surface $\Sigma_2$ ("double torus", $g = 2$, $\chi = -2$).

(d) The general genus-$g$ surface $\Sigma_g$ ($\chi = 2 - 2g$).

Then explain why **no smooth deformation of any of these surfaces in $\mathbb{R}^3$ can change the answer**, even though $K$ itself changes pointwise under such deformation.

**Recall:**

![[Thm - Gauss-Bonnet Theorem for Surfaces#Statement]]

The **Euler characteristic** of a closed orientable surface of genus $g$ is $\chi = 2 - 2g$. Equivalently: $g = 0$ gives $\chi = 2$ (sphere); $g = 1$ gives $\chi = 0$ (torus); higher $g$ gives negative $\chi$.

---

# Convergent Strategy

**Problem class:** Topological computation of a global integral via Gauss–Bonnet. The integral $\int_M K\, dA$ is *intrinsic* to the surface (independent of embedding) and *topological* (depends only on $\chi$). For any specific surface, the computation is one line: $\int K\, dA = 2\pi\chi(M) = 2\pi(2 - 2g)$.

**Assumption pattern:** Each surface is closed and orientable (the formula applies). The Euler characteristic is determined by the topological type, which we know for each example ($g = 0, 1, 2, \ldots$). We do NOT need a specific Riemannian metric or embedding — the integral is the same for any metric or embedding compatible with the topological type.

**Theorem routing:** Apply $\int_M K\, dA = 2\pi\chi(M) = 2\pi(2 - 2g)$ for each of (a)–(d). For (e), the deformation invariance follows from $\chi$ being a *topological* invariant — smooth deformations of $M$ in $\mathbb{R}^3$ preserve the topological type, hence preserve $\chi$, hence preserve the integral.

**Key decision point:** Whether to verify the formula by an alternative method (direct integration on a specific metric / embedding) or just cite Gauss–Bonnet. For the sphere of radius $a$, direct computation gives $\int K\, dA = (1/a^2)\cdot 4\pi a^2 = 4\pi = 2\pi\cdot 2$, matching $2\pi\chi(S^2)$. For the torus, the verification requires integrating the non-constant Gauss curvature over the toroidal surface — a calculation that works out to zero precisely because $\chi(T^2) = 0$. The Gauss–Bonnet route gives the answers immediately without the integration; the direct verification reinforces that the integral really is $2\pi\chi$ for any chosen metric.

---

# Legal Operations Used

1. **Operation 6 from the topic page (apply Gauss–Bonnet for global integrals):** Direct application of $\int K\, dA = 2\pi\chi(M)$ for each closed oriented surface.

2. **Operation 7 from the topic page (apply Poincaré–Hopf):** Alternative verification — $\chi(M) = \sum_p\mathrm{Ind}_p(v)$ for any vector field with isolated zeros, giving another route to the same answer.

---

# Hints

> [!note]- Hint 1
> For a closed orientable surface of genus $g$, the Euler characteristic is $\chi(M) = 2 - 2g$. So $\int K\, dA = 2\pi(2 - 2g) = 4\pi(1 - g)$.

> [!note]- Hint 2
> For the **sphere** ($g = 0$), the integral is $4\pi$. Direct verification on the sphere of radius $a$ (with $K = 1/a^2$ constant): $\int K\, dA = K\cdot\mathrm{Area} = (1/a^2)\cdot 4\pi a^2 = 4\pi$. Matches.

> [!note]- Hint 3
> For the **torus** ($g = 1$), the integral is $0$. This is *not* obvious from inspection — the standard torus of revolution in $\mathbb{R}^3$ has $K > 0$ on the outer half and $K < 0$ on the inner half. The two contributions exactly cancel, by Gauss–Bonnet. (Direct verification by integrating the non-constant $K$ on a standard torus would be a substantial calculation; Gauss–Bonnet gives the answer immediately.)

---

# Solution

The solution applies Gauss–Bonnet directly to each case and then addresses the deformation invariance.

**Step 1: Apply Gauss–Bonnet to each surface.**

> [!note]- Derivation
> By Gauss–Bonnet, $\int_M K\, dA = 2\pi\chi(M) = 2\pi(2 - 2g)$ for any closed oriented surface of genus $g$.
>
> **(a) Sphere $S^2$ ($g = 0$, $\chi = 2$):**
> $$
> \int_{S^2} K\, dA = 2\pi\cdot 2 = 4\pi.
> $$
> Direct verification on the unit sphere: $K = 1$, area $= 4\pi$, integral $= 4\pi$. Matches.
>
> **(b) Torus $T^2$ ($g = 1$, $\chi = 0$):**
> $$
> \int_{T^2} K\, dA = 2\pi\cdot 0 = 0.
> $$
> Despite the Gauss curvature being nontrivial pointwise (positive on the outer half of the torus, negative on the inner half), the total cancels exactly.
>
> **(c) Genus-$2$ surface $\Sigma_2$ ($g = 2$, $\chi = -2$):**
> $$
> \int_{\Sigma_2} K\, dA = 2\pi\cdot(-2) = -4\pi.
> $$
> The integrated curvature is *negative*, meaning the integrated $K$ is on average negative — consistent with the genus-$2$ surface having more "saddle-like" regions than "convex" regions.
>
> **(d) Genus-$g$ surface $\Sigma_g$ ($\chi = 2 - 2g$):**
> $$
> \int_{\Sigma_g} K\, dA = 2\pi(2 - 2g) = 4\pi(1 - g).
> $$
> The integral is positive for $g = 0$, zero for $g = 1$, and negative for $g \geq 2$. The magnitude grows linearly with $g$.

**Step 2: Explain the deformation invariance.**

> [!note]- Derivation
> Consider a smooth one-parameter family of embeddings $\mathbf{x}_t : M \hookrightarrow \mathbb{R}^3$ for $t \in [0, 1]$, with $\mathbf{x}_0 = \mathbf{x}$ the original embedding. Each $\mathbf{x}_t$ gives an induced Riemannian metric $g_t$ on $M$ and an induced Gauss curvature $K_t$ — these vary continuously with $t$, and so does the integral $\int_M K_t\, dA_t$.
>
> But by Gauss–Bonnet, $\int_M K_t\, dA_t = 2\pi\chi(M)$ for each $t$. The right side depends only on $\chi(M)$, which is a *topological* invariant — it does not depend on the metric or the embedding. So the integral is *constant* in $t$: any smooth deformation of the embedding preserves the integral, even though $K_t$ changes pointwise.
>
> **Specific example:** Start with the standard torus of revolution in $\mathbb{R}^3$ (a doughnut). Deform it smoothly by stretching, squashing, or twisting (any [[Def - Homeomorphism|homeomorphism]] that remains an embedding) — the integral $\int K\, dA$ stays at $0$. Even pinching the torus into a "skinny" shape with more concentrated negative curvature on the inner side: the positive-$K$ regions adjust to compensate, and the total stays zero. This is one of the most striking topological-vs-geometric facts in classical surface theory.
>
> **Why the deformation invariance is forced:** The integral $\int K\, dA = 4\pi\deg(N)$ (via the change-of-area formula and the [[Def - Brouwer Degree of a Map|Brouwer degree]] of the Gauss map). The Brouwer degree is a [[Def - Homotopy|homotopy]] invariant of $N : M \to S^2$; any smooth deformation of the embedding $\mathbf{x}_t$ gives a smooth homotopy of the corresponding Gauss maps $N_t$, hence $\deg(N_t)$ is constant in $t$, hence the integral is constant in $t$.

> [!note]- Complete formal solution
> By the [[Thm - Gauss-Bonnet Theorem for Surfaces|Gauss–Bonnet theorem]], for any closed oriented Riemannian surface $M$,
> $$
> \int_M K\, dA = 2\pi\chi(M).
> $$
> The Euler characteristic of a closed orientable surface of genus $g$ is $\chi(M) = 2 - 2g$. Substituting:
>
> (a) Sphere ($g = 0$): $\int K\, dA = 4\pi$.
> (b) Torus ($g = 1$): $\int K\, dA = 0$.
> (c) Genus-$2$ surface ($g = 2$): $\int K\, dA = -4\pi$.
> (d) Genus-$g$ surface: $\int K\, dA = 4\pi(1 - g)$.
>
> **Deformation invariance.** For a smooth one-parameter family of embeddings $\mathbf{x}_t : M \hookrightarrow \mathbb{R}^3$, the induced Gauss curvatures $K_t$ and area forms $dA_t$ vary smoothly, but the integral $\int_M K_t\, dA_t = 2\pi\chi(M)$ is constant in $t$ because $\chi(M)$ is a topological invariant. Equivalently: the Brouwer degree $\deg(N_t)$ of the Gauss map is a homotopy invariant, and $\int K_t\, dA_t = 4\pi\deg(N_t)$. $\square$

> [!tip] Cross-check via Poincaré–Hopf
> For each surface, the Euler characteristic can be independently computed as the index sum of any tangent vector field. For the sphere: a Morse function (height) gives $1 + 1 = 2$ (south pole min + north pole max, each index $+1$). For the torus: a Morse function (height of standard donut) gives $1 - 1 - 1 + 1 = 0$ (1 min, 2 saddles, 1 max — saddles have index $-1$). For the genus-$g$ surface: Morse function gives $1 - 2g + 1 = 2 - 2g$ (1 min, $2g$ saddles arising from the $g$ handles, 1 max). All consistent with the Gauss–Bonnet computation.

---

# Key Takeaways

**Gauss–Bonnet locks the total curvature to the topology with no wiggle room.** No matter how you deform the metric (or the embedding, in the embedded case), the integral $\int K\, dA$ stays equal to $2\pi\chi(M)$. You can redistribute the curvature — concentrate it in small bumps, spread it uniformly, alternate signs — but the *total* is fixed. This is a rare and powerful kind of result in differential geometry: a *topological* quantity (the genus) controlling a *geometric* integral (the curvature integral) exactly, with no error term. Most local-to-global theorems in geometry have error terms or inequality formulations; Gauss–Bonnet is an exact equality.

**The sphere is the only closed orientable surface that can support a metric of everywhere positive Gauss curvature.** If $K > 0$ everywhere on a closed orientable $M$, then $\int K\, dA > 0$, so $\chi(M) > 0$, hence $g < 1$, hence $g = 0$ — $M$ is a sphere. This is a topological *obstruction* on positive curvature; the torus and higher-genus surfaces cannot have a Riemannian metric with everywhere positive $K$. **Trigger:** "is there a metric of positive curvature on this closed surface?" → "compute $\chi$; if $\chi \leq 0$, no."

**The genus-$g$ surface ($g \geq 1$) cannot have a metric of everywhere negative Gauss curvature only if you remove the sphere case.** Conversely, by Gauss–Bonnet, $K < 0$ everywhere $\Rightarrow$ $\int K\, dA < 0$ $\Rightarrow$ $\chi(M) < 0$ $\Rightarrow$ $g \geq 2$. So genus-$0$ (sphere) and genus-$1$ (torus) surfaces *cannot* have everywhere-negative-$K$ metrics — only the higher-genus surfaces. The torus admits flat metrics ($K = 0$) but not strictly negative ones. This is part of the **uniformisation theorem**'s content: every closed orientable surface admits a constant-curvature metric, of sign determined by $\chi$.

**The "torus has zero total curvature despite varying $K$" is the central calibration example for non-constant curvature on a closed surface.** A standard torus of revolution in $\mathbb{R}^3$ has $K > 0$ on the outer half (the "outer equator" is convex) and $K < 0$ on the inner half (the "inner equator" of the hole is a saddle). The cancellation between these is exact — *not* approximate, not "to leading order", but exact: $\int_{\text{outer}}K\, dA = -\int_{\text{inner}}K\, dA$. This is a direct consequence of Gauss–Bonnet's exact form. **Internalising this**: in any "is the integral of $K$ on this surface nonzero?" question, default to "compute $\chi$, multiply by $2\pi$".

**The genus-$g$ surface's total negative curvature scales linearly with genus.** $\int K\, dA = 4\pi(1 - g)$, so as $g \to \infty$, the total curvature $\to -\infty$ linearly. For a constant-curvature hyperbolic metric ($K = -1$), this means $\mathrm{Area}(M) = 4\pi(g - 1)$ — the area grows linearly with genus. This is one of the most explicit links between geometry (area) and topology (genus) in mathematics.

**Companion exercises:** Compare with [[Ex - Holonomy around a Spherical Cap is the Solid Angle]] (the local-to-global content of $K$ as parallel-transport holonomy) and [[Ex - Hairy Ball Theorem from Poincare-Hopf]] (the alternative Poincaré–Hopf route to $\chi$). The three together — curvature integral, parallel-transport holonomy, vector-field index sum — all compute $\chi(M)$ via different geometric mechanisms.
