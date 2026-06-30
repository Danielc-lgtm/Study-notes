---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Noether Theorem (Relativistic Particle)"
  - "Def - Relativistic Action of a Free Particle"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - The Poincaré Group"
tags: [physics, special-relativity]
---

# Problem Statement

A free particle has Lagrangian $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ (with $c = 1$).

1. Verify that $L$ is invariant under a spacetime translation $x'^\mu = x^\mu + \varepsilon\,a^\mu$ (with $a^\mu$ a constant vector), and identify the generator $G^\mu$.
2. Apply [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]] to conclude that the four-momentum $p_\mu = m u_\mu$ is conserved, and verify directly that $dp_\mu/d\tau = 0$ on the free worldline.
3. Decompose the conserved $p_\mu$ relative to an inertial observer into the energy $E = p_0$ and three-momentum $\mathbf{P} = (p_i)$, and state the four conservation laws in observer language.
4. Explain why the conserved Noether charge takes the form $p_\mu G^\mu$ — a momentum *one-form* contracted with a generator *vector* — and what this says about the geometric nature of four-momentum.

**Recall:**

![[Thm - Noether Theorem (Relativistic Particle)#Statement]]

The free Lagrangian $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ has generalized four-momentum $p_\mu = \partial L/\partial\dot x^\mu = m u_\mu$, the [[Def - Four-Momentum and Rest Mass|four-momentum]] $P = mU$. A spacetime translation is one of the ten [[Def - The Poincaré Group|Poincaré]] transformations, the four-dimensional generalisation of "the Lagrangian has no explicit position dependence."

---

# Convergent Strategy

**Problem class.** A *read-off-a-conserved-quantity-from-a-symmetry* problem, the central application of [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]]: identify the symmetry, read the generator, write down the conserved charge — no equation of motion need be solved.

**Assumption pattern.** The free Lagrangian has *no explicit dependence on the coordinates $x^\mu$* (it depends only on $\dot x^\mu$ through $\eta_{\mu\nu}\dot x^\mu\dot x^\nu$). This is precisely translation invariance: shifting all coordinates by a constant leaves $L$ unchanged. The generator of a translation is the constant vector $a^\mu$, the simplest possible $G^\mu$.

**Theorem routing.** Translation invariance (the symmetry) feeds [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]], whose conserved charge $p_\mu G^\mu$ becomes, with $G^\mu = a^\mu$ constant, the statement that $p_\mu a^\mu$ is conserved for *every* constant $a^\mu$ — hence each component $p_\mu$ is conserved, the [[Def - Four-Momentum and Rest Mass|four-momentum]].

**Key decision point.** The subtle point is recognising that conservation of $p_\mu a^\mu$ for *all* constant $a^\mu$ implies conservation of every component $p_\mu$ — not just one combination. Since the four translations $a^\mu = \delta^\mu_{\;\nu}$ ($\nu = 0,1,2,3$) are independent, running over them gives four independent conservation laws. The second subtlety is the geometric reading: the conserved quantity is the momentum *contracted with* the translation direction, which forces the momentum to be a covector.

---

# Legal Operations Used

1. **Apply Noether's theorem** (operation 3 from the topic page). Translation invariance of $L$ yields the conserved charge $p_\mu G^\mu = p_\mu a^\mu$.

2. **Recognise a conserved quantity as a momentum contracted with a generator** (operation 9). Here the generator is the constant translation vector $a^\mu$, so the charge $p_\mu a^\mu$ conserved for all $a^\mu$ gives $p_\mu = \text{const}$.

3. **Compute the generalized four-momentum** (operation 5). For the free particle $p_\mu = \partial L/\partial\dot x^\mu = m u_\mu$.

---

# Hints

> [!note]- Hint 1
> A translation is $x'^\mu = x^\mu + \varepsilon a^\mu$ with $a^\mu$ constant, so $G^\mu = a^\mu$ and $\dot G^\mu = 0$ (the generator is constant along the worldline). The Lagrangian depends on $x^\mu$ only through the constant metric, so $L(x', \dot x') = L(x, \dot x)$ exactly — translation invariance is manifest.

> [!note]- Hint 2
> Noether gives $p_\mu G^\mu = p_\mu a^\mu = \text{const}$. Since this holds for every constant $a^\mu$, and the four basis translations $a^\mu = \delta^\mu_{\;\nu}$ are independent, each $p_\nu$ is separately conserved. Directly: $p_\mu = m u_\mu$ and $du_\mu/d\tau = 0$ on the free worldline (the geodesic equation), so $dp_\mu/d\tau = 0$.

> [!note]- Hint 3
> Relative to an inertial observer, $p_0 = E$ (energy) and $p_i = -P^i$ or $P_i$ (three-momentum, sign depending on index placement). Conservation of $p_0$ is energy conservation; conservation of $p_i$ is three-momentum conservation. So translation invariance in *time* gives energy conservation, in *space* gives momentum conservation.

> [!note]- Hint 4
> The conserved charge is $p_\mu a^\mu$, a contraction. The translation $a^\mu$ is a *vector* (a direction in spacetime); to extract a scalar from it, $p_\mu$ must be a *linear form* eating vectors. So four-momentum is fundamentally a covector — the object you contract against displacements — not a vector. This is Gourgoulhon's Remark 11.11.

---

# Solution

The solution is four short steps. Step 1 verifies translation invariance and identifies the constant generator. Step 2 applies Noether and confirms conservation directly. Step 3 decomposes into observer language. Step 4 draws the geometric moral. The whole point is that a conservation law (four-momentum) drops out of a symmetry (translation invariance) with no differential equation solved — the power of Noether's theorem.

**Step 1: Translation invariance and the generator.**

> [!note]- Derivation
> A spacetime translation by the constant vector $a^\mu$ is $x'^\mu = x^\mu + \varepsilon a^\mu$, so comparing with the general form $x'^\mu = x^\mu + \varepsilon G^\mu$, the generator is the *constant* vector $G^\mu = a^\mu$. Its parameter-derivative vanishes: $\dot G^\mu = dG^\mu/d\lambda = 0$. The parameter-velocity is unchanged, $\dot x'^\mu = \dot x^\mu + \varepsilon\dot a^\mu = \dot x^\mu$. The Lagrangian $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ depends on the coordinates only through the *constant* metric $\eta_{\mu\nu}$, so
> $$L(x', \dot x') = -m\sqrt{\eta_{\mu\nu}\dot x'^\mu\dot x'^\nu} = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu} = L(x, \dot x).$$
> The invariance is exact (not just to first order): the free Lagrangian is translation-invariant because it has no explicit position dependence.

**Step 2: Four-momentum is conserved.**

> [!note]- Derivation
> By [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]], the invariance of $L$ under $x'^\mu = x^\mu + \varepsilon a^\mu$ implies the conserved charge
> $$\frac{\partial L}{\partial\dot x^\mu}G^\mu = p_\mu a^\mu = \text{const}.$$
> This holds for *every* constant translation vector $a^\mu$. Choosing the four independent basis translations $a^\mu = \delta^\mu_{\;\nu}$ for $\nu = 0,1,2,3$ in turn, each component $p_\nu = m u_\nu$ is separately conserved:
> $$p_\mu = m u_\mu = \text{const along the worldline}.$$
> *Direct verification:* $p_\mu = m u_\mu$, and on the free worldline the geodesic equation gives $du_\mu/d\tau = 0$ ([[Thm - Free-Particle Worldline Extremises Proper Time]]), so $dp_\mu/d\tau = m\,du_\mu/d\tau = 0$. The Noether route and the direct route agree, but the Noether route *explains* the conservation by tracing it to translation invariance, while the direct route merely computes it.

**Step 3: Energy and momentum in observer language.**

> [!note]- Derivation
> Relative to an inertial observer $\mathcal{O}$, the four-momentum $P = mU$ decomposes into a time component and spatial components. The time component is the **energy** $p_0 = E = m\gamma$ (the observer's measured energy, including rest energy $m$), and the spatial components are the **three-momentum** $P_i = m\gamma V_i$ (see [[Def - Four-Momentum and Rest Mass]]). The four conservation laws $p_\mu = \text{const}$ therefore read:
> $$E = \text{const} \quad(\text{time translation}), \qquad \mathbf{P} = \text{const} \quad(\text{space translation}).$$
> **Translation invariance in time gives energy conservation; translation invariance in space gives momentum conservation** — the relativistic, unified statement of the two most basic conservation laws of physics, both following from the single fact that the free Lagrangian has no explicit dependence on where or when the particle is.

**Step 4: Four-momentum is a one-form.**

> [!note]- Derivation
> The conserved Noether charge is $p_\mu a^\mu$, a *contraction* of the momentum with the translation vector $a^\mu$. The translation $a^\mu$ is unambiguously a **vector** — it is a displacement, a direction in spacetime, the thing that connects the point $x$ to the point $x + \varepsilon a$. To produce a scalar (a number, the conserved quantity) by contracting against a vector, the momentum $p_\mu$ must be a **linear form** — an object that eats vectors and returns numbers. So the four-momentum is fundamentally a *covector* (a one-form), not a vector: it is the thing you contract *against* displacements, which is the defining behaviour of the dual space. This is the content of Gourgoulhon's Remark 11.11, and it is no mere pedantry: it is why the natural pairing $\langle P, G\rangle = p_\mu G^\mu$ appears, why momentum lives in the cotangent space, and why Hamilton's equations are written on a cotangent bundle. The metric lets us raise the index and *also* regard the four-momentum as a vector $P^\mu = m U^\mu$, but its primary, Noether-given identity is as a linear form.

> [!note]- Complete formal solution
> A translation $x'^\mu = x^\mu + \varepsilon a^\mu$ ($a^\mu$ constant) has generator $G^\mu = a^\mu$, $\dot G^\mu = 0$, and leaves $\dot x^\mu$ and hence $L = -m\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}$ exactly invariant (the metric is constant, no explicit $x$-dependence). By [[Thm - Noether Theorem (Relativistic Particle)|Noether's theorem]], $p_\mu a^\mu = \text{const}$ for every constant $a^\mu$; running over the four independent basis translations gives $p_\mu = m u_\mu = \text{const}$, conservation of the four-momentum. Directly, $du_\mu/d\tau = 0$ on the geodesic worldline confirms $dp_\mu/d\tau = 0$. Relative to an observer, $p_0 = E$ and $p_i = P_i$, so time translation gives $E = \text{const}$ and space translation gives $\mathbf{P} = \text{const}$. The conserved charge $p_\mu a^\mu$ is a contraction of the momentum covector with the translation vector, showing four-momentum is fundamentally a one-form (Remark 11.11). $\blacksquare$

---

# Key Takeaways

**Energy and momentum conservation are the same theorem: translation invariance via Noether.** The deepest content of this exercise is that the two most fundamental conservation laws of physics — energy and momentum — are not separate facts but two faces of one symmetry. Translation invariance in time (the laws of physics are the same now as later) gives energy conservation; translation invariance in space (the laws are the same here as there) gives momentum conservation; together they are the conservation of the four-momentum, the Noether charge of spacetime translation. The reusable principle is that whenever a Lagrangian lacks explicit dependence on a coordinate, the conjugate momentum is conserved — and the relativistic version unifies time and space, so the absence of *all four* coordinates from the free Lagrangian gives conservation of the *entire* four-momentum. The trigger to recognise: a Lagrangian with no explicit $x$-dependence has a conserved momentum; if it also has no explicit $t$-dependence (in the non-covariant picture), energy is conserved. Noether's theorem is what makes "symmetry implies conservation" precise and computable.

**The Noether route explains conservation; the direct route only computes it.** One can verify $dp_\mu/d\tau = 0$ directly from the geodesic equation, and one can derive it from translation invariance via Noether — both are correct, but they are not equally illuminating. The direct route says "the momentum happens to be constant because the worldline happens to be straight"; the Noether route says "the momentum *must* be constant *because* spacetime is translation-invariant." The latter is explanatory: it traces the conservation law to a structural symmetry, and it tells you that *any* translation-invariant theory — not just the free particle — will conserve momentum, including theories whose equations of motion are too complicated to solve. This is why Noether's theorem is indispensable in field theory, where the equations of motion are often intractable but the symmetries (and hence the conservation laws) are manifest. When you want to know *whether* a quantity is conserved, look for a symmetry, not for a solvable equation of motion.

**The conserved charge is a pairing, which is why four-momentum is a covector.** The Noether charge $p_\mu G^\mu$ is the contraction of the momentum with the symmetry generator, and this single structural fact pins down the geometric nature of momentum: since the generator $G^\mu$ is a vector (a direction in spacetime), the momentum $p_\mu$ must be a linear form to produce a scalar by contraction. Four-momentum is the thing you contract *against* displacements — a covector, a one-form, an inhabitant of the cotangent space — and the metric's ability to raise the index, recasting it as a vector $P^\mu$, is a convenience layered on top of its primary covector nature. This matters operationally: it is why momentum pairs naturally with position to form phase space (a cotangent bundle), why Hamilton's equations live on $T^*Q$, and why the quantisation rule is $p_\mu \to -i\hbar\partial_\mu$ (the derivative is a covector). The same Noether pairing, applied to rotation and boost generators, gives the angular-momentum tensor; see [[Ex - Angular momentum and the centre of inertia from Lorentz invariance]]. For the static-field case where only the energy is conserved, see [[Ex - Conserved energy and momentum in a static field]].
