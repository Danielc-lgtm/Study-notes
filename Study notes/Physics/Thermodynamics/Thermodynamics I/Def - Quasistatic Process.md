---
type: definition
subject: thermodynamics
prereqs:
  - "Def - Thermodynamic State Space"
  - "Def - Smooth Manifold"
tags: [physics, thermodynamics]
---

# Notation

$M$ is the [[Def - Thermodynamic State Space|thermodynamic state space]], a smooth manifold of dimension $n+1$. A path is a smooth map $\gamma : [a, b] \to M$ from a closed interval into $M$; $\dot\gamma(t)$ is its tangent vector at parameter value $t$. Equilibrium states are points of $M$; non-equilibrium states are not in $M$ at all. See [[Thermodynamics I — Caratheodory's Approach to the Second Law]] for the full registry.

---

# Axiom Motivation

The motivation for the quasistatic-process concept is to make sense of an integral $\int \delta Q$ or $\int \delta W$ along "the process by which heat $Q$ is added or work $W$ is done". For these integrals to be meaningful, two things have to be true: there must be an actual path in the state space along which to integrate, and the 1-forms $\delta Q$ and $\delta W$ must be defined at every intermediate state. Both demands force the process to pass only through equilibrium states.

The first demand — that a path exists — is geometric. The state space $M$ contains only equilibrium states, so any path in $M$ is a continuous family of equilibrium states. A real-world process like "violently stirring a fluid" begins at an equilibrium state $x$, ends at an equilibrium state $y$, but passes through *non-equilibrium* intermediate states that are not in $M$. There is no path in $M$ representing the actual physical trajectory of such a process; the best we can do is record the endpoints $(x, y)$ and accept that the intermediate dynamics happens "off the manifold". Drawings of such processes show a dashed line from $x$ to $y$ to indicate that no path in $M$ exists.

The second demand — that the 1-forms be defined — adds a physical constraint. The work 1-form $\delta W = p\, dV$ requires the *pressure* $p$ to be defined; pressure is defined only when the system is in mechanical equilibrium, with a uniform pressure throughout. If the system is turbulent, $p$ is spatially varying and ill-defined, so $\delta W$ has no meaning. Similarly, the heat 1-form $\delta Q$ requires a meaningful flow of heat into a well-defined temperature distribution, which requires thermal equilibrium. So the integrability of $\delta Q$ and $\delta W$ along the path $\gamma$ requires that $\gamma$ pass through states where pressure and temperature are well-defined — i.e., equilibrium states.

A process satisfying both demands is **quasistatic**: it traces out a smooth curve in the equilibrium manifold $M$. "Quasi" because no real process is exactly equilibrium-preserving — driving the system across $M$ at finite speed always disturbs the equilibrium slightly. But for processes slow compared to the system's relaxation time, the disturbance is small and the path-in-$M$ idealisation is accurate.

It is critical to distinguish quasistatic from **reversible**. A quasistatic process is one whose path lies in $M$; a reversible process is one that can be run backwards along the same path (with the surroundings restored) at no net entropy cost. Every reversible process is quasistatic (you must pass through equilibrium states to undo each step), but not every quasistatic process is reversible — slow compression with friction is quasistatic (the path lies in $M$, since the system is in equilibrium at each instant) but irreversible (friction dissipates work as heat, and entropy of the system-plus-surroundings strictly increases). The distinction matters because the integral $\int_\gamma \delta Q / T = \Delta S$ is correct for any quasistatic $\gamma$, but $\delta Q$ along an irreversible quasistatic path is less than the maximum heat that could have been absorbed without doing work — frictional dissipation is "wasted" heat absorbed by the system rather than work done.

---

# The Definition

A **quasistatic process** in a thermodynamic state space $M$ is a smooth (or piecewise smooth) path $\gamma : [a, b] \to M$ — a smooth map from a closed interval into $M$. Its **initial state** is $\gamma(a)$, its **final state** is $\gamma(b)$, and its **tangent vector** at parameter value $t$ is $\dot\gamma(t) \in T_{\gamma(t)} M$. The process is **closed** or a **cycle** if $\gamma(a) = \gamma(b)$.

A **non-quasistatic process** (also called a *transition* or *irreversible jump*) is a pair $(x, y)$ of equilibrium states without an associated path — physically, the system starts at $x$, undergoes some violent dynamics off the equilibrium manifold, and ends at $y$. Such processes are represented schematically by a dashed line from $x$ to $y$; the integrals $\int \delta Q$ and $\int \delta W$ along the "process" are undefined, though differences of state functions (such as $U(y) - U(x)$ or $S(y) - S(x)$) remain well-defined.

A quasistatic process is **reversible** if its time-reversal $\bar\gamma(t) := \gamma(a + b - t)$, together with corresponding reverse heat and work exchanges with the surroundings, restores both system and surroundings to their initial states. It is **irreversible** otherwise.

---

# Relate to Other Fields / Compression

A quasistatic process is the **path-in-the-equilibrium-manifold idealisation** of a real thermodynamic transition. In the language of dynamical systems, it is an integral curve of some (possibly time-dependent) vector field on $M$, and the choice of which vector field encodes the experimental protocol.

**True name:** A quasistatic process is a process slow enough that **the system is always in equilibrium with a well-defined temperature and pressure**, so that the differential forms $\delta Q$ and $\delta W$ can be evaluated along its tangent at every instant. The "slow enough" criterion is concretely "much slower than the system's relaxation time" — the time for the system to reach equilibrium from a small perturbation.

In differential geometry, the quasistatic-vs-non-quasistatic distinction is the distinction between **a smooth path in $M$** and **a discontinuous jump between two points of $M$**. The non-quasistatic case is what you get when the "intermediate trajectory" leaves $M$ entirely — corresponding to phase-space dynamics that violently disturbs the equilibrium foliation of an underlying microscopic system.

---

# Examples / Corollaries

**Is an instance: slow compression of an ideal gas.** Push a piston in slowly enough that the gas remains spatially uniform throughout. The path in $M$ is parametrised by the volume coordinate $V$ decreasing from $V_i$ to $V_f$, with the equation of state determining $p(V)$ and $T(V)$. The process is quasistatic because the system is in equilibrium at every instant.

**Is an instance: slow heating at constant volume.** Place the gas in thermal contact with a sequence of heat reservoirs at infinitesimally higher temperatures. The path lies along a fibre of the submersion $\pi$ (constant volume), parametrised by $U$ or $T$ increasing.

**Is NOT an instance: free expansion (Joule expansion).** A gas in a container with a valve into an evacuated chamber, with the valve suddenly opened. The gas rushes through the valve in a turbulent, non-equilibrium way; intermediate states are not in $M$. The endpoints (initial state with gas in one chamber, final state with gas filling both) are equilibrium states, but no path in $M$ connects them along the actual process. For an ideal gas, the first law and the fact that no work is done (against zero pressure) and no heat is exchanged (the container is insulated) give $\Delta U = 0$, so $T$ is unchanged — but this is deduced from endpoint data, not from integrating along a path.

**Is NOT an instance: stirring a fluid.** A paddle wheel turning in a fluid at constant volume does work on the fluid (mechanical), which becomes heat by viscous dissipation. The process is adiabatic (no heat enters from outside) but not quasistatic (the fluid is turbulent during stirring). The endpoint state has higher $U$ than the initial state, and no path in $M$ connects them — this is Frankel's prototype of a non-quasistatic adiabatic transition (the "stirring" process used to set up the entropy direction).

**Calibration check.** If you understand the definition, you should be able to (1) explain why "slow compression with friction" is quasistatic but irreversible (the system is in equilibrium at each instant, but the surroundings cannot be restored without net heat exchange), (2) sketch a quasistatic adiabatic process and a non-quasistatic adiabatic process between the same endpoints, and (3) name a thermodynamic quantity that can be computed for the non-quasistatic process despite the absence of a path (answer: any state-function difference like $\Delta U$, $\Delta S$, $\Delta H$).

---

# Unlocked by This

> [!tip] Reversible vs Irreversible Processes *(from this topic)*
> The distinction between quasistatic and reversible processes is the geometric prerequisite for the **second law in inequality form**: $dS \geq \delta Q / T_{\text{surr}}$, with equality for reversible processes only. Quasistatic but irreversible processes (like compression with friction) saturate strict inequality, and the gap is the "wasted work" dissipated as heat. The full theory of irreversibility lives in non-equilibrium thermodynamics and statistical mechanics.

> [!tip] The Carnot Cycle as the Unique Maximum-Efficiency Reversible Cycle *(from Engineering Thermodynamics)*
> The Carnot cycle is the unique cycle composed entirely of quasistatic reversible isotherms and adiabats; its efficiency $\eta = 1 - T_c/T_h$ is the maximum possible efficiency for any cycle operating between two reservoirs at $T_h$ and $T_c$. The proof that no cycle can exceed Carnot efficiency uses the quasistatic-process formalism crucially: any cycle's efficiency is bounded by integrating $dS \geq \delta Q / T$ around the cycle, and only Carnot saturates the bound. See [[Ex - Carnot Cycle in Pressure-Volume and in Temperature-Entropy]].

> [!tip] The Jarzynski Equality *(from Non-Equilibrium Statistical Mechanics)*
> For *non-quasistatic* processes — fast switching, driven dynamics — there is no classical "$\int \delta W$" path integral. The **Jarzynski equality** $\langle e^{-\beta W} \rangle = e^{-\beta \Delta F}$ relates the *distribution* of work values over many repetitions of a fast process to the equilibrium free-energy difference, even when each individual realisation is wildly non-quasistatic. This is one of the rare exact results bridging equilibrium and non-equilibrium thermodynamics, and it relies fundamentally on the quasistatic-process formalism being inadequate — the equality says the failure of quasistaticity has a precise statistical character.
