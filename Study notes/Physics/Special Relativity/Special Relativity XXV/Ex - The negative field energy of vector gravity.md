---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Vector and Tensor Theories of Gravity"
  - "Def - The Energy-Momentum Tensor"
  - "Def - The Electromagnetic Field Tensor"
tags: [physics, special-relativity]
---

# Problem Statement

A vector theory of gravity is obtained from electromagnetism by the substitution $\varepsilon_0 \leftrightarrow -1/(4\pi G)$, chosen so that like masses attract (where like charges repel).

1. Apply this substitution to the electromagnetic field energy density $\rho_{\mathrm{em}} = \tfrac12(\varepsilon_0\vec E\cdot\vec E + \mu_0^{-1}\vec B\cdot\vec B)$ to obtain the gravitational field energy density $\rho_{\mathrm{grav}}$, and show it is *negative*.
2. Argue that a negative field energy density makes the theory unstable: the field can carry arbitrarily negative energy, so the vacuum is not the lowest-energy state.
3. Explain physically, using the "gravitational Poynting vector" of an oscillating mass, how the instability manifests as energy radiated *toward* the source.
4. Explain why the sign flip is *forced* (gravity attracts) and why this rules out a vector (spin-1) theory of gravity, while a scalar (spin-0) or tensor (spin-2) theory escapes the problem.

**Recall:**

![[Def - Vector and Tensor Theories of Gravity#The vector theory of gravity]]

The **electromagnetic field energy density** with respect to an observer is $\rho_{\mathrm{em}} = \tfrac12(\varepsilon_0\vec E\cdot\vec E + \mu_0^{-1}\vec B\cdot\vec B) > 0$, manifestly positive ([[Def - The Energy-Momentum Tensor]], [[Def - The Electromagnetic Field Tensor]]). With $c^2 = 1/(\varepsilon_0\mu_0)$, this is $\tfrac{\varepsilon_0}{2}(\vec E\cdot\vec E + c^2\vec B\cdot\vec B)$. Maxwell himself (1865) noted that a gravitational theory built on this model would have negative field energy.

---

# Convergent Strategy

**Problem class.** A *test-a-theory-for-theoretical-viability* problem: rather than confronting the theory with observation (as for the scalar theory), one finds an internal inconsistency — a Hamiltonian unbounded below. The computation is a sign-tracking exercise; the significance is that it kills the vector theory on theoretical grounds alone.

**Assumption pattern.** The given is the substitution $\varepsilon_0 \to -1/(4\pi G)$, which is *forced* by the requirement that gravity attract. The recognisable feature is that this substitution flips the sign of every term in the energy density, and since the electromagnetic energy was positive-definite, the gravitational one becomes negative-definite. The condition that makes this fatal is that the energy is a *kinetic* (field) energy, so its unboundedness below means runaway instability.

**Theorem routing.** Apply the substitution to $\rho_{\mathrm{em}}$ ([[Def - The Energy-Momentum Tensor]]) to get $\rho_{\mathrm{grav}} < 0$; see [[Def - Vector and Tensor Theories of Gravity]]. The instability is read off from the sign of the gravitational Poynting vector of a radiating mass, which points toward the source. The escape for even-spin theories follows from the even/odd-spin attraction/repulsion rule.

**Key decision point.** The crux is recognising that the *attractive* nature of gravity forces the sign flip, and the sign flip forces negative energy — so there is no freedom to fix it within a vector theory. The tempting "fix" — keep the electromagnetic sign for positive energy — is not available, because then like masses would repel, which is not gravity. The decision is to see that attraction and positive energy are incompatible for a vector field, which is the structural content.

---

# Legal Operations Used

1. **Read off the sign of a field energy density** (operation 8 from the topic page): the entire problem is computing $\rho_{\mathrm{grav}}$ and checking its sign, which is negative; a theory whose field energy is unbounded below is unstable.

2. **Build gravity on the electromagnetic template — but recognise the illegal sign** (illegal operation 4 from the topic page): the exercise *is* the demonstration that the electromagnetic template fails for gravity, because the sign that gives attraction gives negative energy.

---

# Hints

> [!note]- Hint 1
> Write the electromagnetic energy density as $\rho_{\mathrm{em}} = \tfrac{\varepsilon_0}{2}(\vec E\cdot\vec E + c^2\vec B\cdot\vec B)$. The substitution $\varepsilon_0 \to -1/(4\pi G)$ multiplies the whole expression by a negative number.

> [!note]- Hint 2
> $\rho_{\mathrm{grav}} = -\tfrac{1}{8\pi G}(\vec E\cdot\vec E + c^2\vec B\cdot\vec B)$. Since $\vec E\cdot\vec E \geq 0$ and $\vec B\cdot\vec B \geq 0$, this is $\leq 0$, and strictly negative wherever the field is nonzero.

> [!note]- Hint 3
> A negative field energy means the field's contribution to the total energy *decreases* as the field grows. So a configuration can lower its energy by making the field bigger — there is no ground state. For the radiating oscillator, the energy-flux vector $\vec\varphi$ points *toward* the mass, so the system gains energy as it oscillates: an instability that runs away.

> [!note]- Hint 4
> The sign flip is forced because attraction (not repulsion) is the defining feature of gravity. A general theorem of field theory: even-spin mediators (spin-0, spin-2) give attraction between like sources *with* positive energy; odd-spin mediators (spin-1) give repulsion between like sources with positive energy, so forcing them to attract flips the energy negative. Gravity is even-spin.

---

# Solution

The argument is a sign computation with a structural punchline. Step 1 applies the substitution and finds the field energy negative. Step 2 draws the stability consequence. Step 3 gives the physical picture of energy flowing the wrong way. Step 4 explains why the defect is unavoidable for spin-1 and absent for even spin. The non-obvious move is recognising that the attractive sign flip and positive energy are incompatible for a vector field.

**Step 1: The field energy density is negative.**

> [!note]- Derivation
> The electromagnetic field energy density with respect to an observer is, with $c^2 = 1/(\varepsilon_0\mu_0)$,
> $$\rho_{\mathrm{em}} = \frac12\Big(\varepsilon_0\,\vec E\cdot\vec E + \frac{1}{\mu_0}\vec B\cdot\vec B\Big) = \frac{\varepsilon_0}{2}\Big(\vec E\cdot\vec E + c^2\,\vec B\cdot\vec B\Big) > 0,$$
> manifestly positive (a sum of squares with positive coefficient). The vector theory of gravity replaces $\varepsilon_0$ by $-1/(4\pi G)$:
> $$\rho_{\mathrm{grav}} = -\frac{1}{2\cdot 4\pi G}\Big(\vec E\cdot\vec E + c^2\,\vec B\cdot\vec B\Big) = -\frac{1}{8\pi G}\Big(\vec E\cdot\vec E + c^2\,\vec B\cdot\vec B\Big).$$
> Since $\vec E\cdot\vec E \geq 0$ and $\vec B\cdot\vec B \geq 0$, this is $\rho_{\mathrm{grav}} \leq 0$, and strictly **negative** wherever the gravitational "electric" or "magnetic" field is nonzero. The field carries negative energy.

**Step 2: Negative field energy means instability.**

> [!note]- Derivation
> A physical theory requires its energy to be bounded below — there must be a lowest-energy state (the vacuum) that the system can settle into. If the field energy density is negative and can be made arbitrarily large in magnitude (by making the field large), then the total energy is unbounded below: any state can lower its energy by exciting the field further. There is no ground state, the vacuum is unstable, and the system runs away — spontaneously generating ever-larger fields and ever-more-negative energy, with the deficit going into other degrees of freedom. This is a fatal flaw: such a theory does not describe a stable world. Unlike the scalar theory, which was at least internally consistent (and failed only against observation), the vector theory is **not viable even on theoretical grounds**.

**Step 3: The radiating oscillator — energy flows toward the source.**

> [!note]- Derivation
> The instability has a vivid manifestation. Consider a mass $m$ oscillating along an axis, with acceleration collinear to its velocity, observed by an inertial observer $\mathcal{O}$. By analogy with an oscillating electric charge (which radiates electromagnetic energy *outward*), the mass radiates "gravitational" energy, and the energy-flux vector (the gravitational Poynting vector), obtained from the electromagnetic Poynting vector by the substitution $\varepsilon_0 \to -1/(4\pi G)$ and $q \to m$, is
> $$\vec\varphi = -\frac{G m^2\,\Gamma^2\sin^2\theta}{4\pi c^3 r^2(1 - \tfrac{V}{c}\cos\theta)^6}\,\vec n,$$
> where $\vec n$ points from the mass's retarded position to the observation point and $\Gamma$ is the Lorentz factor. The crucial feature is the overall **minus sign**: $\vec\varphi$ is anti-parallel to $\vec n$, so energy flows *toward* the particle, not away from it. The system "gravitational field + particle" therefore *gains* energy as the particle oscillates, feeding the oscillation, which grows without bound. This is the negative field energy in action: instead of radiating energy away and damping (as a charge does), the oscillating mass draws energy in and is destabilised.

**Step 4: Why the sign flip is forced, and why even spin escapes.**

> [!note]- Derivation
> The sign flip $\varepsilon_0 \to -1/(4\pi G)$ is **forced**, not chosen: it is what makes the force between like sources *attractive*. In electromagnetism like charges repel, and that repulsion is encoded in the positive $\varepsilon_0$; to make like masses attract, the sign must flip. But the same sign sets the sign of the field energy, so attraction and positive energy are tied together with *opposite* signs for a vector field — one cannot have both.
>
> This is a special case of a general theorem of relativistic field theory: **the spin of the mediating field determines whether like sources attract or repel, at fixed (positive) energy.** Even-spin mediators (spin-0, spin-2) produce *attraction* between like sources with positive field energy; odd-spin mediators (spin-1) produce *repulsion* between like sources with positive energy. So:
> - **Spin-1 (vector):** like sources repel with positive energy; forcing attraction flips the energy negative — fatal. Gravity is not spin-1.
> - **Spin-0 (scalar):** like sources attract with positive energy — fine (Nordström's theory has positive field energy, $\propto +(\partial\Phi)^2$); it fails only observationally (no light bending).
> - **Spin-2 (tensor):** like sources attract with positive energy — fine; this is the spin of gravity, and the Fierz-Pauli energy is positive.
>
> Both viable gravity candidates (scalar and tensor) are even-spin, and both give attraction with positive energy. The vector theory is the odd one out, and its negative energy is the price of trying to make an odd-spin field attract. The deeper reason gravity must be spin-2 (rather than spin-0): only a spin-2 field couples to the *full* energy-momentum tensor (the actual source of gravity), and only spin-2 bends light correctly.

> [!note]- Complete formal solution
> The electromagnetic field energy density $\rho_{\mathrm{em}} = \tfrac{\varepsilon_0}{2}(\vec E\cdot\vec E + c^2\vec B\cdot\vec B) > 0$ becomes, under $\varepsilon_0 \to -1/(4\pi G)$, the gravitational field energy density $\rho_{\mathrm{grav}} = -\tfrac{1}{8\pi G}(\vec E\cdot\vec E + c^2\vec B\cdot\vec B) < 0$. A negative field energy unbounded below means no ground state: the theory is unstable. Concretely, the gravitational Poynting vector of an oscillating mass, $\vec\varphi \propto -\vec n$, points toward the source, so the system gains energy and the oscillation runs away. The sign flip is forced by the attractive nature of gravity, and for a vector (spin-1) field attraction and positive energy have opposite signs, so they are incompatible — gravity cannot be spin-1. Even-spin theories (scalar spin-0, tensor spin-2) give attraction with positive energy and escape the problem; gravity is the spin-2 case, the only one coupling to the full stress tensor. $\blacksquare$

---

# Key Takeaways

**The sign of the field energy is a non-negotiable viability test, and for a vector field it clashes with attraction.** The central lesson is that a physical field theory must have energy bounded below, and this is a constraint as binding as agreement with experiment — a theory with negative kinetic energy is dead regardless of what it predicts. The trigger: whenever a field theory is proposed, compute the sign of its field energy density before anything else. For the vector theory of gravity, the attractive force law forces a sign flip that makes the energy negative, so the theory fails this most basic test. The reusable diagnostic is that "ghost" fields (negative kinetic energy) signal an inconsistent theory, and they arise generically when one tries to make a field mediate the "wrong" kind of force for its spin.

**Spin determines the sign of the force, and this is why gravity is even-spin.** The deepest structural fact this exercise teaches is the even/odd-spin attraction/repulsion rule: even-spin mediators (spin-0, spin-2) attract like sources with positive energy, odd-spin (spin-1) repel them. This single rule explains the whole pattern of §25.1 — why the scalar and tensor theories are viable (even spin, attraction, positive energy) and the vector theory is not (odd spin, forced attraction, negative energy). It also explains electromagnetism (spin-1, like charges repel) and the strong force's confinement properties. The trigger to recall it: any time the *sign* of a long-range force matters, ask the spin of the mediator. Gravity attracts universally, so its mediator is even-spin; and since it must couple to the full energy-momentum tensor, it is spin-2 — the graviton.

**Internal consistency and observational adequacy are independent failure modes, and a theory can die of either.** The scalar theory and the vector theory fail in completely different ways, and the contrast is instructive. The scalar theory is internally consistent — well-posed, positive energy, stable — but disagrees with observation (no light bending, wrong perihelion). The vector theory never even reaches the observational stage: it is internally inconsistent (negative energy, unstable), so it is rejected on theoretical grounds alone. The reusable lesson is that when evaluating a candidate theory, both tests must be applied, and they are logically independent: a theory can be beautiful and consistent yet wrong (scalar gravity), or it can be inconsistent before any data is consulted (vector gravity). Only the tensor theory passes both — and it does so by becoming general relativity, which is the subject the rest of the chapter points toward.
