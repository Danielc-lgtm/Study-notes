---
type: external
paper: "BH26"
subject: brownian-loops
tags: [paper, external, spectral-theory, microlocal-analysis]
---

# Signature

| symbol | type |
|---|---|
| $\bar X$ | compactification of $X$ with a circle at infinity on each end |
| $x$ | boundary defining function on $\bar X$ |
| $p_X(t,z,z)$ | the heat-kernel diagonal, $t>0$, $z\in X$ |
| ${}^0\mathrm{Tr}$ | the 0-trace, [[Def - Renormalised Integral and the 0-Trace\|(60)]] |
| $P$ | orthogonal projection onto $\ker_{L^2}\Delta_X$ |

---

# Statement

> **(M) Controlled expansion and the 0-trace.** *Precondition:*
> **(P1)** $X$ geometrically finite hyperbolic, $\bar X$ its compactification with fixed $x$;
> **(P2)** the ends are cusps or funnels in their standard coordinates.
>
> *Conclusion:*
> **(C1)** $p_X(t,\cdot,\cdot)$ has a controlled asymptotic expansion at the ends, so $\int_Xx^zp_X(t,z,z)\,\mathrm{d}\mathrm{vol}_g$ converges for $\mathrm{Re}(z)$ large and continues meromorphically in $z$; hence ${}^0\mathrm{Tr}(e^{-t\Delta_X})$ is defined for every $t>0$.
> **(C2)** ${}^0\mathrm{Tr}(e^{-t\Delta_X})\to\mathrm{rank}\,P$ **exponentially** as $t\to\infty$.
> **(C3)** As $t\downarrow0$, ${}^0\mathrm{Tr}(e^{-t\Delta_X})$ has an asymptotic expansion in powers of $t$ **and $t\log t$**, the logarithmic terms coming from the cusps.
> **(C4)** Consequently $\zeta^0_X$ of (61) continues meromorphically to $\mathbb{C}$ and is **regular at $s=0$**, so $(\zeta^0_X)'(0)$ and $\det_0\Delta_X$ are well defined.
> **(C5)** Riesz and Hadamard renormalisations agree on these functions.

---

# Type card

> [!abstract] Type card — (M)
> **Given.** (P1),(P2).
>
> **Produces.** (C1)–(C5): existence of ${}^0\mathrm{Tr}$, its behaviour at both ends of the $t$-range, and regularity of $\zeta^0_X$ at $0$.
>
> **Lets you.** Write down $\det_0\Delta_X$ at all. Without (C1) the definition (60) is empty; without (C3),(C4) the derivative $(\zeta^0_X)'(0)$ has no meaning.

---

# Status

- **Proved here:** no. §5.2 states the construction and refers out for the analysis.
- **Source:** Melrose, *The Atiyah–Patodi–Singer Index Theorem* (b-calculus and the b-trace); Guillopé–Zworski; Borthwick, *Spectral Theory of Infinite-Area Hyperbolic Surfaces* for the surface case and the explicit cusp/funnel coordinates.
- **DAG node that would close this:** **none exists.** Microlocal analysis / the b-calculus is absent from `Study notes/Prerequisite DAG.md`. A node here would also cover the renormalised Gauss–Bonnet of [[Def - Renormalised Integral and the 0-Trace|(F3)]].
- **What is safe to assume:** all of (C1)–(C5). The paper never manipulates the expansion; it uses only that $\det_0$ exists and reduces to $\det_\zeta$ on closed surfaces.
- **Scope:** §5.2's construction. Everything downstream goes through [[Ext - Borthwick–Judge–Perry Determinant Formula|(BJP)]], which is stated in terms of $\det_0$ and needs no further access to (M).

> [!warning] The 0-trace is not a trace
> ${}^0\mathrm{Tr}(AB)\neq{}^0\mathrm{Tr}(BA)$ in general — the b-trace has an anomaly. Nothing in this paper uses cyclicity, but the name invites the assumption, and it is false.

---

# Used at

- [[Def - Renormalised Integral and the 0-Trace]] — (C1)–(C5) are exactly its well-posedness
- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] §5.2

---

# Commentary

> [!note]- Commentary (skippable)
> This is the most technically remote import in the paper, and also the least consequential for reading it. Its entire job is to certify that a definition makes sense. A reader who grants (C1)–(C5) can follow §5.2 end to end: $\det_0$ is a number attached to $\Delta_X+\kappa$, (BJP) writes it through $Z_X(s)$ and some explicit Gamma and Barnes factors, and Corollary 4.3 replaces $-\log Z_X(s)$ by a total loop mass. The loop-measure content of §5.2 is one substitution; the analysis is all in the imports.
>
> Worth noting what the paper deliberately did **not** do. The alternative repair — a *relative* determinant comparing $\Delta_X$ against a model operator on the ends — avoids the b-calculus, but then the resulting object does not automatically reduce to $\det_\zeta$ in the compact case, and the comparison with §5.1 would need its own argument. Choosing Melrose's route buys (F2) of the 0-trace page for free.
