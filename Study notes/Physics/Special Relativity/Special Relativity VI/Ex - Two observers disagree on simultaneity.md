---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Nonexistence of Absolute Time"
  - "Def - Observer and Local Rest Space"
  - "Def - Einstein-Poincaré Simultaneity"
  - "Def - Rapidity"
tags: [physics, special-relativity]
---

# Problem Statement

In an inertial frame with coordinates $(t, x, y, z)$ and $c = 1$, observer $\mathcal{O}$ is at rest, with [[Def - Four-Velocity and Four-Acceleration|four-velocity]] $U_0 = (1, 0, 0, 0)$, and observer $\mathcal{O}'$ moves at velocity $v$ along $x$, with four-velocity $U_0' = \gamma(1, v, 0, 0)$, $\gamma = (1-v^2)^{-1/2}$. Their worldlines cross at the origin event $O$.

1. Compute the [[Def - Observer and Local Rest Space|local rest spaces]] $U_0^\perp$ and $U_0'^\perp$ at $O$, and show they are different — confirming [[Thm - Nonexistence of Absolute Time|the nonexistence of absolute time]].
2. Exhibit two events $P, Q$ that are **simultaneous for $\mathcal{O}$** but **not for $\mathcal{O}'$**, and compute the $\mathcal{O}'$-date difference between them.
3. Show that on a spacetime diagram, $\mathcal{O}'$'s line of simultaneity is tilted relative to $\mathcal{O}$'s by an angle related to the [[Def - Rapidity|rapidity]] $\varphi = \tanh^{-1}v$ (the lines $x'$-axis and $x$-axis make equal angles with the light ray).
4. Verify the general principle: the tilt vanishes iff $v = 0$, i.e. iff the observers are momentarily co-moving ($U_0' = U_0$).

**Recall:**

![[Thm - Nonexistence of Absolute Time#Statement]]

The [[Def - Observer and Local Rest Space|local rest space]] of an observer with four-velocity $U_0$ is $U_0^\perp = \{X : X\cdot U_0 = 0\}$; events simultaneous with $O$ for that observer are those in $O + U_0^\perp$ ([[Def - Einstein-Poincaré Simultaneity|Einstein–Poincaré simultaneity]]). The [[Def - Rapidity|rapidity]] is $\varphi = \tanh^{-1}v$, with $\gamma = \cosh\varphi$, $\gamma v = \sinh\varphi$. The metric is $\eta = \mathrm{diag}(+1,-1,-1,-1)$, so $X\cdot Y = X^0Y^0 - X^1Y^1 - X^2Y^2 - X^3Y^3$.

---

# Convergent Strategy

**Problem class.** A *make-the-abstract-concrete* problem: the theorem says rest spaces differ; here we compute the two rest spaces explicitly and produce named events that the two observers date differently. The [[Special Relativity VI — Observers, Local Rest Spaces and Local Frames#Problem-Solving Strategy|topic strategy]] is to translate simultaneity into orthogonality and work with the explicit four-velocities.

**Assumption pattern.** The given data are two explicit four-velocities differing by a boost. The relevant fact is that orthogonality to $U_0$ and to $U_0'$ are different conditions whenever $U_0\neq U_0'$; the relative velocity $v$ measures the difference, and the rapidity $\varphi$ measures the tilt. The signpost is "two observers in relative motion crossing at an event" — the precondition of the nonexistence theorem.

**Theorem routing.** Compute $U_0^\perp$ and $U_0'^\perp$ from $X\cdot U_0 = 0$ and $X\cdot U_0' = 0$; they differ, so by [[Thm - Nonexistence of Absolute Time|the theorem]] dates disagree. Pick $W\in U_0^\perp\setminus U_0'^\perp$ and form $P, Q = P + W$: they are $\mathcal{O}$-simultaneous but not $\mathcal{O}'$-simultaneous, with date difference $W\cdot U_0'$. The tilt angle follows from the slope of the $x'$-axis, $\tanh\varphi = v$.

**Key decision point.** The crux is choosing $W$ in the *spatial* direction of the boost ($W$ along $x$), because that is where the two rest spaces differ — the transverse directions $y, z$ are shared. A purely transverse $W$ would be simultaneous for *both* observers (no disagreement); the disagreement lives entirely in the boost plane.

---

# Legal Operations Used

1. **Translate simultaneity into orthogonality** (operation 2 from the topic page). Both rest spaces are computed as orthogonal complements; "simultaneous for $\mathcal{O}'$" becomes $W\cdot U_0' = 0$, which fails for the chosen $W$.

2. **Project onto the local rest space** (operation 1, implicitly). The disagreement is the nonzero $U_0'$-component of a vector lying in $U_0^\perp$ — i.e. $W$ has zero $U_0$-component but nonzero $U_0'$-component.

3. **Switch to rapidity** (operation 6 from the topic page). The tilt of the simultaneity line is governed by $\tanh\varphi = v$, the rapidity parametrisation.

---

# Hints

> [!note]- Hint 1
> The rest space $U_0^\perp$ for $U_0 = (1,0,0,0)$ is the set of $X$ with $X^0 = 0$ — purely spatial. For $U_0' = \gamma(1,v,0,0)$, solve $X\cdot U_0' = \gamma(X^0 - vX^1) = 0$, i.e. $X^0 = vX^1$. These hyperplanes differ.

> [!note]- Hint 2
> Take $W$ in the boost plane and in $\mathcal{O}$'s rest space: $W = (0, L, 0, 0)$ (a purely spatial separation along $x$). Then $W\cdot U_0 = 0$ ($\mathcal{O}$-simultaneous), but $W\cdot U_0' = \gamma(0 - vL) = -\gamma vL\neq 0$ ($\mathcal{O}'$ disagrees).

> [!note]- Hint 3
> The $x'$-axis (the $\mathcal{O}'$ simultaneity line through $O$) is the set $X^0 = vX^1$, i.e. the line $t = vx$ in the $(t,x)$ plane — slope $v$ from the $x$-axis. Since $v = \tanh\varphi$, the tilt angle $\theta$ satisfies $\tan\theta = v = \tanh\varphi$.

> [!note]- Hint 4
> When $v = 0$, $U_0' = (1,0,0,0) = U_0$, the condition $X^0 = vX^1$ becomes $X^0 = 0$, and the two rest spaces coincide. The tilt $\tan\theta = v$ vanishes. Disagreement requires relative motion.

---

# Solution

The computation is explicit and short. Step 1 writes the two rest spaces as orthogonality conditions and sees they differ. Step 2 picks a spatial separation along the boost and computes that $\mathcal{O}$ calls its endpoints simultaneous while $\mathcal{O}'$ does not, with an explicit date gap. Step 3 reads the tilt of the simultaneity line as $\tan\theta = v = \tanh\varphi$. Step 4 confirms agreement exactly at $v = 0$. The recurring move is "simultaneous = orthogonal to the four-velocity".

**Step 1: The two rest spaces differ.**

> [!note]- Derivation
> For $\mathcal{O}$ with $U_0 = (1,0,0,0)$, the [[Def - Observer and Local Rest Space|rest space]] is
> $$U_0^\perp = \{X : X\cdot U_0 = 0\} = \{X : X^0 = 0\},$$
> the purely spatial hyperplane (using $X\cdot U_0 = X^0$).
>
> For $\mathcal{O}'$ with $U_0' = \gamma(1, v, 0, 0)$,
> $$X\cdot U_0' = \gamma(X^0\cdot 1 - X^1\cdot v - 0 - 0) = \gamma(X^0 - vX^1),$$
> so
> $$U_0'^\perp = \{X : X^0 = vX^1\}.$$
> These hyperplanes are different whenever $v\neq 0$: $U_0^\perp$ is "$X^0 = 0$", $U_0'^\perp$ is "$X^0 = vX^1$", and a vector like $(0, 1, 0, 0)$ lies in the first but not the second (its $U_0'^\perp$ condition would need $0 = v$). By [[Thm - Nonexistence of Absolute Time|the nonexistence of absolute time]], the two observers therefore assign different dates — there is no shared "now".

**Step 2: Two events, simultaneous for $\mathcal{O}$ but not $\mathcal{O}'$.**

> [!note]- Derivation
> Choose a purely spatial separation along the boost direction: let $P$ be any event and $Q = P + W$ with
> $$W = (0, L, 0, 0), \qquad L > 0.$$
> Then $\overrightarrow{PQ} = W$, and
> $$W\cdot U_0 = 0 \quad\Rightarrow\quad P, Q \text{ are simultaneous for } \mathcal{O},$$
> since $W\in U_0^\perp$ (its time component is zero). But
> $$W\cdot U_0' = \gamma(0 - vL) = -\gamma vL \neq 0 \quad\Rightarrow\quad P, Q \text{ are NOT simultaneous for } \mathcal{O}'.$$
> The $\mathcal{O}'$-date difference between $P$ and $Q$ is the $U_0'$-component of their separation:
> $$\Delta t' = \frac{W\cdot U_0'}{U_0'\cdot U_0'} = \frac{-\gamma vL}{1} = -\gamma vL.$$
> So $\mathcal{O}$ sees $P$ and $Q$ happen at the same time, while $\mathcal{O}'$ sees them separated in time by $\gamma vL$ — the relativity of simultaneity, made numerical. (This is exactly Einstein's lightning-and-train: two strikes simultaneous on the platform are not simultaneous on the train.)

**Step 3: The tilt of the simultaneity line and the rapidity.**

> [!note]- Derivation
> Restrict to the $(t, x)$ plane. The $\mathcal{O}$ simultaneity line through $O$ is $X^0 = 0$, i.e. the $x$-axis. The $\mathcal{O}'$ simultaneity line (the $x'$-axis) is $X^0 = vX^1$, i.e. the line $t = vx$, of slope $v$ measured from the $x$-axis. Its tilt angle $\theta$ satisfies
> $$\tan\theta = v = \tanh\varphi, \qquad \varphi = \tanh^{-1}v \text{ the } [[Def - Rapidity|rapidity]].$$
> Symmetrically, the $\mathcal{O}'$ time axis (the $t'$-axis, the worldline $x = vt$) makes the same angle $\theta$ with the $t$-axis, on the other side — so the $t'$ and $x'$ axes "scissor" symmetrically toward the light ray $t = x$ (which is the fixed $45°$ line, $\tanh\varphi\to 1$). The two simultaneity lines coincide with the light ray only in the limit $v\to 1$ ($\varphi\to\infty$).

**Step 4: Agreement exactly at zero relative velocity.**

> [!note]- Derivation
> If $v = 0$, then $U_0' = \gamma(1, 0, 0, 0) = (1, 0, 0, 0) = U_0$ (with $\gamma = 1$), the condition $X^0 = vX^1$ becomes $X^0 = 0$, and $U_0'^\perp = U_0^\perp$: the rest spaces coincide and the observers agree on all dates. The tilt $\tan\theta = v = 0$. Thus disagreement on simultaneity is *exactly* the presence of relative motion: $U_0^\perp = U_0'^\perp\Leftrightarrow U_0 = U_0'\Leftrightarrow v = 0$, which is the corollary of [[Thm - Nonexistence of Absolute Time|the nonexistence theorem]].

> [!note]- Complete formal solution
> With $U_0 = (1,0,0,0)$ and $U_0' = \gamma(1,v,0,0)$: the rest spaces are $U_0^\perp = \{X^0 = 0\}$ and $U_0'^\perp = \{X^0 = vX^1\}$, which differ for $v\neq 0$, so dates disagree (nonexistence of absolute time). Taking $W = (0, L, 0, 0)$ and $Q = P + W$: $W\cdot U_0 = 0$ (so $P, Q$ are $\mathcal{O}$-simultaneous) but $W\cdot U_0' = -\gamma vL\neq 0$, giving an $\mathcal{O}'$-date gap $\Delta t' = -\gamma vL$. In the $(t,x)$ plane the $x'$-axis is $t = vx$, tilted by $\tan\theta = v = \tanh\varphi$ from the $x$-axis, scissoring symmetrically with the $t'$-axis toward the $45°$ light ray. At $v = 0$, $U_0' = U_0$, the rest spaces coincide, and the tilt vanishes — agreement holds exactly when the observers are co-moving. $\blacksquare$

---

# Key Takeaways

**The disagreement on simultaneity lives entirely in the boost plane; transverse directions are shared.** The two rest spaces $U_0^\perp = \{X^0 = 0\}$ and $U_0'^\perp = \{X^0 = vX^1\}$ differ only in how they treat the boost direction $x$: a separation along $y$ or $z$ has $X^0 = 0 = vX^1$ in both, so it is simultaneous for both observers. This is why we chose $W$ along $x$ — the disagreement is concentrated where the relative motion is. The transferable diagnostic: when two observers in relative motion disagree about simultaneity, the disagreement is a $\gamma v$ effect along the line of relative motion, and quantities transverse to the motion are unaffected. This same "only the boost direction is affected" structure recurs in length contraction (only longitudinal lengths contract) and in the transformation of fields (transverse components mix, longitudinal ones are inert).

**The date gap $W\cdot U_0'$ is the relativity of simultaneity made into a number.** The abstract statement "the rest spaces differ" becomes concrete the moment you compute the $U_0'$-component of a vector lying in $U_0^\perp$: that component, $W\cdot U_0' = -\gamma vL$, is precisely how much $\mathcal{O}'$ disagrees with $\mathcal{O}$ about the timing of two events $\mathcal{O}$ calls simultaneous. This is Einstein's train paradox in one line — two lightning strikes a distance $L$ apart, simultaneous on the platform, are timed $\gamma vL$ apart on the train. The reusable principle: to quantify a simultaneity disagreement, take the separation vector of the events one observer calls simultaneous and contract it with the *other* observer's four-velocity. The result is the date gap, and its sign tells you which event the second observer dates earlier.

**Rapidity is the natural measure of the tilt, and the symmetric scissoring is why no observer is privileged.** The simultaneity lines tilt by $\tan\theta = v = \tanh\varphi$, and the $t'$ and $x'$ axes scissor symmetrically about the $45°$ light ray. This symmetry is the geometric expression of the principle of relativity: neither observer's axes are "really" orthogonal and the other's "really" tilted — on the spacetime diagram each sees the other's axes scissored, by equal and opposite angles, and the construction is reciprocal. The rapidity $\varphi$ is the right variable because it is the additive boost parameter and because the tilt is literally a hyperbolic rotation by $\varphi$. The lesson for problem-solving: whenever a spacetime diagram shows tilted axes, the tilt is a rapidity, the scissoring is symmetric, and the apparent asymmetry between the two observers is an artifact of drawing one observer's axes square — the physics is reciprocal, which is exactly why "whose clock is really slow" and "whose now is really now" have no observer-independent answer.
