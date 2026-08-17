---
type: paper-section
paper: "BH26"
subject: brownian-loops
section: "7"
tags: [paper, section, hyperbolic-3-manifolds, self-contained]
---

> [!info] Part of [[Map - Brownian Loops on Homotopy and Homology Classes]]. Self-contained: every symbol, predicate and imported result used below is written out on this page. Grey callouts are folds on THIS page — opening one is a scroll, not a jump to another file. You can typecheck §7 front-to-back without opening anything else.

**What §7 buys you.** Everything in §2–§3 was built from a heat kernel, bridge measures, the weight $dt/t$ and the volume form — none of which needs a surface. §7 replaces $X=\Gamma\backslash\mathbb H^2$ by a hyperbolic **3-manifold** $X=\Gamma\backslash\mathbb H^3$ and reruns the machine: the class-decomposition (Theorem 7.1) is dimension-blind, and because the $\mathbb H^3$ heat kernel is **elementary** the analogue of the imported Wang–Xue strip identity is *derived here* (§7's one real computation). The class mass becomes $\mu_X(\mathcal C_X(\gamma^m))=\tfrac1m|e^{mL_\gamma}-1|^{-2}$ with a **complex** length $L_\gamma=\ell_\gamma+i\theta_\gamma$ — and this squared-modulus shape is exactly why the §4 Selberg-zeta identity does **not** transfer: the paper's most concrete open problem.

# A. Standing setup

Everything in §7 lives on a fixed hyperbolic 3-manifold $X$ and concerns the mass its Brownian loop measure assigns to a free-homotopy class. The paragraphs below fix those objects, inlined so that dropping straight into §7 needs nothing from earlier sections. The one structural novelty against §2–§6: the group now sits in $\mathrm{PSL}(2,\mathbb C)$, and a closed geodesic carries a **complex** length.

**The manifold.** $\Gamma\subseteq\mathrm{PSL}(2,\mathbb C)$ is a discrete, torsion-free group of orientation-preserving isometries of hyperbolic 3-space $\mathbb H^3$ (upper half-space $\{(z,y):z\in\mathbb C,\ y>0\}$, metric $(|dz|^2+dy^2)/y^2$) — a **Kleinian group**. Discrete and torsion-free means it acts **freely** — $\forall h\in\Gamma\setminus\{1\}\ \forall w\in\mathbb H^3:\ hw\neq w$ (no non-identity isometry fixes a point) — and **properly discontinuously** — $\forall K\Subset\mathbb H^3:\ \#\{h\in\Gamma:hK\cap K\neq\varnothing\}<\infty$ (each compact set meets only finitely many of its $\Gamma$-translates). Under exactly these two conditions the quotient $X=\Gamma\backslash\mathbb H^3$ (points glued when one is a $\Gamma$-image of the other) is a smooth complete orientable hyperbolic 3-manifold and $\pi:\mathbb H^3\to X$ is a **covering map** (a local isometry under which $\mathbb H^3$ wraps around $X$) with **deck group** $\Gamma$ (the isometries permuting the sheets over each point), $\Gamma\cong\pi_1(X)$. We take $X$ **geometrically finite**; the only consequence used is that the length spectrum is locally finite, so a shortest geodesic exists.

**Loxodromic elements and complex length.** In $\mathrm{PSL}(2,\mathbb C)$ a non-identity isometry is one of three types; the torsion-free discrete $\Gamma$ has no elliptics (rotations, which fix a point) or — for the classes that matter — parabolics (peripheral / cusp elements, fixing a boundary point, no closed geodesic). Every element that gives a genuine class is **loxodromic**: it has an oriented geodesic **axis**, along which it **translates** by a distance $\ell_\gamma>0$ **and about which it rotates** by an angle $\theta_\gamma\in\mathbb R/2\pi\mathbb Z$ (the **holonomy angle**). These package into one complex number, the **complex length**
$$L_\gamma:=\ell_\gamma+i\theta_\gamma,\qquad \ell_\gamma>0,\ \theta_\gamma\in\mathbb R/2\pi\mathbb Z .$$
Conjugating $\tau\in\Gamma$ into **standard form** puts its axis on the vertical geodesic from $0$ to $\infty$, where it acts by
$$\tau:(z,y)\longmapsto\big(e^{L_\gamma}z,\ e^{\ell_\gamma}y\big),\qquad\text{so}\quad \tau^m:(z,y)\longmapsto\big(e^{mL_\gamma}z,\ e^{m\ell_\gamma}y\big).\tag{82}$$
The height scales by the **real** factor $e^{\ell_\gamma}$; the holonomy $\theta_\gamma$ lives in the complex multiplier $e^{L_\gamma}=e^{\ell_\gamma}e^{i\theta_\gamma}$ acting on the horizontal coordinate $z$.

**Geodesics and their classes.** A closed geodesic $\gamma$ is **primitive** if it is not a repeated traversal of a shorter one — its representative $\tau\in\Gamma$ satisfies $\tau=\sigma^k\ (\sigma\in\Gamma,k\ge1)\Rightarrow k=1$. Write $\mathcal P_X$ for the primitive oriented closed geodesics; each $\gamma\in\mathcal P_X$ is a primitive loxodromic conjugacy class with complex length $L_\gamma$. Two oriented loops are **freely homotopic** if one deforms into the other through closed curves with no basepoint fixed; free-homotopy classes correspond bijectively to conjugacy classes $[h]=\{qhq^{-1}:q\in\Gamma\}$ in $\Gamma$, and — restricting to **non-trivial, non-peripheral** (i.e. loxodromic) classes — to pairs $(\gamma,m)\in\mathcal P_X\times\mathbb Z_{\ge1}$: $\mathcal C_X(\gamma^m)$ is the class winding $m$ times around $\gamma$, i.e. the conjugacy class $[\tau^m]=\{h\tau^m h^{-1}:h\in\Gamma\}$, which contains a unique oriented closed geodesic representative. **The only geometric input to the class mass is now the single complex number $L=mL_\gamma=m\ell_\gamma+im\theta_\gamma$.**

**Notation for §7.**

| symbol | type |
|---|---|
| $X=\Gamma\backslash\mathbb H^3$ | geometrically finite hyperbolic 3-manifold; $\mathbb H^3=\{(z,y):z\in\mathbb C,y>0\}$ |
| $\Gamma\subseteq\mathrm{PSL}(2,\mathbb C)$ | discrete torsion-free (Kleinian) group; $\Gamma\cong\pi_1(X)$ |
| $\mathcal P_X$ | primitive oriented closed geodesics $\gamma$ (loxodromic conjugacy classes) |
| $\ell_\gamma,\ \theta_\gamma$ | translation length $\in(0,\infty)$; holonomy angle $\in\mathbb R/2\pi\mathbb Z$ |
| $L_\gamma,\ L$ | complex length $\ell_\gamma+i\theta_\gamma$; $L:=mL_\gamma=m\ell_\gamma+im\theta_\gamma$ |
| $m$ | winding number $\in\mathbb Z_{\ge1}$ |
| $\tau,\ \tau^m$ | representative in standard form (82); $\tau^m(z,y)=(e^{mL_\gamma}z,e^{m\ell_\gamma}y)$ |
| $\mathcal C_X(\gamma^m)$ | free-homotopy class of $\gamma^m$ $=$ conjugacy class $[\tau^m]$; measurable set of loops |
| $F_\tau$ | fundamental slab $\{(z,y):1\le y<e^{\ell_\gamma}\}$ for $\langle\tau\rangle$ acting on $\mathbb H^3$ |
| $p_{\mathbb H^3}(t,\cdot,\cdot),\ p^E_{\mathbb H^3}$ | Brownian / Dirichlet-form heat kernel on $\mathbb H^3$ at duration $t$ |
| $\rho$ | hyperbolic distance $d(w,\tau^m w)$ on $\mathbb H^3$ (the kernel's spatial argument) |
| $\mu^\phi_X,\ \mu_X$ | $\phi$-subordinate / plain Brownian loop measure; class mass $\in(0,\infty)$ |
| $\phi,\ V_\phi$ | a Bernstein function; its weighted potential measure on $(0,\infty)$ (recalls below) |
| $t$ | loop duration $\in(0,\infty)$ (integrated $dt/t$) |
| $u$ | subordination / proper-time variable $\in(0,\infty)$ — the paper's overloaded "$s$", renamed |

**Standing conventions.** $\Delta_X\ge0$ (geometer's sign; $\operatorname{spec}\Delta_X\subseteq[0,\infty)$); Brownian motion at speed $2$ (generator $-\Delta_X$). Three time-like variables are kept typographically distinct, deviating from the paper's single "$s$": the **spectral parameter** $s$; the **subordination / proper-time** variable $u$ (integrated in $I_\phi$ and $V_\phi$); the **loop duration** $t$ (integrated $\mathrm{d}t/t$). Spectral $s$ and killing $\kappa$ are linked by $s=\tfrac12+\sqrt{\tfrac14+\kappa}\iff\kappa=s(s-1)$, with $\kappa\ge-\tfrac14$ (at $\kappa=-\tfrac14$, $s=\tfrac12=\inf\operatorname{spec}\Delta_{\mathbb H^2}$). **Total mass** always means the sum over **non-trivial, non-peripheral** free-homotopy classes: the trivial (contractible) class carries infinite mass and is excluded, and peripheral (cusp) classes have no closed geodesic and are excluded.

Two objects built earlier reach §7 only through their end-formulas; their definitions are folded here so nothing is off-page. Note $\mathbb H^3$ does **not** reuse the surface object $I_\phi$ (whose kernel is the $\mathbb H^2$ one) — §7 rebuilds the analytic factor from the $\mathbb H^3$ kernel — but it does reuse $V_\phi$ and the Bernstein hypothesis.

**Used here — $\phi$, Bernstein with Assumption 2.3:** only that it yields a well-defined potential measure $V_\phi$; no other property of $\phi$ is used.
> [!recall]- $\phi$ a Bernstein function satisfying Assumption 2.3
> $\phi:(0,\infty)\to[0,\infty)$ is **Bernstein** if it is $C^\infty$ with $(-1)^{n-1}\phi^{(n)}(\lambda)\ge0$ for all $n\ge1,\lambda>0$ (its derivative completely monotone). Equivalently (Lévy–Khintchine) $\phi(\lambda)=a+b\lambda+\int_0^\infty(1-e^{-\lambda u})\,\nu(\mathrm du)$ for a unique triple $(a,b,\nu)$ with $a,b\ge0$ and $\int_0^\infty(1\wedge u)\,\nu(\mathrm du)<\infty$ — the Laplace exponent of a **subordinator** (an increasing random clock $T_t\ge0$, $\mathbb E[e^{-\lambda T_t}]=e^{-t\phi(\lambda)}$): $a$ = killing rate, $b$ = drift, $\nu$ = jump intensity. **Assumption 2.3:** $b>0$ **or** $\nu(0,\infty)=\infty$ — the clock strictly increases, so its law has no atom at $0$ and the subordinate heat kernel is a genuine density. *(It says nothing about $a$: killing is allowed — $\phi(\lambda)=\lambda+\kappa$ has $a=\kappa$, passes via $b=1$.)* The four instances: $\phi(\lambda)=\lambda,\ \lambda+\kappa,\ \lambda^{\alpha/2},\ (\lambda+\kappa)^{\alpha/2}$.

**Used here — $V_\phi$ (Definition 2.9):** only as the $\sigma$-finite measure that Theorem 7.2 integrates the $\mathbb H^3$ kernel against; its Brownian value $du/u$ is all Corollary 7.3 needs.
> [!recall]- $V_\phi$, the weighted potential measure
> $V_\phi$ — the **weighted potential measure** — is the $\sigma$-finite measure on $(0,\infty)$ obtained by integrating the subordinator's time-$t$ law $\psi^\phi_t$ over all durations against the multiplicative Haar weight, $V_\phi(\mathrm du)=\int_0^\infty\psi^\phi_t(\mathrm du)\,\mathrm dt/t$. Its four values: $\mathrm du/u$ (Brownian), $e^{-\kappa u}\,\mathrm du/u$ (killing $\kappa$), $\tfrac\alpha2\,\mathrm du/u$ ($\alpha$-stable), $\tfrac\alpha2 e^{-\kappa u}\,\mathrm du/u$ (shifted stable). $V_\phi$ carries the whole dependence of the class mass on the process; all geometry sits in the prefactor.

# B. Spine of §7 (skim layer)

Four moves, each the $\mathbb H^3$ echo of a §3 move. Read this list and you have §7's logical content; drop into the matching subsection for expansions, the one derivation, and proofs.

1. **§7.1 — decomposition (Theorem 7.1).** *Given* the loxodromic standard form (82), the cyclic centraliser $C_\Gamma(\tau^m)=\langle\tau\rangle$, and absolute convergence of the periodisation; *produce* $\mu^E_X(\mathcal C_X(\gamma^m))=\int_0^\infty\tfrac{dt}{t}\int_{F_\tau}p^E_{\mathbb H^3}(t,w,\tau^m w)\,d\mathrm{vol}(w)$ — verbatim the §3 decomposition, dimension-blind.
2. **§7.2 — the $\mathbb H^3$ slab identity (88)–(89), DERIVED.** *Given* the elementary $\mathbb H^3$ heat kernel; *produce* $\int_{F_\tau}p_{\mathbb H^3}(t,w,\tau^m w)\,d\mathrm{vol}=\tfrac{\ell_\gamma}{2(\cosh m\ell_\gamma-\cos m\theta_\gamma)}\cdot\tfrac{e^{-t-(m\ell_\gamma)^2/4t}}{\sqrt{4\pi t}}$ — the $\mathbb H^3$ analogue of Wang–Xue, proved not imported (odd dimension ⟹ elementary kernel).
3. **§7.2 — subordinate mass (Theorem 7.2).** *Given* the slab identity and the collapse Lemma 2.11; *produce* $\mu^\phi_X(\mathcal C_X(\gamma^m))=\tfrac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^{L}-1|^2}\int_{(0,\infty)}\tfrac{2u\,e^{-u}}{(4\pi u)^{3/2}}e^{-(m\ell_\gamma)^2/4u}\,V_\phi(du)$.
4. **§7.2 — Brownian mass (Corollary 7.3) + open question.** *Given* $V_\phi(du)=du/u$ and the Gaussian reciprocal integral; *produce* $\mu_X(\mathcal C_X(\gamma^m))=\tfrac1m|e^{mL_\gamma}-1|^{-2}$ — squared modulus of a complex length. *Warning:* this shape is **not** $(C/m)e^{(1-s)L}/(e^L-1)$, so no §4 zeta identity, no probability measure, no determinant formula transfer.

# C. The results

## §7.1  General homotopy-class decomposition (Theorem 7.1)

The §3 unfolding used the group and the covering, never the dimension. It transfers verbatim; the only $\mathbb H^3$-specific inputs are the standard form (82) and the shape of the fundamental region.

**New symbols.** $F_\tau$ (fundamental slab, below); $p^E_{\mathbb H^3}$, the Dirichlet-form heat kernel on $\mathbb H^3$ — the transition density of any **regular symmetric Dirichlet form** (a symmetric, Markovian, closed bilinear energy form $\mathcal E$ on $L^2(X,\mathrm{vol})$ whose semigroup $e^{-t A}$ has a jointly measurable symmetric density $p^E$); for the paper's four processes $p^E_{\mathbb H^3}$ is exactly the subordinate Brownian kernel $p^\phi_{\mathbb H^3}$, so the reader may read $p^E$ as $p^\phi$ throughout.

> [!recall]- Fundamental region, and why the slab works in $\mathbb H^3$
> A **fundamental region** for a group $H$ acting on $\mathbb H^3$ is a Borel set $F$ with $\bigcup_{h\in H}hF=\mathbb H^3$ and $\mathrm{vol}(hF\cap F)=0$ for $h\neq1$ (one representative per orbit, up to measure zero). In standard form (82) $\tau$ scales height by the **real** factor $e^{\ell_\gamma}$, so each $\langle\tau\rangle$-orbit meets the slab $\{1\le y<e^{\ell_\gamma}\}$ in exactly one point:
> $$F_\tau:=\{(z,y)\in\mathbb H^3:1\le y<e^{\ell_\gamma}\}\qquad\text{ranges over all }z\in\mathbb C.\tag{84}$$
> The holonomy rotation $\theta_\gamma$ acts *within* each slab (it moves $z$, not $y$) and does not affect which slab a point lies in — this is why complex length changes the integrand later but not the region.

> [!recall]- The centraliser is cyclic: $C_\Gamma(\tau^m)=\langle\tau\rangle$ (dimension-independent)
> Since $\Gamma$ is discrete and torsion-free, anything commuting with $\tau^m$ preserves the axis of $\tau$; the elements of $\Gamma$ preserving that axis form an infinite cyclic subgroup generated by the primitive $\tau$, so $C_\Gamma(\tau^m)=\langle\tau\rangle=\{\tau^k:k\in\mathbb Z\}$. Hence two elements $h_1,h_2$ give the same conjugate $h_i\tau^m h_i^{-1}$ iff $h_1^{-1}h_2\in\langle\tau\rangle$, and $[\tau^m]=\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^m r^{-1}\}$ — one distinct conjugate per left coset. This is the same argument as §3; it never used that the model was two-dimensional.

**Used here — the periodisation-convergence assumption:** an explicit hypothesis of the paper (not proved), that lets the lifted diagonal kernel be summed term-by-term over $\Gamma$.
> [!import]- (P) Periodisation converges — Says / Needs / Gives
> **Says.** The $\mathbb H^3$ Dirichlet-form heat kernel $p^E_{\mathbb H^3}$ decays fast enough in its spatial variables that, with $\Gamma$ discrete, the periodisation $\sum_{h\in\Gamma}p^E_{\mathbb H^3}(t,\tilde w,h\tilde w)$ converges absolutely.
> **Needs.** $\Gamma$ discrete; the heat kernel's spatial decay (automatic for the four subordinate Brownian processes on $\mathbb H^3$).
> **Gives.** Permission to descend the loop measure to $X$ and split the diagonal kernel over conjugacy classes term-by-term. Assume freely; the paper states it as a hypothesis and does not re-prove it. Not a genuine external gap — it is a decay estimate — but it is an explicit assumption, so it is flagged.

> **Theorem 7.1 (homotopy-class decomposition on $\mathbb H^3$).** Assume:
> **(H1)** $\gamma\in\mathcal P_X$ primitive, with loxodromic representative $\tau\in\Gamma$ in standard form (82), and $m\ge1$.
> **(H2)** the periodisation $\sum_{h\in\Gamma}p^E_{\mathbb H^3}(t,\tilde w,h\tilde w)$ converges absolutely.
> **Then** the mass of the Dirichlet-form loop measure in the class $\mathcal C_X(\gamma^m)$ is
> $$\mu^E_X\big(\mathcal C_X(\gamma^m)\big)=\int_0^\infty\frac{dt}{t}\int_{F_\tau}p^E_{\mathbb H^3}(t,w,\tau^m w)\,d\mathrm{vol}_{\mathbb H^3}(w).\tag{85}$$

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | descent + (H2) | lifted diagonal loop measure on $\mathbb H^3$ | diagonal kernel $=\sum_{h\in\Gamma}p^E_{\mathbb H^3}(t,\tilde w,h\tilde w)$ |
| 2 | restrict to $[\tau^m]$ | the sum, keeping $h$ conjugate to $\tau^m$ | class-$\mathcal C_X(\gamma^m)$ part $=\sum_{r\in\Gamma/\langle\tau\rangle}p^E_{\mathbb H^3}(t,\tilde w,r\tau^m r^{-1}\tilde w)$ |
| 3 | centraliser recall $C_\Gamma(\tau^m)=\langle\tau\rangle$ | unfold the coset sum over $\Gamma/\langle\tau\rangle$ | integral over one fundamental region $F_\tau$ for $\langle\tau\rangle$ |
| 4 | fundamental-region recall (84) | $F_\tau=\{1\le y<e^{\ell_\gamma}\}$ | (85) |

Every symbol is typed above; every predicate is an import or recall above. The block typechecks with nothing off-page.

> [!note]- Proof (skippable — identical in structure to Theorem 3.2)
> Lift the loop measure to $\mathbb H^3$. The diagonal heat kernel on $X$ is the periodisation $\sum_{h\in\Gamma}p^E_{\mathbb H^3}(t,\tilde w,h\tilde w)$, absolutely convergent by (H2). Selecting the free-homotopy class $\mathcal C_X(\gamma^m)$ keeps precisely the terms with $h$ in the conjugacy class $[\tau^m]$. By the centraliser recall, $[\tau^m]=\bigsqcup_{r\in\Gamma/\langle\tau\rangle}\{r\tau^m r^{-1}\}$, one term per left coset of $\langle\tau\rangle$. Unfolding this coset sum against a fundamental domain for $\Gamma$ turns it into a single integral over a fundamental region for the *stabiliser* $\langle\tau\rangle$, namely the slab $F_\tau$ of (84); conjugation-invariance of the kernel ($p^E_{\mathbb H^3}(t,w,r\tau^m r^{-1}w)$ against $d\mathrm{vol}$ over $rF_\tau$ becomes $p^E_{\mathbb H^3}(t,w,\tau^m w)$ over $F_\tau$). Reinstating $\int_0^\infty dt/t$ gives (85). Nothing in this used $\dim=2$. $\square$

## §7.2  The $\mathbb H^3$ slab identity, subordinate mass, and the Brownian corollary

Here is the payoff of working in odd dimension. In §3 the spatial integral over the strip was **imported** (Wang–Xue) because the $\mathbb H^2$ heat kernel has no elementary closed form. On $\mathbb H^3$ the kernel *is* elementary, so the analogous integral is a change of variables — done in full below.

**New symbols.** $\rho=d(w,\tau^m w)$ (hyperbolic distance, the kernel's argument); the subordinate kernel $p^\phi_{\mathbb H^3}(t,w,\tau^m w)=\int_{[0,\infty)}p_{\mathbb H^3}(u,w,\tau^m w)\,\psi^\phi_t(du)$ (Phillips subordination — the process time-changed by the clock $\phi$).

**Used here — the $\mathbb H^3$ Brownian heat kernel:** its explicit closed form is the whole reason the slab integral is derived rather than imported.
> [!import]- The $\mathbb H^3$ heat kernel (elementary — NOT a gap) — Says / Needs / Gives
> **Says.** The speed-$2$, geometer-sign Brownian heat kernel on $\mathbb H^3$ is
> $$p_{\mathbb H^3}(t,z,w)=\frac{1}{(4\pi t)^{3/2}}\,\frac{\rho}{\sinh\rho}\,e^{-t-\rho^2/4t},\qquad \rho=d(z,w).\tag{87}$$
> **Needs.** $t>0$; $\rho=d(z,w)$ the hyperbolic distance. (The constant $e^{-t}$ is the spectral bottom of $\Delta_{\mathbb H^3}$, $\big(\tfrac{n-1}2\big)^2=1$ at $n=3$.)
> **Gives.** A closed-form integrand for the slab integral. Assume freely: in **odd** dimension the hyperbolic heat kernel is elementary (a finite expression in $\rho,t$); this is *why* §7 can derive its strip identity where §3 had to import Wang–Xue (even $\mathbb H^2$ has no such closed form). Not a gap — it is a textbook formula.

**Used here — the modulus identity:** the single algebraic bridge from the derived $\cosh-\cos$ form to the complex-length $|e^{L}-1|^2$ form; used in the slab identity and again in Corollary 7.3.
> [!import]- $|e^{a+ib}-1|^2=2e^{a}(\cosh a-\cos b)$ (elementary) — Says / Needs / Gives
> **Says.** For real $a,b$: $\ |e^{a+ib}-1|^2=(e^a\cos b-1)^2+(e^a\sin b)^2=e^{2a}-2e^a\cos b+1=2e^{a}\big(\cosh a-\cos b\big)$, and equivalently $=(e^a-1)^2+4e^a\sin^2(b/2)$.
> **Needs.** $a,b\in\mathbb R$. Here $a=m\ell_\gamma$, $b=m\theta_\gamma$, so $|e^{L}-1|^2=2e^{m\ell_\gamma}(\cosh m\ell_\gamma-\cos m\theta_\gamma)$, $L=mL_\gamma$.
> **Gives.** Interchange of the two ways of writing the slab denominator. Anchor-level; not a gap. Assume freely; nothing here re-proves it.

### The slab identity (88)–(89) — derived

> **Slab identity.** For $t>0$, $m\ge1$, $\tau$ in standard form (82), $L=mL_\gamma=m\ell_\gamma+im\theta_\gamma$:
> $$\int_{F_\tau}p_{\mathbb H^3}(t,w,\tau^m w)\,d\mathrm{vol}_{\mathbb H^3}(w)=\frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^{L}-1|^2}\cdot\frac{2t\,e^{-t}}{(4\pi t)^{3/2}}\,e^{-(m\ell_\gamma)^2/4t}\tag{88}$$
> $$\qquad\qquad=\frac{\ell_\gamma}{2\big(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)\big)}\cdot\frac{e^{-t-(m\ell_\gamma)^2/4t}}{\sqrt{4\pi t}}.\tag{89}$$

**Discharge (the typecheck of the derivation).**

| step | apply | to | get |
|---|---|---|---|
| 1 | distance in standard form | $w=(z,y)$, $\tau^m w=(e^{L}z,e^{m\ell_\gamma}y)$ | $\cosh\rho=\cosh(m\ell_\gamma)+\dfrac{|e^{L}-1|^2\,|z|^2}{2e^{m\ell_\gamma}y^2}$ |
| 2 | polar $z=re^{i\varphi}$, $\rho$ depends on $z$ only via $r$ | angular integral $\int_0^{2\pi}d\varphi$ | factor $2\pi$; leaves $\int_1^{e^{\ell_\gamma}}\!\int_0^\infty p_{\mathbb H^3}(t,\rho)\,\dfrac{r\,dr\,dy}{y^3}$ |
| 3 | change $r\mapsto\rho$: $\sinh\rho\,d\rho=\dfrac{|e^{L}-1|^2\,r}{e^{m\ell_\gamma}y^2}dr$ | so $r\,dr=\dfrac{e^{m\ell_\gamma}y^2}{|e^{L}-1|^2}\sinh\rho\,d\rho$, $\ \rho:m\ell_\gamma\to\infty$ | the kernel's $1/\sinh\rho$ cancels $\sinh\rho$ |
| 4 | Gaussian $\int_{m\ell_\gamma}^\infty\rho\,e^{-\rho^2/4t}d\rho=2t\,e^{-(m\ell_\gamma)^2/4t}$ | inner $\int_0^\infty p_{\mathbb H^3}(t,\rho)\,r\,dr$ | $\dfrac{e^{m\ell_\gamma}y^2}{|e^{L}-1|^2}\cdot\dfrac{2t\,e^{-t}}{(4\pi t)^{3/2}}e^{-(m\ell_\gamma)^2/4t}$ |
| 5 | $y$-integral: $y^2/y^3=1/y$, $\int_1^{e^{\ell_\gamma}}\!\tfrac{dy}{y}=\ell_\gamma$ | outer integral over the slab | $\times\,\ell_\gamma$, giving (88) |
| 6 | modulus identity $|e^{L}-1|^2=2e^{m\ell_\gamma}(\cosh m\ell_\gamma-\cos m\theta_\gamma)$ and $\dfrac{2\pi\cdot2t}{(4\pi t)^{3/2}}=\dfrac1{\sqrt{4\pi t}}$ | (88) | (89) |

Every symbol is typed above; every predicate is (87), the modulus identity, or an explicit integral. The derivation typechecks with nothing off-page.

> [!note]- Proof of the slab identity (skippable — the full computation)
> **Distance (step 1).** With $w=(z,y)$ and $\tau^m w=(e^{L}z,e^{m\ell_\gamma}y)$, the upper-half-space distance formula gives
> $$\cosh\rho=1+\frac{|z-e^{L}z|^2+(y-e^{m\ell_\gamma}y)^2}{2e^{m\ell_\gamma}y^2}=\cosh(m\ell_\gamma)+\frac{|e^{L}-1|^2\,|z|^2}{2e^{m\ell_\gamma}y^2},$$
> using $|z-e^{L}z|^2=|e^{L}-1|^2|z|^2$ and $1+\tfrac{(1-e^{m\ell_\gamma})^2}{2e^{m\ell_\gamma}}=\cosh(m\ell_\gamma)$. So $\rho$ depends on $z$ only through $|z|=r$.
> **Angular + change of variable (steps 2–3).** The volume element is $d\mathrm{vol}_{\mathbb H^3}=y^{-3}\,dA(z)\,dy$ with $dA(z)=r\,dr\,d\varphi$. The angular integral yields $2\pi$. Fix $y$ and differentiate the distance relation: $\sinh\rho\,d\rho=\tfrac{|e^{L}-1|^2\,r}{e^{m\ell_\gamma}y^2}\,dr$, hence $r\,dr=\tfrac{e^{m\ell_\gamma}y^2}{|e^{L}-1|^2}\sinh\rho\,d\rho$; as $r:0\to\infty$, $\rho:m\ell_\gamma\to\infty$. In $p_{\mathbb H^3}(t,\rho)=\tfrac1{(4\pi t)^{3/2}}\tfrac{\rho}{\sinh\rho}e^{-t-\rho^2/4t}$ the factor $\sinh\rho$ cancels the $1/\sinh\rho$:
> $$\int_0^\infty p_{\mathbb H^3}(t,\rho)\,r\,dr=\frac{e^{m\ell_\gamma}y^2}{|e^{L}-1|^2}\cdot\frac{e^{-t}}{(4\pi t)^{3/2}}\int_{m\ell_\gamma}^\infty \rho\,e^{-\rho^2/4t}\,d\rho.$$
> **Gaussian (step 4).** $\int_{m\ell_\gamma}^\infty\rho\,e^{-\rho^2/4t}\,d\rho=\big[-2t\,e^{-\rho^2/4t}\big]_{m\ell_\gamma}^\infty=2t\,e^{-(m\ell_\gamma)^2/4t}$. Thus the inner integral is $\tfrac{e^{m\ell_\gamma}y^2}{|e^{L}-1|^2}\cdot\tfrac{2t\,e^{-t}}{(4\pi t)^{3/2}}e^{-(m\ell_\gamma)^2/4t}$.
> **Slab (step 5).** The $y^2$ meets the $y^{-3}$: $\int_1^{e^{\ell_\gamma}}y^{-1}\,dy=\ell_\gamma$. Restoring the $2\pi$ gives (88). The rewrite (89) is the modulus identity plus $\tfrac{2\pi\cdot2t}{(4\pi t)^{3/2}}=\tfrac1{\sqrt{4\pi t}}$. $\square$

> [!warning] Why the analogue was *imported* on $\mathbb H^2$ but *derived* here
> The single move that makes this elementary is the cancellation $\tfrac{\rho}{\sinh\rho}\cdot\sinh\rho=\rho$ — the $\mathbb H^3$ kernel's $\rho/\sinh\rho$ against the Jacobian's $\sinh\rho$, leaving a bare Gaussian $\rho\,e^{-\rho^2/4t}$. The $\mathbb H^2$ kernel has **no** elementary closed form (it is an integral of $\cosh$-weighted Gaussians), so §3 had to import the strip identity from Wang–Xue. Odd hyperbolic dimensions inherit the elementary kernel; even ones do not.

### Subordinate mass (Theorem 7.2)

Same three moves as §3.5: put the slab identity under the subordination integral, then collapse the $dt/t$-integral into $V_\phi$.

**Used here — the collapse lemma:** it turns the double $(t,u)$ integral into one integral against $V_\phi$.
> [!import]- Lemma 2.11 (collapse) — Says / Needs / Gives
> **Says.** For measurable $h\ge0$ on $(0,\infty)$: $\int_0^\infty\frac{\mathrm dt}{t}\int_{[0,\infty)}h(u)\,\psi^\phi_t(\mathrm du)=\int_0^\infty h(u)\,V_\phi(\mathrm du)$.
> **Needs.** Assumption 2.3 (so $\psi^\phi_t(\{0\})=0$; integral effectively over $(0,\infty)$).
> **Gives.** Collapses the double $(t,u)$ integral into one integral against $V_\phi$ — the move that turns Theorem 7.1 into Theorem 7.2. Derivation is Tonelli (anchor); not a gap. Assume freely; nothing here re-proves it.

> **Theorem 7.2 (mass of the subordinate Brownian loop measure on $\mathbb H^3$).** Assume $\phi$ Bernstein with Assumption 2.3 (H1), $\gamma\in\mathcal P_X$, $m\ge1$, with complex length $L=mL_\gamma=m\ell_\gamma+im\theta_\gamma$. Then
> $$\mu^\phi_X\big(\mathcal C_X(\gamma^m)\big)=\frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^{L}-1|^2}\int_{(0,\infty)}\frac{2u\,e^{-u}}{(4\pi u)^{3/2}}\,e^{-(m\ell_\gamma)^2/4u}\,V_\phi(du).\tag{90}$$

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | Theorem 7.1 with $p^E=p^\phi$, expand Phillips subordination | (85) | $\mu^\phi_X=\int_0^\infty\tfrac{dt}{t}\int_{F_\tau}\int_{[0,\infty)}p_{\mathbb H^3}(u,w,\tau^m w)\,\psi^\phi_t(du)\,d\mathrm{vol}$ |
| 2 | slab identity (88) at proper time $u$ | inner spatial integral $\int_{F_\tau}p_{\mathbb H^3}(u,\cdot,\cdot)\,d\mathrm{vol}$ | $=\dfrac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^{L}-1|^2}\dfrac{2u\,e^{-u}}{(4\pi u)^{3/2}}e^{-(m\ell_\gamma)^2/4u}$ |
| 3 | Lemma 2.11 with $h(u)=\tfrac{2u\,e^{-u}}{(4\pi u)^{3/2}}e^{-(m\ell_\gamma)^2/4u}$ | the remaining $\int_0^\infty\tfrac{dt}{t}\int_{[0,\infty)}h\,\psi^\phi_t(du)$ | $\int_{(0,\infty)}h(u)\,V_\phi(du)$, i.e. (90) |

Every symbol is typed above; every predicate is the slab identity or Lemma 2.11. The block typechecks with nothing off-page.

> [!note]- Proof (skippable)
> Start from (85) with $p^E=p^\phi_{\mathbb H^3}$ and expand the subordinate kernel by Phillips, $p^\phi_{\mathbb H^3}(t,\cdot,\cdot)=\int_{[0,\infty)}p_{\mathbb H^3}(u,\cdot,\cdot)\,\psi^\phi_t(du)$:
> $$\mu^\phi_X(\mathcal C_X(\gamma^m))=\int_0^\infty\frac{dt}{t}\int_{F_\tau}\int_{[0,\infty)}p_{\mathbb H^3}(u,w,\tau^m w)\,\psi^\phi_t(du)\,d\mathrm{vol}(w).$$
> The spatial integral is against the Brownian kernel at time $u$, so the slab identity (88) evaluates it to $\tfrac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^{L}-1|^2}\cdot\tfrac{2u\,e^{-u}}{(4\pi u)^{3/2}}e^{-(m\ell_\gamma)^2/4u}$. Pulling the ($u$-free) prefactor out and applying Lemma 2.11 with $h(u)$ that integrand collapses $\int_0^\infty\tfrac{dt}{t}\int_{[0,\infty)}h(u)\psi^\phi_t(du)=\int_{(0,\infty)}h(u)V_\phi(du)$, which is (90). (Against §3: here the spectral shift is $e^{-u}$ not $e^{-u/4}$, and the normalisation carries $u^{-3/2}\cdot u=u^{-1/2}$ from the $\mathbb H^3$ kernel.) $\square$

### Brownian mass (Corollary 7.3), and the open question

**Used here — the Gaussian reciprocal integral:** it closes (90) at $V_\phi(du)=du/u$ into the final formula.
> [!import]- Gaussian reciprocal integral — Says / Needs / Gives
> **Says.** $\int_0^\infty u^{-3/2}e^{-au-b/u}\,\mathrm du=\sqrt{\pi/b}\,e^{-2\sqrt{ab}}$. **Needs.** $a,b>0$. **Gives.** the closed form for the Brownian case; here $a=1$ (the $\mathbb H^3$ spectral bottom $\big(\tfrac{n-1}2\big)^2=1$) and $b=(m\ell_\gamma)^2/4$, so the integral $=\sqrt{4\pi/(m\ell_\gamma)^2}\,e^{-m\ell_\gamma}=\tfrac{2\sqrt\pi}{m\ell_\gamma}e^{-m\ell_\gamma}$. Anchor-level (elementary); not a gap. Assume freely; nothing here re-proves it.

> **Corollary 7.3 (Brownian class mass on $\mathbb H^3$).** Let $X=\Gamma\backslash\mathbb H^3$ be geometrically finite, $\gamma\in\mathcal P_X$ primitive with complex length $L_\gamma=\ell_\gamma+i\theta_\gamma$, and $m\ge1$. Then, with $mL_\gamma=m\ell_\gamma+im\theta_\gamma$,
> $$\mu_X\big(\mathcal C_X(\gamma^m)\big)=\frac1m\cdot\frac{1}{\,|e^{mL_\gamma}-1|^2\,}\tag{91}$$
> $$=\frac{e^{-m\ell_\gamma}}{2m\big(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)\big)}=\frac1m\Big[(e^{m\ell_\gamma}-1)^2+4e^{m\ell_\gamma}\sin^2\tfrac{m\theta_\gamma}2\Big]^{-1}.\tag{92}$$
> When $\theta_\gamma=0$ the holonomy term drops and the denominator becomes $(e^{m\ell_\gamma}-1)^2$.

**Discharge (the typecheck).**

| step | apply | to | get |
|---|---|---|---|
| 1 | Theorem 7.2 with $V_\phi(du)=du/u$ (Brownian) | (90) | $\mu_X=\dfrac{2\pi e^{m\ell_\gamma}\ell_\gamma}{|e^{L}-1|^2}\cdot\dfrac{2}{(4\pi)^{3/2}}\displaystyle\int_0^\infty u^{-3/2}e^{-u-(m\ell_\gamma)^2/4u}\,du$ |
| 2 | Gaussian reciprocal, $a=1,\ b=(m\ell_\gamma)^2/4$ | the integral | $=\dfrac{2\sqrt\pi}{m\ell_\gamma}e^{-m\ell_\gamma}$ |
| 3 | collect constants $\tfrac{2\pi\cdot2}{(4\pi)^{3/2}}\cdot\tfrac{2\sqrt\pi}{m\ell_\gamma}=\tfrac1{m\ell_\gamma}$, and $e^{m\ell_\gamma}e^{-m\ell_\gamma}=1$ | step 1 $\times$ step 2 | $\mu_X=\dfrac{\ell_\gamma}{m\ell_\gamma}\cdot\dfrac1{|e^{L}-1|^2}=\dfrac1m|e^{mL_\gamma}-1|^{-2}$ — (91) |
| 4 | modulus identity ($a=m\ell_\gamma,b=m\theta_\gamma$) | $|e^{L}-1|^2$ | the two forms (92) |

Every symbol is typed above; every predicate is Theorem 7.2, the Gaussian reciprocal, or the modulus identity. The block typechecks with nothing off-page.

> [!note]- Verification of the constant collapse in step 3 (skippable — every number from this page)
> $(4\pi)^{3/2}=8\pi^{3/2}$, so $\tfrac{2}{(4\pi)^{3/2}}=\tfrac1{4\pi^{3/2}}$. Then $2\pi\cdot\tfrac1{4\pi^{3/2}}=\tfrac1{2\sqrt\pi}$, and $\tfrac1{2\sqrt\pi}\cdot\tfrac{2\sqrt\pi}{m\ell_\gamma}=\tfrac1{m\ell_\gamma}$. The prefactor's $e^{m\ell_\gamma}$ cancels the integral's $e^{-m\ell_\gamma}$, and the prefactor's $\ell_\gamma$ meets $\tfrac1{m\ell_\gamma}$ to leave $\tfrac1m$. What survives is $\tfrac1m\cdot\tfrac1{|e^{L}-1|^2}$. The two forms (92) are the modulus identity $|e^{m\ell_\gamma+im\theta_\gamma}-1|^2=2e^{m\ell_\gamma}(\cosh m\ell_\gamma-\cos m\theta_\gamma)=(e^{m\ell_\gamma}-1)^2+4e^{m\ell_\gamma}\sin^2(m\theta_\gamma/2)$, the last via $1-\cos m\theta_\gamma=2\sin^2(m\theta_\gamma/2)$.

> [!warning] Why the §4 Selberg-zeta identity does NOT transfer (the paper's open question)
> The §4 criterion needed the class mass to have the exact shape $\dfrac{C}{m}\dfrac{e^{(1-s)L}}{e^{L}-1}$ with $C,s$ **independent of $L$** and $L$ **real** — because that is the $(\gamma,m)$-summand of $-\log Z_X(s)=\sum_{\gamma,m}\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$, so summing gives a Selberg zeta value. The $\mathbb H^3$ mass (91) is $\dfrac1m\dfrac1{|e^{mL_\gamma}-1|^2}$: a **squared modulus** of a factor with **complex** $L_\gamma=\ell_\gamma+i\theta_\gamma$. That is not the required shape (no linear exponent $e^{(1-s)L}$, no single $e^L-1$ downstairs, and the holonomy $\theta_\gamma$ has nowhere to go in a real Selberg zeta). **Consequently §7 has:** no total-mass zeta identity, no normalised probability measure on classes (§6), no determinant formula (§5). A holonomy-twisted Selberg zeta $\prod_{\gamma,k}(1-e^{-(s+k)L_\gamma})$ (with complex $L_\gamma$) is the natural candidate to absorb the twist, but the paper does not pursue it. This is the paper's most concrete open problem.

# D. Exports, climb, commentary

**Exports (what later sections consume).** None — §7 is the terminal section. It changes the dimension and reruns §2–§3; it does *not* feed §4–§6 (those consumed the surface class mass, whose shape §7 shows breaks in dimension 3). The one thing §7 hands forward is a negative: the class-mass shape that made the whole zeta/determinant/probability tower possible is special to surfaces.

**Climb (optional — none is needed to typecheck §7).** Sibling sections and ledgers: [[§2 The Loop Measure and Subordination]] · [[§3 Mass of a Homotopy Class]] · [[§4 Zeta Identities and Finiteness]] · [[§5 Determinants and the Polyakov Anomaly]] · [[§6 Probability on Homotopy and Homology Classes]] · [[External Inputs and Gaps]] · [[Anchors and Prerequisites]]. All deletable with zero loss to the typecheck above.

> [!note]- Commentary (skippable)
> The moral of §7 is a dependency audit. Section 2's loop measure needed only a heat kernel, bridge disintegrations, the weight $dt/t$, and the volume form — objects that exist on any complete Riemannian manifold. Section 3's decomposition needed only the descent to the covering and the unfolding over cosets of a cyclic centraliser — group theory, blind to dimension. What actually tied the paper to surfaces was elsewhere: the **conformal invariance** of the Brownian loop measure, on which the Polyakov anomaly of §5 and the Wang–Xue length identity of §3.4 rested. And the instant you switch on a killing rate or any nonlinear subordination, conformal invariance is gone anyway — so nothing is lost by leaving surfaces. Replacing $\mathbb H^2$ by $\mathbb H^3$ costs one thing and buys one thing. It costs the length becoming complex, $L_\gamma=\ell_\gamma+i\theta_\gamma$, because loxodromics rotate as they translate. It buys an *elementary* heat kernel, because odd hyperbolic dimensions have closed-form kernels ($\rho/\sinh\rho$ times a Gaussian) — so the strip identity that §3 had to import from Wang–Xue is, here, a one-page change of variables whose only trick is that $\rho/\sinh\rho$ cancels the volume Jacobian's $\sinh\rho$.
>
> The sting is in the answer. The surface mass $\tfrac1m\tfrac{e^{(1-s)L}}{e^L-1}$ was a *free-boson mode energy* in disguise, and summing it gave $-\log Z_X(s)$ — the entire spectral tower of §4–§6. The 3-manifold mass $\tfrac1m|e^{mL_\gamma}-1|^{-2}$ is a squared modulus of a complex length: structurally the wrong shape, with the holonomy angle $\theta_\gamma$ homeless in any real Selberg zeta. So the tower collapses at the first step. The honest way to read §7 is that it isolates *exactly* which feature of surfaces the miracle depended on — not the loop measure, not the decomposition, but the coincidence that a real translation length makes the class mass a geometric-series summand. A twisted zeta over complex lengths is the obvious repair, and the fact that the paper flags it and stops is the cleanest statement of where this line of work runs out.