---
type: definition
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Fuchsian Group and the Quotient Surface"
tags: [paper, hyperbolic-geometry, spectral-theory]
---

# Signature

| symbol | type |
|---|---|
| $\Gamma$ | a Fuchsian group; $X=\Gamma\backslash\mathbb{H}^2$ geometrically finite |
| $z$ | $\in\mathbb{H}^2$, any base point (the value of $\delta$ does not depend on it) |
| $d$ | the hyperbolic distance on $\mathbb{H}^2$ |
| $\delta$ | $:=\inf\big\{s>0:\sum_{h\in\Gamma}e^{-s\,d(z,h\cdot z)}<\infty\big\}\in(0,1]$ |
| $\Lambda(\Gamma)$ | $\subseteq\partial\mathbb{H}^2$ — the limit set |
| $\Omega$ | $\subseteq T^1X$ — the non-wandering set of the geodesic flow |
| $\lambda_0$ | the bottom of $\mathrm{Spec}(\Delta_X)$ |

---

# Definition

> **Definition (critical exponent).** $\delta$ is the **exponent of convergence of the Poincaré series**
> $$\mathcal{P}(s,z):=\sum_{h\in\Gamma}e^{-s\,d(z,h\cdot z)},\qquad\delta:=\inf\{s>0:\mathcal{P}(s,z)<\infty\}.$$
> It measures the rate at which the orbit $\Gamma z$ accumulates on $\partial\mathbb{H}^2$.

> **(F1) Dichotomy used throughout.**
> $$\mathrm{area}(X)<\infty\iff\delta=1,\qquad \mathrm{area}(X)=\infty\Rightarrow\delta<1.$$
>
> **(F2) Patterson–Sullivan.** $\delta=\dim_{\mathrm{H}}\Lambda(\Gamma)$, the Hausdorff dimension of the limit set.
>
> **(F3) Dynamics.** $\delta$ is the **topological entropy** of the geodesic flow on $\Omega\subseteq T^1X$. In the finite-area case $\Omega=T^1X$.
>
> **(F4) Spectrum.** If $\delta>\tfrac12$ then $\lambda_0=\delta(1-\delta)$, lying below $\tfrac14$ (the bottom of the continuous spectrum when $X$ is non-compact). Finite area: $\delta=1$, $\lambda_0=0$.
>
> **(F5) Geodesic proliferation.** $\delta$ is also the exponential growth rate of the closed-geodesic counting function — see [[Ext - Prime Geodesic Theorem|(PGT)]]. **This is the only property §4.2 uses.**

---

# Type card

> [!abstract] Type card — $\delta$
> **Given.** **(H1)** $\Gamma$ Fuchsian, geometrically finite.
>
> **Produces.** A number $\delta\in(0,1]$ that is simultaneously: an abscissa of convergence, a Hausdorff dimension, an entropy, a spectral parameter, and a growth rate.
>
> **Lets you.** State the one inequality on which all of §4.2, §6 and the very existence of the probability measure depend: $s>\delta$. Read it as *decay rate beats proliferation rate*.

---

# Depends on

- [[Def - Fuchsian Group and the Quotient Surface]] — $\Gamma$ and its action
- [[Def - Geometrically Finite Surfaces, Cusps and Funnels]] — the finite/infinite-area dichotomy (F1)
- 🟢 Hausdorff dimension, topological entropy, $L^2$ spectra — *Functional Analysis* (8,10), *Dynamical Systems*
- Sources for (F2),(F3),(F4): Patterson, Sullivan; quoted, not used

---

# Checks

**Instance.** $X$ closed or finite-area with cusps: $\delta=1$. The convergence condition $s>\delta$ then reads $s>1$, i.e. $\tfrac12+\sqrt{\tfrac14+\kappa}>1$, i.e. $\boxed{\kappa>0}$. **This is why a strictly positive killing rate is needed on a finite-area surface** and why §5 must renormalise the Brownian ($\kappa=0$) case.

**Instance.** $X$ an infinite-area funnel surface (convex-cocompact, Schottky): $\delta<1$, so $s=1$ already satisfies $s>\delta$ and the **Brownian** total mass $-\log Z_X(1)$ is finite with no killing at all.

**Non-instance (fails F4's hypothesis).** $\delta\leq\tfrac12$: then $\delta(1-\delta)\geq\tfrac14$ and there is **no** $L^2$-eigenvalue below the continuous spectrum; (F4) says nothing. Thin Schottky groups are of this kind. §4.2 is unaffected — it only uses (F5).

---

# Used at

- [[Def - Selberg Zeta Function]] — the abscissa of convergence in (31)
- [[Ext - Prime Geodesic Theorem]] — the growth rate in (40)
- [[Thm - Finiteness of the Total Mass]] — the condition $s(\phi)>\delta$
- [[Thm - Selberg Zeta Criterion]] — $s>\delta$ guarantees absolute convergence
- [[§4 Zeta Identities and Finiteness of the Total Mass]]
- [[Thm - Distribution of the Total Homology of the Loop Soup]] — $\mathrm{Re}(s)>\delta$

---

# Commentary

> [!note]- Commentary (skippable)
> Five descriptions of one number, and only one of them is used. That is worth stating plainly: for the purposes of this paper $\delta$ is *the exponential growth rate of closed geodesics*, nothing more. (F2)–(F4) are context, and the paper lists them as such.
>
> The comparison $s>\delta$ has a clean reading. The mass of the class of $\gamma^m$ decays like $e^{-s\ell_\gamma}$ in the length of the geodesic; the number of geodesics of length $\leq R$ grows like $e^{\delta R}$. A sum of $e^{\delta R}$ terms of size $e^{-sR}$ converges exactly when $s>\delta$. Everything in §4.2 is that comparison made precise, with the logarithmic corrections of (PGT) deciding the boundary case $s=\delta$ — which diverges, like $\int^\infty\mathrm{d}R/R$.
>
> The one structural consequence: on a finite-area surface $\delta=1$ and the Brownian loop measure has infinite total mass over non-trivial classes. There is no probability measure on homotopy classes without either killing ($\kappa>0$) or renormalisation (§5). That tension is what the rest of the paper is organised around.
