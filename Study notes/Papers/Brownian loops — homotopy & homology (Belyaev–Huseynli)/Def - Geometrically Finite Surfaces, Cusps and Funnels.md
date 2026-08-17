---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Fuchsian Group and the Quotient Surface"
tags: [paper, hyperbolic-geometry]
---

# Signature

| symbol | type |
|---|---|
| $X$ | $=\Gamma\backslash\mathbb{H}^2$, $\Gamma$ torsion-free Fuchsian |
| $g$ | $\in\mathbb{Z}_{\geq0}$ — genus |
| $n_C,\ n_F$ | $\in\mathbb{Z}_{\geq0}$ — numbers of cusps and of funnels |
| $b$ | $=n_C+n_F$ — number of ends |
| $\chi(X)$ | $=2-2g-b\in\mathbb{Z}$ — Euler characteristic |
| $\operatorname{Area}(X)$ | $=\rho_X(X)\in(0,\infty]$; $=-2\pi\chi(X)$ when finite (Gauss–Bonnet) |
| $\delta$ | $\in(0,1]$ — the [[Def - Critical Exponent\|critical exponent]] of $\Gamma$ |
| $H_1(X,\mathbb{Z})$ | $\cong\mathbb{Z}^r$, $r=2g$ (closed) or $r=2g+b-1$ ($b\geq1$) |
| $\mathcal{C}_X(\cdot)$ | a free homotopy class of oriented closed curves on $X$ |

---

# Definition

> **Definition (geometrically finite).** $\Gamma$ is **geometrically finite** if it admits a fundamental region in $\mathbb{H}^2$ that is a finite-sided convex polygon. Then $X$ is a compact core with finitely many ends, each a cusp or a funnel.

> **Definition (cusp, funnel).** An end of $X$ is
> **(D1) a cusp** if isometric to $\{z\in\mathbb{H}^2:\operatorname{Im}z>c\}/\langle z\mapsto z+1\rangle$ — the quotient by a **parabolic** — of **finite** area;
> **(D2) a funnel** if isometric to one side of the core geodesic in $\langle z\mapsto e^{\ell}z\rangle\backslash\mathbb{H}^2$ — the quotient by a **hyperbolic** — of **infinite** area.

> **Definition (non-trivial, non-peripheral).** A free homotopy class $\mathcal{C}$ of oriented closed curves on $X$ is
> **(D3) non-trivial** if its loops are not null-homotopic; equivalently the corresponding conjugacy class in $\Gamma$ is not $\{1\}$;
> **(D4) non-peripheral** if its loops are neither freely homotopic into a cusp nor freely homotopic to a boundary component; equivalently the corresponding conjugacy class consists of **hyperbolic**, not parabolic, elements.
>
> **Standing convention from §3 on:** all free homotopy classes satisfy (D3) and (D4) unless stated otherwise. **Each such class contains a unique closed geodesic representative.**

---

# Type card

> [!abstract] Type card — geometric finiteness
> **Given.** **(H1)** $\Gamma$ torsion-free Fuchsian, geometrically finite.
>
> **Produces.** Integers $g,n_C,n_F$ with $b=n_C+n_F$ and $\chi(X)=2-2g-b$; a dichotomy $\operatorname{Area}(X)<\infty\iff n_F=0\iff\delta=1$; the rank $r$ of $H_1(X,\mathbb{Z})$; and countability of $\mathcal{P}_X$ with $N_X(R)<\infty$ for all $R$.
>
> **Lets you.** Keep every sum in the paper indexed by something enumerable, and decide in advance — via the $\delta$ dichotomy — whether §5's renormalisation is needed.

---

# Depends on

- [[Def - Fuchsian Group and the Quotient Surface]] — (H1); (F2) there gives parabolic $\leftrightarrow$ cusp, hyperbolic $\leftrightarrow$ funnel
- [[Def - Euler Characteristic]], [[Thm - Gauss-Bonnet Theorem for Surfaces]] — for $\chi$ and $\operatorname{Area}(X)=-2\pi\chi(X)$
- 🟢 classification of surfaces by genus and ends

---

# The dichotomy (used constantly)

$$\operatorname{Area}(X)<\infty\ \iff\ n_F=0\ \iff\ \delta=1,\qquad\qquad \operatorname{Area}(X)=\infty\ \iff\ n_F\geq1\ \iff\ \delta<1 .$$

| consequence | finite area ($\delta=1$) | infinite area ($\delta<1$) |
|---|---|---|
| Brownian total mass ($s=1$), [[Thm - Finiteness of the Total Mass\|Cor. 4.7]] | **diverges** ($s=\delta$) | finite |
| needs a killing rate or §5 | yes | no |
| $\lambda_0=0$ in the $L^2$ spectrum | yes | no |
| $Z_X$ at $s=1$ | simple **zero**; formulas use $Z'_X(1)$ | $Z_X(1)\neq0$ |
| continuous spectrum of $\Delta_X$ | $[\tfrac14,\infty)$, multiplicity $n_C$ | present, funnel-type |
| $e^{-t\Delta_X}$ trace class | **no** if $n_C\geq1$ | no |

---

# Checks

**Instance (closed).** $g\geq2$, $b=n_C=n_F=0$: $\chi=2-2g<0$, $\operatorname{Area}(X)=4\pi(g-1)$, $\delta=1$, $H_1\cong\mathbb{Z}^{2g}$, $\widehat{H_1}\cong\operatorname{Jac}(X)$. Setting of §5.1 and of Remark 6.6.

**Instance (cusped, finite area).** Once-punctured torus: $g=1$, $n_C=1$, $n_F=0$, $b=1$, $\chi=-1$, $\operatorname{Area}=2\pi$, $\delta=1$, $r=2$. Setting of §5.2: continuous spectrum of multiplicity $1$, $e^{-t\Delta_X}$ not trace class, $\det_0$ needed.

**Instance (infinite area).** Three-funnelled sphere: $g=0$, $n_C=0$, $n_F=3$, $\chi=-1$, $\delta<1$, $r=2$. Here [[Thm - Finiteness of the Total Mass|Cor. 4.7]] gives finite Brownian total mass with $\kappa=0$, and §6's measure exists with no renormalisation.

**Non-instance (fails D4).** A loop once around a cusp. It **satisfies (D3)** — its element of $\Gamma$ is a non-identity parabolic — but fails (D4). Consequence: $\inf_\eta\ell_g(\eta)=0$ and is **not attained**; the class has no closed geodesic, no translation length $\ell_\gamma$, no axis. Every formula in §3 fails to parse for it. This is why (D4) is in the standing hypothesis rather than an afterthought.

---

# Used at

- [[Def - Free Homotopy Class and Conjugacy Class Correspondence]] — where (D3),(D4) are imposed
- [[Def - Critical Exponent]] — the $\delta$ dichotomy
- [[Thm - Finiteness of the Total Mass]] — which surfaces need regularising
- [[Ext - Borthwick–Judge–Perry Determinant Formula]], [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)]] — $n_C$, $\chi$ appear explicitly
- [[Def - Eisenstein Series and the Continuous Spectrum]] — one Eisenstein series per cusp
- [[Def - Character Torus and the Pontryagin Dual]], [[Constr - The Mass in a Homology Class]] — $r=2g+n_C+n_F-1$
- [[Thm - Distribution of the Total Homology of the Loop Soup]] — $\mathcal{L}^*_\lambda$ excludes contractible and cusp-homotopic loops

---

# Commentary

> [!note]- Commentary (skippable)
> Geometric finiteness is what makes $\mathcal{P}_X$ countable with a sensible counting function, $H_1(X,\mathbb{Z})$ finitely generated, and every sum in the paper indexed by something one can enumerate.
>
> Telling cusps from funnels is the single most useful piece of bookkeeping in §4–§6, because the table above is really one table: *does $X$ have a funnel?* If yes, everything converges and §5 is unnecessary; if no, the Brownian case sits exactly on the boundary $s=\delta=1$ and needs either a killing rate or the renormalisation.
>
> The word *peripheral* exists solely to exclude classes living in the ends. Such a loop has no closed geodesic representative, so the entire §3 apparatus — indexed by closed geodesics — has nothing to say about it. Excluding those together with the trivial class is what makes "the total mass" of §4 a well-defined finite object.
>
> The equivalences in the dichotomy, and the classification of ends, are quoted from Borthwick and Buser.
