---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Lorentz Factor and Relative Velocity"
  - "Def - Four-Velocity and Four-Acceleration"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Problem Statement

Let $\mathcal{O}$ be an inertial observer with four-velocity $U_0$ and orthonormal frame $(e_\alpha)$, $e_0 = U_0$, and let $\mathcal{P}$ be a massive particle with four-velocity $U$, moving at speed $v$ along the $e_1$-axis. Working with $c = 1$ in the mostly-minus signature:

1. Write the components of $U$ in the observer's frame, and verify the unit-norm constraint $U \cdot U = 1$.
2. Compute the Lorentz factor two ways — as the scalar product $\Gamma = U \cdot U_0$ and as the time component $u^0$ — and check they agree.
3. Extract the relative velocity $V$ from the orthogonal decomposition $U = \Gamma(U_0 + V)$, and confirm $V \cdot U_0 = 0$ and $|\mathbf V| = v$.
4. Now let a *second* inertial observer $\mathcal{O}'$ have four-velocity $U_0' = U$ (so $\mathcal{O}'$ rides along with $\mathcal{P}$). Show that the Lorentz factor of $\mathcal{O}$ relative to $\mathcal{O}'$ equals that of $\mathcal{P}$ relative to $\mathcal{O}$ — the reciprocity of the Lorentz factor.

**Recall:**

The exercise rests on the four-velocity, the Lorentz factor, and the orthogonal decomposition.

![[Def - Lorentz Factor and Relative Velocity#The Definition]]

A [[Def - Four-Velocity and Four-Acceleration|four-velocity]] is a future-directed timelike unit vector, $U \cdot U = 1$, tangent to a particle's worldline and parametrised by [[Def - Proper Time|proper time]]. The Minkowski scalar product in the observer's orthonormal frame is $X \cdot Y = \eta_{\mu\nu}X^\mu Y^\nu = X^0 Y^0 - X^1 Y^1 - X^2 Y^2 - X^3 Y^3$, with $\eta = \mathrm{diag}(1,-1,-1,-1)$. The observer's four-velocity is $U_0 = e_0$, with components $(1,0,0,0)$.

---

# Convergent Strategy

**Problem class.** A *compute-a-kinematic-quantity-from-four-velocities* problem, the most basic of the chapter's [[Special Relativity VII — Kinematics I, Motion Relative to an Observer#Problem-Solving Strategy|problem-solving routine]]: express the desired quantity (here the Lorentz factor and relative velocity) as a scalar product or projection of $U$ and $U_0$, and evaluate it in the observer's own frame where the scalar product becomes a single component.

**Assumption pattern.** Two four-velocities are present — the observer's $U_0$ and the particle's $U$ — and the observer is inertial, so the simple form $\Gamma = U \cdot U_0$ and the clean decomposition $U = \Gamma(U_0 + V)$ both hold without correction terms. The motion is along a single axis, so only the $0$ and $1$ components are nontrivial, reducing the computation to $1+1$ dimensions. The phrase "second observer riding along" signals that part 4 is about the *symmetry* of the scalar product.

**Theorem routing.** Parts 1–3 are direct applications of the definition [[Def - Lorentz Factor and Relative Velocity]]: the unit-norm constraint $U \cdot U = 1$ fixes the components, the scalar product $\Gamma = U \cdot U_0$ gives the Lorentz factor, and the projection $V = (1/\Gamma)\perp_{U_0}U$ gives the relative velocity. Part 4 uses the symmetry of the Minkowski inner product, $U \cdot U_0 = U_0 \cdot U$, which is the route to reciprocity and underlies [[Thm - Time Dilation (General Observer)]].

**Key decision point.** The non-obvious move is recognising that the Lorentz factor is the *same number* computed two ways — as an abstract scalar product $U \cdot U_0$ and as a concrete component $u^0$ — and that this is not a coincidence but the content of "compute in the observer's frame": choosing $e_0 = U_0$ makes the scalar product collapse to the time component. The natural alternative, computing $\Gamma$ from the velocity formula $\Gamma = (1-v^2)^{-1/2}$, is fine but hides the geometric meaning that makes part 4 (reciprocity) immediate.

---

# Legal Operations Used

1. **Read the Lorentz factor as a scalar product of four-velocities** (operation 1 from the topic page). The Lorentz factor is computed as $\Gamma = U \cdot U_0$, evaluated in the observer's frame where it reduces to the time component $u^0$.

2. **Decompose the four-velocity orthogonally with respect to the observer** (operation 2). The four-velocity is split as $U = \Gamma(U_0 + V)$ to extract the relative velocity $V$ as its rest-space part.

3. **Use the unit-norm constraint** (operation 4). The constraint $U \cdot U = 1$ fixes the time component $u^0 = \sqrt{1 + (u^1)^2}$ and certifies the components are consistent.

4. **Compute in the observer's own frame** (operation 5). Choosing $e_0 = U_0$ turns every scalar product into a component operation, making $\Gamma = u^0$ and $V^i = u^i/\Gamma$.

---

# Hints

> [!note]- Hint 1
> A particle moving at speed $v$ along $e_1$ has four-velocity $U = \Gamma(U_0 + v e_1)$, because its relative velocity is $V = v e_1$ and the decomposition is $U = \Gamma(U_0 + V)$. Write out the components $u^\alpha = (\Gamma, \Gamma v, 0, 0)$.

> [!note]- Hint 2
> To compute $\Gamma = U \cdot U_0$ in the observer's frame, contract $u^\alpha = (\Gamma, \Gamma v, 0, 0)$ with $U_0 = (1,0,0,0)$ using $\eta = \mathrm{diag}(1,-1,-1,-1)$: only the time–time term survives, giving $\Gamma = u^0\cdot 1 = u^0$.

> [!note]- Hint 3
> For reciprocity (part 4), the scalar product is symmetric: $U_0 \cdot U_0' = U_0 \cdot U = U \cdot U_0$. So the Lorentz factor of $\mathcal{O}$ relative to $\mathcal{O}'$ (which is $U_0 \cdot U_0'$) equals the Lorentz factor of $\mathcal{P}$ relative to $\mathcal{O}$ (which is $U \cdot U_0$). No new computation is needed — just the symmetry of the dot product.

---

# Solution

The route is to write the particle's four-velocity in the observer's frame, then read every requested quantity off as a scalar product or component. Step 1 fixes the components from the decomposition and the unit-norm constraint; Step 2 computes the Lorentz factor two equivalent ways; Step 3 extracts and checks the relative velocity; Step 4 invokes the symmetry of the scalar product for reciprocity. The whole exercise is the single identity $\Gamma = U \cdot U_0 = u^0$ unpacked, with reciprocity as its immediate corollary.

**Step 1: The four-velocity components are $u^\alpha = (\Gamma, \Gamma v, 0, 0)$ with $\Gamma = (1-v^2)^{-1/2}$.**

> [!note]- Derivation
> The particle moves at speed $v$ along $e_1$, so its [[Def - Velocity Relative to an Observer|relative velocity]] is $V = v e_1$, a rest-space vector with $V \cdot U_0 = 0$ (since $e_1 \cdot e_0 = 0$). The orthogonal decomposition of the four-velocity is
> $$U = \Gamma(U_0 + V) = \Gamma(e_0 + v e_1),$$
> so the components are $u^\alpha = (\Gamma, \Gamma v, 0, 0)$. To find $\Gamma$, impose the unit-norm constraint:
> $$U \cdot U = \eta_{\mu\nu}u^\mu u^\nu = (\Gamma)^2 - (\Gamma v)^2 = \Gamma^2(1 - v^2) = 1,$$
> so $\Gamma^2 = (1-v^2)^{-1}$ and, taking the positive root (future-directed), $\Gamma = (1-v^2)^{-1/2}$. This confirms both the components and the unit-norm constraint simultaneously.

**Step 2: The Lorentz factor is $\Gamma = U \cdot U_0 = u^0$, the same number both ways.**

> [!note]- Derivation
> *As a scalar product.* With $U_0 = e_0$ having components $(1,0,0,0)$,
> $$\Gamma_{\text{(scalar product)}} = U \cdot U_0 = \eta_{\mu\nu}u^\mu (U_0)^\nu = \eta_{00}u^0(U_0)^0 = (1)(\Gamma)(1) = \Gamma,$$
> since only the time–time term $\eta_{00} = 1$ survives (all spatial components of $U_0$ vanish).
>
> *As the time component.* Directly, $u^0 = \Gamma$ by Step 1.
>
> The two agree: $U \cdot U_0 = u^0 = \Gamma = (1-v^2)^{-1/2}$. This is the content of "compute in the observer's frame" — choosing $e_0 = U_0$ makes the scalar product collapse to the time component. The agreement is not a coincidence but the defining identity of the Lorentz factor, and it is what makes the next step (reciprocity) trivial.

**Step 3: The relative velocity is $V = v e_1$, with $V \cdot U_0 = 0$ and $|\mathbf V| = v$.**

> [!note]- Derivation
> Project the four-velocity onto the rest space and divide by $\Gamma$:
> $$V = \frac{1}{\Gamma}\perp_{U_0}U = \frac{1}{\Gamma}\big(U - (U\cdot U_0)U_0\big) = \frac{1}{\Gamma}\big(\Gamma(e_0 + v e_1) - \Gamma e_0\big) = v e_1.$$
> Check orthogonality: $V \cdot U_0 = v\,(e_1 \cdot e_0) = 0$. Check the speed: $V$ is spacelike with $V \cdot V = v^2(e_1 \cdot e_1) = -v^2$, so $|\mathbf V| = \sqrt{-V\cdot V} = v$. The relative velocity is the spatial part of the four-velocity with the $\Gamma$ stripped off, and its magnitude is the speed $v$ — consistent with the decomposition $U = \Gamma(U_0 + V)$.

**Step 4: The Lorentz factor of $\mathcal{O}$ relative to $\mathcal{O}'$ equals that of $\mathcal{P}$ relative to $\mathcal{O}$ — reciprocity.**

> [!note]- Derivation
> Let $\mathcal{O}'$ have four-velocity $U_0' = U$. The Lorentz factor of $\mathcal{O}$ relative to $\mathcal{O}'$ is, by [[Def - Lorentz Factor and Relative Velocity|definition]], the scalar product of their four-velocities:
> $$\Gamma_{\mathcal{O}/\mathcal{O}'} = U_0 \cdot U_0' = U_0 \cdot U.$$
> The Lorentz factor of $\mathcal{P}$ relative to $\mathcal{O}$ is
> $$\Gamma_{\mathcal{P}/\mathcal{O}} = U \cdot U_0.$$
> By the symmetry of the Minkowski scalar product, $U_0 \cdot U = U \cdot U_0$, so
> $$\Gamma_{\mathcal{O}/\mathcal{O}'} = \Gamma_{\mathcal{P}/\mathcal{O}} = \Gamma = (1-v^2)^{-1/2}.$$
> Each observer measures the other's clock to run slow by the *same* factor $\Gamma$. This reciprocity is the symmetry of the inner product, nothing more, and it is the seed of the apparent twin paradox (each sees the other's clock slow — consistently, because they compare different pairs of events).

> [!note]- Complete formal solution
> A particle at speed $v$ along $e_1$ has [[Def - Velocity Relative to an Observer|relative velocity]] $V = v e_1$ and four-velocity $U = \Gamma(e_0 + v e_1)$, components $u^\alpha = (\Gamma, \Gamma v, 0, 0)$. The unit-norm constraint $U \cdot U = \Gamma^2(1-v^2) = 1$ gives $\Gamma = (1-v^2)^{-1/2}$. The Lorentz factor, computed as the scalar product $\Gamma = U \cdot U_0$ with $U_0 = e_0$, reduces to the time component $u^0 = \Gamma$, since only the $\eta_{00} = 1$ term survives — the two computations agree because choosing $e_0 = U_0$ collapses the scalar product to a component. The relative velocity, recovered as $V = (1/\Gamma)\perp_{U_0}U = v e_1$, satisfies $V \cdot U_0 = 0$ and $|\mathbf V| = \sqrt{-V\cdot V} = v$. Finally, for a second observer $\mathcal{O}'$ with $U_0' = U$, the symmetry of the scalar product gives $\Gamma_{\mathcal{O}/\mathcal{O}'} = U_0 \cdot U = U \cdot U_0 = \Gamma_{\mathcal{P}/\mathcal{O}}$ — the Lorentz factor is reciprocal, each observer seeing the other's clock dilated by the same $\Gamma$. $\blacksquare$

---

# Key Takeaways

**The Lorentz factor is the scalar product of the two four-velocities, and "computing in the observer's frame" is what makes the scalar product a single component.** This is the master identity of the whole chapter, and the exercise drills the mechanism behind it: when you choose the orthonormal frame with $e_0 = U_0$, the observer's four-velocity is $(1,0,0,0)$, and the scalar product $U \cdot U_0$ contracts to $\eta_{00}u^0 = u^0$, the time component of the particle's four-velocity. So the abstract, frame-independent $\Gamma = U \cdot U_0$ and the concrete, frame-dependent $u^0$ are the same number, and the choice of frame is what converts one into the other. The trigger to use this: whenever you have two four-velocities and need their relative Lorentz factor, dot them — and if you want a number, do the dot product in the frame of one of them, where it is just the time component of the other.

**The relative velocity is the four-velocity with its observer-time part removed and the $\Gamma$ stripped off.** The decomposition $U = \Gamma(U_0 + V)$ is the structural skeleton of the chapter, and this exercise shows how to invert it: project $U$ onto the rest space (subtract its $U_0$-component) to get $\Gamma V$, then divide by $\Gamma$ to get $V$. The division is essential — it converts the rate of change of position with respect to the *particle's* proper time into the rate with respect to the *observer's* clock, which is the physical speed bounded by $c$. The reusable diagnostic: if a quantity comes out unbounded as $v \to c$, you have probably forgotten to divide by $\Gamma$ and computed the proper velocity (celerity) instead of the relative velocity. The same projection-and-rescale recovers the propagation direction of a photon and the relative acceleration, so the pattern recurs throughout the chapter.

**Reciprocity of the Lorentz factor is nothing but the symmetry of the inner product, and it dissolves the twin paradox.** The fact that each of two observers measures the other's clock to run slow by the *same* factor looks paradoxical until you see it is forced by $U \cdot U_0 = U_0 \cdot U$ — the Minkowski scalar product is symmetric, so the Lorentz factor cannot tell which of the two worldlines is "the moving one". There is no contradiction, because the two observers are comparing *different pairs of events*: each one's "the other's clock between my two ticks" refers to a different segment of the other's worldline. Whenever a relativity problem seems to give a contradiction from a symmetry ("each sees the other slow, so who is really slow?"), the resolution is that the symmetric quantity is symmetric *by construction* and the apparent paradox comes from conflating two different comparisons; the symmetry of the scalar product is the cleanest way to see this. For the full resolution with worldlines and turnaround, see [[Ex - The twin paradox]].
