---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Noether Current for an Internal Symmetry"
  - "Def - The Lie Algebra of a Lie Group"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Prerequisite Concepts

- [[Def - Noether Current for an Internal Symmetry]]
- [[Def - The Lie Algebra of a Lie Group]]

# Notation

$M$ is a (pseudo-)Riemannian $n$-dimensional manifold (typically $n = 4$, spacetime); $E \to M$ a vector bundle whose fibre carries a representation of a Lie group $G$; $\phi$ a smooth section of $E$, locally $\phi^a(x)$. $\mathcal{L} = \mathcal{L}(\phi, \partial\phi, x)$ is a Lagrangian density, a scalar function of the field, its first derivatives, and the spacetime point.

The action is $S[\phi] = \int_M \mathcal{L}\,\operatorname{vol}_g$. The Euler–Lagrange equations are $\partial_\mu(\partial\mathcal{L}/\partial(\partial_\mu\phi^a)) - \partial\mathcal{L}/\partial\phi^a = 0$.

An **internal symmetry** is a transformation $\phi \to \phi'(\phi)$ acting only on the fibre coordinates (leaving spacetime points fixed) that leaves $\mathcal{L}$ pointwise invariant: $\mathcal{L}(\phi', \partial\phi') = \mathcal{L}(\phi, \partial\phi)$. For a 1-parameter subgroup $g(\alpha) = e^{\alpha E}$ of an internal-symmetry group, the infinitesimal variation is $\delta\phi^a = E^a{}_b\phi^b$ (for some generator $E \in \mathfrak{g}$).

The Noether current is $J^\mu = (\partial\mathcal{L}/\partial(\partial_\mu\phi^a))\,\delta\phi^a$. See [[Def - Noether Current for an Internal Symmetry]].

---

# Statement

> **Theorem (Noether, internal symmetries).** Let $\mathcal{L}(\phi, \partial\phi, x)$ be a Lagrangian density for a field $\phi$ (section of a vector bundle $E \to M$), and let $\delta\phi^a = E^a{}_b\phi^b$ be an infinitesimal *internal symmetry* of $\mathcal{L}$ — a variation that leaves $\mathcal{L}$ pointwise invariant ($\delta\mathcal{L} = 0$) without acting on spacetime coordinates. Then the **Noether current**
> $$J^\mu = \frac{\partial \mathcal{L}}{\partial(\partial_\mu\phi^a)}\,\delta\phi^a$$
> satisfies the conservation law
> $$\partial_\mu J^\mu = 0$$
> for every field $\phi$ that is a solution of the Euler–Lagrange equations (i.e., on shell).

> **Corollary (conserved charge).** If $\phi$ falls off sufficiently fast at spatial infinity, the integrated charge $Q(t) = \int_{V^3(t)} J^0(t, \vec x)\,d^3x$ on any spatial slice $V^3(t)$ is constant in time: $dQ/dt = 0$.

---

# Motivation

Noether's theorem solves the most basic question one can ask about a Lagrangian: given that the action has a continuous symmetry, what does that symmetry *do*? The answer — *it produces a conserved quantity*, with an explicit formula computable from the Lagrangian — is one of the deepest and most general principles in physics. It is the bridge between the algebra of Lie groups (the continuous-symmetry side) and the analysis of conservation laws (the dynamical-consequence side), and it allowed Noether to derive, in a single 1918 paper, the existence of conserved energy, momentum, angular momentum, electric charge, isospin, and every other conserved quantity of physics from the appropriate symmetry of the Lagrangian.

Before Noether, conservation laws were treated as separate axioms of physics — Newton postulated conservation of momentum independently of his force law, and energy conservation was a separate empirical principle. Noether showed that *every* such conservation law arises from a symmetry of the action, with the symmetry generator determining the conserved quantity explicitly. The proof is short, the conclusion is universal, and the implications are vast: a symmetry of $\mathcal{L}$ is not just an aesthetic feature; it is a *forecasting tool* — once you spot a symmetry, you have proven a conservation law.

The internal-symmetry case is the simplest and most directly applicable to gauge theory. External symmetries (translations, rotations, Lorentz transformations) act on spacetime and require the more sophisticated *covariant* Noether construction with the energy-momentum tensor; internal symmetries (phase rotations, isospin rotations, colour rotations) act only on the field components and give the direct current formula $J^\mu = p^\mu_a\,\delta\phi^a$. Both follow from the same variational identity, but the internal case is conceptually cleanest and is what the gauge principle relies on.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis Noether requires is bare: *a continuous internal symmetry of the Lagrangian*. The skill is in recognising, in a problem that mentions no symmetry at all, that an internal symmetry is secretly present. Each of the following is a property $B$ from which the precondition $A$ (symmetry of $\mathcal{L}$) can be extracted.

The most common source is **a Lagrangian written in terms of $|\phi|^2$ or $\phi^\dagger\phi$**. Property $B$ is "$\mathcal{L}$ depends on $\phi$ only through the Hermitian-bilinear combination $\phi^\dagger\phi$", and the bridge is that $\phi^\dagger\phi$ is invariant under $\phi \to e^{i\alpha}\phi$ for any phase $\alpha$. So any Lagrangian of the form $\mathcal{L} = f(\phi^\dagger\phi, \partial_\mu\phi^\dagger\partial^\mu\phi)$ has the global $U(1)$ symmetry $\phi \to e^{i\alpha}\phi$ as a hidden feature — and hence (by Noether) a conserved current. This is the source behind every "charge conservation" theorem in physics: scalar QED, the Klein–Gordon Lagrangian $|\partial\phi|^2 - m^2|\phi|^2$, the Higgs Lagrangian, and so on. The trigger is spotting the bilinear in $\phi$.

A second source is **a Lagrangian whose field $\psi$ is a doublet (or higher) with kinetic and mass terms compatible with a representation of a non-abelian group**. Property $B$ is "$\psi$ is a column vector $(\psi^1, \dots, \psi^N)^T$ and $\mathcal{L} = \bar\psi(i\gamma^\mu\partial_\mu - m)\psi$ with no off-diagonal mixing terms", and the bridge is that the global $SU(N)$ rotation $\psi \to U\psi$ for $U \in SU(N)$ leaves both terms invariant. This is the source behind the **Heisenberg nucleon**: the proton-neutron doublet has approximate $SU(2)$ isospin symmetry, producing three conserved isospin currents. It is also the source behind the **chiral symmetry** of QCD with massless quarks: the doublet structure of quarks of different flavours produces the $SU(N_f) \times SU(N_f)$ chiral group, and its (partial) breaking produces the pions as Goldstone bosons.

A third source is **a Lagrangian invariant under shifting the field by a constant**. Property $B$ is "$\mathcal{L}$ depends on $\partial_\mu\phi$ but not on $\phi$ itself", and the bridge is that $\phi \to \phi + c$ leaves $\mathcal{L}$ invariant for any constant $c$. The corresponding conserved current is $J^\mu = \partial\mathcal{L}/\partial(\partial_\mu\phi)$ — the canonical momentum density. This is the source behind energy and momentum conservation: if $\mathcal{L}$ does not depend explicitly on $t$ (resp. $x^i$), then $\partial/\partial t$ (resp. $\partial/\partial x^i$) is a symmetry, and the conserved current is the energy (resp. momentum) density. (This is technically an external symmetry, not internal, but the variational machinery is analogous.)

**Targets (Output Amplification)**

The conclusion Noether delivers is *one conservation law per independent continuous symmetry*. Combined with one more property $D$, this becomes a more refined structural result.

The most powerful combination is **conservation plus integration over a spatial slice gives a conserved charge**. Add the property $D$ that $\phi$ has compact spatial support (or decays sufficiently fast at infinity), and integrate $\partial_\mu J^\mu = 0$ over the spacetime region $V^3 \times [t_1, t_2]$. Applying Gauss's theorem, the integral becomes $\int_{V^3(t_2)}J^0\,d^3x - \int_{V^3(t_1)}J^0\,d^3x = 0$ (the spatial boundary contributions vanish), so the charge $Q(t) = \int J^0\,d^3x$ is the same at $t_1$ and $t_2$. The result $E$ is a *time-independent number* — the conserved charge — which classically is one of the basic observables of physics and quantum-mechanically becomes a generator of the symmetry on Hilbert space.

A second combination is **conservation of multiple currents satisfying a current algebra**. Add the property $D$ that the symmetry group is non-abelian (so there are multiple generators $T^a$ satisfying $[T^a, T^b] = if^{abc}T^c$). Then there are multiple currents $J^{\mu,a}$ (one per generator), and their *equal-time commutators* form an algebra reproducing the Lie algebra of the symmetry group: $[J^{0,a}(\vec x), J^{0,b}(\vec y)] = if^{abc}J^{0,c}(\vec x)\delta^3(\vec x - \vec y)$. The result $E$ is the **current algebra**, a powerful constraint on the dynamics that has been the basis for many non-perturbative results in QCD (Adler sum rule, Goldberger–Treiman relation, etc.). This combination is non-obvious because conservation of each current individually says nothing about their commutators — the algebraic structure emerges from the structure of the symmetry group.

A third combination is **conservation plus a gauge principle gives an interaction term**. Add the property $D$ that the symmetry should be promoted from global to local. Then by the gauge principle, the Lagrangian must be modified by replacing $\partial_\mu \to D_\mu = \partial_\mu - iqA_\mu$ for a gauge field $A_\mu$. The Noether current $J^\mu$ becomes the *source* of the gauge field in the YM equation $d_A\star F = \star J$. The result $E$ is the structure of the entire fundamental interactions of nature: every conserved current of a global symmetry becomes the source of a gauge boson once the symmetry is gauged. This is the conceptual route from Noether's theorem to the Standard Model.

---

# Why Is It True

The intuition is captured in a single sentence: **invariance of the action under a symmetry, plus the equations of motion, plus integration by parts, force the symmetry's "boundary term" to vanish — and that boundary term is the divergence of the Noether current**.

The argument breaks into three steps that anyone can follow at the whiteboard.

*Step 1 — Write the first variation of the action.* For any variation $\delta\phi$, $\delta S = \int_M\delta\mathcal{L}\,\operatorname{vol}_g = \int_M\left[\frac{\partial\mathcal{L}}{\partial\phi^a}\delta\phi^a + \frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^a)}\partial_\mu(\delta\phi^a)\right]\operatorname{vol}_g$. The second term has a derivative on $\delta\phi$, which obstructs reading off "Euler–Lagrange equations × variation".

*Step 2 — Integrate by parts to pull the derivative off $\delta\phi$.* The second term equals $\int_M\left[\partial_\mu\left(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^a)}\delta\phi^a\right) - \partial_\mu\left(\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^a)}\right)\delta\phi^a\right]\operatorname{vol}_g$. The first part is a total divergence; the second part combines with the original first term to give the Euler–Lagrange operator acting on $\delta\phi$. So the variation organises as
$$\delta S = \int_M\left[\frac{\partial\mathcal{L}}{\partial\phi^a} - \partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^a)}\right]\delta\phi^a\,\operatorname{vol}_g + \int_M \partial_\mu\left[\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^a)}\delta\phi^a\right]\operatorname{vol}_g.$$

*Step 3 — Apply the hypothesis and equations of motion to extract the conservation law.* The first integrand is the Euler–Lagrange operator, which vanishes on solutions ($\phi$ on shell). The second integrand is the divergence of $J^\mu = (\partial\mathcal{L}/\partial(\partial_\mu\phi^a))\delta\phi^a$, the Noether current. So *on shell*, $\delta S = \int_M \partial_\mu J^\mu\,\operatorname{vol}_g$. The hypothesis says $\delta\mathcal{L} = 0$ pointwise (symmetry), so $\delta S = 0$ identically — for *every* region. Since the integral of $\partial_\mu J^\mu$ vanishes over every region of $M$, the integrand must vanish pointwise: $\partial_\mu J^\mu = 0$.

The mechanism in one sentence: **invariance of $\mathcal{L}$ kills the bulk piece of $\delta S$, the equations of motion kill the Euler–Lagrange piece, and what remains is the divergence of the current — which must vanish because the whole $\delta S$ does**.

The corollary on the conserved charge is then standard: integrate $\partial_\mu J^\mu = 0$ over a spacetime cylinder $V^3 \times [t_1, t_2]$ and apply Gauss; the spatial-boundary contribution vanishes by the falloff assumption, and the time-boundary contributions give $Q(t_2) = Q(t_1)$.

---

# What Makes This Hard

The most common stumbling block is the *interchange of $\delta$ and $\partial$* in Step 2: $\delta(\partial_\mu\phi) = \partial_\mu(\delta\phi)$ holds for *internal* symmetries (where $\delta$ is a variation of the field at a fixed spacetime point) but *not* for external symmetries (where $\delta$ also acts on the spacetime point — the correct formula is $\delta(\partial_\mu\phi) = \partial_\mu(\delta\phi) - (\partial_\mu\xi^\nu)\partial_\nu\phi$ for an external variation $\delta\phi = \xi^\nu\partial_\nu\phi$). Confusing the two cases produces a wrong formula for the current — typically missing the $-\delta^\mu_\nu\mathcal{L}$ term in the energy–momentum tensor. A second common error is to forget that the symmetry hypothesis $\delta\mathcal{L} = 0$ is *pointwise*, not merely an integral statement: $\int_M\delta\mathcal{L} = 0$ would allow the divergence of an unwanted "improvement" current, and only the stronger pointwise condition gives the clean Noether current.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Take the first variation of $S$ for an arbitrary $\delta\phi$, integrate by parts to expose the Euler–Lagrange operator and a total divergence, then specialise to a symmetry variation (so $\delta\mathcal{L} = 0$) and to an on-shell field (so the EL operator gives zero). The total divergence must vanish for every region, and hence pointwise — this is the conservation law.

**Subgoal decomposition:**

1. **Compute $\delta\mathcal{L}$ for an arbitrary internal variation.** Using $\delta(\partial_\mu\phi) = \partial_\mu(\delta\phi)$ (internal-variation property), $\delta\mathcal{L} = (\partial\mathcal{L}/\partial\phi^a)\delta\phi^a + (\partial\mathcal{L}/\partial(\partial_\mu\phi^a))\partial_\mu(\delta\phi^a)$.
   - *Hint:* This is the chain rule. The two terms come from the two arguments of $\mathcal{L}$.
   - *Why needed:* This is the starting expression that gets integrated by parts to expose the Noether current.

2. **Integrate by parts on the second term.** Write $(\partial\mathcal{L}/\partial(\partial_\mu\phi^a))\partial_\mu(\delta\phi^a) = \partial_\mu[(\partial\mathcal{L}/\partial(\partial_\mu\phi^a))\delta\phi^a] - \partial_\mu(\partial\mathcal{L}/\partial(\partial_\mu\phi^a))\delta\phi^a$.
   - *Hint:* Product rule in reverse: $f\partial_\mu g = \partial_\mu(fg) - g\partial_\mu f$.
   - *Why needed:* This isolates the total divergence (which becomes $\partial_\mu J^\mu$) and the term combining with the original first term to give the Euler–Lagrange operator.

3. **Combine to organise as EL × variation + total divergence.** $\delta\mathcal{L} = [\partial\mathcal{L}/\partial\phi^a - \partial_\mu(\partial\mathcal{L}/\partial(\partial_\mu\phi^a))]\delta\phi^a + \partial_\mu[(\partial\mathcal{L}/\partial(\partial_\mu\phi^a))\delta\phi^a]$. The bracket on the left is the **Euler–Lagrange operator**, vanishing on shell; the bracket on the right is $J^\mu$, the **Noether current**.
   - *Hint:* The pattern $\delta\mathcal{L} = (\text{EL})\cdot\delta\phi + \partial_\mu J^\mu$ is universal.
   - *Why needed:* This identifies the Noether current explicitly.

4. **Specialise to a symmetry variation and on-shell field.** The hypothesis $\delta\mathcal{L} = 0$ kills the LHS; the on-shell condition kills the EL term; what survives is $0 = \partial_\mu J^\mu$.
   - *Hint:* Both conditions are needed simultaneously to conclude.
   - *Why needed:* This is the conservation law.

---

# Lemma Decomposition

> [!note]- Lemma 1: Internal variations commute with partial derivatives
> **Statement:** For an *internal* variation $\delta\phi^a$ at fixed spacetime point (not acting on $x$), $\delta(\partial_\mu\phi^a) = \partial_\mu(\delta\phi^a)$.
>
> **Hint:** The variation $\delta$ here is a derivative with respect to a parameter $\alpha$ at $\alpha = 0$; it commutes with $\partial_\mu$ because mixed partial derivatives commute for smooth functions of two arguments.
>
> **Why needed:** Without this commutation, the chain rule in Step 1 of the scaffold would have an extra term proportional to "the variation of $\partial_\mu$" — but internal variations leave $\partial_\mu$ alone, since they do not move the spacetime point.
>
> > [!note]- Full proof
> > Let $\phi(x, \alpha)$ be a 1-parameter family of fields with $\phi(x, 0) = \phi(x)$ and $\partial_\alpha\phi(x, 0) = \delta\phi(x)$. The variation $\delta(\partial_\mu\phi)$ is defined as $\partial_\alpha(\partial_\mu\phi(x, \alpha))|_{\alpha=0}$. Since $\phi$ is smooth in $(x, \alpha)$, mixed partials commute: $\partial_\alpha\partial_\mu\phi = \partial_\mu\partial_\alpha\phi$. Evaluating at $\alpha = 0$ gives $\delta(\partial_\mu\phi) = \partial_\mu(\delta\phi)$. The argument fails for external variations, where the parameter $\alpha$ also acts on $x$ — then $\phi$ depends on $\alpha$ both through its field values and through the moving spacetime point, and the commutation picks up an additional Lie-derivative term.

> [!note]- Lemma 2: The Euler–Lagrange operator vanishes on shell
> **Statement:** If $\phi$ is a solution of the equations of motion, then $\partial\mathcal{L}/\partial\phi^a - \partial_\mu(\partial\mathcal{L}/\partial(\partial_\mu\phi^a)) = 0$ pointwise.
>
> **Hint:** This is the definition of "on shell" — by setting $\delta S = 0$ for all compactly-supported $\delta\phi$, one derives the Euler–Lagrange equations as the bulk integrand.
>
> **Why needed:** This is what kills the first bracket in Step 3 of the scaffold, leaving only the total-divergence term.
>
> > [!note]- Full proof
> > By definition, $\phi$ is on shell if $\delta S = 0$ for all compactly-supported variations $\delta\phi$. Taking $\delta\phi$ a bump function localised in a small region $U$ and applying Step 3 of the scaffold (with no symmetry hypothesis), the total-divergence term integrates to zero by Gauss (boundary contributions vanish on a compactly-supported $\delta\phi$), and what remains is $\int_U[\partial\mathcal{L}/\partial\phi^a - \partial_\mu(\partial\mathcal{L}/\partial(\partial_\mu\phi^a))]\delta\phi^a\,\operatorname{vol}_g = 0$. Since $U$ and $\delta\phi$ are arbitrary, the integrand must vanish pointwise, giving the Euler–Lagrange equations.

> [!note]- Lemma 3: Vanishing of $\int_M F\,\operatorname{vol}_g$ for every region implies $F = 0$ pointwise
> **Statement:** If $F : M \to \mathbb{R}$ is a continuous function and $\int_U F\,\operatorname{vol}_g = 0$ for every open subset $U \subseteq M$, then $F \equiv 0$.
>
> **Hint:** Suppose $F(x_0) \neq 0$ at some point. By continuity $F$ has constant sign on a small neighbourhood $U$ of $x_0$, and its integral over $U$ is non-zero — contradiction.
>
> **Why needed:** This is what converts the on-shell statement "$\partial_\mu J^\mu$ integrates to zero over every region" into the pointwise conservation law "$\partial_\mu J^\mu = 0$".
>
> > [!note]- Full proof
> > Suppose for contradiction $F(x_0) > 0$ (the case $F(x_0) < 0$ is symmetric). By continuity, there is a neighbourhood $U$ of $x_0$ on which $F > F(x_0)/2 > 0$. Then $\int_U F\,\operatorname{vol}_g \ge (F(x_0)/2)\operatorname{vol}(U) > 0$, contradicting the hypothesis. Hence $F \equiv 0$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\delta\phi^a = E^a{}_b\phi^b$ be an internal symmetry variation, so $\delta\mathcal{L} = 0$ pointwise on $M$ by hypothesis.
>
> By Lemma 1, $\delta(\partial_\mu\phi^a) = \partial_\mu(\delta\phi^a)$. By the chain rule for $\mathcal{L}(\phi, \partial\phi, x)$,
> $$\delta\mathcal{L} = \frac{\partial\mathcal{L}}{\partial\phi^a}\delta\phi^a + \frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^a)}\partial_\mu(\delta\phi^a).$$
>
> Apply the product rule in reverse on the second term: $\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^a)}\partial_\mu(\delta\phi^a) = \partial_\mu\left[\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^a)}\delta\phi^a\right] - \partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^a)}\cdot\delta\phi^a$. Substituting and rearranging:
> $$\delta\mathcal{L} = \left[\frac{\partial\mathcal{L}}{\partial\phi^a} - \partial_\mu\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^a)}\right]\delta\phi^a + \partial_\mu\left[\frac{\partial\mathcal{L}}{\partial(\partial_\mu\phi^a)}\delta\phi^a\right].$$
>
> Recognise the first bracket as the Euler–Lagrange operator and the second bracket as the Noether current $J^\mu = (\partial\mathcal{L}/\partial(\partial_\mu\phi^a))\delta\phi^a$. So
> $$\delta\mathcal{L} = \left(\frac{\delta\mathcal{L}}{\delta\phi^a}\right)\delta\phi^a + \partial_\mu J^\mu.$$
>
> By hypothesis, $\delta\mathcal{L} = 0$. By Lemma 2 (the on-shell condition), the Euler–Lagrange operator vanishes. Hence $\partial_\mu J^\mu = 0$ pointwise on $M$ for every on-shell solution $\phi$. This is the Noether conservation law.
>
> *Corollary (conserved charge).* Integrating $\partial_\mu J^\mu = 0$ over the spacetime cylinder $V^3 \times [t_1, t_2]$ (with $V^3$ a fixed spatial region) and applying Gauss's theorem:
> $$0 = \int_{V^3\times[t_1, t_2]}\partial_\mu J^\mu\,d^4x = \int_{V^3(t_2)}J^0\,d^3x - \int_{V^3(t_1)}J^0\,d^3x + \int_{\partial V^3\times[t_1, t_2]}J^i n_i\,dS\,dt.$$
> The last term vanishes if $\phi$ (and hence $J^\mu$) decays at the spatial boundary $\partial V^3$ (taken to infinity). Hence $Q(t_2) = Q(t_1)$ where $Q(t) := \int_{V^3(t)}J^0\,d^3x$.

---

# Cross-Field Exercise Suggestions

**Application 1 — Energy conservation in classical mechanics from time-translation invariance.** For a Lagrangian $L(q, \dot q)$ that does not depend explicitly on $t$, the time-translation $q(t) \to q(t + \alpha)$ is an external symmetry (though the variational machinery is parallel to the internal-symmetry case). The Noether-type derivation produces the energy $E = \dot q\,\partial L/\partial\dot q - L$ (the Hamiltonian) as the conserved quantity. This is the classical-mechanics version of Noether and the historical seed of the theorem.

**Application 2 — Soliton-number conservation in non-linear sigma models.** For the $O(3)$ sigma model on $\mathbb{R}^{2+1}$, $\mathcal{L} = \tfrac12(\partial_\mu\vec n)\cdot(\partial^\mu\vec n)$ with $|\vec n| = 1$, the *topological* current $J^\mu = \tfrac{1}{8\pi}\epsilon^{\mu\nu\rho}\epsilon^{abc}n^a\partial_\nu n^b\partial_\rho n^c$ is conserved (not by Noether but by a topological argument). However, the *Noether* current associated to the global $SO(3)$ symmetry $\vec n \to R\vec n$ produces a genuine internal current — and the soliton charge counts the winding number $\vec n : S^2_\infty \to S^2$, which is *not* a Noether charge. This contrast illustrates that not all conserved currents come from symmetries.

**Application 3 — Lepton number and baryon number in the Standard Model.** The Standard Model Lagrangian has accidental global $U(1)_L$ (lepton number) and $U(1)_B$ (baryon number) symmetries, *not* gauged. Noether's theorem produces the corresponding conserved currents $J^\mu_L$ and $J^\mu_B$, predicting that lepton and baryon number are conserved separately at the classical level. *Quantum-mechanically* the symmetry is broken by the chiral anomaly to $U(1)_{B-L}$ only, with $B + L$ violated by instanton effects (electroweak sphalerons) — but in a finely controlled way calculable from the anomaly. This is the Noether construction at its full mature form: classical conservation + quantum anomaly + Wess–Zumino consistency.

---

# Bridges

- **Connection to the [[Def - Gauge-Covariant Derivative|gauge-covariant derivative]] and the gauge principle:** Noether's theorem produces a conserved current $J^\mu$ from any global symmetry of $\mathcal{L}$. When the symmetry is promoted to a *local* gauge symmetry by introducing $D_\mu = \partial_\mu - iqA_\mu$, the Noether current becomes the *source* of the gauge field: $\delta S/\delta A_\mu = J^\mu$, so the YM equation $d_A\star F = \star J$ is sourced precisely by the gauge-Noether current of the matter field. Every gauge boson in the Standard Model is sourced by a Noether current of an internal symmetry.

- **Connection to the [[Geometric Mechanics I — Symplectic Manifolds and Hamiltonian Dynamics|momentum map]] in symplectic geometry:** Noether's theorem is the field-theoretic version of the symplectic momentum map $\mu : P \to \mathfrak{g}^*$. For a Hamiltonian $G$-action on a symplectic manifold $(P, \omega)$, the function $\langle\mu, E\rangle$ (the moment-map paired with a generator $E \in \mathfrak{g}$) is the conserved quantity generating the symmetry $E$ via Hamilton's equations. In the field-theoretic setting $P$ is the infinite-dimensional space of fields and the momentum map gives, after suitable smearing, the integrated Noether charges. The **Marsden–Weinstein reduction** $\mu^{-1}(c)/G_c$ in mechanics corresponds to the **gauge-orbit moduli space** $\mathcal{A}/\mathcal{G}$ in gauge theory.

- **Connection to Killing vector fields in [[Riemannian Geometry I — Connections and Covariant Differentiation|Riemannian geometry]]:** A Killing vector field $X$ on a Riemannian manifold $(M, g)$ generates a flow of isometries — a continuous symmetry of the metric. Particles moving along geodesics on $(M, g)$ have a conserved quantity $\langle X, \dot\gamma\rangle$ (the inner product of the Killing field with the geodesic tangent), which is the Noether charge of the geodesic Lagrangian under the isometry. For example, on the round sphere $S^2$ with axial Killing field $\partial_\phi$, the conserved quantity is the angular momentum about the symmetry axis. This is the classical-mechanics version of Noether applied to a particle moving in a symmetric background.

- **Connection to anomalies in quantum field theory:** Noether's theorem holds classically — but in the quantum theory, the symmetry may be *anomalous*, meaning the path integral measure $\mathcal{D}\phi$ is *not* invariant under the symmetry transformation even though $\mathcal{L}$ is. The classical conservation law $\partial_\mu J^\mu = 0$ is then replaced by $\partial_\mu J^\mu = \mathcal{A}$ for an anomaly $\mathcal{A}$, often involving instanton-type quantities like $\operatorname{tr}(F\wedge F)$. The most famous example is the **axial anomaly** $\partial_\mu J^{\mu,5} = \frac{e^2}{16\pi^2}F_{\mu\nu}\tilde F^{\mu\nu}$, which explains the decay rate $\pi^0 \to 2\gamma$ and which (in QCD) accounts for the heavy mass of the $\eta'$ meson. Anomalies are quantum departures from Noether's theorem.
