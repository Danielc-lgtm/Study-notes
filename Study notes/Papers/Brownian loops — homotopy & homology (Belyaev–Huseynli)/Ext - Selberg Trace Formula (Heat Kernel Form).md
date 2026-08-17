---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, spectral-theory, hyperbolic-geometry]
---

# Signature

| symbol | type |
|---|---|
| $X=\Gamma\backslash\mathbb{H}^2$ | **closed** hyperbolic surface |
| $\{\lambda_j\}_{j\geq0}$ | the Laplace spectrum, with multiplicity |
| $S_X$ | $(0,\infty)\to(0,\infty)$ — the **geometric** term, defined below |
| $\mathcal{P}_X$ | primitive closed geodesics; $\ell(\gamma)=\ell_\gamma$ |
| $t$ | $>0$, the heat time |

---

# Statement

> **(STF) Selberg trace formula, heat-kernel form.** *Precondition:* **(P1)** $X$ closed hyperbolic. *Conclusion:*
> $$\sum_{j\geq0}e^{-t\lambda_j}=\underbrace{\mathrm{Area}(X)\frac{e^{-t/4}}{(4\pi t)^{3/2}}\int_0^\infty\frac{r\,e^{-r^2/(4t)}}{\sinh(r/2)}\,\mathrm{d}r}_{\text{identity contribution}}+\underbrace{S_X(t)}_{\text{hyperbolic contribution}},\tag{44}$$
> $$S_X(t):=\sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^{\infty}\frac{e^{-t/4}}{(4\pi t)^{1/2}}\cdot\frac{\ell(\gamma)}{2\sinh\big(m\ell(\gamma)/2\big)}\,e^{-(m\ell(\gamma))^2/(4t)}.$$

> **(F1) Asymptotics of $S_X$.** $S_X(t)$ is **exponentially small** as $t\downarrow0$; $\lvert S_X(t)-1\rvert$ is **exponentially small** as $t\to\infty$. Both are used to bound the correction $R_\kappa=O(\kappa)$ in Theorem 5.1(ii).
>
> **(F2) $S_X$ is the loop-measure integrand.** Comparing with [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Thm 3.5]]:
> $$\int_0^\infty\frac{S_X(t)}{t}\,\mathrm{d}t=\sum_{\gamma\in\mathcal{P}_X}\sum_{m\geq1}\mu_X\big(\mathcal{C}_X(\gamma^m)\big),$$
> and with a killing weight, $\displaystyle\int_0^\infty e^{-\kappa t}\frac{S_X(t)}{t}\,\mathrm{d}t=\sum_{\gamma,m}\mu^\kappa_X(\mathcal{C}_X(\gamma^m))=:M_\kappa$. **This identification is the hinge of all of §5.1.**
>
> **(F3) Term-by-term match.** The $(\gamma,m)$ summand of $S_X$, integrated $\int_0^\infty\frac{\mathrm{d}t}{t}e^{-\kappa t}(\cdot)$, is exactly the §3 mass formula — the same Gaussian integral [[Ext - Gaussian Reciprocal Integral Identity|(GI)]] with $a=\tfrac14+\kappa$, $b=(m\ell_\gamma)^2/4$.

---

# Type card

> [!abstract] Type card — (STF)
> **Given.** (P1).
>
> **Produces.** The identity (44): heat trace $=$ identity term $+$ geometric term, i.e. an equality between a **spectral** sum and a **length-spectrum** sum.
>
> **Lets you.** Convert the total loop mass into a heat trace and back. In this paper it is used only through (F2): $M_\kappa=\int_0^\infty e^{-\kappa t}S_X(t)\,\mathrm{d}t/t$, and the identity contribution is precisely the divergent, purely-local piece that regularisation removes.

---

# Status

- **Proved here:** no.
- **Source:** Selberg (1956); standard, see Buser, *Geometry and Spectra of Compact Riemann Surfaces*, Ch. 9; Hejhal.
- **DAG node that would close this:** 🔵 *Automorphic Forms / Selberg Trace Formula* (non-anchor). **A genuine gap** — the same one as [[Ext - Prime Geodesic Theorem]] and [[Ext - Meromorphic Continuation of the Selberg Zeta and L-Functions]]; all three are trace-formula consequences and none is proved in this note-set.
- **What is safe to assume:** (44),(F1),(F2),(F3). A reader taking (STF) on faith loses nothing: the paper never manipulates the identity contribution, only quotes that it is $X$-dependent through $\mathrm{Area}(X)$ alone.
- **Scope:** §5.1, via [[Ext - Naud's Formula for the Log-Determinant|(N)]] and the proof of Theorem 5.1.

> [!warning] The identity contribution is where the divergence lives
> $\int_0^\infty\frac{\mathrm{d}t}{t}\times$ (identity term) diverges at $t\downarrow0$ like $\mathrm{Area}(X)/4\pi t$; $\int_0^\infty\frac{\mathrm{d}t}{t}S_X(t)$ converges at $t\downarrow0$ by (F1) and diverges only at $t\to\infty$ (where $S_X\to1$), which the $\kappa>0$ weight or the tail subtraction $S_X-1$ handles. **The contractible class is the divergence; the non-trivial classes are almost fine.**

---

# Used at

- [[Ext - Naud's Formula for the Log-Determinant]] — (44) is its input
- [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]] — (F1),(F2) throughout the proof
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]]

---

# Commentary

> [!note]- Commentary (skippable)
> The trace formula is the reason this paper's two halves are the same subject. Its left side is spectral, its right side is a sum over closed geodesics with weight $\frac{\ell_\gamma}{2\sinh(m\ell_\gamma/2)}e^{-(m\ell_\gamma)^2/4t}$ — and that weight is, factor for factor, the mass of the free homotopy class of $\gamma^m$ before the $t$-integration. §3 derived it from scratch by unfolding a periodised heat kernel over a fundamental region, never mentioning Selberg; (F2) is the observation that the two derivations produce the same function.
>
> So the paper can be read as: the geometric side of the Selberg trace formula, decomposed loop-measure-theoretically, term by term. What §3 adds is the interpretation — each term is a *measure of a set of loops*, not just a number — and that interpretation is what makes normalisation into a probability measure possible.
