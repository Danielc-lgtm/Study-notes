---
type: remark
subject: probability-geometry
prereqs:
  - "Def - Brownian Loop Measure"
  - "Def - Heat Kernel and Heat Semigroup"
  - "Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure"
  - "Def - Signed and Infinite Measures for Loop Measures"
tags: [paper, brownian-loops, measure-theory]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §2.1 — small-$t$ (short-loop) divergence of the total loop mass"
---

# Notation

$(X,g)$ a complete orientable Riemannian surface, area measure $\operatorname{vol}_g$, $\operatorname{Area}(X)=\int_X d\operatorname{vol}_g\in(0,\infty]$. $p(t,x,y):(0,\infty)\times X\times X\to(0,\infty)$ the heat kernel of the positive Laplace–Beltrami operator $\Delta_X$; $p(t,x,x)$ its on-diagonal value at the basepoint $x$. $\mathbb{W}^t_{x\to x}$ the Brownian bridge measure from $x$ back to $x$ in time $t$, of total mass $|\mathbb{W}^t_{x\to x}|=p(t,x,x)$. $\mu^*_X=\int_0^\infty\frac{dt}{t}\int_X\mathbb{W}^t_{x\to x}\,d\operatorname{vol}_g(x)$ the rooted Brownian loop measure ([[Def - Brownian Loop Measure|Definition 2.1]]); $|\mu^*_X|$ its total mass. All symbols free except the bound integration variables $t\in(0,\infty)$, $x\in X$.

> [!recall]- Short-time on-diagonal heat-kernel asymptotic $p(t,x,x)\sim 1/(4\pi t)$
> **Formally:** for any $x$ in the interior of a Riemannian surface $(X,g)$, the heat kernel $p(t,x,y)$ satisfies $\lim_{t\downarrow 0}\,4\pi t\,p(t,x,x)=1$, uniformly on compact subsets of the interior. Equivalently, $p(t,x,x)=\frac{1}{4\pi t}\bigl(1+O(t)\bigr)$ as $t\downarrow 0$, with the leading constant $\frac{1}{4\pi}$ dictated by the surface dimension being $2$ and the paper's speed-$2$ Brownian normalisation.
> **In words:** for very short times, the random walker on $X$ has barely wandered — it is still essentially in the flat tangent plane at $x$, where the heat kernel is the two-dimensional Gaussian with density $\frac{1}{4\pi t}e^{-|x-y|^2/(4t)}$; at $y=x$ this Gaussian evaluates to $\frac{1}{4\pi t}$. Every Riemannian surface *looks flat* near any interior point at scales small enough that curvature has no time to matter, so this flat-space value is what a curved surface's diagonal heat kernel converges to as $t\to 0$.
> **Concretely:** on the flat plane $\mathbb{R}^2$ (curvature zero) the identity is exact for every $t$: $p(t,x,x)=\frac{1}{4\pi t}$. On the round sphere of radius $R$ (uniform positive curvature), the same $\frac{1}{4\pi t}$ leading term holds as $t\downarrow 0$, with an $O(t)$ correction whose coefficient involves the scalar curvature; at moderate times the on-diagonal kernel falls off, and at very large $t$ it equilibrates to $\frac{1}{4\pi R^2}$ (the reciprocal of the sphere's area). On the hyperbolic plane $\mathbb{H}^2$ (uniform negative curvature) the leading term is still $\frac{1}{4\pi t}$, so the *small-$t$* behaviour is identical. This is a general two-dimensional fact, see [[Def - Heat Kernel and Heat Semigroup]].

> [!recall]- The multiplicative Haar measure $\frac{dt}{t}$ on $(0,\infty)$
> **Formally:** the $\sigma$-finite Borel measure on $(0,\infty)$ characterised by $\int_{\lambda a}^{\lambda b}\frac{dt}{t}=\int_a^b\frac{dt}{t}$ for every $\lambda>0$ and $0<a<b<\infty$; infinite total mass, finite on every interval bounded away from $0$ and $\infty$.
> **In words:** the scale-invariant weight on positive reals — doubling every $t$ leaves the mass of any interval unchanged. It counts *ratios* of durations, not their differences.
> **Concretely:** the substitution $u=\log t$ turns $\int_a^b f(t)\,\frac{dt}{t}$ into $\int_{\log a}^{\log b}f(e^u)\,du$ (plain Lebesgue in the log-time coordinate). So $\int_1^{e^n}\frac{dt}{t}=n$: each multiplicative factor of $e$ contributes one unit of mass. The divergences at $0$ and $\infty$ correspond to $\log 0=-\infty$ and $\log\infty=+\infty$. See [[Def - Signed and Infinite Measures for Loop Measures]].

---

# Claim / Identity

> **Claim (small-$t$ divergence of the total loop mass).** The total mass of the rooted Brownian loop measure is infinite,
> $$|\mu^*_X| \;=\; \int_0^\infty\frac{dt}{t}\int_X p(t,x,x)\,d\operatorname{vol}_g(x) \;=\; +\infty,$$
> and the divergence is confined to the small-$t$ end of the integral. Concretely, near $t=0$ the integrand behaves as
> $$\frac{1}{t}\int_X p(t,x,x)\,d\operatorname{vol}_g(x) \;\sim\; \frac{\operatorname{Area}(X)}{4\pi\,t^2}\qquad\text{as }t\downarrow 0,$$
> and $\int_0\frac{dt}{t^2}=+\infty$. The large-$t$ end is integrable when $X$ has finite area and there is spectral gap; in either case, the infinity in $|\mu^*_X|$ is a **short-loop** effect, not a long-loop one.

---

# In One Line

The total Brownian-loop mass on a Riemannian surface is infinite because arbitrarily short loops are counted, and there are far too many of them; when loops are later sorted by topological type, the short ones cluster into the trivial homotopy class and *every non-trivial class carries finite mass* — that is why this innocuous observation is the seed of the paper.

---

# Why It's True

**Mechanism (one sentence).** Two-dimensional locality forces $p(t,x,x)$ to blow up as $1/(4\pi t)$ near $t=0$, the extra factor of $1/t$ in the duration weight pushes the small-$t$ integrand to $1/t^2$, and $\int_0 dt/t^2$ diverges.

Physically: for very small $t$ the Brownian walker has barely moved, so *every* point of $X$ is a plausible basepoint of a tiny loop returning to itself — the on-diagonal heat kernel captures exactly this "how likely to still be back at $x$" density, and its $1/t$ divergence says short loops are exponentially more numerous than long ones (in the scale-invariant $\frac{dt}{t}$ accounting). The divergence is not a defect of the definition; it is the correct statement that "count every loop of every duration on equal footing" produces infinitely many when arbitrarily short durations are allowed. What redeems the construction is that **every short loop is contractible** — a loop small enough that it fits inside a coordinate patch cannot wind around any hole — so once loops are sorted by topological type, all the divergence concentrates in the trivial class and each non-trivial class is finite. That per-class finiteness is [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] and it is the paper's first substantive result.

---

# Derivation

> [!note]- Gap-free derivation of the small-$t$ divergence
> **Step 1 — write the total mass as an iterated integral.** By definition of the rooted Brownian loop measure,
> $$\mu^*_X \;=\; \int_0^\infty\frac{dt}{t}\int_X \mathbb{W}^t_{x\to x}\,d\operatorname{vol}_g(x).$$
> Taking total masses on both sides and using $|\mathbb{W}^t_{x\to x}|=p(t,x,x)$ (the bridge-mass identity from [[Def - Disintegration and the Bridge Measure|disintegration]]),
> $$|\mu^*_X| \;=\; \int_0^\infty\frac{dt}{t}\int_X p(t,x,x)\,d\operatorname{vol}_g(x).$$
> The order of integration is legitimate because the integrand is non-negative, so Tonelli applies with no integrability hypothesis.
>
> **Step 2 — insert the short-time asymptotic.** By the small-$t$ on-diagonal asymptotic (recall above), for each interior $x\in X$ we have $p(t,x,x)\sim\frac{1}{4\pi t}$ as $t\downarrow 0$, uniformly on compact subsets of the interior. When $\operatorname{Area}(X)<\infty$ (the paper's finite-area case), integrating over $X$ against $\operatorname{vol}_g$ gives
> $$\int_X p(t,x,x)\,d\operatorname{vol}_g(x) \;\sim\; \frac{\operatorname{Area}(X)}{4\pi\,t}\qquad\text{as }t\downarrow 0,$$
> since the leading pointwise asymptotic is uniform enough (this uniformity is a standard fact for Weyl-type heat-kernel asymptotics on compact — or, with the appropriate technical care, geometrically finite — Riemannian surfaces). When $\operatorname{Area}(X)=+\infty$ the same conclusion holds after replacing $\operatorname{Area}(X)$ by the area of any compact subregion that already exceeds a chosen threshold — the divergence is a local statement and needs no global control.
>
> **Step 3 — combine the two factors.** Substituting the Step-2 asymptotic into Step 1's integrand,
> $$\frac{1}{t}\int_X p(t,x,x)\,d\operatorname{vol}_g(x) \;\sim\; \frac{\operatorname{Area}(X)}{4\pi\,t^2}\qquad\text{as }t\downarrow 0.$$
> Cutting the outer $\int_0^\infty$ at a small $\epsilon>0$,
> $$\int_0^\epsilon\frac{dt}{t}\int_X p(t,x,x)\,d\operatorname{vol}_g(x) \;\ge\; \frac{\operatorname{Area}(X)}{4\pi}\cdot\frac{1}{2}\int_0^\epsilon\frac{dt}{t^2}$$
> (the factor $\frac{1}{2}$ absorbs any $(1+o(1))$ term from the asymptotic, valid on a sufficiently small $\epsilon$-neighbourhood of $0$). The elementary integral
> $$\int_0^\epsilon\frac{dt}{t^2} \;=\; \Big[-\frac{1}{t}\Big]_0^\epsilon \;=\; +\infty$$
> (the antiderivative $-1/t$ diverges at $t=0$) shows that the small-$t$ piece of $|\mu^*_X|$ is already infinite. Hence $|\mu^*_X|=+\infty$, and the divergence is *entirely* a short-loop (small-$t$) effect.
>
> **Step 4 — check that the divergence is only at small $t$.** The large-$t$ end is finite when $X$ has finite area and there is a spectral gap: on a compact hyperbolic surface the small $\Delta_X$-eigenvalue is $0$ (constant function) and the next is $\lambda_1>0$, so $p(t,x,x)\to 1/\operatorname{Area}(X)$ as $t\to\infty$ with exponential rate $e^{-\lambda_1 t}$ in the difference, and $\int_1^\infty\frac{dt}{t}\cdot\text{const}=+\infty$ *would* threaten a large-$t$ log-divergence — but the paper's finite-mass results (§3, §5) always work on the *per-topological-class* mass, or after subtracting off exactly this trivial-class piece. On finite-area cases without a spectral gap (cusps, infinite-area ends) an $O(t^{-3/2})$-type decay of $p(t,x,x)$ makes the large-$t$ integral converge; the paper handles these by geometric finiteness (see [[Def - Fuchsian Group and the Hyperbolic Quotient Surface]]). In every case the *small*-$t$ piece is what makes $|\mu^*_X|$ infinite. $\qquad\blacksquare$

---

# Where the paper uses this

Stated on the Brownian-loop side in [[Def - Brownian Loop Measure|Definition 2.1]] (§2.1) and inherited by the [[Def - Dirichlet Form Loop Measure|Dirichlet-form]] and [[Def - Subordinate Brownian Loop Measure|subordinate]] cases (§2.2, §2.4) where the same $\frac{dt}{t}$ weighting sits atop an $O(t^{-1})$ on-diagonal kernel (for Brownian) or an $O(t^{-2/\alpha})$ one (for $\alpha$-stable). The observation is the *seed* of the entire paper: [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] shows that the divergence disappears once loops are sorted by topological type — every non-trivial class carries finite mass because winding around a hole forces the loop to be long. [[Thm - Finiteness of the Total Loop Mass|Theorem 5.1]] renormalises the divergence by subtracting off the small-$t$ singular part explicitly. Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.1]]; used in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3]] and [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5]].
