---
type: definition
subject: thermodynamics
prereqs:
  - "Def - Thermodynamic State Space"
  - "Def - Heat 1-Form and Work 1-Form"
  - "Def - Closed and Exact Forms"
  - "Def - The Differential of a Function as a 1-Form"
tags: [physics, thermodynamics, differential-geometry]
---

# Notation

$M^{n+1}$ is the [[Def - Thermodynamic State Space|thermodynamic state space]]; $U : M \to \mathbb{R}$ is the internal energy; $dU$ is its exact differential; $\delta Q$ and $\delta W$ are the [[Def - Heat 1-Form and Work 1-Form|heat and work 1-forms]]. The first law is a relation among 1-forms on $M$. See [[Thermodynamics I — Caratheodory's Approach to the Second Law]] for the full registry.

---

# Axiom Motivation

The first law of thermodynamics is the assertion that **internal energy is a state function and is conserved when heat and work exchanges are accounted for**. It is not a mathematical theorem; it is a physical axiom, summarising centuries of experiments showing that energy is neither created nor destroyed in thermodynamic processes (Joule's mechanical-equivalent-of-heat experiments being the canonical evidence).

The geometric content of the axiom has two parts, and it is essential to separate them because they say different things.

**Part one: there exists a globally defined function $U : M \to \mathbb{R}$.** This is the substantive existence claim. The internal energy of a system is well-defined as a function of state, meaning: any two paths in $M$ connecting equilibrium states $x$ and $y$ give the same value of $U(y) - U(x)$. If you bring a litre of gas from $(p_1, V_1)$ to $(p_2, V_2)$ by two different reversible paths and measure heat absorbed and work done along each, the sums $Q - W$ agree even though $Q$ and $W$ separately differ. This consistency, observed across all experiments, is the empirical content of "energy is a state function" and is what licenses calling $U$ a function on $M$ in the first place. Dropping this would mean energy depends on history, not just on the present state — and would dissolve the entire thermodynamic formalism, since "energy of this gas" would not be a meaningful concept.

**Part two: the 1-form $dU$ equals $\delta Q - \delta W$.** Given the existence of $U$, this part says that the difference of the two transit 1-forms ($\delta Q$ in, $\delta W$ out) is the exact differential of $U$. Equivalently, along any quasistatic path $\gamma$, $U(\gamma(b)) - U(\gamma(a)) = \int_\gamma (\delta Q - \delta W)$. This is **conservation of energy** in differential form: at each instant, the rate of increase of $U$ equals the rate at which heat enters minus the rate at which work is done. The "minus" sign for work reflects our sign convention ($\delta W$ is work done *by* the system, so work done by the system *decreases* its energy).

A reader might ask: why this particular combination $\delta Q - \delta W$? Why not $\delta Q + \delta W$ or some other linear combination? The answer is that this is the empirical content: experiments confirm that the *specific combination* heat-in minus work-out matches the change in internal energy. With a different sign convention ($\delta W$ as work done *on* the system), the law reads $dU = \delta Q + \delta W$ — but the physical content is the same. The substantive claim is not the sign but the structure: there is exactly one linear combination of $\delta Q$ and $\delta W$ that is exact, and that combination is $dU$.

Why is the *exactness* of $dU$ the interesting feature? Because it tells you that out of three Pfaffians on $M$ ($dU$, $\delta Q$, $\delta W$), exactly one is exact. The other two are non-exact, meaning heat and work are individually path-dependent. The first law is therefore a precise statement about the structure of $T^*M$: it picks out a particular exact 1-form $dU$ and decomposes it as a difference of two non-exact 1-forms with physical meaning. This decomposition is non-unique (one could add an exact form to $\delta Q$ and subtract it from $\delta W$ without changing $dU$), but the physical meaning of each summand is fixed by what is being held constant during the process.

A subtler aspect of the first law: the *axiomatic* content of "$U$ is a state function" is independent of the second law. The first law alone tells you energy is conserved but says nothing about which direction processes run; you can transform heat into work and work into heat freely under the first law. The second law (Caratheodory's principle) is what introduces irreversibility and the entropy direction. So the first law is *necessary* for thermodynamics but not *sufficient*; both laws are needed, and the second law is the geometric content of [[Thm - Caratheodory's Theorem on the Second Law|Caratheodory's theorem]].

---

# The Definition

The **first law of thermodynamics** is the relation

$$dU = \delta Q - \delta W$$

among 1-forms on the [[Def - Thermodynamic State Space|thermodynamic state space]] $M$, where $U : M \to \mathbb{R}$ is the globally defined internal energy function (an exact 1-form $dU$), $\delta Q$ is the [[Def - Heat 1-Form and Work 1-Form|heat 1-form]], and $\delta W$ is the [[Def - Heat 1-Form and Work 1-Form|work 1-form]]. The sign convention is that $\delta W$ is work done **by** the system on its surroundings and $\delta Q$ is heat absorbed **by** the system.

The integrated form, for any quasistatic process $\gamma : [a, b] \to M$:

$$U(\gamma(b)) - U(\gamma(a)) = Q_\gamma - W_\gamma \quad \text{where} \quad Q_\gamma = \int_\gamma \delta Q, \quad W_\gamma = \int_\gamma \delta W.$$

For a non-quasistatic transition $(x, y)$, the integrals $Q$ and $W$ may not individually be defined (no path exists in $M$), but the equation
$$U(y) - U(x) = Q - W$$
remains valid as a relation among *energy*, *heat exchanged*, and *work done* — provided $Q$ and $W$ are measured externally (calorimetrically and mechanically).

A direct consequence: for any closed quasistatic cycle $\gamma$ (with $\gamma(a) = \gamma(b)$), $\oint_\gamma dU = 0$, hence $\oint \delta Q = \oint \delta W$ — the net heat absorbed in a cycle equals the net work done. This is the basic principle of all heat engines.

---

# Relate to Other Fields / Compression

The first law is a **conservation law expressed as the exactness of a single 1-form on the state space**. In classical mechanics, the analogous statement is that $dE = 0$ along any trajectory of an autonomous Hamiltonian system — the total energy is conserved. The first law is the thermodynamic generalisation: total internal energy is conserved when heat and work exchanges are accounted for, and "accounted for" means subtracting the exact decomposition $\delta Q - \delta W$.

**True name:** The first law is the statement that **$\delta Q - \delta W$ is exact, even though neither $\delta Q$ nor $\delta W$ is exact individually**. This is what makes $U$ a state function and licenses the entire algebraic apparatus of thermodynamic potentials (Legendre transforms, Maxwell relations) that builds on $U$.

In the language of de Rham cohomology, $\delta Q$ and $\delta W$ are 1-cocycles modulo the 1-coboundary $dU$ — they represent the same de Rham class. The non-exactness of $\delta Q$ and $\delta W$ individually means that, viewed as elements of $H^1(M)$, neither is zero (or rather, only their combination is reducible to the zero class via $dU$).

---

# Examples / Corollaries

**Ideal gas: heating at constant volume.** Along an isochore $dV = 0$, $\delta W = p\, dV = 0$, so $\delta Q = dU$. The heat absorbed equals the energy increase: $Q = \Delta U = (f/2)nR\Delta T$. The heat capacity at constant volume is $C_V = (\partial U/\partial T)_V = (f/2)nR$ — *by definition* of $C_V$, the heat needed per unit temperature rise at fixed volume is the partial derivative of $U$.

**Ideal gas: adiabatic process.** Along an adiabat $\delta Q = 0$, so $dU = -\delta W$, i.e., $(f/2) nR\, dT = -p\, dV = -(nRT/V)\, dV$. Separating variables, $(f/2) dT/T = -dV/V$, giving $T V^{2/f} = \text{const}$, or with $\gamma = 1 + 2/f$, the adiabatic equation of state $pV^\gamma = \text{const}$.

**Ideal gas: isothermal expansion.** Along an isotherm $dT = 0$, so $dU = (f/2) nR\, dT = 0$ — internal energy is unchanged. So $\delta Q = \delta W = (nRT/V)\, dV$, giving $Q = W = nRT \log(V_f/V_i)$ — all heat absorbed becomes work done.

**Joule's free expansion (non-quasistatic).** A gas in chamber $A$ at volume $V_1$ expands suddenly into the evacuated chamber $B$ through an opened valve, with the container insulated. No work is done (against zero external pressure) and no heat enters (insulated): $W = 0$, $Q = 0$. So $\Delta U = 0$ by the first law. For an ideal gas this forces $\Delta T = 0$ (since $U$ depends only on $T$); for a real gas, $T$ changes — this is the Joule coefficient $(\partial T/\partial V)_U$ and is nonzero for non-ideal gases.

**Calibration check.** If you understand the first law, you should be able to (1) explain why $\oint \delta Q \neq 0$ around a non-trivial cycle even though "energy is conserved" — the resolution is $\oint dU = 0$ but $\oint \delta Q$ equals $\oint \delta W$, both nonzero, (2) compute $C_p - C_V$ for an ideal gas using the first law (answer: $nR$, derivable from $dU = \delta Q - p\, dV$ and the equation of state), and (3) verify that the *non-exactness* of $\delta Q$ is the content of "heat is not stored", whereas the exactness of $dU$ is the content of "energy is stored".

---

# Unlocked by This

> [!tip] Maxwell Relations and Thermodynamic Potentials *(from this topic)*
> The exactness of $dU$ — and the corresponding exactness of $dH$, $dF$, $dG$ for the Legendre-transformed potentials — is what enables the [[Thm - Maxwell Relations from Closedness|Maxwell relations]] $(\partial T/\partial V)_S = -(\partial p/\partial S)_V$ etc. These are simply $d^2 = 0$ applied to the exact differentials, and they are the workhorse identities of thermodynamic computations. See [[Def - Thermodynamic Potential (U, H, F, G)]].

> [!tip] The Second Law as the Existence of a Second State Function *(from this topic)*
> The first law gives one state function $U$. The second law, via [[Thm - Caratheodory's Theorem on the Second Law|Caratheodory's theorem]], gives a second state function $S$ (entropy) defined up to constants. With $U$ and $S$ in hand, the equilibrium thermodynamics of a simple system is essentially complete: every other equilibrium-state quantity is a function of $U$ and the volume coordinates, and every Maxwell relation follows from $d^2 = 0$ on $U$ and its Legendre transforms.

> [!tip] Conservation of Energy in General Relativity *(from General Relativity)*
> In **general relativity**, the analogue of the first law is the divergence-free condition $\nabla_\mu T^{\mu\nu} = 0$ on the stress-energy tensor — automatic from the Bianchi identity on Einstein's equations. Energy conservation in GR is subtler because *global* energy is not well-defined on a non-asymptotically-flat spacetime (no globally defined timelike Killing vector), and the first-law analogue at the horizon of a black hole becomes the **first law of black hole mechanics** $dM = (\kappa/8\pi) dA + \Omega\, dJ + \Phi\, dQ$, with surface gravity $\kappa$ playing the role of temperature and horizon area $A/4$ the role of entropy (the **Bekenstein-Hawking entropy**). The structural parallel with the thermodynamic first law is the seed of **black hole thermodynamics**.

> [!tip] Information-Theoretic Conservation Laws *(from Information Theory)*
> The first law has an informational analogue: the **information** in a system, suitably defined, is conserved under reversible (unitary in quantum mechanics) dynamics. Erasing one bit of information dissipates at least $k_B T \log 2$ of heat (**Landauer's principle**), tying information loss to heat generation. **Maxwell's demon** scenarios are resolved by including the demon's information storage in the energy ledger — the apparent violation of the second law disappears once the demon's bookkeeping is paid for in heat. The active research area **Maxwell's demon and algorithmic thermodynamics** investigates these ideas in the setting of **algorithmic information theory**, where the relevant "information" is Kolmogorov complexity rather than Shannon entropy.
