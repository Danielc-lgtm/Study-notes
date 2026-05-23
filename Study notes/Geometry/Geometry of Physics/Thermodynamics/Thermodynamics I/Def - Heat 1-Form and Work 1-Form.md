---
type: definition
subject: thermodynamics
prereqs:
  - "Def - Thermodynamic State Space"
  - "Def - Quasistatic Process"
  - "Def - Covector Field and Differential 1-Form"
  - "Def - Closed and Exact Forms"
  - "Def - Line Integral of a 1-Form"
tags: [physics, thermodynamics, differential-geometry]
---

# Notation

$M^{n+1}$ is the [[Def - Thermodynamic State Space|thermodynamic state space]]. $\delta Q$ is the heat 1-form; $\delta W$ is the work 1-form. Both are smooth nowhere-vanishing sections of $T^*M$. For a quasistatic process $\gamma : [a, b] \to M$, the line integrals $\int_\gamma \delta Q$ and $\int_\gamma \delta W$ are real numbers — the heat absorbed and work done along the process. The notation $\delta$ (rather than $d$) emphasises that these are *non-exact* 1-forms; some texts use $\bar d Q$ or $đQ$ for the same purpose. See [[Thermodynamics I — Caratheodory's Approach to the Second Law]] for the full registry.

This is a compound page: it defines two interlocking notions — the heat 1-form $\delta Q$ and the work 1-form $\delta W$ — because they are introduced together and neither is fully usable without the other (the first law $dU = \delta Q - \delta W$ ties them).

---

# Axiom Motivation

Heat and work are the two ways energy is exchanged between a thermodynamic system and its surroundings, and the mathematical structure capturing them must reflect a fundamental observation: **both heat and work are path-dependent, not state functions**. A given pair of equilibrium states $(x, y)$ admits many quasistatic paths joining them, and the amount of heat absorbed (or work done) depends on the path chosen — not just on the endpoints.

The classical example is the same gas brought from state $A$ to state $B$ by two different paths. Along path 1 (slow isothermal expansion), heat flows in and work is done; along path 2 (adiabatic expansion followed by heating at constant volume), no heat flows during the first leg and a different amount flows during the second. Both paths have the same endpoints, the same $\Delta U$, but different $\int_1 \delta Q$ and $\int_2 \delta Q$. So $\int \delta Q$ is not the difference of any state function $Q(y) - Q(x)$ — heat is not stored in the system, it is a *transit quantity*.

The right mathematical object to capture a path-dependent quantity is a **1-form that is not exact**. A 1-form $\omega$ on $M$ assigns to every tangent vector $v \in T_xM$ a real number $\omega_x(v)$; integrated along a path $\gamma$, it gives $\int_\gamma \omega$. The integral is path-independent (depending only on endpoints) iff $\omega$ is exact — iff $\omega = df$ for some smooth function $f$ on $M$. If $\omega$ is *not* exact, $\int_\gamma \omega$ depends on the path. This is exactly what heat and work require.

The notation $\delta Q$ (rather than $dQ$) is chosen *precisely* to warn that $\delta Q$ is not the differential of any function $Q$. The temptation to write $Q(y) - Q(x)$ for $\int \delta Q$ is what the notation guards against. Some texts use $\bar d Q$, $đQ$, or simply $dQ$ with a verbal warning; Frankel (and we) use $\delta Q$ as the cleanest convention. The asymmetry with $dU$ — where $U$ is genuinely a state function and $dU$ is genuinely exact — is the entire content of the first law.

Why is the *work* form $\delta W$ specifically $p\, dV$ for a simple gas? The work done by a gas in expanding against external pressure $p_{\text{ext}}$ across a piston is $p_{\text{ext}}\, dV$ — force times distance. For a quasistatic process, $p_{\text{ext}} = p$ (the system's own pressure, since the system is in mechanical equilibrium with the surroundings), so $\delta W = p\, dV$. This is exact iff $p$ depends only on $V$, which is *not* generic — $p$ also depends on $T$ via the equation of state, so $\delta W = p(V, T)\, dV$ is not exact. The dependence on $T$ is what makes $\delta W$ non-exact: the work done in compressing a gas depends on whether you compress it hot or cold.

Why is $\delta Q$ not specified by an analogous formula? Because there is no single conjugate variable to "heat" the way $p$ is conjugate to $V$. In Caratheodory's setup, $\delta Q$ is *defined* via the first law as $\delta Q := dU + \delta W$ — heat is "internal-energy-change-plus-work-done". This is well-defined because $U$ is a state function (so $dU$ is fixed) and $\delta W$ is specified by the mechanical configuration. The resulting $\delta Q$ is then automatically a 1-form, and the question of whether it is closed or exact is what the second law will answer.

We assume $\delta Q$ and $\delta W$ are smooth and **nowhere vanishing**. The nowhere-vanishing assumption matters: it ensures that the [[Def - Adiabatic Process and Adiabatic Distribution|adiabatic distribution]] $\ker \delta Q$ is a smooth codimension-one distribution, with no singularities where its rank would jump. Physically, $\delta Q$ vanishing at a point would mean that *no* infinitesimal process can absorb or release heat at that state — physically pathological and ruled out for ordinary systems.

---

# The Definition

Let $M^{n+1}$ be a [[Def - Thermodynamic State Space|thermodynamic state space]] with mechanical manifold $V^n$, projection $\pi : M \to V$, and internal energy function $U : M \to \mathbb{R}$.

The **work 1-form** $\delta W$ is the smooth 1-form on $M$ defined by

$$\delta W := \sum_{i=1}^n p_i(x)\, dv^i,$$

where $v^1, \ldots, v^n$ are local coordinates on $V$ pulled back via $\pi$, and $p_i(x)$ is the pressure of the $i$-th region as a function of the state $x \in M$. For a simple gas ($n = 1$), $\delta W = p\, dV$.

The **heat 1-form** $\delta Q$ is the smooth 1-form on $M$ defined by the first law of thermodynamics:

$$\delta Q := dU + \delta W,$$

where $dU$ is the exact differential of the internal energy. Equivalently, the heat absorbed along a quasistatic process $\gamma$ is $\int_\gamma \delta Q = \int_\gamma dU + \int_\gamma \delta W = U(\gamma(b)) - U(\gamma(a)) + \int_\gamma \delta W$.

Both $\delta Q$ and $\delta W$ are assumed **smooth** and **nowhere vanishing** on $M$. Neither is assumed exact in general, and indeed neither is exact for any physical system with a non-trivial equation of state.

The **work done by the system** during a quasistatic process $\gamma : [a, b] \to M$ is
$$W_\gamma := \int_\gamma \delta W = \int_a^b \delta W(\dot\gamma(t))\, dt,$$
and the **heat absorbed by the system** is
$$Q_\gamma := \int_\gamma \delta Q.$$

---

# Relate to Other Fields / Compression

The heat and work 1-forms are the simplest physical instance of **non-exact 1-forms whose sum is exact**: $\delta Q - \delta W = dU$ is exact even though neither summand is. The same algebraic structure appears in electromagnetism (the gauge-dependent four-potential $A$ is not gauge-invariant, but its exterior derivative $F = dA$ is) and in symplectic mechanics (the canonical Poincaré 1-form $\theta$ is not closed, but $\omega = -d\theta$ is — and $\omega$ is the symplectic form).

**True name:** The heat 1-form is the **non-exact part of the differential of internal energy**. The work 1-form is the **mechanically computable part**. Their difference is exact because $U$ is a state function; their individual non-exactness reflects that "how much energy left the system as work" and "how much energy entered the system as heat" are protocol-dependent — they depend on what you do, not on where you end up.

In differential-geometric language, $\delta Q$ is a **Pfaffian form** — an alternative term for a smooth 1-form, used especially when the form defines a constraint or is being tested for integrability. The Pfaffian equation $\delta Q = 0$ defines the adiabatic distribution.

---

# Examples / Corollaries

**Is an instance: $\delta W = p\, dV$ for an ideal gas.** With $pV = nRT$ and $T$ as a second coordinate, $\delta W = (nRT/V)\, dV$. To verify non-exactness, compute $d(\delta W) = (nR/V)\, dT \wedge dV \neq 0$ — so $\delta W$ is not closed, hence not exact. Along an isotherm ($dT = 0$), $\delta W = (nRT/V)\, dV$ integrates to $nRT \log(V_f/V_i)$; along an adiabat the answer is different because $T$ changes with $V$.

**Is an instance: $\delta Q$ for an ideal gas.** With $U = (f/2) nRT$, $dU = (f/2)nR\, dT$. So
$$\delta Q = dU + \delta W = \frac{f}{2}nR\, dT + \frac{nRT}{V}\, dV.$$
This is not closed: $d(\delta Q) = (nR/V)\, dT \wedge dV \neq 0$. But dividing by $T$:
$$\frac{\delta Q}{T} = \frac{f}{2}nR\, \frac{dT}{T} + nR\, \frac{dV}{V} = d\left[ \frac{f}{2}nR \log T + nR \log V\right],$$
so $\delta Q / T$ *is* exact — the function in brackets is the entropy. The integrating factor $\lambda = 1/T$ has done its job.

**Is NOT an instance: $\delta Q$ a state function.** Any attempt to write $\delta Q = dQ$ for a function $Q$ fails. Concretely, for an ideal gas around a closed isothermal–adiabatic Carnot cycle, $\oint \delta Q = Q_h - Q_c \neq 0$ (this nonzero is exactly the engine's net heat absorption), whereas $\oint d Q = 0$ for any state function $Q$. The non-exactness of $\delta Q$ is what makes heat engines possible.

**Is NOT an instance: $\delta Q$ vanishing somewhere.** A nowhere-vanishing assumption is what makes the kernel $\ker \delta Q$ a smooth codimension-one distribution. If $\delta Q$ vanished at a state $x$, the rank of $\ker \delta Q$ would jump at $x$, the distribution would not be smooth, and Frobenius's theorem would not apply. Physical systems have $\delta Q \neq 0$ everywhere because every state can absorb or release heat by some infinitesimal process.

**Calibration check.** If you understand the definition, you should be able to (1) write $\delta W$ for two gas regions with pressures $p_1, p_2$ and volumes $v_1, v_2$ (answer: $\delta W = p_1\, dv_1 + p_2\, dv_2$), (2) verify that $d(\delta W) \neq 0$ for an ideal gas by direct computation, and (3) explain why the integral $\oint \delta Q$ around a closed cycle in the state space need not vanish even though "energy is conserved" — the resolution is that $\oint dU = 0$ (energy is a state function) but $\oint \delta Q = \oint \delta W$ (the net heat absorbed equals the net work done, both nonzero).

---

# Unlocked by This

> [!tip] The First Law and the Conservation of Energy *(from this topic)*
> The relation $dU = \delta Q - \delta W$ is the **first law of thermodynamics**, but the *interesting* part is the exactness of $dU$. The non-exactness of $\delta Q$ and $\delta W$ individually is the "thermodynamic" content; the exactness of their difference is what justifies calling $U$ a conserved energy. See [[Def - The First Law of Thermodynamics]].

> [!tip] The Frobenius Integrability Question for $\delta Q$ *(from this topic)*
> The next question is whether the 1-form $\delta Q$, though non-exact, admits an **integrating factor** — a function $\lambda$ such that $\delta Q / \lambda$ is exact. The Frobenius integrability condition $\delta Q \wedge d(\delta Q) = 0$ is necessary and sufficient (locally) for an integrating factor to exist. Caratheodory's principle is the physical input that forces this condition. See [[Thm - Caratheodory's Theorem on the Second Law]].

> [!tip] Gauge Theory and Connection 1-Forms *(from Gauge Theory)*
> The notion of a non-exact 1-form whose exterior derivative carries physical meaning recurs throughout **gauge theory**: the electromagnetic four-potential $A_\mu\, dx^\mu$ is gauge-dependent (not exact, gauge transformations shift $A$ by $d\chi$), but its exterior derivative $F = dA$ is the gauge-invariant field strength. The connection 1-form on a principal bundle is the geometric generalisation of $A$, with curvature $F = dA + A \wedge A$ as the generalisation of the electromagnetic field strength. See [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]] and [[Gauge Theory III — Connections in Principal and Associated Bundles]].
