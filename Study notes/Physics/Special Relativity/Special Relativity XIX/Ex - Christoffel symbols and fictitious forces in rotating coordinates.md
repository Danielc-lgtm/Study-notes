---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Christoffel Symbols"
  - "Def - The Covariant Derivative"
tags: [physics, special-relativity]
---

# Problem Statement

Work in flat spacetime with rotating coordinates. To keep the algebra transparent, use *Cartesian-type* rotating coordinates $(ct,x,y,z)$ co-rotating about the $z$-axis with angular velocity $\omega$, related to inertial Cartesian coordinates $(ct',x',y',z')$ by
$$ct' = ct, \quad x' = x\cos\omega t - y\sin\omega t, \quad y' = x\sin\omega t + y\cos\omega t, \quad z' = z.$$

1. Compute the metric $g_{\alpha\beta}$ in these rotating coordinates. (You should find a position-dependent $g_{tt}$ and cross terms $g_{tx}, g_{ty}$.)
2. Compute the Christoffel symbols and exhibit the ones responsible for the **centrifugal** and **Coriolis** accelerations.
3. Write the spatial geodesic equation $\ddot{x}^i + \Gamma^i{}_{\alpha\beta}\dot{x}^\alpha\dot{x}^\beta = 0$ for a slowly-moving free particle and recover the Newtonian centrifugal and Coriolis terms.
4. Confirm that the spacetime is flat (zero curvature) and conclude that these "forces" are fictitious — pure Christoffel symbols with zero Riemann tensor.

**Recall:**

![[Special Relativity XIX/Def - Christoffel Symbols#The Definition]]

The geodesic equation $\ddot{x}^\gamma + \Gamma^\gamma{}_{\alpha\beta}\dot{x}^\alpha\dot{x}^\beta = 0$ (dots are derivatives with respect to proper time) is the equation of a free particle; see [[Def - The Covariant Derivative]] for its origin as $\boldsymbol{\nabla}_{\vec u}\vec u = 0$. In mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$.

---

# Convergent Strategy

**Problem class.** A *compute-the-connection-and-interpret-it-physically* problem, the ⭐⭐⭐ synthesis of [[Special Relativity XIX/Def - Christoffel Symbols|Def - Christoffel Symbols]] with the geodesic equation. It demonstrates the chapter's central thesis — Christoffel symbols are fictitious forces — on the cleanest possible example.

**Assumption pattern.** The coordinate change is a time-dependent rotation, so the Jacobian carries time-derivatives of the rotation matrix, producing cross terms and a position-dependent $g_{tt} = 1 - \omega^2(x^2+y^2)$. The signpost that centrifugal and Coriolis terms will appear is the explicit $\omega$ in the rotation.

**Theorem routing.** Part 1: metric transformation law. Part 2: Christoffel formula of [[Special Relativity XIX/Def - Christoffel Symbols|Def - Christoffel Symbols]]. Part 3: geodesic equation in the slow-motion limit. Part 4: vanishing of the Riemann tensor by flatness.

**Key decision point.** The crux is the slow-motion limit in Part 3: setting $\dot t \approx 1$ (proper time $\approx$ coordinate time) and keeping the velocity-linear (Coriolis) and velocity-independent (centrifugal) Christoffel contributions, while dropping higher-order terms. Identifying which Christoffel symbol is centrifugal ($\Gamma^x{}_{tt}$, velocity-independent) versus Coriolis ($\Gamma^x{}_{ty}$, velocity-linear) is the physical payoff.

---

# Legal Operations Used

1. **Read off the metric from a coordinate change** (operation 1 from the topic page) for Part 1.
2. **Compute Christoffel symbols from the metric** (operation 2 from the topic page) for Part 2.
3. **Use the geodesic / connection structure** to interpret the symbols as accelerations in Part 3.

---

# Hints

> [!note]- Hint 1
> Differentiate the rotation. With $c=1$: $\partial x'/\partial t = -\omega(x\sin\omega t + y\cos\omega t) = -\omega y'$, but expressed in rotating coordinates $\partial x'/\partial t = -\omega(x\sin\omega t+y\cos\omega t)$. It is cleaner to compute $g_{\alpha\beta}$ by transforming the inertial line element $\mathrm{d}s^2 = \mathrm{d}t^2 - \mathrm{d}x'^2-\mathrm{d}y'^2-\mathrm{d}z'^2$ and substituting $\mathrm{d}x' = \cos\omega t\,\mathrm{d}x - \sin\omega t\,\mathrm{d}y - \omega(x\sin\omega t+y\cos\omega t)\mathrm{d}t$, etc.

> [!note]- Hint 2
> The line element works out to $\mathrm{d}s^2 = [1-\omega^2(x^2+y^2)]\mathrm{d}t^2 + 2\omega y\,\mathrm{d}t\,\mathrm{d}x - 2\omega x\,\mathrm{d}t\,\mathrm{d}y - \mathrm{d}x^2 - \mathrm{d}y^2 - \mathrm{d}z^2$ (with $c=1$). So $g_{tt} = 1-\omega^2(x^2+y^2)$, $g_{tx} = \omega y$, $g_{ty} = -\omega x$, and $g_{xx}=g_{yy}=g_{zz}=-1$.

> [!note]- Hint 3
> The relevant Christoffels (to lowest order in $\omega$) are $\Gamma^x{}_{tt} = -\omega^2 x$, $\Gamma^y{}_{tt} = -\omega^2 y$ (centrifugal: velocity-independent) and $\Gamma^x{}_{ty} = \Gamma^x{}_{yt} = -\omega$, $\Gamma^y{}_{tx} = \Gamma^y{}_{xt} = +\omega$ (Coriolis: couple to velocity). Compute, e.g., $\Gamma^x{}_{tt} = \tfrac12 g^{xx}(2\partial_t g_{xt} - \partial_x g_{tt})$.

> [!note]- Hint 4
> In the slow-motion limit $\dot t\approx 1$, the geodesic equation $\ddot x + \Gamma^x{}_{tt}\dot t^2 + 2\Gamma^x{}_{ty}\dot t\dot y \approx 0$ becomes $\ddot x = \omega^2 x + 2\omega\dot y$ — the centrifugal acceleration $\omega^2 x$ plus the Coriolis acceleration $2\omega\dot y$, exactly the Newtonian rotating-frame forces.

---

# Solution

The plan: Step 1 transforms the line element to get the rotating metric with its cross terms. Step 2 computes the centrifugal and Coriolis Christoffel symbols. Step 3 feeds them into the slow-motion geodesic equation and recovers Newton's rotating-frame accelerations. Step 4 confirms flatness, so the forces are fictitious.

**Step 1: The rotating metric.**

> [!note]- Derivation
> Start from the inertial line element $\mathrm{d}s^2 = \mathrm{d}t^2 - \mathrm{d}x'^2 - \mathrm{d}y'^2 - \mathrm{d}z'^2$ ($c=1$). Differentiate the rotation:
> $$\mathrm{d}x' = \cos\omega t\,\mathrm{d}x - \sin\omega t\,\mathrm{d}y - \omega(x\sin\omega t + y\cos\omega t)\,\mathrm{d}t,$$
> $$\mathrm{d}y' = \sin\omega t\,\mathrm{d}x + \cos\omega t\,\mathrm{d}y + \omega(x\cos\omega t - y\sin\omega t)\,\mathrm{d}t, \qquad \mathrm{d}z' = \mathrm{d}z.$$
> Compute $\mathrm{d}x'^2 + \mathrm{d}y'^2$. The rotation is orthogonal, so the pure $\mathrm{d}x,\mathrm{d}y$ part gives $\mathrm{d}x^2+\mathrm{d}y^2$; the pure $\mathrm{d}t$ part gives $\omega^2(x^2+y^2)\mathrm{d}t^2$; and the cross terms give $-2\omega y\,\mathrm{d}t\,\mathrm{d}x + 2\omega x\,\mathrm{d}t\,\mathrm{d}y$ (after using the angle-addition identities). Therefore
> $$\mathrm{d}s^2 = \big[1 - \omega^2(x^2+y^2)\big]\mathrm{d}t^2 + 2\omega y\,\mathrm{d}t\,\mathrm{d}x - 2\omega x\,\mathrm{d}t\,\mathrm{d}y - \mathrm{d}x^2 - \mathrm{d}y^2 - \mathrm{d}z^2,$$
> giving $g_{tt} = 1-\omega^2(x^2+y^2)$, $g_{tx}=g_{xt}=\omega y$, $g_{ty}=g_{yt}=-\omega x$, $g_{xx}=g_{yy}=g_{zz}=-1$, all other components zero. (This is the Cartesian form of the Langevin metric.)

**Step 2: The centrifugal and Coriolis Christoffel symbols.**

> [!note]- Derivation
> To lowest order in $\omega$ the relevant inverse-metric entries are $g^{xx}=g^{yy}=-1$ (corrections are $O(\omega^2)$). Compute the spatial Christoffels with a time index, dropping $O(\omega^3)$:
>
> *Centrifugal (two time indices, velocity-independent).*
> $$\Gamma^x{}_{tt} = \tfrac12 g^{xx}\big(2\partial_t g_{xt} - \partial_x g_{tt}\big) = \tfrac12(-1)\big(2\partial_t(\omega y) - \partial_x[1-\omega^2(x^2+y^2)]\big) = \tfrac12(-1)\big(0 + 2\omega^2 x\big) = -\omega^2 x.$$
> Similarly $\Gamma^y{}_{tt} = -\omega^2 y$.
>
> *Coriolis (one time, one space index, velocity-linear).*
> $$\Gamma^x{}_{ty} = \tfrac12 g^{xx}\big(\partial_t g_{xy} + \partial_y g_{xt} - \partial_x g_{ty}\big) = \tfrac12(-1)\big(0 + \partial_y(\omega y) - \partial_x(-\omega x)\big) = \tfrac12(-1)(\omega+\omega) = -\omega.$$
> Similarly $\Gamma^y{}_{tx} = +\omega$ (the antisymmetry in the spatial label reflects that the Coriolis force is perpendicular to the velocity). So the connection contains exactly the centrifugal symbols $\Gamma^{x,y}{}_{tt} = -\omega^2(x,y)$ and the Coriolis symbols $\Gamma^x{}_{ty}=-\omega$, $\Gamma^y{}_{tx}=+\omega$.

**Step 3: The geodesic equation gives Newton's rotating-frame forces.**

> [!note]- Derivation
> The free particle moves on a geodesic $\ddot{x}^\gamma + \Gamma^\gamma{}_{\alpha\beta}\dot{x}^\alpha\dot{x}^\beta = 0$, dots being proper-time derivatives. In the slow-motion (non-relativistic) limit, proper time $\approx$ coordinate time, so $\dot t\approx 1$ and the spatial velocities $\dot x,\dot y$ are small. Keep the terms with at least one $\dot t$:
> $$\ddot x + \Gamma^x{}_{tt}\dot t^2 + 2\Gamma^x{}_{ty}\dot t\dot y \approx 0 \quad\Longrightarrow\quad \ddot x + (-\omega^2 x)(1) + 2(-\omega)(1)\dot y \approx 0,$$
> $$\boxed{\;\ddot x = \omega^2 x + 2\omega\dot y\;}$$
> and symmetrically $\ddot y = \omega^2 y - 2\omega\dot x$. The first term $\omega^2 x$ (pointing outward) is the **centrifugal acceleration** $\boldsymbol{\omega}\times(\boldsymbol{\omega}\times\mathbf{r})$; the term $2\omega\dot y$ (perpendicular to the velocity) is the **Coriolis acceleration** $-2\boldsymbol{\omega}\times\dot{\mathbf{r}}$. These are exactly the fictitious forces a Newtonian physicist introduces in a rotating frame — here derived as Christoffel symbols of flat spacetime.

**Step 4: Flatness — the forces are fictitious.**

> [!note]- Derivation
> The rotating metric was obtained from the inertial metric by an explicit (time-dependent) coordinate change, so running it backwards reduces $g_{\alpha\beta}$ to $\eta$. The **Riemann curvature tensor** $R^\rho{}_{\sigma\mu\nu}$ is a tensor that vanishes in inertial coordinates (where $g=\eta$ and $\Gamma=0$), hence vanishes in *all* coordinates: $R^\rho{}_{\sigma\mu\nu} = 0$ identically. So although the Christoffel symbols $\Gamma^{x,y}{}_{tt}$ and $\Gamma^{x,y}{}_{ty}$ are nonzero, the curvature built from their derivatives is zero. This is the precise statement that the centrifugal and Coriolis forces are **fictitious**: they are artefacts of the rotating coordinates, removable everywhere at once by transforming to an inertial frame. The contrast with gravity is exact and is the whole pedagogical point — a *gravitational* field is also encoded in Christoffel symbols, and also looks like a fictitious force locally (equivalence principle), but its Riemann tensor is *not* zero, so it cannot be transformed away globally. The rotating frame is the flat-space rehearsal; gravity is the same play with the curvature turned on.

> [!note]- Complete formal solution
> Transforming the inertial line element through the time-dependent rotation gives $\mathrm{d}s^2 = [1-\omega^2(x^2+y^2)]\mathrm{d}t^2 + 2\omega y\,\mathrm{d}t\mathrm{d}x - 2\omega x\,\mathrm{d}t\mathrm{d}y - \mathrm{d}x^2-\mathrm{d}y^2-\mathrm{d}z^2$. The Christoffel formula yields the centrifugal symbols $\Gamma^x{}_{tt}=-\omega^2 x$, $\Gamma^y{}_{tt}=-\omega^2 y$ and the Coriolis symbols $\Gamma^x{}_{ty}=-\omega$, $\Gamma^y{}_{tx}=+\omega$. The slow-motion geodesic equation ($\dot t\approx 1$) gives $\ddot x = \omega^2 x + 2\omega\dot y$ and $\ddot y = \omega^2 y - 2\omega\dot x$ — the Newtonian centrifugal $\omega^2\mathbf{r}$ and Coriolis $-2\boldsymbol{\omega}\times\dot{\mathbf{r}}$ accelerations. Since the metric reduces to $\eta$ under the inverse coordinate change, the Riemann tensor vanishes identically, so these forces are fictitious — nonzero Christoffel symbols with zero curvature. $\blacksquare$

---

# Key Takeaways

**Centrifugal and Coriolis forces are Christoffel symbols, and the geodesic equation is Newton's rotating-frame equation of motion.** This exercise makes concrete the chapter's deepest claim: the "fictitious forces" of a rotating frame are not separate physics but components of the connection. The centrifugal force is the velocity-independent symbol $\Gamma^i{}_{tt}$ (two time indices), and the Coriolis force is the velocity-linear symbol $\Gamma^i{}_{tj}$ (one time, one space index); the geodesic equation, which says a free particle has zero covariant acceleration, reproduces $\ddot x = \omega^2 x + 2\omega\dot y$ exactly. The trigger for this identification is any non-inertial frame and a free particle; the diagnostic is that a velocity-independent fictitious force lives in $\Gamma^i{}_{tt}$ while a velocity-dependent one lives in $\Gamma^i{}_{tj}$. This reframes all of rotating-frame mechanics as flat-spacetime geometry in curvilinear coordinates.

**The slow-motion limit is what connects the relativistic geodesic equation to Newtonian intuition.** The geodesic equation is exact and fully relativistic, but to recognise the familiar centrifugal and Coriolis forces one takes the limit where proper time approximates coordinate time ($\dot t\approx 1$) and velocities are small, keeping the Christoffel terms with at least one factor of $\dot t$. This is the same limiting procedure by which general relativity recovers Newtonian gravity: there, $\Gamma^i{}_{tt}\approx \partial_i\Phi$ becomes the Newtonian gravitational acceleration $-\nabla\Phi$, just as here $\Gamma^i{}_{tt} = -\omega^2 x^i$ becomes the centrifugal acceleration. Mastering the slow-motion reduction of the geodesic equation in this flat, transparent setting is exactly the skill needed to extract the Newtonian limit of a curved spacetime, and the parallel between centrifugal force and gravity is the seed of the equivalence principle.

**Nonzero Christoffel symbols with zero curvature is the precise signature of a fictitious force — and the precise contrast with gravity.** The single most transferable insight is the distinction the exercise draws: the rotating frame has nonzero Christoffel symbols (so there are apparent forces) but zero Riemann tensor (so the forces are fictitious, removable everywhere by one change of coordinates). A genuine gravitational field also has nonzero Christoffels and also produces locally-removable apparent forces (free fall cancels gravity, as the equivalence principle demands), but its Riemann tensor is *nonzero*, which is why it cannot be transformed away globally and why tidal forces — the genuinely observable, coordinate-independent part of gravity — survive. The whole conceptual bridge from special to general relativity is this one distinction, and the rotating frame is the cleanest place to internalise it, because here you can verify by explicit coordinate change that the curvature really is zero. When you later meet the Schwarzschild metric, the question "is this curvature real or a coordinate artefact?" is answered by exactly the Riemann-tensor computation rehearsed here.
