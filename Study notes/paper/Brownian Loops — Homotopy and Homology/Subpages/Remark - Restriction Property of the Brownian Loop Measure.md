---
type: remark
subject: probability-geometry
prereqs:
  - "Def - Brownian Loop Measure"
  - "Def - Riemannian Surface, Laplace-Beltrami Operator, and Volume Measure"
tags: [paper, brownian-loops, measure-theory]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §2.1 — restriction property (from [LW04, §4])"
---

# Notation

$(X,g)$ a complete orientable Riemannian surface, $X'\subseteq X$ an open subset. $\mathbb{W}^{t,X}_{x\to x}$ the Brownian bridge measure on $X$ from $x$ back to $x$ in time $t$, of mass $p_X(t,x,x)$; $\mathbb{W}^{t,X'}_{x\to x}$ the same for the sub-surface $X'$ with **Dirichlet boundary conditions** (Brownian motion is killed the first time it hits $\partial X'$), of mass $p_{X'}(t,x,x)$. $\mu_X$ and $\mu_{X'}$ the (unrooted) Brownian loop measures of [[Def - Brownian Loop Measure|Definition 2.1]] on $C_X$ and $C_{X'}$ respectively. $\eta\in C_X$ a loop, viewed as a subset of $X$ (the image $\eta([0,t_\eta])$ of its parametrising interval); $\mathbf 1_{\{\eta\subseteq X'\}}$ the indicator that the loop's image lies entirely in $X'$.

> [!recall]- Killed process on exit, Dirichlet boundary condition
> **Formally:** for an open $X'\subseteq X$, the Brownian motion on $X$ **killed on exit** from $X'$ is the process whose trajectory agrees with Brownian motion on $X$ until the first exit time $\tau_{X'}:=\inf\{t\ge 0:B_t\notin X'\}$ and is sent to a cemetery state $\dagger$ thereafter. Its transition density $p_{X'}(t,x,y)$ (for $x,y\in X'$) is the sub-probability density of "still alive and at $y$ at time $t$, having started at $x$"; equivalently, it is the heat kernel of $\Delta_X$ with **Dirichlet boundary conditions** on $\partial X'$ (the function vanishes on $\partial X'$). By construction $p_{X'}(t,x,y)\le p_X(t,x,y)$, with equality only in the limit $X'\uparrow X$.
> **In words:** allow the random walker to keep going unless and until it crosses out of $X'$; the moment it does, freeze its counter (delete it, count it as "killed"). The kernel $p_{X'}(t,x,y)$ integrates the mass of "still-alive" paths from $x$ to $y$ that stayed in $X'$ the whole time.
> **Concretely:** on $X=\mathbb{R}^2$ let $X'$ be the open unit disk $\{|x|<1\}$. Brownian motion in $\mathbb{R}^2$ killed at $\partial X'$ is planar Brownian motion frozen the first time it touches the unit circle. Its heat kernel $p_{X'}(t,x,y)$ is smaller than the plane's $p_{\mathbb{R}^2}(t,x,y)=\frac{1}{4\pi t}e^{-|x-y|^2/(4t)}$: for $x=y=0$ and small $t$ they agree ($p_{X'}(t,0,0)\approx\frac{1}{4\pi t}$, since the walker has not had time to reach $\partial X'$), but for large $t$ the ambient kernel decays like $1/t$ while $p_{X'}(t,0,0)$ decays exponentially at rate $\lambda_1(X')$, the smallest Dirichlet eigenvalue on the disk.

> [!recall]- Restriction of a measure to a subset
> **Formally:** for a measure $\mu$ on a measurable space $(\Omega,\mathcal F)$ and a measurable subset $A\in\mathcal F$, the **restriction** $\mu|_A$ (or $\mathbf 1_A\cdot\mu$) is the measure on $(\Omega,\mathcal F)$ defined by $(\mu|_A)(E)=\mu(E\cap A)$, or equivalently $d(\mu|_A)(\eta)=\mathbf 1_A(\eta)\,d\mu(\eta)$.
> **In words:** $\mu|_A$ keeps only the mass of $\mu$ that sits inside $A$ and forgets the rest. The mass outside $A$ becomes zero.
> **Concretely:** on $(\mathbb{R},\text{Lebesgue})$, the restriction to $A=[0,1]$ is the length measure on $[0,1]$: any set that meets $[0,1]$ in $E\cap[0,1]$ has restricted mass $|E\cap[0,1]|$. Here we restrict $\mu_X$ to $A=\{\eta\subseteq X'\}$, the (measurable) set of loops whose image is contained in $X'$.

---

# Claim / Identity

> **Claim (restriction, [LW04, §4]).** Let $(X,g)$ be a complete orientable Riemannian surface and $X'\subseteq X$ open. Then the Brownian loop measure $\mu_{X'}$ of the sub-surface $X'$ (constructed with Dirichlet boundary conditions on $\partial X'$) equals the ambient loop measure $\mu_X$ restricted to loops whose image is contained in $X'$:
> $$d\mu_{X'}(\eta) \;=\; \mathbf 1_{\{\eta\subseteq X'\}}\,d\mu_X(\eta),\qquad\eta\in C_X.$$
> Equivalently, for any non-negative measurable functional $F:C_X\to[0,\infty]$,
> $$\int F(\eta)\,d\mu_{X'}(\eta) \;=\; \int F(\eta)\,\mathbf 1_{\{\eta\subseteq X'\}}\,d\mu_X(\eta).$$

---

# In One Line

Cutting a subdomain out of $X$ and running Brownian motion killed at its boundary produces the same loops as taking the ambient loops and throwing away every loop that pokes outside the subdomain — the two constructions agree on the nose.

---

# Why It's True

**Mechanism (one sentence).** The bridge measure of Brownian motion killed on exit from $X'$ is, by construction, the ambient bridge measure supported on paths that stay inside $X'$; the loop measure is a $\frac{dt}{t}$- and $\operatorname{vol}_g$-weighted average of these bridges, and the same restriction identity survives the average.

The mental picture: think of Brownian paths as "ambient objects" that live on $X$ regardless of whether they respect $X'$. A path either stays inside $X'$ throughout its duration or exits at least once. Killed-on-exit dynamics simply *delete* the second kind (they are truncated at their exit time and never make it back to the basepoint to close into a loop). What is left — full loops that never crossed $\partial X'$ — is exactly what the ambient measure's indicator $\mathbf 1_{\{\eta\subseteq X'\}}$ selects. The identity is not a *theorem* about $\mu_{X'}$; it is a *definition-level compatibility* between the two constructions.

**Why it matters.** Downstream this identity is the technical device that lets the paper study loops inside a *fundamental domain* on the hyperbolic surface as loops of a Dirichlet-boundary-condition process there — no separate loop-measure theory required for the sub-surface. Equally, it is what allows [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] to reduce a class-mass computation on $X$ to an integral on a lifted strip in the universal cover: the strip's process is the ambient process restricted, so its loop measure is the ambient loop measure restricted.

---

# Derivation

> [!note]- Gap-free derivation of the restriction identity
> **Step 1 — identify the sub-surface bridge with the ambient bridge on stay-in-$X'$ paths.** By definition of the killed-on-exit process, its law $\mathbb{W}^{t,X'}_x$ on the path space $C([0,t],X')$ equals $\mathbb{W}^{t,X}_x$ (the ambient Wiener measure) restricted to the event $\{\omega([0,t])\subseteq X'\}$: a path is either killed by an excursion out of $X'$ (weight $0$ in the killed process) or it survives, in which case its weight in the killed process is exactly its weight in the ambient one. Disintegrating over the endpoint $\omega(t)=x$ preserves this identity, and for $x\in X'$
> $$\mathbb{W}^{t,X'}_{x\to x} \;=\; \mathbb{W}^{t,X}_{x\to x}\big|_{\{\omega([0,t])\subseteq X'\}}.$$
> Total masses on both sides give the standard sub-heat-kernel bound $p_{X'}(t,x,x)\le p_X(t,x,x)$, with the difference equal to the mass of loops that escape.
>
> **Step 2 — feed this into the loop-measure definition.** By [[Def - Brownian Loop Measure|Definition 2.1]], applied first on $X'$,
> $$\mu^*_{X'} \;=\; \int_0^\infty\frac{dt}{t}\int_{X'}\mathbb{W}^{t,X'}_{x\to x}\,d\operatorname{vol}_g(x) \;=\; \int_0^\infty\frac{dt}{t}\int_{X'}\mathbb{W}^{t,X}_{x\to x}\big|_{\{\omega\subseteq X'\}}\,d\operatorname{vol}_g(x)$$
> using Step 1. Since $\mathbb{W}^{t,X}_{x\to x}$ has zero mass on paths ending at $x\in X\setminus X'$ that also stay inside $X'$ (impossible: they would have to lie in $X'$ but end at a point outside), and $\mathbb{W}^{t,X}_{x\to x}$ for $x\in X'$ is precisely the ambient bridge from $x\in X'$, we may extend the inner integral to all of $X$ without changing the value:
> $$\mu^*_{X'} \;=\; \int_0^\infty\frac{dt}{t}\int_X \mathbf 1_{X'}(x)\,\mathbb{W}^{t,X}_{x\to x}\big|_{\{\omega\subseteq X'\}}\,d\operatorname{vol}_g(x).$$
> But the indicator $\mathbf 1_{X'}(x)$ is redundant: any path that stays in $X'$ starts at a point in $X'$, so the basepoint $x=\omega(0)\in X'$ is forced by the restriction $\{\omega\subseteq X'\}$. Hence
> $$\mu^*_{X'} \;=\; \int_0^\infty\frac{dt}{t}\int_X \mathbb{W}^{t,X}_{x\to x}\big|_{\{\omega\subseteq X'\}}\,d\operatorname{vol}_g(x) \;=\; \mathbf 1_{\{\omega\subseteq X'\}}\cdot\mu^*_X.$$
>
> **Step 3 — push forward to the unrooted quotient.** The condition $\{\omega\subseteq X'\}$ depends only on the loop's image, hence descends to the quotient $C_X=C^*_X/\!\sim$: for two rooted representatives $(t,\omega)\sim(s,\tilde\omega)$ of the same unrooted loop $\eta$, $\omega\subseteq X'$ iff $\tilde\omega\subseteq X'$ (they trace the same image up to reparametrisation). So $\mathbf 1_{\{\omega\subseteq X'\}}$ is the pullback of $\mathbf 1_{\{\eta\subseteq X'\}}$ under the quotient map, and the pushforward identity yields
> $$d\mu_{X'}(\eta) \;=\; \mathbf 1_{\{\eta\subseteq X'\}}\,d\mu_X(\eta),$$
> as claimed. The full proof (with the technical care needed for the equivalence of Dirichlet-boundary and killed-on-exit definitions, and for the joint measurability of $\mathbf 1_{\{\eta\subseteq X'\}}$ against $\mu_X$) is [LW04, §4]. $\qquad\blacksquare$

> [!cite]- External input — Lawler–Werner, "The Brownian loop soup"
> **Statement (used):** the restriction identity $d\mu_{X'}=\mathbf 1_{\{\eta\subseteq X'\}}d\mu_X$ for open $X'\subseteq X$.
> **Source:** G. F. Lawler and W. Werner, *The Brownian loop soup*, Probability Theory and Related Fields **128** (2004), 565–588, §4. The reference proves this for planar Brownian motion in the conformal-invariance setting; extension to general Riemannian surfaces is standard (see also [FOT11] for the Dirichlet-form-theoretic version and [LJ11, Ch. 2] for the fully abstract statement, which the paper's [[Def - Dirichlet Form Loop Measure|Definition 2.2]] restatement uses).

---

# Where the paper uses this

Introduced as a property of the Brownian loop measure in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.1]]. Extended verbatim to the [[Def - Dirichlet Form Loop Measure|Dirichlet-form loop measure]] in §2.2 and to the [[Def - Subordinate Brownian Loop Measure|subordinate loop measure]] in §2.4 (both inherit it because the killed-form / part-form construction preserves it). Used implicitly whenever the paper cuts a loop-measure computation to a sub-domain — most conspicuously in [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]]'s reduction of a class-mass to an integral over a fundamental strip in the universal cover.
