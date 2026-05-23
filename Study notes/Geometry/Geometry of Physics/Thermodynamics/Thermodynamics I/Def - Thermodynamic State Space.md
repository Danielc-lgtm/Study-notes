---
type: definition
subject: thermodynamics
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Immersion, Submersion, and Embedding"
tags: [physics, thermodynamics, differential-geometry]
---

# Notation

$M$, $M^{n+1}$ — the thermodynamic state space; a smooth manifold of dimension $n+1$. $V^n$ — the mechanical manifold (volume-coordinate base). $U : M \to \mathbb{R}$ — the internal energy, a globally defined smooth function. $\pi : M \to V$ — the projection submersion onto the mechanical manifold. $p$, $p_i$ — pressures; $v^i$ — volume coordinates; $T$ — empirical temperature. See [[Thermodynamics I — Caratheodory's Approach to the Second Law]] for the full registry.

---

# Axiom Motivation

The first thing to settle in thermodynamics is *what kind of object* a thermodynamic state is, because the entire formal apparatus — heat, work, entropy, temperature, the laws — is built on top of "the set of equilibrium states of a system". The classical answer, which Caratheodory and Frankel both adopt, is that this set is a **smooth manifold**, and the entire machinery of differential geometry then becomes available to discuss it. The axioms behind this choice are worth unpacking, because each captures a non-trivial physical assumption.

The first demand is that we restrict attention to **equilibrium states**. A thermodynamic system has, in principle, an enormous number of microscopic degrees of freedom — for a litre of gas, on the order of $10^{23}$ molecular positions and velocities — and the state space of the *microscopic* system is a $6 \times 10^{23}$-dimensional phase space, far too large to do anything with directly. Equilibrium states are macroscopically distinguishable configurations: collections of microstates that look identical to a macroscopic observer (same volumes, same pressures, same temperatures of each subregion). If we drop this restriction and try to put non-equilibrium states into the state space too, the manifold becomes infinite-dimensional and the formalism collapses; non-equilibrium thermodynamics is a separate, harder subject. The axiom is therefore: **states are equilibrium states only**.

The second demand is **finite-dimensionality**. For a system of $n$ contiguous bags of fluid separated by diathermous membranes (heat-permeable, fluid-impermeable), each bag has an independent volume $v^i$ and a uniform pressure $p_i$ and temperature $T_i$. At thermal equilibrium, the temperatures are equal ($T_1 = \cdots = T_n =: T$) and the equation of state $p_i = p_i(T, v^i)$ eliminates the pressures. What remains is the $n$ volumes and a single temperature, or equivalently the $n$ volumes and a single global internal energy — a total of $n+1$ coordinates. The dimension is forced by the system's macroscopic degrees of freedom. If we dropped the diathermous-membrane assumption (allowing thermal isolation between bags), the dimension would be $2n$ — one temperature plus one volume per bag — but the connectivity of the system would change. Frankel's setup picks the simplest non-trivial case: connected, in mutual thermal equilibrium.

The third demand is the existence of a **globally defined internal energy function** $U : M \to \mathbb{R}$. This is the substantive content of the first law of thermodynamics. Without a global $U$, the first law would only say that *change* in some quantity equals heat minus work — but "change" would refer to a path-dependent integral, not the difference of a state function. The axiom that $U$ is a globally defined smooth function on $M$ is what makes $U$ a *state* function: $U(y) - U(x)$ depends only on $x$ and $y$, not on how the system got from $x$ to $y$. If we dropped this and allowed $U$ to be only locally defined or multivalued, the entire structure of the first law would dissolve — energy would no longer be conserved between equilibrium states, only along specific paths. So $U$ being a globally defined function is the geometric form of "energy is a state function".

The fourth demand is the **submersion** $\pi : M \to V^n$ onto a mechanical manifold of pure volume coordinates, with $\pi$ everywhere of full rank. Physically this says: the volume coordinates alone parametrise an $n$-dimensional submanifold of mechanical configurations, and the extra coordinate "above each $v$" is the internal energy (or equivalently the temperature). The submersion structure is what lets us speak of "heating at constant volume" — moving along a fibre $\pi^{-1}(v)$ — and "doing work" — moving along the base $V^n$. If $\pi$ failed to be a submersion at some point, the volumes would not be independent coordinates there and the formalism would break down. The full-rank condition is a transversality demand: the volume coordinates and the energy coordinate must be everywhere independent.

A reader who is sceptical of the manifold axiom should note what would go wrong without it: thermodynamics could no longer use differential forms, the first and second laws could not be written as equations among 1-forms ($dU = \delta Q - \delta W$, $\delta Q = T\, dS$), and the integrability condition that produces entropy would have no formulation. Caratheodory's entire achievement is to convert thermodynamics into geometry; the price of admission is the manifold axiom.

---

# The Definition

A **thermodynamic state space** of dimension $n+1$ is the data:

1. A smooth manifold $M^{n+1}$, whose points are the equilibrium states of the system.
2. A smooth manifold $V^n$, the **mechanical manifold**, and a smooth submersion $\pi : M \to V$ that is everywhere of full rank. The fibres $\pi^{-1}(v)$ are 1-dimensional embedded submanifolds, and each fibre is assumed connected.
3. A globally defined smooth function $U : M \to \mathbb{R}$, the **internal energy**, whose restriction to each fibre $\pi^{-1}(v)$ is a diffeomorphism onto its image (so $U$ parametrises each fibre).

Local coordinates on $M$ are typically of the form $(v^1, \ldots, v^n, U)$ where $v^1, \ldots, v^n$ are coordinates on $V$ pulled back via $\pi$ and $U$ is the energy. Alternative coordinates on a single fibre include the temperature $T$, with $U$ and $T$ related by the equation of state and the heat capacities.

---

# Relate to Other Fields / Compression

A thermodynamic state space is a **smooth fibre bundle** over the mechanical manifold $V^n$ with one-dimensional fibres parametrised by the energy coordinate, with extra structure (the global energy function) singling out a section-class. The submersion $\pi$ is the projection of the bundle; "heating at constant volume" is motion along a fibre; "doing reversible work" is motion in the horizontal complement of the fibre (which is *not* a connection — there is no preferred horizontal direction, only the fibre direction is preferred). The data is closer to a *cosphere bundle* or *line bundle* depending on additional structure one imposes.

**True name:** A thermodynamic state space is **the macroscopic manifold whose tangent space at each state encodes the directions in which slow (quasistatic) experimental controls can drive the system**. The dimension $n+1$ is the number of macroscopic controls — $n$ volume-like controls plus one energy-like control (heat input). This is the right way to think about it: the state space is the experimentalist's parameter space, not an abstract manifold.

---

# Examples / Corollaries

**Is an instance: a single ideal gas.** $n = 1$, so $M$ is $2$-dimensional. Coordinates can be taken as $(V, T)$, $(V, p)$, or $(V, U)$; the equation of state $pV = nRT$ and the formula $U = \frac{f}{2} nRT$ for an ideal gas with $f$ degrees of freedom let you convert between them. The mechanical manifold $V^1$ is the half-line $\mathbb{R}_{>0}$ of positive volumes; the fibres $\pi^{-1}(V)$ are the isochores ("heating at constant volume"), parametrised by $T$ or equivalently $U$.

**Is an instance: $n$ ideal gases in contiguous diathermous bags.** $M$ is $(n+1)$-dimensional with coordinates $(v^1, \ldots, v^n, T)$ or $(v^1, \ldots, v^n, U)$; each bag has its own pressure $p_i = n_i R T / v^i$ determined by its volume and the common temperature. The internal energy is $U = \sum_i (f_i/2) n_i R T$. The submersion $\pi : M \to V^n$ projects $(v^1, \ldots, v^n, T) \mapsto (v^1, \ldots, v^n)$.

**Is NOT an instance: a system at a phase transition.** At a first-order phase transition (e.g., water at $100^\circ$C and 1 atm), the heat capacity diverges and the smoothness of $M$ breaks down — the manifold structure has a corner or cusp. Classical thermodynamics as developed here applies only on the smooth regions away from phase boundaries. To handle phase transitions one passes to a singular extension of the manifold or works with the convex envelope of the entropy function. This is the principal way the smooth-manifold axiom fails in practice.

**Is NOT an instance: a system out of equilibrium.** A gas in the middle of a turbulent expansion has microscopic states that are not at any well-defined temperature or pressure; it is not a point of $M$ at all. Such states do exist in physics but require a much larger (infinite-dimensional) configuration space.

**Calibration check.** If you have understood the definition, you should be able to (1) name the dimension of the state space for two ideal gases separated by a diathermous membrane (answer: $3$), (2) write down the submersion $\pi$ explicitly in coordinates for the single ideal gas case ($\pi(V, T) = V$), and (3) explain why the assumption that fibres of $\pi$ are connected is what lets you reach any state at constant volume by heating or cooling from any other state on the same isochore.

---

# Unlocked by This

> [!tip] Heat 1-Form and Adiabatic Distribution *(from this topic)*
> Once $M$ is a manifold, the cotangent space $T^*_x M$ exists and one can speak of 1-forms on $M$. The heat 1-form $\delta Q$ and work 1-form $\delta W$ are smooth nowhere-vanishing 1-forms on $M$, and the [[Def - Adiabatic Process and Adiabatic Distribution|adiabatic distribution]] $\ker \delta Q$ is a smooth codimension-one distribution. The integrability question for this distribution — the Frobenius question — is what produces the entropy. The state-space-as-manifold axiom is what makes all of this even formulable.

> [!tip] Statistical Mechanics and the Coarse-Graining Question *(from Statistical Mechanics)*
> The macroscopic state manifold $M^{n+1}$ is a vast coarse-graining of the microscopic phase space $\Gamma^{6N}$ for $N \sim 10^{23}$ particles. Each point of $M$ corresponds to a set of microstates in $\Gamma$ — a **macrostate**. The question of *which* coarse-graining to choose is part of what statistical mechanics has to specify, and different choices give different effective entropies. The standard choice (Boltzmann/Gibbs) gives the entropy of this chapter; alternative choices (e.g., counting only microstates indistinguishable by a specified set of macroscopic observables) lead to **subjective entropy** and ultimately to **information-theoretic entropy** and the **maximum-entropy principle**.

> [!tip] Black Hole Thermodynamics *(from General Relativity)*
> For black holes, the "thermodynamic state space" is parametrised by mass $M$, charge $Q$, and angular momentum $J$ (the no-hair theorem). The **Bekenstein-Hawking entropy** $S = A/4$ (in natural units) makes the horizon area into an entropy function on this finite-dimensional state space, and the four **laws of black hole mechanics** mirror the laws of thermodynamics — providing one of the most striking instances of the state-space-as-manifold paradigm in a context where the underlying microstates are not classically definable. This is the seed of **holography** and one of the deepest puzzles in modern physics.
