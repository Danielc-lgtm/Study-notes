---
type: remark
subject: probability-geometry
prereqs:
  - "Def - Brownian Loop Measure"
  - "Def - Dirichlet Form Loop Measure"
  - "Def - Signed and Infinite Measures for Loop Measures"
tags: [paper, brownian-loops, measure-theory]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "unnumbered; §2.1–§2.2 — invariance of the rooted loop measure under the circular time-shift, and well-definedness of the pushforward to unrooted loops"
---

# Notation

$(X,g)$ a Riemannian surface. $C^*_X=\{(t,\omega):t\ge 0,\ \omega:[0,t]\to X\text{ continuous or càdlàg},\ \omega(0)=\omega(t)\}$ the space of parametrised rooted loops (with continuous $\omega$ in §2.1, càdlàg $\omega$ in §2.2). For $t>0$ and $s_0\in[0,t)$, the **circular time-shift** is the map
$$\mathrm{shift}_{s_0}:C^*_X\to C^*_X,\qquad \mathrm{shift}_{s_0}(t,\omega)\;=\;(t,\omega_{s_0}),\qquad \omega_{s_0}(r):=\omega(r+s_0\bmod t);$$
that is, keep the duration $t$, shift the basepoint by $s_0$ around the circle $[0,t]/{0\sim t}$. The equivalence relation $\sim$ on $C^*_X$ identifying two rooted loops iff they are related by such a shift (and an orientation-preserving reparametrisation) is what defines the quotient $C_X:=C^*_X/\!\sim$ of unrooted, unparametrised, oriented loops. $\mu^{*,E}_X$ the rooted loop measure of a Dirichlet form $(\mathcal E,\mathcal F)$ ([[Def - Dirichlet Form Loop Measure|Definition 2.2]]); $\mu^E_X$ its pushforward to $C_X$.

> [!recall]- Pushforward of a measure under a map $f$
> **Formally:** if $f:(\Omega_1,\mathcal F_1,\mu)\to(\Omega_2,\mathcal F_2)$ is a measurable map, the **pushforward** $f_*\mu$ (also written $\mu\circ f^{-1}$) is the measure on $(\Omega_2,\mathcal F_2)$ defined by $(f_*\mu)(A):=\mu(f^{-1}(A))$ for $A\in\mathcal F_2$. Its defining property: $\int g\,d(f_*\mu)=\int g\circ f\,d\mu$ for every non-negative measurable $g$ on $\Omega_2$.
> **In words:** relabel each point $x\in\Omega_1$ as $f(x)\in\Omega_2$ and move its $\mu$-mass over there — $f_*\mu$ is what you get. If $f$ collapses two points to one, their masses add.
> **Concretely:** on $(\mathbb{R},\text{Lebesgue})$, the pushforward under $x\mapsto x^2$ sends the Lebesgue-mass of $\mathbb{R}$ to a measure on $[0,\infty)$; on a symmetric set $[-a,a]$, the pushforward puts $2\,da$-mass on $a^2$-th values. For loops: the pushforward of $\mu^{*,E}_X$ under the quotient map $\pi:C^*_X\to C_X$ sends the mass of each rooted representative $(t,\omega)$ to its equivalence class $[\omega]\in C_X$. For $\mu^E_X:=\pi_*\mu^{*,E}_X$ to be well-defined and to have the "natural" meaning, the rooted measure must give the same mass to every representative of a given class — that is what circular time-shift invariance secures.

> [!recall]- Quotient space and well-defined descent of a measure
> **Formally:** given an equivalence relation $\sim$ on $(\Omega,\mathcal F)$, the quotient $\Omega/\!\sim$ carries the $\sigma$-algebra $\mathcal F/\!\sim:=\{A\subseteq\Omega/\!\sim\ :\ \pi^{-1}(A)\in\mathcal F\}$ (where $\pi:\Omega\to\Omega/\!\sim$ is the quotient map). A measure $\mu$ on $(\Omega,\mathcal F)$ **descends** to a measure $\bar\mu$ on the quotient iff $\mu$ is invariant under the group of transformations generating $\sim$ (equivalently, iff for every equivalence class $C$, all representatives of $C$ carry the same $\mu$-mass in a certain measure-theoretic sense).
> **In words:** to define a measure on unrooted loops from one on rooted loops, the rooted measure must not distinguish between different rootings of the same unrooted loop. If it did, the pushforward would depend on which representative you happened to pick, and would not be well-defined.
> **Concretely:** on $\mathbb{R}$ with the translation equivalence $x\sim x+n$ ($n\in\mathbb{Z}$), the Lebesgue measure descends to the standard Lebesgue measure on the circle $\mathbb{R}/\mathbb{Z}$ *because* Lebesgue is translation-invariant. If instead one used the measure $e^{-x^2}dx$ on $\mathbb{R}$, it would *not* descend cleanly — different rootings of a "point on the circle" carry different masses, and the naïve pushforward would double-count (indeed, its value on any set would be $+\infty$). For loops: the rooted-loop measure $\mu^{*,E}_X$ must not care about where the basepoint sits along the loop, else the mass of an unrooted loop is ill-defined.

> [!recall]- Fubini–Tonelli theorem (invariance-under-integrand-shift, used in the proof)
> **Formally:** if $(\Omega,\mu)$ is $\sigma$-finite and $F:\Omega\times[0,t]\to[0,\infty]$ is jointly measurable and non-negative, then $\int_\Omega\int_0^t F(x,s)\,ds\,d\mu(x)=\int_0^t\int_\Omega F(x,s)\,d\mu(x)\,ds$ (Tonelli). Combined with translation-invariance of Lebesgue on $[0,t]$ modulo $t$ (i.e. of the uniform measure $\frac{ds}{t}$ on the circle), this justifies swapping a "sum over rooted representatives" with an "average over the basepoint circle".
> **In words:** for non-negative integrands you can freely swap the order of integration; combined with translation-invariance of the uniform measure on a circle, you can average a rooted-loop functional over its basepoint circle and get the same answer as summing over rooted representatives.
> **Concretely:** used in Step 2 of the derivation below, where the invariance of $\mu^{*,E}_X$ under $\mathrm{shift}_{s_0}$ (for every $s_0\in[0,t)$) follows from the fact that the loop-measure integrand $\int_X\mathbb{W}^{t,E}_{x\to x}\,d\operatorname{vol}_g(x)$ is a *symmetric* sum over all possible basepoints of the loop — hence unaffected by rotating the parametrisation.

---

# Claim / Identity

> **Claim (circular time-shift invariance and well-defined descent).** For every regular symmetric Dirichlet form $(\mathcal E,\mathcal F)$ on $L^2(X,\operatorname{vol}_g)$ with transition density $p^E$, the rooted loop measure $\mu^{*,E}_X$ of [[Def - Dirichlet Form Loop Measure|Definition 2.2]] is invariant under the circular time-shift: for every $s_0\ge 0$,
> $$(\mathrm{shift}_{s_0})_*\,\mu^{*,E}_X \;=\; \mu^{*,E}_X.$$
> Consequently, the pushforward $\mu^E_X:=\pi_*\mu^{*,E}_X$ under the quotient map $\pi:C^*_X\to C_X=C^*_X/\!\sim$ is well-defined (independent of the choice of rooted representative in each equivalence class), and $\mu^E_X$ is the paper's **Dirichlet-form loop measure** on unrooted, unparametrised, oriented loops. The same statement applies in particular to the Brownian case of [[Def - Brownian Loop Measure|Definition 2.1]] and to the subordinate case of [[Def - Subordinate Brownian Loop Measure|Definition 2.8]], since both are instances of Definition 2.2.

---

# In One Line

The rooted loop measure gives the same mass to every rooting of a given loop, so the natural way to forget the basepoint (push forward under the quotient) produces a well-defined measure on unrooted loops — without this, the unrooted loop measure would either double-count or depend on an arbitrary choice.

---

# Why It's True

**Mechanism (one sentence).** The rooted-loop formula $\int_0^\infty\frac{dt}{t}\int_X\mathbb{W}^{t,E}_{x\to x}\,d\operatorname{vol}_g(x)$ averages the bridge measure $\mathbb{W}^{t,E}_{x\to x}$ over *all* basepoints $x\in X$ against $\operatorname{vol}_g$; the average is symmetric in the choice of "starting point", and shifting the basepoint of a loop around its own parametrising circle is just relabelling which of the loop's own points is called "the start" — this relabelling permutes the basepoints being averaged over, but leaves the average unchanged.

**The mental picture.** A rooted loop is a *pointed circle* — a circular curve on $X$ together with a marked "start" position on it. Sliding the start position around the circle produces new rooted loops with the same underlying image; there are as many rooted representatives of a given unrooted loop as there are points on the circle (a continuous family, parametrised by $[0,t]/{0\sim t}$). If the rooted measure were biased toward one rooting over another, the naïve pushforward would either overcount (if it summed the masses of all rooted representatives) or make an arbitrary choice (if it picked one). The invariance says these masses are all equal, so there is no ambiguity.

**Where the invariance comes from.** The bridge measure $\mathbb{W}^{t,E}_{x\to x}$ from $x$ to itself is *symmetric* in the process — the transition density $p^E(t,x,x)$ is invariant under time-reversal, and a closed loop's "starting point" is a purely bookkeeping choice from the process's viewpoint. Averaging over all $x\in X$ against the symmetric reference measure $\operatorname{vol}_g$ makes the rooted-loop density on $C^*_X$ symmetric under the circular action. Le Jan [LJ11, Ch. 2] verifies this in the abstract Dirichlet-form setting; the same argument (with continuous instead of càdlàg paths) handles the Brownian case.

---

# Derivation

> [!note]- Gap-free derivation of the circular time-shift invariance
> **Step 1 — restate what needs to be shown.** For each fixed $s_0\ge 0$, and each non-negative measurable functional $F:C^*_X\to[0,\infty]$, we need
> $$\int F(t,\omega_{s_0})\,d\mu^{*,E}_X(t,\omega) \;=\; \int F(t,\omega)\,d\mu^{*,E}_X(t,\omega),$$
> where $\omega_{s_0}(r)=\omega(r+s_0\bmod t)$ is the rotated parametrisation. This is the definitional equivalent of $(\mathrm{shift}_{s_0})_*\mu^{*,E}_X=\mu^{*,E}_X$.
>
> **Step 2 — write out the loop-measure integral against $F(t,\omega_{s_0})$.** By [[Def - Dirichlet Form Loop Measure|Definition 2.2]],
> $$\int F(t,\omega_{s_0})\,d\mu^{*,E}_X(t,\omega) \;=\; \int_0^\infty\frac{dt}{t}\int_X\bigl(\int F(t,\omega_{s_0})\,d\mathbb{W}^{t,E}_{x\to x}(\omega)\bigr)\,d\operatorname{vol}_g(x).$$
> (The outer $\frac{dt}{t}$-integral commutes with any pointwise operation on $\omega$; the inner $\operatorname{vol}_g$-integral aggregates over basepoints.)
>
> **Step 3 — relate the shifted bridge to a re-rooted bridge.** For a Brownian-like or Dirichlet-form-associated process, the "loop-from-$x$-to-$x$" bridge, viewed as a random circular path, is the *same object* regardless of which of its own points is called "the start"; formally, for the bridge from $x$ to itself, the shift $\omega\mapsto\omega_{s_0}$ produces a bridge from $\omega(s_0\bmod t)$ to itself (the walker at time $t-s_0$ becomes the "new start", and by circularity ends up at the same point $t$ later). The precise identity, in the symmetric-bridge framework of [FOT11]/[LJ11], is
> $$\int F(t,\omega_{s_0})\,d\mathbb{W}^{t,E}_{x\to x}(\omega) \;=\; \int F(t,\omega)\,d\mathbb{W}^{t,E}_{\omega(s_0)\to\omega(s_0)}(\omega),$$
> where the right-hand side integrates the *unshifted* functional against the bridge from the *shifted* basepoint $\omega(s_0)$. (Making this precise is the substance of [LJ11, Ch. 2]'s treatment of the loop measure for symmetric Markov processes; the key input is that $p^E$ is symmetric, so the bridge law from $x$ to $x$ can be reversed and cut without changing its distribution.)
>
> **Step 4 — average over the basepoint.** Substituting Step 3 into Step 2,
> $$\int F(t,\omega_{s_0})\,d\mu^{*,E}_X \;=\; \int_0^\infty\frac{dt}{t}\int_X\bigl(\int F(t,\omega)\,d\mathbb{W}^{t,E}_{\omega(s_0)\to\omega(s_0)}(\omega)\bigr)\,d\operatorname{vol}_g(x).$$
> The inner integrand is now a functional of the *new* basepoint $y:=\omega(s_0)$ rather than the old one $x$. But the outer average over $x\in X$ against the symmetric $\operatorname{vol}_g$ is *insensitive* to which point of the loop we call the basepoint — pulling $y$ out and re-averaging against $\operatorname{vol}_g$ gives the same value. Concretely: fixing $\omega$ and letting $y=\omega(s_0)$, the map $x\mapsto y$ (for $x$ ranging over $X$ against $\operatorname{vol}_g$) is a measurable rearrangement that preserves $\operatorname{vol}_g$-mass on the set of loops that pass through $y$ at time $s_0$, so integrating over $x$ or over $y$ gives the same value. Formally, this is a Tonelli-plus-symmetry argument for the joint measure $\mathbb{W}^{t,E}_{x\to x}(\omega)\,d\operatorname{vol}_g(x)$ on the enlarged space $(x,\omega)$ — see [LJ11, Ch. 2, Prop. 2.1] for the detailed accounting.
>
> **Step 5 — conclude.** After the change of averaging variable in Step 4, the right-hand side becomes
> $$\int_0^\infty\frac{dt}{t}\int_X\bigl(\int F(t,\omega)\,d\mathbb{W}^{t,E}_{y\to y}(\omega)\bigr)\,d\operatorname{vol}_g(y) \;=\; \int F\,d\mu^{*,E}_X.$$
> Thus $(\mathrm{shift}_{s_0})_*\mu^{*,E}_X=\mu^{*,E}_X$ for every $s_0$, establishing the invariance.
>
> **Step 6 — descent to the unrooted quotient.** Since $\mu^{*,E}_X$ is invariant under the group generated by the circular shifts (and, on the càdlàg space, under orientation-preserving reparametrisations, which are handled by an analogous argument), it descends to a measure $\mu^E_X$ on the quotient $C_X=C^*_X/\!\sim$. The pushforward $\pi_*\mu^{*,E}_X$ is well-defined and equals $\mu^E_X$. $\qquad\blacksquare$
>
> *(Le Jan's [LJ11, Ch. 2] gives the argument in the general symmetric-Dirichlet-form setting; the Brownian case is a special instance.)*

> [!cite]- External input — Le Jan, "Markov paths, loops and fields"
> **Statement (used):** invariance of the parametrised loop measure under the circular time-shift (and orientation-preserving reparametrisations), hence well-definedness of the pushforward to the unrooted loop space.
> **Source:** Y. Le Jan, *Markov paths, loops and fields*, Lecture Notes in Mathematics **2026**, Springer 2011, Chapter 2 (in particular Proposition 2.1). The invariance is shown there for the general regular-symmetric-Dirichlet-form loop measure; the Brownian case ([LW04, §4]) is a special case that appeared first in the continuous, planar setting.

---

# Where the paper uses this

Stated as a property of $\mu^*_X$ in [[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2.1]] (Brownian case) and again for $\mu^{*,E}_X$ in the same section (Dirichlet-form case, [[Def - Dirichlet Form Loop Measure|Definition 2.2]]). Its role is *structural*: without it, the unrooted loop measure $\mu^E_X$ on $C_X$ — the paper's actual object of interest — would not be well-defined. Every downstream computation is in $\mu^E_X$ (or its subordinate variant $\mu^\phi_X$), so every downstream computation depends on this invariance. In particular, [[Thm - Mass of a Free Homotopy Class|Theorem 3.2]]'s per-conjugacy-class mass formula treats unrooted loops as its unit, and would be meaningless if the notion of an "unrooted loop mass" were ambiguous.
