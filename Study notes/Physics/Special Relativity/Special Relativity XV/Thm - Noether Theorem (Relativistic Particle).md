---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Relativistic Action of a Free Particle"
  - "Def - Generalized Four-Momentum and the Relativistic Hamiltonian"
  - "Def - The Poincaré Group"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Angular Momentum Four-Tensor"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the mostly-minus signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so a timelike worldline has $\eta_{\mu\nu}\dot x^\mu\dot x^\nu > 0$ (Gourgoulhon's source uses mostly-plus, $\mathrm{diag}(-1,+1,+1,+1)$ with the opposite sign throughout). A particle $\mathcal{P}$ has worldline $x^\mu = x^\mu(\lambda)$ parametrised by an arbitrary $\lambda$, with parameter-velocity $\dot x^\mu = dx^\mu/d\lambda$. The Lagrangian is $L(x^\mu, \dot x^\mu)$ and the action is $S = \int_{\lambda_1}^{\lambda_2} L\,d\lambda$ (see [[Def - Relativistic Action of a Free Particle]]). The **generalized four-momentum** is the linear form with components $p_\mu = \partial L/\partial\dot x^\mu$ (see [[Def - Generalized Four-Momentum and the Relativistic Hamiltonian]]). An infinitesimal coordinate change is written $x'^\mu = x^\mu + \varepsilon G^\mu(x)$ with $\varepsilon$ infinitesimal and $G^\mu$ the **generators**; $G = G^\mu e_\mu$ is the associated vector. We write $\dot G^\mu = dG^\mu/d\lambda$. Full registry on [[Special Relativity XV — The Principle of Least Action]].

---

# Statement

> **Theorem (Noether, for a relativistic particle).** Let $\mathcal{P}$ be a particle whose worldline satisfies the Euler–Lagrange equations of a Lagrangian $L(x^\mu, \dot x^\mu)$, and let $x'^\mu = x^\mu + \varepsilon G^\mu(x)$ be a one-parameter family of infinitesimal coordinate changes under which $L$ is **invariant**, in the sense that
> $$L\big(x^\mu + \varepsilon G^\mu,\ \dot x^\mu + \varepsilon\dot G^\mu\big) = L\big(x^\mu, \dot x^\mu\big) + O(\varepsilon^2).$$
> Then the quantity
> $$\frac{\partial L}{\partial \dot x^\mu}\,G^\mu \;=\; p_\mu G^\mu \;=\; \langle P, G\rangle$$
> is **constant along the worldline** of $\mathcal{P}$. In words: every continuous symmetry of the Lagrangian yields a conserved quantity, equal to the generalized four-momentum one-form $P$ evaluated on the generator vector $G$.

> **Corollary (free particle, Poincaré symmetry).** For a free particle, $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ is invariant under the full ten-parameter [[Def - The Poincaré Group|Poincaré group]]. The ten conserved quantities are: the four-momentum $p_\mu = m u_\mu$ (from the four translations), giving conservation of energy $E$ and three-momentum $\mathbf{P}$; the three spatial components $J_{ij}$ of the angular momentum (from the three rotations); and the three components $J_{i0}$ (from the three boosts), equivalent to the centre-of-inertia theorem $x^i - V^i t = \text{const}$.

The conserved quantity is a *one-form contracted with a vector*: $P$ is the four-momentum one-form, $G$ the generator vector pointing along the symmetry direction, and $\langle P, G\rangle = p_\mu G^\mu$ the number they produce — see Why Is It True.

---

# Motivation

The two preceding chapters established the conservation of four-momentum and of angular momentum for a free particle, each by its own dynamical argument: four-momentum is conserved because the worldline is straight, angular momentum because the four-momentum is constant and the position grows linearly. These are correct but unsatisfying — they look like coincidences, two separate facts about free motion. Noether's theorem reveals that they are not coincidences at all but two faces of one principle: each is the conserved charge of a symmetry of spacetime.

The question the theorem answers is structural. Given that the laws of physics are invariant under the Poincaré group — translations in time and space, rotations, boosts — what must be true of the *solutions*? The answer is that each one-parameter symmetry pins down a quantity that cannot change as the particle moves. Translation invariance in time forces energy to be conserved; translation invariance in space forces momentum to be conserved; rotation invariance forces angular momentum to be conserved; boost invariance forces the centre of mass to move uniformly. The symmetries of the arena dictate the conservation laws of its inhabitants.

This is one of the great unifying insights of theoretical physics, and its importance far outruns the single-particle case treated here. The same theorem, generalised from a one-dimensional integral (over the worldline parameter) to a four-dimensional integral (over spacetime), is what produces the conserved currents and the energy-momentum tensor of field theory; it is the reason every symmetry of a Lagrangian field theory comes with a conservation law, and the reason gauge symmetries come with charge conservation. The relativistic particle is the simplest instance, where the machinery is fully visible and the conserved quantities are the familiar ones. Mastering it here is mastering the prototype of a tool used everywhere downstream.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "the Lagrangian is invariant under a one-parameter family $x'^\mu = x^\mu + \varepsilon G^\mu$." The art of applying it lies in recognising the many disguises an invariance wears.

The first disguised source is **"the Lagrangian does not depend explicitly on a particular coordinate $x^{\mu_0}$."** A cyclic coordinate is the simplest symmetry: if $\partial L/\partial x^{\mu_0} = 0$, then $L$ is invariant under translation in $x^{\mu_0}$, the generator being $G^\mu = \delta^\mu_{\;\mu_0}$, and the conserved quantity is $p_{\mu_0}$ itself. The bridge is that "absence from $L$" *is* "translation invariance in that direction." *Example problem:* for a particle in a static field whose potential one-form $A$ is time-independent, $L$ has no explicit $t$, so the energy $p_0$ is conserved — the relativistic statement of energy conservation in a static field.

The second disguised source is **"the configuration is invariant under a geometric transformation of spacetime."** Rotational symmetry of a central field, axial symmetry about an axis, boost symmetry of a translationally-invariant configuration — each is a one-parameter subgroup of the Poincaré (or Lorentz) group leaving the Lagrangian unchanged, and each has a generator $G^\mu = M^\mu_{\;\nu}x^\nu$ built from the corresponding Lie-algebra matrix $M$. The bridge is the identification of geometric symmetries with elements of the [[Def - Lie Algebra of the Lorentz Group|Lorentz Lie algebra]]. *Example problem:* a particle in a field with axial symmetry about the $z$-axis conserves the angular momentum $J_{xy} = x p_y - y p_x$, read off from the rotation generator.

The third disguised source is **"the action differs by a boundary term under the transformation."** The strict hypothesis $L(x',\dot x') = L(x,\dot x)$ can be relaxed: if the Lagrangian changes by a total derivative, $\delta L = \varepsilon\,dF/d\lambda$, the action changes only by the fixed endpoints and the equations of motion are still invariant, yielding a modified conserved quantity $p_\mu G^\mu - F$. The bridge is that the equations of motion, not the Lagrangian itself, are what a symmetry must preserve. *Example problem:* gauge transformations of the electromagnetic potential, $A \mapsto A + d\chi$, change the interaction Lagrangian by the total derivative $\tfrac{q}{c}\,d\chi/d\lambda$, and the corresponding conserved quantity is the gauge-invariant kinetic momentum.

**Targets (Output Amplification)**

The conclusion is "$p_\mu G^\mu$ is conserved."

Combine the conclusion with **the ten generators of the Poincaré group**. Running $G$ over the full ten-dimensional [[Def - The Poincaré Group|Poincaré]] Lie algebra produces ten independent conserved quantities at once — not one conservation law but the complete set for a free particle. The further result is that the conserved quantities organise into two tensors: the four-momentum one-form $p_\mu$ (four translations) and the angular-momentum two-tensor $J^{\mu\nu}$ (three rotations and three boosts). The combination is useful because it derives *all* conservation laws of free relativistic motion from a single theorem applied ten times, replacing ten separate dynamical arguments. *Example:* the entire content of [[Special Relativity XIII — Energy and Momentum]] and [[Special Relativity XIV — Angular Momentum and Spin]] for a free particle.

Combine the conclusion with **the boost generators specifically**. The three boost generators $K_i$ give conserved quantities $J_{i0} = x^i p_0 - x^0 p_i$, and since $p_0 = E$ is itself conserved, dividing by $E$ shows $x^i - (P_i/E)\,t = \text{const}$, i.e. the centre of inertia moves in a straight line at constant velocity. The further result is the **centre-of-inertia theorem**, the relativistic counterpart of the Newtonian theorem that an isolated system's centre of mass moves uniformly. The combination is nonobvious because boost invariance — the equivalence of all inertial frames — looks like a statement about observers, yet it produces a concrete dynamical conservation law. *Example:* the uniform rectilinear motion of an isolated particle, recovered as Noether's boost charge.

Combine the conclusion with **the quantisation map $p_\mu \to i\hbar\,\partial_\mu$**. The classical conserved charges $p_\mu G^\mu$ become, upon quantisation, the *generators* of the symmetry acting on the Hilbert space — the momentum operator generates translations, the angular-momentum operator generates rotations. The further result is that the Casimir invariants built from these generators, $P_\mu P^\mu = m^2$ and the squared Pauli–Lubanski vector, classify the irreducible representations and hence the elementary particles ([[Special Relativity XII — Inertial Observers and the Poincaré Group|Wigner]]). The combination is the bridge from a classical conservation law to the quantum definition of a particle, and it is why Noether's theorem is foundational to quantum field theory.

---

# Why Is It True

The theorem is true for a reason that can be stated in one line and then unpacked: **a symmetry of the Lagrangian means the action is unchanged by sliding the worldline along the symmetry direction, and the Euler–Lagrange equations say the action is also unchanged by any endpoint-fixed wiggle — so the symmetry-slide, which moves the endpoints, can only change the action through a boundary term, and that boundary term is the conserved quantity.**

Take this slowly. The first variation of the action under *any* infinitesimal change of the worldline $\delta x^\mu$ is, after integration by parts,
$$\delta S = \int_{\lambda_1}^{\lambda_2}\Big[\frac{\partial L}{\partial x^\mu} - \frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu}\Big]\delta x^\mu\,d\lambda + \Big[\frac{\partial L}{\partial\dot x^\mu}\delta x^\mu\Big]_{\lambda_1}^{\lambda_2}.$$
This formula holds for any $\delta x^\mu$, whether or not it vanishes at the endpoints. Now feed it the symmetry variation $\delta x^\mu = \varepsilon G^\mu$. Two facts conspire. First, on the physical worldline the Euler–Lagrange bracket vanishes, so the bulk integral is zero — this is where "the worldline satisfies the equations of motion" enters. Second, the symmetry hypothesis says the Lagrangian is unchanged by the variation, so $\delta S = 0$ as well. Setting the surviving boundary term to zero,
$$\Big[\frac{\partial L}{\partial\dot x^\mu}\,\varepsilon G^\mu\Big]_{\lambda_1}^{\lambda_2} = 0,$$
which says the quantity $p_\mu G^\mu$ has the same value at $\lambda_2$ as at $\lambda_1$. Since $\lambda_1$ and $\lambda_2$ were arbitrary points on the worldline, $p_\mu G^\mu$ is constant everywhere along it. That is the whole proof.

The reason the conserved quantity takes the particular form $p_\mu G^\mu$ — a momentum contracted with a generator — is geometric. The generator $G^\mu$ are the components of the vector $G$ pointing in the direction the symmetry pushes spacetime; the generalized momentum $p_\mu$ is a *linear form*, an object built to eat vectors and return numbers. The boundary term in the variation is exactly $p_\mu \delta x^\mu$, the momentum evaluated on the displacement, and for a symmetry the displacement is $\varepsilon G$. So the conserved quantity is $\langle P, G\rangle$, the natural pairing of the momentum one-form with the symmetry vector. This is also why the theorem makes four-momentum's covector nature inescapable: the conserved Noether charge is a pairing, and a pairing needs one object from each of the dual spaces.

The free-particle application is then just bookkeeping over the ten Poincaré generators. The Lagrangian $-m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ depends on $\dot x^\mu$ only through the Lorentz-invariant combination $\eta_{\mu\nu}\dot x^\mu\dot x^\nu$, which is unchanged by any Lorentz transformation, and it does not depend on $x^\mu$ at all, so it is unchanged by any translation. Every Poincaré generator is therefore a symmetry, and Noether's theorem applied ten times gives the ten conservation laws.

---

# What Makes This Hard

The proof itself is short, and the place people stumble is conceptual: the crucial move is to use the *unrestricted* variation formula — the one that keeps the boundary term — and then to supply the two cancellations (equations of motion kill the bulk, symmetry kills $\delta S$) so that only the boundary term survives. The common error is to use the fixed-endpoint variation formula, in which the boundary term has been discarded, and then to find nothing left to identify as the conserved quantity. The non-obvious step is recognising that a symmetry transformation is a variation that *moves the endpoints*, which is exactly why its boundary term is meaningful and is the conserved charge; one must resist the habit, drilled in by the derivation of the Euler–Lagrange equations, of always setting $\delta x^\mu = 0$ at the ends.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Write the invariance hypothesis to first order in $\varepsilon$, then use the Euler–Lagrange equations to rewrite the $\partial L/\partial x^\mu$ term as a total derivative, exposing a perfect $\lambda$-derivative that must vanish. The conserved quantity is what sits inside that derivative.

**Subgoal decomposition:**

1. **Expand the invariance hypothesis to first order.** Show that $L(x + \varepsilon G, \dot x + \varepsilon\dot G) = L(x,\dot x)$ gives $\dfrac{\partial L}{\partial x^\mu}G^\mu + \dfrac{\partial L}{\partial\dot x^\mu}\dot G^\mu = 0$.
   - *Hint:* Taylor-expand in $\varepsilon$, subtract $L(x,\dot x)$, divide by $\varepsilon$.
   - *Why needed:* It turns the symmetry statement into a differential identity involving $G^\mu$ and $\dot G^\mu$.

2. **Replace $\partial L/\partial x^\mu$ using Euler–Lagrange.** On the physical worldline, $\dfrac{\partial L}{\partial x^\mu} = \dfrac{d}{d\lambda}\dfrac{\partial L}{\partial\dot x^\mu}$; substitute this into the identity from step 1.
   - *Hint:* The Euler–Lagrange equation is precisely this equality.
   - *Why needed:* It is the only place the equations of motion enter, and it is what allows the two terms to combine into one derivative.

3. **Recognise a total derivative.** Show that the result of step 2 is $\dfrac{d}{d\lambda}\Big(\dfrac{\partial L}{\partial\dot x^\mu}G^\mu\Big) = 0$.
   - *Hint:* The product rule: $\dfrac{d}{d\lambda}(\frac{\partial L}{\partial\dot x^\mu}G^\mu) = (\frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu})G^\mu + \frac{\partial L}{\partial\dot x^\mu}\dot G^\mu$.
   - *Why needed:* A vanishing total $\lambda$-derivative means the quantity inside is constant along the worldline — the conclusion.

4. **(Free particle) Run $G$ over the Poincaré generators.** With $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ and $\partial L/\partial\dot x^\mu = m u_\mu$, substitute the translation, rotation, and boost generators to obtain $p_\mu = mu_\mu$ conserved, $J_{ij}$ conserved, and $J_{i0}$ conserved.
   - *Hint:* Translation $G^\mu = \delta^\mu_{\;\mu_0}$; rotation/boost $G^\mu = M^\mu_{\;\nu}x^\nu$ with $M$ the Lie-algebra matrix.
   - *Why needed:* It specialises the abstract theorem to the ten concrete conservation laws of free motion.

---

# Lemma Decomposition

> [!note]- Lemma 1: The unrestricted first variation of the action
> **Statement:** For any infinitesimal change $\delta x^\mu(\lambda)$ of the worldline (not necessarily vanishing at the endpoints),
> $$\delta S = \int_{\lambda_1}^{\lambda_2}\Big[\frac{\partial L}{\partial x^\mu} - \frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu}\Big]\delta x^\mu\,d\lambda + \Big[\frac{\partial L}{\partial\dot x^\mu}\delta x^\mu\Big]_{\lambda_1}^{\lambda_2}.$$
>
> **Hint:** Vary $S = \int L\,d\lambda$, use $\delta\dot x^\mu = \tfrac{d}{d\lambda}\delta x^\mu$, and integrate the second term by parts.
>
> **Why needed:** It is the master formula; keeping the boundary term (rather than discarding it as in the Euler–Lagrange derivation) is what makes the conserved quantity visible.
>
> > [!note]- Full proof
> > By definition $\delta S = \int_{\lambda_1}^{\lambda_2}\big[\frac{\partial L}{\partial x^\mu}\delta x^\mu + \frac{\partial L}{\partial\dot x^\mu}\delta\dot x^\mu\big]d\lambda$. Since $\delta\dot x^\mu = \frac{d}{d\lambda}(\delta x^\mu)$, integrate the second term by parts:
> > $$\int_{\lambda_1}^{\lambda_2}\frac{\partial L}{\partial\dot x^\mu}\frac{d(\delta x^\mu)}{d\lambda}\,d\lambda = \Big[\frac{\partial L}{\partial\dot x^\mu}\delta x^\mu\Big]_{\lambda_1}^{\lambda_2} - \int_{\lambda_1}^{\lambda_2}\frac{d}{d\lambda}\Big(\frac{\partial L}{\partial\dot x^\mu}\Big)\delta x^\mu\,d\lambda.$$
> > Substituting back and grouping the two bulk integrands gives the stated formula. $\blacksquare$

> [!note]- Lemma 2: The first-order form of the invariance hypothesis
> **Statement:** Invariance $L(x + \varepsilon G, \dot x + \varepsilon\dot G) = L(x, \dot x) + O(\varepsilon^2)$ is equivalent to $\dfrac{\partial L}{\partial x^\mu}G^\mu + \dfrac{\partial L}{\partial\dot x^\mu}\dot G^\mu = 0$.
>
> **Hint:** Taylor-expand the left side to first order in $\varepsilon$.
>
> **Why needed:** It converts the symmetry assumption into a usable differential identity, the left-hand side of which becomes a total derivative once the equations of motion are invoked.
>
> > [!note]- Full proof
> > Taylor expansion in $\varepsilon$: $L(x + \varepsilon G, \dot x + \varepsilon\dot G) = L(x,\dot x) + \varepsilon\big(\frac{\partial L}{\partial x^\mu}G^\mu + \frac{\partial L}{\partial\dot x^\mu}\dot G^\mu\big) + O(\varepsilon^2)$. Equating to $L(x,\dot x) + O(\varepsilon^2)$, the $O(\varepsilon)$ coefficient must vanish, giving the identity. $\blacksquare$

> [!note]- Lemma 3: The Euler–Lagrange substitution produces a total derivative
> **Statement:** On a worldline satisfying the Euler–Lagrange equations $\frac{\partial L}{\partial x^\mu} = \frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu}$, the identity of Lemma 2 becomes $\dfrac{d}{d\lambda}\Big(\dfrac{\partial L}{\partial\dot x^\mu}G^\mu\Big) = 0$.
>
> **Hint:** Substitute the Euler–Lagrange equation into Lemma 2 and recognise the product rule.
>
> **Why needed:** A vanishing total derivative is exactly the statement that $p_\mu G^\mu$ is conserved — the conclusion of the theorem.
>
> > [!note]- Full proof
> > By Lemma 2, $\frac{\partial L}{\partial x^\mu}G^\mu + \frac{\partial L}{\partial\dot x^\mu}\dot G^\mu = 0$. Replace $\frac{\partial L}{\partial x^\mu}$ by $\frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu}$ (the Euler–Lagrange equation, valid on the physical worldline):
> > $$\Big(\frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu}\Big)G^\mu + \frac{\partial L}{\partial\dot x^\mu}\dot G^\mu = 0.$$
> > The left side is exactly $\frac{d}{d\lambda}\big(\frac{\partial L}{\partial\dot x^\mu}G^\mu\big)$ by the product rule. Hence $\frac{d}{d\lambda}(p_\mu G^\mu) = 0$, so $p_\mu G^\mu$ is constant along the worldline. $\blacksquare$

> [!note]- Lemma 4: The ten Poincaré generators and their charges (free particle)
> **Statement:** For $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$, with $p_\mu = m u_\mu$, the translation generators give $p_\mu = \text{const}$; the rotation generators give $J_{ij} = x_i p_j - x_j p_i = \text{const}$; the boost generators give $J_{i0} = x_i p_0 - x_0 p_i = \text{const}$.
>
> **Hint:** Translation: $G^\mu = \delta^\mu_{\;\mu_0}$. Rotation/boost: $G^\mu = M^\mu_{\;\nu}x^\nu$ with $M$ antisymmetric (when lowered).
>
> **Why needed:** It turns the abstract theorem into the explicit conservation laws of energy, momentum, and angular momentum for free relativistic motion.
>
> > [!note]- Full proof
> > The Lagrangian depends on $\dot x^\mu$ only through $\eta_{\mu\nu}\dot x^\mu\dot x^\nu$, invariant under every Lorentz transformation; and it has no explicit $x^\mu$, so it is invariant under every translation. Hence every Poincaré generator is a symmetry.
> > *Translations:* $x'^\mu = x^\mu + \varepsilon\delta^\mu_{\;\mu_0}$ gives $G^\mu = \delta^\mu_{\;\mu_0}$, so $p_\mu G^\mu = p_{\mu_0}$ is conserved. Running $\mu_0$ over $0,1,2,3$ gives $p_\mu = m u_\mu = \text{const}$: energy $E = p_0$ and three-momentum $\mathbf{P} = (p_i)$ are conserved.
> > *Rotations:* the generator of a rotation in the $i$–$j$ plane is $G^\mu = (J_{[ij]})^\mu_{\;\nu}x^\nu$, with the matrix nonzero only in the $i,j$ block; contracting, $p_\mu G^\mu = x_i p_j - x_j p_i = J_{ij}$, conserved.
> > *Boosts:* the generator of a boost in the $0$–$i$ plane is $G^\mu = (K_i)^\mu_{\;\nu}x^\nu$, giving $p_\mu G^\mu = x_i p_0 - x_0 p_i = J_{i0}$, conserved. Since $p_0 = E$ is itself conserved (translations), dividing $J_{i0} = \text{const}$ by $E$ yields $x^i - (P_i/E)t = \text{const}$, the uniform motion of the centre of inertia. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — well-posedness.** Assume the worldline $x^\mu(\lambda)$ satisfies the Euler–Lagrange equations $\frac{\partial L}{\partial x^\mu} - \frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu} = 0$, and that $L$ is invariant under the one-parameter family $x'^\mu = x^\mu + \varepsilon G^\mu(x)$, meaning $L(x + \varepsilon G, \dot x + \varepsilon\dot G) = L(x,\dot x) + O(\varepsilon^2)$, where $\dot G^\mu = dG^\mu/d\lambda = (\partial G^\mu/\partial x^\nu)\dot x^\nu$.
>
> **Step 1.** Expand the invariance hypothesis to first order in $\varepsilon$ (Lemma 2):
> $$\frac{\partial L}{\partial x^\mu}G^\mu + \frac{\partial L}{\partial\dot x^\mu}\dot G^\mu = 0.$$
>
> **Step 2.** On the physical worldline, the Euler–Lagrange equation gives $\frac{\partial L}{\partial x^\mu} = \frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu}$. Substitute into Step 1 (Lemma 3):
> $$\Big(\frac{d}{d\lambda}\frac{\partial L}{\partial\dot x^\mu}\Big)G^\mu + \frac{\partial L}{\partial\dot x^\mu}\dot G^\mu = 0.$$
>
> **Step 3.** The left-hand side is a total derivative by the product rule:
> $$\frac{d}{d\lambda}\Big(\frac{\partial L}{\partial\dot x^\mu}G^\mu\Big) = 0.$$
> Therefore $\dfrac{\partial L}{\partial\dot x^\mu}G^\mu = p_\mu G^\mu = \langle P, G\rangle$ is constant along the worldline. This is the theorem.
>
> **Step 4 — free particle.** For $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ one computes $\frac{\partial L}{\partial\dot x^\mu} = -m\,\frac{\eta_{\mu\nu}\dot x^\nu}{\sqrt{\eta_{\rho\sigma}\dot x^\rho\dot x^\sigma}} = m u_\mu$ (using $u^\mu = \dot x^\mu/\sqrt{\eta_{\rho\sigma}\dot x^\rho\dot x^\sigma}$, the unit-normalised four-velocity). The Lagrangian is invariant under all ten Poincaré generators (no explicit $x$-dependence gives translation invariance; dependence only through $\eta_{\mu\nu}\dot x^\mu\dot x^\nu$ gives Lorentz invariance). By Lemma 4:
> - translations ($G^\mu = \delta^\mu_{\;\mu_0}$) give $p_{\mu_0} = m u_{\mu_0} = \text{const}$, i.e. $E = \text{const}$ and $\mathbf{P} = \text{const}$;
> - rotations give $J_{ij} = x_i p_j - x_j p_i = \text{const}$;
> - boosts give $J_{i0} = x_i p_0 - x_0 p_i = \text{const}$, equivalently $x^i - (P_i/E)t = \text{const}$.
>
> These are the ten conserved quantities of free relativistic motion, summarised as: invariance of the free Lagrangian under the Poincaré group yields conservation of the four-momentum one-form $P$ (translations) and the angular-momentum two-tensor $J$ (boosts and rotations). $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Conserved currents in classical field theory.** The same theorem, generalised so that the integration parameter $\lambda$ is replaced by the four spacetime coordinates and the worldline by a field configuration, gives Noether's theorem for fields: each continuous symmetry of a Lagrangian density yields a conserved *current* $j^\mu$ with $\partial_\mu j^\mu = 0$. Translation invariance produces the energy-momentum tensor $T^{\mu\nu}$; this is the field-theoretic parent of the particle four-momentum derived here. The application is nonobvious because the particle case hides the current behind a single conserved number, whereas in field theory the current is a spacetime field; see [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

**The moment map in symplectic geometry.** A Lie group acting on a symplectic manifold by symmetries has a moment map $\mu : M \to \mathfrak{g}^*$ whose components are conserved under any invariant Hamiltonian — this is Noether's theorem in geometric form. The ten conserved quantities here are the components of the moment map of the Poincaré action on the particle's phase space. The application is surprising because it recasts a physics conservation law as a purely geometric object, and it is the starting point for symplectic reduction; see the moment-map discussion in [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics]].

**Conserved quantities of geodesic flow from Killing vectors.** On a curved spacetime, a continuous isometry is generated by a Killing vector field $\xi^\mu$, and the quantity $p_\mu\xi^\mu$ is conserved along every geodesic — Noether's theorem for the geodesic Lagrangian, with $\xi$ the generator. This is how conserved energy and angular momentum are extracted for orbits in the Schwarzschild metric, where time-translation and rotation Killing vectors give the conserved energy and angular momentum of a planet. The application is out-of-distribution because the symmetry now belongs to a curved metric, yet the mechanism is identical; see [[General Relativity I — Einstein's Equations and Schwarzschild]].

---

# Bridges

- **[[Def - Four-Momentum and Rest Mass|Four-momentum]]** — the conserved charge of spacetime translations is exactly the four-momentum $p_\mu = m u_\mu$, so this theorem is the variational *explanation* of why four-momentum is conserved for a free particle. The dynamical argument of [[Special Relativity XIII — Energy and Momentum]] (the worldline is straight, so $U$ is constant) and the Noether argument (translation invariance) are two derivations of the same fact; the Noether one explains *why* by tracing it to a symmetry rather than to a solved equation of motion.

- **[[Def - Angular Momentum Four-Tensor|Angular-momentum tensor]]** — the conserved charges of rotations and boosts together fill out the antisymmetric tensor $J^{\mu\nu} = x^\mu p^\nu - x^\nu p^\mu$. The spatial part $J_{ij}$ is ordinary angular momentum (rotation charge); the mixed part $J_{i0}$ is the centre-of-inertia charge (boost charge). The single tensor $J^{\mu\nu}$ unifies "angular momentum" and "centre-of-mass motion" because the Lorentz group unifies rotations and boosts, and Noether's theorem maps that unification onto the conserved quantities; see [[Special Relativity XIV — Angular Momentum and Spin]].

- **The Hamiltonian version of Noether** — in the Hamiltonian formalism (reviewed in [[Thm - Hamiltonian Formulation (Relativistic Particle)]]) the same result reads: a phase-space function $G$ is conserved if and only if the Hamiltonian is invariant under the canonical transformation it generates, expressed through the [[Def - Poisson Bracket|Poisson bracket]] as $\{G, H\} = 0$. The generating function $G$ of an infinitesimal canonical transformation plays the role of the Noether generator, and $dG/d\lambda = \{G, H\}$ vanishes exactly when $G$ generates a symmetry. The Lagrangian and Hamiltonian statements are the same theorem in dual languages.

- **[[Thm - Free-Particle Worldline Extremises Proper Time|The geodesic principle]]** — Noether's theorem presupposes that the worldline satisfies the Euler–Lagrange equations, which for the free particle *is* the geodesic equation. So the conservation laws here are statements about geodesics: a free particle's four-momentum is conserved precisely because its worldline is a geodesic of the (flat) metric, and on a curved metric the analogous conserved quantities require Killing vectors. The theorem and the geodesic principle are the two halves of free-particle dynamics — the equation of motion and its conserved quantities.

---

# Unlocked by This

> [!tip] The Energy-Momentum Tensor as a Noether Current *(from Field Theory)*
> Generalising the one-dimensional worldline integral to a four-dimensional spacetime integral turns this theorem into **Noether's theorem for fields**: translation invariance of a Lagrangian density yields the conserved **energy-momentum tensor** $T^{\mu\nu}$ with $\partial_\mu T^{\mu\nu} = 0$, and Lorentz invariance yields a conserved angular-momentum current. The particle four-momentum and angular-momentum tensor of this page are the integrated, single-particle shadows of these field currents. $T^{\mu\nu}$ is the source of gravity in **general relativity**; see [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy]].

> [!tip] Wigner's Classification of Particles *(from Quantum Field Theory)*
> Quantised, the ten conserved Poincaré charges become the generators of a unitary representation of the **Poincaré group** on a Hilbert space. The two **Casimir invariants** built from them — the mass $P_\mu P^\mu = m^2$ and the spin (the squared Pauli–Lubanski vector $W_\mu W^\mu$) — are constant on each irreducible representation, and **Wigner's theorem** identifies an *elementary particle* with such an irreducible representation, labelled by its mass and spin. The classical conservation laws derived here are the seed: their quantum versions *define* what a particle is. See [[Special Relativity XII — Inertial Observers and the Poincaré Group]].
