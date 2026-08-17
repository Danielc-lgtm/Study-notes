---
type: paper-section
paper: "BH26"
subject: brownian-loops
section: "4"
tags: [paper, section, zeta-functions, self-contained]
---

> [!info] Part of [[Map - Brownian Loops on Homotopy and Homology Classes]]. Self-contained: every symbol, predicate and imported result used below is written out on this page. Grey callouts are folds on THIS page — opening one is a scroll, not a jump to another file. You can typecheck §4 front-to-back without opening anything else.

**What §4 buys you.** §3 gave one number per free-homotopy class. §4 adds them up over all classes and recognises the sum as $-\log Z_X(s)$ for the Selberg zeta function — turning "is the total loop mass a spectral quantity?" into a one-variable functional equation (the *Selberg zeta criterion*), verifying it for the four processes of the paper, and settling exactly when the sum is finite (so §6's probability measure exists).

# A. Standing setup

Everything in §4 lives on a fixed hyperbolic surface $X$ and concerns the masses a fixed loop measure assigns to its free-homotopy classes. The three paragraphs below fix those objects, inlined so that dropping straight into §4 needs nothing from earlier sections.

**The surface.** $\Gamma\subseteq\mathrm{PSL}(2,\mathbb R)$ is a discrete, torsion-free group of isometries of the hyperbolic plane $\mathbb H^2$ (upper half-plane, metric $|dz|/\operatorname{Im}z$), acting **freely** — $\forall h\in\Gamma\setminus\{1\}\ \forall z\in\mathbb H^2:\ hz\neq z$ (no non-identity isometry fixes a point) — and **properly discontinuously** — $\forall K\Subset\mathbb H^2:\ \#\{h\in\Gamma:\ hK\cap K\neq\varnothing\}<\infty$ (each compact set meets only finitely many of its $\Gamma$-translates). Under exactly these two conditions the quotient $X=\Gamma\backslash\mathbb H^2$ (points of $\mathbb H^2$ glued when one is a $\Gamma$-image of the other) is a smooth hyperbolic surface and $\pi:\mathbb H^2\to X$ is a **covering map** (a local isometry under which $\mathbb H^2$ wraps around $X$) with **deck group** $\Gamma$ (the isometries permuting the sheets over each point), $\Gamma\cong\pi_1(X)$. We take $X$ **geometrically finite** — $\Gamma$ finitely generated, equivalently $X$ has a finite-sided fundamental polygon; the only consequence used in §4 is that the length spectrum is locally finite, $\#\{\gamma:\ell_\gamma\le R\}<\infty$ for every $R$.

**Geodesics and their classes.** A closed geodesic $\gamma$ is **primitive** if it is not a repeated traversal of a shorter one — on the group side its representative $\tau\in\Gamma$ satisfies $\tau=\sigma^k\ (\sigma\in\Gamma,\,k\ge1)\Rightarrow k=1$. Write $\mathcal P_X$ for the primitive oriented closed geodesics and $\ell_\gamma:=\min_z d(z,\tau z)>0$ for the length of $\gamma$ (the **translation length** of $\tau$). Every closed geodesic is the $m$-fold iterate $\gamma^m$ of a unique primitive $\gamma$, of length $L:=m\ell_\gamma$. Two oriented closed curves are **freely homotopic** if one deforms into the other through closed curves with **no basepoint fixed** ($\exists$ continuous $H:S^1\times[0,1]\to X$ between them); the free-homotopy classes of loops on $X$ correspond bijectively to conjugacy classes $[h]=\{qhq^{-1}:q\in\Gamma\}$ in $\Gamma$, and — restricting to **non-trivial, non-peripheral** classes — to pairs $(\gamma,m)\in\mathcal P_X\times\mathbb Z_{\ge1}$: write $\mathcal C_X(\gamma^m)$ for the class winding $m$ times around $\gamma$, i.e. the conjugacy class $[\tau^m]$. **The only geometric input to every mass below is the single positive number $L=m\ell_\gamma$.**

**The loop measure.** $\mathcal C_X$ is the space of unrooted, unparametrised, oriented loops on $X$ (a loop as a stochastic process produces it, stripped of its start-point and its clock). $\mu^\phi_X$ is the $\phi$-subordinate Brownian **loop measure** on $\mathcal C_X$: a $\sigma$-finite measure of **infinite** total mass, $\mu^\phi_X(\mathcal C_X)=\infty$, built from Brownian motion time-changed by the random clock $\phi$ (recall below). What §4 consumes from it is one number per class, the class mass $\mu^\phi_X(\mathcal C_X(\gamma^m))\in(0,\infty)$, computed in §3 (Theorem 3.5, imported in §4.2).

**Notation for §4.**

| symbol | type |
|---|---|
| $X=\Gamma\backslash\mathbb H^2$ | geometrically finite hyperbolic surface |
| $\mathcal P_X$ | primitive oriented closed geodesics $\gamma$; $\ell_\gamma\in(0,\infty)$ their lengths |
| $m,\,L$ | $m\in\mathbb Z_{\ge1}$; $L:=m\ell_\gamma\in(0,\infty)$ |
| $\mathcal C_X(\gamma^m)$ | free-homotopy class of $\gamma^m$ $=$ conjugacy class $[\tau^m]$; a measurable set of loops |
| $\mu^\phi_X$ | $\sigma$-finite measure on $\mathcal C_X$, total mass $\infty$; class mass $\mu^\phi_X(\mathcal C_X(\gamma^m))\in(0,\infty)$ |
| $\phi,\ I_\phi,\ V_\phi$ | a Bernstein function; its heat-kernel integral $(0,\infty)\to(0,\infty)$; its potential measure on $(0,\infty)$ (recalls below) |
| $s$ | spectral parameter; $s\in\mathbb C$, in §4 real with $s>\delta$; $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ |
| $\kappa$ | mass/killing parameter, $\kappa\ge-\tfrac14$; $\kappa=s(s-1)$ |
| $u$ | subordination (proper-time) variable $\in(0,\infty)$ — the paper's overloaded "$s$", renamed |
| $Z_X,\ \delta$ | Selberg zeta $\{\operatorname{Re}s>\delta\}\to\mathbb C$; critical exponent $\in(0,1]$ (both defined §4.1) |
| $\ell_{\mathrm{sys}},\ N_X(R)$ | systole $\inf_\gamma\ell_\gamma>0$; count $\#\{\gamma\in\mathcal P_X:\ell_\gamma\le R\}<\infty$ |

**Standing conventions.** $\Delta_X\ge0$ (geometer's sign; $\operatorname{spec}\Delta_X\subseteq[0,\infty)$); Brownian motion at speed $2$ (generator $-\Delta_X$). Three time-like variables are kept distinct, deviating from the paper's single "$s$": the **spectral** $s$, the **subordination/proper-time** $u$ (integrated in $I_\phi,V_\phi$), the **loop duration** $t$ (already integrated out). $s$ and $\kappa$ are linked by $s=\tfrac12+\sqrt{\tfrac14+\kappa}\iff\kappa=s(s-1)$, $\kappa\ge-\tfrac14$. **Total mass** always means the sum over **non-trivial, non-peripheral** classes: the trivial class carries infinite mass, and peripheral (cusp) classes have no closed geodesic and are excluded.

Two objects built earlier reach §4 only through their end-formulas; their definitions are folded here so nothing is off-page.

**Used here — $\phi$, Bernstein with Assumption 2.3:** only that it yields a well-defined $I_\phi$; no other property of $\phi$ is used.
> [!recall]- $\phi$ a Bernstein function satisfying Assumption 2.3
> $\phi:(0,\infty)\to[0,\infty)$ is **Bernstein** if it is $C^\infty$ with $(-1)^{n-1}\phi^{(n)}(\lambda)\ge0$ for all $n\ge1,\lambda>0$ (its derivative completely monotone). Equivalently (Lévy–Khintchine) $\phi(\lambda)=a+b\lambda+\int_0^\infty(1-e^{-\lambda u})\,\nu(du)$ for a unique triple $(a,b,\nu)$, $a,b\ge0$, $\int_0^\infty(1\wedge u)\,\nu(du)<\infty$ — the Laplace exponent of a **subordinator** (an increasing random clock $T_t\ge0$, $\mathbb E[e^{-\lambda T_t}]=e^{-t\phi(\lambda)}$): $a$ = killing rate, $b$ = drift, $\nu$ = jump intensity. **Assumption 2.3:** $b>0$ **or** $\nu(0,\infty)=\infty$ — the clock strictly increases, so its law has no atom at $0$ and the subordinate heat kernel is a genuine density. *(It says nothing about $a$: killing is allowed — $\phi(\lambda)=\lambda+\kappa$ has $a=\kappa$ and passes via $b=1$.)* The four instances: $\phi(\lambda)=\lambda,\ \lambda+\kappa,\ \lambda^{\alpha/2},\ (\lambda+\kappa)^{\alpha/2}$.

**Used here — $I_\phi$ (Definition 3.6):** only its value as a function of $L$; its internals are not touched by §4.
> [!recall]- $I_\phi$, the weighted heat-kernel integral, and $V_\phi$
> $\displaystyle I_\phi(L):=\int_0^\infty\frac{e^{-u/4}\,e^{-L^2/(4u)}}{2\sqrt{\pi u}}\,V_\phi(du)\ \in(0,\infty),\qquad L>0,$
> where the kernel $e^{-u/4}e^{-L^2/(4u)}/(2\sqrt{\pi u})$ is the speed-$2$, mass-shifted Brownian heat kernel on $\mathbb H^2$ at proper time $u$ between two points a hyperbolic distance $L$ apart, and $V_\phi$ — the **weighted potential measure** — is the $\sigma$-finite measure on $(0,\infty)$ obtained by integrating the subordinator's time-$t$ law $\psi^\phi_t$ over all durations, $V_\phi(du)=\int_0^\infty\psi^\phi_t(du)\,dt/t$. Its four values: $du/u$ (Brownian), $e^{-\kappa u}\,du/u$ (killing $\kappa$), $\tfrac\alpha2\,du/u$ ($\alpha$-stable), $\tfrac\alpha2 e^{-\kappa u}\,du/u$ (shifted stable). $I_\phi$ is the **only** factor of the class mass that depends on the process; all geometry sits in the prefactor.

# B. Spine of §4 (skim layer)

The section is four moves. Read this list and you have §4's logical content; drop into the matching subsection for expansions, imports and proofs.

1. **§4.1 — $Z_X$ and $\delta$.** *Define* $Z_X(s)=\prod_\gamma\prod_{k\ge0}(1-e^{-(s+k)\ell_\gamma})$ (converges for $\operatorname{Re}s>\delta$) and the critical exponent $\delta$; *produce* the log-expansion $-\log Z_X(s)=\sum_{\gamma,m}\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$.
2. **§4.2 — the criterion (Lemma 4.2).** *Given* $\tfrac{L}{2\sinh(L/2)}I_\phi(L)=C\,\tfrac{e^{(1-s)L}}{e^L-1}$ with $C,s$ independent of $L$; *produce* $\sum_{\gamma,m}\mu^\phi_X(\mathcal C_X(\gamma^m))=-C\log Z_X(s)$.
3. **§4.3 — the four processes (Cor 4.3).** *Verify* the hypothesis for $\phi=\lambda,\lambda+\kappa,\lambda^{\alpha/2},(\lambda+\kappa)^{\alpha/2}$; *produce* the killing identity $\sum_{\gamma,m}\mu^\kappa_X(\mathcal C_X(\gamma^m))=-\log Z_X(\tfrac12+\sqrt{\tfrac14+\kappa})$.
4. **§4.4 — finiteness (Cor 4.7).** *Given* $s>\delta$; *produce* finiteness of the total mass (divergence for $s\le\delta$), hence the dichotomy: infinite-area surfaces are finite already at $\kappa=0$; finite-area surfaces need killing.

# C. The results

## §4.1  The Selberg zeta function $Z_X$ and the critical exponent $\delta$

Both are defined here; $\delta$ is first load-bearing on this page, so it gets its full expansion.

> [!def]+ $\delta$, the critical exponent
> $\displaystyle\delta:=\inf\Big\{s>0:\sum_{h\in\Gamma}e^{-s\,d(z,hz)}<\infty\Big\}\in(0,1]$ (abscissa of convergence of the Poincaré series; independent of the base point $z\in\mathbb H^2$). **Used here — one property only:** $\delta$ is the exponential growth rate of closed geodesics,
> $$N_X(R):=\#\{\gamma\in\mathcal P_X:\ell_\gamma\le R\}\ \sim\ \frac{e^{\delta R}}{\delta R}\qquad(R\to\infty),$$
> together with the dichotomy $\delta=1\iff\operatorname{area}(X)<\infty$ (so $\operatorname{area}(X)=\infty\Rightarrow\delta<1$). Read every "$s>\delta$" below as **decay rate beats geodesic-proliferation rate**.

> **Definition 4.1 (Selberg zeta function).** For $\operatorname{Re}(s)>\delta$,
> $$Z_X(s):=\prod_{\gamma\in\mathcal P_X}\ \prod_{k=0}^{\infty}\Big(1-e^{-(s+k)\ell_\gamma}\Big).\tag{31}$$
> A double product: outer over primitive geodesics (the "primes"), inner over $k\ge0$.

The single fact §4.2–§4.4 use is its logarithm, and it is elementary.

> [!import]- (F1) The $-\log Z_X$ expansion — Says / Needs / Gives
> **Says.** For $\operatorname{Re}(s)>\delta$, $\displaystyle -\log Z_X(s)=\sum_{\gamma\in\mathcal P_X}\sum_{m=1}^{\infty}\frac1m\cdot\frac{e^{(1-s)L}}{e^L-1}\Big|_{L=m\ell_\gamma}.\tag{32}$
> **Needs.** $\operatorname{Re}(s)>\delta$ (so (31) converges absolutely).
> **Gives.** The right-hand side of every §4 identity, as a double sum with summand $\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$.
> **Derivation (assume freely; anchors only):** apply $-\log(1-x)=\sum_{m\ge1}x^m/m$ to each factor of (31), then sum the inner geometric series $\sum_{k\ge0}e^{-(s+k)m\ell_\gamma}=e^{-sm\ell_\gamma}/(1-e^{-m\ell_\gamma})=e^{(1-s)L}/(e^L-1)$. No zeta theory is used.

## §4.2  The Selberg zeta criterion (Lemma 4.2)

The section's engine: it empties the geometry out of "is the total mass a zeta value?", leaving a one-variable functional equation.

> **Lemma 4.2 (Selberg zeta criterion).** Assume:
> **(H1)** $\phi$ is Bernstein with Assumption 2.3, and $I_\phi$ is its weighted heat-kernel integral (both recalled in §4.0).
> **(H2)** there exist $C>0$ and $s>\delta$, **both independent of $L$**, with
> $$\frac{L}{2\sinh(L/2)}\,I_\phi(L)=C\cdot\frac{e^{(1-s)L}}{e^{L}-1}\qquad\text{for all }L>0.\tag{33}$$
> **Then** the total mass over all non-trivial non-peripheral classes is the zeta value
> $$\sum_{\gamma\in\mathcal P_X}\ \sum_{m=1}^{\infty}\mu^\phi_X\big(\mathcal C_X(\gamma^m)\big)=-C\log Z_X(s),\tag{34}$$
> the double sum absolutely convergent.

> [!warning] Why "independent of $L$" is the entire hypothesis
> $L=m\ell_\gamma$ ranges over all class-lengths. If $C$ or $s$ could depend on $L$, (33) would be solvable for $C(L)$ pointwise and say nothing; one pair $(C,s)$ serving every $L$ at once is the whole content.

> [!import]- (24) The class-mass formula [§3, Theorem 3.5] — Says / Needs / Gives
> **Says.** For primitive $\gamma$, $m\ge1$, $L=m\ell_\gamma$: $\displaystyle\mu^\phi_X\big(\mathcal C_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L)=\frac1m\cdot\frac{L}{2\sinh(L/2)}\,I_\phi(L).$
> **Needs.** (H1): $\phi$ Bernstein with Assumption 2.3 (so $I_\phi$ exists); $\gamma\in\mathcal P_X$; $m\ge1$.
> **Gives.** The class mass as *(geometric prefactor $\tfrac1m\tfrac{L}{2\sinh(L/2)}$)* $\times$ *(analytic factor $I_\phi(L)$)*. Assume freely; §3 proves it (covering-space unfolding $+$ the Wang–Xue strip identity $+$ collapse of the time integral into $V_\phi$). Nothing here re-proves it.

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | import (24) | $L=m\ell_\gamma,\ \ell_\gamma=L/m$ | $\mu^\phi_X(\mathcal C_X(\gamma^m))=\tfrac1m\tfrac{L}{2\sinh(L/2)}I_\phi(L)$ |
| 2 | hypothesis (33) | the factor $\tfrac{L}{2\sinh(L/2)}I_\phi(L)$ | $\mu^\phi_X(\mathcal C_X(\gamma^m))=C\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$ |
| 3 | import (F1)/(32) | sum step 2 over $\gamma\in\mathcal P_X,\,m\ge1$ | $\sum_{\gamma,m}\mu^\phi_X=C\sum_{\gamma,m}\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}=-C\log Z_X(s)$ |
| 4 | $s>\delta$ (§4.1) | the double sum | absolute convergence |

Every symbol in every row is typed in §4.0; every predicate is an import or recall above. The lemma typechecks with nothing off-page.

> [!note]- Proof (skippable — the Discharge is the proof)
> By (24) with $L=m\ell_\gamma$ and $\ell_\gamma=L/m$, $\ \mu^\phi_X(\mathcal C_X(\gamma^m))=\tfrac1m\tfrac{L}{2\sinh(L/2)}I_\phi(L)$. Substitute (33) into the second factor: $\ \mu^\phi_X(\mathcal C_X(\gamma^m))=\tfrac{C}{m}\tfrac{e^{(1-s)L}}{e^L-1}$, exactly $C$ times the $(\gamma,m)$ summand of (32). Summing over $\gamma\in\mathcal P_X,\ m\ge1$ gives $-C\log Z_X(s)$. Since $s>\delta$, geodesics grow like $e^{\delta R}$ while each summand decays like $e^{-sR}$, so the sum converges absolutely (made precise in §4.4). $\square$

## §4.3  The four processes, and the killing identity (Corollary 4.3)

Lemma 4.2 leaves one line per process: check (33) using the closed $I_\phi$ of §4.0 and $2\sinh(L/2)=e^{L/2}-e^{-L/2}=e^{-L/2}(e^L-1)$.

| $\phi(\lambda)$ | $V_\phi(du)$ | $I_\phi(L)$ | $C$ | $s$ | total mass finite iff |
|---|---|---|---|---|---|
| $\lambda$ (Brownian) | $du/u$ | $e^{-L/2}/L$ | $1$ | $1$ | $\delta<1$ |
| $\lambda+\kappa$, $\kappa\ge-\tfrac14$ | $e^{-\kappa u}du/u$ | $e^{-L\sqrt{1/4+\kappa}}/L$ | $1$ | $\tfrac12+\sqrt{\tfrac14+\kappa}$ | $s>\delta$ |
| $\lambda^{\alpha/2}$, $\alpha\in(0,2)$ | $\tfrac\alpha2 du/u$ | $\tfrac\alpha2 e^{-L/2}/L$ | $\alpha/2$ | $1$ | $\delta<1$ |
| $(\lambda+\kappa)^{\alpha/2}$ | $\tfrac\alpha2 e^{-\kappa u}du/u$ | $\tfrac\alpha2 e^{-L\sqrt{1/4+\kappa}}/L$ | $\alpha/2$ | $\tfrac12+\sqrt{\tfrac14+\kappa}$ | $s>\delta$ |

> [!note]- Verification of row 2 (killing), from which the others follow (skippable)
> With $V_\phi(du)=e^{-\kappa u}du/u$, $I_\kappa(L)=\int_0^\infty\frac{e^{-(1/4+\kappa)u}e^{-L^2/(4u)}}{2\sqrt\pi\,u^{3/2}}\,du$. The **Gaussian reciprocal integral** $\int_0^\infty u^{-3/2}e^{-au-b/u}\,du=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$ (for $a,b>0$; here $a=\tfrac14+\kappa,\ b=\tfrac{L^2}4$) gives $I_\kappa(L)=\frac{1}{2\sqrt\pi}\cdot\frac{2\sqrt\pi}{L}e^{-L\sqrt{1/4+\kappa}}=\frac{e^{-L\sqrt{1/4+\kappa}}}{L}$. With $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, so $\sqrt{\tfrac14+\kappa}=s-\tfrac12$,
> $$\frac{L}{2\sinh(L/2)}I_\kappa(L)=\frac{e^{-(s-1/2)L}}{2\sinh(L/2)}=\frac{e^{-(s-1/2)L}}{e^{-L/2}(e^L-1)}=\frac{e^{(1-s)L}}{e^L-1},$$
> so (33) holds with $C=1$. Brownian is $\kappa=0$ ($s=1$). The stable rows scale $V_\phi$ by $\tfrac\alpha2$, so $I_\phi=\tfrac\alpha2 I_{\mathrm{BM/killed}}$ and $C=\alpha/2$, $s$ unchanged.

Feeding each row into Lemma 4.2 gives four total-mass identities. The one the rest of the paper uses:

> **Corollary 4.3 (the killing / Selberg identity).** For $\kappa\ge-\tfrac14$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}>\delta$,
> $$\sum_{\gamma\in\mathcal P_X}\ \sum_{m=1}^{\infty}\mu^\kappa_X\big(\mathcal C_X(\gamma^m)\big)=-\log Z_X\Big(\tfrac12+\sqrt{\tfrac14+\kappa}\Big).\tag{35}$$
> In particular (Brownian, $\kappa=0$, when $\delta<1$) the total mass is $-\log Z_X(1)$.

## §4.4  Finiteness of the total mass, and the dichotomy (Corollary 4.7)

(34)–(35) equate the total mass to $-C\log Z_X(s)$, finite **when** $s>\delta$. That the sum is genuinely finite there (and infinite otherwise) is what makes §6's probability measure exist.

> **Corollary 4.7 (finiteness).** Let $\phi$ be one of the four processes, with $\mu^\phi_X(\mathcal C_X(\gamma^m))=\tfrac{C}{m}\tfrac{e^{(1-s)L}}{e^L-1}$, $s=s(\phi)$, $C=C(\phi)>0$. Then
> $$\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\mu^\phi_X\big(\mathcal C_X(\gamma^m)\big)<\infty\iff s>\delta.\tag{41}$$
> If $s\le\delta$ the sum diverges, and $Z_X(s)\to0$ as $s\downarrow\delta$.

> [!import]- (F2) Systole bound — Says / Needs / Gives
> **Says.** With $\ell_{\mathrm{sys}}:=\inf_{\gamma\in\mathcal P_X}\ell_\gamma$, for every $L\ge\ell_{\mathrm{sys}}$: $\ \tfrac{e^{(1-s)L}}{e^L-1}\le\tfrac{e^{-sL}}{1-e^{-\ell_{\mathrm{sys}}}}$.
> **Needs.** $\ell_{\mathrm{sys}}>0$ — true because $N_X(R)<\infty$ for all $R$ (geometric finiteness), so a shortest geodesic exists.
> **Gives.** Every class-length $L=m\ell_\gamma\ge\ell_{\mathrm{sys}}$ obeys the clean exponential bound; the geometry enters only through the constant $1/(1-e^{-\ell_{\mathrm{sys}}})$.

> [!import]- (PGT) Prime geodesic theorem — Says / Needs / Gives  [the one genuine gap of §4]
> **Says.** $N_X(R)=\#\{\gamma\in\mathcal P_X:\ell_\gamma\le R\}\sim e^{\delta R}/(\delta R)$ as $R\to\infty$.
> **Needs.** $X$ geometrically finite.
> **Gives.** $\int^\infty e^{-sR}\,dN_X(R)$ converges $\iff s>\delta$ (tail integrand $e^{-(s-\delta)R}/R$). **Status:** not proved here; a consequence of the Selberg trace formula, and the only unproved input to §4.

**Discharge.**

| step | apply | to | get |
|---|---|---|---|
| 1 | (F2) $+\ \sum_{m\ge1}x^m/m=-\log(1-x)$, $x=e^{-s\ell_\gamma}$ | the $m$-sum, per $\gamma$ | $\sum_m\mu^\phi_X(\mathcal C_X(\gamma^m))\asymp C\,e^{-s\ell_\gamma}$ |
| 2 | reduces (41) to | $\sum_{\gamma}e^{-s\ell_\gamma}$ | (41) $\iff\sum_\gamma e^{-s\ell_\gamma}<\infty$ |
| 3 | (PGT), integrate $\int e^{-sR}dN_X(R)$ by parts | the geodesic sum | converges $\iff s>\delta$; at $s=\delta$, tail $\sim\int^\infty dR/R=\infty$ |
| 4 | monotonicity of (32) as $s\downarrow\delta$ | $-\log Z_X(s)$ | $\uparrow\infty$, so $Z_X(s)\to0$ |

> [!note]- Proof (skippable)
> **Step 1 (sum over iterates $m$).** For $L=m\ell_\gamma\ge\ell_{\mathrm{sys}}$, (F2) gives $\tfrac{e^{(1-s)L}}{e^L-1}\le\tfrac{e^{-sL}}{1-e^{-\ell_{\mathrm{sys}}}}$; with $x=e^{-s\ell_\gamma}$ and $\sum_m x^m/m=-\log(1-x)$, $\ \sum_{m\ge1}\mu^\phi_X(\mathcal C_X(\gamma^m))\le\tfrac{-C}{1-e^{-\ell_{\mathrm{sys}}}}\log(1-e^{-s\ell_\gamma})$, and $\ge Ce^{-s\ell_\gamma}$ (the $m=1$ term). Since $\ell_\gamma\to\infty$ along $\mathcal P_X$, $-\log(1-e^{-s\ell_\gamma})=e^{-s\ell_\gamma}+O(e^{-2s\ell_\gamma})$, so (41) $\iff\sum_\gamma e^{-s\ell_\gamma}<\infty$.
> **Step 2 (sum over geodesics).** Integrating by parts, $\sum_{\ell_\gamma\le T}e^{-s\ell_\gamma}=e^{-sT}N_X(T)+s\int_0^T e^{-sR}N_X(R)\,dR$. By (PGT) the large-$R$ integrand is $\sim e^{-(s-\delta)R}/R$: convergent for $s>\delta$, divergent like $\int^\infty dR/R$ at $s=\delta$, divergent for $s<\delta$. Hence (41) $\iff s>\delta$; and $-\log Z_X(s)\uparrow\infty$ as $s\downarrow\delta$, i.e. $Z_X(s)\to0$. $\square$

**The dichotomy (why §5 exists).**

| $X$ | $\delta$ | Brownian $\phi=\lambda$ ($s=1$) | killed $\phi=\lambda+\kappa,\ \kappa>0$ ($s>1$) |
|---|---|---|---|
| infinite area | $<1$ | **finite**, $=-\log Z_X(1)$ | finite |
| finite area (closed / cusped) | $=1$ | **infinite** | finite, $=-\log Z_X(s)$ |

On a finite-area surface the Brownian total mass diverges: $s=1=\delta$ is the boundary case, which (PGT) decides against convergence. A strictly positive killing $\kappa>0$ (pushing $s>1$) is **necessary** to make the mass finite — or one renormalises, which is §5, and the renormalised value turns out to be $\log\det\Delta_X$.

# D. Exports, climb, commentary

**Exports (what later sections consume from §4).**
- **(E1)** the criterion (34): total mass $=-C\log Z_X(s)$ whenever (33) holds. → §5, §6, §7.
- **(E2)** the killing identity (35): $\sum_{\gamma,m}\mu^\kappa_X(\mathcal C_X(\gamma^m))=-\log Z_X(s)$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$. → §6 (the normalising constant of $\mathbb P_s$), §5.
- **(E3)** finiteness (41): $s>\delta\Rightarrow$ total mass finite. → §6 (existence of the probability measure), §5 (the finite-area divergence is what §5 renormalises).

**Climb (optional — none is needed to typecheck §4).** Sibling sections: [[§3 Mass of a Homotopy Class]] (proves the (24) class-mass import) · [[§5 Determinants and the Polyakov Anomaly]] (renormalises the finite-area divergence) · [[§6 Probability on Homotopy and Homology Classes]] (normalises the total mass). Import sources, status and gap-depth: [[External Inputs and Gaps]]. Backchain to anchors: [[Anchors and Prerequisites]].

> [!note]- Commentary (skippable)
> §4 costs almost nothing and delivers the paper's headline. §3 computed one number per class; §4 adds them up and recognises the answer — two applications of $-\log(1-x)=\sum x^m/m$, one to the outer product, one to the inner, matched against the shape $\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$ that the Wang–Xue strip identity had already produced. That the analytic factor $I_\phi$ reproduces the geometric shape $e^{(1-s)L}/(e^L-1)$ *up to a constant* is the entire content of the criterion, and it is why a question about subordinators becomes a one-variable functional equation. Killing passes because the Gaussian reciprocal integral manufactures exactly the exponential the $\sinh$ needs; the stable case passes for the different reason that scale-invariance forces $V_\phi\propto du/u$, collapsing $I_\phi$ to $\tfrac\alpha2$ times the Brownian one. A generic Bernstein $\phi$ does not pass — the source of §7's open question.
>
> The comparison $s>\delta$ is a prime-number-theorem argument with geodesics for primes, and it fails in the case one most cares about — a closed surface, no killing, $s=\delta=1$. That failure is not an annoyance to route around: it is the reason §5 exists, and the reason the renormalised finite value turns out to be $\log\det\Delta_X$. (Companion reading, Remark 4.4: with $Z(s)=Z_X(s)^{-1}$, (35) says the total mass is the free energy $\log Z(s)$ of a non-interacting Bose gas whose modes $(\gamma,k)$ have energies $(s+k)\ell_\gamma$; the loop-soup independence of §3.3 is its probabilistic shadow.)