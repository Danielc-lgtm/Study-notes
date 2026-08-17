---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, hyperbolic-geometry, heat-kernels]
---

# Signature

| symbol | type |
|---|---|
| $p_{\mathbb{H}^2}$ | $(0,\infty)\times\mathbb{H}^2\times\mathbb{H}^2\to(0,\infty)$; kernel of $e^{-s\Delta_{\mathbb{H}^2}}$ against $\rho$; speed $2$ |
| $s$ | $\in(0,\infty)$ — here the **subordination** variable, not the spectral parameter |
| $m$ | $\in\mathbb{Z}_{\geq1}$; $\ell_\gamma\in(0,\infty)$; $L:=m\ell_\gamma\in(0,\infty)$ |
| $\tau$ | $z\mapsto e^{\ell_\gamma}z$; $\tau^mz=e^Lz$ |
| $F_\tau$ | $=\{z\in\mathbb{H}^2:1\leq\operatorname{Im}z<e^{\ell_\gamma}\}$; $\rho(F_\tau)=\infty$ |
| $\rho$ | $\mathrm{d}\rho=(\operatorname{Im}z)^{-2}\mathrm{d}x\,\mathrm{d}y$ |

---

# Statement

> **(WX) Wang–Xue strip identity (Lemma 3.4).** *Precondition:*
> **(P1)** $s>0$;
> **(P2)** $m\in\mathbb{Z}_{\geq1}$, $\ell_\gamma>0$; $L:=m\ell_\gamma$;
> **(P3)** $\tau$ in [[Constr - Standard-Form Representative and the Fundamental Strip|standard form (9)]], $F_\tau$ the strip (12);
> **(P4)** $p_{\mathbb{H}^2}$ the **speed-2** Brownian heat kernel on $\mathbb{H}^2$.
>
> *Conclusion:*
> $$\int_{F_\tau}p_{\mathbb{H}^2}\big(s,z,e^{L}z\big)\,\mathrm{d}\rho(z) \;=\; \underbrace{\frac{\ell_\gamma}{2\sinh(L/2)}}_{\text{geometric}}\cdot\underbrace{\frac{e^{-s/4}\,e^{-L^2/(4s)}}{2\sqrt{\pi s}}}_{\text{analytic in }(s,L)}.\tag{20}$$

> [!warning] The factorisation is the point
> The geometric factor depends only on $(\ell_\gamma,m)$ and **never meets $V_\phi$**; the analytic factor depends only on $(s,L)$ and is the **only** thing $V_\phi$ integrates against. This split is what makes every special case in §3.1 a one-line substitution.

---

# Type card

> [!abstract] Type card — (WX)
> **Given.** (P1)–(P4).
>
> **Produces.** A positive real number, factorising as (geometric prefactor) $\times$ (analytic factor in $(s,L)$).
>
> **Lets you.** Discharge the spatial integral of [[Thm - General Homotopy Class Decomposition for Hyperbolic Surfaces|Theorem 3.2]] completely, leaving a one-dimensional integral in $t$ — exactly the shape [[Thm - Collapsing the Time Integral into the Weighted Potential Measure|Lemma 2.11]] consumes.

---

# Status

- **Proved here:** no.
- **Source:** Wang–Xue, *The Brownian loop measure on Riemann surfaces and applications to length spectra*, CPAM 78 (2025), Lemma 3.2 / eq. (20) in this paper.
- **DAG node that would close this:** *Spectral Geometry* (🔵) with *Riemannian Geometry*; the computation is elementary given the explicit $\mathbb{H}^2$ heat kernel.
- **What is safe to assume:** (20) verbatim under (P1)–(P4). No proof in the paper unfolds it.
- **The honest model of what its proof looks like:** [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity]], derived in full in §7 precisely because no citation is available there. Same strategy: the angular direction integrates out; the change of variables from the transverse coordinate to the displacement produces a $\sinh u$ cancelling the kernel's $1/\sinh u$; the strip's height gives the prefactor; a Gaussian remains.

---

# Used at

- [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces]] — the **sole** consumer; discharges the inner spatial integral of (19), after which Lemma 2.11 finishes
- [[Constr - The Weighted Heat-Kernel Integral Iϕ]] — $I_\phi(L)$ is the analytic factor integrated against $V_\phi$
- [[§3 Decomposition over Homotopy Classes]] — §3.1.1–3.1.4 run on the analytic factor

---

# Commentary

> [!note]- Commentary (skippable)
> Reading off each factor.
>
> **Analytic factor.** A one-dimensional Gaussian in the displacement times $e^{-s/4}$. The $e^{-L^2/4s}$ is the cost of travelling distance $L$ in time $s$ — the lifts of loops in $\mathcal{C}_X(\gamma^m)$ must cover at least that. The $2\sqrt{\pi s}$ is the one-dimensional normalisation: after integrating out the two transverse directions, one dimension is left, along the axis. And $e^{-s/4}$ is the signature of hyperbolic geometry — $\tfrac14=\inf\operatorname{spec}_{L^2}\Delta_{\mathbb{H}^2}$, appearing as exponential decay in time. **Every $\tfrac14$ in the paper — in $s=\tfrac12+\sqrt{\tfrac14+\kappa}$, in the range $\kappa\geq-\tfrac14$ — enters here.**
>
> **Geometric factor.** $\ell_\gamma$ is the height of the strip in the $\log\operatorname{Im}$ coordinate. $2\sinh(L/2)=e^{L/2}-e^{-L/2}$ is the transverse volume factor at displacement $L$; combined with the Gaussian it produces $1/(e^L-1)$ in the Brownian case, via $e^{-L/2}/2\sinh(L/2)=1/(e^L-1)$.
>
> **Convention warning.** At speed $1$ the factors would be $e^{-s/8}$ and $e^{-L^2/2s}$. Comparing against another source without checking the speed convention is the easiest way to get every constant in §3.1 wrong.
>
> Wang–Xue's paper is the immediate predecessor of this one: it establishes the Brownian case on surfaces, whence $\mu_X(\mathcal{C}_X(\gamma^m))=\frac1m\frac1{e^L-1}$ and the length-spectrum identity. This paper's contributions relative to it are the subordination framework and §7.
