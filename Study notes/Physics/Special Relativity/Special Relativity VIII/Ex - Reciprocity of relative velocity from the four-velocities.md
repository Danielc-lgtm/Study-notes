---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Reciprocity of Relative Velocity"
  - "Def - Velocity Relative to an Observer"
  - "Def - The Orthogonal Projector onto the Local Rest Space"
tags: [physics, special-relativity]
---

# Problem Statement

Two observers $\mathcal{O}, \mathcal{O}'$ have future-directed unit four-velocities $u, u'$ (so $u\cdot u = u'\cdot u' = 1$ in the mostly-minus signature) and worldlines crossing at an event $O$. The velocity of $\mathcal{O}'$ relative to $\mathcal{O}$ is $U \in E_u$, defined by $u' = \Gamma_0(u + U)$ with $\Gamma_0 = u\cdot u'$ and $u\cdot U = 0$; the velocity of $\mathcal{O}$ relative to $\mathcal{O}'$ is $U' \in E_{u'}$, defined by $u = \Gamma_0(u' + U')$ with $u'\cdot U' = 0$. Working with $c = 1$:

1. Show that $\lVert U\rVert_g^2 = 1 - 1/\Gamma_0^2$, and deduce $\lVert U'\rVert_g = \lVert U\rVert_g$ (equal relative speeds).
2. Show explicitly that $U' \ne -U$ in general by computing $u'\cdot U$ and observing it does not vanish; conclude that $U \notin E_{u'}$, so $-U$ cannot even be the reciprocal velocity (which must lie in $E_{u'}$).
3. Derive the explicit relation $U' = -\dfrac{1}{\Gamma_0}\perp_{u'}U$, where $\perp_{u'}X = X - (u'\cdot X)u'$.
4. Identify precisely where the Galilean intuition $U' = -U$ breaks, and recover it in the limit $\lVert U\rVert_g \to 0$.

**Recall:**

This drills the reciprocity theorem directly.

![[Thm - Reciprocity of Relative Velocity#Statement]]

The [[Def - Velocity Relative to an Observer|relative velocity]] $U$ of $\mathcal{O}'$ with respect to $\mathcal{O}$ is the spatial part of $\mathcal{O}'$'s four-velocity in $\mathcal{O}$'s [[Def - Observer and Local Rest Space|rest space]]: $u' = \Gamma_0(u + U)$ with $U \in E_u$. The [[Def - The Orthogonal Projector onto the Local Rest Space|orthogonal projector]] onto $E_{u'}$ is $\perp_{u'}X = X - (u'\cdot X)u'$ (mostly-minus form, since $u'\cdot u' = +1$). A spacelike vector has $\lVert X\rVert_g = \sqrt{-X\cdot X}$.

---

# Convergent Strategy

**Problem class.** An *establish-a-reciprocity / invariant* problem: show two observers agree on a scalar (their relative speed) even though the Galilean vector identity fails. The [[Special Relativity VIII — Kinematics II, Change of Observer#Problem-Solving Strategy|topic strategy]] says: track which vector lives in which rest space, and hunt for the invariant that survives the change.

**Assumption pattern.** Two four-velocities and their two decompositions, with the orthogonality conditions $u\cdot U = 0$ and $u'\cdot U' = 0$ as the structural constraints. The symmetry of the scalar product $u\cdot u' = u'\cdot u$ is the hidden assumption that makes $\Gamma_0$ — and hence the speed — the same both ways.

**Theorem routing.** Squaring the decomposition and using $u'\cdot u' = 1$ routes the relative speed through $\Gamma_0$ ([[Thm - Reciprocity of Relative Velocity]] Lemma 1). Projecting $u = \Gamma_0(u' + U')$ onto $E_{u'}$ with the [[Def - The Orthogonal Projector onto the Local Rest Space|projector]] routes to the explicit $U' = -\Gamma_0^{-1}\perp_{u'}U$. The magnitude equality follows by symmetry of the two decompositions.

**Key decision point.** The crux is recognising that the statement "$U' = -U$" is *type-incorrect*, not merely numerically wrong: $U \in E_u$ and $U' \in E_{u'}$ are vectors in different subspaces, so the equation cannot even be written without an identification of the two spaces. The decisive computation is $u'\cdot U = -\Gamma_0\lVert U\rVert^2 \ne 0$, which proves $U \notin E_{u'}$ and so $-U$ is not an admissible reciprocal velocity at all.

---

# Legal Operations Used

1. **Compute the Lorentz factor as a scalar product** (operation 3 from the topic page). $\Gamma_0 = u\cdot u'$, symmetric, so the relative speed extracted from it is the same for both observers.

2. **Project onto a rest space with $\perp_{u'}$** (operation 2 from the topic page). Projecting the decomposition $u = \Gamma_0(u' + U')$ onto $E_{u'}$ isolates $U'$ and produces the explicit reciprocal-velocity formula.

3. **Take a Galilean limit to check** (operation 9 from the topic page). As $\lVert U\rVert \to 0$, $\Gamma_0 \to 1$ and $\perp_{u'} \to \mathrm{Id}$, recovering $U' = -U$.

---

# Hints

> [!note]- Hint 1
> Take the Minkowski square of $u' = \Gamma_0(u + U)$. Use $u'\cdot u' = 1$, $u\cdot u = 1$, $u\cdot U = 0$, and $U\cdot U = -\lVert U\rVert^2$ (spacelike). You will get $1 = \Gamma_0^2(1 - \lVert U\rVert^2)$.

> [!note]- Hint 2
> To test whether $-U$ could be $U'$, check whether $U \in E_{u'}$, i.e. whether $u'\cdot U = 0$. Compute $u'\cdot U$ using $u' = \Gamma_0(u + U)$: it equals $\Gamma_0(u\cdot U + U\cdot U) = \Gamma_0(0 - \lVert U\rVert^2) \ne 0$. So $U$ is not even in $E_{u'}$.

> [!note]- Hint 3
> Apply $\perp_{u'}$ to $u = \Gamma_0(u' + U')$. Note $\perp_{u'}u' = 0$ (the projector kills $u'$) and $\perp_{u'}U' = U'$ (since $U' \in E_{u'}$). So $\perp_{u'}u = \Gamma_0 U'$. Now $\perp_{u'}u = u - (u'\cdot u)u' = u - \Gamma_0 u'$, so $U' = (u - \Gamma_0 u')/\Gamma_0$. Show this equals $-\Gamma_0^{-1}\perp_{u'}U$.

> [!note]- Hint 4
> The breakdown is in two places at once: the factor $\Gamma_0 \ne 1$ and the projection $\perp_{u'} \ne \mathrm{Id}$. Both go away as $\lVert U\rVert \to 0$: then $\Gamma_0 \to 1$ and the two rest spaces $E_u, E_{u'}$ merge, so $\perp_{u'}U \to U$ and $U' \to -U$.

---

# Solution

Reciprocity is the surviving magnitude-equality of a Galilean vector identity that fails. Step 1 extracts the relative speed from the symmetric Lorentz factor and gets equality of speeds; Step 2 shows the vector identity $U' = -U$ is type-incorrect because $U \notin E_{u'}$; Step 3 produces the correct explicit relation via projection; Step 4 locates the breakdown and recovers the Galilean limit. The non-obvious point is that the failure is not numerical but structural — the two velocities live in different spaces.

**Step 1: Equal relative speeds.**

> [!note]- Derivation
> Square $u' = \Gamma_0(u + U)$:
> $$u'\cdot u' = \Gamma_0^2(u\cdot u + 2u\cdot U + U\cdot U) = \Gamma_0^2(1 + 0 - \lVert U\rVert_g^2),$$
> using $u\cdot u = 1$, $u\cdot U = 0$ (as $U \in E_u$), $U\cdot U = -\lVert U\rVert_g^2$. Since $u'\cdot u' = 1$,
> $$1 = \Gamma_0^2(1 - \lVert U\rVert_g^2) \;\Longrightarrow\; \lVert U\rVert_g^2 = 1 - \frac{1}{\Gamma_0^2}.$$
> The second decomposition $u = \Gamma_0(u' + U')$ has identical form with $(u, U) \leftrightarrow (u', U')$ and the *same* $\Gamma_0 = u\cdot u' = u'\cdot u$ (symmetry of the metric). Squaring it gives $\lVert U'\rVert_g^2 = 1 - 1/\Gamma_0^2$, the same right-hand side. Hence
> $$\lVert U'\rVert_g = \lVert U\rVert_g.$$
> The relative speeds are equal — the surviving Galilean identity.

**Step 2: The vector identity is type-incorrect.**

> [!note]- Derivation
> For $-U$ to be the reciprocal velocity, $U'$ would have to equal $-U$; but $U'$ lives in $E_{u'}$ by definition, so $-U$ would have to lie in $E_{u'}$ too, i.e. $u'\cdot U = 0$. Compute:
> $$u'\cdot U = \Gamma_0(u + U)\cdot U = \Gamma_0(u\cdot U + U\cdot U) = \Gamma_0(0 - \lVert U\rVert_g^2) = -\Gamma_0\lVert U\rVert_g^2.$$
> This is nonzero whenever $\lVert U\rVert_g \ne 0$. Therefore $U \notin E_{u'}$: the vector $U$ does not even belong to $\mathcal{O}'$'s rest space, so $-U$ is *not an admissible relative velocity for $\mathcal{O}'$* — the equation $U' = -U$ is not merely false, it is comparing vectors in different subspaces $E_u$ and $E_{u'}$.

**Step 3: The explicit reciprocal velocity.**

> [!note]- Derivation
> Apply the projector $\perp_{u'}$ to $u = \Gamma_0(u' + U')$. Since $\perp_{u'}u' = u' - (u'\cdot u')u' = 0$ and $\perp_{u'}U' = U' - (u'\cdot U')u' = U'$ (because $u'\cdot U' = 0$), the right side projects to $\Gamma_0 U'$. The left side projects to
> $$\perp_{u'}u = u - (u'\cdot u)u' = u - \Gamma_0 u'.$$
> So $\Gamma_0 U' = u - \Gamma_0 u'$, i.e. $U' = u/\Gamma_0 - u'$. To recognise this as $-\Gamma_0^{-1}\perp_{u'}U$, compute $\perp_{u'}U = U - (u'\cdot U)u' = U + \Gamma_0\lVert U\rVert^2 u'$ (using Step 2). Then
> $$-\frac{1}{\Gamma_0}\perp_{u'}U = -\frac{1}{\Gamma_0}U - \lVert U\rVert^2 u'.$$
> Substitute $u' = \Gamma_0(u + U)$: $= -\Gamma_0^{-1}U - \lVert U\rVert^2\Gamma_0(u + U) = -\Gamma_0\lVert U\rVert^2 u - (\Gamma_0^{-1} + \Gamma_0\lVert U\rVert^2)U$. Now $\Gamma_0^{-1} + \Gamma_0\lVert U\rVert^2 = \Gamma_0^{-1}(1 + \Gamma_0^2\lVert U\rVert^2) = \Gamma_0^{-1}\cdot\Gamma_0^2 = \Gamma_0$ (using $\Gamma_0^2\lVert U\rVert^2 = \Gamma_0^2 - 1$ from Step 1). So $-\Gamma_0^{-1}\perp_{u'}U = -\Gamma_0\lVert U\rVert^2 u - \Gamma_0 U$. Independently, from $U' = u/\Gamma_0 - u'$ and $u' = \Gamma_0(u+U)$: $U' = u/\Gamma_0 - \Gamma_0 u - \Gamma_0 U = (\Gamma_0^{-1} - \Gamma_0)u - \Gamma_0 U = -\Gamma_0\lVert U\rVert^2 u - \Gamma_0 U$, matching. Hence
> $$U' = -\frac{1}{\Gamma_0}\perp_{u'}U.$$

**Step 4: Where Galilean intuition breaks, and its limit.**

> [!note]- Derivation
> The relation $U' = -\Gamma_0^{-1}\perp_{u'}U$ differs from the Galilean $U' = -U$ in two coupled ways: the scalar factor $1/\Gamma_0 \ne 1$, and the projection $\perp_{u'} \ne \mathrm{Id}$ (which tilts $U$ out of $E_u$ into $E_{u'}$). Both are consequences of the two rest spaces being *different* tilted slices of spacetime. As $\lVert U\rVert_g \to 0$: $\Gamma_0 = (1 - \lVert U\rVert^2)^{-1/2} \to 1$, and the tilt between $E_u$ and $E_{u'}$ vanishes, so $\perp_{u'}$ restricted to $E_u$ becomes the identity and $\perp_{u'}U \to U$. Hence $U' \to -U$: the Galilean identity is the small-speed limit, where all rest spaces collapse onto one Newtonian space of simultaneity. The minus sign is real (the reciprocal velocity does point "backward"); what fails at finite speed is the equality of the two *vectors*, an artefact of pretending the slices coincide.

> [!note]- Complete formal solution
> Squaring $u' = \Gamma_0(u + U)$ with $u'\cdot u' = u\cdot u = 1$, $u\cdot U = 0$ gives $1 = \Gamma_0^2(1 - \lVert U\rVert_g^2)$, so $\lVert U\rVert_g^2 = 1 - \Gamma_0^{-2}$; by the symmetry of $\Gamma_0 = u\cdot u'$, the same holds for $U'$, giving $\lVert U'\rVert_g = \lVert U\rVert_g$. The identity $U' = -U$ fails because $u'\cdot U = -\Gamma_0\lVert U\rVert_g^2 \ne 0$, so $U \notin E_{u'}$ and $-U$ is not an admissible reciprocal velocity. Projecting $u = \Gamma_0(u' + U')$ onto $E_{u'}$ gives $\Gamma_0 U' = u - \Gamma_0 u'$, equal to $-\Gamma_0^{-1}\perp_{u'}U$ after substitution. As $\lVert U\rVert_g \to 0$, $\Gamma_0 \to 1$ and the rest spaces merge, recovering $U' = -U$. $\blacksquare$

---

# Key Takeaways

**A relative velocity is a vector in someone's rest space, so "$U' = -U$" is type-incorrect, not just wrong.** The single most important lesson of reciprocity is that there is no frame-independent vector "the relative velocity of two observers" — there are two different vectors, $U \in E_u$ and $U' \in E_{u'}$, living in two different three-dimensional subspaces of spacetime. Writing $U' = -U$ silently identifies these two spaces, which is illegitimate at finite relative speed. The diagnostic to carry forward: before equating or subtracting two velocity vectors, check that they live in the *same* rest space; if they belong to different observers, they belong to different spaces, and the only safe comparison is of their magnitudes. This is the prototype for the whole chapter's discipline of rest-space bookkeeping, and the explicit failure $u'\cdot U \ne 0$ is the cleanest way to *prove* the spaces differ.

**The symmetry of the metric is the engine of every reciprocity.** Equal relative speeds, equal mutual time dilation, equal mutual length contraction — all of these trace back to the single algebraic fact that $u\cdot u' = u'\cdot u$, so the Lorentz factor $\Gamma_0$ is the same whichever observer is called "moving". Whenever a relativistic problem asks "do the two observers agree?", the first thing to check is whether the quantity in question is built symmetrically from the two four-velocities; if it is $\Gamma_0$ or a function of it, the answer is automatically yes. This converts apparent paradoxes (each sees the other's clock slow, each sees the other's ruler short) into immediate consequences of metric symmetry, and it is why mutual effects are consistent rather than contradictory.

**The projector $\perp_{u'}$ is the universal tool for carrying a vector between rest spaces, and reciprocity is its simplest use.** The explicit formula $U' = -\Gamma_0^{-1}\perp_{u'}U$ shows the general mechanism: to express a vector known in one observer's terms ($U$, an $E_u$-vector) in another observer's rest space ($E_{u'}$), project it with $\perp_{u'}$ and rescale by the Lorentz factor. This same projection reappears, with the same role, in the [[Thm - Law of Velocity Composition|velocity-composition law]] and the [[Thm - Aberration of Light|aberration law]] — reciprocity is the special case where the "particle" being transformed is one of the observers themselves. Recognising $\perp_{u'}$ as the change-of-rest-space operator unifies all the transformation laws of the chapter under one move: project, then rescale. The factor of $\Gamma_0$ is always the price of the tilt between the two slices.
