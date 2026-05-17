---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Conservation of Four-Momentum"
  - "Def - The Four-Momentum of a Photon"
  - "Def - Four-Momentum and Rest Mass"
  - "Def - Rapidity"
tags: [physics, special-relativity]
---

# Problem Statement

A **photon rocket** propels itself by converting part of its rest mass into photons and emitting them directly backwards. Initially the rocket is at rest with rest mass $M_0$. After some time it has rest mass $M$ (less than $M_0$, since mass has been spent) and moves at speed $v$ in the original rest frame.

**(a)** By applying conservation of four-momentum to the whole closed system (rocket plus all emitted photons), derive the relation between the rocket's rest mass and its speed. Show that
$$\frac{M_0}{M} \;=\; \sqrt{\frac{1+v/c}{1-v/c}} \;=\; e^{\phi},$$
where $\phi$ is the [[Def - Rapidity|rapidity]] corresponding to the final speed $v$.

**(b)** Hence find the final speed $v$ as a function of the mass ratio $M_0/M$, and determine what fraction of the initial rest mass must be converted to photons to reach $v = 0.99\,c$.

**(c)** Compare with the **Newtonian (Tsiolkovsky) rocket equation** $v = u_{\text{ex}}\ln(M_0/M)$, where $u_{\text{ex}}$ is the exhaust speed. In what sense is the result of (a) the relativistic analogue, with the exhaust "speed" equal to $c$?

**Recall:**

![[Thm - Conservation of Four-Momentum#Statement]]

![[Def - The Four-Momentum of a Photon#The Definition]]

A photon has a null four-momentum, $P_\gamma\cdot P_\gamma = 0$, with $E = |\mathbf{p}|c$. The [[Def - Rapidity|rapidity]] $\phi$ of speed $v$ satisfies $v = c\tanh\phi$, $\gamma = \cosh\phi$, $\gamma v/c = \sinh\phi$; rapidities of collinear boosts add.

---

# Convergent Strategy

**Problem class.** This is a *variable-mass* problem solved by conservation of four-momentum for a *closed system*. The rocket alone has changing rest mass; the rocket-plus-exhaust system is closed.

**Assumption pattern.** The rocket loses rest mass, so the single-particle [[Thm - The Relativistic Equation of Motion|equation of motion]] $F^\mu = dP^\mu/d\tau$ does not apply to the rocket. The closed system — rocket plus all emitted photons — has no external force, so its total four-momentum is conserved.

**Theorem routing.** [[Thm - Conservation of Four-Momentum|Conservation of four-momentum]] for the closed system: $P^\mu_{\text{rocket, initial}} = P^\mu_{\text{rocket, final}} + P^\mu_{\text{all photons}}$. The photons all travel backwards, so their total four-momentum is null and known up to one scalar. Squaring eliminates the photon total, leaving a relation between the rocket's initial and final four-momenta.

**Key decision point.** Two insights. First, *the system to which conservation applies is the closed one* — rocket plus exhaust. Second, *the photon exhaust is a single null four-vector*: all photons go backwards, so their total four-momentum is null, and isolating-and-squaring it (it squares to zero) eliminates it cleanly. The rapidity form $M_0/M = e^\phi$ then exposes the structure: rapidity adds logarithmically with mass, exactly as Newtonian velocity does.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Special Relativity II — Relativistic Kinematics and Dynamics#Legal Operations|the topic page's Legal Operations]]:

1. **Write down the total four-momentum and set it equal before and after** — conservation of four-momentum for the closed rocket-plus-photons system.
2. **Square a four-momentum to extract an invariant mass** — isolating and squaring the photon exhaust (which squares to zero).
3. **Use the photon's null four-momentum** — the total exhaust four-momentum is null.
4. **Use a Lorentz invariant** — the rocket's rest mass and the inner products are evaluated in the convenient (initial rest) frame.

---

# Hints

> [!note]- Hint 1
> The rocket's rest mass changes, so you cannot apply $F^\mu = dP^\mu/d\tau$ to the rocket alone. What is the *closed* system whose total four-momentum is conserved?

> [!note]- Hint 2
> Closed system = rocket + all emitted photons. Conservation of four-momentum in the initial rest frame: $P_{\text{rocket}}^{\text{initial}} = P_{\text{rocket}}^{\text{final}} + P_{\text{photons}}^{\text{total}}$. The photons all go backwards (in $-x$), so their total four-momentum is $Q^\mu = (Q/c)(1,-1,0,0)$ for some $Q > 0$, and $Q\cdot Q = 0$.

> [!note]- Hint 3
> Isolate the photon total: $P_{\text{photons}} = P_{\text{rocket}}^{\text{initial}} - P_{\text{rocket}}^{\text{final}}$. Square both sides. The left is $0$ (null). The right gives a relation between $M_0$, $M$, and the rocket's final energy/momentum.

> [!note]- Hint 4
> Initial rocket: $P^{\text{initial}} = (M_0c,\mathbf{0})$. Final rocket: $P^{\text{final}} = (M\gamma c, M\gamma v, 0, 0)$. After squaring and simplifying, you will get $M_0^2 = M^2 + 2M_0(M\gamma - M\gamma v/c\cdot 0)$... carefully: use $P^{\text{init}}\cdot P^{\text{final}} = M_0\cdot M\gamma c\cdot c = M_0 M\gamma c^2$.

---

# Solution

The rocket alone is a variable-mass system, so conservation of four-momentum is applied to the *closed* system of rocket plus exhaust. The exhaust is a single backward-pointing null four-vector; isolating and squaring it eliminates it, and the surviving relation, written in rapidity, is the relativistic Tsiolkovsky equation.

**Step 1: Set up conservation of four-momentum for the closed system.**

In the initial rest frame, $P^{\text{init}}_{\text{rocket}} = P^{\text{final}}_{\text{rocket}} + Q$, where $Q^\mu$ is the total four-momentum of all emitted photons, a null four-vector pointing backwards.

> [!note]- Derivation
> The rocket converts rest mass into photons and ejects them backwards. Because the rocket's rest mass is *not* constant, the single-particle [[Thm - The Relativistic Equation of Motion|equation of motion]] $F^\mu = dP^\mu/d\tau$ does not apply to the rocket on its own. What *is* closed — no external force, nothing entering or leaving — is the system consisting of the rocket *together with every photon it has emitted*. For that closed system, [[Thm - Conservation of Four-Momentum|conservation of four-momentum]] holds exactly:
> $$P^{\text{init}}_{\text{rocket}} = P^{\text{final}}_{\text{rocket}} + Q,$$
> where $Q^\mu = \sum P_{\gamma}^\mu$ is the total four-momentum of all the emitted photons.
>
> Work in the **initial rest frame** of the rocket, with the rocket accelerating in the $+x$ direction and the photons therefore all emitted in the $-x$ direction. The four-momenta are:
> - Initial rocket, at rest with rest mass $M_0$: $\;P^{\text{init}}_{\text{rocket}} = (M_0c,\ 0,0,0)$.
> - Final rocket, rest mass $M$, speed $v$, $\gamma = (1-v^2/c^2)^{-1/2}$: $\;P^{\text{final}}_{\text{rocket}} = (M\gamma c,\ M\gamma v,\ 0,0)$.
> - All photons travel in $-x$, so each has four-momentum $(\epsilon/c)(1,-1,0,0)$; their sum is $\;Q^\mu = \dfrac{Q}{c}(1,-1,0,0)$ for some total photon energy $Q > 0$. Crucially $Q\cdot Q = (Q/c)^2 - (Q/c)^2 = 0$ — **the total photon four-momentum is null**, even though it is a sum of many photons, because they are all parallel.

**Step 2: Isolate and square the photon exhaust.**

Isolating $Q = P^{\text{init}} - P^{\text{final}}$ and squaring ($Q\cdot Q = 0$) gives $M_0^2c^2 = M^2c^2 + 2P^{\text{init}}\cdot P^{\text{final}}\cdot(-1)$... yielding $M_0 M\gamma(1) = $ — see below.

> [!note]- Derivation
> Isolate the photon total:
> $$Q = P^{\text{init}}_{\text{rocket}} - P^{\text{final}}_{\text{rocket}}.$$
> Square both sides. The left side is null: $Q\cdot Q = 0$. The right side:
> $$0 = (P^{\text{init}} - P^{\text{final}})^2 = P^{\text{init}}\cdot P^{\text{init}} - 2\,P^{\text{init}}\cdot P^{\text{final}} + P^{\text{final}}\cdot P^{\text{final}}.$$
> Use the [[Def - Four-Momentum and Rest Mass|mass shells]]: $P^{\text{init}}\cdot P^{\text{init}} = M_0^2c^2$ (initial rest mass $M_0$), $P^{\text{final}}\cdot P^{\text{final}} = M^2c^2$ (final rest mass $M$). The cross term, in the initial rest frame:
> $$P^{\text{init}}\cdot P^{\text{final}} = (M_0c)(M\gamma c) - (0)(M\gamma v) = M_0 M\gamma c^2.$$
> Substituting:
> $$0 = M_0^2c^2 - 2M_0M\gamma c^2 + M^2c^2 \;\Longrightarrow\; M_0^2 + M^2 = 2M_0M\gamma.$$
> Solve for $\gamma$:
> $$\gamma = \frac{M_0^2 + M^2}{2M_0M} = \frac{1}{2}\Big(\frac{M_0}{M} + \frac{M}{M_0}\Big).$$
> This already relates the rocket's speed (through $\gamma$) to the mass ratio. (Note this matches the standard photon-rocket result $\gamma = \tfrac12(M_0/M + M/M_0)$.)

**Step 3: Rewrite in rapidity form (part a).**

The mass ratio is $M_0/M = e^\phi = \sqrt{(1+v/c)/(1-v/c)}$.

> [!note]- Derivation
> Introduce the [[Def - Rapidity|rapidity]] $\phi$ of the final speed, defined by $v = c\tanh\phi$, so that $\gamma = \cosh\phi$. The relation from Step 2 becomes
> $$\cosh\phi = \frac{1}{2}\Big(\frac{M_0}{M} + \frac{M}{M_0}\Big).$$
> But $\cosh\phi = \tfrac12(e^\phi + e^{-\phi})$. Comparing, the obvious solution is
> $$\frac{M_0}{M} = e^{\phi}, \qquad \frac{M}{M_0} = e^{-\phi}.$$
> (This is the right root: $M_0 > M$ since mass is spent, and $\phi > 0$ since the rocket speeds up, so $M_0/M = e^\phi > 1$. ✓) Now convert $e^\phi$ back to velocity. Since $v/c = \tanh\phi = (e^\phi - e^{-\phi})/(e^\phi + e^{-\phi})$, a short rearrangement gives $e^{2\phi} = (1+v/c)/(1-v/c)$, hence
> $$\boxed{\;\frac{M_0}{M} = e^{\phi} = \sqrt{\frac{1+v/c}{1-v/c}}\;}$$
> The rocket's rapidity grows as the *logarithm* of the mass ratio: $\phi = \ln(M_0/M)$.

**Step 4: Final speed and the mass budget (part b).**

$v/c = \dfrac{(M_0/M)^2 - 1}{(M_0/M)^2 + 1}$; reaching $v = 0.99c$ requires converting about $93\%$ of the initial rest mass to photons.

> [!note]- Derivation
> Invert $M_0/M = \sqrt{(1+v/c)/(1-v/c)}$. Squaring, $(M_0/M)^2 = (1+v/c)/(1-v/c)$; solving for $v/c$,
> $$\frac{v}{c} = \frac{(M_0/M)^2 - 1}{(M_0/M)^2 + 1} = \tanh\!\big(\ln(M_0/M)\big).$$
> For $v = 0.99c$: solve $(M_0/M)^2 = (1+0.99)/(1-0.99) = 1.99/0.01 = 199$, so
> $$\frac{M_0}{M} = \sqrt{199}\approx 14.1.$$
> The rocket retains a fraction $M/M_0 = 1/\sqrt{199}\approx 0.071$ of its initial rest mass — only about $7\%$. The remaining $\approx 93\%$ has been converted into photons. Reaching even $99\%$ of the speed of light demands annihilating the overwhelming bulk of the ship's mass into light; this is the brutal arithmetic that makes a true photon rocket a thought experiment rather than an engineering proposal.

**Step 5: Comparison with the Tsiolkovsky equation (part c).**

> [!note]- Derivation
> The Newtonian **Tsiolkovsky rocket equation** is
> $$v_{\text{Newton}} = u_{\text{ex}}\ln\frac{M_0}{M},$$
> where $u_{\text{ex}}$ is the speed of the exhaust relative to the rocket. It says the *velocity* gained is the exhaust speed times the logarithm of the mass ratio.
>
> Our relativistic result, in rapidity form, is
> $$\phi = \ln\frac{M_0}{M}.$$
> The structural parallel is exact, provided one replaces *velocity* by *rapidity*. Rapidity is the relativistic quantity that genuinely *adds* under successive boosts (velocities do not — see [[Thm - Relativistic Velocity Addition]]), so it is the correct relativistic analogue of Newtonian velocity, which adds. The relativistic rocket equation says: the *rapidity* gained equals (exhaust rapidity) $\times\ln(M_0/M)$, and for a **photon** rocket the exhaust is light, moving at $c$, whose rapidity is "infinite" in the sense that the exhaust four-momentum is null — the per-unit-mass momentum transfer is maximal. Concretely, the photon rocket achieves $\phi = 1\cdot\ln(M_0/M)$: it is the maximally efficient rocket, the exhaust carrying away momentum at the largest possible rate per unit energy ($|\mathbf{p}| = E/c$).
>
> In the low-speed limit $\phi\approx v/c$, so $\phi = \ln(M_0/M)$ becomes $v\approx c\ln(M_0/M)$ — the Tsiolkovsky equation with exhaust speed $u_{\text{ex}} = c$, as it must. The relativistic photon-rocket equation is the Tsiolkovsky equation with *velocity promoted to rapidity* and *exhaust speed set to $c$*.

> [!note]- Complete formal solution
> The closed system is rocket plus all emitted photons; conservation of four-momentum holds for it. In the initial rest frame, $P^{\text{init}} = (M_0c,\mathbf{0})$, $P^{\text{final}} = (M\gamma c, M\gamma v,0,0)$, and the photon total $Q = P^{\text{init}} - P^{\text{final}}$ is null. Squaring,
> $$0 = Q\cdot Q = M_0^2c^2 - 2M_0M\gamma c^2 + M^2c^2 \;\Longrightarrow\; \gamma = \frac{1}{2}\Big(\frac{M_0}{M}+\frac{M}{M_0}\Big).$$
> With $\gamma = \cosh\phi$ and $v = c\tanh\phi$, this gives $M_0/M = e^\phi = \sqrt{(1+v/c)/(1-v/c)}$, i.e. $\phi = \ln(M_0/M)$. Inverting, $v/c = [(M_0/M)^2-1]/[(M_0/M)^2+1]$; for $v=0.99c$, $M_0/M = \sqrt{199}\approx14.1$, so $\approx 93\%$ of the rest mass is converted to photons. The relation $\phi = \ln(M_0/M)$ is the Tsiolkovsky equation with velocity replaced by rapidity and exhaust speed equal to $c$. $\blacksquare$

---

# Key Takeaways

**For a variable-mass problem, apply conservation of four-momentum to the closed system, not the equation of motion to the rocket.** The instinct is to write $F^\mu = dP^\mu/d\tau$ for the rocket — but that single-particle law assumes *constant* rest mass, and a rocket's whole purpose is to shed mass. The correct move is to identify the genuinely *closed* system, here rocket-plus-all-exhaust, for which no external force acts and [[Thm - Conservation of Four-Momentum|four-momentum is conserved exactly]]. This is a general principle: whenever a problem involves a body whose rest mass changes — a rocket, a decaying nucleus, an evaporating drop — do not chase the body with an equation of motion; enlarge the system until it is closed, then conserve the total four-momentum. The variable-mass difficulty dissolves because the *total* four-momentum of the closed system is constant even as it is redistributed among the parts.

**A collinear bundle of photons is a single null four-vector — treat the exhaust as one object.** The rocket emits enormously many photons, but they all travel backwards, so their total four-momentum $Q^\mu$ is a sum of parallel null vectors, which is itself null: $Q\cdot Q = 0$. This is what makes the problem tractable — we never track individual photons, only the one null four-vector $Q^\mu$, and isolating and squaring it (it squares to zero) eliminates the entire exhaust in one stroke. The lesson generalises: a stream of collinear massless particles behaves, for four-momentum bookkeeping, exactly like a single photon, and any process emitting radiation in one direction can have that radiation lumped into a single null four-momentum. (Contrast [[Ex - Pair production and the photon-photon threshold|non-parallel photons]], whose sum is timelike — direction matters.)

**Rapidity is the relativistic velocity, and the rocket equation is Tsiolkovsky with velocity promoted to rapidity.** The headline result $\phi = \ln(M_0/M)$ is the Newtonian Tsiolkovsky equation $v = u_{\text{ex}}\ln(M_0/M)$ with one substitution: Newtonian velocity becomes relativistic rapidity. This is no accident. Velocities do not add relativistically, but rapidities do, and a rocket gains speed by a sequence of infinitesimal boosts — each emission is a small boost in the instantaneous rest frame — so the quantity that accumulates linearly is the rapidity, not the velocity. The Tsiolkovsky derivation sums infinitesimal velocity increments; its relativistic version sums infinitesimal *rapidity* increments, giving $\phi = \ln(M_0/M)$. Whenever a Newtonian result involves adding up velocity increments — rockets, successive collisions, drift — its relativistic form is the same equation with rapidity in place of velocity, because rapidity is the additive one. And the photon rocket, exhausting at $c$, is the optimal case: light carries the most momentum per unit energy, so a photon rocket extracts the maximum rapidity per unit mass spent.
