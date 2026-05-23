---
type: exercise
subject: general-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Einstein Field Equations"
  - "Thm - Newtonian Limit of Einstein's Equations"
  - "Def - The Metric Tensor as Gravitational Potential"
tags: [physics, general-relativity, weak-field-limit, newtonian-gravity]
---

# Problem Statement

**Linearise the Einstein equations $G_{\mu\nu} = 8\pi G\, T_{\mu\nu}$ around Minkowski space: $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h_{\mu\nu}| \ll 1$ (weak field). Specialise to the case of slow matter ($|v| \ll c$, so $T_{00} \approx \rho c^2$ dominates), static metric ($\partial_t h_{\mu\nu} = 0$), and the gauge choice (Lorenz gauge): $\partial^\mu \bar h_{\mu\nu} = 0$ where $\bar h_{\mu\nu} = h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu} h$ is the trace-reversed perturbation.**

**Show that the $(0, 0)$ component of the linearised Einstein equation reduces to**
$$\nabla^2 \phi = 4\pi G \rho$$
**— Newton's Poisson equation — with the identification $h_{00} = -2\phi$ (in mostly-plus signature) or $h_{00} = 2\phi$ (in mostly-minus). Hence the coupling constant $8\pi G$ in the Einstein equations is exactly what produces the $4\pi G$ in Poisson's equation.**

**Recall:**

The Newtonian gravitational potential $\phi$ satisfies Poisson's equation $\nabla^2 \phi = 4\pi G \rho$, with mass density $\rho$. In GR, the metric perturbation $h_{\mu\nu}$ around Minkowski plays the role of the gravitational potential. The (linearised) Einstein equations in Lorenz gauge are $\Box \bar h_{\mu\nu} = -16\pi G\, T_{\mu\nu}$, with $\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu$ the d'Alembertian.

---

# Convergent Strategy

**Problem class:** This is a *limit-derivation* exercise — showing that GR reduces to Newton in the appropriate regime. The class is "post-Newtonian expansion at lowest order", and the technique generalises to higher orders giving the post-Newtonian corrections.

**Assumption pattern:** Three simultaneous limits: (i) weak field $|h| \ll 1$, (ii) slow motion $v \ll c$, (iii) static $\partial_t \to 0$. Plus a gauge choice (Lorenz gauge) to make the linearised field equations as simple as possible. The slow-motion limit means $T_{00} \approx \rho c^2 \approx \rho$ dominates (with $c = 1$), while $T_{0i}, T_{ij}$ are suppressed by powers of $v$.

**Theorem routing:** The route is (linearise $g$, $R_{\mu\nu}$, $G_{\mu\nu}$, $T_{\mu\nu}$) → (Lorenz gauge simplifies field equations to $\Box\bar h_{\mu\nu} = -16\pi G T_{\mu\nu}$) → (static $\Rightarrow$ $\Box \to -\nabla^2$) → (slow matter $\Rightarrow$ $T_{00} \approx \rho$, others negligible) → (the $(0,0)$ equation $\nabla^2 \bar h_{00} = -16\pi G\rho$, with $\bar h_{00} = h_{00} - \frac{1}{2}\eta_{00} h$, and $h_{00} = -2\phi$ identifying the Newtonian potential) → (Poisson equation $\nabla^2 \phi = 4\pi G\rho$).

**Key decision point:** The non-obvious step is the use of *Lorenz gauge*: it simplifies the linearised Einstein tensor from a complex combination of derivatives of $h$ to just $-\frac{1}{2}\Box \bar h_{\mu\nu}$, dramatically simplifying the field equations. Without Lorenz gauge, the linearised Einstein equation has many more terms and is hard to compare to Poisson's equation directly.

---

# Legal Operations Used

1. **Operation 1 from the topic page** (Lift Newtonian intuitions to GR): This is the inverse application — we *descend* from GR to Newton, showing the GR equations reduce to the Newtonian ones. The identification $h_{00} = -2\phi$ is the bridge.

2. **Operation 2 from the topic page** (Use the equivalence principle): The geodesic equation in the weak-field limit gives $\ddot x = -\nabla\phi$, identifying $\phi$ with the metric component $h_{00}/(-2)$ — this is the equivalence-principle reduction (free-fall worldlines $\Leftrightarrow$ Newtonian gravity).

---

# Hints

> [!note]- Hint 1 (linearised Einstein in Lorenz gauge)
> The linearised Einstein tensor is $G^{(1)}_{\mu\nu} = -\frac{1}{2}\Box \bar h_{\mu\nu}$ in Lorenz gauge, where $\bar h_{\mu\nu} = h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu} h$ is the trace-reversed perturbation and $h = \eta^{\mu\nu} h_{\mu\nu}$. So the linearised field equations are $\Box \bar h_{\mu\nu} = -16\pi G T_{\mu\nu}$.

> [!note]- Hint 2 (static limit)
> For static configurations, $\partial_t \bar h_{\mu\nu} = 0$, so $\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu = -\nabla^2$ (with $\nabla^2$ the spatial Laplacian; signature mostly-plus or mostly-minus changes the sign, but for static the operator $-\nabla^2$ is the correct simplification). So the equation becomes $-\nabla^2 \bar h_{\mu\nu} = -16\pi G T_{\mu\nu}$, equivalently $\nabla^2 \bar h_{\mu\nu} = 16\pi G T_{\mu\nu}$.

> [!note]- Hint 3 (slow-matter limit)
> For slow matter, $T_{\mu\nu}$ has its leading component at $T_{00} = \rho$ (rest-frame energy density). So the leading $(0,0)$ equation is $\nabla^2 \bar h_{00} = 16\pi G \rho$.

> [!note]- Hint 4 (identification with Newtonian potential)
> Now relate $\bar h_{00}$ to $h_{00}$ and $h_{00}$ to $\phi$. By definition, $\bar h_{\mu\nu} = h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu} h$, so $\bar h_{00} = h_{00} - \frac{1}{2}\eta_{00} h$. For slow matter, the dominant component of $h$ is $h_{00}$ itself (since $T_{ii}$ from slow matter is small), so $h \approx \eta^{00} h_{00}$.

> [!note]- Hint 5 (sign-tracking)
> Mostly-plus signature: $\eta_{00} = -1$, $h = \eta^{\mu\nu} h_{\mu\nu} \approx \eta^{00} h_{00} = -h_{00}$. So $\bar h_{00} = h_{00} - \frac{1}{2}(-1)(-h_{00}) = h_{00} - \frac{1}{2} h_{00} = \frac{1}{2} h_{00}$. Substituting into $\nabla^2 \bar h_{00} = 16\pi G\rho$: $\nabla^2(\frac{1}{2} h_{00}) = 16\pi G\rho$, hence $\nabla^2 h_{00} = 32\pi G\rho$. With $h_{00} = -2\phi$: $\nabla^2(-2\phi) = 32\pi G\rho$, so $\nabla^2 \phi = -16\pi G\rho$ — sign is wrong!

> [!note]- Hint 6 (sign sorted out)
> Let me redo more carefully. Take **mostly-minus** signature throughout (consistent with Frankel and the topic page). Then $\eta_{\mu\nu} = \mathrm{diag}(1, -1, -1, -1)$, $\eta_{00} = 1$. With $g_{00} = 1 + h_{00}$ and identifying $\phi$ as the *negative* of half the deviation (with $h_{00} = 2\phi$ — where now $\phi < 0$ near mass gives $h_{00} < 0$ giving $g_{00} < 1$, i.e., $g_{00}$ smaller than asymptotic value near gravitating source).

> [!note]- Hint 7 (clean derivation)
> Actually the cleanest derivation uses the trace-reversed Einstein equation $R_{\mu\nu} = 8\pi G(T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T)$. Compute $R_{00}$ in the linearised, static, weak-field limit and equate to $8\pi G(T_{00} - \frac{1}{2}\eta_{00} T)$. For dust at rest: $T_{00} = \rho$, $T = g^{\mu\nu} T_{\mu\nu} \approx \eta^{00} T_{00} = \pm \rho$ (depending on signature). The trace-reversed RHS comes out to $4\pi G \rho$ (with $T_{00} - \frac{1}{2}\eta_{00} T = \rho - \frac{1}{2}(1)\rho = \frac{1}{2}\rho$ in either signature when carefully done). The LHS is $R_{00} \approx \frac{1}{2}\nabla^2 h_{00}$ for static metric. So $\frac{1}{2}\nabla^2 h_{00} = 4\pi G\rho$, hence $\nabla^2 h_{00} = 8\pi G\rho$. With $h_{00} = 2\phi$ (Newtonian identification): $\nabla^2 \phi = 4\pi G\rho$. **Done.**

---

# Solution

The proof breaks into three steps. Step 1 linearises the Einstein equations in Lorenz gauge. Step 2 takes the static slow-matter limit, reducing the $(0,0)$ component to a Poisson-like equation for $h_{00}$. Step 3 identifies $h_{00}$ with the Newtonian potential via the equivalence principle and recovers Poisson's equation. The non-obvious move is in Step 2: the use of the *trace-reversed* form $R_{\mu\nu} = 8\pi G(T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T)$ rather than the original $G_{\mu\nu} = 8\pi G T_{\mu\nu}$, which makes the $(0,0)$ equation cleaner in the dust limit.

**Step 1: Linearise the Einstein equations.**

Set $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h| \ll 1$ (signature $+---$, $\eta_{00} = 1$). The linearised Ricci tensor is
$$R^{(1)}_{\mu\nu} = \frac{1}{2}(\partial^\rho\partial_\mu h_{\nu\rho} + \partial^\rho\partial_\nu h_{\mu\rho} - \Box h_{\mu\nu} - \partial_\mu\partial_\nu h),$$
with $h = \eta^{\mu\nu} h_{\mu\nu}$ and $\Box = \eta^{\mu\nu}\partial_\mu\partial_\nu$.

In Lorenz gauge $\partial^\mu \bar h_{\mu\nu} = 0$ (with $\bar h_{\mu\nu} = h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu} h$), the first two terms of $R^{(1)}_{\mu\nu}$ simplify dramatically: $\partial^\rho\partial_\mu h_{\nu\rho} = \partial_\mu\partial^\rho h_{\nu\rho} = \frac{1}{2}\partial_\mu\partial_\nu h$ (and similar for $\nu$), so they cancel against the $-\partial_\mu\partial_\nu h$ piece, leaving $R^{(1)}_{\mu\nu} = -\frac{1}{2}\Box h_{\mu\nu}$. The linearised Einstein tensor is $G^{(1)}_{\mu\nu} = R^{(1)}_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu} R^{(1)} = -\frac{1}{2}\Box \bar h_{\mu\nu}$ (after using the trace relation).

So the linearised Einstein equations in Lorenz gauge are
$$\Box \bar h_{\mu\nu} = -16\pi G\, T_{\mu\nu}.$$

> [!note]- Derivation
> Standard linearised GR. The Lorenz gauge condition $\partial^\mu \bar h_{\mu\nu} = 0$ is the GR analogue of Lorenz gauge in EM, $\partial^\mu A_\mu = 0$. It simplifies the linearised Einstein equation by killing the cross-terms, leaving the wave-equation form $\Box \bar h_{\mu\nu} \propto T_{\mu\nu}$.

**Step 2: Static slow-matter limit.**

Static: $\partial_t h_{\mu\nu} = 0$, so $\Box = \partial_t^2 - \nabla^2 \to -\nabla^2$ when acting on time-independent functions.

Slow matter at rest: $T^{\mu\nu} \approx \rho u^\mu u^\nu$ with $u^\mu = (1, 0, 0, 0)$, so $T^{00} = \rho$ and $T_{00} = g_{00}^2 T^{00} \approx \rho$ (to leading order in $h$). Other components ($T^{0i}, T^{ij}$) are suppressed by powers of $v$ or $p$ (for dust, $p = 0$).

The trace $T = T^\mu{}_\mu = g_{00} T^{00} \approx 1\cdot\rho = \rho$.

The trace-reversed equation $R_{\mu\nu} = 8\pi G(T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T)$ for $(\mu\nu) = (0, 0)$: $R_{00} = 8\pi G(T_{00} - \frac{1}{2} g_{00} T) = 8\pi G(\rho - \frac{1}{2}\cdot 1\cdot\rho) = 4\pi G\rho$.

For the LHS, linearised $R_{00}$ for static weak metric: from the formula above (Lorenz gauge), $R^{(1)}_{00} = -\frac{1}{2}\Box h_{00} = -\frac{1}{2}(-\nabla^2) h_{00} = \frac{1}{2}\nabla^2 h_{00}$.

So: $\frac{1}{2}\nabla^2 h_{00} = 4\pi G\rho$, i.e., $\nabla^2 h_{00} = 8\pi G\rho$.

> [!note]- Derivation
> The trace-reversed form is convenient because for dust, $T$ is a simple number, and the trace-subtraction is easy. The factor $1/2$ in the trace subtraction gives the factor $1/2$ in $T_{00} - \frac{1}{2} g_{00} T = (1 - 1/2)\rho = \rho/2$; combined with the $8\pi G$ coefficient, $R_{00} = 8\pi G \cdot \rho/2 = 4\pi G\rho$.

**Step 3: Identification with Newtonian potential.**

The Newtonian potential $\phi$ is identified via the equivalence principle from the geodesic equation: $\ddot x^\alpha = -\Gamma^\alpha{}_{00} = -\frac{1}{2}\partial^\alpha h_{00}$, which equals Newton's $-\partial^\alpha\phi$ iff $h_{00} = 2\phi$.

Substituting $h_{00} = 2\phi$ into $\nabla^2 h_{00} = 8\pi G\rho$:
$$\nabla^2(2\phi) = 8\pi G\rho, \quad \text{hence} \quad \boxed{\nabla^2 \phi = 4\pi G\rho.}$$

This is **Newton's Poisson equation** with the correct coupling constant $4\pi G$. The factor of $8\pi G$ in the original Einstein equations is exactly what produces the $4\pi G$ in Poisson — after the trace-reversal and the identification $h_{00} = 2\phi$.

> [!note]- Derivation
> Combining Steps 2 and 3: $\nabla^2 h_{00} = 8\pi G \rho$ (from linearised Einstein); $h_{00} = 2\phi$ (from equivalence-principle identification); substituting gives $\nabla^2 \phi = 4\pi G \rho$. The coupling constant of GR ($8\pi G$) is fixed to produce the correct Newtonian coupling ($4\pi G$).

> [!note]- Complete formal solution
> Linearise $g_{\mu\nu} = \eta_{\mu\nu} + h_{\mu\nu}$ with $|h| \ll 1$ around Minkowski. In **Lorenz gauge** $\partial^\mu \bar h_{\mu\nu} = 0$ (with $\bar h_{\mu\nu} = h_{\mu\nu} - \frac{1}{2}\eta_{\mu\nu} h$), the linearised Einstein equations reduce to $\Box \bar h_{\mu\nu} = -16\pi G T_{\mu\nu}$.
>
> For static configurations ($\partial_t h = 0$) and slow matter ($T_{00} \approx \rho$, others negligible), the $(0, 0)$ trace-reversed equation $R_{00} = 8\pi G(T_{00} - \frac{1}{2} g_{00} T)$ becomes:
> $$\tfrac{1}{2}\nabla^2 h_{00} = 4\pi G\rho \quad \Rightarrow \quad \nabla^2 h_{00} = 8\pi G\rho.$$
>
> Identifying the Newtonian potential via $h_{00} = 2\phi$ (forced by the equivalence-principle reduction of the geodesic equation to $\ddot x = -\nabla \phi$):
> $$\nabla^2 \phi = 4\pi G\rho,$$
> Newton's Poisson equation with the correct coupling constant. $\square$

> [!note]- Sanity-check via independent route
> The Newtonian potential of a point mass $M$ at the origin is $\phi(r) = -GM/r$, satisfying $\nabla^2 \phi = 0$ for $r > 0$ and $\int \nabla^2 \phi\, dV = -4\pi GM$ (delta-function source). The Schwarzschild metric in the weak-field limit has $g_{00} = -(1 - 2M/r) \approx -(1 + 2(-M/r))$, identifying $\phi = -M/r$ — the correct Newtonian potential of a point mass $M$. The integration constant $M$ in the Schwarzschild derivation equals the Newtonian mass, confirming the identification.

---

# Key Takeaways

**The Newtonian limit fixes the coupling constant of GR.** The factor $8\pi G$ in the Einstein equations is *not* arbitrary; it is fixed by demanding the correct Newtonian Poisson equation $\nabla^2 \phi = 4\pi G\rho$ in the weak-field, slow-motion limit. This is the structural role of the Newtonian limit: not a derivation of GR from Newton (which is impossible — GR is more general), but a consistency check that fixes one numerical parameter. The trigger: any time you encounter the $8\pi G$ in GR, remember it's there because of the Newtonian limit, and the factor of 2 in $h_{00} = 2\phi$.

**Lorenz gauge dramatically simplifies the linearised Einstein equations.** Without gauge-fixing, $G^{(1)}_{\mu\nu}$ involves many derivatives of $h$ in a complicated combination. In Lorenz gauge $\partial^\mu \bar h_{\mu\nu} = 0$, it reduces to $-\frac{1}{2}\Box \bar h_{\mu\nu}$ — just a wave operator on the trace-reversed perturbation. This is the GR analogue of EM in Lorenz gauge: Maxwell's equations $\partial^\nu(\partial_\mu A_\nu - \partial_\nu A_\mu) = 4\pi J_\mu$ becomes $\Box A_\mu = -4\pi J_\mu$ in Lorenz gauge $\partial^\mu A_\mu = 0$. The trigger: for any gauge-theory calculation, always look for a convenient gauge (Lorenz, transverse-traceless, harmonic, etc.) that simplifies the field equations.

**The trace-reversed Einstein equation is convenient for matter-coupled problems.** The original $G_{\mu\nu} = 8\pi G T_{\mu\nu}$ has the Einstein tensor on the LHS; equivalent is $R_{\mu\nu} = 8\pi G(T_{\mu\nu} - \frac{1}{2} g_{\mu\nu} T)$ — the *trace-reversed* form, which has the Ricci tensor on the LHS. The latter is often easier when $T$ is simple. For dust at rest, $T - \frac{1}{2} g_{00} T = \rho/2$, immediately giving $R_{00} = 4\pi G\rho$. For vacuum, the trace-reversed form is $R_{\mu\nu} = 0$ — simpler than $G_{\mu\nu} = 0$. The trigger: any time you're solving the Einstein equations in a specific matter context, consider whether the trace-reversed form is simpler.

**Identification $h_{00} = 2\phi$ is the foundation of the post-Newtonian expansion.** Every post-Newtonian correction to Newton's gravity is computed as a correction to this leading-order identification. The next term is the **gravitomagnetic potential** $h_{0i} = A^G_i$, identified via the linearised geodesic at $O(v)$. The next is the spatial $h_{ij}$ corrections, identified via $O(v^2)$ effects. Knowing the leading identification puts you in position to compute all higher-order corrections systematically. The trigger: any computation in the weak-field regime starts from $h_{00} = 2\phi$ (or with sign convention $-2\phi$ in the other signature) and builds outward.
