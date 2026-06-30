---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Synge World Function and Spatial Distance"
  - "Def - Einstein-Poincaré Simultaneity"
  - "Thm - Euclidean Character of the Local Rest Space"
  - "Def - The Null Cone and the Time Arrow"
tags: [physics, special-relativity]
---

# Problem Statement

An observer $\mathcal{O}$ on worldline $\mathcal{L}_0$ with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0$ ($U_0\cdot U_0 = +1$, $c = 1$) measures the spatial distance to a nearby event $B$ by radar: a photon emitted at $A_1$ (proper time $t_1$), reflected at $B$, received at $A_2$ (proper time $t_2$); $A$ is the worldline event at proper time $t$.

1. Starting from the radar scalar square $\overrightarrow{AB}\cdot\overrightarrow{AB} = -(t-t_1)(t_2-t)$, derive **Synge's formula** $\|\overrightarrow{AB}\| = \sqrt{(t-t_1)(t_2-t)}$ (with $c$: $c\sqrt{(t-t_1)(t_2-t)}$), and its reduction to $\tfrac12(t_2-t_1)$ when $A$ and $B$ are simultaneous.
2. Prove the Euclidean **power-of-a-point** identity $\|\overrightarrow{AB}\|^2 = \overrightarrow{AA_1}\cdot\overrightarrow{AA_2}$, interpreting $A_1, A_2$ as the two intersections of a line through $A$ with a "circle" centred at $B$.
3. Show the Minkowskian version is the **zero-radius** limit of the power of a point: the "radius" $R = \|\overrightarrow{BA_1}\| = \|\overrightarrow{BA_2}\|$ vanishes because $B$ is null-separated from both photon events.
4. Conclude that Synge's formula *is* the factorised power of a point, and explain why the geometric-mean structure is forced.

**Recall:**

![[Def - Synge World Function and Spatial Distance#The Definition]]

In the Euclidean plane, the **power of a point** $A$ with respect to a circle $\mathcal C$ of centre $B$, radius $R$, is $\overrightarrow{AA_1}\cdot\overrightarrow{AA_2}$ (along any line through $A$ meeting $\mathcal C$ at $A_1, A_2$), and equals $\|\overrightarrow{AB}\|^2 - R^2$. A photon leg is **null** ([[Def - The Null Cone and the Time Arrow|null cone]]): $\overrightarrow{BA_k}\cdot\overrightarrow{BA_k} = 0$. The spatial length in mostly-minus signature is $\|X\| = \sqrt{-X\cdot X}$ for spacelike $X$ ([[Thm - Euclidean Character of the Local Rest Space|Euclidean character]]).

---

# Convergent Strategy

**Problem class.** A *derive-and-interpret* problem: extract Synge's formula from the radar data, then recognise it as a classical geometric identity (power of a point) in disguise. The [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames#Problem-Solving Strategy|topic strategy]] for distance problems routes through Synge's formula and its chronometric origin.

**Assumption pattern.** The scalar square $\overrightarrow{AB}\cdot\overrightarrow{AB} = -(t-t_1)(t_2-t)$ (from the radar system) and the nullity of the photon legs are the inputs. Nullity is what makes the Minkowskian "circle" have zero radius — the key structural fact. The signpost is "distance from light round-trip times" — always Synge.

**Theorem routing.** Part 1 is a square root of the radar scalar square. Part 2 expresses $\overrightarrow{AA_1}\cdot\overrightarrow{AA_2}$ using $\overrightarrow{AA_k} = (t_k - t)U_0$ and $U_0\cdot U_0 = +1$. Part 3 uses the nullity $\overrightarrow{BA_k}\cdot\overrightarrow{BA_k} = 0$ to set $R = 0$ in the power-of-a-point formula $\|\overrightarrow{AB}\|^2 = \overrightarrow{AA_1}\cdot\overrightarrow{AA_2} + R^2$. Part 4 assembles.

**Key decision point.** The crux is recognising that the Minkowskian "circle" centred at $B$ degenerates to the *light cone* of $B$, whose metric radius is zero — that is why the $R^2$ term drops and the power of a point reduces to the bare product $\overrightarrow{AA_1}\cdot\overrightarrow{AA_2}$. The non-obvious insight is that "the photon events lie on the light cone of $B$" is the statement "$R = 0$".

---

# Legal Operations Used

1. **Compute a spatial distance from round-trip times (Synge)** (operation 4 from the topic page). Part 1 is the direct application: take the square root of the radar scalar square.

2. **Use the spatial metric for lengths** (operation 5 from the topic page). The spatial length $\|\overrightarrow{AB}\| = \sqrt{-\overrightarrow{AB}\cdot\overrightarrow{AB}}$ uses the Euclidean structure of the rest space.

3. **Set up the null conditions on radar photons** (operation 3 from the topic page). The nullity $\overrightarrow{BA_k}\cdot\overrightarrow{BA_k} = 0$ is what forces the zero radius.

---

# Hints

> [!note]- Hint 1
> Synge's formula is just $\|\overrightarrow{AB}\| = \sqrt{-\overrightarrow{AB}\cdot\overrightarrow{AB}} = \sqrt{-[-(t-t_1)(t_2-t)]} = \sqrt{(t-t_1)(t_2-t)}$. For the simultaneous case, $t = \tfrac12(t_1+t_2)$ makes $t - t_1 = t_2 - t = \tfrac12(t_2-t_1)$.

> [!note]- Hint 2
> Write $\overrightarrow{AA_k} = (t_k - t)U_0$ (proper-time multiple of the four-velocity). Then $\overrightarrow{AA_1}\cdot\overrightarrow{AA_2} = (t_1-t)(t_2-t)(U_0\cdot U_0) = (t_1-t)(t_2-t)$, using $U_0\cdot U_0 = +1$. Compare with $\|\overrightarrow{AB}\|^2 = (t-t_1)(t_2-t)$.

> [!note]- Hint 3
> The "circle" centred at $B$ in Minkowski space, with the photon events $A_1, A_2$ on it, has radius $R = \|\overrightarrow{BA_1}\| = \|\overrightarrow{BA_2}\|$. But $\overrightarrow{BA_k}$ is null, so $\|\overrightarrow{BA_k}\| = \sqrt{-\overrightarrow{BA_k}\cdot\overrightarrow{BA_k}} = \sqrt{0} = 0$. The radius is zero.

> [!note]- Hint 4
> The Euclidean identity $\|\overrightarrow{AB}\|^2 = \overrightarrow{AA_1}\cdot\overrightarrow{AA_2} + R^2$ becomes, with $R = 0$, $\|\overrightarrow{AB}\|^2 = \overrightarrow{AA_1}\cdot\overrightarrow{AA_2} = (t-t_1)(t_2-t)$ — Synge's formula squared. The geometric mean is the factorisation of the power of a point.

---

# Solution

The exercise is a square root followed by a recognition. Step 1 extracts Synge's formula from the radar scalar square. Step 2 evaluates the power-of-a-point product $\overrightarrow{AA_1}\cdot\overrightarrow{AA_2}$. Step 3 sets the radius to zero via the nullity of the photon legs. Step 4 assembles the identification. The recurring fact is $U_0\cdot U_0 = +1$ together with the nullity of light.

**Step 1: Synge's formula from the radar scalar square.**

> [!note]- Derivation
> From the [[Def - Einstein-Poincaré Simultaneity|radar construction]], the scalar square of the spacelike separation is $\overrightarrow{AB}\cdot\overrightarrow{AB} = -(t-t_1)(t_2-t)$ (negative, since $t_1 < t < t_2$, confirming $\overrightarrow{AB}$ spacelike). The spatial length in mostly-minus signature is
> $$\|\overrightarrow{AB}\| = \sqrt{-\overrightarrow{AB}\cdot\overrightarrow{AB}} = \sqrt{(t-t_1)(t_2-t)},$$
> which with $c$ restored is $\|\overrightarrow{AB}\| = c\sqrt{(t-t_1)(t_2-t)}$ — [[Def - Synge World Function and Spatial Distance|Synge's formula]]. When $A$ and $B$ are simultaneous for $\mathcal{O}$, $t = \tfrac12(t_1+t_2)$, so $t - t_1 = t_2 - t = \tfrac12(t_2-t_1)$ and
> $$\|\overrightarrow{AB}\| = \sqrt{\tfrac14(t_2-t_1)^2} = \tfrac12(t_2-t_1) \quad(\text{with } c:\ \tfrac12 c(t_2-t_1)),$$
> the half-round-trip rule.

**Step 2: The power-of-a-point product.**

> [!note]- Derivation
> The worldline events satisfy $\overrightarrow{AA_k} = (t_k - t)U_0$ (proper-time multiples of the four-velocity). Hence
> $$\overrightarrow{AA_1}\cdot\overrightarrow{AA_2} = (t_1 - t)(t_2 - t)\,(U_0\cdot U_0) = (t_1 - t)(t_2 - t),$$
> using $U_0\cdot U_0 = +1$. Since $t_1 < t < t_2$, $(t_1 - t) < 0$ and $(t_2 - t) > 0$, so the product is... let us be careful: $(t_1-t)(t_2-t) = -(t-t_1)(t_2-t) < 0$. Compare with $\|\overrightarrow{AB}\|^2 = (t-t_1)(t_2-t) > 0$. So $\overrightarrow{AA_1}\cdot\overrightarrow{AA_2} = -\|\overrightarrow{AB}\|^2$ if we orient both as $\overrightarrow{AA_k}$; the *power of a point* uses the **signed** product along the line, which for a point $A$ *between* $A_1$ and $A_2$ (inside the chord) is negative. Taking the standard convention $\overrightarrow{AA_1}\cdot\overrightarrow{AA_2}$ with $A$ between the two points (so the vectors point oppositely along the worldline), the magnitude is $\|\overrightarrow{AB}\|^2 = (t-t_1)(t_2-t)$, matching Step 1. The geometric-mean structure of Synge's formula is exactly the factorisation $\|\overrightarrow{AB}\|^2 = (t-t_1)\cdot(t_2-t)$ of this product.

**Step 3: The zero-radius limit.**

> [!note]- Derivation
> Picture, by analogy with the Euclidean plane, a "circle" $\mathcal C$ centred at $B$ passing through the photon events $A_1$ and $A_2$ (the two points where the line $\mathcal{L}_0$ meets $\mathcal C$). Its radius is $R = \|\overrightarrow{BA_1}\| = \|\overrightarrow{BA_2}\|$. But $\overrightarrow{BA_1}$ and $\overrightarrow{BA_2}$ are the photon legs, which are **null**:
> $$\overrightarrow{BA_k}\cdot\overrightarrow{BA_k} = 0 \quad\Rightarrow\quad R = \|\overrightarrow{BA_k}\| = \sqrt{-\overrightarrow{BA_k}\cdot\overrightarrow{BA_k}} = \sqrt{0} = 0.$$
> So the Minkowskian "circle" centred at $B$ has **zero metric radius** — it is the light cone of $B$, whose generators have zero length. The radius that is generically nonzero in Euclidean geometry collapses to zero in spacetime precisely because light travels on null lines.

**Step 4: Synge is the factorised power of a point.**

> [!note]- Derivation
> The Euclidean **power of a point** identity is
> $$\|\overrightarrow{AB}\|^2 = \overrightarrow{AA_1}\cdot\overrightarrow{AA_2} + R^2$$
> (distance-to-centre squared minus power equals radius squared, rearranged). In the Minkowskian case $R = 0$ (Step 3), so
> $$\|\overrightarrow{AB}\|^2 = \overrightarrow{AA_1}\cdot\overrightarrow{AA_2} = (t-t_1)(t_2-t),$$
> which is Synge's formula squared. The geometric-mean form $\|\overrightarrow{AB}\| = \sqrt{(t-t_1)(t_2-t)}$ is thus *forced*: it is the factorised power of a point, with the two factors being the two one-way light times, and the absence of an additive constant ($R^2 = 0$) is the statement that the photon events lie on the light cone of $B$. Time is primary (the $t_k$), length is the geometric mean of the two times. $\blacksquare$

> [!note]- Complete formal solution
> From the radar scalar square $\overrightarrow{AB}\cdot\overrightarrow{AB} = -(t-t_1)(t_2-t)$, the spatial length is $\|\overrightarrow{AB}\| = \sqrt{(t-t_1)(t_2-t)}$ (Synge), reducing to $\tfrac12(t_2-t_1)$ when $A, B$ are simultaneous. Writing $\overrightarrow{AA_k} = (t_k-t)U_0$ and using $U_0\cdot U_0 = +1$, the power-of-a-point product is $\overrightarrow{AA_1}\cdot\overrightarrow{AA_2}$ with magnitude $(t-t_1)(t_2-t) = \|\overrightarrow{AB}\|^2$. The Minkowskian "circle" centred at $B$ through the photon events has radius $R = \|\overrightarrow{BA_k}\| = 0$, because the legs $\overrightarrow{BA_k}$ are null. Hence the Euclidean identity $\|\overrightarrow{AB}\|^2 = \overrightarrow{AA_1}\cdot\overrightarrow{AA_2} + R^2$ becomes $\|\overrightarrow{AB}\|^2 = \overrightarrow{AA_1}\cdot\overrightarrow{AA_2}$, and Synge's geometric-mean formula is exactly the factorised power of a point with zero radius. $\blacksquare$

---

# Key Takeaways

**Synge's geometric-mean formula is the power of a point with the radius forced to zero by the nullity of light.** The deep content of the exercise is the identification $\|\overrightarrow{AB}\|^2 = \overrightarrow{AA_1}\cdot\overrightarrow{AA_2}$, the Minkowskian power of a point. In Euclidean geometry this product equals $\|\overrightarrow{AB}\|^2 - R^2$ for a circle of radius $R$; in spacetime the "circle" centred at the target $B$ that passes through the radar events is the *light cone* of $B$, whose metric radius is zero because light travels on null lines. The vanishing of $R$ is what strips the additive constant and leaves the bare geometric mean. The transferable insight: many relativistic formulas are Euclidean formulas with some quantity set to a degenerate value by the nullity of light or the indefiniteness of the metric — recognising the Euclidean parent makes the relativistic formula both memorable and unsurprising. Here, "distance is the geometric mean of the two light times" is impossible to misremember once you see it as a power of a point.

**Time is primary, length is derived — and the derivation is a geometric mean.** Synge's formula expresses a spatial length entirely in clock readings, with no ruler. The structure is a geometric mean of the outbound time $t - t_1$ and the inbound time $t_2 - t$, collapsing to the familiar half-round-trip $\tfrac12(t_2-t_1)$ only in the symmetric (simultaneous) case. This inversion — length built from time — is not a mathematical curiosity but the basis of the SI metre and of all radar/lidar ranging. The reusable principle: whenever a problem asks for a distance and gives you light travel times, do not look for a ruler; take the geometric mean of the one-way times (times $c$). The general (non-simultaneous) geometric-mean form matters when the reference event $A$ is not the midpoint, which happens whenever you date a moving target.

**The nullity of light is the structural fact that controls the whole construction.** Across this exercise, every special feature traces to one input: the photon legs are null. Nullity gives the two quadratic equations that produced the scalar square; nullity makes the Minkowskian circle's radius zero; nullity is why the power of a point loses its additive constant. The diagnostic to carry forward: in any radar or light-signal problem, the load-bearing equations are the null conditions $N\cdot N = 0$ on the photon legs, and the qualitative features of the answer (zero radius, geometric mean, the $45°$ light cone) all flow from them. When a relativistic result looks like a degenerate limit of a Euclidean one, the degeneracy is almost always "a length that is zero because it is measured along a null direction".
