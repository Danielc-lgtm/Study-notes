---
type: exercise
subject: thermodynamics
difficulty: "⭐⭐"
prereqs:
  - "Def - Caratheodory's Principle (Inaccessibility)"
  - "Def - Heat 1-Form and Work 1-Form"
  - "Def - The First Law of Thermodynamics"
  - "Def - Adiabatic Process and Adiabatic Distribution"
tags: [physics, thermodynamics, second-law]
---

# Problem Statement

**Kelvin's statement of the second law of thermodynamics:** No quasistatic cyclic process can absorb heat from a single thermal reservoir and convert it entirely into mechanical work.

**Caratheodory's statement:** In every neighbourhood of every equilibrium state, there exist states that are not adiabatically accessible.

Prove that **Kelvin's statement implies Caratheodory's statement** for any thermodynamic system with $\delta Q \neq 0$ on isochores (the system can absorb or release heat at constant volume).

*Strategy:* Given a state $x$, consider the isochore (constant-volume curve) through $x$, parametrised by internal energy $U$. Show that if Kelvin's principle holds, then states on this isochore differing from $x$ in $U$ cannot all be reached from $x$ adiabatically — establishing the existence of inaccessible nearby states.

**Recall:**

[[Def - Caratheodory's Principle (Inaccessibility)|Caratheodory's principle]] requires inaccessible nearby states in every neighbourhood.

[[Def - Adiabatic Process and Adiabatic Distribution|Adiabatic processes]] satisfy $\delta Q = 0$ along the path. Along an [[Def - Quasistatic Process|isochore]] ($dV = 0$), $\delta W = 0$ and $\delta Q = dU$ — heating at constant volume directly increases $U$.

The [[Def - The First Law of Thermodynamics|first law]]: $dU = \delta Q - \delta W$, so $\oint \delta Q = \oint \delta W$ around any closed cycle.

---

# Convergent Strategy

**Problem class:** A logical implication problem of the form "axiom A implies axiom B". The recurring pattern: assume the conclusion fails (some nearby state IS accessible), construct a cycle that violates Kelvin, hence the original assumption (Kelvin holds) forces the conclusion (Caratheodory holds).

**Assumption pattern:** Kelvin's statement is given. The system has a well-defined isochore through $x$ along which heat can be exchanged (since $\delta Q \neq 0$ on isochores). The state space is connected enough to allow constructing the cycle.

**Theorem routing:** Proof by contrapositive — assume Caratheodory fails, construct a cycle that contradicts Kelvin. The cycle uses two arcs: (i) the isochore from $x$ to some $y$ on the same isochore with $U(y) < U(x)$ (cooling at constant volume, releasing heat to a reservoir), then (ii) a hypothetical adiabatic path from $y$ back to $x$ (which we assumed exists, contradicting Caratheodory). Compute the net work done and net heat absorbed; the cycle violates Kelvin if the heat is absorbed at a single reservoir and converted entirely to work.

**Key decision point:** The non-obvious choice is which point $y$ on the isochore to choose: the proof works for any $y$ with $U(y) < U(x)$, and the *cooling* leg from $x$ to $y$ is what releases heat to the reservoir (heat that would then be converted to work on the hypothetical adiabatic return path). Choosing $U(y) > U(x)$ instead would not give the contradiction — the direction of the isochore traversal matters.

---

# Legal Operations Used

1. **Operation 1 from the topic page (split a 1-form using the first law).** Along the isochore, $\delta Q = dU$, allowing direct calculation of heat exchanged.

2. **Operation 6 from the topic page (integrate along an adiabat).** Along the hypothesised adiabatic return path, $\delta Q = 0$, so $dU = -\delta W$, allowing computation of net work.

3. **Operation 3 from the topic page (restrict 1-forms to processes).** Each leg of the cycle has a specific restriction (isochoric vs adiabatic) that simplifies the integral.

---

# Hints

> [!note]- Hint 1
> Suppose Caratheodory's principle fails at some state $x$: there exists a neighbourhood in which *every* nearby state is adiabatically accessible from $x$. In particular, on the isochore through $x$, every nearby state with different $U$ is adiabatically accessible.

> [!note]- Hint 2
> Choose a nearby state $y$ on the isochore through $x$ with $U(y) < U(x)$. By the assumption (Caratheodory fails), there is a quasistatic adiabatic path $\gamma_{\text{adi}}$ from $y$ to $x$. Also, the isochore from $x$ to $y$ (cooling at constant volume) is a quasistatic path $\gamma_{\text{iso}}$, with $\delta W = 0$ and $\delta Q = dU$, releasing heat $Q_{\text{out}} = U(x) - U(y) > 0$ to the reservoir.

> [!note]- Hint 3
> Concatenate: traverse $\gamma_{\text{iso}}$ from $x$ to $y$ (cooling, releasing $Q_{\text{out}}$ to reservoir), then $\gamma_{\text{adi}}$ from $y$ back to $x$ (no heat exchanged). This is a closed cycle.
>
> Around the closed cycle: $\oint dU = 0$ (since $U$ is a state function), so $\oint \delta Q = \oint \delta W$. The total heat absorbed is $-Q_{\text{out}}$ (heat *released* to the single reservoir, so absorbed is negative). Hence net work done is also $-Q_{\text{out}} < 0$ — net work is done *on* the gas by the cycle.

> [!note]- Hint 4
> Reverse the cycle: traverse $\gamma_{\text{adi}}^{-1}$ (from $x$ to $y$, still adiabatic), then $\gamma_{\text{iso}}^{-1}$ (from $y$ to $x$, *heating* at constant volume, absorbing $Q_{\text{out}}$ from the same reservoir).
>
> Around the reversed cycle: net heat absorbed = $+Q_{\text{out}} > 0$ (from the single reservoir), net work done by the gas = $+Q_{\text{out}} > 0$ (by the first law). But this is *exactly* Kelvin's forbidden process: a cyclic process absorbing heat from a single reservoir and converting it entirely to work. Contradiction.

---

# Solution

The proof is by contrapositive in three steps. Step 1 negates Caratheodory's principle and chooses a specific nearby state $y$. Step 2 constructs the cycle using the isochore (heating leg) and the hypothesised adiabatic return. Step 3 shows the cycle violates Kelvin's statement, completing the contrapositive. The non-obvious move is in Step 3: reversing the cycle direction to make the heat absorption (and work output) positive — converting the contradiction into Kelvin's exact forbidden form.

**Step 1: Negate Caratheodory's principle.**

> [!note]- Derivation
> Suppose Caratheodory's principle is *false* at some state $x \in M$. Then there is an open neighbourhood $U$ of $x$ such that every $y \in U$ is adiabatically accessible from $x$ — every nearby state can be reached by a quasistatic adiabatic path.
>
> In particular, on the isochore through $x$ (the fibre $\pi^{-1}(\pi(x))$ in the submersion of the [[Def - Thermodynamic State Space|state space]]), there exists a nearby state $y$ with $U(y) < U(x)$ (a state with lower internal energy on the same volume coordinate) such that $y$ is adiabatically accessible from $x$. Let $\gamma_{\text{adi}}$ be a quasistatic adiabatic path from $x$ to $y$.

**Step 2: Construct the cycle.**

> [!note]- Derivation
> Concatenate two paths:
> - $\gamma_{\text{iso}}$: heating along the isochore from $y$ to $x$. Along this path $dV = 0$, so $\delta W = p\, dV = 0$. By the first law, $\delta Q = dU$, and integrating: $Q_{\text{in}} := \int_{\gamma_{\text{iso}}} \delta Q = U(x) - U(y) > 0$. The system absorbs heat $Q_{\text{in}}$ from a single reservoir (the one whose temperature matches the system's during this isochoric heating).
> - $\gamma_{\text{adi}}$: adiabatic return from $x$ to $y$. Along this path $\delta Q = 0$, so $\int_{\gamma_{\text{adi}}} \delta Q = 0$. The work done is $W := \int_{\gamma_{\text{adi}}} \delta W = -(U(y) - U(x)) = U(x) - U(y) = Q_{\text{in}}$ (using the first law $dU = -\delta W$ along the adiabat).
>
> The concatenated path $\gamma = \gamma_{\text{iso}} + \gamma_{\text{adi}}$ is a closed quasistatic cycle from $y$ back to $y$.

**Step 3: The cycle violates Kelvin's statement.**

> [!note]- Derivation
> Around the closed cycle $\gamma$:
> - Total heat absorbed: $\oint_\gamma \delta Q = Q_{\text{in}} + 0 = Q_{\text{in}} > 0$, all of it from a single reservoir during the isochoric heating leg.
> - Total work done: $\oint_\gamma \delta W = 0 + W = U(x) - U(y) = Q_{\text{in}} > 0$.
> - $\oint dU = 0$ (since $U$ is a state function on a closed loop).
>
> The cycle absorbs heat $Q_{\text{in}}$ from a single reservoir and converts *all* of it to work — exactly the process Kelvin's statement forbids.
>
> So the assumption that Caratheodory's principle is false at $x$ leads to a violation of Kelvin's statement at $x$. By contrapositive, Kelvin's statement implies Caratheodory's principle.

> [!note]- Complete formal solution
> Suppose Caratheodory's principle fails at $x$: there is a nearby state $y$ on the isochore through $x$ with $U(y) < U(x)$ that is adiabatically accessible from $x$ via $\gamma_{\text{adi}}$.
>
> Consider the cycle: heat the gas along the isochore from $y$ to $x$ (absorbing $Q_{\text{in}} = U(x) - U(y) > 0$ from a single reservoir, no work done), then return adiabatically from $x$ to $y$ (no heat exchanged, work done $W = U(x) - U(y) = Q_{\text{in}}$).
>
> Around the closed cycle: $\oint \delta Q = Q_{\text{in}}$ (all from one reservoir), $\oint \delta W = Q_{\text{in}}$ (net work output). The cycle converts heat from a single reservoir entirely to work — forbidden by Kelvin. Contradiction.
>
> So Caratheodory's principle holds at every $x$, given Kelvin's statement.

---

# Key Takeaways

**Kelvin's principle is *stronger* than Caratheodory's principle.** Both are formulations of the second law, but Caratheodory's is purely geometric (no mention of cycles, reservoirs, work) and is logically weaker. The implication Kelvin ⇒ Caratheodory is one-way; the converse (Caratheodory ⇒ Kelvin) is true for "simple" thermodynamic systems but requires additional connectivity hypotheses on the adiabatic foliation. The two are equivalent for the systems Frankel considers. The advantage of Caratheodory's formulation is geometric clarity: it converts directly to a Frobenius integrability condition on $\delta Q$, whereas Kelvin's requires a roundabout argument about cyclic engines.

**The proof uses the fundamental structure of cycles: isochore plus adiabatic = closed loop with net work output.** This is the basic structure of any heat engine: heating raises the energy, adiabatic expansion converts it to work. The cycle in the proof is degenerate (the engine reduces to an isochoric heat absorption followed by an adiabatic expansion — no isothermal expansion to do work efficiently), but the structural pattern is what every heat engine cycle uses. Recognising "isochore plus adiabatic = work-extracting loop" is the cycle-design intuition behind the Otto cycle (internal combustion engine), the Stirling cycle, and many others.

**The geometric content: adiabatic accessibility across the isochore is forbidden by Kelvin.** Frankel's geometric picture: the isochores are transverse curves to the adiabatic distribution, and Kelvin's principle says you cannot adiabatically jump from one point of an isochore to another (in either direction). Combined with Caratheodory's principle (no adiabatic accessibility of nearby off-isochore states either), this forces the adiabatic distribution to be integrable: the adiabatic surfaces *partition* the state space, and the isochores transversely cut across this partition. The transversal structure is what allows the global entropy construction in [[Thm - The Heat 1-Form is Integrable]]: every adiabatic leaf meets the basic transversal exactly once, and the entropy is the parameter of that intersection.
