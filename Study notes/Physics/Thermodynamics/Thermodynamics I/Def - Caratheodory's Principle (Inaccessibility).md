---
type: definition
subject: thermodynamics
prereqs:
  - "Def - Adiabatic Process and Adiabatic Distribution"
  - "Def - Thermodynamic State Space"
tags: [physics, thermodynamics]
---

# Notation

$M^{n+1}$ is the [[Def - Thermodynamic State Space|thermodynamic state space]]. A state $y \in M$ is **adiabatically accessible** from $x \in M$ if there exists a piecewise smooth quasistatic path $\gamma$ from $x$ to $y$ with $\delta Q(\dot\gamma) = 0$ everywhere — an integral curve of the [[Def - Adiabatic Process and Adiabatic Distribution|adiabatic distribution]] $\ker \delta Q$. We allow $y$ to be at the end of a *broken* sequence of such curves (changing tangent direction at corners), corresponding to physical adiabatic processes that change direction in state space. See [[Thermodynamics I — Caratheodory's Approach to the Second Law]] for the full registry.

---

# Axiom Motivation

Caratheodory's principle is one of several logically equivalent (or weaker, in this case) axiomatic formulations of the second law of thermodynamics. To motivate why this particular formulation matters, it helps to see what the alternatives are and why this one is the one that connects cleanly to differential geometry.

The **Kelvin formulation** says: *no cyclic process can absorb heat from a single reservoir and convert it entirely into work*. Physically natural — it forbids the perpetual-motion machine of the second kind — but mathematically opaque. It mentions cycles, single reservoirs, heat-to-work conversion, none of which are obviously geometric concepts. The **Clausius formulation** is similar: *no process can transfer heat from a colder to a hotter body without other compensating changes*. Also physically natural, also mathematically opaque.

Caratheodory's formulation, in 1909, is purely geometric: **in every neighbourhood of every equilibrium state, there exist other states that cannot be reached from the original by any adiabatic process**. No cycles, no reservoirs, no engines — just a statement about which paths in $M$ exist. The reason this matters is that it converts the second law into a constraint on the geometry of the adiabatic distribution, and Frobenius's theorem then converts that constraint into the existence of entropy.

The first design choice in Caratheodory's principle is *adiabatic*. Why focus on adiabatic processes specifically? Because adiabatic processes are the ones controlled entirely by the system's geometry — they are the integral curves of $\ker \delta Q$, with no reference to the surroundings beyond "no heat exchange". If you ask "which states are accessible from $x$ via *arbitrary* quasistatic processes?", the answer is "all of them" (you can heat or cool freely), which is geometrically vacuous. If you ask "which states are accessible via *isothermal* processes?", you tie the system to an external reservoir, which is unphysical to assume always exists. Adiabatic accessibility is the geometric question: which states does the *intrinsic* structure of $M$ and $\delta Q$ permit you to reach?

The second design choice is *in every neighbourhood of every state*. Why this local form? Because integrability is a local condition — Frobenius's theorem produces local integral submanifolds. The contrapositive of Chow's theorem (which Caratheodory uses) tells us that if a distribution is *not* integrable, then locally *all* nearby points are reachable by horizontal paths. So requiring that some nearby points be inaccessible — locally, in every neighbourhood — is exactly enough to force integrability. A global "some pair of states is inaccessible" would be weaker and would not directly give integrability.

The third design choice is to allow *piecewise smooth* paths (with corners). Smooth paths alone might not be enough to reach all of the integrable foliation's leaf through $x$; physical adiabatic processes can change direction (cooling then heating along different curves). Allowing corners makes "adiabatically accessible" coincide with "on the same maximal leaf" (after Caratheodory's theorem is applied), which is the right physical equivalence class. This also matches the Chow-theorem setup, which considers piecewise-smooth horizontal paths.

Why is Caratheodory's principle *weaker* than Kelvin's? Because Kelvin's principle (no cyclic heat-to-work conversion from a single reservoir) directly implies that adiabatic processes cannot mix arbitrarily — specifically, if states $x$ and $y$ are connected by an isochore ($\pi(x) = \pi(y)$) with $U(x) > U(y)$, then there is no quasistatic adiabatic path from $x$ to $y$ (a short argument given in [[Thm - Caratheodory's Theorem on the Second Law#Why Is It True|the theorem's "Why Is It True" section]]). This produces inaccessible states in every neighbourhood: the isochore through $x$ contains states arbitrarily close to $x$ that are not adiabatically accessible from $x$. So Kelvin implies Caratheodory. The converse is not obvious — Caratheodory's principle could in principle be true without ruling out all single-reservoir cycles — but for "simple" thermodynamic systems, the two are equivalent.

The remarkable feature of Caratheodory's principle is that it is enough. Combined with Chow's theorem and Frobenius's theorem, this seemingly weak local statement produces the full machinery of entropy and absolute temperature. The conversion is the content of [[Thm - Caratheodory's Theorem on the Second Law]].

---

# The Definition

**Caratheodory's principle (the second law of thermodynamics, Caratheodory's formulation).** Let $M^{n+1}$ be a [[Def - Thermodynamic State Space|thermodynamic state space]] with [[Def - Heat 1-Form and Work 1-Form|heat 1-form]] $\delta Q$. Then:

*In every open neighbourhood $U$ of every equilibrium state $x \in M$, there exists a state $y \in U$ that is not adiabatically accessible from $x$ — that is, there is no piecewise smooth quasistatic path $\gamma : [a, b] \to U$ with $\gamma(a) = x$, $\gamma(b) = y$, and $\delta Q(\dot\gamma) = 0$ everywhere.*

Equivalently: the [[Def - Adiabatic Process and Adiabatic Distribution|adiabatic distribution]] $\ker \delta Q$ is *not* horizontally connecting in any open subset of $M$ — there are local obstructions to adiabatic accessibility.

This is a *physical axiom*, not a theorem; it is one of several equivalent forms of the second law of thermodynamics, distinguished by being purely geometric (no engines, cycles, or reservoirs). It is taken as input to [[Thm - Caratheodory's Theorem on the Second Law]], which derives integrability of $\ker \delta Q$ from it.

---

# Relate to Other Fields / Compression

Caratheodory's principle is the **physical input that selects integrable codimension-one distributions from among all codimension-one distributions**. In the language of sub-Riemannian geometry, it says the adiabatic distribution is *not* bracket-generating — there exists no local "horizontal connectivity". By Chow's theorem's contrapositive (in the codimension-one case), this forces integrability.

**True name:** Caratheodory's principle is **the geometric version of the second law**: there are local obstructions to adiabatic accessibility, encoded as the existence of nearby inaccessible states. The integrability of $\ker \delta Q$, the existence of entropy, and the irreversibility of stirring all flow from this single assumption.

In control theory, Caratheodory's principle is a **non-controllability statement**: the "control system" whose accessible states from $x$ are exactly the adiabatically reachable states from $x$ is *not locally controllable*. The integrability conclusion is the control-theoretic dual of Chow's bracket-generation criterion.

---

# Examples / Corollaries

**Is an instance: Caratheodory's principle holds for an ideal gas.** Take an ideal gas state $(V_0, T_0)$. Adiabats are curves $TV^{2/f} = \text{const}$. The adiabat through $(V_0, T_0)$ is a 1-dimensional curve in the 2-dimensional state space; *all* nearby states off this curve (which is most of the neighbourhood) are not adiabatically accessible from $(V_0, T_0)$. So inaccessible states abound in every neighbourhood — Caratheodory's principle holds trivially in 2 dimensions, as the codimension of $\ker \delta Q$ is 1 and the curve through any point obviously misses most of a 2-dimensional neighbourhood.

**Is an instance: Caratheodory's principle for two gas regions.** Take a state space $M = \{(V_1, V_2, T)\}$ for two ideal gas regions in mutual thermal contact at common temperature $T$. The adiabatic distribution is 2-dimensional in this 3-dimensional space. Caratheodory's principle says nearby states are not all reachable by 2-dimensional adiabatic motion — and indeed, for an integrable distribution they are not, since the adiabatic leaves are 2-dimensional surfaces and any neighbourhood of a leaf contains states on adjacent leaves.

**Is NOT an instance: Caratheodory's principle for Frankel's contact-form example.** Take $\theta = y\, dx - x\, dy + dz$ on $\mathbb{R}^3$ (the standard contact form, treated as a hypothetical "heat 1-form"). Compute $\theta \wedge d\theta = -2\, dx \wedge dy \wedge dz \neq 0$. By Chow's theorem (or direct construction with broken integral curves), *every* point of $\mathbb{R}^3$ is reachable from the origin by piecewise horizontal paths. So Caratheodory's principle *fails* for $\theta$. A thermodynamic system with this $\delta Q$ would violate the second law and have no entropy. See [[Ex - Non-Integrability of a Hypothetical Adiabatic Distribution (Counterexample)]].

**Is NOT an instance: Caratheodory's principle for $\delta Q$ defined as $dT$ (trivial heat form).** If we (silly hypothetical) set $\delta Q := dT$, an exact form, then the adiabatic distribution is the kernel of $dT$ — the codimension-one distribution where temperature is constant. This is trivially integrable (since $dT$ is exact), the leaves are the isotherms, and Caratheodory's principle holds (states off the isotherm through $x$ are not adiabatically accessible). The integrating factor is $\lambda = 1$ and "entropy" is just $T$. This is a degenerate case where the second law is satisfied but trivially — no information beyond temperature is needed to label adiabats. Real $\delta Q$ is more complicated and the entropy carries genuine new information.

**Calibration check.** If you understand Caratheodory's principle, you should be able to (1) state why it is trivially true in 2-dimensional state spaces (1-dimensional distributions are always integrable, so accessibility is along a 1-curve and most of the neighbourhood is off-curve), (2) explain in your own words why Kelvin's principle implies Caratheodory's (the argument: if states $x, y$ on the same isochore had $y$ adiabatically accessible from $x$ then heat could be taken in along the isochore from $y$ to $x$ and converted to work along the adiabatic path $x \to y$, violating Kelvin), and (3) sketch the geometric picture: adiabatic accessibility from $x$ traces out a connected subset of $M$, and Caratheodory says this subset always misses points in every neighbourhood of $x$.

---

# Unlocked by This

> [!tip] Caratheodory's Theorem on the Second Law *(from this topic)*
> The principle is the input to [[Thm - Caratheodory's Theorem on the Second Law]], which states that Caratheodory's principle implies $\delta Q \wedge d(\delta Q) = 0$ — the Frobenius integrability condition for $\ker \delta Q$. From there, locally $\delta Q = T\, dS$ and entropy exists.

> [!tip] Chow's Theorem (Contrapositive) *(from Sub-Riemannian Geometry)*
> The proof of the Caratheodory–Frobenius theorem uses [[Thm - Chow's Connectivity Theorem (Statement)|Chow's theorem]] in contrapositive form: if a distribution is *bracket-generating* on a connected manifold, then every point is reachable by horizontal paths from every other. Caratheodory's principle denies horizontal connectivity, so by Chow $\ker \delta Q$ cannot be bracket-generating — in the codimension-one case, this forces it to be involutive (integrable). The principle is therefore the *Chow-style non-controllability* of the adiabatic distribution.

> [!tip] Lieb-Yngvason Axiomatic Thermodynamics *(from Mathematical Physics)*
> The most rigorous modern axiomatic foundation of thermodynamics, due to Lieb and Yngvason (1999), takes **adiabatic accessibility** as the *primitive* notion and derives the existence of entropy purely from order-theoretic axioms on the accessibility relation $x \prec y$ ("$y$ is adiabatically accessible from $x$"). The entropy $S$ is constructed as the unique (up to affine transformations) monotone function on $M$ satisfying $S(y) \geq S(x)$ iff $x \prec y$, with additivity $S(x \otimes y) = S(x) + S(y)$ for composite systems. Caratheodory's principle is the geometric input that makes this construction nondegenerate; Lieb-Yngvason replace the geometric input with an order-theoretic one. See Lieb & Yngvason, "The Physics and Mathematics of the Second Law of Thermodynamics", *Physics Reports* 310 (1999).
