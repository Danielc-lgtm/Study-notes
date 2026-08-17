---
type: paper-section
paper: "BH26"
subject: brownian-loops
section: "5"
tags: [paper, section, self-contained]
---

> [!info] Part of [[Map - Brownian Loops on Homotopy and Homology Classes]]. Self-contained: every symbol, predicate and imported result used below is written out on this page. Grey callouts are folds on THIS page — opening one is a scroll, not a jump to another file. You can typecheck §5 front-to-back without opening anything else.

**What §5 buys you.** §4 found the total loop mass equals $-\log Z_X(s)$ when it converges, and diverges exactly when a finite-area surface is run with zero killing ($s=\delta=1$). §5 renormalises that divergence: it identifies the regularised total Brownian loop mass with $\log\det_\zeta\Delta_X$ (the zeta-regularised determinant of the Laplacian), reads off the closed-form $\log\det_\zeta\Delta_X=\mathrm{Area}(X)E+\log Z_X'(1)$ on a closed surface via the $\kappa\to0^+$ cancellation of two $\log\kappa$ terms, transports the transformation law under conformal rescaling from Polyakov's anomaly formula, and extends the whole picture to cusped surfaces where the spectrum is no longer discrete (a renormalised $0$-trace replaces the trace, Borthwick–Judge–Perry replaces D'Hoker–Phong).

# A. Standing setup

Everything in §5 lives on a fixed hyperbolic surface $X$ and concerns the *total* mass its loop measure assigns to all non-trivial classes, packaged as a spectral determinant. The paragraphs below fix those objects inline, so that dropping straight into §5 needs nothing from earlier sections. §5.1 assumes $X$ **closed** (compact, no boundary); §5.2 relaxes to **geometrically finite** (cusps and/or funnels allowed).

**The surface.** $\Gamma\subseteq\mathrm{PSL}(2,\mathbb R)$ is a discrete, torsion-free group of isometries of the hyperbolic plane $\mathbb H^2$ (upper half-plane $\{z:\operatorname{Im}z>0\}$, metric $|dz|/\operatorname{Im}z$), acting **freely** — $\forall h\in\Gamma\setminus\{1\}\ \forall z\in\mathbb H^2:\ hz\neq z$ (no non-identity isometry fixes a point) — and **properly discontinuously** — $\forall K\Subset\mathbb H^2:\ \#\{h\in\Gamma:\ hK\cap K\neq\varnothing\}<\infty$ (each compact set meets only finitely many of its $\Gamma$-translates). Under exactly these two conditions the quotient $X=\Gamma\backslash\mathbb H^2$ (points of $\mathbb H^2$ glued when one is a $\Gamma$-image of the other) is a smooth hyperbolic surface and $\pi:\mathbb H^2\to X$ is a **covering map** (a local isometry under which $\mathbb H^2$ wraps around $X$) with **deck group** $\Gamma\cong\pi_1(X)$ (the isometries permuting the sheets over each point). $X$ is **geometrically finite**: $\Gamma$ finitely generated, equivalently $X$ has a finite-sided fundamental polygon. A **closed** surface has genus $g$, Euler characteristic $\chi(X)=2-2g<0$, and (constant curvature $-1$, Gauss–Bonnet) area $\mathrm{Area}(X)=-2\pi\chi(X)=4\pi(g-1)$. A finite-area non-compact surface has finitely many **cusps** — ends isometric to a shrinking horn $\{y>c\}/(z\mapsto z+1)$, exponentially thin funnels of infinite geometric depth but finite volume; $n_C$ counts them. An infinite-area surface additionally has **funnels** — flaring ends of infinite area.

**Geodesics and their classes.** A closed geodesic $\gamma$ is **primitive** if it is not a repeated traversal of a shorter one — its representative $\tau\in\Gamma$ satisfies $\tau=\sigma^k\ (\sigma\in\Gamma,\,k\ge1)\Rightarrow k=1$. Write $\mathcal P_X$ for the primitive oriented closed geodesics, $\ell_\gamma:=\min_z d(z,\tau z)>0$ for the length of $\gamma$ (the **translation length** of $\tau$), and $\mathcal G(X)$ for **all** oriented closed geodesics. Every closed geodesic is the $m$-fold iterate $\gamma^m$ of a unique primitive $\gamma$, of length $L:=m\ell_\gamma$; so $\mathcal G(X)\setminus\mathcal P_X$ is exactly the geodesics with $m\ge2$. Free-homotopy classes of loops correspond bijectively to conjugacy classes $[h]=\{qhq^{-1}:q\in\Gamma\}$ in $\Gamma$, and — restricting to **non-trivial, non-peripheral** classes — to pairs $(\gamma,m)\in\mathcal P_X\times\mathbb Z_{\ge1}$: $\mathcal C_X(\gamma^m)$ is the class winding $m$ times around $\gamma$, i.e. the conjugacy class $[\tau^m]$.

**The Laplacian and its loop measure.** $\Delta_X$ is the (positive) Laplace–Beltrami operator on $X$; on a **closed** surface its spectrum is a discrete increasing sequence $0=\lambda_0<\lambda_1\le\lambda_2\le\cdots$ (the zero eigenvalue simple, eigenfunctions constant) with **Weyl's law** $\lambda_j\sim4\pi j/\mathrm{Area}(X)$ (the $j$-th eigenvalue grows linearly at that rate). $\mu^\phi_X$ is the $\phi$-subordinate Brownian **loop measure** on unrooted, unparametrised, oriented loops: a $\sigma$-finite measure of **infinite** total mass, whose value on one class, $\mu^\phi_X(\mathcal C_X(\gamma^m))\in(0,\infty)$, was computed in §3. §5 studies the *sum* of those values, which §4 showed to be $-\log Z_X(s)$ where finite, and $\infty$ (finite area, $\kappa=0$) where it must be renormalised.

**Notation for §5.**

| symbol | type |
|---|---|
| $X=\Gamma\backslash\mathbb H^2$ | hyperbolic surface; §5.1 closed, §5.2 geometrically finite |
| $g,\ \chi(X),\ \mathrm{Area}(X)$ | genus; $\chi=2-2g$; $\mathrm{Area}=-2\pi\chi=4\pi(g-1)$ (closed) |
| $n_C$ | number of cusps (finite-area non-compact case) |
| $\Delta_X$ | positive Laplacian; $\operatorname{spec}\Delta_X\subseteq[0,\infty)$ |
| $\lambda_j$ | eigenvalues (closed): $0=\lambda_0<\lambda_1\le\cdots$, $\lambda_j\sim4\pi j/\mathrm{Area}(X)$ |
| $\zeta_X(s)$ | spectral zeta $\sum_{j\ge1}\lambda_j^{-s}$, $\operatorname{Re}s>1$; continued to $\mathbb C$ |
| $\det_\zeta\Delta_X$ | zeta-regularised determinant, $\log\det_\zeta\Delta_X:=-\zeta_X'(0)$ ($\lambda_0=0$ excluded) |
| $\det_0\Delta_X$ | renormalised determinant on a cusped surface (§5.2) |
| $\zeta_R,\ \zeta_R'(-1)$ | Riemann zeta; its derivative at $-1$, $\approx-0.1654$ |
| $E$ | $(4\zeta_R'(-1)-\tfrac12+\log2\pi)/(4\pi)\approx0.0538$ |
| $\gamma_{\mathrm{EM}}$ | Euler–Mascheroni constant $\approx0.5772$ |
| $Z_X,\ \delta$ | Selberg zeta $\{\operatorname{Re}s>\delta\}\to\mathbb C$; critical exponent $\in(0,1]$ (recalls below) |
| $s,\ \kappa$ | spectral parameter $s=\tfrac12+\sqrt{\tfrac14+\kappa}$; killing $\kappa\ge-\tfrac14$, $\kappa=s(s-1)$ |
| $t,\ u$ | loop duration (integrated $dt/t$); subordination/proper time (in $I_\phi,V_\phi$) |
| $m,\ L,\ \ell_\gamma$ | $m\in\mathbb Z_{\ge1}$; $L=m\ell_\gamma$; primitive length |
| $\mathcal P_X,\ \mathcal G(X)$ | primitive / all oriented closed geodesics; $\mathcal G(X)\setminus\mathcal P_X\leftrightarrow m\ge2$ |
| $\mathcal C_X(\gamma^m)$ | free-homotopy class $=[\tau^m]$; a measurable set of loops |
| $\mu_X,\mu^\kappa_X,\mu^\phi_X$ | Brownian / killed / subordinate loop measures; $\mu^\phi_X(\mathcal C_X(\gamma^m))\in(0,\infty)$ |
| $\phi,\ I_\phi,\ V_\phi$ | Bernstein function; its heat-kernel integral; its potential measure (recalls below) |
| $S_X(t),\ S^{\mathrm p}_X(t)$ | geometric heat-trace term; its primitive ($m=1$) part |
| $N_X(R)$ | $\#\{\gamma\in\mathcal P_X:\ell_\gamma\le R\}<\infty$ |
| $\operatorname{Li},\ \widetilde{\operatorname{Li}}$ | $\operatorname{Li}(x)=\int_2^x dt/\log t$; cutoff $\widetilde{\operatorname{Li}}(x)=\operatorname{Li}(x)\mathbf 1_{x\ge2}$ |
| $x,\ {}^0\!\!\int_X,\ {}^0\mathrm{Tr}$ | boundary-defining function; renormalised integral; $0$-trace (§5.2) |
| $\zeta^0_X,\ P,\ R_X(s)$ | renormalised spectral zeta; $L^2$-null projection; resolvent $(\Delta_X-s(1-s))^{-1}$ |
| $M,\ F,\ D_X(s),\ C_X$ | Borthwick–Judge–Perry constants/factors; $C_X=e^M(2\pi)^{-\chi}(\sqrt{2\pi})^{-n_C}$ |
| $\sigma,\ P_X(\sigma),\ K_0$ | conformal factor $g=e^{2\sigma}g_0$; Polyakov correction; Gauss curvature of $g_0$ |

**Standing conventions.** $\Delta_X\ge0$ (geometer's sign; $\operatorname{spec}\Delta_X\subseteq[0,\infty)$); Brownian motion at speed $2$ (generator $-\Delta_X$). Three time-like variables are kept typographically distinct, deviating from the paper's single "$s$": the **spectral parameter** $s$; the **subordination / proper-time** variable $u$ (integrated in $I_\phi$ and $V_\phi$); the **loop duration** $t$ (integrated $\mathrm{d}t/t$). Spectral $s$ and killing $\kappa$ are linked by $s=\tfrac12+\sqrt{\tfrac14+\kappa}\iff\kappa=s(s-1)$, with $\kappa\ge-\tfrac14$ (at $\kappa=-\tfrac14$, $s=\tfrac12=\inf\operatorname{spec}\Delta_{\mathbb H^2}$). **Total mass** always means the sum over **non-trivial, non-peripheral** free-homotopy classes: the trivial (contractible) class carries infinite mass and is excluded, and peripheral (cusp) classes have no closed geodesic and are excluded.

Objects built in earlier sections that §5 uses only through an end-formula are folded here, so nothing is off-page.

**Used here — $Z_X$ and its logarithm:** §5 uses only that the total mass is $-\log Z_X(s)$ (its $-\log$ expansion) and that $Z_X$ has a simple zero at $s=1$ on a finite-area surface (from $\lambda_0=0$).
> [!recall]- $Z_X$, the Selberg zeta function, and the $-\log Z_X$ expansion (F1) [home §4]
> $\displaystyle Z_X(s):=\prod_{\gamma\in\mathcal P_X}\prod_{k=0}^\infty\big(1-e^{-(s+k)\ell_\gamma}\big),\quad\operatorname{Re}s>\delta$ (a double product: outer over primitive geodesics = the "primes", inner over $k\ge0$). Its logarithm is elementary:
> $$-\log Z_X(s)=\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\frac1m\cdot\frac{e^{(1-s)L}}{e^L-1}\Big|_{L=m\ell_\gamma},\qquad\operatorname{Re}s>\delta.$$
> (Apply $-\log(1-x)=\sum_{m\ge1}x^m/m$ to each factor, then the inner geometric series $\sum_{k\ge0}e^{-(s+k)m\ell_\gamma}=e^{(1-s)L}/(e^L-1)$.) On a **finite-area** surface $\lambda_0=0$ forces $Z_X$ a **simple zero at $s=1$**: $Z_X(s)=Z_X'(1)(s-1)+O((s-1)^2)$, so $-\log Z_X(s)=-\log Z_X'(1)-\log(s-1)+O(s-1)$.

**Used here — the critical exponent $\delta$:** §5 uses only the dichotomy $\delta=1\iff\mathrm{Area}(X)<\infty$ (so finite-area $\Rightarrow s>\delta$ needs $\kappa>0$; infinite-area $\Rightarrow\delta<1$ and $s=1>\delta$ already works).
> [!recall]- $\delta$, the critical exponent [home §4]
> $\displaystyle\delta:=\inf\{s>0:\sum_{h\in\Gamma}e^{-s\,d(z,hz)}<\infty\}\in(0,1]$ (abscissa of convergence of the Poincaré series; base-point independent) is the exponential growth rate of closed geodesics, $N_X(R)\sim e^{\delta R}/(\delta R)$, and $\delta=1\iff\operatorname{area}(X)<\infty$.

**Used here — the class mass (24):** §5 uses the closed value of each class mass, and in the Brownian case its collapse $\int_0^\infty\frac{dt}t\frac{e^{-t/4}}{\sqrt{4\pi t}}\frac{\ell_\gamma}{2\sinh(L/2)}e^{-L^2/4t}=\frac1m\frac1{e^L-1}$.
> [!recall]- Class mass $\mu^\phi_X(\mathcal C_X(\gamma^m))$ and its killed value [home §3, Thm 3.5]
> $\displaystyle\mu^\phi_X(\mathcal C_X(\gamma^m))=\frac{\ell_\gamma}{2\sinh(L/2)}I_\phi(L)=\frac1m\cdot\frac L{2\sinh(L/2)}I_\phi(L)$, where $I_\phi(L)=\int_0^\infty\frac{e^{-u/4}e^{-L^2/(4u)}}{2\sqrt{\pi u}}V_\phi(du)$ integrates the speed-$2$ mass-shifted $\mathbb H^2$ heat kernel against the potential measure $V_\phi$. For **killing $\kappa$** ($V_\phi=e^{-\kappa u}du/u$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$): $\mu^\kappa_X(\mathcal C_X(\gamma^m))=\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$. For **Brownian** ($\kappa=0$, $s=1$): $\mu_X(\mathcal C_X(\gamma^m))=\tfrac1m\tfrac1{e^L-1}$. For **$\alpha$-stable**: $\mu^\alpha_X=\tfrac\alpha2\mu_X$ term by term.

**Used here — $\phi$ Bernstein:** §5 uses only that $\phi$ is one of the paper's four processes, so that the class mass and its total exist; no analytic property of $\phi$ is touched.
> [!recall]- $\phi$ a Bernstein function satisfying Assumption 2.3 [home §2]
> $\phi:(0,\infty)\to[0,\infty)$ is **Bernstein** if $C^\infty$ with $(-1)^{n-1}\phi^{(n)}\ge0$ ($n\ge1$); equivalently $\phi(\lambda)=a+b\lambda+\int_0^\infty(1-e^{-\lambda u})\nu(du)$, the Laplace exponent of an increasing random clock. **Assumption 2.3:** $b>0$ or $\nu(0,\infty)=\infty$. The four instances: $\phi(\lambda)=\lambda,\ \lambda+\kappa,\ \lambda^{\alpha/2},\ (\lambda+\kappa)^{\alpha/2}$.

# B. Spine of §5 (skim layer)

Eight moves. Read this list and you have §5's logical content; drop into the matching subsection for expansions, imports and proofs.

1. **§5.1 — $\det_\zeta\Delta_X$.** *Define* $\zeta_X(s)=\sum_{j\ge1}\lambda_j^{-s}$ and $\log\det_\zeta\Delta_X:=-\zeta_X'(0)$; *produce* (via the heat-trace short-time expansion) a $\zeta_X$ regular at $s=0$, so the determinant exists.
2. **§5.1 — Schwinger link.** *Recall* from §3.2 that $-\log\det(\Delta+\kappa)$ "$=$" $\int_0^\infty\frac{dt}t e^{-\kappa t}\mathrm{Tr}(e^{-t\Delta})$, the regularised total killed loop mass; *produce* the object §5 renormalises.
3. **§5.1 — Selberg trace formula (import).** *Given* $\sum_j e^{-t\lambda_j}=[\text{identity}]+S_X(t)$; *produce* $\int_0^\infty e^{-\kappa t}S_X(t)\frac{dt}t=$ total loop mass $=-\log Z_X(s)$.
4. **§5.1 — Naud's formula (import).** *Given* the closed surface; *produce* $-\log\det_\zeta\Delta_X$ as a length-spectrum integral $-\mathrm{Area}(X)E-\gamma_{\mathrm{EM}}+\int_0^1\frac{S_X}t+\int_1^\infty\frac{S_X-1}t$.
5. **§5.1 — Theorem 5.1.** *Combine* Naud + Selberg + §4; *produce* the loop-measure expressions (i) Brownian (cutoff-renormalised), (ii) killing (with the $\kappa\to0^+$ two-$\log\kappa$ cancellation giving $\log\det_\zeta\Delta=\mathrm{Area}(X)E+\log Z_X'(1)$), (iii) $\alpha$-stable ($\times\tfrac\alpha2$).
6. **§5.1 — Polyakov + Cor 5.4.** *Given* the anomaly transformation law under $g=e^{2\sigma}g_{\mathrm{hyp}}$; *produce* the determinant of **every** metric in the conformal class as $P_X(\sigma)+\mathrm{Area}(X)E+\log Z_X'(1)$ — loop measure computed once per conformal class.
7. **§5.2 — $\det_0$ construction.** *Given* a cusped surface (continuous spectrum $[\tfrac14,\infty)$, $e^{-t\Delta_X}$ not trace class); *produce* the renormalised $0$-trace ${}^0\mathrm{Tr}$, the regular-at-$0$ zeta $\zeta^0_X$, and $\det_0\Delta_X:=e^{-(\zeta^0_X)'(0)}$ (Melrose import), reducing to $\det_\zeta$ when closed.
8. **§5.2 — Borthwick–Judge–Perry + Theorem 5.7.** *Given* $\det_0(\Delta_X-s(1-s))=Z_X(s)\cdot(\text{explicit }\Gamma/\text{Barnes factors})$; *produce* $-\log\det_0(\Delta_X+\kappa)=F\kappa-M+\sum\mu^\kappa_X-D_X(s)$, and $\kappa\to0^+$ gives $\log\det_0\Delta_X=\log C_X+\log Z_X'(1)$ — same global $Z_X'(1)$, local factor now $\chi,n_C$ instead of $\mathrm{Area}$.

# C. The results

## §5.1  The determinant on a closed surface

### The zeta-regularised determinant $\det_\zeta\Delta_X$

The naive determinant $\prod_{j\ge1}\lambda_j$ diverges ($\sum_{j\ge1}\log\lambda_j=\infty$ by Weyl's law). Ray–Singer's fix routes through the spectral zeta function.

**Used here —** $\det_\zeta\Delta_X$ is the finite number §5 identifies with the renormalised total Brownian loop mass.
> [!def]+ $\zeta_X$, the spectral zeta function, and $\det_\zeta\Delta_X$
> $\displaystyle\zeta_X(s):=\sum_{j=1}^\infty\lambda_j^{-s},\qquad\operatorname{Re}(s)>1$ (converges by Weyl's law $\lambda_j\sim4\pi j/\mathrm{Area}(X)$; the sum omits $\lambda_0=0$). The formal identity $-\zeta_X'(0)"="\sum_{j\ge1}\log\lambda_j$ then **defines**
> $$\log\det_\zeta\Delta_X:=-\zeta_X'(0),$$
> once $\zeta_X$ is meromorphically continued and shown regular at $s=0$ (standard, from the heat trace, below).

The continuation is standard and elementary from the heat trace: writing each $\lambda_j^{-s}=\Gamma(s)^{-1}\int_0^\infty t^{s-1}e^{-t\lambda_j}\,dt$ (Mellin) and summing,
$$\zeta_X(s)=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}\big(\mathrm{Tr}(e^{-t\Delta_X})-1\big)\,dt,$$
where subtracting $1=\dim\ker\Delta_X$ drops $\lambda_0=0$. The short-time heat-trace asymptotic
$$\mathrm{Tr}(e^{-t\Delta_X})-1\ \sim\ \frac{\mathrm{Area}(X)}{4\pi t}+\Big(\frac{\chi(X)}6-1\Big)+O(t)\qquad(t\downarrow0)$$
controls the integral near $t=0$: the $t^{-1}$ term gives $\zeta_X$ a simple pole at $s=1$; the constant term would give a pole at $s=0$, but the simple zero of $1/\Gamma(s)$ there cancels it, leaving $\zeta_X$ **analytic at $0$** with $\zeta_X(0)=\chi(X)/6-1$, so $\zeta_X'(0)$ — hence $\det_\zeta\Delta_X$ — is well defined.

### The Schwinger link (why this is a loop mass)

The bridge from §3.2 makes $\log\det_\zeta$ a loop-measure quantity in the first place.

**Used here —** it exhibits $-\log\det(\Delta+\kappa)$ as the regularised total killed loop mass, the object Theorem 5.1(ii) renormalises; divergent at $t\to0$ as written.
> [!recall]- Schwinger / heat-kernel representation of $\log\det$ [home §3.2]
> For the killed operator $\Delta+\kappa$, formally $\displaystyle-\log\det(\Delta+\kappa)\ "="\ \int_0^\infty\frac{dt}t\,e^{-\kappa t}\,\mathrm{Tr}(e^{-t\Delta})\ =\ |\mu^\kappa_X|_{\mathrm{reg}}$, the total mass of the killing loop measure. The measure $\tfrac{dt}t\,e^{-\kappa t}$ is exactly the killed loop measure's duration weight; the integral diverges at $t\to0$ (short-time heat trace $\sim\mathrm{Area}/4\pi t$) and is made rigorous by the zeta continuation above.

### Selberg trace formula (import — genuine gap of §5.1)

The trace formula splits the heat trace into an identity part and a geometric part, and it is the geometric part that is a sum over loop-class masses.

**Used here —** its geometric term $S_X(t)$, integrated against $e^{-\kappa t}\,dt/t$, is the total killed loop mass, hence (by §4) $-\log Z_X(s)$; it converts spectral data into length-spectrum data.
> [!import]- Selberg trace formula (heat semigroup, compact) — Says / Needs / Gives  [the first genuine gap of §5.1]
> **Says.** For a closed hyperbolic surface, $\displaystyle\sum_{j=0}^\infty e^{-t\lambda_j}=\underbrace{\mathrm{Area}(X)\frac{e^{-t/4}}{(4\pi t)^{3/2}}\int_0^\infty\frac{r\,e^{-r^2/(4t)}}{\sinh(r/2)}\,dr}_{\text{identity contribution}}+\ S_X(t)$, where the **geometric term** is
> $$S_X(t)=\sum_{\gamma\in\mathcal P_X}\sum_{m=1}^\infty\frac{e^{-t/4}}{(4\pi t)^{1/2}}\cdot\frac{\ell_\gamma}{2\sinh(m\ell_\gamma/2)}\,e^{-(m\ell_\gamma)^2/(4t)}.$$
> $S_X(t)$ is exponentially small as $t\to0$, and $|S_X(t)-1|$ is exponentially small as $t\to\infty$.
> **Needs.** $X$ closed hyperbolic; $t>0$; the length spectrum $\{\ell_\gamma\}$ locally finite.
> **Gives.** $\displaystyle\int_0^\infty e^{-\kappa t}\,S_X(t)\,\frac{dt}t=\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\mu^\kappa_X(\mathcal C_X(\gamma^m))=-\log Z_X(s)$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ — because term by term $\int_0^\infty e^{-\kappa t}\frac{e^{-t/4}}{\sqrt{4\pi t}}\frac{\ell_\gamma}{2\sinh(m\ell_\gamma/2)}e^{-(m\ell_\gamma)^2/4t}\frac{dt}t=\mu^\kappa_X(\mathcal C_X(\gamma^m))$ (the Brownian class-mass collapse). **Status:** assume freely; nothing here re-proves it — this is Selberg's theorem. Not derivable from the anchors.

### Naud's formula (import — deepest gap of §5.1)

Selberg turns the *heat trace* into the length spectrum; Naud turns the *log-determinant* into it, by integrating the trace formula against $dt/t$ with the pole at $s=0$ handled.

**Used here —** it is the length-spectrum expression of $-\log\det_\zeta\Delta_X$ that Theorem 5.1 rewrites in loop-measure terms.
> [!import]- Naud's determinant formula — Says / Needs / Gives  [the deepest genuine gap of §5.1]
> **Says.** For a closed hyperbolic surface,
> $$-\log\det_\zeta\Delta_X=-\mathrm{Area}(X)E-\gamma_{\mathrm{EM}}+\int_0^1\frac{S_X(t)}t\,dt+\int_1^\infty\frac{S_X(t)-1}t\,dt,$$
> where $E=\dfrac{4\zeta_R'(-1)-\tfrac12+\log(2\pi)}{4\pi}\approx0.0538$ ($\zeta_R$ = Riemann zeta), $\gamma_{\mathrm{EM}}\approx0.5772$ is Euler–Mascheroni, and $S_X$ is Selberg's geometric term.
> **Needs.** $X$ closed hyperbolic; the refined prime geodesic theorem (import below) to control the length-spectrum integrals.
> **Gives.** $-\log\det_\zeta\Delta_X$ as two convergent length-spectrum integrals (the split at $t=1$ tames both ends: $S_X$ is exponentially small at $0$, $|S_X-1|$ exponentially small at $\infty$). **Status:** assume freely; Naud's theorem, built on Selberg. Not derivable from the anchors.

The one auxiliary the Brownian case (i) needs is the counting asymptotic.

**Used here —** it makes the cutoff-renormalised integral $\int_0^\infty\frac1{e^R-1}\,d(N_X(R)-\widetilde{\operatorname{Li}}(e^R))$ converge, by controlling $N_X(R)-\widetilde{\operatorname{Li}}(e^R)$.
> [!import]- Refined prime geodesic theorem (43) — Says / Needs / Gives  [genuine gap]
> **Says.** For a closed hyperbolic surface ($\delta=1$), as $R\to\infty$, $\displaystyle N_X(R)=\operatorname{Li}(e^R)+\sum_{0<\lambda_j\le1/4}\operatorname{Li}(e^{s_jR})+O_X\!\big(e^{3R/4}/R\big)$, where $\operatorname{Li}(x)=\int_2^x dt/\log t\sim x/\log x$ and $s_j=\tfrac12+\sqrt{\tfrac14-\lambda_j}\in(\tfrac12,1)$ are the small-eigenvalue exponents. In particular $|N_X(R)-\widetilde{\operatorname{Li}}(e^R)|=O_X(e^{(1-\epsilon)R})$ for some $\epsilon>0$.
> **Needs.** $X$ closed hyperbolic.
> **Gives.** Convergence of $\int_0^\infty\frac1{e^R-1}\,d(N_X(R)-\widetilde{\operatorname{Li}}(e^R))$ by parts (the integrand decays like $e^{-\epsilon R}$). **Status:** assume freely; a consequence of the Selberg trace formula. Not derivable from the anchors.

### Theorem 5.1 (the determinant as a loop mass, compact)

> **Result 5.1 (zeta-regularised determinant via subordinate loop measure, compact case).** Let $X=\Gamma\backslash\mathbb H^2$ be a closed hyperbolic surface of genus $g$; write $\det_\zeta\Delta$ for the determinant with $\lambda_0=0$ excluded. Assume:
> **(H1)** $\phi$ is one of the paper's four Bernstein functions, so every class mass $\mu^\phi_X(\mathcal C_X(\gamma^m))$ is finite and given by the class-mass recall.
> **(H2)** Naud's formula, the Selberg trace formula, and the refined prime geodesic theorem hold (imports above).
> **(H3)** for the killing case, $\kappa>0$ and $s=\tfrac12+\sqrt{\tfrac14+\kappa}>1$, so the total killed mass is finite and equals $-\log Z_X(s)$ (§4).
> **Then:**
> **(i) Brownian** ($\phi(\lambda)=\lambda$): with $C$ a universal constant and $\widetilde{\operatorname{Li}}$ the cutoff of $\operatorname{Li}$ at $2$,
> $$-\log\det_\zeta\Delta=-\mathrm{Area}(X)E+C+\!\!\sum_{\gamma\in\mathcal G(X)\setminus\mathcal P_X}\!\!\mu_X(\mathcal C_X(\gamma))+\int_{R=0}^\infty\frac1{e^R-1}\,d\big(N_X(R)-\widetilde{\operatorname{Li}}(e^R)\big).\tag{46}$$
> **(ii) killing** ($\phi(\lambda)=\lambda+\kappa$, $\kappa>0$): for each $\kappa>0$,
> $$-\log\det_\zeta\Delta=-\mathrm{Area}(X)E+\log\kappa+\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\mu^\kappa_X(\mathcal C_X(\gamma^m))+O(\kappa)=-\mathrm{Area}(X)E+\log\kappa-\log Z_X(s)+O(\kappa),\tag{47–48}$$
> and letting $\kappa\to0^+$ (so $s\to1$; the two $\log\kappa$ cancel via the simple zero of $Z_X$ at $s=1$),
> $$\boxed{\ \log\det_\zeta\Delta=\mathrm{Area}(X)E+\log Z_X'(1)\ }\tag{49}$$
> **(iii) $\alpha$-stable** ($\phi(\lambda)=\lambda^{\alpha/2}$, $\alpha\in(0,2)$): with $\det_\zeta\Delta_{\alpha/2}$ the determinant of $\Delta^{\alpha/2}$ (eigenvalues $\lambda_j^{\alpha/2}$),
> $$-\log\det_\zeta\Delta_{\alpha/2}=\tfrac\alpha2\big(-\mathrm{Area}(X)E+C\big)+\!\!\sum_{\gamma\in\mathcal G(X)\setminus\mathcal P_X}\!\!\mu^\alpha_X(\mathcal C_X(\gamma))+\tfrac\alpha2\int_{R=0}^\infty\frac1{e^R-1}\,d\big(N_X(R)-\widetilde{\operatorname{Li}}(e^R)\big).\tag{50}$$

**Discharge (the typecheck) — killing case (ii), the load-bearing one.**

| step | apply | to | get |
|---|---|---|---|
| 1 | Schwinger recall $+$ Selberg import (its "Gives") | $\sum_{\gamma,m}\mu^\kappa_X(\mathcal C_X(\gamma^m))$ | $M_\kappa:=\int_0^\infty e^{-\kappa t}S_X(t)\,\tfrac{dt}t$ |
| 2 | split at $t=1$, subtract $1$ in the tail, add $E_1(\kappa)=\int_1^\infty e^{-\kappa t}\tfrac{dt}t$ | $M_\kappa$ | Naud integral $=M_\kappa-E_1(\kappa)+R_\kappa$, $\ |R_\kappa|\le\kappa\big(\int_0^1 S_X+\int_1^\infty|S_X-1|\big)=O(\kappa)$ |
| 3 | $E_1(\kappa)=-\gamma_{\mathrm{EM}}-\log\kappa+O(\kappa)$ into Naud's formula (import) | $-\log\det_\zeta\Delta$ | $=-\mathrm{Area}(X)E+\log\kappa+M_\kappa+O(\kappa)$ ($\gamma_{\mathrm{EM}}$ cancels) = (47) |
| 4 | §4 killing identity (H3): $M_\kappa=-\log Z_X(s)$ | (47) | $=-\mathrm{Area}(X)E+\log\kappa-\log Z_X(s)+O(\kappa)$ = (48) |
| 5 | simple zero (recall): $-\log Z_X(s)=-\log Z_X'(1)-\log(s-1)+O(s-1)$, $s-1\sim\kappa$ | (48), $\kappa\to0^+$ | $-\log\det_\zeta\Delta=-\mathrm{Area}(X)E-\log Z_X'(1)$, i.e. (49) |

Every symbol in every row is typed in §5.0; every predicate is an import or recall above. The block typechecks with nothing off-page.

> [!note]- Proof of (i), (ii), (iii) (skippable)
> **(ii) killing.** For $\kappa>0$ the total mass is finite, so no cutoff is needed. The killed heat trace is $e^{-\kappa t}S_X(t)$ (killing weights each loop of duration $t$ by $e^{-\kappa t}$), so by the Schwinger recall and the Selberg import's "Gives", $M_\kappa:=\sum_{\gamma,m}\mu^\kappa_X(\mathcal C_X(\gamma^m))=\int_0^\infty e^{-\kappa t}S_X(t)\,dt/t$. Split at $t=1$ and subtract $1$ from $S_X$ in the tail: $M_\kappa=\int_0^1 e^{-\kappa t}\tfrac{S_X}t\,dt+\int_1^\infty e^{-\kappa t}\tfrac{S_X-1}t\,dt+E_1(\kappa)$ with $E_1(\kappa)=\int_1^\infty e^{-\kappa t}\tfrac{dt}t$ (the exponential integral). Comparing with Naud's integrals, $\int_0^1\tfrac{S_X}t+\int_1^\infty\tfrac{S_X-1}t=M_\kappa-E_1(\kappa)+R_\kappa$, where $R_\kappa=\int_0^1\tfrac{(1-e^{-\kappa t})S_X}t\,dt+\int_1^\infty\tfrac{(1-e^{-\kappa t})(S_X-1)}t\,dt$; using $1-e^{-\kappa t}\le\kappa t$ and the exponential smallness of $S_X$ ($t\to0$) and $S_X-1$ ($t\to\infty$), $|R_\kappa|\le\kappa\big(\int_0^1 S_X\,dt+\int_1^\infty|S_X-1|\,dt\big)=O(\kappa)$. The standard expansion $E_1(\kappa)=-\gamma_{\mathrm{EM}}-\log\kappa+O(\kappa)$ substituted into Naud's formula gives $-\log\det_\zeta\Delta=-\mathrm{Area}(X)E-\gamma_{\mathrm{EM}}+M_\kappa-E_1(\kappa)+R_\kappa=-\mathrm{Area}(X)E+\log\kappa+M_\kappa+O(\kappa)$ — the two $\gamma_{\mathrm{EM}}$ cancel. That is (47); §4 gives $M_\kappa=-\log Z_X(s)$, which is (48). As $\kappa\to0^+$, $s\to1$; the simple zero gives $-\log Z_X(s)=-\log Z_X'(1)-\log(s-1)+O(s-1)$ with $s-1\sim\kappa$, so the explicit $\log\kappa$ and the $-\log(s-1)$ cancel and $O(\kappa)$ vanishes, leaving $\log\det_\zeta\Delta=\mathrm{Area}(X)E+\log Z_X'(1)$, i.e. (49). $\square$
> **(i) Brownian.** No killing, so the total mass diverges and is renormalised by a length-spectrum cutoff. Split Naud's integrals as $\int_0^1\tfrac{S_X}t+\int_1^\infty\tfrac{S_X-1}t=\int_0^\infty\tfrac{S_X-S^{\mathrm p}_X}t+\int_0^1\tfrac{S^{\mathrm p}_X}t+\int_1^\infty\tfrac{S^{\mathrm p}_X-1}t$, where $S^{\mathrm p}_X(t)=\sum_\gamma\tfrac{e^{-t/4}}{\sqrt{4\pi t}}\tfrac{\ell_\gamma}{2\sinh(\ell_\gamma/2)}e^{-\ell_\gamma^2/4t}$ is the primitive ($m=1$) part. The **non-primitive** part needs no renormalisation: term by term the $t$-integral is the Brownian class mass, so $\int_0^\infty\tfrac{S_X-S^{\mathrm p}_X}t\,dt=\sum_\gamma\sum_{m\ge2}\tfrac1m\tfrac1{e^{m\ell_\gamma}-1}=\sum_{\gamma\in\mathcal G(X)\setminus\mathcal P_X}\mu_X(\mathcal C_X(\gamma))$ (52). For the **primitive** part, write $S^{\mathrm p}_X(t)=\int_0^\infty\tfrac{e^{-t/4}}{\sqrt{4\pi t}}\tfrac{R}{2\sinh(R/2)}e^{-R^2/4t}\,dN_X(R)$, exchange the order of integration, and do the inner $t$-integrals via the error function; decomposing $N_X(R)=\widetilde{\operatorname{Li}}(e^R)+(N_X(R)-\widetilde{\operatorname{Li}}(e^R))$, the $\widetilde{\operatorname{Li}}$-part is $X$-independent and gives a universal constant $C_1$, and the remainder collapses to $\int_0^\infty\tfrac1{e^R-1}\,d(N_X(R)-\widetilde{\operatorname{Li}}(e^R))$, convergent by the refined prime geodesic theorem (53). Substituting (52),(53) into Naud with $C=-\gamma_{\mathrm{EM}}+C_1$ gives (46). $\square$
> **(iii) $\alpha$-stable.** Since $\zeta_{\Delta^{\alpha/2}}(s)=\zeta_X(\alpha s/2)$ (eigenvalues $\lambda_j^{\alpha/2}$), $\log\det_\zeta\Delta_{\alpha/2}=(\alpha/2)\log\det_\zeta\Delta$. Multiplying (46) by $\alpha/2$ and using $\mu^\alpha_X=(\alpha/2)\mu_X$ term by term gives (50). $\square$

> [!note]- Verification of the constants (skippable, every number reproducible)
> **$E\approx0.0538$.** With $\zeta_R'(-1)\approx-0.16542$: numerator $4(-0.16542)-0.5+\log(2\pi)=-0.66168-0.5+1.83788=0.67620$; divide by $4\pi=12.56637$: $E\approx0.05381$. ✓
> **The two-$\log\kappa$ cancellation.** From (48), $-\log\det_\zeta\Delta=-\mathrm{Area}(X)E+\log\kappa-\log Z_X(s)+O(\kappa)$. Near $s=1$: $-\log Z_X(s)=-\log Z_X'(1)-\log(s-1)+O(s-1)$. Since $\kappa=s(s-1)$ and $s\to1$, $\kappa=(1+o(1))(s-1)$, so $\log\kappa=\log(s-1)+o(1)$. Hence $\log\kappa-\log Z_X(s)=\log(s-1)-\log Z_X'(1)-\log(s-1)+o(1)=-\log Z_X'(1)+o(1)$. Thus $-\log\det_\zeta\Delta=-\mathrm{Area}(X)E-\log Z_X'(1)$, i.e. $\log\det_\zeta\Delta=\mathrm{Area}(X)E+\log Z_X'(1)$. ✓ The cancellation is only possible because $Z_X$ has a **simple** zero (order exactly $1$) at $s=1$ — a double zero would leave a residual $\log\kappa$.

> [!warning] Why the $\kappa>0$ detour is forced
> One cannot set $\kappa=0$ from the start: at $\kappa=0$ the total Brownian loop mass is **infinite** on a finite-area surface ($s=\delta=1$, §4). The killing $\kappa>0$ pushes $s>1$ so the mass is finite ($=-\log Z_X(s)$), and only *after* subtracting the divergent $\log\kappa$ against the zero of $Z_X$ does the $\kappa\to0^+$ limit exist. Formula (49) is the finite shadow of a mass that never converges directly.

### Polyakov's conformal anomaly (import) and Corollary 5.4

Theorem 5.1 computes $\log\det_\zeta\Delta$ on the **hyperbolic** representative of a conformal class. Polyakov's formula transports it to every metric in that class.

**Used here —** combined with (49) it gives $\log\det_\zeta\Delta$ for *every* metric conformal to $g_{\mathrm{hyp}}$, so the loop measure is computed only once per conformal class.
> [!import]- Polyakov's conformal anomaly formula — Says / Needs / Gives  [genuine gap, shallow]
> **Says.** Let $g_0$ and $g=e^{2\sigma}g_0$ be conformally equivalent smooth metrics on a closed surface $X$, $K_0$ the Gauss curvature of $g_0$. Then
> $$\log\det_\zeta\Delta_g=-\frac1{12\pi}\int_X|\nabla_{g_0}\sigma|^2\,d\mathrm{vol}_{g_0}-\frac1{6\pi}\int_X K_0\,\sigma\,d\mathrm{vol}_{g_0}+\log\frac{\mathrm{vol}_g(X)}{\mathrm{vol}_{g_0}(X)}+\log\det_\zeta\Delta_{g_0}.$$
> **Needs.** $X$ closed; $g,g_0$ smooth and conformally equivalent; $\sigma\in C^\infty(X)$.
> **Gives.** The determinant's dependence on the conformal factor $\sigma$ is purely local (a Dirichlet energy $+$ a curvature coupling $+$ a volume ratio). Specialising $g_0=g_{\mathrm{hyp}}$ (so $K_0\equiv-1$, $\mathrm{vol}_{g_0}(X)=4\pi(g-1)$), the curvature term reduces to $+\tfrac1{6\pi}\int_X\sigma\,dA_{\mathrm{hyp}}$; define the **Polyakov correction** $P_X(\sigma):=-\tfrac1{12\pi}\int_X|\nabla\sigma|^2\,dA_{\mathrm{hyp}}+\tfrac1{6\pi}\int_X\sigma\,dA_{\mathrm{hyp}}+\log\tfrac{\mathrm{vol}_g(X)}{4\pi(g-1)}$, so $\log\det_\zeta\Delta_g=P_X(\sigma)+\log\det_\zeta\Delta_{g_{\mathrm{hyp}}}$. **Status:** assume freely; Polyakov's theorem (heat-kernel variation). Not re-proved here.

> **Result 5.4 (Polyakov's formula via Brownian loop measure).** Let $X$ be a closed hyperbolic surface of genus $g$ and $g=e^{2\sigma}g_{\mathrm{hyp}}$ any smooth metric in its conformal class. Then, with $C$ the universal constant of Theorem 5.1(i),
> $$\log\det_\zeta\Delta_X=P_X(\sigma)+\mathrm{Area}(X)E-C-\!\!\sum_{\gamma\in\mathcal G(X)\setminus\mathcal P_X}\!\!\mu_X(\mathcal C_X(\gamma))-\int_{R=0}^\infty\frac1{e^R-1}\,d\big(N_X(R)-\widetilde{\operatorname{Li}}(e^R)\big),\tag{57}$$
> equivalently, via the $\kappa\to0^+$ limit (49),
> $$\log\det_\zeta\Delta_X=P_X(\sigma)+\mathrm{Area}(X)E+\log Z_X'(1).\tag{58}$$

**Discharge.**

| step | apply | to | get |
|---|---|---|---|
| 1 | Polyakov import (specialised $g_0=g_{\mathrm{hyp}}$) | $\log\det_\zeta\Delta_g$ | $=P_X(\sigma)+\log\det_\zeta\Delta_{g_{\mathrm{hyp}}}$ |
| 2 | Theorem 5.1(i), sign-flipped: $\log\det_\zeta\Delta_{g_{\mathrm{hyp}}}=\mathrm{Area}(X)E-C-\sum_{\mathcal G\setminus\mathcal P}\mu_X-\int\frac{d(N_X-\widetilde{\operatorname{Li}})}{e^R-1}$ | step 1 | $=$ (57) |
| 3 | Theorem 5.1(ii) limit (49): $\log\det_\zeta\Delta_{g_{\mathrm{hyp}}}=\mathrm{Area}(X)E+\log Z_X'(1)$ | step 1 | $=$ (58) |

Every symbol is typed in §5.0; the block typechecks with nothing off-page.

> [!note]- Proof (skippable) and Remark 5.2 (D'Hoker–Phong)
> Immediate: substitute the two forms of $\log\det_\zeta\Delta_{g_{\mathrm{hyp}}}$ from Theorem 5.1(i) and (49) into the specialised Polyakov relation $\log\det_\zeta\Delta_g=P_X(\sigma)+\log\det_\zeta\Delta_{g_{\mathrm{hyp}}}$. $\square$
> **Remark 5.2.** Equation (49) is the classical **D'Hoker–Phong** determinant formula $\det_\zeta\Delta=Z_X'(1)\,e^{(2g-2)(2\zeta_R'(-1)-1/4+\frac12\log2\pi)}$: exponentiating (49), $\det_\zeta\Delta=Z_X'(1)e^{\mathrm{Area}(X)E}$ and $\mathrm{Area}(X)E=4\pi(g-1)\cdot\tfrac{4\zeta_R'(-1)-1/2+\log2\pi}{4\pi}=(2g-2)(2\zeta_R'(-1)-\tfrac14+\tfrac12\log2\pi)$. ✓

## §5.2  The determinant on a cusped surface

Everything above used the discrete spectrum. On a finite-area **non-compact** surface it breaks: alongside the $L^2$ eigenvalues from $\lambda_0=0$, there is now a **continuous spectrum** filling $[\tfrac14,\infty)$, with multiplicity equal to $n_C$ (the number of cusps). Its generalised eigenfunctions are the **Eisenstein series** $E_j(z,s)$ — one per cusp, solving $\Delta_X E_j=s(1-s)E_j$ but *not* in $L^2$ (they grow at the cusp). So there is no discrete list $\{\lambda_j\}$ to feed $\sum_j\lambda_j^{-s}$, and $e^{-t\Delta_X}$ is no longer trace class. The determinant must be built differently.

### The renormalised $0$-trace and $\det_0$ (Melrose import)

The fix keeps $\Delta_X$ itself and renormalises the *integral of the heat-kernel diagonal*.

> [!def]+ boundary-defining function, renormalised integral, $0$-trace
> Compactify $X$ to $\bar X$ by capping each end with a circle at infinity, and fix a **boundary-defining function** $x$ — a smooth $x\ge0$ on $\bar X$ vanishing to first order exactly at the ends (so $x\to0$ down each cusp/funnel). For $f$ with a controlled asymptotic expansion at the ends, $\int_X x^z f\,\mu$ converges for $\operatorname{Re}z$ large and continues meromorphically in $z$; its **finite part** at $z=0$ is the **renormalised integral**
> $${}^0\!\!\int_X f\,\mu:=\operatorname{FP}_{z=0}\int_X x^z f\,\mu$$
> (Riesz renormalisation; the Hadamard version cuts the ends at $x\ge\epsilon$ and takes the finite part as $\epsilon\to0$ — they agree here). Applied to the volume form it gives the **renormalised area** ${}^0\mathrm{Area}(g)={}^0\!\!\int_X d\mathrm{vol}_g=-2\pi\chi(X)$ (Gauss–Bonnet). The **$0$-trace** of the heat semigroup is
> $${}^0\mathrm{Tr}(e^{-t\Delta_X}):={}^0\!\!\int_X p_X(t,z,z)\,d\mathrm{vol}_g(z),\qquad t>0,$$
> the renormalised integral of the (non-integrable) heat-kernel diagonal. As $t\to\infty$ it converges exponentially to the rank of the $L^2$ null space; as $t\to0$ it has an expansion in powers of $t$ **and $t\log t$** (the log terms come from the cusps).

**Used here —** it produces a spectral zeta $\zeta^0_X$ regular at $s=0$, hence a determinant $\det_0\Delta_X$ that reduces to $\det_\zeta$ when $X$ is closed.
> [!import]- Melrose microlocal expansion / $\zeta^0_X$ regular at $0$ — Says / Needs / Gives  [genuine gap; no DAG node]
> **Says.** The short-time expansion of ${}^0\mathrm{Tr}(e^{-t\Delta_X})$ (in $t$ and $t\log t$) gives the renormalised zeta
> $$\zeta^0_X(s):=\frac1{\Gamma(s)}\int_0^\infty t^{s-1}\,{}^0\mathrm{Tr}\big(e^{-t\Delta_X}-P\big)\,dt\qquad(P=\text{projection onto the }L^2\text{ null space})$$
> a meromorphic continuation to $\mathbb C$ that is **regular at $s=0$**, so the **renormalised determinant** $\det_0\Delta_X:=e^{-(\zeta^0_X)'(0)}$ is well defined.
> **Needs.** $X$ geometrically finite; the heat-kernel diagonal has a controlled expansion at the ends; $P$ subtracted so the $t\to\infty$ end converges.
> **Gives.** A determinant $\det_0\Delta_X$ for cusped/funnelled surfaces that **agrees with $\det_\zeta\Delta_X$ when $X$ is closed** (then ${}^0\mathrm{Tr}=\mathrm{Tr}$). **Status:** assume freely; Melrose's microlocal method (b-calculus). Not derivable from the anchors, and it is the one input of §5.2 with no separate DAG node.

### Borthwick–Judge–Perry (import) and Theorem 5.7

BJP tie $\det_0$ to the Selberg zeta through the resolvent, the cusped analogue of D'Hoker–Phong.

**Used here —** its "$-\log$" form (65) is exactly Theorem 5.7 once $-\log Z_X(s)$ is replaced by the total killed loop mass (§4).
> [!import]- Borthwick–Judge–Perry determinant identity — Says / Needs / Gives  [the deepest genuine gap of §5.2]
> **Says.** Let $X$ be geometrically finite with $n_C$ cusps and $\chi=\chi(X)$; $R_X(s)=(\Delta_X-s(1-s))^{-1}$. The renormalised determinant solves $\big(\tfrac1{2s-1}\partial_s\big)^2\log\det_0(\Delta_X-s(1-s))=-{}^0\mathrm{Tr}(R_X(s)^2)$, and integrating twice in $s$ fixes it up to a factor $e^{M+Fs(1-s)}$:
> $$\det_0(\Delta_X-s(1-s))=Z_X(s)\,e^{M+Fs(1-s)}\,\Xi_X(s),\qquad M=\chi\big(\tfrac12\log2\pi-2\zeta_R'(-1)+\tfrac14\big),\ \ F=-\chi,$$
> where $\Xi_X(s)$ is an explicit meromorphic factor assembled from the Barnes $G$-function (the entire solution of $G(s+1)=\Gamma(s)G(s)$, $G(1)=1$) and $\Gamma$, depending only on $\chi$ and $n_C$. Its exact form is in [BJP] and is **not needed below**; the one thing used is its value at $s=1$, which makes $\det_0\Delta_X=C_X\,Z_X'(1)$ when $\mathrm{Area}(X)<\infty$ (and $=C_X\,Z_X(1)$ when $\mathrm{Area}(X)=\infty$), with $C_X=e^M(2\pi)^{-\chi}(\sqrt{2\pi})^{-n_C}$.
> **Needs.** $X$ geometrically finite; the $0$-trace / $\det_0$ construction above.
> **Gives.** Define $D_X(s)$ by taking $-\log$ and separating the zeta term:
> $$-\log\det_0(\Delta_X-s(1-s))=-Fs(1-s)-M-\log Z_X(s)-D_X(s),\qquad D_X(s):=\log\Xi_X(s)^{-1}.$$
> $D_X(s)$ is thus explicit in $\chi,n_C$ (Barnes $G$ and $\Gamma$); the ONLY value used below is $D_X(1)=\log C_X-M=-\chi\log(2\pi)-n_C\log\sqrt{2\pi}$. Assume freely; nothing here re-proves it. **Status:** the Borthwick–Judge–Perry theorem; not derivable from the anchors. *(Remark 5.6: the $Z_X'(1)$ vs $Z_X(1)$ split is because $0$ is an $L^2$ eigenvalue exactly when $\mathrm{Area}(X)<\infty$, forcing the simple zero at $s=1$ that is divided out; in infinite area $Z_X(1)\neq0$ and no derivative is needed.)*

> **Result 5.7 (renormalised determinant via loop measure, finite-area case).** Let $X$ be a geometrically finite hyperbolic surface of **finite area**, with $n_C$ cusps and $\chi=\chi(X)$, and $M,F,D_X(s)$ as in the BJP import. Assume:
> **(H1)** $\kappa\ge0$, and $s=\tfrac12+\sqrt{\tfrac14+\kappa}>1$, so $s(s-1)=\kappa$ and $\Delta_X-s(1-s)=\Delta_X+\kappa$.
> **(H2)** the total killed loop mass equals $-\log Z_X(s)$ (§4; valid since $s>1\ge\delta$ for finite area).
> **(H3)** the BJP identity (its "Gives" form (65)) and the $\det_0$ construction hold.
> **Then** for each $\kappa>0$,
> $$-\log\det_0(\Delta_X+\kappa)=F\kappa-M+\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\mu^\kappa_X(\mathcal C_X(\gamma^m))-D_X(s),\tag{67}$$
> and, dividing out the simple zero to define $\det_0\Delta_X:=\lim_{s\to1}\det_0(\Delta_X-s(1-s))/(s(s-1))$, the limit $\kappa\to0^+$ gives
> $$\boxed{\ \log\det_0\Delta_X=M+D_X(1)+\log Z_X'(1)=\log C_X+\log Z_X'(1)\ }\tag{68}$$
> where $D_X(1)=-\chi\log(2\pi)-n_C\log\sqrt{2\pi}$ and $C_X=e^M(2\pi)^{-\chi}(\sqrt{2\pi})^{-n_C}$.

**Discharge.**

| step | apply | to | get |
|---|---|---|---|
| 1 | BJP "Gives" (65) with $s(1-s)=-\kappa$ | $\det_0(\Delta_X-s(1-s))=\det_0(\Delta_X+\kappa)$ | $-\log\det_0(\Delta_X+\kappa)=F\kappa-M-\log Z_X(s)-D_X(s)$ |
| 2 | §4 killing identity (H2): $-\log Z_X(s)=\sum_{\gamma,m}\mu^\kappa_X(\mathcal C_X(\gamma^m))$ | step 1 | $=F\kappa-M+\sum_{\gamma,m}\mu^\kappa_X(\mathcal C_X(\gamma^m))-D_X(s)$ = (67) |
| 3 | simple zero (recall): $-\log Z_X(s)=-\log Z_X'(1)-\log(s-1)+O(s-1)$; divide by $s(s-1)=\kappa$, $s-1\sim\kappa$ | (67), $\kappa\to0^+$ | $-\log(s-1)$ cancels the $\log$-divergence; $F\kappa\to0$, $D_X(s)\to D_X(1)$ |
| 4 | $D_X(1)=\log C_X-M$ (from $C_X=e^M\cdot$ the $D_X(1)$ factors) | step 3 | $\log\det_0\Delta_X=M+D_X(1)+\log Z_X'(1)=\log C_X+\log Z_X'(1)$ = (68) |

Every symbol is typed in §5.0; every predicate is an import or recall above. The block typechecks with nothing off-page.

> [!note]- Proof (skippable)
> Substitute the §4 killing identity $-\log Z_X(s)=\sum_{\gamma,m}\mu^\kappa_X(\mathcal C_X(\gamma^m))$ into the BJP "Gives" form (65) and use $s(1-s)=-\kappa$: this is (67) directly. For the limit, finite area forces the simple zero $Z_X(s)=Z_X'(1)(s-1)+O((s-1)^2)$, so $-\log Z_X(s)=-\log Z_X'(1)-\log(s-1)+O(s-1)$. Dividing $\det_0(\Delta_X-s(1-s))$ by $s(s-1)$ subtracts $\log(s(s-1))$ from $\log\det_0$; since $s(s-1)=\kappa$ and $s-1\sim\kappa$ as $\kappa\to0^+$, the resulting $-\log(s-1)$ cancels the divergence in $-\log Z_X(s)$. With $F\kappa\to0$, $D_X(s)\to D_X(1)$, and $D_X(1)=\log C_X-M$, this yields $\log\det_0\Delta_X=M+D_X(1)+\log Z_X'(1)=\log C_X+\log Z_X'(1)$, i.e. (68). $\square$

> [!note]- Remark 5.8 (the infinite-area case, skippable)
> When $\mathrm{Area}(X)=\infty$ one has $\delta<1$ (recall), so by §4 the total subordinate loop mass is **already finite** at $\kappa=0$ ($s=1>\delta$). The determinant identity then holds directly at $s=1$: $0$ is not an $L^2$ eigenvalue, $Z_X(1)\neq0$, no derivative is divided out, and BJP gives $\det_0\Delta_X=C_X Z_X(1)$. The corresponding $-\log\det_0\Delta_X$ via the loop mass and the resonance divisor of $Z_X$ is in Lemonde–Wang [LW26]; the Polyakov anomaly for non-compact surfaces exists too.

# D. Exports, climb, commentary

**Exports (what later sections consume from §5).**
- **(E1)** the closed-surface determinant, $\log\det_\zeta\Delta_X=\mathrm{Area}(X)E+\log Z_X'(1)$ (49), with its conformal-class extension $P_X(\sigma)+\mathrm{Area}(X)E+\log Z_X'(1)$ (58). → the self-contained determinant coda; the D'Hoker–Phong identification.
- **(E2)** the cusped-surface determinant, $\log\det_0\Delta_X=\log C_X+\log Z_X'(1)$ (68), $C_X=e^M(2\pi)^{-\chi}(\sqrt{2\pi})^{-n_C}$ — same **global** factor $Z_X'(1)$, **local** factor now $\chi,n_C$ instead of $\mathrm{Area}$.
- **(E3)** the renormalisation itself: the finite-area total Brownian loop mass diverges at $\kappa=0$, and §5 gives it a finite spectral meaning. → §6 sidesteps the divergence entirely by working at $\kappa>0$, where the total mass $-\log Z_X(s)$ is finite and normalises to a probability measure; §6 uses only the remark that $\kappa=0$ is available via §5.

**Climb (optional — none is needed to typecheck §5).** Sibling sections and ledgers: [[§4 Zeta Identities and Finiteness]] (the killing identity $\sum\mu^\kappa_X=-\log Z_X(s)$ and the finite-area divergence this section renormalises) · [[§3 Mass of a Homotopy Class]] (the class mass (24) and its Brownian collapse) · [[§6 Probability on Homotopy and Homology Classes]] (consumes E3) · [[§7 Hyperbolic 3-Manifolds]] · [[External Inputs and Gaps]] (Selberg trace formula, Naud, prime geodesic theorem, Polyakov, Melrose, Borthwick–Judge–Perry) · [[Anchors and Prerequisites]].

> [!note]- Commentary (skippable)
> §5 is the section where the loop-soup picture pays its debt to spectral geometry. §4 left an embarrassment: on the surface one most cares about — closed, no killing — the total Brownian loop mass is *infinite*. §5's whole content is that this infinity is not a defect but the divergence of a determinant, and that the finite part is $\log\det_\zeta\Delta_X$. The mechanism is a single collision of two logarithms. Killing $\kappa>0$ makes the mass finite ($=-\log Z_X(s)$) but drags in a spurious $\log\kappa$ from the exponential integral $E_1(\kappa)=\int_1^\infty e^{-\kappa t}\,dt/t\sim-\log\kappa$; the Selberg zeta, because $\lambda_0=0$ gives it a *simple* zero at $s=1$, contributes an equal and opposite $-\log(s-1)\sim-\log\kappa$; they annihilate, and what survives is $\mathrm{Area}(X)E+\log Z_X'(1)$ — the D'Hoker–Phong formula, now read off Brownian loops. Remove the killing detour and the mass never converges; remove the simple zero (a double zero, say) and a residual $\log\kappa$ would remain — the cancellation is exact only because the kernel of $\Delta_X$ is one-dimensional.
>
> The Naud, Selberg, Polyakov, Melrose and Borthwick–Judge–Perry imports are the deepest borrowings in the paper, and it is honest to see §5 as *four theorems the paper uses and one identity it proves*: the identity is that the length-spectrum integral Naud writes down is, term by term, the loop-class mass — which is the §3 computation run in reverse. Polyakov then costs nothing extra: since the loop measure only sees the hyperbolic representative, and Polyakov's law says the determinant's conformal-factor dependence is a local Dirichlet-plus-curvature functional $P_X(\sigma)$, one computes the loop side **once** per conformal class and slides along the class by adding $P_X(\sigma)$. §5.2 is the same play on a stage where the spectrum has gone continuous: the trace becomes a renormalised $0$-trace (Melrose), D'Hoker–Phong becomes Borthwick–Judge–Perry, and the surface's global data $\mathrm{Area}(X)$ in (49) is replaced by its topological data $\chi,n_C$ in (68) — but the arithmetic core, the factor $Z_X'(1)$ and the same simple-zero cancellation, is untouched.