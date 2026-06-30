---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Angular Momentum Four-Tensor"
  - "Thm - Conservation of Angular Momentum"
  - "Def - Four-Momentum and Rest Mass"
tags: [physics, special-relativity]
---

# Problem Statement

The [[Def - Angular Momentum Four-Tensor|angular momentum]] of a system $\mathscr{S}$ about an event $C$ is the two-form $J_C|_\Sigma = \sum_a\overrightarrow{CM_a}^\flat\wedge p_a$, summed over particles on a spacelike hypersurface $\Sigma$. Working with $c = 1$:

1. Derive the **change-of-origin rule**: if the reference event is moved from $C$ to $C'$, then $J_{C'}|_\Sigma = J_C|_\Sigma + \overrightarrow{C'C}^\flat\wedge P$, where $P = \sum_a p_a$ is the total four-momentum.
2. Deduce that the angular momentum about a point is independent of the point if and only if the total four-momentum vanishes, $P = 0$.
3. For a system with $P\ne 0$, show that there exists a one-parameter family of reference points (a line in the direction of $P$) about which the angular momentum two-form takes the same value, and characterise that line.
4. Use the change-of-origin rule to show that the angular momentum about the [[Def - Centre of Inertia|centre of inertia]] $G$, namely $J_G$, is the part of the angular momentum that is independent of the reference point — the [[Def - Spin Four-Vector|spin]].

**Recall:**

![[Def - Angular Momentum Four-Tensor#The Definition]]

The exterior product is bilinear: $(a + b)\wedge c = a\wedge c + b\wedge c$. Chasles' relation for displacements: $\overrightarrow{C'M} = \overrightarrow{C'C} + \overrightarrow{CM}$. The total four-momentum is $P = \sum_a p_a$, conserved for an isolated system ([[Thm - Conservation of Angular Momentum]]).

---

# Convergent Strategy

**Problem class.** A *change-of-reference-point* algebra problem. The [[Special Relativity XIV — Angular Momentum and Spin#Problem-Solving Strategy|topic strategy]] says: moving the reference point shifts the angular momentum by the wedge of the displacement with the *total* four-momentum, and the part that does not shift is the spin.

**Assumption pattern.** The angular momentum is a sum of wedges $\overrightarrow{CM_a}^\flat\wedge p_a$. The signpost is "the reference point is being moved": this is operation 3 of the topic page, and the entire derivation is bilinearity of the wedge plus Chasles' relation.

**Theorem routing.** Part 1 uses Chasles and bilinearity. Part 2 reads off the condition for the shift to vanish. Part 3 finds the directions of displacement that kill the shift. Part 4 specialises to $C = G$, routing to the [[Thm - König Theorem (Relativistic)|König decomposition]] and the definition of [[Def - Spin Four-Vector|spin]].

**Key decision point.** The crux is recognising that the shift $\overrightarrow{C'C}^\flat\wedge P$ uses the *total* four-momentum, not the individual momenta — so the change of origin acts only on the "orbital" part and leaves the spin untouched. This is what makes the spin point-independent.

---

# Legal Operations Used

1. **Operation 3 from the topic page (change the reference point with the inhomogeneous rule).** The entire exercise is the derivation and exploitation of this rule.

2. **Operation 5 from the topic page (strip orbital from spin via König).** Part 4 uses the change-of-origin rule to isolate the spin as the $C$-independent angular momentum about $G$.

---

# Hints

> [!note]- Hint 1
> For each particle, write $\overrightarrow{C'M_a} = \overrightarrow{C'C} + \overrightarrow{CM_a}$ (Chasles), then expand $\overrightarrow{C'M_a}^\flat\wedge p_a$ by bilinearity of the wedge. The term $\overrightarrow{C'C}^\flat\wedge p_a$ has a common factor $\overrightarrow{C'C}^\flat$; sum it over $a$.

> [!note]- Hint 2
> The shift is $\overrightarrow{C'C}^\flat\wedge P$. This vanishes for *all* choices of $C'$ if and only if $P = 0$ (since $\overrightarrow{C'C}$ can point in any direction). If $P\ne 0$, the shift is nonzero for displacements not parallel to $P$.

> [!note]- Hint 3
> The wedge $\overrightarrow{C'C}^\flat\wedge P$ vanishes when $\overrightarrow{C'C}$ is parallel to $P$ (the wedge of parallel vectors is zero). So all points $C'$ on the line through $C$ in the direction of $P$ give the same angular momentum.

> [!note]- Hint 4
> The centre of inertia $G$ is the point about which the orbital angular momentum vanishes. Setting $C = G$ in the König decomposition $J_C = J_G + \overrightarrow{CG}^\flat\wedge P$, the angular momentum about $G$ is $J_G = S$, the spin, and it is independent of any other reference point because the $C$-dependence is entirely in the orbital term.

---

# Solution

The exercise is a short algebra of the wedge product. Part 1 derives the change-of-origin rule from Chasles and bilinearity; parts 2–3 read off when and along which directions the angular momentum is point-independent; part 4 identifies the point-independent core as the spin.

**Step 1: The change-of-origin rule.**

> [!note]- Derivation
> For each particle, Chasles' relation gives $\overrightarrow{C'M_a} = \overrightarrow{C'C} + \overrightarrow{CM_a}$, hence $\overrightarrow{C'M_a}^\flat = \overrightarrow{C'C}^\flat + \overrightarrow{CM_a}^\flat$. Then
> $$J_{C'}|_\Sigma = \sum_a\overrightarrow{C'M_a}^\flat\wedge p_a = \sum_a\big(\overrightarrow{C'C}^\flat + \overrightarrow{CM_a}^\flat\big)\wedge p_a.$$
> By bilinearity of the wedge, split the sum:
> $$J_{C'}|_\Sigma = \sum_a\overrightarrow{C'C}^\flat\wedge p_a + \sum_a\overrightarrow{CM_a}^\flat\wedge p_a = \overrightarrow{C'C}^\flat\wedge\Big(\sum_a p_a\Big) + J_C|_\Sigma.$$
> The first sum factors because $\overrightarrow{C'C}^\flat$ is independent of $a$. Recognising $\sum_a p_a = P$,
> $$\boxed{\,J_{C'}|_\Sigma = J_C|_\Sigma + \overrightarrow{C'C}^\flat\wedge P\,}.$$
> The change of origin shifts the angular momentum by the wedge of the displacement with the *total* four-momentum — the angular momentum, about $C'$, of a single point particle at $C$ carrying $P$.

**Step 2: Point-independence iff $P = 0$.**

> [!note]- Derivation
> The angular momentum is the same about every point iff the shift $\overrightarrow{C'C}^\flat\wedge P$ vanishes for *all* $C'$. Since $\overrightarrow{C'C}$ can be any vector (choose $C'$ freely), the wedge $\overrightarrow{C'C}^\flat\wedge P$ vanishes for all $\overrightarrow{C'C}$ iff $P = 0$: if $P\ne 0$, pick $\overrightarrow{C'C}$ not parallel to $P$ and the wedge is nonzero. So
> $$J_{C'} = J_C\ \text{for all } C, C'\quad\iff\quad P = 0.$$
> This is the centre-of-momentum condition: in the barycentric frame, where the total spatial momentum vanishes, the angular momentum two-form... but note $P = 0$ as a *four*-vector means the total energy also vanishes, which happens only for the trivial system. The physically relevant statement is the next one: even when $P\ne 0$, there is a *line* of points giving the same angular momentum.

**Step 3: The line of equal angular momentum.**

> [!note]- Derivation
> The shift $\overrightarrow{C'C}^\flat\wedge P$ vanishes when $\overrightarrow{C'C}$ is parallel to $P$, because the exterior product of a vector with (the dual of) a parallel vector is zero: if $\overrightarrow{C'C} = \lambda\,\vec u$ with $P = m\vec u$, then $\overrightarrow{C'C}^\flat\wedge P = \lambda m\,\vec u^\flat\wedge\vec u = 0$. So all points $C'$ lying on the line through $C$ in the direction of the four-momentum $P$ give the *same* angular momentum two-form:
> $$J_{C'} = J_C\quad\text{whenever}\quad\overrightarrow{C'C}\parallel P.$$
> Geometrically this is the worldline of the centre of inertia (and its parallels): moving the reference point *along the direction of motion of the system* does not change the angular momentum, because the orbital contribution of such a displacement is zero. This is why the centre of inertia, whose worldline is parallel to $P$, gives a well-defined intrinsic angular momentum.

**Step 4: The spin is the point-independent core.**

> [!note]- Derivation
> Take $C = G$, the [[Def - Centre of Inertia|centre of inertia]]. By the change-of-origin rule, for any other point $C$,
> $$J_C = J_G + \overrightarrow{CG}^\flat\wedge P.$$
> The second term, $\overrightarrow{CG}^\flat\wedge P$, is the *orbital* angular momentum — it carries all the $C$-dependence. The first term, $J_G$, is independent of $C$ (it is the angular momentum about the fixed point $G$). By the [[Thm - König Theorem (Relativistic)|König theorem]], $J_G = S$ is the [[Def - Spin Four-Vector|spin]] two-form: the part of the angular momentum that does not change when you move the reference point. So the change-of-origin rule does double duty — it tells you how the angular momentum depends on the reference point, *and* it isolates the spin as the part that does not. $\blacksquare$

> [!note]- Complete formal solution
> **Part 1.** Chasles: $\overrightarrow{C'M_a} = \overrightarrow{C'C} + \overrightarrow{CM_a}$. Bilinearity of $\wedge$: $J_{C'} = \sum_a(\overrightarrow{C'C}^\flat + \overrightarrow{CM_a}^\flat)\wedge p_a = \overrightarrow{C'C}^\flat\wedge P + J_C$. Hence $J_{C'} = J_C + \overrightarrow{C'C}^\flat\wedge P$.
>
> **Part 2.** The shift vanishes for all $C'$ iff $\overrightarrow{C'C}^\flat\wedge P = 0$ for all $\overrightarrow{C'C}$, iff $P = 0$.
>
> **Part 3.** For $\overrightarrow{C'C}\parallel P$ (i.e. $\overrightarrow{C'C} = \lambda\vec u$, $P = m\vec u$), the shift $\lambda m\,\vec u^\flat\wedge\vec u = 0$. So all points on the line through $C$ in the direction $P$ give the same angular momentum — the worldline of the centre of inertia and its parallels.
>
> **Part 4.** Setting $C = G$: $J_C = J_G + \overrightarrow{CG}^\flat\wedge P$. The orbital term $\overrightarrow{CG}^\flat\wedge P$ carries all the $C$-dependence; $J_G = S$ is the spin, the point-independent core. $\blacksquare$

---

# Key Takeaways

**The change of origin acts on the total momentum, which is why it touches only the orbital part.** The single fact to carry away is that moving the reference point shifts the angular momentum by $\overrightarrow{C'C}^\flat\wedge P$ — the wedge with the *total* four-momentum, not with any individual particle's momentum. This is what cleanly separates the angular momentum into a $C$-dependent orbital piece and a $C$-independent spin piece: the orbital piece is the angular momentum of the whole system treated as a point at $G$ carrying $P$, and it is the only thing that responds to a change of origin. The trigger to recognise this pattern is any question about angular momentum "about a point" — the reference-point dependence is always linear in the displacement and always through the total momentum, so you can move the origin to wherever the computation is easiest (usually the centre of inertia, where the orbital part vanishes).

**Parallel displacements are invisible to the wedge — the direction of motion is a free axis.** The wedge $\overrightarrow{C'C}^\flat\wedge P$ vanishes when the displacement is parallel to $P$, so sliding the reference point along the direction of the system's motion does not change the angular momentum. This is the algebraic reason the centre of inertia gives a well-defined intrinsic angular momentum: its worldline is parallel to $P$, and any point on that worldline gives the same answer. The transferable diagnostic is that whenever you wedge a displacement with a momentum, the component of the displacement *along* the momentum drops out — only the perpendicular (transverse) displacement contributes a moment. This is the four-dimensional version of "only the perpendicular lever arm matters" from elementary mechanics.

**Isolating an invariant by killing its variable part is a master technique.** The deepest lesson is the move in part 4: the angular momentum depends on $C$, so to find its intrinsic content you choose the $C$ that kills the variable part (the orbital term), leaving the invariant core (the spin). This is a recurring strategy across physics — when a quantity depends on an arbitrary choice (origin, gauge, frame), find the choice that simplifies it maximally, and what remains is the physical content. Here the choice is $C = G$, the centre of inertia, and the residue is the spin. The same pattern appears in choosing the rest frame to find rest mass, the Lorenz gauge to find the wave equation, and the principal axes to diagonalise the inertia tensor. Recognising "this depends on an arbitrary choice; pick the choice that isolates the invariant" is a reusable problem-solving reflex.
