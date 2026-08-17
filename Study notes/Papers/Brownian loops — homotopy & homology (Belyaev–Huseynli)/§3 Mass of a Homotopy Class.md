---
type: paper-section
paper: "BH26"
subject: brownian-loops
section: "3"
tags: [paper, section, self-contained]
---

> [!info] Part of [[Map - Brownian Loops on Homotopy and Homology Classes]]. Self-contained: every symbol, predicate and imported result used below is written out on this page. Grey callouts are folds on THIS page — opening one is a scroll, not a jump to another file. You can typecheck §3 front-to-back without opening anything else.

**What §3 buys you.** §2 built a $\sigma$-finite loop measure $\mu^\phi_X$ of infinite total mass; §3 computes the ONE number it assigns to each free-homotopy class and finds it closed-form: $\mu^\phi_X(\mathcal C_X(\gamma^m))=\tfrac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)$, geometry (the prefactor) times process (the analytic factor $I_\phi$). It then upgrades those numbers to a random object — the Poissonian loop soup, whose class-counts are independent Poissons — and shows the same numbers already determine the surface: they recover the marked length spectrum, hence (in $2$D) the metric up to isometry.

# A. Standing setup

Everything in §3 lives on a fixed hyperbolic surface $X$ and computes the mass a fixed loop measure assigns to a single free-homotopy class of loops. The paragraphs below fix those objects as literal text, so dropping straight into §3 needs nothing from earlier sections.

**The surface.** $\Gamma\subseteq\mathrm{PSL}(2,\mathbb R)$ is a discrete, torsion-free group of isometries of the hyperbolic plane $\mathbb H^2$ (upper half-plane $\{z:\operatorname{Im}z>0\}$, metric $|dz|/\operatorname{Im}z$), acting **freely** — $\forall h\in\Gamma\setminus\{1\}\ \forall z\in\mathbb H^2:\ hz\neq z$ (no non-identity isometry fixes a point) — and **properly discontinuously** — $\forall K\Subset\mathbb H^2:\ \#\{h\in\Gamma:hK\cap K\neq\varnothing\}<\infty$ (each compact set meets only finitely many of its $\Gamma$-translates). Under exactly these two conditions the quotient $X=\Gamma\backslash\mathbb H^2$ (points of $\mathbb H^2$ glued when one is a $\Gamma$-image of the other) is a smooth hyperbolic surface and $\pi:\mathbb H^2\to X$ is a **covering map** (a local isometry under which $\mathbb H^2$ wraps around $X$) with **deck group** $\Gamma$ (the isometries permuting the sheets over each point), $\Gamma\cong\pi_1(X)$. $X$ is **geometrically finite**: $\Gamma$ finitely generated (equivalently $X$ has a finite-sided fundamental polygon); the only consequence used is that the length spectrum is locally finite, $\#\{\gamma:\ell_\gamma\le R\}<\infty$ for every $R$.

**Geodesics and their classes.** A closed geodesic $\gamma$ is **primitive** if it is not a repeated traversal of a shorter one — its representative $\tau\in\Gamma$ satisfies $\tau=\sigma^k\ (\sigma\in\Gamma,k\ge1)\Rightarrow k=1$. $\mathcal P_X$ = primitive oriented closed geodesics; $\ell_\gamma:=\min_z d(z,\tau z)>0$ = length of $\gamma$ (the **translation length** of $\tau$). Every closed geodesic is the $m$-fold iterate $\gamma^m$ of a unique primitive $\gamma$, of length $L:=m\ell_\gamma$. Two oriented loops are **freely homotopic** if one deforms into the other through closed curves with no basepoint fixed ($\exists$ continuous $H:S^1\times[0,1]\to X$ between them); free-homotopy classes correspond bijectively to conjugacy classes $[h]=\{qhq^{-1}:q\in\Gamma\}$ in $\Gamma$, and — restricting to non-trivial, non-peripheral classes — to pairs $(\gamma,m)\in\mathcal P_X\times\mathbb Z_{\ge1}$: $\mathcal C_X(\gamma^m)$ is the class winding $m$ times around $\gamma$, i.e. the conjugacy class $[\tau^m]$. **The only geometric input to every class mass is the single positive number $L=m\ell_\gamma$.**

**The loop measure.** $\mathcal C_X$ is the space of unrooted, unparametrised, oriented loops on $X$ (a loop as a stochastic process produces it, stripped of its start-point and its clock). $\mu^\phi_X$ is the $\phi$-subordinate Brownian **loop measure** on $\mathcal C_X$: a $\sigma$-finite measure of **infinite** total mass, $\mu^\phi_X(\mathcal C_X)=\infty$ (the divergence is carried entirely by the trivial contractible class). Superscript $E$ instead of $\phi$ names its generalisation from an arbitrary regular symmetric Dirichlet form $(E,\mathcal F)$; $\mu^\kappa_X:=\mu^\phi_X$ for $\phi(\lambda)=\lambda+\kappa$. What §3 does is compute the single number $\mu^\phi_X(\mathcal C_X(\gamma^m))\in(0,\infty)$.

**Notation for §3.**

| symbol | type |
|---|---|
| $X=\Gamma\backslash\mathbb H^2$ | geometrically finite hyperbolic surface; $\mathbb H^2$ its universal cover |
| $\Gamma$ | discrete torsion-free $\subseteq\mathrm{PSL}(2,\mathbb R)$, $\cong\pi_1(X)$; deck group |
| $\gamma,\ \tau,\ \sigma$ | primitive closed geodesic; its representative $\tau\in\Gamma$; a generic element |
| $\mathcal P_X,\ \ell_\gamma$ | primitive oriented closed geodesics; $\ell_\gamma\in(0,\infty)$ their lengths |
| $m,\ L$ | $m\in\mathbb Z_{\ge1}$; $L:=m\ell_\gamma\in(0,\infty)$ |
| $\mathcal C_X(\gamma^m)$ | free-homotopy class of $\gamma^m$ $=$ conjugacy class $[\tau^m]$; a measurable set of loops |
| $\langle\tau\rangle,\ C_\Gamma(\tau^m)$ | infinite cyclic subgroup $\{\tau^k:k\in\mathbb Z\}$; centraliser $\{q\in\Gamma:q\tau^m=\tau^m q\}$ |
| $F_\tau$ | fundamental region for $\langle\tau\rangle$ acting on $\mathbb H^2$; standard form $\{1\le\operatorname{Im}z<e^{\ell_\gamma}\}$ |
| $\mu^E_X,\ \mu^\phi_X,\ \mu^\kappa_X$ | Dirichlet-form / $\phi$-subordinate / killing-$\kappa$ loop measure on $\mathcal C_X$; total mass $\infty$ |
| $p_{\mathbb H^2},\ p^E_{\mathbb H^2},\ p^\phi_{\mathbb H^2}$ | heat kernel on $\mathbb H^2$ (Brownian / Dirichlet-form / subordinate); density of $e^{-u\Delta}$ |
| $W^t_{x\to y}$ | unnormalised Brownian bridge measure on paths $[0,t]$, total mass $p(t,x,y)$ |
| $\psi^\phi_t$ | law of the subordinator $T_t$ at time $t$; a measure on $[0,\infty)$ |
| $V_\phi$ | weighted potential measure on $(0,\infty)$: $\int_0^\infty\psi^\phi_t\,dt/t$ |
| $I_\phi(L)$ | weighted heat-kernel integral $(0,\infty)\to(0,\infty)$, Definition 3.6 |
| $\phi,\ a,b,\nu$ | Bernstein function; its Lévy–Khintchine triple (killing, drift, jump intensity) |
| $\kappa,\ s,\ \alpha$ | killing $\kappa\ge-\tfrac14$; spectral parameter $s=\tfrac12+\sqrt{\tfrac14+\kappa}$; stable index $\alpha\in(0,2)$ |
| $u,\ t$ | subordination / proper-time $\in(0,\infty)$ (paper's "$s$"); loop duration $\in(0,\infty)$ |
| $\mathcal L_c,\ c,\ N_A$ | loop soup (Poisson point process, intensity $c\mu^\phi_X$); intensity $c>0$; count $\#\{\eta\in\mathcal L_c:\eta\in A\}$ |
| $P,\ \mathrm{MLS}$ | polar set $\subset X$; marked length spectrum $\mathcal C_X(\gamma^m)\mapsto m\ell_\gamma$ |

**Standing conventions.** $\Delta_X\ge0$ (geometer's sign; $\operatorname{spec}\Delta_X\subseteq[0,\infty)$); Brownian motion at speed $2$ (generator $-\Delta_X$). Three time-like variables are kept typographically distinct, deviating from the paper's single "$s$": the **spectral parameter** $s$; the **subordination / proper-time** variable $u$ (integrated in $I_\phi$ and $V_\phi$); the **loop duration** $t$ (integrated $\mathrm{d}t/t$). Spectral $s$ and killing $\kappa$ are linked by $s=\tfrac12+\sqrt{\tfrac14+\kappa}\iff\kappa=s(s-1)$, with $\kappa\ge-\tfrac14$ (at $\kappa=-\tfrac14$, $s=\tfrac12=\inf\operatorname{spec}\Delta_{\mathbb H^2}$). **Total mass** always means the sum over **non-trivial, non-peripheral** free-homotopy classes: the trivial (contractible) class carries infinite mass and is excluded, and peripheral (cusp) classes have no closed geodesic and are excluded.

Four objects are built in §2 and reach §3 only through their end-formulas; their definitions are folded here so nothing is off-page.

**Used here — $\phi$, Bernstein with Assumption 2.3:** only that it yields a well-defined $I_\phi$; no other property of $\phi$ is used.
> [!recall]- $\phi$ a Bernstein function satisfying Assumption 2.3
> $\phi:(0,\infty)\to[0,\infty)$ is **Bernstein** if it is $C^\infty$ with $(-1)^{n-1}\phi^{(n)}(\lambda)\ge0$ for all $n\ge1,\lambda>0$ (its derivative completely monotone). Equivalently (Lévy–Khintchine) $\phi(\lambda)=a+b\lambda+\int_0^\infty(1-e^{-\lambda u})\,\nu(du)$ for a unique triple $(a,b,\nu)$ with $a,b\ge0$ and $\int_0^\infty(1\wedge u)\,\nu(du)<\infty$ — the Laplace exponent of a **subordinator** (an increasing random clock $T_t\ge0$, $\mathbb E[e^{-\lambda T_t}]=e^{-t\phi(\lambda)}$): $a$ = killing rate, $b$ = drift, $\nu$ = jump intensity. **Assumption 2.3:** $b>0$ **or** $\nu(0,\infty)=\infty$ — the clock strictly increases, so its law has no atom at $0$ and the subordinate heat kernel is a genuine density. *(It says nothing about $a$: killing is allowed — $\phi(\lambda)=\lambda+\kappa$ has $a=\kappa$, passes via $b=1$.)* The four instances: $\phi(\lambda)=\lambda,\ \lambda+\kappa,\ \lambda^{\alpha/2},\ (\lambda+\kappa)^{\alpha/2}$.

**Used here — $V_\phi$, the weighted potential measure:** §3 touches only its four closed values in the table below; its construction is inert.
> [!recall]- $V_\phi$, the weighted potential measure, and the subordinator law $\psi^\phi_t$
> The subordinator's time-$t$ law $\psi^\phi_t$ is the measure on $[0,\infty)$ with $\int_{[0,\infty)}e^{-\lambda u}\,\psi^\phi_t(du)=e^{-t\phi(\lambda)}$. The **weighted potential measure** is the $\sigma$-finite measure on $(0,\infty)$ obtained by integrating $\psi^\phi_t$ over all durations against the Haar weight $dt/t$: $\displaystyle V_\phi(du)=\int_0^\infty\psi^\phi_t(du)\,\frac{dt}{t}$. Its four values, one per process: $du/u$ (Brownian $\phi=\lambda$), $e^{-\kappa u}\,du/u$ (killing $\phi=\lambda+\kappa$), $\tfrac\alpha2\,du/u$ ($\alpha$-stable $\phi=\lambda^{\alpha/2}$), $\tfrac\alpha2 e^{-\kappa u}\,du/u$ (shifted stable $\phi=(\lambda+\kappa)^{\alpha/2}$).

**Used here — the heat kernel and unnormalised bridge:** the decomposition (Theorem 3.2) is written against $p^E_{\mathbb H^2}$; its downstairs value is the periodisation of $p_{\mathbb H^2}$ over $\Gamma$.
> [!recall]- Heat kernel $p$, unnormalised bridge $W^t$, and the loop measure $\mu^E_X$
> $p_X(t,x,y)$ is the **heat kernel** on $X$: the density of the semigroup $e^{-t\Delta_X}$, equivalently the transition density of speed-$2$ Brownian motion, symmetric and satisfying $\int_X p_X(t,x,z)p_X(u,z,y)\,d\mathrm{vol}(z)=p_X(t+u,x,y)$. $W^t_{x\to y}$ is the **unnormalised Brownian bridge**: the measure on continuous paths $[0,t]\to X$ from $x$ to $y$ with total mass $|W^t_{x\to y}|=p_X(t,x,y)$ (its normalisation to a probability is the pinned bridge). The **loop measure** is $\displaystyle\mu^E_X=\int_0^\infty\frac{dt}{t}\int_X W^t_{x\to x}\,d\mathrm{vol}(x)$ pushed forward to unrooted, unparametrised loops; $\mu^\phi_X$ is its $\phi$-subordinate version, got by replacing $p$ with $p^\phi(t,\cdot,\cdot)=\int_0^\infty p(u,\cdot,\cdot)\,\psi^\phi_t(du)$. Superscript $E$ marks the same construction from any regular symmetric Dirichlet form; the only consequence used is that it yields a heat semigroup with a kernel.

**Used here — Lemma 2.11 collapse:** it turns the double $(t,u)$ integral of Theorem 3.2 into the single integral against $V_\phi$ that defines $I_\phi$; the move that carries Theorem 3.2 to Theorem 3.5.
> [!import]- (Lemma 2.11) The collapse identity — Says / Needs / Gives
> **Says.** For measurable $h\ge0$ on $(0,\infty)$: $\displaystyle\int_0^\infty\frac{dt}{t}\int_{[0,\infty)}h(u)\,\psi^\phi_t(du)=\int_0^\infty h(u)\,V_\phi(du).$
> **Needs.** Assumption 2.3 (so $\psi^\phi_t(\{0\})=0$; the integral runs over $(0,\infty)$).
> **Gives.** Collapses the double $(t,u)$ integral into one integral against $V_\phi$. **Derivation (assume freely; anchors only):** Tonelli on the non-negative integrand, then the definition of $V_\phi$. Not a gap.

# B. Spine of §3 (skim layer)

Read this list and you have §3's logical content; drop into the matching subsection for expansions, imports and proofs.

1. **§3.1 (Theorem 3.2, decomposition).** *Given* the subordinate loop measure and covering $\pi:\mathbb H^2\to X$ ⊢ *Produces* $\mu^E_X(\mathcal C_X(\gamma^m))=\int_0^\infty\tfrac{dt}{t}\int_{F_\tau}p^E_{\mathbb H^2}(t,w,\tau^m w)\,d\mathrm{vol}(w)$ (unfold the class onto one $\langle\tau\rangle$-fundamental strip).
2. **§3.1 (Wang–Xue, imported gap).** *Given* $u>0,\ L=m\ell_\gamma$, $\tau$ in standard form ⊢ *Produces* the spatial integral $\int_{F_\tau}p_{\mathbb H^2}(u,w,e^Lw)\,d\mathrm{vol}=\tfrac{\ell_\gamma}{2\sinh(L/2)}\cdot\tfrac{e^{-u/4}e^{-L^2/(4u)}}{2\sqrt{\pi u}}$ (geometry $\times$ analytic).
3. **§3.1 (Theorem 3.5, class mass).** *Given* Theorem 3.2 $+$ Wang–Xue $+$ Lemma 2.11 ⊢ *Produces* $\mu^\phi_X(\mathcal C_X(\gamma^m))=\tfrac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)=\tfrac1m\tfrac{L}{2\sinh(L/2)}I_\phi(L)$ — the (24) formula used everywhere later.
4. **§3.1 (special cases, Remark 3.7).** *Given* the four $V_\phi$ values $+$ the Gaussian reciprocal integral ⊢ *Produces* the four closed masses; killing gives $\tfrac1m e^{(1-s)L}/(e^L-1)$, valid down to $\kappa=-\tfrac14$.
5. **§3.2 (quantum digression, folded).** A dictionary: Feynman–Kac $\to$ killing kernel $\to$ Schwinger $-\log\det(\Delta+\kappa)=|\mu^\kappa_X|_{\mathrm{reg}}$. No later result consumes it.
6. **§3.3 (Proposition 3.8, loop soup).** *Given* $c\mu^\phi_X$ as a Poisson intensity ⊢ *Produces* $N_{\gamma,m}\sim\mathrm{Poisson}(c\mu^\phi_X(\mathcal C_X(\gamma^m)))$, jointly independent across distinct classes; plus the exponential formula (exported to §6).
7. **§3.4 (Proposition 3.11, MLS inversion).** *Given* the Brownian / killing class mass ⊢ *Produces* $\ell_\gamma=\log(1+1/\mu_X(\mathcal C_X(\gamma)))$, mass strictly monotone in $\ell_\gamma$, so the masses recover the marked length spectrum.
8. **§3.4 (Corollary 3.12, rigidity).** *Given* equal masses for two hyperbolic metrics $+$ Otal–Croke ⊢ *Produces* the metrics isometric, same point of Teichmüller space.

# C. The results

## §3.1  The class mass: decomposition, Wang–Xue, and the closed form

The whole computation is three moves: unfold the class onto one fundamental strip (Theorem 3.2), evaluate the resulting spatial integral by an imported heat-kernel identity (Wang–Xue), and collapse the time integral into $V_\phi$ (Lemma 2.11). The output is one number per class.

**New symbols.** $F_\tau$ (fundamental region for $\langle\tau\rangle$); $C_\Gamma(\tau^m)$ (centraliser); the "standard form" of $\tau$; $I_\phi$ (isolated after Theorem 3.5).

Four tokens in the coming statements are not anchors. Their expansions:

**Fundamental region.** A **fundamental region** for a group $H$ of isometries acting on $\mathbb H^2$ is a Borel set $F$ with $\bigcup_{h\in H}hF=\mathbb H^2$ and $\mathrm{vol}(hF\cap F)=0$ for $h\neq1$ — one representative point from each $H$-orbit, up to a null set. For $\langle\tau\rangle$ in **standard form** $\tau:z\mapsto e^{\ell_\gamma}z$ (any primitive $\tau$ is conjugate to this: it is hyperbolic, so fixes two boundary points, moved to $0,\infty$), the region is the **annular strip** $F_\tau=\{z\in\mathbb H^2:1\le\operatorname{Im}z<e^{\ell_\gamma}\}$: the map $z\mapsto e^{\ell_\gamma}z$ scales imaginary parts by $e^{\ell_\gamma}$, so each orbit meets the strip once.

**Centraliser and the coset decomposition.** The **centraliser** $C_\Gamma(\tau^m):=\{q\in\Gamma:q\tau^m=\tau^m q\}$ is the elements commuting with $\tau^m$. Anything commuting with $\tau^m$ preserves the axis of $\tau$ (the geodesic $\{iy:y>0\}$ through its two fixed points); the axis-preserving elements of a discrete torsion-free $\Gamma$ form exactly the infinite cyclic group $\langle\tau\rangle=\{\tau^k:k\in\mathbb Z\}$. Hence the conjugacy class $[\tau^m]$ is the disjoint union over left cosets $\displaystyle[\tau^m]=\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^m r^{-1}\}$: distinct cosets give distinct conjugates, and summing a $\Gamma$-periodic function over these cosets, then integrating over the fundamental domain of $\Gamma$, equals integrating over the single larger fundamental region $F_\tau$ of $\langle\tau\rangle$ (the "unfolding").

**Periodisation.** The heat kernel on the quotient $X=\Gamma\backslash\mathbb H^2$ is the **periodisation** of the kernel upstairs: $p_X(t,\pi w,\pi w')=\sum_{h\in\Gamma}p_{\mathbb H^2}(t,w,hw')$ (sum a walk downstairs over all lifts of its endpoint). Restricting the diagonal $w'=w$ sum to the terms $h\in[\tau^m]$ isolates the loops in the class $\mathcal C_X(\gamma^m)$.

**Used here — Wang–Xue strip identity:** it supplies the exact spatial integral in Theorem 3.5; the $\mathbb H^2$ heat kernel has no elementary closed form, so this is imported, not derived (contrast §7, where $\mathbb H^3$ is elementary and the analogue is proved).
> [!import]- (20) Wang–Xue strip identity [WX25, Lemma 3.2] — Says / Needs / Gives  [genuine gap of §3]
> **Says.** For $u>0$, $m\ge1$, $L=m\ell_\gamma$, and $\tau$ in standard form $z\mapsto e^{\ell_\gamma}z$: $\displaystyle\int_{F_\tau}p_{\mathbb H^2}(u,w,e^{L}w)\,d\mathrm{vol}(w)=\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-u/4}\,e^{-L^2/(4u)}}{2\sqrt{\pi u}}.$
> **Needs.** $u>0$; $L=m\ell_\gamma>0$; $\tau$ standard form; $p_{\mathbb H^2}$ the speed-$2$ hyperbolic heat kernel.
> **Gives.** The spatial integral over the strip factorises as *(geometric $\tfrac{\ell_\gamma}{2\sinh(L/2)}$)* $\times$ *(analytic in $u,L$)*, the second factor being the speed-$2$, mass-shifted Euclidean heat kernel at proper time $u$ between points a hyperbolic distance $L$ apart. **Status:** not proved here; imported from [WX25, Lem 3.2]. Assume freely; nothing here re-proves it.

> **Theorem 3.2 (covering-space decomposition).** For a regular symmetric Dirichlet-form loop measure $\mu^E_X$, $\gamma\in\mathcal P_X$, $m\ge1$, with $\tau\in\Gamma$ representing $\gamma$ and $F_\tau$ a fundamental region for $\langle\tau\rangle$:
> $$\mu^E_X\big(\mathcal C_X(\gamma^m)\big)=\int_0^\infty\frac{dt}{t}\int_{F_\tau}p^E_{\mathbb H^2}(t,w,\tau^m w)\,d\mathrm{vol}(w).\tag{18}$$

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | loop-measure recall $+$ periodisation | $\mu^E_X$ on the diagonal | $\int_0^\infty\tfrac{dt}{t}\int_X\sum_{h\in\Gamma}p^E_{\mathbb H^2}(t,w,hw)\,d\mathrm{vol}$ over a $\Gamma$-domain |
| 2 | restrict $h$ to the conjugacy class | $\{h\in[\tau^m]\}$ | picks out the loops in $\mathcal C_X(\gamma^m)$ |
| 3 | $C_\Gamma(\tau^m)=\langle\tau\rangle$, coset split | $[\tau^m]=\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^m r^{-1}\}$ | $\Gamma$-sum over cosets |
| 4 | unfold coset sum into one strip | $\bigcup_r$ over the $\Gamma$-domain | $\int_{F_\tau}p^E_{\mathbb H^2}(t,w,\tau^m w)\,d\mathrm{vol}$ |

Every symbol is typed above; the block typechecks with nothing off-page.

> [!note]- Proof of Theorem 3.2 (skippable)
> Lift the loop measure to $\mathbb H^2$: the diagonal Dirichlet-form heat kernel on $X$ is the periodisation $p^E_X(t,\pi w,\pi w)=\sum_{h\in\Gamma}p^E_{\mathbb H^2}(t,w,hw)$, and a loop downstairs that closes up in the class $\mathcal C_X(\gamma^m)$ lifts to a path from $w$ to $hw$ with $h$ in the conjugacy class $[\tau^m]$. Restricting the periodisation sum to $h\in[\tau^m]$ therefore isolates exactly the loops of the class. Because commuting with $\tau^m$ forces preservation of the axis of $\tau$, and axis-preserving elements of a discrete torsion-free $\Gamma$ are exactly $\langle\tau\rangle$, the centraliser is $C_\Gamma(\tau^m)=\langle\tau\rangle$; so the class is the disjoint coset union $[\tau^m]=\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^m r^{-1}\}$. Summing the conjugates $r\tau^m r^{-1}$ over $r\in\Gamma/\langle\tau\rangle$ while integrating over a fundamental domain of $\Gamma$ is, by the standard unfolding, a single integral over the larger fundamental region $F_\tau$ of $\langle\tau\rangle$, giving (18). $\square$

Specialising the Dirichlet form to the $\phi$-subordinate Brownian process ($p^E\rightsquigarrow p^\phi$, and $p^\phi(t,\cdot,\cdot)=\int_{[0,\infty)}p(u,\cdot,\cdot)\,\psi^\phi_t(du)$) turns (18) into a double integral over duration $t$ and proper time $u$:
$$\mu^\phi_X\big(\mathcal C_X(\gamma^m)\big)=\int_0^\infty\frac{dt}{t}\int_{F_\tau}\int_{[0,\infty)}p_{\mathbb H^2}(u,w,\tau^m w)\,\psi^\phi_t(du)\,d\mathrm{vol}(w).\tag{19}$$

> **Theorem 3.5 (mass of the subordinate Brownian loop measure).** Assume:
> **(H1)** $\phi$ is Bernstein with Assumption 2.3 (so the subordinator law $\psi^\phi_t$ has no atom at $0$ and $V_\phi,\ I_\phi$ are well defined);
> **(H2)** $\gamma\in\mathcal P_X$, $m\ge1$, $L=m\ell_\gamma$.
> **Then**
> $$\mu^\phi_X\big(\mathcal C_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{e^{-u/4}\,e^{-L^2/(4u)}}{2\sqrt{\pi u}}\,V_\phi(du).\tag{21}$$

**Discharge.**

| step | apply | to | get |
|---|---|---|---|
| 1 | Theorem 3.2 specialised | $p^E\rightsquigarrow p^\phi$ | the double integral (19) |
| 2 | import (20) Wang–Xue at proper time $u$ | inner spatial integral $\int_{F_\tau}p_{\mathbb H^2}(u,w,\tau^m w)\,d\mathrm{vol}$ | $\tfrac{\ell_\gamma}{2\sinh(L/2)}\tfrac{e^{-u/4}e^{-L^2/(4u)}}{2\sqrt{\pi u}}$ |
| 3 | import Lemma 2.11 with $h(u)=\tfrac{e^{-u/4}e^{-L^2/(4u)}}{2\sqrt{\pi u}}$ | double $(t,u)$ integral against $\psi^\phi_t$, $dt/t$ | single integral against $V_\phi$ |

Every symbol is typed above; every predicate is an import or recall above. The block typechecks with nothing off-page.

> [!note]- Proof of Theorem 3.5 (skippable)
> Start from (19). The inner spatial integral is evaluated at each fixed proper time $u$ by the Wang–Xue strip identity (20), pulling the geometric factor $\tfrac{\ell_\gamma}{2\sinh(L/2)}$ out front and leaving $\tfrac{e^{-u/4}e^{-L^2/(4u)}}{2\sqrt{\pi u}}$ under the $\psi^\phi_t(du)$ integral:
> $$\mu^\phi_X\big(\mathcal C_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}\int_0^\infty\frac{dt}{t}\int_{[0,\infty)}\frac{e^{-u/4}e^{-L^2/(4u)}}{2\sqrt{\pi u}}\,\psi^\phi_t(du).\tag{22}$$
> Apply Lemma 2.11 with $h(u)=e^{-u/4}e^{-L^2/(4u)}/(2\sqrt{\pi u})$: the double integral against $\psi^\phi_t$ and $dt/t$ collapses to a single integral against $V_\phi$, giving (21). $\square$

The process-dependent factor is worth a name.

> **Definition 3.6 ($I_\phi$).** $\displaystyle I_\phi(L):=\int_0^\infty\frac{e^{-u/4}\,e^{-L^2/(4u)}}{2\sqrt{\pi u}}\,V_\phi(du)\in(0,\infty),\qquad L>0,\tag{23}$ so that Theorem 3.5 reads
> $$\mu^\phi_X\big(\mathcal C_X(\gamma^m)\big)=\frac{\ell_\gamma}{2\sinh(L/2)}\,I_\phi(L)=\frac1m\cdot\frac{L}{2\sinh(L/2)}\,I_\phi(L),\qquad L=m\ell_\gamma.\tag{24}$$

This (24) is the single import every later section consumes; **$I_\phi(L)$ is the only factor that depends on the process, all geometry sitting in the prefactor $\tfrac1m\tfrac{L}{2\sinh(L/2)}$.**

**The four special cases.** Each $V_\phi$ from the recall table feeds through (23), evaluated by the elementary Gaussian reciprocal integral.

**Used here — Gaussian reciprocal integral:** it turns every $I_\phi$ into a closed exponential; used twice here.
> [!import]- Gaussian reciprocal integral — Says / Needs / Gives
> **Says.** $\displaystyle\int_0^\infty u^{-3/2}e^{-au-b/u}\,du=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}.$ **Needs.** $a,b>0$. **Gives.** Closed form for every $I_\phi$; in §3 with $a=\tfrac14+\kappa$, $b=L^2/4$, so $2\sqrt{ab}=L\sqrt{\tfrac14+\kappa}$. Anchor-level (elementary); not a gap. Assume freely; nothing here re-proves it.

| $\phi(\lambda)$ | $V_\phi(du)$ | $I_\phi(L)$ | $\mu^\phi_X(\mathcal C_X(\gamma^m))$ | eq. |
|---|---|---|---|---|
| $\lambda$ (Brownian) | $du/u$ | $e^{-L/2}/L$ | $\dfrac1m\cdot\dfrac{1}{e^L-1}$ | — |
| $\lambda+\kappa$ (killing, $\kappa\ge-\tfrac14$) | $e^{-\kappa u}\,du/u$ | $e^{-L\sqrt{1/4+\kappa}}/L$ | $\dfrac1m\cdot\dfrac{e^{(\frac12-\sqrt{\frac14+\kappa})L}}{e^L-1}=\dfrac1m\dfrac{e^{(1-s)L}}{e^L-1}$ | (26) |
| $\lambda^{\alpha/2}$ ($\alpha$-stable, $\alpha\in(0,2)$) | $\tfrac\alpha2\,du/u$ | $\tfrac\alpha2\,e^{-L/2}/L$ | $\dfrac\alpha2\cdot\dfrac1m\cdot\dfrac1{e^L-1}$ | (27) |
| $(\lambda+\kappa)^{\alpha/2}$ (shifted stable) | $\tfrac\alpha2 e^{-\kappa u}\,du/u$ | $\tfrac\alpha2\,e^{-L\sqrt{1/4+\kappa}}/L$ | $\dfrac\alpha2\cdot\dfrac1m\cdot\dfrac{e^{(1-s)L}}{e^L-1}$ | (29) |

> [!note]- Verification of the killing row (26), from which the others follow (skippable)
> With $V_\phi(du)=e^{-\kappa u}\,du/u$, $\ I_\kappa(L)=\int_0^\infty\frac{e^{-(1/4+\kappa)u}e^{-L^2/(4u)}}{2\sqrt\pi\,u^{3/2}}\,du$. The Gaussian reciprocal integral at $a=\tfrac14+\kappa$, $b=\tfrac{L^2}4$ gives $\int_0^\infty u^{-3/2}e^{-au-b/u}du=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}=\tfrac{2\sqrt\pi}{L}e^{-L\sqrt{1/4+\kappa}}$, so $I_\kappa(L)=\tfrac1{2\sqrt\pi}\cdot\tfrac{2\sqrt\pi}{L}e^{-L\sqrt{1/4+\kappa}}=\tfrac{e^{-L\sqrt{1/4+\kappa}}}{L}$ (this is (25)). Then, using $\ell_\gamma/L=1/m$ and $2\sinh(L/2)=e^{L/2}-e^{-L/2}=e^{-L/2}(e^L-1)$, and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ so $\sqrt{\tfrac14+\kappa}=s-\tfrac12$:
> $$\mu^\kappa_X(\mathcal C_X(\gamma^m))=\frac{\ell_\gamma}{2\sinh(L/2)}\cdot\frac{e^{-L\sqrt{1/4+\kappa}}}{L}=\frac1m\cdot\frac{e^{-(s-1/2)L}}{e^{-L/2}(e^L-1)}=\frac1m\cdot\frac{e^{(1-s)L}}{e^L-1}.$$
> Brownian is $\kappa=0$ ($s=1$): $\mu_X(\mathcal C_X(\gamma^m))=\tfrac1m\tfrac1{e^L-1}$. The stable rows scale $V_\phi$ by $\tfrac\alpha2$, so $I_\phi=\tfrac\alpha2 I_{\mathrm{BM/killed}}$ and every mass acquires the factor $\tfrac\alpha2$. (The $\alpha$-stable collapse to a constant multiple of $du/u$ is forced: self-similar subordinators are exactly the stable ones, the weight $dt/t$ is itself scale-invariant, and the only measure on $(0,\infty)$ compatible with both scalings is a constant times $du/u$ — so the stable case yields no new geometry.)

> [!warning] Remark 3.7 — why the range is $\kappa\ge-\tfrac14$, below the Bernstein regime
> For $\kappa>0$, $\mu^\kappa_X$ is the mass of the Brownian loop measure with constant killing rate $\kappa$ (the process's generator is the Schrödinger operator $\Delta_{\mathbb H^2}+\kappa$, not the Laplacian). For $\kappa\in[-\tfrac14,0)$ the function $\phi(\lambda)=\lambda+\kappa$ is **no longer Bernstein** (its killing rate $a=\kappa$ is negative), so Theorem 3.5's hypothesis (H1) fails — yet the closed formula (26) and the integral (25) continue to converge and are used anyway. Writing $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, the condition $\kappa\ge-\tfrac14$ is exactly what keeps $s$ real; at $\kappa=-\tfrac14$, $s=\tfrac12$, the bottom of the $L^2$-spectrum of $\Delta_{\mathbb H^2}$. This is the widest range over which $\mu^\kappa_X$ makes sense, and Proposition 3.11's strict monotonicity holds uniformly down to it.

## §3.2  Euclidean-quantum-mechanics digression

The paper pauses to read the killing loop measure as a physical object. Nothing later in the paper consumes it, so it is folded whole.

> [!note]- §3.2 Euclidean-QM digression (a dictionary; no later result uses it)
> After Wick rotation $t=-i\tau$, the Schrödinger unitary group $e^{-it\hat H/\hbar}$ of a particle with Hamiltonian $\hat H=\Delta_X+V$ becomes the contraction semigroup $e^{-t\hat H}$ (well-defined for $t\ge0$ since $\hat H\ge0$), whose Euclidean time $t$ is the diffusion time of §2. In units $\hbar^2/2m=1$ its kernel $p_V(t,x,y)$ is the transition density of Brownian motion **killed at rate $V$**, given by the **Feynman–Kac formula**
> $$p_V(t,x,y)=\int_{C([0,t];X)}e^{-\int_0^t V(\omega(r))\,dr}\,W^t_{x\to y}(d\omega),$$
> each Brownian bridge weighted by its survival probability against the killing. For $V\equiv\kappa$ the weight is $e^{-\kappa t}$, giving $p_\kappa(t,x,y)=e^{-\kappa t}p(t,x,y)$ — exactly the killing kernel of §2. So $\mu^\kappa_X$ is the intensity of the loop ensemble of a Euclidean quantum particle in a constant potential (the loop soup of §3.3). Feynman–Kac is the rigorous form of the path integral $\int\mathcal D\omega\,e^{-S[\omega]}$ with action $S[\omega]=\int_0^t\big(\tfrac14|\dot\omega|^2+V(\omega)\big)dr$: kinetic part in the bridge measure, potential part in the weight; $\mathcal D\omega$ is the (non-existent) formal Lebesgue measure on paths.
> **Looking ahead to §5.** For a free scalar field of mass $\sqrt\kappa$ ($\kappa=m^2>0$) with quadratic Euclidean action $S_E[\phi]=\tfrac12\langle\phi,(\Delta_X+\kappa)\phi\rangle$, the Gaussian path integral is $Z^\kappa_X=\int\mathcal D\phi\,e^{-S_E[\phi]}\propto\det(\Delta_X+\kappa)^{-1/2}$, so the one-loop effective action is $\Gamma^{(1)}_X(\kappa)=-\log Z^\kappa_X=\tfrac12\log\det(\Delta_X+\kappa)$. The Schwinger proper-time representation
> $$-\log\det(\Delta_X+\kappa)=\int_0^\infty\frac{dt}{t}\,e^{-\kappa t}\,\mathrm{Tr}\big(e^{-t\Delta_X}\big),\qquad\mathrm{Tr}(e^{-t\Delta_X})=\int_X p(t,x,x)\,d\mathrm{vol}(x),$$
> is built from Brownian paths that start and return to the same point, integrated with the Haar weight $dt/t$ and the killing weight $e^{-\kappa t}$ — precisely the structure of the killing loop measure. So $-\log\det(\Delta_X+\kappa)=\big(\mu^\kappa_X\big)_{\mathrm{reg}}$, the regularised total mass over **all** loops (including the divergent contractible and peripheral contributions), and $Z^\kappa_X\propto\exp(\tfrac12(\mu^\kappa_X)_{\mathrm{reg}})$: the partition function of a free real scalar field of mass $\sqrt\kappa$ is the exponential of half the regularised total loop mass with killing $\kappa$. Divergent as written; §5 makes it rigorous via zeta regularisation.

## §3.3  The loop soup and its Poissonian structure

Every class mass is a non-negative number; a $\sigma$-finite measure can be the intensity of a Poisson point process. Promoting $\mu^\phi_X$ this way turns the masses from expectations into an actual random collection of loops, so one may speak of the distribution of topological quantities, not only their means.

**New symbols.** $\mathcal L_c$ (loop soup), $c$ (intensity), $N_A$ (count in a set $A$), the marking $(B,S)$.

**Poisson point process.** A **Poisson point process** with $\sigma$-finite intensity measure $\Lambda$ on a space is a random countable set of points such that, for each measurable $A$ with $\Lambda(A)<\infty$, the count $N_A\sim\mathrm{Poisson}(\Lambda(A))$, and counts over disjoint sets are independent. Following Lawler–Werner, the **loop soup** $\mathcal L_c$ is the Poisson point process of loops on $X$ with intensity $c\mu^\phi_X$ ($c>0$): a random countable collection of loops.

**Used here — the count of a class:** distinct classes are disjoint measurable sets, so their loop-counts are independent Poissons.
> [!import]- Poisson point process facts — Says / Needs / Gives
> **Says.** For a $\sigma$-finite intensity $c\mu^\phi_X$ and measurable $A$ with $\mu^\phi_X(A)<\infty$: $N_A:=\#\{\eta\in\mathcal L_c:\eta\in A\}\sim\mathrm{Poisson}(c\mu^\phi_X(A))$; for pairwise disjoint $A_1,\dots,A_k$ the counts $N_{A_1},\dots,N_{A_k}$ are jointly independent. **Needs.** $c\mu^\phi_X$ $\sigma$-finite (§2) and each $\mu^\phi_X(A)<\infty$ (Theorem 3.5 for $A=\mathcal C_X(\gamma^m)$). **Gives.** Every class mass is the mean of a Poisson variable, and distinct classes are independent. Anchor-level (Poisson process theory); not a gap. Assume freely; nothing here re-proves it.

> **Proposition 3.8 (Poissonian structure of homotopy classes).** For $\gamma\in\mathcal P_X$, $m\ge1$, the number $N_{\gamma,m}$ of loops of $\mathcal L_c$ in the class $\mathcal C_X(\gamma^m)$ is $\mathrm{Poisson}\big(c\,\mu^\phi_X(\mathcal C_X(\gamma^m))\big)$; and for any finite collection of pairwise distinct classes these counts are jointly independent.

**Discharge.**

| step | apply | to | get |
|---|---|---|---|
| 1 | Theorem 3.5 (24) | $A=\mathcal C_X(\gamma^m)$ | $\mu^\phi_X(A)\in(0,\infty)$, finite |
| 2 | PPP facts, count | $N_{\gamma,m}=N_A$ | $\sim\mathrm{Poisson}(c\mu^\phi_X(\mathcal C_X(\gamma^m)))$ |
| 3 | distinct classes disjoint | $\mathcal C_X(\gamma^m)\cap\mathcal C_X(\gamma'^{m'})=\varnothing$ | joint independence |

Every symbol is typed above; the block typechecks with nothing off-page.

> [!note]- Proof of Proposition 3.8 (skippable)
> Distinct free-homotopy classes are disjoint measurable sets of loops, and each has finite mass by Theorem 3.5. Both statements are then immediate from the defining properties of a Poisson point process with intensity $c\mu^\phi_X$: the count in a finite-mass set is Poisson with mean the intensity of the set, and counts over disjoint sets are independent. $\square$

> [!warning] When $\phi$ has jumps, the class needs marking
> For a jump process (e.g. an $\alpha$-stable $\phi$) the loops are càdlàg and the set $\mathcal C_X(\gamma^m)$ is **not** measurable as a set of raw loops — a jumping loop can change homotopy type discontinuously. One then takes $\mathcal L_c$ to be the Poisson point process of **marked** loops carrying the pair $(B,S)$ (the underlying Brownian trajectory $B$ and its subordinating clock $S$), on which the monodromy class **is** measurable and has the same intensity $c\mu^\phi_X(\mathcal C_X(\gamma^m))$. In the diffusion cases ($\phi=\lambda,\lambda+\kappa$) no marking is needed.

**Used here — the exponential formula:** it computes the Laplace/character transform of any additive functional of the soup; §6 uses it with $F=\log\chi([\eta])$ to get the law of the total homology.
> [!import]- Exponential (Campbell) formula for a Poisson point process — Says / Needs / Gives
> **Says.** For a Poisson point process with intensity $\nu=c\mu^\phi_X$ and measurable $F$ with $\int(e^{F}-1)\wedge|F|\,d\nu<\infty$: $\displaystyle\mathbb E\Big[\prod_{\eta\in\mathcal L_c}e^{F(\eta)}\Big]=\exp\Big(\int(e^{F(\eta)}-1)\,\nu(d\eta)\Big).$ **Needs.** $\nu$ $\sigma$-finite; the integrability above. **Gives.** The generating functional of any additive statistic $\sum_\eta F(\eta)$ of the soup in one closed exponential. Anchor-level (Campbell's theorem); not a gap. Assume freely; nothing here re-proves it. Exported to §6.

## §3.4  Length-spectrum identities and rigidity

The masses computed in §3.1 are not just convenient numbers: they already encode the surface's geometry. Two Brownian invariances — restriction and conformal invariance — give an identity between length spectra of different surfaces; and the killing masses are strictly monotone in the geodesic length, so they invert to recover it.

**New symbols.** $P$ (polar set), $\mathrm{MLS}$ (marked length spectrum), $g_1,g_2$ (two hyperbolic metrics on the same $X$).

**Polar set.** A Borel set $P\subset X$ is **polar** for a process if from every starting point the process almost surely never hits $P$ at a positive time: $\mathbb P_x(T_P<\infty)=0$ for all $x$, where $T_P$ is the hitting time. For Brownian motion on a Riemann surface this holds exactly when $P$ has **zero logarithmic capacity** in every local chart; in particular every singleton is polar, polar sets form a $\sigma$-ideal (closed under subsets and countable unions), so every countable set is polar. A killing rate changes only the clock, not the paths, so for $\phi(\lambda)=\lambda+\kappa$ the polar sets are still Brownian. Take $P$ a closed discrete set — countable, hence polar.

**Restriction and conformal invariance.** Two structural properties of the Brownian loop measure: **restriction** (the measure of a set of loops avoiding $P$ is unchanged by deleting $P$) and **conformal invariance** (invariance under conformal changes of metric). Because $\mu^\kappa_X$ is supported on loops avoiding the polar $P$, restriction gives $\mu^\kappa_{X,g}(\mathcal C_X(\gamma^m))=\mu^\kappa_{X\setminus P,g}(\mathcal C_X(\gamma^m))$, where $g$ on the right is the ambient metric **restricted** to $X\setminus P$ (not the complete hyperbolic metric of the punctured surface). For subordinate processes with jumps this is the whole story — a conformal change $g'=e^{2\sigma}g$ rescales the Laplacian, $\Delta_{X,g'}=e^{-2\sigma}\Delta_{X,g}$, but $\phi$ does not commute with that rescaling ($\phi(e^{-2\sigma}\Delta)\neq e^{-2\sigma}\phi(\Delta)$) unless $\phi(\lambda)=c\lambda$, so only a trivial form of the identity survives. For genuine Brownian motion conformal invariance lets one replace $g$ on $X\setminus P$ by the **unique complete hyperbolic metric** $g'$ (a cusp at each point of $P$), and the identity becomes a comparison of the two length spectra.

**Used here — Wang–Xue length identity:** it equates the Brownian class mass on $X$ to a sum of masses over homotopic classes on the punctured surface $X'=X\setminus P$, relating their length spectra.
> [!import]- (Theorem 3.9) Wang–Xue length-spectrum identity [WX25, Thm 4.2] — Says / Needs / Gives  [genuine gap of §3]
> **Says.** For a complete hyperbolic surface $X$ (possibly infinite type, with **cusps** — ends of finite area shrinking to zero width — or **funnels** — flaring ends of infinite area), a non-empty closed polar set $P\subset X$, and $X'=X\setminus P$ with its unique complete hyperbolic metric: for $\gamma\in\mathcal P_X$, $m\ge1$,
> $$\frac1m\cdot\frac1{e^{m\ell_\gamma}-1}=\sum_{\substack{\gamma'\in\mathcal P_{X'},\,m'\ge1\\ \gamma'^{m'}\simeq_X\gamma^m}}\frac1{m'}\cdot\frac1{e^{m'\ell_{\gamma'}}-1},$$
> where $\simeq_X$ is free homotopy as curves in $X$, and $\ell_\gamma,\ell_{\gamma'}$ are primitive lengths measured on $X$ and $X'$. **Needs.** $P$ closed, non-empty, polar. **Gives.** The Brownian class mass on $X$ equals the total Brownian mass of all $X'$-classes homotopic to it in $X$ — a length-spectrum comparison across the puncturing. **Status:** not proved here; imported from [WX25, Thm 4.2]. Assume freely.

**Marked length spectrum.** Write $\ell_g(\eta)$ for the length of a loop $\eta$ in the metric $g$. The **marked length spectrum** of $(X,g)$ is $\mathrm{MLS}:\mathcal C_X(\gamma^m)\mapsto\inf_{\eta\in\mathcal C_X(\gamma^m)}\ell_g(\eta)$, assigning to each non-trivial free-homotopy class the infimum length in it; on a hyperbolic surface the infimum is attained by the unique closed geodesic, so $\mathrm{MLS}(\mathcal C_X(\gamma^m))=m\ell_\gamma$. The **marking** — the record of *which* class realises *which* length — is strictly stronger than the multiset of lengths: there exist non-isometric hyperbolic surfaces (Vignéras) whose length multisets agree, so bare lengths do not determine $X$, while the marked function does (in $2$D, by Otal–Croke).

> **Proposition 3.11 (loop masses recover the marked length spectrum).** For every $\gamma\in\mathcal P_X$:
> $$\ell_\gamma=\log\Big(1+\frac1{\mu_X(\mathcal C_X(\gamma))}\Big).\tag{30}$$
> Moreover, for $\phi(\lambda)=\lambda+\kappa$ with $\kappa\ge-\tfrac14$, the mass $\mu^\kappa_X(\mathcal C_X(\gamma))$ is a strictly decreasing function of $\ell_\gamma$, hence again determines it. Both hold for every $m\ge1$, so in either case the loop masses determine $\mathrm{MLS}$.

**Discharge.**

| step | apply | to | get |
|---|---|---|---|
| 1 | Brownian row of §3.1 at $m=1$ | $\mu_X(\mathcal C_X(\gamma))=1/(e^{\ell_\gamma}-1)$ | invertible for $\ell_\gamma$ |
| 2 | solve for $\ell_\gamma$ | $e^{\ell_\gamma}-1=1/\mu_X$ | $\ell_\gamma=\log(1+1/\mu_X(\mathcal C_X(\gamma)))$ |
| 3 | killing row (26) at $m=1$, log-derivative in $\ell_\gamma$ | $\big(\tfrac12-\sqrt{\tfrac14+\kappa}\big)-\tfrac{e^{\ell_\gamma}}{e^{\ell_\gamma}-1}$ | $<\tfrac12-1<0$, strictly decreasing |

Every symbol is typed above; the block typechecks with nothing off-page.

> [!note]- Proof of Proposition 3.11 (skippable)
> By the Brownian row of §3.1 at $m=1$, $\mu_X(\mathcal C_X(\gamma))=1/(e^{\ell_\gamma}-1)$; solving gives $e^{\ell_\gamma}=1+1/\mu_X(\mathcal C_X(\gamma))$, i.e. (30). For $\phi=\lambda+\kappa$, (26) at $m=1$ gives $\mu^\kappa_X(\mathcal C_X(\gamma))=e^{(\frac12-\sqrt{\frac14+\kappa})\ell_\gamma}/(e^{\ell_\gamma}-1)$; its logarithmic derivative in $\ell_\gamma$ is
> $$\frac{d}{d\ell_\gamma}\Big[\big(\tfrac12-\sqrt{\tfrac14+\kappa}\big)\ell_\gamma-\log(e^{\ell_\gamma}-1)\Big]=\Big(\tfrac12-\sqrt{\tfrac14+\kappa}\Big)-\frac{e^{\ell_\gamma}}{e^{\ell_\gamma}-1}<\tfrac12-1<0,$$
> since $\sqrt{\tfrac14+\kappa}\ge0$ makes the first term $\le\tfrac12$ and $e^{\ell_\gamma}/(e^{\ell_\gamma}-1)>1$; the bound is uniform down to $\kappa=-\tfrac14$. Strict monotonicity gives injectivity, so the mass determines $\ell_\gamma$. The same computation applies for every $m\ge1$. $\square$

**Used here — Otal–Croke rigidity:** it upgrades "same marked length spectrum" to "isometric" in dimension $2$; the last step of Corollary 3.12.
> [!import]- (Otal–Croke) Marked-length-spectrum rigidity in $2$D — Says / Needs / Gives  [genuine gap of §3]
> **Says.** Two negatively curved metrics on a closed surface with the same marked length spectrum are isometric by an isometry isotopic to the identity. **Needs.** Closed surface; both metrics negatively curved (hyperbolic metrics qualify); equal $\mathrm{MLS}$ with the identity marking. **Gives.** Equal marked length spectra $\Rightarrow$ same point of Teichmüller space. **Status:** not proved here; the $2$D case of the Burns–Katok conjecture, proved by Otal and by Croke. Assume freely.

> **Corollary 3.12 (loop masses determine the hyperbolic surface).** Let $X$ be a closed hyperbolic surface, $g_1,g_2$ hyperbolic metrics on $X$, $\kappa\ge-\tfrac14$. If $\mu^\kappa_{X,g_1}(\mathcal C_X(\gamma^m))=\mu^\kappa_{X,g_2}(\mathcal C_X(\gamma^m))$ for every free-homotopy class $\mathcal C_X(\gamma^m)$, then $(X,g_1)$ and $(X,g_2)$ are isometric by an isometry **isotopic to the identity** (deformable to $\mathrm{id}_X$ through a continuous family of diffeomorphisms) — equivalently, $g_1$ and $g_2$ are **the same point of Teichmüller space** $\mathcal T(X)$ (the set of hyperbolic metrics on $X$ modulo diffeomorphisms isotopic to $\mathrm{id}_X$; "same point" is just a restatement of "isometric via an isometry isotopic to $\mathrm{id}_X$").

**Discharge.**

| step | apply | to | get |
|---|---|---|---|
| 1 | Proposition 3.11 to each metric | equal masses per class | equal $\ell_\gamma$ per class, i.e. equal $\mathrm{MLS}$ with identity marking |
| 2 | import Otal–Croke | equal $\mathrm{MLS}$, hyperbolic (negatively curved) metrics | isometry isotopic to the identity |
| 3 | Teichmüller | isometry isotopic to identity | same point of Teichmüller space |

Every symbol is typed above; the block typechecks with nothing off-page.

> [!note]- Proof of Corollary 3.12 (skippable)
> By Proposition 3.11 the mass in each free-homotopy class determines the length of that class's geodesic representative, so the hypothesis forces $g_1$ and $g_2$ to have the same marked length spectrum, with the identity marking. Hyperbolic metrics are negatively curved, so Otal–Croke gives an isometry between $(X,g_1)$ and $(X,g_2)$ homotopic — hence isotopic — to the identity; the two metrics therefore define the same point of Teichmüller space. $\square$

# D. Exports, climb, commentary

**Exports (what later sections consume from §3).**
- **(E24)** the class-mass formula (24): $\mu^\phi_X(\mathcal C_X(\gamma^m))=\tfrac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)=\tfrac1m\tfrac{L}{2\sinh(L/2)}I_\phi(L)$, and its four closed values (Brownian $\tfrac1m\tfrac1{e^L-1}$; killing $\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$; stable $\tfrac\alpha2\times$). → §4 (summed into $-\log Z_X$), §5, §6, §7.
- **(E-soup)** the loop soup $\mathcal L_c$, the Poissonian independence of class-counts (Prop 3.8), and the exponential formula. → §6 (the law of the loop soup's total homology).
- **(E-mls)** loop masses $\mapsto$ marked length spectrum $\mapsto$ rigidity (Prop 3.11, Cor 3.12): a self-contained coda showing the masses already determine the surface.

**Climb (optional — none is needed to typecheck §3).** Sibling sections and the ledgers: [[§2 The Loop Measure and Subordination]] · [[§4 Zeta Identities and Finiteness]] · [[§5 Determinants and the Polyakov Anomaly]] · [[§6 Probability on Homotopy and Homology Classes]] · [[§7 Hyperbolic 3-Manifolds]] · [[External Inputs and Gaps]] · [[Anchors and Prerequisites]]. All deletable with zero loss to the typecheck above.

> [!note]- Commentary (skippable)
> The engine of §3 is a single change of viewpoint: a loop in a homotopy class is a path in $\mathbb H^2$ between a point and a specified $\Gamma$-translate of it, so computing the class mass means integrating the upstairs heat kernel over the right coset of the deck group. Everything geometric — that the centraliser of $\tau^m$ is just $\langle\tau\rangle$, that $\tau$ is conjugate to a clean dilation $z\mapsto e^{\ell_\gamma}z$, that its fundamental strip is the annulus $1\le\operatorname{Im}z<e^{\ell_\gamma}$ — is in service of turning a coset sum into one strip integral (Theorem 3.2). The one thing that is genuinely hard, and genuinely imported, is the strip integral itself: the $\mathbb H^2$ heat kernel has no elementary closed form, so Wang–Xue's evaluation is a black box. Notice how cleanly it factors — geometry $\tfrac{\ell_\gamma}{2\sinh(L/2)}$ times a bare Euclidean Gaussian in the proper time — and how that factorisation is exactly what lets Lemma 2.11 fold the two time integrals into the single $I_\phi(L)$. The four processes then differ only through $V_\phi$, and $I_\phi$ closes in one line via the Gaussian reciprocal integral.
>
> The killing shape $\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$ is the paper's protagonist: §4 recognises its sum over classes as $-\log Z_X(s)$, and the mechanism is that the $\sinh$ in the prefactor manufactures precisely the $e^{L}-1$ denominator that the Selberg product wants. What breaks the pattern is loss of scale-invariance: the pure $\alpha$-stable case collapses to a constant multiple of Brownian because $dt/t$ and the stable subordinator share a scaling, forcing $V_\phi\propto du/u$ and hiding all geometry; the way to something new is to break that symmetry (shift by $\kappa$). And the coda (§3.4) is a reminder that these numbers are not arbitrary: for the diffusion cases the map class $\mapsto$ mass is injective in the geodesic length, so the masses recover the marked length spectrum, and by Otal–Croke — the one deep rigidity input — the metric itself. The masses of Brownian loops see the whole hyperbolic structure. What does **not** transfer is anything using conformal invariance under a genuine metric change: subordination does not commute with the conformal rescaling of $\Delta$, so §3.4's strong length identity survives only for pure Brownian motion.