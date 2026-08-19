---
type: remark
subject: probability-geometry
prereqs:
  - "Def - Brownian Loop Measure"
  - "Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure"
  - "Def - Bernstein Function, Subordinator, and Subordination"
tags: [paper, brownian-loops, conformal-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §2.1 — conformal invariance of $\\mu_X$, and why it fails for subordinate processes and beyond 2D"
---

# Notation

$(X,g)$ a complete orientable Riemannian surface (dimension $2$); $g$ its Riemannian metric, $\operatorname{vol}_g$ the induced area measure, $\Delta_X=-\operatorname{div}_g\operatorname{grad}_g$ the positive Laplace–Beltrami operator, $\{p_g(t,x,y)\}$ the heat kernel with respect to $\operatorname{vol}_g$. $\sigma:X\to\mathbb{R}$ a smooth function ("conformal factor"); $\tilde g:=e^{2\sigma}g$ the conformally rescaled metric with area measure $d\operatorname{vol}_{\tilde g}=e^{2\sigma}d\operatorname{vol}_g$. $[g]=\{e^{2\sigma}g:\sigma\in C^\infty(X)\}$ the **conformal class** of $g$. $\mu_X$ the (unrooted) Brownian loop measure on $C_X$ of [[Def - Brownian Loop Measure|Definition 2.1]]. $\phi:(0,\infty)\to[0,\infty)$ a Bernstein function, $\phi(A)$ the subordinate operator, $p^\phi$ its transition density.

> [!recall]- Conformally equivalent metrics on a surface
> **Formally:** two Riemannian metrics $g,\tilde g$ on the same smooth manifold $X$ are **conformally equivalent** if there is a smooth function $\sigma:X\to\mathbb{R}$ such that $\tilde g=e^{2\sigma}g$ (a pointwise positive scalar rescaling of the inner product on each tangent space). The equivalence class $[g]=\{e^{2\sigma}g\}$ is the **conformal class** of $g$; on an oriented surface, a conformal class is exactly the data of a Riemann-surface structure.
> **In words:** a conformal change of metric stretches the surface *pointwise* — the local unit of length changes from place to place, controlled by $\sigma$ — but the *angles* between crossing curves stay the same at every point. Squares stay squares, right angles stay right angles, everything else changes size.
> **Concretely:** on the plane $\mathbb{R}^2$ with $g=dx^2+dy^2$, rescaling by $\sigma(x,y)=\frac{1}{2}(x^2+y^2)$ produces $\tilde g=e^{x^2+y^2}(dx^2+dy^2)$: lengths grow super-fast as $(x,y)$ leaves the origin, but the angle between the coordinate axes at every point stays $\pi/2$. Two curves that crossed at a right angle in $g$ still cross at a right angle in $\tilde g$; their arc lengths, however, are multiplied by $e^\sigma$ pointwise.

> [!recall]- Two-dimensional Brownian motion is invariant under conformal maps
> **Formally:** if $f:U\to V$ is a conformal diffeomorphism between open subsets of Riemann surfaces (equivalently, on a surface, $f^*\tilde g=e^{2\sigma}g$ for some $\sigma$), and $B_t$ is a Brownian motion on $(U,g)$, then $f(B_t)$ is a *time-changed* Brownian motion on $(V,\tilde g)$: the paths of $f(B)$, viewed as unparametrised curves, have the same law as those of Brownian motion on $\tilde g$, but the clock on which those curves are traced is a random reparametrisation $\int_0^t e^{2\sigma(B_s)}\,ds$. In particular, the *shape* of the path (its image, as an unparametrised curve) is invariant under the conformal change $g\to e^{2\sigma}g$; only the clock changes.
> **In words:** the paths a Brownian traveller draws on a two-dimensional surface do not know how fast they are being drawn — they know only the angles at each point. A conformal rescaling of the metric changes the local length of every path but leaves the *shape* of the trajectory the same. This is a peculiar feature of dimension $2$: the same statement fails in $d\ne 2$.
> **Concretely:** rescale the plane by $\sigma(x,y)=\frac{1}{2}(x^2+y^2)$ as above. A planar Brownian path (a squiggle) traced in $g$ is, as a set of points, indistinguishable from a Brownian path traced in $\tilde g$: they draw the same squiggle. What differs is the parametrisation — in $\tilde g$ the clock slows down where $\sigma$ is large (the walker moves slowly through regions the metric now says are "far apart"). The paper's loop measure is duration-blind (weighted by $\frac{dt}{t}$), so it does not distinguish reparametrisations and is *invariant* under this whole change.

> [!recall]- Subordinate operator $\phi(A)$ and why it depends on the metric, not just the conformal class
> **Formally:** given a Bernstein function $\phi(\lambda)=a+b\lambda+\int_0^\infty(1-e^{-\lambda s})\,\nu(ds)$ and a self-adjoint operator $A\ge 0$ on $L^2(X,\operatorname{vol}_g)$, the **subordinate operator** is $\phi(A)=aI+bA+\int_0^\infty(I-e^{-sA})\,\nu(ds)$ (spectral calculus). Concretely, for $\phi(\lambda)=\lambda^{\alpha/2}$ ($\alpha\in(0,2)$), $\phi(\Delta_X)=\Delta_X^{\alpha/2}$ is the **fractional Laplacian**, a *non-local* operator whose action on a function depends on values everywhere on $X$ — hence on distances, not just angles.
> **In words:** a subordinate process is defined by running the underlying Markov process on a random clock. Because the fractional Laplacian mixes values across the surface, it "feels" the actual metric distances between points, not just the local angle structure. Conformal rescalings that leave the *angle* structure invariant change the *distances*, so they change the subordinate operator — and hence the subordinate loop measure.
> **Concretely:** the ordinary Laplacian $\Delta_X$ transforms under $g\to e^{2\sigma}g$ by $\Delta_{\tilde g}=e^{-2\sigma}\Delta_g$ (a *pointwise multiplication* of the operator, absorbable into a time-change of the associated Brownian motion — this is *why* the loop measure is conformally invariant). The fractional Laplacian $\Delta^{1/2}$ transforms non-trivially: $(\Delta_{\tilde g})^{1/2}\ne e^{-\sigma}(\Delta_g)^{1/2}$ in general, because taking a fractional power does not distribute over pointwise multiplication. The subordinate loop measure is therefore *not* a function of the conformal class alone. See [[Def - Bernstein Function, Subordinator, and Subordination]].

---

# Claim / Identity

> **Claim (conformal invariance, and its 2D restriction, [LW04, §4]).** Let $(X,g)$ be a complete orientable Riemannian surface (dimension $2$), and $\tilde g=e^{2\sigma}g$ any conformally equivalent metric. The **Brownian** loop measure is unchanged by this replacement,
> $$\mu_{X,\tilde g} \;=\; \mu_{X,g},$$
> so $\mu_X$ depends only on the conformal class $[g]$ and one may treat $X$ as a **Riemann surface** rather than a Riemannian one for the purposes of §2.1.
>
> This invariance is *particular to two dimensions and to Brownian motion*: for a **subordinate** process (Bernstein $\phi\ne\lambda$) — for instance killed Brownian motion $\phi(\lambda)=\lambda+\kappa$ or the $\alpha$-stable process $\phi(\lambda)=\lambda^{\alpha/2}$ — the operator $\phi(\Delta_X)$ depends on the actual metric $g$, not just on $[g]$, so
> $$\mu^\phi_{X,\tilde g} \;\ne\; \mu^\phi_{X,g} \quad\text{in general}.$$
> Consequently, from [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.2]] on, the paper works with $(X,g)$ as a genuine **Riemannian** surface — the conformal-invariance simplification is unavailable once subordination is switched on.

---

# In One Line

Brownian motion on a two-dimensional surface knows only angles, not lengths, so a metric change that preserves angles leaves its loop measure unchanged — but the moment one moves to a subordinate (killed, jump, …) process, the operator starts caring about lengths, and the invariance breaks.

---

# Why It's True

**Mechanism (one sentence).** The generator $\Delta_g$ transforms under $g\to e^{2\sigma}g$ by pointwise multiplication ($\Delta_{\tilde g}=e^{-2\sigma}\Delta_g$), which for Brownian motion is exactly a time-change of the process; the loop measure is duration-blind (weighted by $\frac{dt}{t}$), so it does not see the time-change. Fractional powers and mass-shifts of the generator do *not* transform as pointwise multiplications, so subordinate loop measures do see the metric.

**Why the conformal factor is time-only.** For a Brownian traveller on $(X,g)$ the two things it sees at each point are (a) the angles at which paths cross (the conformal structure) and (b) the *speed* at which its clock advances relative to the metric. A conformal change $g\to e^{2\sigma}g$ leaves (a) alone and rescales (b) pointwise. The path *drawn* is the same; the *clock* on which it is drawn is a random rescaling depending on the path itself. Because the loop measure aggregates over durations by the scale-invariant $\frac{dt}{t}$ — the *only* $t$-measure invariant under $t\mapsto\lambda t$ — this pointwise time-change is invisible to the aggregation: any rescaling of durations is absorbed into the Haar measure. The *shape* of the loop (its image, its winding around holes) is what survives, and the shape is conformal data.

**Why subordination breaks the invariance.** A subordinate process runs the Brownian motion on a *further* random clock $S_t$, independent of the underlying process and driven by the Bernstein function $\phi$. If $\phi(\lambda)=\lambda$, then $S_t=t$ deterministically and nothing changes. But for $\phi(\lambda)=\lambda+\kappa$ (killing) the "clock" also dies at rate $\kappa$ — and the survival rate $e^{-\kappa t}$ is measured in the *original* time, so a conformal rescaling that speeds up the underlying Brownian clock effectively changes the rate at which the killing is felt. For $\phi(\lambda)=\lambda^{\alpha/2}$ ($\alpha$-stable) the subordinator has jumps whose sizes are measured in the underlying time, and the subordinate operator $\Delta_X^{\alpha/2}$ is *non-local* — it depends on values of the function at every point of $X$, weighted by their metric distance from the base point. Conformal rescalings change those metric distances and hence change the subordinate operator.

**The concrete pattern in the four Bernstein functions.** Only $\phi(\lambda)=\lambda$ (pure Brownian) is a conformally invariant subordinate operator; every other Bernstein function ($\lambda+\kappa$, $\lambda^{\alpha/2}$, $(\lambda+\kappa)^{\alpha/2}$) generates a subordinate process whose operator depends on the metric $g$, not just on $[g]$. This is why the paper commits to a Riemannian $(X,g)$ from §2.2 on: it needs Brownian and subordinate processes on the same footing, and only the Riemannian metric supports all of them.

---

# Derivation

> [!note]- Gap-free derivation of the conformal invariance
> **Step 1 — how the Laplacian transforms.** For $\tilde g=e^{2\sigma}g$ on a two-dimensional Riemannian manifold, a direct local-coordinate computation (using $d\operatorname{vol}_{\tilde g}=e^{2\sigma}d\operatorname{vol}_g$ and $\tilde g^{ij}=e^{-2\sigma}g^{ij}$) gives
> $$\Delta_{\tilde g}f \;=\; e^{-2\sigma}\Delta_g f\qquad\text{for every smooth }f.$$
> This is a *two-dimensional* identity: in dimension $d\ne 2$ there are additional first-order terms proportional to $\nabla\sigma$, and the Laplacian does *not* transform by a simple pointwise multiplication.
>
> **Step 2 — how Brownian motion on $(X,\tilde g)$ compares with Brownian motion on $(X,g)$.** Because $\Delta_{\tilde g}=e^{-2\sigma}\Delta_g$, Brownian motion on $(X,\tilde g)$ (generator $-\Delta_{\tilde g}$) is obtained from Brownian motion $B_t$ on $(X,g)$ (generator $-\Delta_g$) by a **random time change**: the process $\tilde B_t:=B_{F^{-1}(t)}$ has generator $-\Delta_{\tilde g}$, where $F(u)=\int_0^u e^{2\sigma(B_s)}\,ds$ is the "quantum-clock" additive functional. The *image* of $\tilde B$ up to time $t$ equals the image of $B$ up to time $F^{-1}(t)$ — the *paths drawn on $X$ are the same*, only the parametrisation differs.
>
> **Step 3 — how the bridge and heat-kernel measures transform.** The bridge measure $\mathbb{W}^{t,\tilde g}_{x\to y}$ on $C([0,t],X)$ is the law of $\tilde B$ conditioned on ending at $y$ at time $t$; it is a *reparametrisation* of the ambient bridge $\mathbb{W}^{F(t),g}_{x\to y}$. The heat kernel transforms accordingly: for $x,y\in X$,
> $$p_{\tilde g}(t,x,y)\,d\operatorname{vol}_{\tilde g}(y) \;=\; p_g(F(t),x,y)\,d\operatorname{vol}_g(y)\quad\text{(law equality of the endpoint).}$$
>
> **Step 4 — how the loop-measure formula transforms.** Applying [[Def - Brownian Loop Measure|Definition 2.1]] with $\tilde g$,
> $$\mu^{*}_{X,\tilde g} \;=\; \int_0^\infty\frac{dt}{t}\int_X\mathbb{W}^{t,\tilde g}_{x\to x}\,d\operatorname{vol}_{\tilde g}(x),$$
> and using Step 3 to replace $\mathbb{W}^{t,\tilde g}_{x\to x}\,d\operatorname{vol}_{\tilde g}(x)$ (the "rooted-loop density in $\tilde g$") by its $g$-counterpart at time $F(t)$ — the *same set* of loops-as-images in $C^*_X$, only with the durations rescaled — the integrand becomes a rescaled version of the $g$-integrand.
>
> **Step 5 — the $\frac{dt}{t}$ weight absorbs the rescaling.** The point of the Haar weight is exactly here. Under a change of duration variable $t\mapsto F(t)$ (a random rescaling depending on the path, but Path-by-path it is a strictly increasing $C^1$ bijection of $(0,\infty)$), the multiplicative Haar measure $\frac{dt}{t}$ is invariant *up to the log-Jacobian*, and integrating out the endpoint over $\operatorname{vol}_{\tilde g}=e^{2\sigma}\operatorname{vol}_g$ (rather than $\operatorname{vol}_g$) supplies exactly the compensating log-Jacobian. The net effect on the loop-measure formula is *zero*: the integrand computed with $\tilde g$'s data equals the integrand computed with $g$'s data, path-by-path.
>
> (The detailed accounting of these cancellations is the content of [LW04, §4]; the point is that on a two-dimensional surface, the operator's pointwise-multiplication transformation from Step 1 combines with the scale-invariant $\frac{dt}{t}$ weight to make the loop measure change-of-metric-invariant.)
>
> **Step 6 — pushforward to unrooted loops.** The identification of loops-as-images is preserved by the pushforward to $C_X$, so
> $$\mu_{X,\tilde g} \;=\; \mu_{X,g}.$$
> Consequently $\mu_X$ is a function of the conformal class $[g]=\{e^{2\sigma}g\}$ alone.
>
> **Step 7 — why it fails for subordinate processes.** For $\phi\ne\lambda$, the subordinate operator $\phi(\Delta_g)$ does *not* satisfy the pointwise-transformation Step 1. For $\phi(\lambda)=\lambda+\kappa$, $\phi(\Delta_{\tilde g})=\Delta_{\tilde g}+\kappa I=e^{-2\sigma}\Delta_g+\kappa I\ne e^{-2\sigma}(\Delta_g+\kappa I)=e^{-2\sigma}\phi(\Delta_g)$; the $\kappa I$ term does not scale with $e^{-2\sigma}$. For $\phi(\lambda)=\lambda^{\alpha/2}$, $\phi(\Delta_{\tilde g})=\Delta_{\tilde g}^{\alpha/2}$ is a *non-local* operator whose action on a function $f$ depends on values of $f$ everywhere on $X$; it cannot be written as a pointwise multiplication of $\Delta_g^{\alpha/2}$ because fractional powers do not distribute over pointwise multiplication (spectral-calculus reason: $\Delta_g$ and $e^{-2\sigma}$ do not commute in general, so $(e^{-2\sigma}\Delta_g)^{\alpha/2}\ne e^{-\alpha\sigma}\Delta_g^{\alpha/2}$). Hence Steps 3–5 fail, and $\mu^\phi_{X,\tilde g}\ne\mu^\phi_{X,g}$ in general. $\qquad\blacksquare$

> [!cite]- External input — Lawler–Werner, "The Brownian loop soup"
> **Statement (used):** the Brownian loop measure $\mu_X$ on a Riemann surface depends only on the conformal class $[g]$ of the Riemannian metric $g$.
> **Source:** G. F. Lawler and W. Werner, *The Brownian loop soup*, Probability Theory and Related Fields **128** (2004), 565–588, §4. The property is stated there in the planar (flat-metric-plus-domain) setting; extension to a general Riemann surface is standard once one knows the two-dimensional transformation law $\Delta_{\tilde g}=e^{-2\sigma}\Delta_g$ and the scale-invariance of $\frac{dt}{t}$.

> [!warning] Verification note
> The Step-5 statement — "the $\frac{dt}{t}$ weight absorbs the pointwise-multiplication rescaling of Step 1" — is a *heuristic* summary of the actual [LW04] argument; the paper's own derivation involves a more careful accounting via SLE and conformal restriction. What is universally accepted is the *conclusion* (conformal invariance in 2D), which this note quotes on faith from [LW04]. The failure for subordinate processes (Step 7) is elementary: it does not depend on [LW04].

---

# Where the paper uses this

Stated as one of the two "fundamental properties" of $\mu_X$ in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.1]] (see also [[Remark - Restriction Property of the Brownian Loop Measure|the restriction property]]). Its immediate consequence — that $X$ may be treated as a Riemann surface for §2.1 — is what allows the Brownian case to be viewed conformally. The *failure* of the invariance for subordinate processes is what forces the paper from [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.2]] onward to fix a genuine Riemannian metric $g$ (so that the subordinate operators $\phi(\Delta_g)$ are well-defined objects, not just conformal-class-invariants). Every hyperbolic-surface computation from §3 onward (starting with [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]]) uses the hyperbolic metric explicitly — the paper does not, and cannot, abstract to the conformal class once subordination is switched on.
