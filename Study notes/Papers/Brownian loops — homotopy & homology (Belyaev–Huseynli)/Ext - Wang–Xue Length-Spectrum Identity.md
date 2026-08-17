---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, hyperbolic-geometry, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $X$ | complete hyperbolic surface without boundary; possibly infinite type, cusps, funnels |
| $P$ | $\subseteq X$ non-empty, closed, [[Def - Polar Set\|polar]]; $X':=X\setminus P$ |
| $g$ | the metric on $X$; $g'$ the **unique complete hyperbolic metric on $X'$** — a *different* metric, with a cusp at each point of $P$ |
| $\simeq_X$ | free homotopy as curves **in $X$** |
| $\ell_\gamma,\ \ell_{\gamma'}$ | primitive geodesic lengths measured in $(X,g)$ and $(X',g')$ respectively |
| $\gamma,\gamma'$ | $\in\mathcal{P}_X$, $\in\mathcal{P}_{X'}$; $m,m'\in\mathbb{Z}_{\geq1}$ |

---

# Statement

> **(WXL) Wang–Xue length-spectrum identity (Theorem 3.9).** *Precondition:*
> **(P1)** $X$ a complete hyperbolic surface without boundary;
> **(P2)** $P\subseteq X$ non-empty, closed, polar for Brownian motion;
> **(P3)** $X'=X\setminus P$ carries its **own** complete hyperbolic metric $g'$ ([[Ext - Uniformisation of Punctured Hyperbolic Surfaces|(UN)]]);
> **(P4)** $\gamma\in\mathcal{P}_X$, $m\geq1$;
> **(P5)** the process is **pure Brownian motion** — no killing, no nonlinear subordination.
>
> *Conclusion:*
> $$\frac1m\cdot\frac{1}{e^{m\ell_\gamma}-1}\;=\;\sum_{\substack{\gamma'\in\mathcal{P}_{X'},\ m'\geq1\\ \gamma'^{m'}\simeq_X\gamma^m}}\frac{1}{m'}\cdot\frac{1}{e^{m'\ell_{\gamma'}}-1}.$$

---

# Type card

> [!abstract] Type card — (WXL)
> **Given.** (P1)–(P5).
>
> **Produces.** An identity between the geodesic length spectra of **two different hyperbolic surfaces**: one term on $(X,g)$ equals a sum over all classes on $(X',g')$ that fuse into it in $X$.
>
> **Lets you.** Trade [[Ext - Lawler–Werner Restriction and Conformal Invariance|(LW1)+(LW2)]] for an exact relation between length spectra — and, read backwards, see exactly which structural property each side pays for.

---

# Status

- **Proved here:** no.
- **Source:** Wang–Xue [WX25, Theorem 4.2].
- **DAG node that would close this:** *Riemann Surfaces* (🔵) for (P3); the argument itself is two applications of (LW1),(LW2) plus the Brownian mass formula.
- **What is safe to assume:** the conclusion under (P1)–(P5).
- **Sketch of the two moves** (all one needs to see why it is true): (LW1) says $\mu_X(\mathcal{C}_X(\gamma^m))=\mu_{X\setminus P,g}(\mathcal{C}_X(\gamma^m))$ since $P$ is polar; (LW2) then swaps the restricted $g$ for $g'$; recomputing the same number on $(X',g')$, the single class in $X$ splits into all classes that fuse under filling in the punctures, and the sum appears.

---

# Scope: what survives subordination

> **(S1) Restriction survives.** By [[Def - Polar Set|(F4)]], for $\phi(\lambda)=\lambda+\kappa$ the polar sets are Brownian ones, so
> $$\mu^\kappa_{X,g}\big(\mathcal{C}_X(\gamma^m)\big)=\mu^\kappa_{X\setminus P,\,g}\big(\mathcal{C}_X(\gamma^m)\big),$$
> with $g$ on the right the **ambient** metric restricted to $X\setminus P$, and the class measured in $X$ on both sides. Genuine, but weak: puncturing changes nothing *provided the metric is unchanged*.
>
> **(S2) Conformal invariance does not survive**, and the obstruction is exact:
> $$\Delta_{X,e^{2\sigma}g}=e^{-2\sigma}\Delta_{X,g},\qquad \phi\big(e^{-2\sigma}\Delta_{X,g}\big)\neq e^{-2\sigma}\phi\big(\Delta_{X,g}\big)\ \text{ unless }\phi(\lambda)=c\lambda .$$
> **So for every nonlinear subordination the metric cannot be swapped, and the comparison of length spectra collapses to (S1).**

---

# Used at

- [[§3 Decomposition over Homotopy Classes]] §3.4 — where the identity and its degeneration are discussed
- [[Constr - The Brownian Loop Measure]] — the **only** place both (P1) and (P2) of that page are used together

Nothing later in the paper depends on it; §3.4 is a coda.

---

# Commentary

> [!note]- Commentary (skippable)
> Both sides are the same loop mass, computed on two surfaces the loop measure cannot tell apart. Restriction says puncturing at a polar set costs nothing; conformal invariance says the punctured surface may then be re-metrised for free; and the identity is the same number computed before and after, with one homotopy class in $X$ splitting into many in $X'$.
>
> The two sides are genuinely about different geometry: the lengths $\ell_{\gamma'}$ are measured in the hyperbolic metric of $X'$ and are **longer** than the corresponding lengths in $X$ — adding a cusp lengthens the geodesics that must go around it. So this is a non-trivial constraint relating two length spectra, not bookkeeping.
>
> Its value in this paper is diagnostic. Having built a framework covering four process families, §3.4 is where the paper says out loud that one of the two structural properties motivating the whole subject is available only in the original case. (S2) is the sharpest statement anywhere of what subordination costs — and §7 opens by observing that this loss is precisely what frees the construction from dimension two.
