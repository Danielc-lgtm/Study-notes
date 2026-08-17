---
type: paper-section
paper: "BH26"
subject: brownian-loops
section: "6"
tags: [paper, section, self-contained]
---

> [!info] Part of [[Map - Brownian Loops on Homotopy and Homology Classes]]. Self-contained: every symbol, predicate and imported result used below is written out on this page. Grey callouts are folds on THIS page — opening one is a scroll, not a jump to another file. You can typecheck §6 front-to-back without opening anything else.

**What §6 buys you.** §4 turned the total loop mass into the single spectral number $-\log Z_X(s)$. §6 divides one class mass by that number to make an honest probability measure $\mathbb P_s$ on free-homotopy classes, reads its every moment off derivatives of $\log(-\log Z_X)$, and watches it concentrate on the shortest geodesics as the killing rate $\kappa\to\infty$. Then it coarsens the partition from homotopy to homology: twisting the Selberg zeta by a unitary character gives a Selberg $L$-function whose logarithm is the Fourier transform (over the lattice $H_1(X,\mathbb Z)\cong\mathbb Z^r$) of the homology-class masses, and one exponential-formula computation delivers the exact law of the total homology of the whole loop soup. Throughout §6 the killing is strictly positive, $\kappa>0$.

# A. Standing setup

Everything in §6 lives on a fixed hyperbolic surface $X$ and manipulates the masses a fixed killed Brownian loop measure assigns to its free-homotopy classes, together with the twisted zeta functions those masses generate. The paragraphs below fix every standing object, inlined so that dropping straight into §6 needs nothing from earlier sections.

**The surface.** $\Gamma\subseteq\mathrm{PSL}(2,\mathbb R)$ is a discrete, torsion-free group of isometries of the hyperbolic plane $\mathbb H^2$ (upper half-plane $\{z:\operatorname{Im}z>0\}$, metric $|dz|/\operatorname{Im}z$), acting **freely** — $\forall h\in\Gamma\setminus\{1\}\ \forall z\in\mathbb H^2:\ hz\neq z$ (no non-identity isometry fixes a point) — and **properly discontinuously** — $\forall K\Subset\mathbb H^2:\ \#\{h\in\Gamma:\ hK\cap K\neq\varnothing\}<\infty$ (each compact set meets only finitely many of its $\Gamma$-translates). Under exactly these two conditions the quotient $X=\Gamma\backslash\mathbb H^2$ (points of $\mathbb H^2$ glued when one is a $\Gamma$-image of the other) is a smooth hyperbolic surface and $\pi:\mathbb H^2\to X$ is a **covering map** (a local isometry under which $\mathbb H^2$ wraps around $X$) with **deck group** $\Gamma$ (the isometries permuting the sheets over each point), $\Gamma\cong\pi_1(X)$. We take $X$ **geometrically finite** — $\Gamma$ finitely generated, equivalently $X$ has a finite-sided fundamental polygon; the consequences used in §6 are that the length spectrum is locally finite, $\#\{\gamma:\ell_\gamma\le R\}<\infty$ for every $R$ (so a shortest geodesic exists), and that $H_1(X,\mathbb Z)$ is a finitely generated free abelian group.

**Geodesics and their classes.** A closed geodesic $\gamma$ is **primitive** if it is not a repeated traversal of a shorter one — on the group side its representative $\tau\in\Gamma$ satisfies $\tau=\sigma^k\ (\sigma\in\Gamma,\,k\ge1)\Rightarrow k=1$. Write $\mathcal P_X$ for the primitive oriented closed geodesics and $\ell_\gamma:=\min_z d(z,\tau z)>0$ for the length of $\gamma$ (the **translation length** of $\tau$). Every closed geodesic is the $m$-fold iterate $\gamma^m$ of a unique primitive $\gamma$, of length $L:=m\ell_\gamma$. Two oriented closed curves are **freely homotopic** if one deforms into the other through closed curves with **no basepoint fixed** ($\exists$ continuous $H:S^1\times[0,1]\to X$ between them); the free-homotopy classes of loops on $X$ correspond bijectively to conjugacy classes $[h]=\{qhq^{-1}:q\in\Gamma\}$ in $\Gamma$, and — restricting to **non-trivial, non-peripheral** classes — to pairs $(\gamma,m)\in\mathcal P_X\times\mathbb Z_{\ge1}$: write $\mathcal C_X(\gamma^m)$ for the class winding $m$ times around $\gamma$, i.e. the conjugacy class $[\tau^m]$. **The only geometric input to every mass below is the single positive number $L=m\ell_\gamma$.**

**The loop measure and its class masses.** $\mu^\kappa_X$ is the killed Brownian **loop measure** on the space of unrooted, unparametrised, oriented loops on $X$: a $\sigma$-finite measure of **infinite** total mass, built from Brownian motion killed at rate $\kappa>0$. What §6 consumes from it is one finite positive number per class, the class mass $\mu^\kappa_X(\mathcal C_X(\gamma^m))\in(0,\infty)$, computed in §3–§4 and recalled below. The two names for the same object — the free-homotopy class $\mathcal C_X(\gamma^m)$ and the length $L=m\ell_\gamma$ of its geodesic representative — are used interchangeably.

**Notation for §6.**

| symbol | type |
|---|---|
| $X=\Gamma\backslash\mathbb H^2$ | geometrically finite hyperbolic surface; $\Gamma\cong\pi_1(X)$ |
| $\mathcal P_X$ | primitive oriented closed geodesics $\gamma$; $\ell_\gamma\in(0,\infty)$ their lengths |
| $m,\,L$ | $m\in\mathbb Z_{\ge1}$; $L:=m\ell_\gamma\in(0,\infty)$ |
| $\mathcal C_X(\gamma^m)$ | free-homotopy class of $\gamma^m$ $=$ conjugacy class $[\tau^m]$; a measurable set of loops |
| $\kappa,\ s$ | killing $\kappa>0$; spectral parameter $s=\tfrac12+\sqrt{\tfrac14+\kappa}>1$, real, $\operatorname{Re}s>\delta$ |
| $\mu^\kappa_X(\mathcal C_X(\gamma^m))$ | class mass $\in(0,\infty)$, $=\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$ (recall below) |
| $Z_X,\ \delta$ | Selberg zeta $\{\operatorname{Re}s>\delta\}\to\mathbb C$; critical exponent $\in(0,1]$ (recalls below) |
| $\mathbb P_s$ | probability measure on non-trivial non-peripheral classes (§6.1) |
| $F(s)$ | $:=-\log Z_X(s)\in(0,\infty)$, the total mass; $F^{(n)}$ its $s$-derivatives |
| $\mathbb E_s,\ \operatorname{Var}_s$ | expectation / variance under $\mathbb P_s$ (the class-length $L$ is the random variable) |
| $\ell_{\mathrm{sys}},\ N_{\mathrm{sys}}$ | systole $\min_{\gamma}\ell_\gamma>0$; number of systolic classes $\#\{\gamma:\ell_\gamma=\ell_{\mathrm{sys}}\}\ge2$ |
| $H_1(X,\mathbb Z)\cong\mathbb Z^r$ | first homology; rank $r=2g$ (closed) or $r=2g+b-1$ ($b\ge1$ ends) |
| $g,\ b,\ n_C,\ n_F$ | genus; number of ends $b=n_C+n_F$ ($n_C$ cusps, $n_F$ funnels) |
| $[\gamma],\ \beta$ | homology image of $\gamma\in\mathcal P_X$; a homology class $\beta\in H_1(X,\mathbb Z)$; $[\gamma^m]=m[\gamma]$ |
| $\widehat H_1,\ \chi,\ d\chi$ | character torus $\operatorname{Hom}(H_1,S^1)\cong(S^1)^r$; unitary character $\chi$; normalised Haar $d\chi$ |
| $L_X(s,\chi)$ | Selberg $L$-function (twisted zeta); $L_X(s,\mathbf 1)=Z_X$ |
| $\mu^\kappa_X(\beta)$ | mass in homology class $\beta$, $=\sum_{m[\gamma]=\beta}\mu^\kappa_X(\mathcal C_X(\gamma^m))$ |
| $\mathcal L_\lambda,\ \mathcal L^*_\lambda,\ \lambda$ | loop soup of intensity $\lambda>0$; its non-contractible non-peripheral loops |
| $\beta(\lambda)$ | total homology $\sum_{\eta\in\mathcal L^*_\lambda}[\eta]\in H_1(X,\mathbb Z)$ |

**Standing conventions.** $\Delta_X\ge0$ (geometer's sign; $\operatorname{spec}\Delta_X\subseteq[0,\infty)$); Brownian motion at speed $2$ (generator $-\Delta_X$). Three time-like variables are kept typographically distinct, deviating from the paper's single "$s$": the **spectral parameter** $s$; the **subordination / proper-time** variable $u$ (integrated in $I_\phi$ and $V_\phi$); the **loop duration** $t$ (integrated $\mathrm{d}t/t$). Spectral $s$ and killing $\kappa$ are linked by $s=\tfrac12+\sqrt{\tfrac14+\kappa}\iff\kappa=s(s-1)$, with $\kappa\ge-\tfrac14$ (at $\kappa=-\tfrac14$, $s=\tfrac12=\inf\operatorname{spec}\Delta_{\mathbb H^2}$). **Total mass** always means the sum over **non-trivial, non-peripheral** free-homotopy classes: the trivial (contractible) class carries infinite mass and is excluded, and peripheral (cusp) classes have no closed geodesic and are excluded.

Four objects built in earlier sections reach §6 only through their end-formulas; they are folded here so nothing is off-page.

**Used here — the killing class mass (§3 Theorem 3.5 / §4 (35)):** only its value $\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$ as a function of the class-length $L$, and the fact that summing it over all classes gives $-\log Z_X(s)$.
> [!import]- (24$_\kappa$) The killing class mass and its total — Says / Needs / Gives
> **Says.** For primitive $\gamma$, $m\ge1$, $L=m\ell_\gamma$, killing $\kappa>0$ and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$:
> $$\mu^\kappa_X\big(\mathcal C_X(\gamma^m)\big)=\frac1m\cdot\frac{e^{(1-s)L}}{e^{L}-1},\qquad\text{and}\qquad\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\mu^\kappa_X\big(\mathcal C_X(\gamma^m)\big)=-\log Z_X(s).$$
> **Needs.** $\kappa>0$ (so $s>1\ge\delta$ and the sum converges — §4 finiteness); $\gamma\in\mathcal P_X$; $m\ge1$.
> **Gives.** A closed positive number per class, depending on the geometry only through $L$, whose total over all non-trivial non-peripheral classes is the single spectral value $-\log Z_X(s)$. Assume freely; §3 proves the per-class value (covering-space unfolding $+$ Wang–Xue strip identity $+$ Gaussian reciprocal integral) and §4 sums it (the Selberg zeta criterion). Nothing here re-proves it.

**Used here — the Selberg zeta $Z_X$ and its log-expansion (F1) (§4):** only the identity $-\log Z_X(s)=\sum_{\gamma,m}\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$ and that it converges absolutely for $\operatorname{Re}s>\delta$.
> [!recall]- $Z_X$, the Selberg zeta function, and its logarithm
> $\displaystyle Z_X(s):=\prod_{\gamma\in\mathcal P_X}\ \prod_{k=0}^{\infty}\big(1-e^{-(s+k)\ell_\gamma}\big),\qquad\operatorname{Re}s>\delta$ (a double product: outer over primitive geodesics — the "primes"; inner over $k\ge0$). Its logarithm is elementary:
> $$-\log Z_X(s)=\sum_{\gamma\in\mathcal P_X}\sum_{m=1}^{\infty}\frac1m\cdot\frac{e^{(1-s)L}}{e^{L}-1}\Big|_{L=m\ell_\gamma},\qquad\operatorname{Re}s>\delta,$$
> got by applying $-\log(1-x)=\sum_{m\ge1}x^m/m$ to each factor and summing the inner geometric series $\sum_{k\ge0}e^{-(s+k)m\ell_\gamma}=e^{-sm\ell_\gamma}/(1-e^{-m\ell_\gamma})=e^{(1-s)L}/(e^L-1)$. No zeta theory is used. Since $\kappa>0$ forces $s>1$, and $\delta\le1$, the range $\operatorname{Re}s>\delta$ holds throughout §6.

**Used here — the critical exponent $\delta$ (§4):** only that $s>\delta$ (guaranteed by $\kappa>0$) makes the total mass finite and positive.
> [!recall]- $\delta$, the critical exponent
> $\displaystyle\delta:=\inf\Big\{s>0:\sum_{h\in\Gamma}e^{-s\,d(z,hz)}<\infty\Big\}\in(0,1]$ (abscissa of convergence of the Poincaré series; base-point independent). It is the exponential growth rate of closed geodesics, $N_X(R):=\#\{\gamma\in\mathcal P_X:\ell_\gamma\le R\}\sim e^{\delta R}/(\delta R)$, and $\delta=1\iff\operatorname{area}(X)<\infty$. Read "$s>\delta$" as **decay rate beats geodesic-proliferation rate**; with $\kappa>0$ giving $s>1\ge\delta$, the total mass $-\log Z_X(s)\in(0,\infty)$.

**Used here — the loop soup (§3.3):** only that it is a Poisson point process whose intensity is $\lambda$ times the loop measure, so the number of non-trivial non-peripheral loops it contains is $\operatorname{Poisson}$ with mean $\lambda$ times the total class mass.
> [!recall]- The loop soup $\mathcal L_\lambda$ as a Poisson point process
> $\mathcal L_\lambda$ is the **Poisson point process** on loops with intensity measure $\lambda\,\mu^\kappa_X$ ($\lambda>0$ the intensity): a random countable multiset of loops such that, for disjoint measurable loop-sets $A_1,\dots,A_k$ of finite mass, the counts $\#(\mathcal L_\lambda\cap A_i)$ are independent $\operatorname{Poisson}(\lambda\,\mu^\kappa_X(A_i))$. Write $\mathcal L^*_\lambda$ for the sub-collection of loops that are non-contractible and not homotopic into a cusp (i.e. those lying in some class $\mathcal C_X(\gamma^m)$). Because the union of those classes has finite total mass $-\log Z_X(s)$, $\ \#\mathcal L^*_\lambda\sim\operatorname{Poisson}\!\big(\lambda\,(-\log Z_X(s))\big)$ is almost surely finite.

# B. Spine of §6 (skim layer)

The section is seven moves. Read this list and you have §6's logical content; drop into the matching subsection for expansions, imports and proofs. Throughout, $\kappa>0$ and $F(s):=-\log Z_X(s)\in(0,\infty)$.

1. **§6.1 — $\mathbb P_s$.** *Given* class masses summing to $F(s)$; *produce* the probability measure $\mathbb P_s(\mathcal C_X(\gamma^m))=\mu^\kappa_X(\mathcal C_X(\gamma^m))/F(s)$ on non-trivial non-peripheral classes.
2. **§6.1 — moments.** *Given* the weight is analytic in $s$ with $\partial_s\mu^\kappa_X=-L\,\mu^\kappa_X$; *produce* $\mathbb E_s[e^{-rL}]=F(s+r)/F(s)$ (shift $=$ tilt), $\mathbb E_s[L^n]=(-1)^nF^{(n)}/F$, $\mathbb E_s[L]=-(\log F)'$, $\operatorname{Var}_s(L)=(\log F)''$; $s\mapsto\mathbb E_s[L]$ strictly decreasing.
3. **§6.1 — concentration.** *Given* $s\to\infty$; *produce* $\mathbb P_s\to$ uniform on the $N_{\mathrm{sys}}\ge2$ systolic classes, $\mathbb E_s[L]\to\ell_{\mathrm{sys}}$, $F(s)\sim\frac{N_{\mathrm{sys}}}{1-e^{-\ell_{\mathrm{sys}}}}e^{-s\ell_{\mathrm{sys}}}$, and both $\ell_{\mathrm{sys}},N_{\mathrm{sys}}$ recoverable from that asymptotic.
4. **§6.2 — homology mass (Def 6.1).** *Given* the abelianisation $\pi_1\twoheadrightarrow H_1(X,\mathbb Z)\cong\mathbb Z^r$; *produce* $\mu^\kappa_X(\beta):=\sum_{m[\gamma]=\beta}\mu^\kappa_X(\mathcal C_X(\gamma^m))$, one mass per lattice point $\beta$.
5. **§6.2 — twisted zeta (Def 6.3, Cor 6.4).** *Define* $L_X(s,\chi)=\prod_\gamma\prod_k(1-\chi([\gamma])e^{-(s+k)\ell_\gamma})$ over the character torus $\widehat H_1\cong(S^1)^r$; *produce* $-\log L_X(s,\chi)=\sum_{\gamma,m}\chi([\gamma])^m\mu^\kappa_X(\mathcal C_X(\gamma^m))$.
6. **§6.2 — Fourier (Thm 6.5).** *Regroup* by homology, $-\log L_X(s,\chi)=\sum_\beta\chi(\beta)\mu^\kappa_X(\beta)$; *invert* by orthogonality of characters, $\mu^\kappa_X(\beta)=\int_{\widehat H_1}(-\log L_X(s,\chi))\,\overline{\chi(\beta)}\,d\chi$.
7. **§6.3 — total homology of the soup (Prop 6.7).** *Given* the loop soup $\mathcal L_\lambda$ and the exponential formula; *produce* the characteristic function $\mathbb E[\chi(\beta(\lambda))]=(Z_X(s)/L_X(s,\chi))^\lambda$ and the exact law $\mathbb P(\beta(\lambda)=\beta)=Z_X(s)^\lambda\int L_X(s,\chi)^{-\lambda}\overline{\chi(\beta)}\,d\chi$.

# C. The results

## §6.1  The probability measure $\mathbb P_s$ on free-homotopy classes

**New symbols (delta from the table):** $\mathbb P_s$ (the measure), $F(s)=-\log Z_X(s)$ (its normalising constant $=$ total mass), $\mathbb E_s,\operatorname{Var}_s$.

**Expansions.** The only object needed beyond the standing recalls is that the normalising constant is finite and positive — that is exactly $F(s)=-\log Z_X(s)\in(0,\infty)$ for $s>\delta$, supplied by the import (24$_\kappa$) and the recall on $\delta$. There is no new jargon; the construction is a division.

> **Construction 6.0 (probability measure on classes).** Fix $\kappa>0$ and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$. Assume:
> **(H1)** the class masses are $\mu^\kappa_X(\mathcal C_X(\gamma^m))=\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}\in(0,\infty)$, $L=m\ell_\gamma$, one per non-trivial non-peripheral class.
> **(H2)** their total is finite and positive: $F(s):=\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\mu^\kappa_X(\mathcal C_X(\gamma^m))=-\log Z_X(s)\in(0,\infty)$.
> **Then** setting
> $$\mathbb P_s\big(\mathcal C_X(\gamma^m)\big):=\frac{\mu^\kappa_X(\mathcal C_X(\gamma^m))}{-\log Z_X(s)}=\frac{\mu^\kappa_X(\mathcal C_X(\gamma^m))}{\displaystyle\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\mu^\kappa_X(\mathcal C_X(\gamma^m))}\tag{6.0}$$
> defines a probability measure on the countable set of non-trivial non-peripheral free-homotopy classes: each atom is positive and the atoms sum to $1$.

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | import (24$_\kappa$), first identity | each class $(\gamma,m)$ | atom $\mu^\kappa_X(\mathcal C_X(\gamma^m))=\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}>0$ |
| 2 | import (24$_\kappa$), second identity | sum step 1 over $\gamma,m$ | $F(s)=-\log Z_X(s)$ |
| 3 | recall on $\delta$, with $s>1\ge\delta$ | $F(s)$ | $F(s)\in(0,\infty)$, so the division (6.0) is legal |
| 4 | divide | step 1 by step 2 | $\sum_{\gamma,m}\mathbb P_s(\mathcal C_X(\gamma^m))=F(s)/F(s)=1$ |

Every symbol is typed above; the block typechecks with nothing off-page.

> [!note]- Proof (skippable — the Discharge is the proof)
> By (24$_\kappa$) each atom is a strictly positive real number, and their sum is the finite positive number $-\log Z_X(s)$ (positive because $\kappa>0$ gives $s>1$, hence each factor $1-e^{-(s+k)\ell_\gamma}\in(0,1)$ and $Z_X(s)\in(0,1)$, so $-\log Z_X(s)>0$; finite because $s>\delta$, §4 finiteness). Dividing every atom by that constant leaves the atoms non-negative and summing to $1$: a probability measure. $\square$

> [!warning] This is not the loop measure normalised
> $\mu^\kappa_X$ itself has **infinite** total mass (the trivial contractible class alone carries $\infty$), so it cannot be normalised. $\mathbb P_s$ normalises only the restriction to non-trivial non-peripheral classes, whose total $-\log Z_X(s)$ is finite precisely because $\kappa>0$. At $\kappa=0$ on a finite-area surface this total diverges ($s=\delta=1$), and one must instead use the renormalised value of §5.

## §6.1 (continued)  Moments: shift equals tilt

**New symbols:** $r$ (a Laplace shift, $s+r>\delta$); $F^{(n)}$ ($n$-th $s$-derivative of $F$); the length $L=m\ell_\gamma$ now read as a **random variable** under $\mathbb P_s$.

**Expansions.** The single analytic fact used is that each atom is smooth in $s$ with $s$-derivative $-L$ times itself — a one-line computation printed in the proof, needing only $\partial_s e^{(1-s)L}=-L\,e^{(1-s)L}$. "Random variable $L$" means: under $\mathbb P_s$, the sample space is the set of classes, and the function assigning to $\mathcal C_X(\gamma^m)$ its geodesic length $L=m\ell_\gamma$ is the observable whose moments we compute — no measure theory beyond the anchor.

> **Result 6.1 (moments and cumulants).** Fix $\kappa>0$, $s=\tfrac12+\sqrt{\tfrac14+\kappa}>\delta$. Assume:
> **(H1)** $\mathbb P_s$ is the measure (6.0), with atoms $\mu^\kappa_X(\mathcal C_X(\gamma^m))=\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$ and total $F(s)=-\log Z_X(s)$.
> **(H2)** $r\in\mathbb R$ with $s+r>\delta$ (so $F(s+r)$ is defined and finite).
> **Then**, with $L$ the class-length random variable:
> $$\partial_s\,\mu^\kappa_X(\mathcal C_X(\gamma^m))=-L\,\mu^\kappa_X(\mathcal C_X(\gamma^m)),\tag{69}$$
> $$\mathbb E_s\big[e^{-rL}\big]=\frac{-\log Z_X(s+r)}{-\log Z_X(s)}=\frac{\log Z_X(s+r)}{\log Z_X(s)},\tag{70}$$
> $$\mathbb E_s\big[L^n\big]=\frac{(-1)^nF^{(n)}(s)}{F(s)}\quad(n\ge1),\tag{71}$$
> $$\mathbb E_s[L]=-\frac{d}{ds}\log\!\big(-\log Z_X(s)\big)=-\frac{F'(s)}{F(s)},\tag{72}$$
> $$\operatorname{Var}_s(L)=\frac{d^2}{ds^2}\log\!\big(-\log Z_X(s)\big)=\frac{F''(s)F(s)-F'(s)^2}{F(s)^2}.\tag{73}$$
> Moreover $\log F$ is strictly convex on $(1,\infty)$, so $\operatorname{Var}_s(L)>0$ and $s\mapsto\mathbb E_s[L]$ is strictly decreasing: **increasing the killing shortens the typical class.**

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | $\partial_s e^{(1-s)L}=-L\,e^{(1-s)L}$ | atom $\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$ | $(69)$: $\partial_s\mu^\kappa_X=-L\,\mu^\kappa_X$ |
| 2 | multiply atom at $s$ by $e^{-rL}$ | $=$ atom at $s+r$ (since $e^{(1-s)L}e^{-rL}=e^{(1-(s+r))L}$) | $\sum_{\gamma,m}\mu^\kappa_X e^{-rL}=F(s+r)$ |
| 3 | divide step 2 by $F(s)$ | definition $\mathbb E_s[e^{-rL}]=\sum\mathbb P_s\,e^{-rL}$ | $(70)$ |
| 4 | differentiate $F=\sum\mu^\kappa_X$ $n$ times, use $(69)$ | $F^{(n)}=\sum(-L)^n\mu^\kappa_X$ | $\sum L^n\mu^\kappa_X=(-1)^nF^{(n)}$, divide by $F$ $\Rightarrow(71)$ |
| 5 | $(71)$ at $n=1,2$; $\mathbb E[L]=-F'/F$, $\mathbb E[L^2]=F''/F$ | $\operatorname{Var}=\mathbb E[L^2]-\mathbb E[L]^2$ | $(72),(73)$; $(\log F)''=(F''F-F'^2)/F^2$ |

Every symbol is typed above; the block typechecks with nothing off-page.

> [!note]- Proof (skippable)
> **(69).** The atom is $\mu^\kappa_X(\mathcal C_X(\gamma^m))=\tfrac1m\,e^{(1-s)m\ell_\gamma}/(e^{m\ell_\gamma}-1)$; only the numerator depends on $s$, and $\partial_s e^{(1-s)m\ell_\gamma}=-(m\ell_\gamma)e^{(1-s)m\ell_\gamma}=-L\,e^{(1-s)m\ell_\gamma}$. Hence $\partial_s\mu^\kappa_X=-L\,\mu^\kappa_X$. Differentiating the convergent series termwise is legal for $s>\delta$ (the differentiated series converges locally uniformly, being dominated by the same geodesic sum with an extra polynomial factor in $L$).
> **(70).** The atom at $s$ times $e^{-rL}$ equals the atom at $s+r$, because $\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}e^{-rL}=\tfrac1m\tfrac{e^{(1-(s+r))L}}{e^L-1}$ and the geometric prefactor $\tfrac1m\tfrac1{e^L-1}$ is $s$-free. Summing over all classes, $\sum_{\gamma,m}\mu^\kappa_X(\mathcal C_X(\gamma^m))e^{-rL}=-\log Z_X(s+r)=F(s+r)$; dividing by $F(s)$ gives $\mathbb E_s[e^{-rL}]=F(s+r)/F(s)$. **Shifting the spectral parameter by $r$ is the same as exponentially tilting the class-length by $r$.** Valid whenever $s+r>\delta$ (the paper's condition $r>1-s$ is this when $\delta=1$, the finite-area case).
> **(71).** Differentiating $F(s)=\sum_{\gamma,m}\mu^\kappa_X(\mathcal C_X(\gamma^m))$ $n$ times and using (69) at each step, $F^{(n)}(s)=\sum_{\gamma,m}(-L)^n\mu^\kappa_X(\mathcal C_X(\gamma^m))=(-1)^n\sum_{\gamma,m}L^n\mu^\kappa_X$. Divide by $F(s)$: $\mathbb E_s[L^n]=\sum L^n\mu^\kappa_X/F=(-1)^nF^{(n)}/F$. (Equivalently, differentiate (70) $n$ times in $r$ at $r=0$.)
> **(72),(73).** $\mathbb E_s[L]=(-1)F'/F=-(\log F)'$. And $\operatorname{Var}_s(L)=\mathbb E_s[L^2]-\mathbb E_s[L]^2=F''/F-(F'/F)^2=(F''F-F'^2)/F^2=(\log F)''$.
> **Monotonicity.** By (73), $\operatorname{Var}_s(L)=(\log F)''\ge0$, and it is a genuine variance of a non-degenerate variable (there are at least two distinct class-lengths), so $(\log F)''>0$: $\log F$ is strictly convex on $(1,\infty)$. Then $\dfrac{d}{ds}\mathbb E_s[L]=-(\log F)''<0$, so $s\mapsto\mathbb E_s[L]$ strictly decreases. Since larger $s$ means larger $\kappa$, more killing shortens the typical class. $\square$

## §6.1 (continued)  Concentration on the systole as $\kappa\to\infty$

**New symbols:** $\ell_{\mathrm{sys}}:=\min_{\gamma\in\mathcal P_X}\ell_\gamma>0$ (the **systole** — the length of the shortest closed geodesic); $N_{\mathrm{sys}}:=\#\{\gamma\in\mathcal P_X:\ell_\gamma=\ell_{\mathrm{sys}}\}$ (how many primitive classes attain it).

**Expansions.** The systole exists and is positive because geometric finiteness makes $\{\gamma:\ell_\gamma\le R\}$ finite for every $R$, so the infimum of lengths is a minimum. The one structural fact is that **oriented** primitive geodesics come in mirror pairs of equal length that are never the same class:

**Used here — $N_{\mathrm{sys}}\ge2$:** the systolic length is attained by at least two classes, so the limit measure is genuinely spread out.
> [!def]+ Orientation-reversal and $N_{\mathrm{sys}}\ge2$
> $\mathcal P_X$ consists of **oriented** primitive closed geodesics: reversing orientation sends $\gamma$ to $\gamma^{-1}$ (group side: $\tau\mapsto\tau^{-1}$), of the same length $\ell_{\gamma^{-1}}=\ell_\gamma$. A **hyperbolic element $\tau$ of a torsion-free Fuchsian group is never conjugate to its inverse** — $\tau$ and $\tau^{-1}$ translate along the same axis in opposite directions, and no orientation-preserving isometry in $\Gamma\subseteq\mathrm{PSL}(2,\mathbb R)$ can swap the two endpoints of that axis while fixing the group. Hence $\gamma\ne\gamma^{-1}$ as free-homotopy classes, and every systolic geodesic contributes its distinct reverse. Therefore $N_{\mathrm{sys}}=\#\{\gamma\in\mathcal P_X:\ell_\gamma=\ell_{\mathrm{sys}}\}\ge2$.

> **Result 6.2 (concentration on the systole).** Fix $\kappa>0$ and let $s=\tfrac12+\sqrt{\tfrac14+\kappa}\to\infty$ (equivalently $\kappa\to\infty$). Assume:
> **(H1)** $\mathbb P_s$ is the measure (6.0) with atoms $\mu^\kappa_X(\mathcal C_X(\gamma^m))=\tfrac1m\,e^{-sm\ell_\gamma}/(1-e^{-m\ell_\gamma})$ (the same atom, rewritten by multiplying numerator and denominator by $e^{-L}$).
> **(H2)** the systole $\ell_{\mathrm{sys}}=\min_\gamma\ell_\gamma>0$ is attained by exactly $N_{\mathrm{sys}}\ge2$ primitive classes.
> **Then** as $s\to\infty$:
> $$\mathbb P_s\big(\mathcal C_X(\gamma)\big)\to\frac1{N_{\mathrm{sys}}}\ \text{ for each primitive }\gamma\text{ with }\ell_\gamma=\ell_{\mathrm{sys}},\qquad \mathbb P_s\big(\mathcal C_X(\gamma^m)\big)\to0\ \text{ for every other class},$$
> $$\mathbb E_s[L]\to\ell_{\mathrm{sys}},\qquad -\log Z_X(s)\ \sim\ C\,e^{-s\ell_{\mathrm{sys}}}\ \ \text{with}\ \ C=\frac{N_{\mathrm{sys}}}{1-e^{-\ell_{\mathrm{sys}}}},$$
> and both invariants are recovered from the asymptotics of the total mass:
> $$\ell_{\mathrm{sys}}=-\lim_{s\to\infty}\frac1s\log\!\big(-\log Z_X(s)\big),\qquad N_{\mathrm{sys}}=\big(1-e^{-\ell_{\mathrm{sys}}}\big)\lim_{s\to\infty}e^{s\ell_{\mathrm{sys}}}\big(-\log Z_X(s)\big).$$

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | rewrite atom $\times\,e^{-L}/e^{-L}$ | $\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$ | atom $=\tfrac1m\,e^{-sL}/(1-e^{-L})$, so leading order $e^{-sL}$ |
| 2 | compare exponents $e^{-sL}$, $L=m\ell_\gamma\ge\ell_{\mathrm{sys}}$ | the class family | slowest decay at $m=1,\ \ell_\gamma=\ell_{\mathrm{sys}}$: exactly the $N_{\mathrm{sys}}$ systolic classes |
| 3 | sum step 1 over classes, keep leading terms | $F(s)=-\log Z_X(s)$ | $F(s)\sim N_{\mathrm{sys}}\tfrac{e^{-s\ell_{\mathrm{sys}}}}{1-e^{-\ell_{\mathrm{sys}}}}=C e^{-s\ell_{\mathrm{sys}}}$ |
| 4 | divide systolic atom by $F(s)$ | (6.0) | $\mathbb P_s(\mathcal C_X(\gamma))\to1/N_{\mathrm{sys}}$; all others $\to0$ |
| 5 | $\mathbb E_s[L]=\sum L\,\mathbb P_s$, mass $\to$ systolic classes at $L=\ell_{\mathrm{sys}}$ | $(72)$ | $\mathbb E_s[L]\to\ell_{\mathrm{sys}}$ |
| 6 | invert $F(s)\sim Ce^{-s\ell_{\mathrm{sys}}}$ | take $-\tfrac1s\log F$ and $e^{s\ell_{\mathrm{sys}}}F$ | recover $\ell_{\mathrm{sys}},N_{\mathrm{sys}}$ |

Every symbol is typed above; the block typechecks with nothing off-page.

> [!note]- Proof (skippable)
> **Atom rewrite.** $\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}=\tfrac1m\tfrac{e^{(1-s)L}e^{-L}}{1-e^{-L}}=\tfrac1m\tfrac{e^{-sL}}{1-e^{-L}}$. As $s\to\infty$ each atom decays like $e^{-sL}$, and $L=m\ell_\gamma\ge\ell_{\mathrm{sys}}$ with equality exactly for the $N_{\mathrm{sys}}$ primitive systolic classes ($m=1$, $\ell_\gamma=\ell_{\mathrm{sys}}$). Every non-systolic class has $L\ge\ell_{\mathrm{sys}}+\epsilon$ for some $\epsilon>0$ (discreteness of the length spectrum) or $m\ge2$, so its atom is $O(e^{-s(\ell_{\mathrm{sys}}+\epsilon)})$, exponentially smaller.
> **Total mass asymptotic.** The $N_{\mathrm{sys}}$ systolic atoms each equal $\tfrac{e^{-s\ell_{\mathrm{sys}}}}{1-e^{-\ell_{\mathrm{sys}}}}(1+o(1))$; all other terms are lower order. Hence $-\log Z_X(s)=\sum_{\gamma,m}\tfrac1m\tfrac{e^{-sL}}{1-e^{-L}}\sim N_{\mathrm{sys}}\tfrac{e^{-s\ell_{\mathrm{sys}}}}{1-e^{-\ell_{\mathrm{sys}}}}=Ce^{-s\ell_{\mathrm{sys}}}$.
> **Uniform limit.** For a systolic $\gamma$, $\mathbb P_s(\mathcal C_X(\gamma))=\dfrac{e^{-s\ell_{\mathrm{sys}}}/(1-e^{-\ell_{\mathrm{sys}}})}{Ce^{-s\ell_{\mathrm{sys}}}}(1+o(1))=\dfrac1{N_{\mathrm{sys}}}(1+o(1))$; a non-systolic class has numerator exponentially smaller than the denominator, so its probability $\to0$. The mass thus spreads uniformly over the $N_{\mathrm{sys}}$ shortest oriented geodesics.
> **Mean.** $\mathbb E_s[L]=\sum_{\gamma,m}L\,\mathbb P_s(\mathcal C_X(\gamma^m))$; all but a $o(1)$ fraction of the mass sits on classes of length $\ell_{\mathrm{sys}}$, so $\mathbb E_s[L]\to\ell_{\mathrm{sys}}$ (consistent with (72), $-(\log F)'\to\ell_{\mathrm{sys}}$ since $\log F\sim\log C-s\ell_{\mathrm{sys}}$).
> **Recovery.** From $F(s)\sim Ce^{-s\ell_{\mathrm{sys}}}$: $\ -\tfrac1s\log F(s)=\ell_{\mathrm{sys}}-\tfrac1s\log C+o(1/s)\to\ell_{\mathrm{sys}}$, and $e^{s\ell_{\mathrm{sys}}}F(s)\to C=N_{\mathrm{sys}}/(1-e^{-\ell_{\mathrm{sys}}})$, so $N_{\mathrm{sys}}=(1-e^{-\ell_{\mathrm{sys}}})\lim_{s\to\infty}e^{s\ell_{\mathrm{sys}}}F(s)$. The systole and its multiplicity are read off the tail of a single spectral function. $\square$

## §6.2  Mass in a homology class (Definition 6.1)

**New symbols:** $H_1(X,\mathbb Z)\cong\mathbb Z^r$ (first homology); $g,b,n_C,n_F$ (genus; ends, of which cusps and funnels); $[\gamma]\in H_1(X,\mathbb Z)$ (homology image of $\gamma$); $\beta$ (a homology class); $\mu^\kappa_X(\beta)$ (its mass).

**Expansions.** Free homotopy remembers the *order* in which handles are traversed (it is a conjugacy class in the generally non-abelian $\pi_1$); homology forgets that, keeping only net winding. The passage is the abelianisation map, and the rank is fixed by the topology of $X$.

**Used here — homology as the abelianisation:** it turns the fine partition by conjugacy class into a coarse partition indexed by a lattice $\mathbb Z^r$, on which $[\gamma^m]=m[\gamma]$, so a whole homology class collects infinitely many free-homotopy classes.
> [!def]+ $H_1(X,\mathbb Z)$, the first homology group
> $H_1(X,\mathbb Z)$ is the **abelianisation** of $\pi_1(X)\cong\Gamma$: the quotient $\Gamma/[\Gamma,\Gamma]$ by the commutator subgroup (the **Hurewicz theorem** identifies it with the first singular homology). It records only the *net winding* around each independent cycle, discarding the non-abelian order-of-traversal information. It is a finitely generated free abelian group, $H_1(X,\mathbb Z)\cong\mathbb Z^r$, of rank $r=2g$ when $X$ is closed of genus $g$, and $r=2g+b-1$ when $X$ has $b\ge1$ ends (with $b=n_C+n_F$, $n_C$ cusps and $n_F$ funnels, so $r=2g+n_C+n_F-1$). Write $\Gamma\twoheadrightarrow H_1(X,\mathbb Z)$ for the abelianisation map and $[\gamma]$ for the image of a primitive $\gamma\in\mathcal P_X$; then $[\gamma^m]=m[\gamma]$ (winding $m$ times multiplies the homology class by $m$).

> **Definition 6.1 (mass of the killed loop measure in a homology class).** For $\beta\in H_1(X,\mathbb Z)$, $\kappa>0$ and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}s>\delta$, the mass of the killed Brownian loop measure in homology class $\beta$ is
> $$\mu^\kappa_X(\beta):=\sum_{\substack{\gamma\in\mathcal P_X,\,m\ge1\\ m[\gamma]=\beta}}\mu^\kappa_X\big(\mathcal C_X(\gamma^m)\big)=\sum_{\substack{\gamma\in\mathcal P_X,\,m\ge1\\ m[\gamma]=\beta}}\frac1m\cdot\frac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}.\tag{74}$$
> The sum is over the infinitely many free-homotopy classes whose iterate lands in the fixed lattice point $\beta$; it is a sub-sum of the absolutely convergent total (24$_\kappa$), hence finite.

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | abelianisation $\Gamma\twoheadrightarrow\mathbb Z^r$, $[\gamma^m]=m[\gamma]$ | each class $(\gamma,m)$ | a well-defined image $\beta=m[\gamma]\in H_1(X,\mathbb Z)$ |
| 2 | partition classes by the value of $\beta$ | the class set | each $\beta$ gets the sub-collection $\{(\gamma,m):m[\gamma]=\beta\}$ |
| 3 | sum atoms (24$_\kappa$) over that sub-collection | the atoms | $\mu^\kappa_X(\beta)$, a sub-sum of the finite total $-\log Z_X(s)$ |

Every symbol is typed above; the block typechecks with nothing off-page.

> [!note]- Proof (skippable — it is a definition; only finiteness needs a word)
> Each atom $\mu^\kappa_X(\mathcal C_X(\gamma^m))>0$; the sum defining $\mu^\kappa_X(\beta)$ is a sub-sum of $\sum_{\gamma,m}\mu^\kappa_X(\mathcal C_X(\gamma^m))=-\log Z_X(s)<\infty$ (import (24$_\kappa$), $s>\delta$), hence converges to a finite non-negative number. It is $0$ only for the classes containing no closed geodesic (the trivial and peripheral ones, already excluded). $\square$

## §6.2 (continued)  The character torus and the Selberg $L$-function (Definition 6.3, Corollary 6.4)

**New symbols:** $\widehat H_1$ (character torus / Pontryagin dual); $\chi$ (unitary character); $d\chi$ (normalised Haar measure); $L_X(s,\chi)$ (Selberg $L$-function).

**Expansions.** Because $\mu^\kappa_X(\beta)$ collects infinitely many free-homotopy classes with no closed form, we do not compute it directly. Instead we detect the distribution of geodesics across homology by testing against characters — the exact analogue of Dirichlet characters detecting primes in arithmetic progressions. The characters form a compact torus dual to the lattice $\mathbb Z^r$.

**Used here — the character torus:** it is the compact abelian group over which we will integrate to Fourier-invert the homology masses; each $\chi$ is a phase per generator.
> [!def]+ $\widehat H_1$, the character torus (Pontryagin dual)
> A **character** of $H_1(X,\mathbb Z)$ is a group homomorphism $\chi:H_1(X,\mathbb Z)\to\mathbb C^\times$; it is **unitary** if it lands in the unit circle, $\chi:H_1(X,\mathbb Z)\to S^1$. The unitary characters form the **character torus** (the **Pontryagin dual**) $\widehat H_1(X,\mathbb Z)$. Since $H_1(X,\mathbb Z)\cong\mathbb Z^r$, a unitary character is fixed by its values on a $\mathbb Z$-basis $e_1,\dots,e_r$: choosing phases $\theta_1,\dots,\theta_r\in\mathbb R/\mathbb Z$ and setting $\chi(e_j)=e^{2\pi i\theta_j}$ gives
> $$\widehat H_1(X,\mathbb Z)\cong(S^1)^r\cong(\mathbb R/\mathbb Z)^r,$$
> a compact real torus carrying a unique translation-invariant probability measure, the **normalised Haar measure** $d\chi$. Unitarity gives $|\chi(\beta)|=1$ for every $\beta$, and $\overline{\chi(\beta)}=\chi(-\beta)=\chi(\beta)^{-1}$.

> **Definition 6.3 (Selberg $L$-function).** For a unitary character $\chi\in\widehat H_1(X,\mathbb Z)$ and $\operatorname{Re}s>\delta$,
> $$L_X(s,\chi):=\prod_{\gamma\in\mathcal P_X}\ \prod_{k=0}^{\infty}\Big(1-\chi([\gamma])\,e^{-(s+k)\ell_\gamma}\Big).\tag{75}$$
> It is the Selberg zeta twisted by the one-dimensional abelian representation $\chi$; when $\chi=\mathbf 1$ is trivial, $L_X(s,\mathbf 1)=Z_X(s)$.

> **Corollary 6.4 (Selberg $L$-function identity).** Let $\chi\in\widehat H_1(X,\mathbb Z)$ be a unitary character and $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}s>\delta$. Assume:
> **(H1)** $L_X(s,\chi)$ is the product (75); $|\chi([\gamma])|=1$.
> **(H2)** the class masses are $\mu^\kappa_X(\mathcal C_X(\gamma^m))=\tfrac1m\tfrac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$.
> **Then**
> $$-\log L_X(s,\chi)=\sum_{\gamma\in\mathcal P_X}\sum_{m=1}^\infty\chi([\gamma])^m\,\mu^\kappa_X\big(\mathcal C_X(\gamma^m)\big)=\sum_{\gamma\in\mathcal P_X}\sum_{m=1}^\infty\frac1m\cdot\frac{\chi([\gamma])^m\,e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1},\tag{76}$$
> absolutely convergent for $\operatorname{Re}s>\delta$.

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | unitarity $\|\chi([\gamma])e^{-(s+k)\ell_\gamma}\|=e^{-(\operatorname{Re}s+k)\ell_\gamma}<1$ | each factor of (75) | may take $\log$ term by term; product converges absolutely for $\operatorname{Re}s>\delta$ |
| 2 | $-\log(1-z)=\sum_{m\ge1}z^m/m$, $z=\chi([\gamma])e^{-(s+k)\ell_\gamma}$ | $-\log$ of each factor | $-\log(1-z)=\sum_m\tfrac1m\chi([\gamma])^m e^{-(s+k)m\ell_\gamma}$ |
| 3 | sum over $k\ge0$: $\sum_k e^{-(s+k)m\ell_\gamma}=\tfrac{e^{-sm\ell_\gamma}}{1-e^{-m\ell_\gamma}}=\tfrac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}$ | the inner $k$-series | summand $\tfrac1m\chi([\gamma])^m\tfrac{e^{(1-s)m\ell_\gamma}}{e^{m\ell_\gamma}-1}=\chi([\gamma])^m\mu^\kappa_X$ |
| 4 | collect over $\gamma,m$ | steps 2–3 | $(76)$ |

Every symbol is typed above; the block typechecks with nothing off-page.

> [!note]- Proof (skippable)
> For $\operatorname{Re}s>\delta$ the Euler product (75) converges absolutely, so one may take logarithms term by term. Set $z=\chi([\gamma])e^{-(s+k)\ell_\gamma}$; since $\chi$ is unitary, $|z|=e^{-(\operatorname{Re}s+k)\ell_\gamma}<1$, and $-\log(1-z)=\sum_{m\ge1}z^m/m=\sum_{m\ge1}\tfrac1m\chi([\gamma])^m e^{-(s+k)m\ell_\gamma}$. Summing the inner geometric series over $k\ge0$ gives $\sum_{k\ge0}e^{-(s+k)m\ell_\gamma}=e^{-sm\ell_\gamma}/(1-e^{-m\ell_\gamma})=e^{(1-s)m\ell_\gamma}/(e^{m\ell_\gamma}-1)$. Hence the $(\gamma,m)$ summand is $\tfrac1m\chi([\gamma])^m e^{(1-s)m\ell_\gamma}/(e^{m\ell_\gamma}-1)=\chi([\gamma])^m\mu^\kappa_X(\mathcal C_X(\gamma^m))$. This is exactly the untwisted expansion (F1) with each summand carrying the extra phase $\chi([\gamma])^m$. $\square$

## §6.2 (continued)  Fourier expansion and inversion by homology (Theorem 6.5)

**New symbols:** none beyond $\widehat H_1,\chi,d\chi,\mu^\kappa_X(\beta)$.

**Expansions.** The twist $\chi([\gamma])^m$ depends only on the homology $m[\gamma]$, so the double sum in (76) can be regrouped by homology class — turning $-\log L_X(s,\chi)$ into an honest Fourier series on the torus $\widehat H_1$ with the homology masses as coefficients. Recovering a coefficient is Fourier inversion, i.e. orthogonality of characters, an anchor.

**Used here — the twist is a homology invariant:** $\chi([\gamma])^m=\chi(m[\gamma])=\chi(\beta)$ whenever $m[\gamma]=\beta$, which is exactly what lets the double sum be regrouped by $\beta$.
> [!def]+ Why $\chi([\gamma])^m=\chi(\beta)$
> $\chi$ is a group homomorphism and $[\gamma^m]=m[\gamma]$, so $\chi([\gamma])^m=\chi(m[\gamma])=\chi([\gamma^m])$. If $m[\gamma]=\beta$ then $\chi([\gamma])^m=\chi(\beta)$ — the phase attached to a free-homotopy class in (76) is constant across all classes sharing a homology class $\beta$. This is the precise sense in which passing to $L$-functions is adapted to homology, not just homotopy.

**Used here — orthogonality of characters:** the integral of a character over the torus isolates a single lattice coefficient, giving the inversion.
> [!import]- Orthogonality of characters on $(S^1)^r$ — Says / Needs / Gives
> **Says.** For $\beta,\beta'\in H_1(X,\mathbb Z)\cong\mathbb Z^r$, with $d\chi$ the normalised Haar measure on $\widehat H_1\cong(S^1)^r$:
> $$\int_{\widehat H_1}\chi(\beta')\,\overline{\chi(\beta)}\,d\chi=\begin{cases}1,&\beta'=\beta,\\ 0,&\beta'\ne\beta.\end{cases}$$
> **Needs.** $\widehat H_1\cong(S^1)^r$ compact with normalised Haar $d\chi$; $\chi(\beta'-\beta)=\prod_j e^{2\pi i(\beta'-\beta)_j\theta_j}$.
> **Gives.** Fourier inversion on the lattice $\mathbb Z^r$: integrating an absolutely convergent character series against $\overline{\chi(\beta)}$ returns the single coefficient at $\beta$. This is ordinary Fourier analysis on the torus (anchor); **not a gap** — assume freely.

> **Theorem 6.5 (Fourier expansion and inversion by homology class).** Let $X=\Gamma\backslash\mathbb H^2$ be geometrically finite with $H_1(X,\mathbb Z)\cong\mathbb Z^r$ ($r=2g+b-1$ for $b\ge1$ ends, $r=2g$ closed), $\kappa\ge-\tfrac14$ with $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ and $\operatorname{Re}s>\delta$. Assume:
> **(H1)** the twisted identity (76): $-\log L_X(s,\chi)=\sum_{\gamma,m}\chi([\gamma])^m\mu^\kappa_X(\mathcal C_X(\gamma^m))$, absolutely convergent.
> **(H2)** the homology masses (74): $\mu^\kappa_X(\beta)=\sum_{m[\gamma]=\beta}\mu^\kappa_X(\mathcal C_X(\gamma^m))$.
> **(H3)** orthogonality of characters on $\widehat H_1\cong(S^1)^r$ against normalised Haar $d\chi$.
> **Then** for every unitary character $\chi\in\widehat H_1$,
> $$-\log L_X(s,\chi)=\sum_{\beta\in H_1(X,\mathbb Z)}\chi(\beta)\,\mu^\kappa_X(\beta),\tag{77}$$
> an absolutely convergent Fourier expansion, and for each $\beta\in H_1(X,\mathbb Z)$ the inversion
> $$\mu^\kappa_X(\beta)=\int_{\widehat H_1(X,\mathbb Z)}\big(-\log L_X(s,\chi)\big)\,\overline{\chi(\beta)}\,d\chi.\tag{78}$$

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | homology-invariance $\chi([\gamma])^m=\chi(\beta)$ for $m[\gamma]=\beta$ | (76) summand | regroup double sum by $\beta$ |
| 2 | (H2) to name the inner sum | $\sum_{m[\gamma]=\beta}\mu^\kappa_X(\mathcal C_X(\gamma^m))$ | $=\mu^\kappa_X(\beta)$, giving $(77)$: $-\log L_X=\sum_\beta\chi(\beta)\mu^\kappa_X(\beta)$ |
| 3 | multiply (77) by $\overline{\chi(\beta)}$, integrate $d\chi$; interchange (abs. conv.) | $\int_{\widehat H_1}(\cdots)\overline{\chi(\beta)}d\chi$ | $\sum_{\beta'}\mu^\kappa_X(\beta')\int\chi(\beta')\overline{\chi(\beta)}d\chi$ |
| 4 | (H3) orthogonality | inner integral $=\mathbf 1_{\beta'=\beta}$ | only $\beta'=\beta$ survives $\Rightarrow(78)$ |

Every symbol is typed above; the block typechecks with nothing off-page.

> [!note]- Proof (skippable)
> **(77).** In (76) group all $(\gamma,m)$ with the same homology class $\beta=m[\gamma]$. For those pairs $\chi([\gamma])^m=\chi(\beta)$ (homology-invariance), so
> $$-\log L_X(s,\chi)=\sum_{\beta\in H_1(X,\mathbb Z)}\Bigg(\sum_{\substack{\gamma,m\\ m[\gamma]=\beta}}\mu^\kappa_X(\mathcal C_X(\gamma^m))\Bigg)\chi(\beta)=\sum_{\beta}\mu^\kappa_X(\beta)\,\chi(\beta),$$
> using (74) for the inner sum. Absolute convergence of (76) permits the regrouping, and makes this a genuine (absolutely convergent) Fourier series on $\widehat H_1$ with coefficients $\mu^\kappa_X(\beta)$.
> **(78).** Multiply (77) by $\overline{\chi(\beta)}$ and integrate over $\widehat H_1$ against $d\chi$. Absolute convergence lets us interchange sum and integral:
> $$\int_{\widehat H_1}\big(-\log L_X(s,\chi)\big)\overline{\chi(\beta)}\,d\chi=\sum_{\beta'\in H_1(X,\mathbb Z)}\mu^\kappa_X(\beta')\int_{\widehat H_1}\chi(\beta')\overline{\chi(\beta)}\,d\chi.$$
> By orthogonality (H3) the inner integral is $1$ if $\beta'=\beta$ and $0$ otherwise, so only the $\beta'=\beta$ term survives, giving (78). $\square$

> [!note]- Remark 6.6 — the closed case over the Jacobian (decorative; used by nothing later)
> When $X$ is closed the character torus has a classical avatar. By the **Hodge theorem** every de Rham cohomology class has a unique harmonic representative, $H^1_{\mathrm{dR}}(X,\mathbb R)\cong\mathcal H^1(X)$ (real harmonic $1$-forms), and $H_1(X,\mathbb Z)$ sits inside as the lattice $\mathcal H^1_{\mathbb Z}(X)$ of harmonic $1$-forms with integer periods. To $\omega$ one attaches the unitary holonomy character $\chi_\omega(\beta)=e^{2\pi i\int_\beta\omega}$, and two forms give the same character iff their periods differ by integers, so
> $$\widehat H_1(X,\mathbb Z)\cong\frac{H^1_{\mathrm{dR}}(X,\mathbb R)}{H^1(X,\mathbb Z)}\cong\frac{\mathcal H^1(X)}{\mathcal H^1_{\mathbb Z}(X)}\cong\operatorname{Jac}(X),$$
> the **Jacobian variety** (the Hodge star $*^2=-1$ makes the $2g$-real-dimensional torus a complex torus of dimension $g$; with the intersection pairing it is a principally polarised abelian variety). Under $\widehat H_1\cong\operatorname{Jac}(X)$ the pairing is $\langle\beta,[\omega]\rangle=\int_\beta\omega\pmod{\mathbb Z}$, so the inversion (78) may be rewritten
> $$\mu^\kappa_X(\beta)=\int_{\operatorname{Jac}(X)}\big(-\log L_X(s,\chi_{[\omega]})\big)\,e^{-2\pi i\int_\beta\omega}\,d[\omega].\tag{79}$$
> This is a rewrite of the same integral over the same torus; it uses shallow Hodge theory (import, not a gap) and no later result needs it. In the non-compact case the Jacobian identification is unavailable.

## §6.3  The total homology of the loop soup (Proposition 6.7)

**New symbols:** $\mathcal L_\lambda$ (loop soup of intensity $\lambda$); $\mathcal L^*_\lambda$ (its non-contractible non-peripheral loops); $\beta(\lambda)=\sum_{\eta\in\mathcal L^*_\lambda}[\eta]$ (its total homology, a random lattice point).

**Expansions.** The construction so far assigned deterministic masses to classes; now sample the whole soup — a Poisson cloud of loops — and add up the homology of every non-trivial loop. Because the soup is Poissonian, its characteristic function is computed in one line by the exponential (Campbell / Lévy–Khintchine) formula, and the answer is a ratio of zeta and $L$-functions.

**Used here — the exponential formula:** it converts the expected product of a per-loop weight over a Poisson soup into the exponential of a single integral against the intensity, which the $L$-function identity evaluates in closed form.
> [!import]- Exponential formula for a Poisson point process (§3.3) — Says / Needs / Gives
> **Says.** If $\mathcal L$ is a Poisson point process of intensity measure $\nu$ and $F$ is measurable on loops, then
> $$\mathbb E\Big[\prod_{\eta\in\mathcal L}e^{F(\eta)}\Big]=\exp\Big(\int\big(e^{F(\eta)}-1\big)\,\nu(d\eta)\Big).$$
> **Needs.** $\nu$ $\sigma$-finite; $\int(e^{\operatorname{Re}F}-1)^+\,d\nu<\infty$ (here $\nu=\lambda\mu^\kappa_X$ restricted to non-trivial non-peripheral loops with $\int|e^{F}-1|d\nu\le2\lambda(-\log Z_X(s))<\infty$, since $|e^{F}|=|\chi([\eta])|=1$).
> **Gives.** the characteristic functional of the total homology in closed form. Assume freely; §3.3 records it for the loop soup (a standard Campbell/Poisson computation) — **not a deep gap.**

> **Proposition 6.7 (distribution of the total homology of the loop soup).** Let $s=\tfrac12+\sqrt{\tfrac14+\kappa}$ with $\operatorname{Re}s>\delta$ ($\kappa>0$), let $\mathcal L_\lambda$ be the loop soup of intensity $\lambda>0$ (Poisson with intensity $\lambda\mu^\kappa_X$), and let
> $$\beta(\lambda):=\sum_{\eta\in\mathcal L^*_\lambda}[\eta]\in H_1(X,\mathbb Z)$$
> be the total homology of the non-contractible, non-cusp loops $\mathcal L^*_\lambda$. Assume:
> **(H1)** $\#\mathcal L^*_\lambda\sim\operatorname{Poisson}\!\big(\lambda\sum_{\gamma,m}\mu^\kappa_X(\mathcal C_X(\gamma^m))\big)=\operatorname{Poisson}\!\big(-\lambda\log Z_X(s)\big)$, so $\beta(\lambda)$ is an a.s.-finite sum.
> **(H2)** the exponential formula for the Poisson soup, and the $L$-function identity (76).
> **Then** for every unitary character $\chi\in\widehat H_1$,
> $$\mathbb E\big[\chi(\beta(\lambda))\big]=\Big(\frac{Z_X(s)}{L_X(s,\chi)}\Big)^{\lambda},\tag{80}$$
> and consequently, for each $\beta\in H_1(X,\mathbb Z)$,
> $$\mathbb P\big(\beta(\lambda)=\beta\big)=Z_X(s)^{\lambda}\int_{\widehat H_1(X,\mathbb Z)}L_X(s,\chi)^{-\lambda}\,\overline{\chi(\beta)}\,d\chi,\tag{81}$$
> with $L_X(s,\chi)^{-\lambda}:=\exp(-\lambda\log L_X(s,\chi))$ and $\log L_X(s,\chi)$ given by (76).

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | set $e^{F(\eta)}=\chi([\eta])$; then $\prod_{\eta\in\mathcal L^*_\lambda}e^{F(\eta)}=\chi\big(\sum_\eta[\eta]\big)=\chi(\beta(\lambda))$ | the soup product | LHS of exponential formula $=\mathbb E[\chi(\beta(\lambda))]$ |
| 2 | exponential formula, $\nu=\lambda\mu^\kappa_X$ | RHS $\exp\big(\lambda\sum_{\gamma,m}(\chi([\gamma])^m-1)\mu^\kappa_X(\mathcal C_X(\gamma^m))\big)$ | split the sum |
| 3 | (76) twice: $\sum\chi([\gamma])^m\mu^\kappa_X=-\log L_X$, $\sum\mu^\kappa_X=-\log Z_X$ | the bracket | $\exp(-\lambda\log L_X+\lambda\log Z_X)=(Z_X/L_X)^\lambda$, i.e. $(80)$ |
| 4 | Fourier-invert on $\mathbb Z^r$: $\mathbb P(\beta(\lambda)=\beta)=\int\mathbb E[\chi(\beta(\lambda))]\overline{\chi(\beta)}d\chi$ | $(80)$ | $Z_X(s)^\lambda\int L_X(s,\chi)^{-\lambda}\overline{\chi(\beta)}d\chi$, i.e. $(81)$ |

Every symbol is typed above; the block typechecks with nothing off-page.

> [!note]- Proof (skippable)
> **(80).** Apply the exponential formula to the Poisson soup with intensity $\lambda\mu^\kappa_X$ and $F(\eta)$ defined by $e^{F(\eta)}=\chi([\eta])$ on $\mathcal L^*_\lambda$ (and $F=0$ on contractible/peripheral loops, which contribute trivial homology). Since $\chi$ is a homomorphism, $\prod_{\eta\in\mathcal L^*_\lambda}\chi([\eta])=\chi\big(\sum_{\eta}[\eta]\big)=\chi(\beta(\lambda))$, so the left side is $\mathbb E[\chi(\beta(\lambda))]$. The right side is
> $$\exp\Big(\lambda\sum_{\gamma\in\mathcal P_X}\sum_{m\ge1}\big(\chi([\gamma])^m-1\big)\mu^\kappa_X(\mathcal C_X(\gamma^m))\Big).$$
> By the $L$-function identity (76), $\sum_{\gamma,m}\chi([\gamma])^m\mu^\kappa_X=-\log L_X(s,\chi)$; applying (76) to the trivial character (where $\chi([\gamma])^m\equiv1$ and $L_X(s,\mathbf 1)=Z_X$) gives $\sum_{\gamma,m}\mu^\kappa_X=-\log Z_X(s)$. Hence the exponent is $\lambda\big(-\log L_X(s,\chi)-(-\log Z_X(s))\big)=\lambda\log\!\big(Z_X(s)/L_X(s,\chi)\big)$, so $\mathbb E[\chi(\beta(\lambda))]=(Z_X(s)/L_X(s,\chi))^\lambda$.
> **(81).** Equation (80) is the characteristic function of the $\mathbb Z^r$-valued random variable $\beta(\lambda)$ evaluated at $\chi\in\widehat H_1$. Fourier inversion on $\mathbb Z^r$ against the character torus (orthogonality of characters, (H3) of Theorem 6.5) recovers the point masses:
> $$\mathbb P(\beta(\lambda)=\beta)=\int_{\widehat H_1}\mathbb E[\chi(\beta(\lambda))]\,\overline{\chi(\beta)}\,d\chi=\int_{\widehat H_1}\Big(\frac{Z_X(s)}{L_X(s,\chi)}\Big)^\lambda\overline{\chi(\beta)}\,d\chi=Z_X(s)^\lambda\int_{\widehat H_1}L_X(s,\chi)^{-\lambda}\overline{\chi(\beta)}\,d\chi,$$
> the last equality because $Z_X(s)^\lambda$ is a $\chi$-independent constant. $\square$

> [!note]- Verification of the exponent split in (80) (skippable)
> The only step that could hide an error is $\sum_{\gamma,m}(\chi([\gamma])^m-1)\mu^\kappa_X=-\log L_X+\log Z_X$. Write $A:=\sum_{\gamma,m}\chi([\gamma])^m\mu^\kappa_X(\mathcal C_X(\gamma^m))$ and $B:=\sum_{\gamma,m}\mu^\kappa_X(\mathcal C_X(\gamma^m))$. Then the exponent is $\lambda(A-B)$. By (76), $A=-\log L_X(s,\chi)$; by (76) at $\chi=\mathbf 1$, $B=-\log Z_X(s)$. So $\lambda(A-B)=\lambda(-\log L_X+\log Z_X)=\lambda\log(Z_X/L_X)$, and exponentiating gives $(Z_X/L_X)^\lambda$. At $\chi=\mathbf 1$ this is $1$ (as it must: $\beta(\lambda)$'s characteristic function at the trivial character is $\mathbb E[1]=1$), and taking $\lambda\to0$ gives $1$ (empty soup). Both sanity checks pass.

# D. Exports, climb, commentary

**Exports (what later sections consume).** §6 is a **terminal** section on the surface: §7 changes dimension (to hyperbolic $3$-manifolds) and reruns §3, not §6. The results below are consumed only internally within §6 and by the reader's understanding of the whole construction.
- **(E1)** the probability measure $\mathbb P_s$ (6.0) and its moment machinery: $\mathbb E_s[e^{-rL}]=\log Z_X(s+r)/\log Z_X(s)$, $\mathbb E_s[L^n]=(-1)^nF^{(n)}/F$, $\mathbb E_s[L]=-(\log F)'$, $\operatorname{Var}_s(L)=(\log F)''$ — the loop-geometry statistics of a hyperbolic surface as spectral derivatives.
- **(E2)** the concentration law: as $\kappa\to\infty$, $\mathbb P_s\to$ uniform on the $N_{\mathrm{sys}}\ge2$ systolic classes, and $\ell_{\mathrm{sys}},N_{\mathrm{sys}}$ are read off the tail of $-\log Z_X(s)$.
- **(E3)** the homology dictionary: $-\log L_X(s,\chi)=\sum_\beta\chi(\beta)\mu^\kappa_X(\beta)$ (Fourier), $\mu^\kappa_X(\beta)=\int(-\log L_X)\overline{\chi(\beta)}d\chi$ (inversion), and the exact law $\mathbb P(\beta(\lambda)=\beta)=Z_X(s)^\lambda\int L_X(s,\chi)^{-\lambda}\overline{\chi(\beta)}d\chi$ of the loop soup's total homology.

**Climb (optional — none is needed to typecheck §6).** Sibling sections and the ledger, all deletable with zero loss: [[§2 The Loop Measure and Subordination]] · [[§3 Mass of a Homotopy Class]] · [[§4 Zeta Identities and Finiteness]] · [[§5 Determinants and the Polyakov Anomaly]] · [[§7 Hyperbolic 3-Manifolds]] · [[External Inputs and Gaps]] · [[Anchors and Prerequisites]].

> [!note]- Commentary (skippable)
> §6 is the payoff: §3 measured one class, §4 summed the measurements into $-\log Z_X(s)$, and now §6 divides to make a probability law and then Fourier-transforms it. The two halves are the same trick at two altitudes. In §6.1 the mechanism is that the killing weight $e^{(1-s)L}$ carries the length $L$ in its exponent, so the spectral derivative $\partial_s$ pulls down exactly $-L$: differentiating the partition function in $s$ *is* computing length-moments, and every cumulant is a derivative of $\log(-\log Z_X)$. That is why "increase the killing" and "shorten the loop" are the same operation (the tilt identity $\mathbb E_s[e^{-rL}]=F(s+r)/F(s)$), and why sending $\kappa\to\infty$ squeezes the whole measure onto the shortest geodesics — a hyperbolic surface's systole and its multiplicity are literally the leading asymptotics of its Selberg zeta.
> In §6.2–§6.3 the mechanism is Pontryagin duality. Homology is the abelianisation, a lattice $\mathbb Z^r$; its dual is a torus of characters; and the twisted zeta $L_X(s,\chi)$ is precisely the generating function whose log-coefficients are the homology masses — the Selberg $L$-function plays for geodesics-by-homology exactly the role Dirichlet $L$-functions play for primes-in-progressions. Once that is set up, the total homology of the entire loop soup is a one-line Poisson computation: the exponential formula turns $\mathbb E[\chi(\beta(\lambda))]$ into $\exp(\lambda\sum(\chi^m-1)\mu)$, the two sums are $-\log L_X$ and $-\log Z_X$, and the characteristic function is the clean ratio $(Z_X/L_X)^\lambda$ whose Fourier inverse is the exact law.
> What breaks without each hypothesis: drop $\kappa>0$ and on a finite-area surface the normalising constant $-\log Z_X(1)$ diverges (that is the $s=\delta=1$ boundary of §4, and the reason §5's renormalisation exists — the note flags that $\kappa=0$ is available only via §5). Drop unitarity of $\chi$ and the Euler product (75) loses its $|z|<1$, so the log-expansion and the abscissa $\delta$ both fail. Drop orthogonality (pure Fourier analysis, an anchor, not a gap) and there is no inversion. Everything else — the exponential formula, the class-mass shape — is inherited intact from §3–§4, which is exactly why §6 costs almost nothing and yet delivers the full probabilistic picture.