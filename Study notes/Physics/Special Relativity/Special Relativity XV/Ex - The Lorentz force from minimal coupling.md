---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Lagrangian for a Particle in a Vector Field"
  - "Def - The Electromagnetic Field Tensor"
  - "Def - Four-Force"
  - "Def - Four-Velocity and Four-Acceleration"
tags: [physics, special-relativity]
---

# Problem Statement

A particle of rest mass $m$ and charge $q$ moves in a vector field with potential one-form $A$, with Lagrangian $L = -mc\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu} + \tfrac{q}{c}A_\mu(x)\dot x^\mu$. Work with $c = 1$ unless restoring $c$ aids recognition.

1. Compute $\partial L/\partial x^\mu$ and $\partial L/\partial\dot x^\mu$, and write down the Euler–Lagrange equations.
2. Simplify them (parametrising by proper time at the end) to the **Lorentz four-force law** $mc^2 a_\mu = qF_{\mu\nu}U^\nu$, where $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$.
3. Verify that this four-force is **pure**: $\langle f, U\rangle = qF_{\mu\nu}U^\mu U^\nu = 0$, so the rest mass is conserved.
4. Show the action is **gauge-invariant**: under $A \mapsto A + d\chi$ for any scalar $\chi$, $S$ changes only by an endpoint term, so the equation of motion is unchanged. Identify what *does* change (the canonical momentum).
5. Decompose the Lorentz force relative to an inertial observer and recover the familiar three-force $\tfrac{d\mathbf{p}}{dt} = q(\mathbf{E} + \mathbf{V}\times\mathbf{B})$.

**Recall:**

![[Def - Lagrangian for a Particle in a Vector Field#The Definition]]

The **field-strength tensor** $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is antisymmetric; relative to an observer its components are the electric field $\mathbf{E}$ (the $F_{0i}$ components) and magnetic field $\mathbf{B}$ (the $F_{ij}$ components); see [[Def - The Electromagnetic Field Tensor]]. A **pure four-force** satisfies $\langle f, U\rangle = 0$, the condition that the rest mass be conserved ([[Def - Four-Force]]). The four-acceleration is $a^\mu = dU^\mu/d\tau$, orthogonal to $U$.

---

# Convergent Strategy

**Problem class.** A *derive-the-force-from-a-coupling* problem: given a minimal-coupling Lagrangian, vary it to obtain the equation of motion. This is the [[Special Relativity XV — The Principle of Least Action#Problem-Solving Strategy|topic strategy]] applied to a particle in a field, and it is the variational derivation of the Lorentz force.

**Assumption pattern.** The interaction term is the line integral of a *one-form*, $\tfrac{q}{c}A_\mu\dot x^\mu$, the unique simplest degree-one homogeneous scalar built from the potential. Its position-derivative produces $\partial_\mu A_\nu$, and the *antisymmetric* combination that survives in the equation of motion is $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ — the field strength appears automatically.

**Theorem routing.** Vary [[Def - Lagrangian for a Particle in a Vector Field|the minimal-coupling Lagrangian]]: the free part gives $-mc\,du_\mu/d\lambda$ as in the geodesic derivation, the interaction part gives the field-strength force, and combining them yields $mc^2 a_\mu = qF_{\mu\nu}U^\nu$. Antisymmetry of $F$ then gives the purity $\langle f, U\rangle = 0$ ([[Def - Four-Force]]); the total-derivative structure of $\int d\chi$ gives gauge invariance; and the observer decomposition of $F$ ([[Def - The Electromagnetic Field Tensor]]) recovers $q(\mathbf{E} + \mathbf{V}\times\mathbf{B})$.

**Key decision point.** The crux is handling the total $\lambda$-derivative of $A_\mu$ correctly: $dA_\mu/d\lambda = (\partial_\nu A_\mu)\dot x^\nu$ (chain rule along the worldline), and the difference between this and the $\partial_\mu A_\nu$ from $\partial L/\partial x^\mu$ is exactly the antisymmetric $F_{\mu\nu}$. Missing this — confusing $dA_\mu/d\lambda$ with $\partial_\mu A_\nu\dot x^\nu$ — is the classic error; the indices must be tracked carefully, and the antisymmetrisation is where the magnetic-type force comes from.

---

# Legal Operations Used

1. **Couple to a field by minimal coupling** (operation 4 from the topic page). The interaction $\tfrac{q}{c}A_\mu\dot x^\mu$ is added to the free Lagrangian; varying it produces the field-strength force.

2. **Vary the action and read off the Euler–Lagrange equations** (operation 1). The full Euler–Lagrange equations of $L = L_{\text{free}} + L_{\text{int}}$ give the Lorentz force after simplification.

3. **Compute the generalized four-momentum** (operation 5). Here $\partial L/\partial\dot x^\mu = mc\,u_\mu + \tfrac{q}{c}A_\mu$, the canonical momentum, whose proper-time derivative enters the equation of motion.

4. **Choose the parameter last** (operation 7). Keep $\lambda$ arbitrary, simplify, and set $\lambda = \tau$ only when reading off the four-acceleration.

---

# Hints

> [!note]- Hint 1
> The interaction term contributes $\partial L_{\text{int}}/\partial x^\mu = \tfrac{q}{c}(\partial_\mu A_\nu)\dot x^\nu$ and $\partial L_{\text{int}}/\partial\dot x^\mu = \tfrac{q}{c}A_\mu$. The free term contributes $\partial L_{\text{free}}/\partial x^\mu = 0$ and $\partial L_{\text{free}}/\partial\dot x^\mu = mc\,u_\mu$ (as in the geodesic derivation).

> [!note]- Hint 2
> The Euler–Lagrange equation is $\tfrac{q}{c}(\partial_\mu A_\nu)\dot x^\nu - \tfrac{d}{d\lambda}\big(mc\,u_\mu + \tfrac{q}{c}A_\mu\big) = 0$. The key step: $\tfrac{dA_\mu}{d\lambda} = (\partial_\nu A_\mu)\dot x^\nu$ by the chain rule. Combine the two $A$-terms: $\tfrac{q}{c}[(\partial_\mu A_\nu) - (\partial_\nu A_\mu)]\dot x^\nu = \tfrac{q}{c}F_{\mu\nu}\dot x^\nu$.

> [!note]- Hint 3
> After dividing by $\sqrt{\eta\dot x\dot x}$ and using $U^\mu = \dot x^\mu/\sqrt{\eta\dot x\dot x}$, the equation becomes $mc^2 a_\mu = qF_{\mu\nu}U^\nu$ (restoring factors). For purity, contract with $U^\mu$: $qF_{\mu\nu}U^\mu U^\nu = 0$ because $F$ is antisymmetric and $U^\mu U^\nu$ is symmetric.

> [!note]- Hint 4
> Under $A \mapsto A + d\chi$, the interaction action $q\int A_\mu dx^\mu \mapsto q\int A_\mu dx^\mu + q\int \partial_\mu\chi\,dx^\mu = q\int A_\mu dx^\mu + q\int d\chi = q\int A_\mu dx^\mu + q[\chi]_{A_1}^{A_2}$. The endpoint term is fixed, so $\delta S$ is unchanged. The canonical momentum $p_\mu = mc\,u_\mu + \tfrac{q}{c}A_\mu$ shifts by $\tfrac{q}{c}\partial_\mu\chi$.

> [!note]- Hint 5
> Use $F_{0i} = E_i$, $F_{ij} = -\epsilon_{ijk}B^k$ (mostly-minus conventions) and $U^\mu = \gamma(1, \mathbf{V})$. The spatial part of $mc^2 a_\mu = qF_{\mu\nu}U^\nu$, divided by $\gamma$ and rewritten in terms of $d\mathbf{p}/dt$, gives $q(\mathbf{E} + \mathbf{V}\times\mathbf{B})$.

---

# Solution

The solution has five steps. Step 1 differentiates the Lagrangian. Step 2 assembles the Euler–Lagrange equation and performs the crucial antisymmetrisation that produces $F_{\mu\nu}$. Step 3 checks the force is pure. Step 4 establishes gauge invariance. Step 5 decomposes to the familiar three-force. The decisive move is in Step 2: the difference between $\partial_\mu A_\nu$ (from the explicit position-derivative) and $\partial_\nu A_\mu$ (from the total derivative of $A_\mu$ along the worldline) is exactly the antisymmetric field strength.

**Step 1: The derivatives of the Lagrangian.**

> [!note]- Derivation
> Write $L = L_{\text{free}} + L_{\text{int}}$ with $L_{\text{free}} = -mc\sqrt{w}$, $w = \eta_{\mu\nu}\dot x^\mu\dot x^\nu$, and $L_{\text{int}} = \tfrac{q}{c}A_\mu(x)\dot x^\mu$.
> *Position-derivatives:* $\partial L_{\text{free}}/\partial x^\mu = 0$ (constant metric); $\partial L_{\text{int}}/\partial x^\mu = \tfrac{q}{c}\dfrac{\partial A_\nu}{\partial x^\mu}\dot x^\nu = \tfrac{q}{c}(\partial_\mu A_\nu)\dot x^\nu$.
> *Velocity-derivatives:* $\partial L_{\text{free}}/\partial\dot x^\mu = mc\,u_\mu$ (from the geodesic derivation, with $u_\mu = \eta_{\mu\nu}\dot x^\nu/\sqrt{w}$); $\partial L_{\text{int}}/\partial\dot x^\mu = \tfrac{q}{c}A_\mu$ (since $A_\mu$ does not depend on $\dot x$). So the generalized momentum is $p_\mu = \partial L/\partial\dot x^\mu = mc\,u_\mu + \tfrac{q}{c}A_\mu$.

**Step 2: The Euler–Lagrange equation is the Lorentz force.**

> [!note]- Derivation
> The Euler–Lagrange equation $\partial L/\partial x^\mu - \tfrac{d}{d\lambda}(\partial L/\partial\dot x^\mu) = 0$ reads
> $$\frac{q}{c}(\partial_\mu A_\nu)\dot x^\nu - \frac{d}{d\lambda}\Big(mc\,u_\mu + \frac{q}{c}A_\mu\Big) = 0.$$
> The crucial step is the total $\lambda$-derivative of $A_\mu$ along the worldline, by the chain rule:
> $$\frac{dA_\mu}{d\lambda} = \frac{\partial A_\mu}{\partial x^\nu}\frac{dx^\nu}{d\lambda} = (\partial_\nu A_\mu)\dot x^\nu.$$
> Substituting,
> $$\frac{q}{c}(\partial_\mu A_\nu)\dot x^\nu - mc\frac{du_\mu}{d\lambda} - \frac{q}{c}(\partial_\nu A_\mu)\dot x^\nu = 0.$$
> The two $A$-terms combine into the **antisymmetric** field strength:
> $$\frac{q}{c}\big[(\partial_\mu A_\nu) - (\partial_\nu A_\mu)\big]\dot x^\nu = \frac{q}{c}F_{\mu\nu}\dot x^\nu, \qquad F_{\mu\nu} := \partial_\mu A_\nu - \partial_\nu A_\mu.$$
> So $\tfrac{q}{c}F_{\mu\nu}\dot x^\nu = mc\,\tfrac{du_\mu}{d\lambda}$. Divide by $\sqrt{w}$ and use $\dot x^\nu/\sqrt{w} = U^\nu$ and $\tfrac{1}{\sqrt{w}}\tfrac{d}{d\lambda} = \tfrac{1}{c}\tfrac{d}{d\tau}$ (from $d\tau = c^{-1}\sqrt{w}\,d\lambda$, so along the worldline $\tfrac{du_\mu}{d\lambda}/\sqrt{w} = c^{-1}\tfrac{du_\mu}{d\tau}$). Then, restoring factors and writing $a_\mu = du_\mu/d\tau$,
> $$mc^2 a_\mu = q F_{\mu\nu}U^\nu, \qquad\text{i.e.}\qquad f = qF(\cdot, U),$$
> the **Lorentz four-force law**. (With $c = 1$: $m a_\mu = qF_{\mu\nu}U^\nu$.) The field strength $F$ appeared *automatically* as the antisymmetrisation of $\partial A$; this is why electromagnetism is governed by $F = dA$ rather than by $A$ itself.

**Step 3: The four-force is pure, so rest mass is conserved.**

> [!note]- Derivation
> A four-force $f_\mu = qF_{\mu\nu}U^\nu$ is **pure** if $\langle f, U\rangle = f_\mu U^\mu = 0$, which guarantees the rest mass is constant (a four-force with a component along $U$ would change $U\cdot U$ and hence the mass). Contract:
> $$f_\mu U^\mu = qF_{\mu\nu}U^\nu U^\mu = qF_{\mu\nu}U^\mu U^\nu.$$
> Now $F_{\mu\nu}$ is antisymmetric ($F_{\mu\nu} = -F_{\nu\mu}$) while $U^\mu U^\nu$ is symmetric under $\mu \leftrightarrow \nu$. The contraction of an antisymmetric tensor with a symmetric one vanishes: relabelling indices, $F_{\mu\nu}U^\mu U^\nu = F_{\nu\mu}U^\nu U^\mu = -F_{\mu\nu}U^\mu U^\nu$, so the quantity equals its own negative and is zero. Hence $\langle f, U\rangle = 0$: the Lorentz force is pure, and $\tfrac{d}{d\tau}(U\cdot U) = 2U\cdot a = \tfrac{2}{mc^2}U^\mu f_\mu = 0$, confirming $m$ is conserved. This is exactly why the one-form coupling is the *right* interaction: its antisymmetric field strength automatically gives a mass-preserving force.

**Step 4: Gauge invariance.**

> [!note]- Derivation
> Under a gauge transformation $A \mapsto A + d\chi$, i.e. $A_\mu \mapsto A_\mu + \partial_\mu\chi$, the interaction action changes by
> $$\Delta S = q\int_{A_1}^{A_2}(\partial_\mu\chi)\,dx^\mu = q\int_{A_1}^{A_2}d\chi = q\,[\chi(A_2) - \chi(A_1)],$$
> using that $\partial_\mu\chi\,dx^\mu = d\chi$ is an exact one-form, whose integral depends only on the endpoints. Since the endpoints $A_1, A_2$ are held fixed in the variational principle, $\Delta S$ is a constant, contributing nothing to $\delta S$; the equations of motion are unchanged. Equivalently, $F = dA$ is gauge-invariant ($d(d\chi) = 0$), and the force depends on $A$ only through $F$. What *does* change is the canonical momentum: $p_\mu = mc\,u_\mu + \tfrac{q}{c}A_\mu \mapsto p_\mu + \tfrac{q}{c}\partial_\mu\chi$. The *kinetic* momentum $mc\,u_\mu = p_\mu - \tfrac{q}{c}A_\mu$ is gauge-invariant; the *canonical* momentum is not. This is the classical seed of the gauge principle and of the Aharonov–Bohm effect.

**Step 5: The familiar three-force.**

> [!note]- Derivation
> Relative to an inertial observer, $U^\mu = \gamma(1, \mathbf{V})$ (with $c = 1$), and the field-strength components are $F_{0i} = E_i$ (electric field) and $F_{ij} = -\epsilon_{ijk}B^k$ (magnetic field), per [[Def - The Electromagnetic Field Tensor]]. The spatial components of $m a_\mu = qF_{\mu\nu}U^\nu$ are
> $$m a_i = qF_{i\nu}U^\nu = q\big(F_{i0}U^0 + F_{ij}U^j\big) = q\big(-E_i\,\gamma + (-\epsilon_{ijk}B^k)\gamma V^j\big) = -q\gamma\big(E_i + (\mathbf{V}\times\mathbf{B})_i\big),$$
> where the sign and the cross product follow from $\epsilon_{ijk}V^j B^k = (\mathbf{V}\times\mathbf{B})_i$ and the lowered spatial index carrying a minus in mostly-minus. Raising the index (another minus) and writing the spatial four-acceleration in terms of $d\mathbf{p}/dt = d(m\gamma\mathbf{V})/dt$ (using $dt = \gamma\,d\tau$), the equation becomes
> $$\frac{d\mathbf{p}}{dt} = q\big(\mathbf{E} + \mathbf{V}\times\mathbf{B}\big),$$
> the textbook **Lorentz three-force**. The electric field accelerates along $\mathbf{E}$; the magnetic field deflects perpendicular to $\mathbf{V}$, doing no work (consistent with the purity of Step 3, since $\mathbf{V}\cdot(\mathbf{V}\times\mathbf{B}) = 0$). The single covariant equation $f = qF(\cdot, U)$ packages both.

> [!note]- Complete formal solution
> For $L = -mc\sqrt{w} + \tfrac{q}{c}A_\mu\dot x^\mu$ ($w = \eta_{\mu\nu}\dot x^\mu\dot x^\nu$): $\partial L/\partial x^\mu = \tfrac{q}{c}(\partial_\mu A_\nu)\dot x^\nu$ and $\partial L/\partial\dot x^\mu = mc\,u_\mu + \tfrac{q}{c}A_\mu$. The Euler–Lagrange equation, using $dA_\mu/d\lambda = (\partial_\nu A_\mu)\dot x^\nu$, gives $\tfrac{q}{c}[(\partial_\mu A_\nu) - (\partial_\nu A_\mu)]\dot x^\nu = mc\,du_\mu/d\lambda$, i.e. $mc^2 a_\mu = qF_{\mu\nu}U^\nu$ with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ (after dividing by $\sqrt{w}$ and parametrising by $\tau$). The force is pure: $qF_{\mu\nu}U^\mu U^\nu = 0$ because antisymmetric contracted with symmetric vanishes, so $m$ is conserved. Under $A \mapsto A + d\chi$, the action changes by the endpoint term $q[\chi]_{A_1}^{A_2}$, leaving the equations of motion invariant (the canonical momentum shifts by $\tfrac{q}{c}\partial_\mu\chi$; the kinetic momentum $mcU$ does not). Decomposing relative to an observer with $F_{0i} = E_i$, $F_{ij} = -\epsilon_{ijk}B^k$, $U^\mu = \gamma(1, \mathbf{V})$ recovers $d\mathbf{p}/dt = q(\mathbf{E} + \mathbf{V}\times\mathbf{B})$. $\blacksquare$

---

# Key Takeaways

**The field strength $F = dA$ appears automatically as the antisymmetrisation of $\partial A$ — this is why electromagnetism is a gauge theory.** The single most important step in the derivation is the combination $\tfrac{q}{c}[(\partial_\mu A_\nu) - (\partial_\nu A_\mu)]\dot x^\nu = \tfrac{q}{c}F_{\mu\nu}\dot x^\nu$, where the symmetric part of $\partial_\mu A_\nu$ cancels and only the antisymmetric field strength survives in the equation of motion. The consequence is profound: the dynamics depends on $A$ only through $F = dA$, so $A$ is determined only up to a gradient (gauge transformation), and the observable physics lives in the gauge-invariant $F$. This is not imposed; it falls out of varying the line integral of a one-form. The reusable insight is that *any* interaction built from the integral of a connection one-form along a path will exhibit this gauge structure, because $\int A$ over a path with fixed endpoints is sensitive to $A$ only modulo exact forms. Electromagnetism, and by extension all of Yang–Mills theory, is the study of these connection one-forms and their curvatures $F = dA$.

**The purity of the Lorentz force — antisymmetric $F$ contracted with symmetric $UU$ — is what keeps the rest mass constant.** A relativistic four-force must satisfy $\langle f, U\rangle = 0$ (it must be orthogonal to the four-velocity), or else it would change $U\cdot U$ and hence the rest mass, turning the particle into a different particle. The Lorentz force passes this test automatically because $F_{\mu\nu}$ is antisymmetric while $U^\mu U^\nu$ is symmetric, and the contraction of an antisymmetric with a symmetric tensor always vanishes. This is the deep reason the one-form coupling is the *correct* interaction for a massive particle: its field strength is necessarily antisymmetric, so its force is necessarily pure. The trigger to recognise: whenever you contract an antisymmetric tensor with a symmetric one, the result is zero — a constantly useful identity, here guaranteeing mass conservation, elsewhere killing unwanted terms in field theory. A coupling whose force was not orthogonal to $U$ (for instance the scalar coupling, whose force involves the acceleration) does not preserve the rest mass in the same clean way.

**Canonical momentum is gauge-dependent; kinetic momentum is gauge-invariant — and the distinction is the origin of minimal substitution.** Under $A \mapsto A + d\chi$ the equation of motion is unchanged, but the canonical momentum $p_\mu = mc\,u_\mu + \tfrac{q}{c}A_\mu$ shifts by $\tfrac{q}{c}\partial_\mu\chi$, while the kinetic momentum $mc\,u_\mu = p_\mu - \tfrac{q}{c}A_\mu$ stays fixed. This is the classical root of the **minimal substitution** $p_\mu \to p_\mu - \tfrac{q}{c}A_\mu$ that couples every charged field to electromagnetism in quantum mechanics: the gauge-invariant object is always the kinetic momentum, so the wave equation must be built from $p_\mu - \tfrac{q}{c}A_\mu$, not from $p_\mu$. The gauge-dependence of the canonical momentum is not a flaw but a feature — it is exactly compensated by the gauge transformation of the wavefunction's phase, which is the content of the Aharonov–Bohm effect, where the line integral $q\oint A$ around a closed loop is observable even where $F = 0$. For the canonical and Hamiltonian formulation of this charged particle, including the Dirac constraint Hamiltonian, see [[Ex - The Dirac Hamiltonian and the primary constraint]]; for the field-strength tensor's structure see [[Special Relativity XXI — The Electromagnetic Field]].
