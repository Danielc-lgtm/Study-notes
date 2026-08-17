---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, spectral-theory, conformal-geometry]
---

# Signature

| symbol | type |
|---|---|
| $X$ | a **closed** surface |
| $g_0$ | a smooth metric; $K_0$ its Gauss curvature |
| $\sigma$ | $X\to\mathbb{R}$ smooth; $g:=e^{2\sigma}g_0$ — a **conformal** change |
| $\mathrm{vol}_g(X)$ | total area in $g$ |
| $g_{\mathrm{hyp}}$ | the unique hyperbolic representative of the conformal class; $K_0\equiv-1$, $\mathrm{vol}(X)=4\pi(g-1)$ |
| $P_X(\sigma)$ | the Polyakov correction relative to $g_{\mathrm{hyp}}$, defined below |

---

# Statement

> **(P) Polyakov's conformal anomaly formula.** *Precondition:*
> **(P1)** $X$ closed;
> **(P2)** $g_0$, $g=e^{2\sigma}g_0$ smooth conformally equivalent metrics;
> **(P3)** $K_0$ the Gauss curvature of $g_0$.
>
> *Conclusion:*
> $$\log{\det}_\zeta\Delta_{X,g}=-\frac{1}{12\pi}\int_X\lvert\nabla_{g_0}\sigma\rvert^2\,\mathrm{d}\mathrm{vol}_{g_0}-\frac{1}{6\pi}\int_XK_0\sigma\,\mathrm{d}\mathrm{vol}_{g_0}+\log\frac{\mathrm{vol}_g(X)}{\mathrm{vol}_{g_0}(X)}+\log{\det}_\zeta\Delta_{X,g_0}.\tag{56}$$

> **(F1) Hyperbolic base point.** With $g_0=g_{\mathrm{hyp}}$ ($K_0\equiv-1$, $\mathrm{vol}_{g_0}(X)=4\pi(g-1)$ by Gauss–Bonnet), the curvature term becomes $+\frac{1}{6\pi}\int_X\sigma\,\mathrm{d}A_{\mathrm{hyp}}$ and (56) reads $\log{\det}_\zeta\Delta_g=P_X(\sigma)+\log{\det}_\zeta\Delta_{g_{\mathrm{hyp}}}$ with
> $$P_X(\sigma):=-\frac{1}{12\pi}\int_X\lvert\nabla\sigma\rvert^2\,\mathrm{d}A_{\mathrm{hyp}}+\frac{1}{6\pi}\int_X\sigma\,\mathrm{d}A_{\mathrm{hyp}}+\log\frac{\mathrm{vol}_g(X)}{4\pi(g-1)}.$$
>
> **(F2) Only the conformal factor enters.** $P_X(\sigma)$ depends on $g$ through $\sigma$ alone. Two metrics in **different** conformal classes are not related by (P) at all.
>
> **(F3) Uniformisation supplies the base point.** Every conformal class on a closed surface of genus $g\geq2$ contains exactly one hyperbolic metric — see [[Ext - Uniformisation of Punctured Hyperbolic Surfaces]] for the version this note-set states.

---

# Type card

> [!abstract] Type card — (P)
> **Given.** (P1),(P2),(P3).
>
> **Produces.** The **transformation law** of $\log{\det}_\zeta\Delta$ under $g\mapsto e^{2\sigma}g$: an explicit local functional of $\sigma$. Type: equality of two real numbers, for each $\sigma$.
>
> **Lets you.** Extend any determinant formula from the hyperbolic representative to **every** metric in its conformal class, by adding $P_X(\sigma)$. Combined with [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|(49)]] this is [[Thm - Polyakov's Formula via Brownian Loop Measure|Corollary 5.4]].

---

# Status

- **Proved here:** no.
- **Source:** Polyakov (1981), *Quantum geometry of bosonic strings*; rigorous treatments by Osgood–Phillips–Sarnak, Alvarez.
- **DAG node that would close this:** 🔵 *Spectral Geometry* / conformal geometry. **A gap**, though a shallow one: the formula is quoted and used as a black box, and its derivation is independent of everything else here.
- **What is safe to assume:** (56) and (F1),(F2). The paper uses only the specialisation (F1).
- **Scope:** §5.1.1 only — Theorem 5.3 and Corollary 5.4. Non-compact versions exist and are referenced but not used.

> [!warning] The determinant is not a conformal invariant
> The whole point of (56) is that $\log{\det}_\zeta\Delta$ **changes** under conformal rescaling, by an explicit anomaly. There is no way to read a metric-independent statement out of §5.1.1; what one gets is a formula for the change.

---

# Used at

- [[Thm - Polyakov's Formula via Brownian Loop Measure]] — the sole consumer
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] §5.1.1

---

# Commentary

> [!note]- Commentary (skippable)
> The anomaly is the reason the determinant is interesting in string theory: the classical bosonic string action is conformally invariant, the quantised one is not, and (56) is the precise failure. Its structure — a Dirichlet energy of $\sigma$, a curvature coupling, and a volume term — is what the Liouville action is built from.
>
> For this paper the role is more modest and entirely instrumental. Theorem 5.1 computes $\log{\det}_\zeta\Delta$ on the **hyperbolic** representative of a conformal class, because the loop-measure machinery of §3 needs constant curvature $-1$: unfolding, translation lengths, and the (WX) strip identity all live on $\mathbb{H}^2$. (P) then transports the answer to every other metric in the class for free. So the division of labour is clean: the hyperbolic geometry does the global work, and Polyakov's formula does the conformal bookkeeping.
