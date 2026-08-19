---
type: definition
subject: probability-geometry
prereqs:
  - "Def - Dirichlet Form and its Operator and Semigroup"
  - "Def - Brownian Loop Measure"
  - "Def - Disintegration and the Bridge Measure"
  - "Def - Signed and Infinite Measures for Loop Measures"
tags: [paper, brownian-loops, dirichlet-forms]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Definition 2.2"
---

# Notation

$(X,g)$ a Riemannian surface with area measure $\operatorname{vol}_g$; $L^2(X,\operatorname{vol}_g)$ the Hilbert space of square-integrable functions. $(\mathcal E,\mathcal F)$ a regular symmetric Dirichlet form on $L^2(X,\operatorname{vol}_g)$ with self-adjoint operator $A$, semigroup $e^{-tA}$, and (assumed jointly measurable and symmetric) transition density $p^E:(0,\infty)\times X\times X\to(0,\infty)$. $\mathbb{W}^{t,E}_x$ the law of the process starting at $x$, running for time $t$; $\mathbb{W}^{t,E}_{x\to y}$ its unnormalised bridge measure with mass $|\mathbb{W}^{t,E}_{x\to y}|=p^E(t,x,y)$.

The **rooted càdlàg loop space** is $C^*_X = \{(t,\omega):t\ge 0,\ \omega\in D([0,t],X),\ \omega(0)=\omega(t)\}$, where $D([0,t],X)$ is the space of càdlàg paths (see the recall below) — the same shape as before but now allowing the jumps a general symmetric Markov process may have. $C_X$ is its quotient by the circular time-shift.

> [!recall]- Regular symmetric Dirichlet form $(\mathcal E,\mathcal F)$ and its data $(A,e^{-tA},p^E)$
> **Formally:** on $L^2(X,\operatorname{vol}_g)$, a **regular symmetric Dirichlet form** is a symmetric non-negative bilinear form $\mathcal E:\mathcal F\times\mathcal F\to\mathbb{R}$ on a dense linear subspace $\mathcal F\subseteq L^2$, closed (i.e. $\mathcal F$ is a Hilbert space under $\|u\|_{\mathcal E}^2 := \mathcal E(u,u)+\|u\|^2_{L^2}$) and Markovian (composing $u\in\mathcal F$ with the clip $u^\#=(0\vee u)\wedge 1$ still gives an element of $\mathcal F$ with $\mathcal E(u^\#,u^\#)\le\mathcal E(u,u)$). It uniquely determines a non-negative self-adjoint operator $A$ on $L^2$ with $\mathcal F=\operatorname{Dom}(A^{1/2})$, $\mathcal E(u,v)=\langle A^{1/2}u,A^{1/2}v\rangle$; a strongly continuous semigroup $e^{-tA}$; a symmetric transition density $p^E$ (when it exists) with $(e^{-tA}f)(x)=\int_X p^E(t,x,y)f(y)\,d\operatorname{vol}_g(y)$; and (Fukushima's theorem) a symmetric Markov (Hunt) process on $X$.
> **In words:** a Dirichlet form assigns an "energy" to each function on $X$ — flat functions cost less energy than wiggly ones. Once you have such an energy, a general machine (Fukushima's theorem) automatically produces a Markov random-walk process whose typical paths dissipate that energy. Different energy choices give different processes: the Dirichlet energy $\int|\nabla u|^2$ gives ordinary Brownian motion; $\int|\nabla u|^2 + \kappa\int u^2$ gives Brownian motion killed at rate $\kappa$; a non-local energy involving jumps gives a jump process.
> **Concretely:** on $X=\mathbb{R}$ take $\mathcal F=H^1(\mathbb{R})$ (functions with one square-integrable derivative) and $\mathcal E(u,v)=\int u'v'\,dx$ — the Dirichlet energy. Its self-adjoint operator is $A=-\frac{d^2}{dx^2}$ (the Laplacian on the line), its heat kernel is the Gaussian $p^E(t,x,y)=\frac{1}{\sqrt{4\pi t}}e^{-(x-y)^2/4t}$, and its process is standard Brownian motion on $\mathbb{R}$. Change $\mathcal E$ to $\int u'v'\,dx + \int uv\,dx$ (add a mass term) and you get Brownian motion killed at unit rate: the process still moves as Brownian motion, but at each moment has probability $e^{-t}$ of surviving to time $t$. See [[Def - Dirichlet Form and its Operator and Semigroup]].

> [!recall]- Càdlàg path
> **Formally:** a path $\omega:[0,t]\to X$ is **càdlàg** (French: *continue à droite, limite à gauche*) if for every $r\in[0,t)$ the right-limit $\lim_{s\downarrow r}\omega(s)$ exists and equals $\omega(r)$, and for every $r\in(0,t]$ the left-limit $\omega(r^-):=\lim_{s\uparrow r}\omega(s)$ exists (but need not equal $\omega(r)$). $D([0,t],X)$ denotes the space of such paths; it contains $C([0,t],X)$ as a subspace.
> **In words:** a path that may jump, but only cleanly — at every jump the path's value equals the right side, and a well-defined left limit still exists. No wild oscillations, no double-valued instants.
> **Concretely:** the step function $\omega(s)=\mathbf 1_{[1/2,1]}(s)$ on $[0,1]$ is càdlàg: at $s=1/2$ it jumps from $0$ to $1$, and by the right-continuity convention takes the right value $\omega(1/2)=1$; the left limit $\omega(1/2^-)=0$ exists too. Continuous paths (diffusions like Brownian motion) are càdlàg with no jumps at all — a special case. Pure-jump processes (like a Poisson process, or an $\alpha$-stable process) are càdlàg with countably many jumps.

> [!recall]- Bridge measure $\mathbb{W}^{t,E}_{x\to y}$ (endpoint-disintegration of the process's law)
> **Formally:** disintegrating $\mathbb{W}^{t,E}_x$ over the endpoint map $\omega\mapsto\omega(t)$ yields $\{\mathbb{W}^{t,E}_{x\to y}\}_{y\in X}$ on $D([0,t],X)$, with $\mathbb{W}^{t,E}_x=\int_X\mathbb{W}^{t,E}_{x\to y}\,d\operatorname{vol}_g(y)$ and $|\mathbb{W}^{t,E}_{x\to y}|=p^E(t,x,y)$; $\mathbb{W}^{t,E}_{x\to y}/p^E(t,x,y)$ is the probability law of the process conditioned on $\omega(t)=y$.
> **In words:** exactly as with Brownian motion: the process's law from $x$ splits into "how likely it is to end at $y$" (density $p^E(t,x,y)$) times "the conditional path given it ends at $y$". Setting $y=x$ picks out loops.
> **Concretely:** on $X=\mathbb{R}$ with $p^E$ the Gaussian, $\mathbb{W}^{t,E}_{0\to 0}$ is the classical Brownian bridge scaled by $p^E(t,0,0)=1/\sqrt{4\pi t}$; a sample is a random continuous loop of duration $t$ pinned at $0$. For a killed process with density $e^{-\kappa t}$ times the Gaussian, the bridge mass shrinks by $e^{-\kappa t}$: fewer paths survive long enough to make it back. See [[Def - Disintegration and the Bridge Measure]].

> [!recall]- The multiplicative Haar measure $\frac{dt}{t}$ on $(0,\infty)$
> **Formally:** $\frac{dt}{t}$ is the $\sigma$-finite Borel measure on $(0,\infty)$ invariant under $t\mapsto\lambda t$ for every $\lambda>0$; infinite total mass but finite on each interval bounded away from $0$ and $\infty$.
> **In words:** the unique (up to a constant) "duration-blind" weight on positive reals — doubling every duration leaves total weight unchanged.
> **Concretely:** the substitution $u=\log t$ turns $\int_a^b f(t)\,\frac{dt}{t}$ into $\int_{\log a}^{\log b}f(e^u)\,du$, ordinary Lebesgue integration in the log-time coordinate. So $\int_1^{e^n}\frac{dt}{t}=n$: each factor of $e$ in duration contributes one unit of mass. See [[Def - Signed and Infinite Measures for Loop Measures]].

---

# Statement

> **Definition (Dirichlet-form loop measure; Belyaev–Huseynli Def. 2.2).** Let $(\mathcal E,\mathcal F)$ be a regular symmetric Dirichlet form on $L^2(X,\operatorname{vol}_g)$ whose semigroup $e^{-tA}$ admits a jointly measurable symmetric transition density $p^E$. The **rooted parametrised loop measure** on the càdlàg rooted loop space $C^*_X$ is the $\sigma$-finite measure
> $$\mu^{*,E}_X \;:=\; \int_0^\infty\frac{dt}{t}\int_X \mathbb{W}^{t,E}_{x\to x}\,d\operatorname{vol}_g(x),$$
> invariant under the circular time-shift [LJ11, Ch. 2]; its pushforward to the unrooted, unparametrised, oriented loop space $C_X$ is the **Dirichlet-form loop measure** $\mu^E_X$. Its total mass is $\int_0^\infty\frac{1}{t}\int_X p^E(t,x,x)\,d\operatorname{vol}_g(x)\,dt$. The **restriction property** holds: for an open $X'\subseteq X$ the process's part-form $(\mathcal E_{X'},\mathcal F_{X'})$ (killed on leaving $X'$) has bridge measures equal to the ambient ones restricted to paths staying in $X'$, hence $\mu^{E_{X'}}_{X'}$ is $\mu^E_X$ restricted to loops in $X'$.

---

# In One Line

The [[Def - Brownian Loop Measure|Brownian loop measure]] construction with Brownian motion replaced by *any* symmetric Markov process coming from a Dirichlet form — Le Jan's abstraction, which is exactly what lets the paper feed killed and $\alpha$-stable jump processes into the same formulas.

---

# Motivation and Unpacking

**Why abstract.** In §2.1 every step of the loop-measure construction used *nothing about Brownian motion in particular*: only that there was a symmetric transition density $p(t,x,y)$ with bridge measures $\mathbb{W}^t_{x\to y}$ of mass $p(t,x,y)$. Any process with these ingredients would work. The **regular symmetric Dirichlet forms** on $L^2(X,\operatorname{vol}_g)$ are exactly the "energy functionals" that produce a self-adjoint operator $A$ with a semigroup $e^{-tA}$ and a symmetric transition density $p^E$; by Fukushima's Dirichlet-form–Hunt-process correspondence, they also produce a genuine random process (with càdlàg paths — jumps allowed) whose law matches $p^E$. This is Le Jan's viewpoint [LJ11]: the whole construction lifts verbatim to $(\mathcal E,\mathcal F)$. The payoff is §2.3, where **subordination** — running the process on a random clock — will hand us a large family of new Dirichlet forms (killed Brownian motion, $\alpha$-stable jump processes, gamma, relativistic-stable, …) all at once, each of which produces its own loop measure by the same formula.

**Unpacking the formula.** The mechanics are exactly as in [[Def - Brownian Loop Measure|Definition 2.1]], with continuous paths replaced by càdlàg ones: pick a duration $t>0$ according to the scale-invariant weight $\frac{dt}{t}$, pick a basepoint $x\in X$ according to $\operatorname{vol}_g$, and place the (unnormalised) bridge $\mathbb{W}^{t,E}_{x\to x}$ of mass $p^E(t,x,x)$ from $x$ back to itself. Integrating out the parametrisation and root by pushforward gives $\mu^E_X$ on $C_X$. The circular time-shift invariance means the formula does not depend on where you chose to "start" the loop — reasonable, since the physical object is an oriented curve, not a parametrised path.

**Total mass and where it diverges.** By the same computation as in §2.1,
$$|\mu^{*,E}_X| \;=\; \int_0^\infty\frac{dt}{t}\int_X p^E(t,x,x)\,d\operatorname{vol}_g(x),$$
and if the short-time on-diagonal asymptotics of $p^E$ are of order $t^{-d/2}$ (as they are for Brownian motion on a $d$-manifold, and — after suitable rescaling — for the [[Def - Subordinate Brownian Loop Measure|subordinate]] cases) then the $t\to 0$ divergence persists. The paper's finiteness results (§3, §5) will always be *per topological class* or *after renormalisation*.

**Restriction (recorded).** Killing the process on exit from $X'$ replaces $(\mathcal E,\mathcal F)$ by its "part on $X'$", $(\mathcal E_{X'},\mathcal F_{X'}):=\{u\in\mathcal F:u=0\ \text{q.e. on}\ X\setminus X'\}$; its transition density is $p^E$ restricted to paths staying in $X'$; its bridge measures are the ambient ones restricted to paths in $X'$. So $\mu^{E_{X'}}_{X'}$ is $\mathbf 1_{\{\eta\subseteq X'\}}\mu^E_X$ — the same restriction identity as the Brownian case.

**Circular time-shift invariance.** The rooted loop measure is invariant under $\mathrm{shift}_{s_0}(t,\omega)=(t,\omega(\cdot+s_0\bmod t))$: sliding the basepoint around a loop keeps the loop's "amount" the same, which is why the pushforward to unrooted loops is well-defined. Le Jan proves this for symmetric Dirichlet forms in [LJ11, Ch. 2].

**The point.** Every downstream loop-measure computation — for killed Brownian motion, for $\alpha$-stable processes, for the [[Def - Subordinate Brownian Loop Measure|subordinate]] setting in general — is *this* construction applied to a specific $(\mathcal E,\mathcal F)$, so the formulas of §2.1 (bridge mass = heat kernel, total mass = double integral, restriction) transfer without change. That is what buys the paper its uniformity.

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.2]]. Immediately specialised in [[Def - Subordinate Brownian Loop Measure|Definition 2.8]] to $(\mathcal E^\phi,\mathcal F^\phi)$, the [[Def - Bernstein Function, Subordinator, and Subordination|subordinate]] Dirichlet form for a Bernstein function $\phi$. Used implicitly throughout §3–§6 wherever a general "loop measure" is invoked: every mass computation ([[Thm - Mass of a Free Homotopy Class|Theorem 3.2]] and its downstream corollaries) is a mass in $\mu^E_X$ for some choice of $(\mathcal E,\mathcal F)$.
