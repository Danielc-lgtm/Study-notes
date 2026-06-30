---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Einstein-Poincaré Simultaneity"
  - "Def - Observer and Local Rest Space"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - The Null Cone and the Time Arrow"
tags: [physics, special-relativity]
---

# Problem Statement

An observer $\mathcal{O}$ moves on a timelike worldline $\mathcal{L}_0$ with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ ($U_0\cdot U_0 = +1$), carrying an ideal clock reading [[Def - Proper Time|proper time]]. To date an event $B$ off the worldline, $\mathcal{O}$ emits a photon at the worldline event $A_1$ (proper time $t_1$), the photon reflects at $B$, and is received back at $A_2$ (proper time $t_2$). Let $A$ be the worldline event at proper time $t$, with $B$ close enough to $\mathcal{L}_0$ that segments may be treated as straight. Work with $c = 1$.

1. Write the two null conditions on the photon legs $\overrightarrow{A_1B}$ and $\overrightarrow{A_2B}$, expanding each via Chasles' relation $\overrightarrow{A_1B} = \overrightarrow{A_1A} + \overrightarrow{AB}$.
2. Solve the resulting $2\times 2$ linear system for the two scalar products $U_0\cdot\overrightarrow{AB}$ and $\overrightarrow{AB}\cdot\overrightarrow{AB}$.
3. Deduce the **simultaneity criterion**: $B$ is simultaneous with $A$ for $\mathcal{O}$ (i.e. $U_0\cdot\overrightarrow{AB} = 0$) if and only if $t = \tfrac12(t_1 + t_2)$.
4. Confirm that this is the **radar date** convention $t = \tfrac12(t_1+t_2)$, and that the scalar square $\overrightarrow{AB}\cdot\overrightarrow{AB} = -(t-t_1)(t_2-t)$ is the (negative, hence spacelike) squared spatial length.

**Recall:**

The exercise rests on the radar definition of simultaneity, the four-velocity, and the null condition for photons.

![[Def - Einstein-Poincaré Simultaneity#The Definition]]

The [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ is the future-directed unit timelike tangent to $\mathcal{L}_0$, $U_0\cdot U_0 = +1$. A photon worldline is **null**: its displacement $N$ satisfies $N\cdot N = 0$ ([[Def - The Null Cone and the Time Arrow|the null cone]]). For two nearby worldline events $A_k$ and $A$ at proper times $t_k$ and $t$, the displacement is $\overrightarrow{A_kA} = (t - t_k)U_0(A)$ (a proper-time multiple of the four-velocity, with $c=1$).

---

# Convergent Strategy

**Problem class.** An *establish-a-criterion-from-a-construction* problem: a physical procedure (radar) is given, and the task is to extract its mathematical content (the simultaneity condition). The [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames#Problem-Solving Strategy|topic strategy]] for radar problems is to set up the null conditions on the photon legs and solve the resulting linear system for the two unknown scalar products.

**Assumption pattern.** The given data are *proper-time readings* $t_1, t_2$ and the *nullity* of the photon legs. Nullity supplies two quadratic equations; the unknowns are the two scalar products $U_0\cdot\overrightarrow{AB}$ (which encodes simultaneity) and $\overrightarrow{AB}\cdot\overrightarrow{AB}$ (which encodes distance). The signpost is "light bounced off an event and timed" — that is always radar, always two null legs.

**Theorem routing.** The two null conditions, expanded by Chasles, become two equations linear in $(U_0\cdot\overrightarrow{AB},\ \overrightarrow{AB}\cdot\overrightarrow{AB})$ once the squares $\overrightarrow{A_kA}\cdot\overrightarrow{A_kA} = (t-t_k)^2$ are computed using $U_0\cdot U_0 = +1$. Subtracting the two equations isolates $U_0\cdot\overrightarrow{AB} = -[t - \tfrac12(t_1+t_2)]$, which vanishes iff $t = \tfrac12(t_1+t_2)$ — the [[Def - Einstein-Poincaré Simultaneity|simultaneity criterion]]. Back-substitution gives $\overrightarrow{AB}\cdot\overrightarrow{AB}$.

**Key decision point.** The crux is recognising that two null legs give *exactly two* equations for *exactly two* unknown scalar products, and that the system is non-degenerate precisely because $B$ is off the worldline ($t_2\neq t_1$). The non-obvious move is to keep $\overrightarrow{AB}$ abstract (not introduce coordinates) and work entirely with scalar products — the criterion is coordinate-free, and introducing a frame would obscure it.

---

# Legal Operations Used

1. **Set up the null conditions on radar photons** (operation 3 from the topic page). The two photon legs $\overrightarrow{A_1B}$ and $\overrightarrow{A_2B}$ are null, giving $\overrightarrow{A_1B}\cdot\overrightarrow{A_1B} = 0$ and $\overrightarrow{A_2B}\cdot\overrightarrow{A_2B} = 0$; Chasles expands each into a quadratic in $\overrightarrow{AB}$.

2. **Translate simultaneity into orthogonality** (operation 2 from the topic page). The output $U_0\cdot\overrightarrow{AB} = 0$ is exactly the statement that $B$ lies in $\mathcal{O}$'s rest space, i.e. is simultaneous with $A$.

---

# Hints

> [!note]- Hint 1
> Both photon legs are null, so $\overrightarrow{A_1B}\cdot\overrightarrow{A_1B} = 0$ and $\overrightarrow{A_2B}\cdot\overrightarrow{A_2B} = 0$. Write $\overrightarrow{A_1B} = \overrightarrow{A_1A} + \overrightarrow{AB}$ and expand the square; you get three terms, one of which is $\overrightarrow{A_1A}\cdot\overrightarrow{A_1A}$.

> [!note]- Hint 2
> Use $\overrightarrow{A_kA} = (t-t_k)U_0$ and $U_0\cdot U_0 = +1$ to evaluate $\overrightarrow{A_kA}\cdot\overrightarrow{A_kA} = (t-t_k)^2$ and $\overrightarrow{A_kA}\cdot\overrightarrow{AB} = (t-t_k)\,U_0\cdot\overrightarrow{AB}$. The two null conditions then read $(t-t_k)^2 + 2(t-t_k)\,U_0\cdot\overrightarrow{AB} + \overrightarrow{AB}\cdot\overrightarrow{AB} = 0$ for $k=1,2$.

> [!note]- Hint 3
> Subtract the $k=2$ equation from the $k=1$ equation. The $\overrightarrow{AB}\cdot\overrightarrow{AB}$ terms cancel, and you are left with a linear equation in $U_0\cdot\overrightarrow{AB}$. Use $(t-t_1)^2 - (t-t_2)^2 = (t_2-t_1)(2t-t_1-t_2)$ and divide by $t_2-t_1\neq 0$.

> [!note]- Hint 4
> Having found $U_0\cdot\overrightarrow{AB} = -[t - \tfrac12(t_1+t_2)]$, set it to zero for simultaneity. Then back-substitute into either null condition to get $\overrightarrow{AB}\cdot\overrightarrow{AB}$, factoring out $(t-t_1)$ and simplifying the bracket to $t-t_2$.

---

# Solution

The proof is a clean $2\times 2$ elimination. Step 1 sets up the two null conditions and reduces them, via $U_0\cdot U_0 = +1$, to two equations in the scalar products $U_0\cdot\overrightarrow{AB}$ and $\overrightarrow{AB}\cdot\overrightarrow{AB}$. Step 2 subtracts to solve for $U_0\cdot\overrightarrow{AB}$, whose vanishing is the simultaneity criterion. Step 3 back-substitutes for the scalar square. The non-obvious move is to stay coordinate-free and treat the two scalar products as the unknowns.

**Step 1: The two null conditions become two equations in the scalar products.**

> [!note]- Derivation
> The worldline events $A_1, A, A_2$ are near each other on $\mathcal{L}_0$, so $\overrightarrow{A_kA} = (t-t_k)U_0$ (proper-time multiple of the [[Def - Four-Velocity and Four-Acceleration|four-velocity]], $c=1$). The photon legs are null:
> $$\overrightarrow{A_1B}\cdot\overrightarrow{A_1B} = 0, \qquad \overrightarrow{A_2B}\cdot\overrightarrow{A_2B} = 0.$$
> By Chasles, $\overrightarrow{A_kB} = \overrightarrow{A_kA} + \overrightarrow{AB}$, so
> $$\overrightarrow{A_kA}\cdot\overrightarrow{A_kA} + 2\,\overrightarrow{A_kA}\cdot\overrightarrow{AB} + \overrightarrow{AB}\cdot\overrightarrow{AB} = 0.$$
> Now $\overrightarrow{A_kA}\cdot\overrightarrow{A_kA} = (t-t_k)^2\,(U_0\cdot U_0) = (t-t_k)^2$ (using $U_0\cdot U_0 = +1$ — note this is $+$ in mostly-minus signature, the sign flip from Gourgoulhon), and $\overrightarrow{A_kA}\cdot\overrightarrow{AB} = (t-t_k)\,U_0\cdot\overrightarrow{AB}$. Hence
> $$(t-t_k)^2 + 2(t-t_k)\,U_0\cdot\overrightarrow{AB} + \overrightarrow{AB}\cdot\overrightarrow{AB} = 0, \qquad k = 1, 2. \tag{$\ast_k$}$$
> These are two linear equations in the unknowns $X := U_0\cdot\overrightarrow{AB}$ and $Y := \overrightarrow{AB}\cdot\overrightarrow{AB}$.

**Step 2: Subtracting gives the simultaneity criterion.**

> [!note]- Derivation
> Subtract $(\ast_2)$ from $(\ast_1)$; the $Y = \overrightarrow{AB}\cdot\overrightarrow{AB}$ terms cancel:
> $$(t-t_1)^2 - (t-t_2)^2 + 2[(t-t_1) - (t-t_2)]\,X = 0.$$
> Using $(t-t_1)^2 - (t-t_2)^2 = (t_2-t_1)(2t-t_1-t_2)$ and $(t-t_1)-(t-t_2) = t_2-t_1$,
> $$(t_2-t_1)(2t-t_1-t_2) + 2(t_2-t_1)X = 0.$$
> Since $B\notin\mathcal{L}_0$, the round trip is nondegenerate and $t_2 - t_1\neq 0$; divide by $t_2-t_1$:
> $$2t - t_1 - t_2 + 2X = 0 \quad\Longrightarrow\quad X = U_0\cdot\overrightarrow{AB} = -\Big[t - \tfrac12(t_1+t_2)\Big].$$
> Therefore $U_0\cdot\overrightarrow{AB} = 0$ **if and only if** $t = \tfrac12(t_1+t_2)$. By the [[Def - Einstein-Poincaré Simultaneity|simultaneity criterion]], $U_0\cdot\overrightarrow{AB} = 0$ means $B$ is simultaneous with $A$; equivalently $B$ lies in $\mathcal{O}$'s [[Def - Observer and Local Rest Space|local rest space]] at $A$. So radar simultaneity ($t$ the midpoint reading) coincides with metric orthogonality.

**Step 3: The scalar square and the radar date.**

> [!note]- Derivation
> Substitute $X = -[t - \tfrac12(t_1+t_2)]$ into $(\ast_1)$:
> $$Y = \overrightarrow{AB}\cdot\overrightarrow{AB} = -(t-t_1)^2 - 2(t-t_1)X = -(t-t_1)^2 + 2(t-t_1)\big[t - \tfrac12(t_1+t_2)\big].$$
> Factor out $(t-t_1)$: the bracket is $-(t-t_1) + (2t-t_1-t_2) = t - t_2$, so
> $$\overrightarrow{AB}\cdot\overrightarrow{AB} = (t-t_1)(t-t_2) = -(t-t_1)(t_2-t).$$
> Since $t_1 < t < t_2$, this is **negative**, confirming $\overrightarrow{AB}$ is spacelike — as it must be, since $B$ lies in (or near) the rest space. The squared spatial length is $\|\overrightarrow{AB}\|^2 = -\overrightarrow{AB}\cdot\overrightarrow{AB} = (t-t_1)(t_2-t)$ (this is [[Def - Synge World Function and Spatial Distance|Synge's formula]] squared, with $c=1$). The **date** of $B$ for $\mathcal{O}$ is $t = \tfrac12(t_1+t_2)$, the midpoint reading — the radar convention.

> [!note]- Complete formal solution
> With $c = 1$ and $U_0\cdot U_0 = +1$, write $\overrightarrow{A_kA} = (t-t_k)U_0$ for the worldline events. The photon legs are null, so by Chasles ($\overrightarrow{A_kB} = \overrightarrow{A_kA} + \overrightarrow{AB}$),
> $$(t-t_k)^2 + 2(t-t_k)\,U_0\cdot\overrightarrow{AB} + \overrightarrow{AB}\cdot\overrightarrow{AB} = 0, \qquad k = 1, 2.$$
> Subtracting the two equations and using $t_2 - t_1\neq 0$ gives $U_0\cdot\overrightarrow{AB} = -[t - \tfrac12(t_1+t_2)]$, which vanishes iff $t = \tfrac12(t_1+t_2)$ — so radar simultaneity (midpoint date) is exactly metric orthogonality to $U_0$, i.e. $B\in\mathcal{O}$'s local rest space. Back-substituting, $\overrightarrow{AB}\cdot\overrightarrow{AB} = (t-t_1)(t-t_2) = -(t-t_1)(t_2-t) < 0$, confirming $\overrightarrow{AB}$ is spacelike with squared spatial length $\|\overrightarrow{AB}\|^2 = (t-t_1)(t_2-t)$. The date of $B$ for $\mathcal{O}$ is the midpoint $\tfrac12(t_1+t_2)$. $\blacksquare$

---

# Key Takeaways

**Two null legs give exactly two equations for the two scalar products that encode "where" and "when".** The entire radar construction is a $2\times 2$ linear system. The reason it works so cleanly is a perfect match of counts: a photon round trip provides two null conditions (one per leg), and the two physically meaningful unknowns — the temporal scalar product $U_0\cdot\overrightarrow{AB}$ (which says whether $B$ is simultaneous) and the spatial scalar square $\overrightarrow{AB}\cdot\overrightarrow{AB}$ (which says how far $B$ is) — are exactly two. Whenever you see "light emitted, reflected, and received, timed by a single clock", set up the two null conditions and solve for these two scalar products; subtracting the equations isolates the temporal one (simultaneity), back-substituting gives the spatial one (distance). This single template underlies dating, the rest space, Synge's distance, and Born rigidity — they are all readings of the same experiment.

**Simultaneity is metric orthogonality, and the radar midpoint is how you measure it.** The deep content of the computation is that the operational midpoint rule $t = \tfrac12(t_1+t_2)$ is *equivalent* to the coordinate-free condition $U_0\cdot\overrightarrow{AB} = 0$. This is the bridge from a procedure to a geometric statement: "simultaneous" means "orthogonal to the four-velocity", and the radar experiment is the physical realisation of that orthogonality. The transferable diagnostic is that any time a problem mentions "now", "at the same time", or "simultaneous", you may replace it by the algebraic equation $U_0\cdot\overrightarrow{(\,\cdot\,)} = 0$ — and conversely, any orthogonality-to-$U_0$ condition has a concrete radar protocol behind it. Keeping both the procedure and the equation in mind is what lets you move freely between the experimentalist's and the geometer's pictures.

**Watch the signature in the scalar square — the sign that confirms "spacelike" is the sign that flips between conventions.** The computation hinged on $U_0\cdot U_0 = +1$ (our mostly-minus convention), which made $\overrightarrow{A_kA}\cdot\overrightarrow{A_kA} = +(t-t_k)^2$; Gourgoulhon's $\vec u\cdot\vec u = -1$ would give the opposite sign throughout, and the final $\overrightarrow{AB}\cdot\overrightarrow{AB} = -(t-t_1)(t_2-t)$ would come out positive (since for him spacelike means positive norm). The numerical *distance* $\|\overrightarrow{AB}\| = \sqrt{(t-t_1)(t_2-t)}$ is convention-independent, but the *sign* of the scalar square is not — and forgetting to track it is the single most common error in this chapter. The reusable discipline: always check that a vector you expect to be spacelike comes out with $X\cdot X < 0$ in mostly-minus (or $> 0$ in mostly-plus), and if it does not, you have dropped a sign in the four-velocity normalisation. This habit catches projector-sign errors, distance-formula errors, and decomposition-sign errors throughout the chapter.
