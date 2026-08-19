---
type: definition
subject: probability-geometry
prereqs:
  - "Def - Disintegration and the Bridge Measure"
  - "Def - Signed and Infinite Measures for Loop Measures"
  - "Def - Heat Kernel and Heat Semigroup"
  - "Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure"
  - "Def - Brownian Motion on a Riemannian Manifold"
tags: [paper, brownian-loops, measure-theory]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 2.1"
---

# Notation

$(X,g)$ a **complete orientable Riemannian surface** (a 2-dimensional smooth manifold with a smoothly varying inner product on tangent vectors), possibly with boundary; when there is a boundary the paper imposes Dirichlet boundary conditions, so Brownian motion is *killed* on first hitting $\partial X$. $\operatorname{vol}_g$ denotes the induced area measure; $\Delta_X = -\operatorname{div}_g\operatorname{grad}_g$ the positive Laplace–Beltrami operator (spectrum in $[0,\infty)$); $p(t,x,y):(0,\infty)\times X\times X\to(0,\infty)$ the heat kernel. Time $t>0$; points $x,y\in X$.

Path space: $C([0,t],X)$ is the set of continuous maps $\omega:[0,t]\to X$. **Wiener measure** $\mathbb{W}^t_x$ is the law on $C([0,t],X)$ of speed-2 Brownian motion started at $x$, run for time $t$; **bridge measure** $\mathbb{W}^t_{x\to y}$ is its unnormalised conditioning on the endpoint $\omega(t)=y$. The **rooted loop space** is
$$C^*_X := \{(t,\omega) : t\ge 0,\; \omega\in C([0,t],X),\; \omega(0)=\omega(t)\},$$
each element a duration $t$, a continuous path $\omega$, and a marked basepoint $\omega(0)=\omega(t)$; the slice $\{t=0\}$ is the constant point-loops.

> [!recall]- Laplace–Beltrami operator $\Delta_X$, heat kernel $p(t,x,y)$, Brownian motion on $X$
> **Formally:** $\Delta_X = -\operatorname{div}_g\operatorname{grad}_g$ is the *positive* Laplace–Beltrami operator on the Riemannian surface $(X,g)$ (spectrum in $[0,\infty)$); the semigroup $e^{-t\Delta_X}$ has integral kernel the **heat kernel** $p:(0,\infty)\times X\times X\to(0,\infty)$, $(e^{-t\Delta_X}f)(x)=\int_X p(t,x,y)f(y)\,d\operatorname{vol}_g(y)$; **Brownian motion at speed 2** is the continuous Markov process with generator $-\Delta_X$ and transition density $p$, its law $\mathbb{W}^t_x$ on $C([0,t],X)$.
> **In words:** $p(t,x,y)$ is the probability density that a random walker on $X$ starting at $x$ is found at $y$ after time $t$. "Brownian motion" is the continuous-time random walk you get from a discrete random walk with vanishing step size. The "speed 2" and the minus-sign are bookkeeping conventions that make the flat-space short-time behaviour $p(t,x,x)\sim 1/(4\pi t)$ come out clean.
> **Concretely:** on the flat plane $\mathbb{R}^2$, $p(t,x,y) = \frac{1}{4\pi t}e^{-|x-y|^2/(4t)}$ — a Gaussian bell widening with $t$. At $t=1$, $x=(0,0)$, $y=(1,0)$: $p(1,x,y) = \frac{1}{4\pi}e^{-1/4} \approx 0.062$. The on-diagonal value $p(t,x,x) = 1/(4\pi t)$ blows up as $t\to 0$ (the walker is definitely still near $x$ for tiny $t$) and decays as $t\to\infty$ (it wanders off). On any compact surface the small-$t$ diagonal still behaves as $1/(4\pi t)$ — locally every surface looks flat — but at large $t$ it equilibrates to $1/\operatorname{Area}(X)$. See [[Def - Heat Kernel and Heat Semigroup]], [[Def - Brownian Motion on a Riemannian Manifold]], [[Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure]].

> [!recall]- Bridge measure $\mathbb{W}^t_{x\to y}$ (disintegration of Wiener measure over the endpoint)
> **Formally:** disintegrating $\mathbb{W}^t_x$ over the endpoint map $\omega\mapsto\omega(t)$ gives a family of unnormalised measures $\mathbb{W}^t_{x\to y}$ on $C([0,t],X)$, each concentrated on paths ending at $y$, with $|\mathbb{W}^t_{x\to y}|=p(t,x,y)$ and $\mathbb{W}^t_x=\int_X\mathbb{W}^t_{x\to y}\,d\operatorname{vol}_g(y)$. The normalised measure $\mathbb{W}^t_{x\to y}/p(t,x,y)$ is the **Brownian bridge** from $x$ to $y$ in time $t$ (an honest probability measure on paths).
> **In words:** $\mathbb{W}^t_{x\to y}$ is the collection of Brownian paths of duration $t$ starting at $x$ and forced to land at $y$, weighted so the total weight equals the probability-density $p(t,x,y)$ of landing there. Setting $y=x$ gives the *loops*: paths that start and end at the same point.
> **Concretely:** to sample from the bridge from $(0,0)$ to $(0,0)$ in $\mathbb{R}^2$ over time $t=1$, sample many Brownian paths starting at the origin; keep only those landing within Euclidean distance $\epsilon$ of the origin; the empirical distribution of those (divided by $\pi\epsilon^2$) converges as $\epsilon\to 0$ to the normalised bridge, a probability measure on continuous loops of unit duration. The bridge $\mathbb{W}^1_{0\to 0}$ itself is that probability measure scaled by $p(1,0,0)=1/(4\pi)$. See [[Def - Disintegration and the Bridge Measure]].

> [!recall]- The multiplicative (Haar) measure $\frac{dt}{t}$ on $(0,\infty)$
> **Formally:** $\frac{dt}{t}$ is the $\sigma$-finite Borel measure on $(0,\infty)$ invariant under the multiplicative group $(0,\infty)\overset{\times}{\to}(0,\infty)$: for every $\lambda>0$ and every $0<a<b<\infty$, $\int_{\lambda a}^{\lambda b}\frac{dt}{t}=\int_a^b\frac{dt}{t}$. Infinite total mass ($\int_0^1=\int_1^\infty=+\infty$); finite on each interval bounded away from $0$ and $\infty$.
> **In words:** $\frac{dt}{t}$ counts *ratios* of durations, not differences. Doubling every loop's duration leaves its total weight unchanged. It is the natural "duration-blind" way to aggregate loops of every length equally.
> **Concretely:** the substitution $u=\log t$ turns $\int_a^b f(t)\,\frac{dt}{t}$ into $\int_{\log a}^{\log b}f(e^u)\,du$ — plain Lebesgue measure in the log-time coordinate. So $\int_1^{e}\frac{dt}{t}=1$, $\int_1^{e^2}\frac{dt}{t}=2$, $\int_1^{e^{10}}\frac{dt}{t}=10$: each factor of $e$ contributes one unit of mass. The infinity at $0$ is $\log 0=-\infty$; at $\infty$ is $\log\infty=+\infty$. See [[Def - Signed and Infinite Measures for Loop Measures]].

> [!recall]- $\sigma$-finite measure
> **Formally:** a measure $\mu$ on a measurable space $(\Omega,\mathcal F)$ is **$\sigma$-finite** if $\Omega=\bigcup_{n\ge 1}\Omega_n$ with each $\mu(\Omega_n)<\infty$.
> **In words:** the space can be broken into countably many pieces of finite mass each. Total mass may be $+\infty$, but you never lose the machinery of integration — Tonelli, Fubini, monotone convergence, dominated convergence all work as usual on $\sigma$-finite measures.
> **Concretely:** Lebesgue measure on $\mathbb{R}$ has $\mu(\mathbb{R})=+\infty$ but $\mathbb{R}=\bigcup_n[-n,n]$ with $\mu([-n,n])=2n<\infty$. The measure $\frac{dt}{t}$ on $(0,\infty)$ is $\sigma$-finite by $\bigcup_n [1/n,n]$, each of mass $\int_{1/n}^n\frac{dt}{t}=2\log n<\infty$. See [[Def - σ-Finite Measure]].

---

# Statement

> **Definition (rooted Brownian loop measure; Belyaev–Huseynli Def. 2.1).** On a complete orientable Riemannian surface $(X,g)$ with Brownian bridge measures $\{\mathbb{W}^t_{x\to y}\}$, the **rooted Brownian loop measure** on $C^*_X$ is the $\sigma$-finite measure
> $$\mu^*_X \;:=\; \int_0^\infty \frac{dt}{t}\int_X \mathbb{W}^t_{x\to x}\,d\operatorname{vol}_g(x).$$
> The **Brownian loop measure** $\mu_X$ is the pushforward of $\mu^*_X$ to the quotient $C_X := C^*_X/\!\sim$ of unparametrised, oriented, unrooted loops, where $(t,\omega)\sim(s,\tilde\omega)$ iff there is an increasing continuous bijection of parametrising circles $i:[0,t]/_{0\sim t}\to[0,s]/_{0\sim s}$ with $\tilde\omega(i(r))=\omega(r)$ (equivalently, generated by the *circular time-shift* $\mathrm{shift}_{s_0}(t,\omega)=(t,\omega(\cdot+s_0\bmod t))$).

---

# In One Line

A duration-blind, scale-invariant way to weigh *every* Brownian loop on the surface: pick a loop's duration by the multiplicative measure $\frac{dt}{t}$, pick its basepoint by the area measure, then place a bridge-from-$x$-back-to-$x$ mass. The total is infinite (a small-$t$ effect), but each topological type of loop will turn out to carry finite mass — the seed of the whole paper.

---

# Motivation and Unpacking

**The construction, motivated.** We want to weigh *all* loops on $X$ on equal footing, regardless of duration or basepoint. A loop of duration $t$ rooted at $x$ has "density" the Brownian bridge $\mathbb{W}^t_{x\to x}$ (an unnormalised measure on paths starting and ending at $x$, of total mass $p(t,x,x)$). Aggregating first over basepoints $x\in X$ against the area measure $d\operatorname{vol}_g$ and then over durations $t>0$ against *some* measure on $(0,\infty)$ gives the loop measure. The only choice is the duration weight, and the requirement of **scale-invariance** — no privileged clock speed — picks it out uniquely: on the positive reals the multiplicative Haar measure $\frac{dt}{t}$ is the unique (up to a constant) measure invariant under $t\mapsto\lambda t$. Weighting durations by $\frac{dt}{t}$ rather than $dt$ is what makes this measure the natural one, and it is why the same construction repeats verbatim for the [[Def - Dirichlet Form Loop Measure|Dirichlet-form]] and [[Def - Subordinate Brownian Loop Measure|subordinate]] generalisations.

**Why the total mass is infinite, and where the divergence lives.** Using $|\mathbb{W}^t_{x\to x}|=p(t,x,x)$, the total mass is
$$|\mu^*_X| \;=\; \int_0^\infty\frac{dt}{t}\int_X p(t,x,x)\,d\operatorname{vol}_g(x).$$
Near $t=0$ the on-diagonal heat kernel behaves as $p(t,x,x)\sim 1/(4\pi t)$ (local flatness of any Riemannian surface), so the integrand behaves like $\frac{1}{t}\cdot\frac{\operatorname{Area}(X)}{4\pi t}=\frac{\operatorname{Area}(X)}{4\pi t^2}$, and $\int_0 \frac{dt}{t^2}=+\infty$. **The total mass is infinite, and the divergence is a short-loop (small-$t$) effect.** This single observation is the seed of the entire paper: the total is infinite, but — as the [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|next section]] shows — the part concentrated on any fixed topological type of loop is finite, because winding around a hole forces the loop to be long, cutting off the small-$t$ divergence.

**From rooted to unrooted.** Two loops should count as the same if they trace the same oriented curve, regardless of basepoint or parametrisation. Formally identify $(t,\omega)$ with $(s,\tilde\omega)$ whenever an increasing continuous bijection between their parametrising circles carries one into the other — forgetting the root and the time-parametrisation but keeping the orientation. These identifications are generated by the circular time-shift $\mathrm{shift}_{s_0}(t,\omega)=(t,\omega(\cdot+s_0\bmod t))$ (slide the basepoint around the loop). The quotient space $C_X$ is the space of unrooted, unparametrised, oriented loops, and $\mu_X$ is $\mu^*_X$ pushed to that quotient.

**Two fundamental properties** (Lawler–Werner [LW04, §4]), used repeatedly downstream:

- **Restriction.** If $X'\subseteq X$ is an open subset, then $\mu_{X'}$ (the loop measure of the process killed on exiting $X'$) equals the restriction of $\mu_X$ to loops that stay inside $X'$: $d\mu_{X'}(\eta) = \mathbf 1_{\{\eta\subseteq X'\}}\,d\mu_X(\eta)$. Mechanism: the killed-on-exit process's bridge measures are the ambient ones cut to paths staying in $X'$.
- **Conformal invariance.** Replacing $g$ by any conformally equivalent metric $e^{2\sigma}g$ leaves $\mu_X$ unchanged, so $\mu_X$ depends only on the *conformal class* $[g]$: one may take $X$ to be a Riemann surface. This is special to two-dimensional Brownian motion — a subordinate (jump) process's operator depends on the metric itself, not the conformal class — which is why the paper works with $(X,g)$ a genuine Riemannian surface from §2.2 onward.

> [!recall]- Conformal class $[g]$ / conformally equivalent metrics
> **Formally:** two Riemannian metrics $g,\tilde g$ on $X$ are **conformally equivalent** if $\tilde g = e^{2\sigma} g$ for some smooth $\sigma:X\to\mathbb{R}$ (pointwise scalar rescaling of the inner product). The equivalence class $[g]$ is the **conformal class**, equivalently the structure of a **Riemann surface**.
> **In words:** a conformal change of metric stretches the surface pointwise without twisting or shearing — it keeps the angle between any two crossing curves the same but changes their lengths. In 2D, Brownian motion "sees" only angles (the shape of paths, not their speed), so the collection of loop-shapes with $\frac{dt}{t}$ weighting on their durations is unchanged.
> **Concretely:** on the flat plane, take $g = dx^2+dy^2$ and rescale by $\sigma(x,y) = \frac{1}{2}(x^2+y^2)$: the new metric $\tilde g = e^{x^2+y^2}(dx^2+dy^2)$ makes lengths grow super-fast far from the origin, but a right-angle intersection at any point stays a right angle. A Brownian path in $\tilde g$ traces the same *shape* on the page as in $g$ — just at a different clock speed — so its (duration-blind, $\frac{dt}{t}$-weighted) loop measure is unchanged. ⚠️ *Made rigorous by [LW04]; special to two dimensions.*

---

# Where the paper uses this

The Brownian loop measure is the paper's central object. It is the concrete model that motivates the general [[Def - Dirichlet Form Loop Measure|Dirichlet-form loop measure]] of §2.2 (Le Jan's abstraction), whose subordinate specialisation is [[Def - Subordinate Brownian Loop Measure|Definition 2.8]]. The observation that the total mass diverges only at small $t$ is exactly what [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] shows is cut off once loops are sorted by their [[Def - Fuchsian Group and the Hyperbolic Quotient Surface|topological type]]; the conformal invariance is what lets the paper work with a Riemann-surface structure in §2.1. Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.1]]; the Poisson point process built from $\mu_X$ is the *loop soup* of [[Def - Poisson Point Process and the Loop Soup|§4]].
