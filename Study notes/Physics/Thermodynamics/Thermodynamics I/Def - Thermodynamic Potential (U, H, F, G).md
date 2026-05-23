---
type: definition
subject: thermodynamics
prereqs:
  - "Def - The First Law of Thermodynamics"
  - "Def - Absolute Temperature and Entropy"
  - "Def - Closed and Exact Forms"
tags: [physics, thermodynamics]
---

# Notation

$U(S, V)$ — internal energy, natural variables $(S, V)$. $H(S, p) = U + pV$ — enthalpy, natural variables $(S, p)$. $F(T, V) = U - TS$ — Helmholtz free energy, natural variables $(T, V)$. $G(T, p) = U + pV - TS = H - TS$ — Gibbs free energy, natural variables $(T, p)$. All four are smooth functions on the [[Def - Thermodynamic State Space|state space]] $M$; the parenthesised arguments name their *natural variables*. See [[Thermodynamics I — Caratheodory's Approach to the Second Law]] for the full registry.

This is a compound page: it defines four interlocking notions — the four thermodynamic potentials $U, H, F, G$ — because they are related by Legendre transforms and form a single algebraic structure (the "Legendre cube"). Each is most useful in a specific experimental setup, and none can be fully understood without seeing how it sits in the family.

---

# Axiom Motivation

The motivation for thermodynamic potentials is that **different experiments hold different variables fixed**, and the natural state function to use depends on what is fixed. Internal energy $U(S, V)$ is the natural variable in a thermally isolated, mechanically rigid box ($S, V$ fixed) — but few experiments hold $S$ fixed. More commonly, one holds $T$ fixed (place the system in a thermal reservoir), or $p$ fixed (open the system to atmospheric pressure), or both. The thermodynamic potentials $H, F, G$ are obtained from $U$ by Legendre transforms swapping conjugate pairs, so that each potential has the experimentally-fixed variables as its natural variables.

The first design choice is the **Legendre transform** itself. Why this specific construction? Because Legendre transforming swaps a variable for its conjugate while preserving the exactness structure: if $dU = T\, dS - p\, dV$ has $(S, V)$ as natural variables and $(T, -p)$ as the corresponding "slopes", then $d(U - TS) = dU - T\, dS - S\, dT = -S\, dT - p\, dV$ has $(T, V)$ as natural variables. So defining $F := U - TS$ packages the transform as an algebraic substitution. The new potential $F$ has *exact* differential $dF$ with new natural variables — exactly what is needed for $d^2 = 0$ to produce useful Maxwell relations in the new variables.

The second design choice is **which transforms to perform**. There are four state variables in a simple gas — $S, V, T, p$ — paired as $(S, T)$ and $(V, p)$. There are $2^2 = 4$ possibilities for which member of each pair is the natural variable, giving four potentials:
- $(S, V)$ both extensive: $U(S, V)$ — internal energy, fundamental
- $(S, p)$: $H(S, p) = U + pV$ — enthalpy
- $(T, V)$: $F(T, V) = U - TS$ — Helmholtz free energy
- $(T, p)$ both intensive: $G(T, p) = U + pV - TS$ — Gibbs free energy

Each name reflects historical use: enthalpy ("warmth") for processes at constant pressure; Helmholtz "free energy" because it is the energy *free to do work* at constant temperature; Gibbs free energy for chemical reactions at constant $T, p$.

The third design choice is the **sign convention** in the Legendre transform. The transform of $f(x)$ in variable $x$ is $\tilde f(p) := p x - f(x)$ (the standard *positive* sign) or $\tilde f(p) := f(x) - px$ (*negative* sign). Thermodynamics uses the negative sign for the $TS$ transform and the positive sign for the $pV$ transform — and the reasons trace back to physical conventions. The Helmholtz energy $F = U - TS$ is what you minimise at fixed $T$ (equilibrium minimises Helmholtz free energy in a thermal bath); the enthalpy $H = U + pV$ is what you compute at fixed $p$ (heat absorbed in an isobaric process equals $\Delta H$). The signs are chosen so each potential plays the right physical role.

The fourth design choice is which natural variables to fix for the **equilibrium minimisation** principle. A system in thermal contact with a reservoir at temperature $T_0$, with its volume held fixed, equilibrates by minimising $F$ (over all internal degrees of freedom of the system) at the bath temperature. The proof is that the entropy of the universe (system plus bath) must increase, and one can show $\Delta S_{\text{universe}} = -\Delta F_{\text{system}} / T_0$ — so minimising $F$ is equivalent to maximising $S_{\text{universe}}$. The same logic gives: $U$ minimised at fixed $(S, V)$ for isolated systems, $H$ minimised at fixed $(S, p)$ for systems in pressure-controlled isolated boxes, $G$ minimised at fixed $(T, p)$ for chemical systems open to the atmosphere. Each potential's natural variables are exactly the variables held fixed in the corresponding experimental setup.

A reader might ask: why are these the four interesting potentials, and not some larger family? The answer is that the state space of a simple gas is 2-dimensional (after fixing the volume of the bag, say), so there are only two pairs of conjugate variables — $(S, T)$ and $(V, p)$. Each pair can be Legendre-transformed independently, giving four combinations. For more complex systems with $n+1$-dimensional state space, there are $2^n$ thermodynamic potentials (one for each subset of conjugate-pair swaps), but the four standard ones $U, H, F, G$ exhaust the simple-system case.

---

# The Definition

Let $M$ be a [[Def - Thermodynamic State Space|thermodynamic state space]] with [[Def - Absolute Temperature and Entropy|absolute temperature]] $T$, [[Def - Absolute Temperature and Entropy|entropy]] $S$, pressure $p$, volume $V$ (for a simple gas; or pressures $p_i$ and volumes $v^i$ for a system of $n$ regions). Then:

**Internal energy.** $U : M \to \mathbb{R}$ is the energy function from the [[Def - The First Law of Thermodynamics|first law]], with natural variables $(S, V)$ and

$$dU = T\, dS - p\, dV, \qquad T = \left(\frac{\partial U}{\partial S}\right)_V, \quad p = -\left(\frac{\partial U}{\partial V}\right)_S.$$

**Enthalpy.** $H : M \to \mathbb{R}$ is defined by $H := U + pV$, with natural variables $(S, p)$ and

$$dH = T\, dS + V\, dp, \qquad T = \left(\frac{\partial H}{\partial S}\right)_p, \quad V = \left(\frac{\partial H}{\partial p}\right)_S.$$

The enthalpy is the natural energy at constant pressure: along an isobaric process ($dp = 0$), $dH = T\, dS = \delta Q$, so $\Delta H$ equals the heat absorbed.

**Helmholtz free energy.** $F : M \to \mathbb{R}$ is defined by $F := U - TS$, with natural variables $(T, V)$ and

$$dF = -S\, dT - p\, dV, \qquad S = -\left(\frac{\partial F}{\partial T}\right)_V, \quad p = -\left(\frac{\partial F}{\partial V}\right)_T.$$

The Helmholtz free energy is minimised at equilibrium for systems at fixed $(T, V)$ (thermal contact with a reservoir at $T$, rigid container). Along an isothermal process ($dT = 0$), $dF = -p\, dV = -\delta W$, so $-\Delta F$ equals the maximum work extractable.

**Gibbs free energy.** $G : M \to \mathbb{R}$ is defined by $G := U + pV - TS = H - TS$, with natural variables $(T, p)$ and

$$dG = -S\, dT + V\, dp, \qquad S = -\left(\frac{\partial G}{\partial T}\right)_p, \quad V = \left(\frac{\partial G}{\partial p}\right)_T.$$

The Gibbs free energy is minimised at equilibrium for systems at fixed $(T, p)$ (open to atmosphere at temperature $T$). It is the central potential for chemistry and phase transitions.

The four potentials are related by the **Legendre cube**:

$$\begin{array}{ccc} U(S, V) & \xleftrightarrow{\;V \leftrightarrow p\;} & H(S, p) \\ \updownarrow {\scriptstyle S \leftrightarrow T} & & \updownarrow {\scriptstyle S \leftrightarrow T} \\ F(T, V) & \xleftrightarrow{\;V \leftrightarrow p\;} & G(T, p) \end{array}$$

Each arrow is a Legendre transform: horizontal arrows swap $(V, p)$, vertical arrows swap $(S, T)$. The diagonal $U \leftrightarrow G$ swaps both. Each potential's differential exhibits its natural variables explicitly.

---

# Relate to Other Fields / Compression

The thermodynamic potentials are **Legendre transforms of a single function (the internal energy) along different combinations of conjugate variable pairs**. The same construction appears in classical mechanics, where the Lagrangian $L(q, \dot q)$ and Hamiltonian $H(q, p)$ are related by the Legendre transform $L \to H = p \dot q - L$ swapping velocity $\dot q$ for momentum $p$.

**True name:** Each thermodynamic potential is **the state function whose minimum on $M$ characterises equilibrium when its natural variables are held fixed**. For an isolated system ($S, V$ fixed): $U$ minimised. For thermal-equilibrium with fixed volume: $F$ minimised. For thermal-and-mechanical equilibrium: $G$ minimised. The choice of potential is dictated by what the experimentalist controls.

In convex analysis, the Legendre transform of a convex function $f$ is the convex conjugate $f^*(p) = \sup_x[px - f(x)]$, and $f^{**} = f$ when $f$ is convex lower-semicontinuous. The four thermodynamic potentials are convex conjugates of one another in the appropriate variables, with convexity (or concavity, depending on which variables and signs) ensured by the second law's stability requirements. Wightman's introduction to Israel's *Convexity in the Theory of Lattice Gases* makes this completely rigorous.

---

# Examples / Corollaries

**Ideal gas potentials.** For a simple ideal gas with $pV = nRT$ and $U = (f/2)nRT$:
- $U(T) = (f/2) nRT$ — depends only on $T$, since $U$ is a function of $S, V$ but for an ideal gas the $V$-dependence vanishes.
- $H(T) = U + pV = (f/2 + 1) nRT = C_p T$ where $C_p = (f/2 + 1) nR$.
- $F(T, V) = U - TS = (f/2) nRT - T[(f/2) nR \log T + nR \log V + \text{const}] = -nRT[(f/2) \log T + \log V] + \text{const} \cdot T + (f/2)nRT$.
- $G(T, p) = H - TS$, more naturally expressed in $(T, p)$ after eliminating $V = nRT/p$: $G(T, p) = nRT \log p + (\text{function of } T)$. The pressure-dependent part is $nRT \log p$ at fixed $T$ — important for the chemical potential of an ideal gas.

**Minimising $F$ at fixed $(T, V)$.** A system in thermal contact with a reservoir at $T_0$ and with fixed volume $V$ equilibrates by minimising $F$. *Proof sketch:* the entropy of system-plus-reservoir is $S_{\text{tot}} = S_{\text{sys}} + S_{\text{res}}$. Energy conservation gives $\Delta U_{\text{sys}} = -\Delta U_{\text{res}}$. The reservoir is large, so $\Delta U_{\text{res}} = T_0 \Delta S_{\text{res}}$ to first order, giving $\Delta S_{\text{res}} = -\Delta U_{\text{sys}}/T_0$. The second law $\Delta S_{\text{tot}} \geq 0$ then becomes $\Delta S_{\text{sys}} - \Delta U_{\text{sys}}/T_0 \geq 0$, equivalently $\Delta(U_{\text{sys}} - T_0 S_{\text{sys}}) \leq 0$. Since $T_0$ is the system's equilibrium temperature, this is $\Delta F_{\text{sys}} \leq 0$ — so equilibrium is reached at the minimum of $F$.

**Heat absorbed at constant pressure is $\Delta H$.** Along an isobaric process ($dp = 0$), $dH = T\, dS + V\, dp = T\, dS = \delta Q$ (by $\delta Q = T\, dS$ for quasistatic). Integrating, $Q_{\text{isobaric}} = \Delta H$. This is why enthalpies of reaction are tabulated for chemistry: chemical reactions happen at constant pressure (atmospheric), so the heat released equals $\Delta H$.

**Calibration check.** If you understand the definition, you should be able to (1) derive $dG = -S\, dT + V\, dp$ starting from $G = U + pV - TS$ and the first law (compute $dG = dU + V\, dp + p\, dV - T\, dS - S\, dT = -p\, dV + T\, dS + V\, dp + p\, dV - T\, dS - S\, dT$ and simplify), (2) state which potential is minimised at fixed $(T, p)$ (answer: $G$), and (3) verify that the Maxwell relation $(\partial S/\partial V)_T = (\partial p/\partial T)_V$ follows from $d^2 F = 0$ and contrast with the corresponding identity from $d^2 G = 0$ in $(T, p)$ variables.

---

# Unlocked by This

> [!tip] Maxwell Relations *(from this topic)*
> Each thermodynamic potential's $d^2 = 0$ produces a [[Thm - Maxwell Relations from Closedness|Maxwell relation]] equating cross-partial derivatives of conjugate variables. Four potentials, one Maxwell relation each. These let you compute hard-to-measure quantities (anything involving $\partial/\partial S$) from easy-to-measure quantities (partial derivatives of $T, p, V$).

> [!tip] Chemical Potential and Phase Transitions *(from Statistical Mechanics)*
> The Gibbs free energy generalises to systems with variable particle number $N$ via $dG = -S\, dT + V\, dp + \mu\, dN$, where $\mu = (\partial G/\partial N)_{T, p}$ is the **chemical potential** — the free-energy cost per added particle. At phase equilibrium (e.g., liquid–vapour), the chemical potentials of the two phases are equal, and the **Clausius–Clapeyron equation** $dp/dT = \Delta S/\Delta V$ for the coexistence curve follows from equating $dG$ of the two phases along the coexistence boundary. Statistical mechanics then computes $\mu$ from the grand canonical partition function via $-\beta \mu = \partial \log Z/\partial N$ at fixed activity.

> [!tip] Convexity and the Stability of Equilibrium *(from Convex Analysis)*
> Equilibrium stability requires concavity of $S(U, V)$, equivalently convexity of $U(S, V)$, and the corresponding convexity/concavity of the other potentials. **Convex analysis** systematises this: the Legendre transform of a convex function is convex (in the conjugate variable), and the second derivatives are reciprocally related ($\partial^2 f / \partial x^2 = 1/(\partial^2 f^* / \partial p^2)$ along the conjugate slope). Violation of convexity signals an instability — a phase transition. Wightman's introduction to Israel's monograph develops this for lattice systems, and Israel's theorem characterises the analytic structure of $G$ near phase transitions in terms of analyticity properties of the partition function.

> [!tip] Legendre Transform in Geometric Mechanics *(from Geometric Mechanics)*
> The Lagrangian-to-Hamiltonian transition in classical mechanics is *literally* a Legendre transform: $H(q, p) = p \dot q - L(q, \dot q)$ with $p = \partial L/\partial \dot q$. The same algebra, the same sign conventions, the same involutivity. The reason both contexts use Legendre transforms is the same: in each case the function's natural variables are not the variables we want to control, and Legendre transforming swaps them. See [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]] for the symplectic-geometric picture and the relation to canonical transformations.
