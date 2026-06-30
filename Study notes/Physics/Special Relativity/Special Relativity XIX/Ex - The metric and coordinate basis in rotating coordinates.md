---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Arbitrary Coordinates and the Coordinate Basis"
tags: [physics, special-relativity]
---

# Problem Statement

A uniformly rotating observer relabels flat spacetime by spherical coordinates $(ct,r,\theta,\varphi)$ that co-rotate with angular velocity $\omega$ about the polar axis. These are related to the inertial spherical coordinates $(ct',r',\theta',\varphi')$ of a non-rotating observer by
$$t' = t, \qquad r' = r, \qquad \theta' = \theta, \qquad \varphi' = \varphi + \omega t.$$
The inertial spherical metric is $g'_{\alpha\beta} = \mathrm{diag}(1,-1,-r^2,-r^2\sin^2\theta)$.

1. Compute the Jacobian matrix $\partial x'^\beta/\partial x^\alpha$ of the coordinate change.
2. Using the tensor transformation law $g_{\alpha\beta} = (\partial x'^\mu/\partial x^\alpha)(\partial x'^\nu/\partial x^\beta)\,g'_{\mu\nu}$, find the components $g_{\alpha\beta}$ of the metric in the rotating coordinates.
3. Identify the off-diagonal term and the position-dependence of $g_{(ct)(ct)}$, and interpret them.
4. Explain why this position-dependent, non-diagonal metric does **not** indicate that the spacetime is curved, and name the test that confirms flatness.

**Recall:**

![[Def - Arbitrary Coordinates and the Coordinate Basis#The Definition]]

In mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, a timelike vector has positive norm. The "Langevin metric" obtained here is the metric of flat Minkowski spacetime expressed in rotating coordinates, not a new metric.

---

# Convergent Strategy

**Problem class.** A *compute-the-metric-from-a-coordinate-change* problem — the most basic operation of the chapter, applying the change-of-basis law for a type $(0,2)$ tensor. The [[Special Relativity XIX — Fields on Spacetime and the Covariant Derivative#Problem-Solving Strategy|topic strategy]] says: get the Jacobian, then $g = J^{\mathsf T}\eta J$, then everything else is mechanical.

**Assumption pattern.** The coordinate change is explicit and affine in $t$, so the Jacobian is constant in the relevant entry — only $\partial\varphi'/\partial(ct) = \omega/c$ couples time to angle. The presence of $\omega$ in the angular coordinate is the signpost that a cross term will appear.

**Theorem routing.** Part 1 is direct differentiation. Part 2 routes through the metric transformation law of [[Def - Arbitrary Coordinates and the Coordinate Basis]]. Part 3 reads off the structure. Part 4 invokes the fact (stated on the definition page) that a position-dependent $g_{\alpha\beta}$ from curvilinear coordinates has zero Riemann tensor.

**Key decision point.** The crux is keeping track of the single off-diagonal Jacobian entry $\partial\varphi'/\partial(ct) = \omega/c$ (with $c=1$, just $\omega$): it is what feeds $g'_{\varphi\varphi} = -r^2\sin^2\theta$ into both the new $g_{(ct)(ct)}$ and the cross term $g_{(ct)\varphi}$. Missing it loses the entire rotating structure.

---

# Legal Operations Used

1. **Read off the metric from a coordinate change** (operation 1 from the topic page). The whole exercise is this operation: form $J = \partial x'/\partial x$ and compute $g = J^{\mathsf T}\eta' J$ with $\eta'$ the inertial spherical metric.

---

# Hints

> [!note]- Hint 1
> With $c = 1$, the only non-trivial coordinate relations are $\varphi' = \varphi + \omega t$ and the identities $t'=t$, $r'=r$, $\theta'=\theta$. So the Jacobian is the identity except for the single entry $\partial\varphi'/\partial t = \omega$ (or $\partial\varphi'/\partial(ct) = \omega/c$ if you carry $c$).

> [!note]- Hint 2
> The transformation law is a double matrix product. Because only $\varphi'$ depends on more than its own coordinate, the only new contributions come from terms in which a $\varphi'$ index appears: $g_{(ct)(ct)}$, $g_{(ct)\varphi}$, and $g_{\varphi\varphi}$ get $g'_{\varphi\varphi}$ contributions weighted by $\partial\varphi'/\partial(ct) = \omega$.

> [!note]- Hint 3
> $g_{(ct)(ct)} = g'_{(ct)(ct)}(\partial(ct')/\partial(ct))^2 + g'_{\varphi\varphi}(\partial\varphi'/\partial(ct))^2 = 1 + (-r^2\sin^2\theta)\omega^2 = 1 - \omega^2 r^2\sin^2\theta$. The cross term $g_{(ct)\varphi} = g'_{\varphi\varphi}\,(\partial\varphi'/\partial(ct))(\partial\varphi'/\partial\varphi) = -\omega r^2\sin^2\theta$.

> [!note]- Hint 4
> A metric is *flat* if some coordinate change reduces it to $\eta$. Here that coordinate change is explicit — go back to inertial spherical $(ct',\dots)$, then to inertial Cartesian. So the Riemann tensor, computed from this metric, must vanish; the position-dependence is an artefact of the rotating coordinates, not of the geometry.

---

# Solution

The route is three short steps. Step 1 differentiates the coordinate relations to get the Jacobian, whose only interesting entry is $\partial\varphi'/\partial(ct) = \omega/c$. Step 2 sandwiches the inertial metric between two copies of the Jacobian and reads off the new components, the rotating structure coming entirely from the $g'_{\varphi\varphi}$ contributions routed through that one entry. Step 3 interprets the cross term and the modified $g_{tt}$ and confirms flatness.

**Step 1: The Jacobian is the identity plus one off-diagonal entry.**

> [!note]- Derivation
> Order the coordinates as $(x^0,x^1,x^2,x^3) = (ct,r,\theta,\varphi)$ and the primed ones as $(x'^0,x'^1,x'^2,x'^3) = (ct',r',\theta',\varphi')$. Differentiating $ct'=ct$, $r'=r$, $\theta'=\theta$, $\varphi'=\varphi+\omega t$:
> $$\frac{\partial x'^\beta}{\partial x^\alpha} = \begin{pmatrix} 1 & 0 & 0 & 0 \\ 0 & 1 & 0 & 0 \\ 0 & 0 & 1 & 0 \\ \omega/c & 0 & 0 & 1 \end{pmatrix},$$
> where rows are indexed by $\beta$ (the primed, target coordinate) and columns by $\alpha$ (the unprimed, source coordinate). The sole off-diagonal entry is $\partial\varphi'/\partial(ct) = \partial(\varphi+\omega t)/\partial(ct) = \omega/c$. Setting $c=1$, this entry is $\omega$.

**Step 2: The rotating metric.**

> [!note]- Derivation
> Apply $g_{\alpha\beta} = \dfrac{\partial x'^\mu}{\partial x^\alpha}\dfrac{\partial x'^\nu}{\partial x^\beta}\,g'_{\mu\nu}$ with $g'_{\mu\nu} = \mathrm{diag}(1,-1,-r^2,-r^2\sin^2\theta)$ and $c=1$.
>
> *Time–time.* Only $\mu=\nu=0$ and $\mu=\nu=3$ survive (the Jacobian's $0$-column has entries in rows $0$ and $3$):
> $$g_{00} = (1)^2 g'_{00} + (\omega)^2 g'_{33} = 1 + \omega^2(-r^2\sin^2\theta) = 1 - \omega^2 r^2\sin^2\theta.$$
>
> *Time–angle.* The $0$-column has entries in rows $0,3$; the $3$-column (for $\varphi$) has its entry in row $3$ only ($\partial\varphi'/\partial\varphi = 1$):
> $$g_{03} = g_{30} = (\omega)(1)\,g'_{33} = \omega\cdot(-r^2\sin^2\theta) = -\omega r^2\sin^2\theta.$$
>
> *Angle–angle.* $g_{33} = (1)^2 g'_{33} = -r^2\sin^2\theta$. The purely spatial $g_{11} = g'_{11} = -1$, $g_{22} = g'_{22} = -r^2$ are unchanged. Assembling,
> $$g_{\alpha\beta} = \begin{pmatrix} 1 - \omega^2 r^2\sin^2\theta & 0 & 0 & -\omega r^2\sin^2\theta \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -r^2 & 0 \\ -\omega r^2\sin^2\theta & 0 & 0 & -r^2\sin^2\theta \end{pmatrix}.$$
> (Restoring $c$: replace $\omega$ by $\omega/c$ and $\omega^2$ by $\omega^2/c^2$ in the entries.)

**Step 3: Interpretation and flatness.**

> [!note]- Derivation
> The off-diagonal term $g_{(ct)\varphi} = -\omega r^2\sin^2\theta$ couples time and azimuthal angle: a clock fixed in the rotating frame is "dragged" around, and this cross term is what produces the Sagnac effect and the impossibility of globally synchronising clocks on a rotating disk. The modified $g_{(ct)(ct)} = 1 - \omega^2 r^2\sin^2\theta$ encodes time dilation that grows with distance $r\sin\theta$ from the axis — and it goes to zero at the *light cylinder* $r\sin\theta = 1/\omega$ (with $c$: $r\sin\theta = c/\omega$), where the co-rotating worldline reaches the speed of light and ceases to be timelike.
>
> Despite all this structure, the spacetime is flat. The metric was obtained from the inertial metric by an explicit coordinate change, $(ct,r,\theta,\varphi)\to(ct',r',\theta',\varphi')\to$ inertial Cartesian; running the change backwards reduces $g_{\alpha\beta}$ to $\eta_{\mu\nu}$. The invariant test is the **Riemann curvature tensor** $R^\rho{}_{\sigma\mu\nu}$: computed from this metric and its Christoffel symbols it vanishes identically, because curvature is a tensor and is zero in the inertial coordinates where $g = \eta$, hence zero in all coordinates. The position-dependence and the cross term are properties of the rotating *coordinates*, not of the *geometry* — exactly the centrifugal/Coriolis "fictitious force" situation. This is the lesson the flat case teaches: a complicated metric need not mean curvature.

> [!note]- Complete formal solution
> With $c=1$ and coordinates $(ct,r,\theta,\varphi)$, the relations $ct'=ct$, $r'=r$, $\theta'=\theta$, $\varphi'=\varphi+\omega t$ give the Jacobian $\partial x'^\beta/\partial x^\alpha = \delta^\beta_\alpha + \omega\,\delta^\beta_3\delta^0_\alpha$ (identity plus the single entry $\partial\varphi'/\partial(ct)=\omega$). Substituting into $g_{\alpha\beta} = (\partial x'^\mu/\partial x^\alpha)(\partial x'^\nu/\partial x^\beta)g'_{\mu\nu}$ with $g'_{\mu\nu} = \mathrm{diag}(1,-1,-r^2,-r^2\sin^2\theta)$ yields
> $$g_{\alpha\beta} = \begin{pmatrix} 1 - \omega^2 r^2\sin^2\theta & 0 & 0 & -\omega r^2\sin^2\theta \\ 0 & -1 & 0 & 0 \\ 0 & 0 & -r^2 & 0 \\ -\omega r^2\sin^2\theta & 0 & 0 & -r^2\sin^2\theta \end{pmatrix}.$$
> The cross term $g_{(ct)\varphi} = -\omega r^2\sin^2\theta$ is frame-dragging by the rotation; $g_{(ct)(ct)} = 1-\omega^2 r^2\sin^2\theta$ vanishes at the light cylinder $r\sin\theta = 1/\omega$. The spacetime is flat: the metric reduces to $\eta$ under the inverse coordinate change, so the Riemann tensor — a tensor, zero in inertial coordinates — vanishes identically. $\blacksquare$

---

# Key Takeaways

**The change-of-basis law $g = J^{\mathsf T}\eta J$ is the workhorse, and the cross terms come from the off-diagonal Jacobian entries.** Whenever you meet a non-inertial coordinate system, the first move is always the same: write the explicit relation to inertial coordinates, differentiate to get the Jacobian, and sandwich the inertial metric between two copies of it. The structure of the resulting metric is dictated entirely by which Jacobian entries are off-diagonal — here the single entry $\partial\varphi'/\partial(ct) = \omega$ is responsible for the entire rotating character, feeding the angular metric component $g'_{\varphi\varphi}$ into both the new $g_{tt}$ and the time–angle cross term. The trigger for recognising this technique is any problem that names an observer's coordinates (rotating, accelerated, spherical) and asks for the geometry; the diagnostic is to locate the coordinates that depend on more than their own inertial counterpart, because those are the ones that generate cross terms and position-dependence.

**A position-dependent or non-diagonal metric is not evidence of curvature — only the Riemann tensor decides.** This is the single most important conceptual point of the whole chapter, and the rotating metric is the cleanest illustration. The metric here has a position-dependent $g_{tt}$, an off-diagonal $g_{t\varphi}$, and a coordinate singularity at the light cylinder, and yet the spacetime is exactly flat Minkowski space. The reason is that "flat" means "reducible to $\eta$ by *some* coordinate change", and that change is available by construction. The invariant, coordinate-free test for curvature is the vanishing of the Riemann tensor, which is zero in any inertial frame and therefore zero everywhere. The transferable lesson, which becomes indispensable in general relativity, is to never read physical curvature off the appearance of the metric components: a complicated-looking metric may be flat space in bad coordinates, and only a tensorial invariant (the Riemann tensor, or its contractions) settles the question.

**The off-diagonal $g_{t\varphi}$ is the frame-dragging seed, and the light cylinder is where the coordinates break.** The cross term $g_{(ct)\varphi} = -\omega r^2\sin^2\theta$ is physically rich even though the geometry is trivial: it is the reason a rotating frame cannot globally synchronise its clocks (the synchronisation gap accumulates around a loop), the origin of the Sagnac time difference between co- and counter-rotating light beams, and the flat-space precursor of the genuine frame-dragging produced by a rotating mass in general relativity (where the analogous $g_{t\varphi}$ is *not* removable). The vanishing of $g_{(ct)(ct)}$ at $r\sin\theta = 1/\omega$ marks the light cylinder, beyond which no observer can co-rotate rigidly because they would have to exceed the speed of light — a coordinate breakdown, not a physical singularity. Recognising which features of a metric are removable artefacts (these) and which are invariant physics (curvature) is the skill that this exercise, and the flat-spacetime setting generally, is designed to build.
