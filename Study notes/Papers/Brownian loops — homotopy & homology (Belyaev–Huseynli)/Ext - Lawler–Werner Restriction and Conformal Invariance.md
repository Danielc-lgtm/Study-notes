---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, probability, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $(X,g)$ | complete orientable Riemannian surface; $\partial X$ possibly non-empty, Dirichlet conditions |
| $\mu_{X,g}$ | the [[Constr - The Brownian Loop Measure\|Brownian loop measure]] on $\mathcal{C}_X$; $\sigma$-finite, infinite total mass |
| $X'$ | $\subseteq X$ open |
| $\eta$ | $\in\mathcal{C}_X$; $\eta\subseteq X'$ means the image of $\eta$ lies in $X'$ |
| $\sigma$ | $\in C^\infty(X,\mathbb{R})$; $e^{2\sigma}g$ the conformally rescaled metric |
| $[g]$ | the conformal class $\{e^{2\sigma}g:\sigma\in C^\infty(X,\mathbb{R})\}$ |

---

# Statement

> **(LW1) Restriction.** *Precondition:* $X'\subseteq X$ open. *Conclusion:*
> $$\mathrm{d}\mu_{X',g}(\eta)=\mathbf{1}_{\{\eta\subseteq X'\}}\,\mathrm{d}\mu_{X,g}(\eta).$$

> **(LW2) Conformal invariance.** *Precondition:* $\sigma\in C^\infty(X,\mathbb{R})$; **the process is two-dimensional Brownian motion** (no killing, no nonlinear subordination). *Conclusion:*
> $$\mu_{X,e^{2\sigma}g}=\mu_{X,g}.$$
> Hence $\mu_X$ depends only on $[g]$, and $X$ may be taken to be a Riemann surface.

> [!warning] Scope of each
> **(LW1) generalises; (LW2) does not.** (LW1) holds for every [[Constr - The Dirichlet-Form Loop Measure|Dirichlet-form loop measure]], because the part form $\mathcal{E}_{X'}$ *is* the form of the process killed on leaving $X'$, so its bridge measures are the ambient ones restricted to paths staying inside.
>
> (LW2) fails for every nonlinear subordination, and the obstruction is exact. In two dimensions a conformal change rescales the Laplacian,
> $$\Delta_{X,e^{2\sigma}g}=e^{-2\sigma}\Delta_{X,g},$$
> and for a Bernstein function $\phi$,
> $$\phi\big(e^{-2\sigma}\Delta_{X,g}\big)\neq e^{-2\sigma}\phi\big(\Delta_{X,g}\big)\qquad\text{unless }\phi(\lambda)=c\lambda,\ c>0.$$
> Conformal covariance is a *linear* phenomenon.

---

# Type card

> [!abstract] Type card — (LW1), (LW2)
> **Given.** For (LW1): $X'\subseteq X$ open. For (LW2): $\sigma\in C^\infty(X,\mathbb{R})$ and $\phi(\lambda)=\lambda$.
>
> **Produces.** Two identities of measures on $\mathcal{C}_X$: (LW1) $\mu_{X'}$ as an indicator restriction of $\mu_X$; (LW2) equality of $\mu_X$ across a conformal class.
>
> **Lets you.** Delete a set the process never visits at no cost (LW1); and change the metric within its conformal class at no cost (LW2). Used together, they give the length-spectrum identity of §3.4; used alone, (LW2) gives the Polyakov corollary of §5.1.1.

---

# Status

- **Proved here:** no.
- **Source:** Lawler–Werner, *The Brownian loop soup*, PTRF 128 (2004), Section 4.
- **DAG node that would close this:** *GFF Isomorphism Theorems / Loop Soups* (🔵); *Random Conformal Geometry* (🔵) for (LW2).
- **What is safe to assume:** both identities verbatim, under the scope stated in the warning above. No proof in the paper unfolds either.

---

# Used at

- [[Constr - The Brownian Loop Measure]] — carried as properties (P1),(P2)
- [[Ext - Wang–Xue Length-Spectrum Identity]] — uses **both**; the only place in the paper that does
- [[Thm - Polyakov's Formula via Brownian Loop Measure]] — uses (LW2): the loop-measure terms are conformally invariant, so all metric dependence isolates into $P_X(\sigma)$
- [[Constr - The Dirichlet-Form Loop Measure]] — inherits (LW1), not (LW2)
- [[Constr - The Subordinate Brownian Loop Measure]] — inherits (LW1), not (LW2)

**(LW2) is spent exactly twice in the paper: §3.4 and Corollary 5.4.** Both times the mechanism is identical — an object built from $\mu_X$ does not move under a conformal change, so all metric dependence isolates into an explicitly computable remainder.

---

# Commentary

> [!note]- Commentary (skippable)
> These two properties are why the Brownian loop measure is worth having as a *measure* rather than as a family of expectations: no probability measure on paths satisfies (LW1), because normalising destroys the additivity that restriction relies on.
>
> The asymmetry in scope is the diagnostic fact of the whole paper. §7 opens by asking what tied the construction to surfaces and answers: (LW2), used in exactly two results. Since (LW2) dies under any killing rate or nonlinear subordination — and §3.4 shows this explicitly — working with $\kappa>0$ frees the construction from dimension two entirely. So the honest reading is that the paper's generalisation to §7 is *paid for* by the loss recorded here.
