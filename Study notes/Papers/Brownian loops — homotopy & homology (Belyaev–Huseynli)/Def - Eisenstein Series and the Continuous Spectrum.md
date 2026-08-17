---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Geometrically Finite Surfaces, Cusps and Funnels"
tags: [paper, spectral-theory, automorphic-forms]
---

# Signature

| symbol | type |
|---|---|
| $X=\Gamma\backslash\mathbb{H}^2$ | non-compact hyperbolic surface of **finite area**, with $n_C\geq1$ cusps |
| $\Delta_X$ | the positive Laplacian; $\mathrm{Spec}(\Delta_X)=\{L^2\text{-eigenvalues}\}\cup[\tfrac14,\infty)$ |
| $E_j$ | $\mathbb{H}^2\times\mathbb{C}\to\mathbb{C}$ — the Eisenstein series attached to cusp $j$, $1\leq j\leq n_C$ |
| $s$ | spectral parameter; $\Delta_XE_j=s(1-s)E_j$ |
| $P$ | the orthogonal projection onto $\ker_{L^2}\Delta_X$ |

---

# Definition

> **(D1) Spectral decomposition.** For $X$ of finite area with $n_C\geq1$ cusps,
> $$\mathrm{Spec}(\Delta_X)=\underbrace{\{0=\lambda_0<\lambda_1\leq\cdots\}}_{L^2\text{-eigenvalues, possibly finite in number}}\ \cup\ \underbrace{\big[\tfrac14,\infty\big)}_{\text{continuous, multiplicity }n_C}.$$
>
> **(D2) Eisenstein series.** $E_j(z,s)$, one per cusp, solve $\Delta_XE_j=s(1-s)E_j$ but $E_j(\cdot,s)\notin L^2(X)$. They are the **generalised eigenfunctions** of the continuous part.

> **(F1) The three consequences that break §5.1.**
> 1. There is no sequence $\{\lambda_j\}$ exhausting the spectrum, so $\zeta_X(s)=\sum_j\lambda_j^{-s}$ is **not defined**.
> 2. $e^{-t\Delta_X}$ is **not trace class**, so $\mathrm{Tr}(e^{-t\Delta_X})$ is undefined and [[Def - Schwinger Proper-Time Representation|(D1)]] there fails.
> 3. Consequently ${\det}_\zeta\Delta_X$ of [[Def - Zeta-Regularised Determinant of the Laplacian|§5.1]] has no meaning.
>
> **(F2) $0$ is still an $L^2$ eigenvalue.** Finite area $\Rightarrow$ the constants are in $L^2$, so $\lambda_0=0$ with $\dim\ker_{L^2}\Delta_X=1$. This is why $\det_0\Delta_X$ requires dividing out a simple zero, and why $Z_X'(1)$ rather than $Z_X(1)$ appears.
>
> **(F3) Contrast, infinite area.** There $0$ is **not** an $L^2$ eigenvalue (constants are not square-integrable), $Z_X(1)\neq0$, and no derivative is needed — Remark 5.6.

---

# Type card

> [!abstract] Type card — continuous spectrum
> **Given.** **(H1)** $X$ geometrically finite, non-compact. **(H2)** $n_C\geq1$ cusps.
>
> **Produces.** The spectral picture (D1),(D2): a discrete part plus a continuum of multiplicity $n_C$ with Eisenstein generalised eigenfunctions.
>
> **Lets you.** See precisely which hypothesis of §5.1 fails, and hence what §5.2 must replace: **$\mathrm{Tr}$ by the [[Def - Renormalised Integral and the 0-Trace|0-trace]], and $\zeta_X$ by $\zeta^0_X$.** Nothing else about Eisenstein series is used.

---

# Depends on

- [[Def - Geometrically Finite Surfaces, Cusps and Funnels]] — cusps, funnels, the finite/infinite-area split
- [[Def - Critical Exponent]] — (F3): infinite area $\iff\delta<1$
- 🟢 spectral theory of self-adjoint operators, continuous spectrum, generalised eigenfunctions — *Functional Analysis* (8,10)
- Sources: Iwaniec, *Spectral Methods of Automorphic Forms*; Borthwick, *Spectral Theory of Infinite-Area Hyperbolic Surfaces*

---

# Checks

**Instance.** The modular surface $\mathrm{PSL}(2,\mathbb{Z})\backslash\mathbb{H}^2$: finite area, one cusp, so continuous spectrum $[\tfrac14,\infty)$ of multiplicity $1$, plus the Maass cusp forms as $L^2$ eigenvalues.

**Non-instance (fails H1's non-compactness).** $X$ closed: no cusps, no continuous spectrum, $e^{-t\Delta_X}$ trace class. §5.1 applies verbatim and $\det_0=\det_\zeta$.

**Non-instance (fails F2).** $X$ of infinite area, e.g. a funnel surface: the constants are not in $L^2$, so $0\notin\mathrm{Spec}_{L^2}$; by (F3) the determinant identity holds at $s=1$ directly with $Z_X(1)\neq0$.

---

# Used at

- [[Def - Renormalised Integral and the 0-Trace]] — the object that replaces $\mathrm{Tr}$
- [[Ext - Borthwick–Judge–Perry Determinant Formula]] — $n_C$ enters its formula explicitly
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Finite-Area Case)]] — (F2) is why $Z_X'(1)$ appears
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] §5.2

---

# Commentary

> [!note]- Commentary (skippable)
> The section needs almost nothing from the theory of Eisenstein series — they appear once, to name what the continuous spectrum's generalised eigenfunctions are, and then never again. What is actually load-bearing is the negative fact: **no discrete spectrum means no $\sum\lambda_j^{-s}$, and no trace class means no heat trace.** Everything §5.2 does is engineered around that.
>
> There is a choice of repair, and the paper names both. One can define a *relative* determinant, comparing $\Delta_X$ to a model operator on the ends so the divergences cancel; or one can keep $\Delta_X$ and regularise the trace itself. The paper takes the second, following Melrose: compactify $X$ by capping each end with a circle at infinity, use that the heat kernel has a controlled expansion there, and integrate the diagonal in a renormalised sense. The advantage is that the resulting $\det_0$ reduces to $\det_\zeta$ on a closed surface with nothing to reconcile.
