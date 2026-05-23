---
type: definition
subject: thermodynamics
prereqs:
  - "Def - Heat 1-Form and Work 1-Form"
  - "Def - Quasistatic Process"
  - "Def - Distribution on a Manifold"
  - "Def - Integral Manifold of a Distribution"
tags: [physics, thermodynamics, differential-geometry]
---

# Notation

$M^{n+1}$ is the [[Def - Thermodynamic State Space|thermodynamic state space]]; $\delta Q$ is the [[Def - Heat 1-Form and Work 1-Form|heat 1-form]], a smooth nowhere-vanishing 1-form. $\ker \delta Q \subset TM$ denotes the kernel of $\delta Q$ as a smooth $n$-plane field on the $(n+1)$-dimensional $M$ — the adiabatic distribution. A quasistatic adiabatic process is a smooth path $\gamma$ with $\delta Q(\dot\gamma) = 0$. See [[Thermodynamics I — Caratheodory's Approach to the Second Law]] for the full registry.

This is a compound page: it defines two interlocking notions — the **adiabatic process** (a 1-dimensional object, a path) and the **adiabatic distribution** (an $n$-dimensional object, a plane field) — because they are the same physical concept viewed at two different scales: a process is an integral curve of the distribution.

---

# Axiom Motivation

The motivation here is to capture the physical notion of "no heat exchanged" — a process during which the system is thermally isolated from its surroundings — as a *geometric* constraint on paths in the state space. Once this is done, the question "are all states accessible by such processes?" becomes the integrability question for the corresponding distribution, and Caratheodory's principle becomes a constraint on the geometry of $M$.

The first design choice: define adiabatic as $\delta Q(\dot\gamma) = 0$ at every instant of $\gamma$, not merely as $\int_\gamma \delta Q = 0$. The integral form is weaker — it requires only that net heat exchanged be zero, not that no heat be exchanged at any instant. A process with $\int \delta Q = 0$ might absorb heat in one part and release it in another, with no net exchange; this is not what "adiabatic" means physically. Adiabatic means *thermally insulated throughout*, so $\delta Q$ vanishes pointwise. This is the natural condition because thermal insulation is a property of the system's interaction with its environment at each instant, not a path-averaged property.

The second design choice: the *adiabatic distribution* $\ker \delta Q$ is then the natural geometric object — the codimension-one plane field annihilated by $\delta Q$ at each point. A path is adiabatic iff its tangent at every point lies in $\ker \delta Q$, i.e., iff $\gamma$ is an [[Def - Integral Manifold of a Distribution|integral curve]] of the distribution. (One-dimensional integral curves of a higher-rank distribution always exist; the question Caratheodory cares about is whether higher-dimensional *integral submanifolds* exist, i.e., whether $\ker \delta Q$ is integrable.)

Why does the *codimension* of $\ker \delta Q$ matter? Because the distribution has codimension one, the natural "integrability question" is whether $M$ is foliated by codimension-one submanifolds (adiabatic surfaces). If $\ker \delta Q$ were integrable, these surfaces would partition $M$, and any two states on the same surface would be connected by adiabatic paths while states on different surfaces would not be. The function whose level sets are these surfaces would be the entropy. So the entire structure of entropy hinges on whether $\ker \delta Q$ is integrable, and the codimension-one structure (one constraint, one resulting state function) is what makes the entropy a single number rather than a multidimensional object.

Why does the assumption $\delta Q \neq 0$ everywhere matter? Because it ensures $\ker \delta Q$ has constant rank $n$ everywhere — the distribution is smooth, with no points where its rank jumps. If $\delta Q$ vanished at some point $x$, then $\ker \delta Q$ would be all of $T_x M$ at $x$ (rank $n+1$) and only $n$-dimensional elsewhere; the distribution would not be a smooth field of $n$-planes and Frobenius's theorem would not apply at the singular point. Physical systems have $\delta Q \neq 0$ everywhere precisely because every equilibrium state can absorb or release heat by some infinitesimal process — heat is a "fundamental" exchange mode.

The naturalness of this distribution-based formulation is what makes Caratheodory's approach work. By converting "no heat exchanged" into "tangent lies in $\ker \delta Q$", and by converting "states are inaccessible" into "$\ker \delta Q$ is integrable", Caratheodory reduces the second law to a single geometric question — and the [[Thm - The Frobenius Theorem|Frobenius theorem]] answers it. Other formulations of the second law (Kelvin's, Clausius's) are physically natural but geometrically opaque; Caratheodory's is the version that makes the geometry transparent.

---

# The Definition

Let $M^{n+1}$ be a [[Def - Thermodynamic State Space|thermodynamic state space]] and $\delta Q$ the [[Def - Heat 1-Form and Work 1-Form|heat 1-form]] (smooth and nowhere vanishing). Then:

**(1) Adiabatic distribution.** The **adiabatic distribution** on $M$ is the smooth $n$-plane field $\Delta \subset TM$ defined by

$$\Delta_x := \ker \delta Q|_x = \{ v \in T_x M : \delta Q_x(v) = 0\}.$$

Since $\delta Q$ is nowhere zero, $\Delta_x$ has dimension exactly $n$ at every $x \in M$, making $\Delta$ a smooth codimension-one [[Def - Distribution on a Manifold|distribution]] on $M$.

**(2) Adiabatic process (quasistatic).** A **quasistatic adiabatic process** is a smooth path $\gamma : [a, b] \to M$ satisfying

$$\delta Q(\dot\gamma(t)) = 0 \quad \text{for all } t \in [a, b],$$

equivalently $\dot\gamma(t) \in \Delta_{\gamma(t)}$ at every $t$. Such a path is a 1-dimensional [[Def - Integral Manifold of a Distribution|integral curve]] of $\Delta$.

**(3) Adiabatic process (non-quasistatic).** A **non-quasistatic adiabatic transition** is a pair $(x, y)$ of equilibrium states such that the system can be brought from $x$ to $y$ while thermally insulated from its surroundings, but via a (possibly violent, non-equilibrium) process whose intermediate states are not in $M$. The canonical examples are *stirring at constant volume* (irreversible work input as heat) and *free expansion* (irreversible volume increase with no work or heat).

**(4) Adiabatic surface.** If $\Delta$ is integrable (the content of Caratheodory's theorem, given Caratheodory's principle), then $M$ is foliated by codimension-one submanifolds called **adiabatic surfaces**. Each adiabatic surface is a maximal connected integral submanifold of $\Delta$; the function whose level sets are these surfaces is (locally) the entropy.

---

# Relate to Other Fields / Compression

The adiabatic distribution is the **physical instance of a codimension-one Pfaffian constraint** — the same kind of structure that appears in [[Differential Geometry X — de Rham Cohomology, Distributions, and Frobenius|DG X §10.3]] as the input to Frobenius's theorem. The integrability question is identical: when is a single-Pfaffian distribution integrable? The answer, $\delta Q \wedge d(\delta Q) = 0$, is the same in both contexts. The thermodynamic application is special only in that the integrability is *not* automatic and must be derived from a physical hypothesis (Caratheodory's principle).

**True name:** The adiabatic distribution is **the field of "directions of zero heat exchange" at each equilibrium state**. A path tangent to this distribution exchanges no heat; the entropy along it is constant. Whether such paths fill out submanifolds (adiabatic surfaces) is the central question.

In sub-Riemannian geometry, the adiabatic distribution would be called a **horizontal distribution** and the adiabatic paths **horizontal curves**. The question Chow's theorem answers — when are all points connected by horizontal curves? — is exactly the question Caratheodory asks (with the answer "no" being the input that produces entropy).

---

# Examples / Corollaries

**Is an instance: an ideal gas's adiabatic distribution.** With $M = \{(V, T) : V, T > 0\}$ and $\delta Q = (f/2) nR\, dT + (nRT/V)\, dV$, the kernel $\ker \delta Q$ is the line field whose tangent at $(V, T)$ satisfies $(f/2) nR\, dT + (nRT/V)\, dV = 0$, i.e., $dT/T = -(2/f)\, dV/V$. Integrating, $T V^{2/f} = \text{const}$, the adiabatic equation. These curves foliate $M$, and the function $TV^{2/f}$ is (up to a constant) the entropy of the ideal gas.

**Is an instance: heating at constant volume is NOT adiabatic.** Along an isochore $dV = 0$, $\delta Q = (f/2) nR\, dT \neq 0$ when $dT \neq 0$. So heating at constant volume exchanges heat — which is the whole point. The fibres of $\pi : M \to V$ are everywhere transverse to the adiabatic distribution.

**Is an instance: stirring at constant volume (non-quasistatic adiabatic).** Insulating the gas and stirring with a paddle increases $U$ (by work input) without exchanging heat. The endpoints are equilibrium states $(V, T_i)$ and $(V, T_f)$ with $T_f > T_i$, but no path in $M$ connects them adiabatically — the stirring trajectory leaves $M$ entirely. The first law gives $\Delta U = W_{\text{stir}}$, with $Q = 0$. This is Frankel's archetypal example of an adiabatic process that is not a path in $M$.

**Is NOT an instance: an isotherm.** Along an isotherm $dT = 0$, $\delta Q = (nRT/V)\, dV \neq 0$ when $dV \neq 0$. Heat flows during isothermal compression or expansion (to keep the temperature constant), so isotherms are not adiabatic. In fact, isotherms and adiabats are *transversal* foliations of an ideal gas's state space — together they form the Carnot grid.

**Calibration check.** If you understand the definition, you should be able to (1) verify that the line field $\ker \delta Q$ on $\mathbb{R}^2$ (for an ideal gas) is automatically integrable because *every* line field on a 2-manifold is integrable (1-dimensional distributions are always integrable, since brackets of multiples of a single vector field land in the same line), (2) explain why on a 3-dimensional state space (e.g., two gas regions) integrability of $\ker \delta Q$ is *not* automatic and requires Caratheodory's principle, and (3) write a non-quasistatic adiabatic transition for an ideal gas using the stirring/free-expansion examples.

---

# Unlocked by This

> [!tip] Frobenius Integrability and the Existence of Entropy *(from this topic)*
> The question "is the adiabatic distribution integrable?" is answered by [[Thm - The Frobenius Theorem|Frobenius's theorem]]: integrability is equivalent to $\delta Q \wedge d(\delta Q) = 0$ identically, equivalently to the existence of locally defined functions $\lambda \neq 0$ and $S$ with $\delta Q = \lambda\, dS$. The function $S$ is the (local) entropy. So **entropy exists locally iff the adiabatic distribution is integrable iff Frobenius's obstruction vanishes**. See [[Thm - The Heat 1-Form is Integrable]] and [[Thm - Existence of Integrating Factor for an Inaccessible Pfaffian]].

> [!tip] Caratheodory's Principle as Integrability Selector *(from this topic)*
> Among nowhere-vanishing 1-forms on $M^{n+1}$, the integrable ones are a *very* special subset (codimension-1 in the space of all such forms, in some appropriate sense). Most random 1-forms have $\theta \wedge d\theta \neq 0$ somewhere. Caratheodory's principle is the physical input that *selects* the integrable forms — the second law literally says "nature gives us an integrable $\delta Q$, not a generic one". This is a deep observation: the second law constrains the geometry of the state space in a precisely measurable way. See [[Def - Caratheodory's Principle (Inaccessibility)]].

> [!tip] Holonomic vs Nonholonomic Constraints *(from Geometric Mechanics)*
> In classical mechanics, **holonomic** constraints (those that arise from algebraic equations $f_i(q) = 0$) are integrable distributions on the configuration space — they reduce the number of degrees of freedom by their codimension. **Nonholonomic** constraints (rolling without slipping, the parallel-parking constraint) are non-integrable distributions: the system retains all its degrees of freedom locally even though the constraint reduces velocities. The adiabatic distribution in thermodynamics is the *holonomic* case (integrable), reducing the dimension of adiabatically accessible states from $n+1$ to $n$; if it were nonholonomic, *all* states would be adiabatically accessible by Chow's theorem and entropy would not exist. The classification holonomic-vs-nonholonomic in mechanics is exactly the integrable-vs-non-integrable classification in geometry. See `Def - Holonomic vs Nonholonomic Constraint` (to be added to DG X via the Frankel completion batch).
