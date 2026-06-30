---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Integration of Forms and the Volume Element"
  - "Def - The Levi-Civita Tensor"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and signature $\eta = \mathrm{diag}(+1,-1,-1,-1)$.

1. In an inertial frame with Cartesian coordinates $(t,x,y,z)$, compute the four-volume of the region $\mathscr{V} = \{0\le t\le T,\ x^2+y^2+z^2\le R^2\}$ (a spatial ball persisting for a time $T$).
2. Recompute the same four-volume in inertial spherical coordinates $(t,r,\theta,\varphi)$, being careful to include the metric volume factor $\sqrt{|g|}$, and confirm you get the same answer.
3. Let $A$ be the 4-form $A = \rho\,\epsilon$, where $\rho(t,r) = \rho_0\,e^{-r/a}$ is a (given) scalar field and $\epsilon$ is the Levi-Civita tensor. Compute $\int_{\mathscr{V}} A$ over the same region, and interpret it as the spacetime integral of the density $\rho$.
4. State, in one sentence each, why the computation in part 2 needed the factor $r^2\sin\theta$ but the *form* integral in part 3 would have been coordinate-independent even if you had forgotten where the metric enters.

**Recall:**

The four-volume element and the integral of a 4-form are defined as follows.

![[Def - Integration of Forms and the Volume Element#The Definition]]

In inertial Cartesian coordinates $g_{\mu\nu} = \eta_{\mu\nu}$, so $g = \det(g_{\mu\nu}) = -1$ and $\sqrt{|g|} = 1$. In inertial spherical coordinates $(t,r,\theta,\varphi)$ the line element is $\mathrm{d}s^2 = \mathrm{d}t^2 - \mathrm{d}r^2 - r^2\mathrm{d}\theta^2 - r^2\sin^2\theta\,\mathrm{d}\varphi^2$, so $g_{\mu\nu} = \mathrm{diag}(1,-1,-r^2,-r^2\sin^2\theta)$ and $g = -r^4\sin^2\theta$.

---

# Convergent Strategy

**Problem class.** A *compute-an-integral-over-a-region* problem, the most basic class of [[Special Relativity XX — Integration in Spacetime and Stokes' Theorem#Problem-Solving Strategy|the chapter]]. The routine is: find coordinates adapted to the region (here the region is a coordinate box in spherical coordinates), write the correct volume element, and evaluate an ordinary Lebesgue integral.

**Assumption pattern.** A region described by inequalities and a density given as a function of position. The signpost that spherical coordinates are natural is that the region is a *ball* — round in space — so its boundary $r = R$ is a coordinate surface there, whereas in Cartesian coordinates it is the awkward constraint $x^2+y^2+z^2\le R^2$. The given $\rho(r)$ depending only on $r$ confirms spherical coordinates will separate the integral cleanly.

**Theorem routing.** Parts 1–2 use the four-volume $\mathrm{vol}\,\mathscr{V} = \int\sqrt{|g|}\,\mathrm{d}^4x$; the coordinate-independence asserted there ([[Def - Integration of Forms and the Volume Element]]) is what guarantees parts 1 and 2 agree. Part 3 uses the integral of a 4-form $\int_{\mathscr{V}} A = \int A_{0123}\,\mathrm{d}^4x$, with $A_{0123} = \rho\,\epsilon_{0123} = \rho\sqrt{|g|}$. The route is: identify the volume factor, set up the iterated integral, evaluate.

**Key decision point.** The non-obvious choice is *which* coordinates and *whether to include $\sqrt{|g|}$*. Choosing spherical coordinates makes the region a box but introduces the factor $r^2\sin\theta$; forgetting that factor (the natural error, since $\sqrt{|g|}=1$ in the Cartesian frame one is used to) gives a coordinate-dependent, wrong answer. The decision is to *always* write the metric volume factor explicitly when leaving Cartesian coordinates.

---

# Legal Operations Used

1. **Operation 1 from the topic page (write the four-volume element as $\sqrt{|g|}\,\mathrm{d}^4x$).** In spherical coordinates this supplies the factor $r^2\sin\theta$; in Cartesian coordinates it is $1$. This is the operation that makes the integral geometric, and the whole exercise is an application of it.

2. **Operation 2 from the topic page (integrate a 4-form by reading off its single component).** For part 3, the 4-form $A = \rho\,\epsilon$ has the single component $A_{0123} = \rho\sqrt{|g|}$, and the integral is the Lebesgue integral of that one number — no metric reasoning beyond extracting the component.

---

# Hints

> [!note]- Hint 1
> The region is a coordinate box in spherical coordinates: $t\in[0,T]$, $r\in[0,R]$, $\theta\in[0,\pi]$, $\varphi\in[0,2\pi)$. Write the four-volume element there and the integral factorises.

> [!note]- Hint 2
> In spherical coordinates $\sqrt{|g|} = \sqrt{r^4\sin^2\theta} = r^2\sin\theta$ (taking the positive root, with $\sin\theta\ge 0$ on $[0,\pi]$). The four-volume element is $r^2\sin\theta\,\mathrm{d}t\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$.

> [!note]- Hint 3
> For part 3, the single component of $A = \rho\,\epsilon$ in spherical coordinates is $A_{0123} = \rho\,\epsilon_{0123} = \rho\sqrt{|g|} = \rho_0 e^{-r/a}\,r^2\sin\theta$. Integrate this over the box; the $\theta,\varphi$ integrals give $4\pi$ and the $r$ integral is $\int_0^R e^{-r/a} r^2\,\mathrm{d}r$.

---

# Solution

The route is short. Part 1 is the elementary product "time interval times ball volume". Part 2 redoes it in spherical coordinates, where the entire subtlety is the factor $r^2\sin\theta = \sqrt{|g|}$. Part 3 integrates a density by extracting the single component $A_{0123} = \rho\sqrt{|g|}$. The non-obvious move is to write $\sqrt{|g|}$ explicitly on leaving Cartesian coordinates.

**Step 1: The four-volume in Cartesian coordinates is $\frac{4}{3}\pi R^3 T$.**

> [!note]- Derivation
> In inertial Cartesian coordinates $\sqrt{|g|} = 1$, so $\mathrm{vol}\,\mathscr{V} = \int_{\mathscr{V}}\mathrm{d}t\,\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z$. The integrand is $1$ and the region factorises into $t\in[0,T]$ and the spatial ball $B_R = \{x^2+y^2+z^2\le R^2\}$:
> $$\mathrm{vol}\,\mathscr{V} = \left(\int_0^T\mathrm{d}t\right)\left(\int_{B_R}\mathrm{d}x\,\mathrm{d}y\,\mathrm{d}z\right) = T\cdot\frac{4}{3}\pi R^3 .$$
> The four-volume of a ball-of-space persisting for time $T$ is its spatial volume times the duration.

**Step 2: The same four-volume in spherical coordinates, with the $r^2\sin\theta$ factor.**

> [!note]- Derivation
> In inertial spherical coordinates $g = -r^4\sin^2\theta$, so $\sqrt{|g|} = r^2\sin\theta$, and the four-volume element is $\mathrm{d}U = r^2\sin\theta\,\mathrm{d}t\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$. The region is the coordinate box $t\in[0,T]$, $r\in[0,R]$, $\theta\in[0,\pi]$, $\varphi\in[0,2\pi)$, so the integral factorises:
> $$\mathrm{vol}\,\mathscr{V} = \int_0^T\mathrm{d}t\int_0^R r^2\,\mathrm{d}r\int_0^\pi\sin\theta\,\mathrm{d}\theta\int_0^{2\pi}\mathrm{d}\varphi = T\cdot\frac{R^3}{3}\cdot 2\cdot 2\pi = \frac{4}{3}\pi R^3 T .$$
> This agrees with Step 1, as the coordinate-independence of the four-volume requires. Had we written $\int\mathrm{d}t\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi$ without the $r^2\sin\theta$, we would have got $T\cdot R\cdot\pi\cdot 2\pi$, a different and meaningless number — the factor $r^2\sin\theta$ is exactly the Jacobian compensator that rescues the geometric answer.

**Step 3: The integral of the 4-form $A = \rho\,\epsilon$ is $4\pi\rho_0 T\,[2a^3 - e^{-R/a}(R^2 a + 2Ra^2 + 2a^3)]$.**

> [!note]- Derivation
> The 4-form $A = \rho\,\epsilon$ has the single independent component (in spherical coordinates) $A_{0123} = \rho\,\epsilon_{0123} = \rho\sqrt{|g|} = \rho_0 e^{-r/a}\,r^2\sin\theta$. By the definition of the integral of a 4-form,
> $$\int_{\mathscr{V}} A = \int_{\mathscr{V}} A_{0123}\,\mathrm{d}t\,\mathrm{d}r\,\mathrm{d}\theta\,\mathrm{d}\varphi = \rho_0\int_0^T\mathrm{d}t\int_0^R e^{-r/a}r^2\,\mathrm{d}r\int_0^\pi\sin\theta\,\mathrm{d}\theta\int_0^{2\pi}\mathrm{d}\varphi .$$
> The angular integrals give $4\pi$ and the time integral gives $T$. For the radial integral, integrate by parts twice (or use $\int e^{-r/a}r^2\,\mathrm{d}r = -e^{-r/a}(a r^2 + 2a^2 r + 2a^3)$):
> $$\int_0^R e^{-r/a}r^2\,\mathrm{d}r = 2a^3 - e^{-R/a}\big(a R^2 + 2a^2 R + 2a^3\big).$$
> Hence
> $$\int_{\mathscr{V}} A = 4\pi\rho_0 T\Big[2a^3 - e^{-R/a}\big(a R^2 + 2a^2 R + 2a^3\big)\Big].$$
> This is the total amount of the density $\rho$ accumulated over the region — interpreting $A = \rho\,\epsilon$ as "$\rho$ times the volume element" makes $\int_{\mathscr{V}} A = \int_{\mathscr{V}}\rho\,\mathrm{d}U$, the spacetime integral of $\rho$. As $R\to\infty$ it tends to the finite total $8\pi\rho_0 a^3 T$, since the exponentially-decaying density has finite integral.

**Step 4: Why part 2 needed $r^2\sin\theta$ but part 3 is intrinsically coordinate-free.**

> [!note]- Derivation
> *Part 2 needed the factor* because the four-volume of a region is a *metric* quantity — "how big" is measured by $g$ — and the metric enters precisely through $\sqrt{|g|} = r^2\sin\theta$, which compensates the change-of-variable Jacobian so the answer matches the Cartesian computation.
>
> *Part 3 is coordinate-free regardless* because $\int_{\mathscr{V}} A$ for a 4-form $A$ depends only on $A$ and $\mathscr{V}$, not on coordinates: in *any* coordinates it equals the Lebesgue integral of the single antisymmetric component $A_{0123}$, and that component transforms exactly by the Jacobian, absorbing the change of variables on its own. The metric appears in this particular problem only because $A$ was *defined* as $\rho\,\epsilon$ and $\epsilon$ carries the metric; the integration recipe itself never consults $g$. This is the chapter's central dichotomy — volumes are metric, form integrals are not — seen in one computation.

> [!note]- Complete formal solution
> In inertial Cartesian coordinates $\sqrt{|g|}=1$ and $\mathrm{vol}\,\mathscr{V} = \int_0^T\mathrm{d}t\int_{B_R}\mathrm{d}^3x = T\cdot\frac{4}{3}\pi R^3$. In inertial spherical coordinates $g=-r^4\sin^2\theta$, so $\sqrt{|g|}=r^2\sin\theta$ and $\mathrm{vol}\,\mathscr{V} = \int_0^T\mathrm{d}t\int_0^R r^2\mathrm{d}r\int_0^\pi\sin\theta\,\mathrm{d}\theta\int_0^{2\pi}\mathrm{d}\varphi = T\cdot\frac{R^3}{3}\cdot2\cdot2\pi = \frac{4}{3}\pi R^3 T$, agreeing with the Cartesian value. For $A=\rho\,\epsilon$ with $\rho=\rho_0 e^{-r/a}$, the single component is $A_{0123}=\rho\sqrt{|g|}=\rho_0 e^{-r/a}r^2\sin\theta$, so $\int_{\mathscr{V}} A = \rho_0\cdot T\cdot 4\pi\cdot\int_0^R e^{-r/a}r^2\mathrm{d}r = 4\pi\rho_0 T[2a^3 - e^{-R/a}(aR^2+2a^2R+2a^3)]$. The four-volume needs the metric factor $r^2\sin\theta$ because a volume is a metric quantity; the 4-form integral is coordinate-independent on its own because the single antisymmetric component absorbs the Jacobian, the metric entering this problem only through the definition $A=\rho\,\epsilon$. $\blacksquare$

---

# Key Takeaways

**The metric volume factor $\sqrt{|g|}$ is not optional and is the first thing to write on leaving Cartesian coordinates.** The single most common error in spacetime integration is to carry the Cartesian habit "$\int f\,\mathrm{d}^4x$" into curvilinear coordinates, where it is wrong by the Jacobian $\sqrt{|g|}$. The trigger to watch for is *any* coordinate system other than inertial Cartesian: spherical, cylindrical, rotating, accelerated, or curvilinear coordinates all have $\sqrt{|g|}\ne 1$, and the factor $r^2\sin\theta$ in spherical coordinates is the familiar instance. The diagnostic is the sanity check of this exercise: compute the same four-volume in two coordinate systems and demand they agree — if they do not, you dropped a $\sqrt{|g|}$. The deeper reason the factor must be there is that it is precisely the inverse Jacobian, engineered so that $\sqrt{|g|}\,\mathrm{d}^4x$ is invariant; "$\mathrm{d}^4x$" alone is a coordinate artefact with no geometric meaning, while "$\sqrt{|g|}\,\mathrm{d}^4x$" is the measure of spacetime itself.

**Integrating a 4-form is never harder than a multivariable Lebesgue integral — extract the single component and integrate.** A 4-form on four-dimensional spacetime has exactly one independent component, $A_{0123}$, and its integral is by definition the ordinary Lebesgue integral of that one number over the coordinate domain. This collapses an apparently abstract "integrate a differential form" into a concrete iterated integral, and the trigger to recognise it is any integrand that is a top-degree form. The transferable point is that the apparatus of differential forms does not make integration harder; it makes it *cleaner*, because the antisymmetry guarantees coordinate-independence automatically. When you meet $\int_{\mathscr{V}} A$ for a 4-form, do not look for sophisticated machinery — find $A_{0123}$ and integrate it.

**Volumes are metric, form integrals are not — and one computation can show both faces.** This exercise deliberately put a metric quantity (the four-volume, part 2) and a form integral (part 3) side by side to expose the chapter's organising dichotomy. The four-volume needs $\sqrt{|g|}$ because "how big is this region" is a question only the metric can answer; the form integral needs no metric because the pairing between a form and a region never measures a size — it only evaluates the form on coordinate boxes and sums. The reason part 3 *looked* metric-dependent is a red herring: the metric entered only because the form $A$ was *built* from $\epsilon$, which carries the metric, not because the integration consulted $g$. The transferable diagnostic, applicable to every integral in the chapter, is to ask "is my integrand an alternating form of the right degree (then no metric) or a scalar density / a volume (then metric)?" — and that single question tells you whether $\sqrt{|g|}$ should appear, heading off most factor errors before they happen.
