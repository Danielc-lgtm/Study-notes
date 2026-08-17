---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)"
  - "Ext - Polyakov Conformal Anomaly Formula"
tags: [paper, spectral-theory, conformal-geometry]
---

# Signature

| symbol | type |
|---|---|
| $X$ | closed hyperbolic surface of genus $g\geq2$ |
| $g_{\mathrm{hyp}}$ | the hyperbolic representative of the conformal class |
| $\sigma$ | $X\to\mathbb{R}$ smooth; $g=e^{2\sigma}g_{\mathrm{hyp}}$ **any** metric in the class |
| $P_X(\sigma)$ | the Polyakov correction, [[Ext - Polyakov Conformal Anomaly Formula\|(F1)]] |
| $E,C,\widetilde{\mathrm{Li}},N_X$ | as in [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)\|Theorem 5.1]] |

> **Convention.** All loop masses, geodesic lengths and counting functions on the right-hand sides are computed in $g_{\mathrm{hyp}}$, **not** in $g$. The only $g$-dependence is through $P_X(\sigma)$.

---

# Type card

> [!abstract] Type card — Corollary 5.4
> **Given.**
> **(H1)** $X$ closed hyperbolic of genus $g$.
> **(H2)** $g=e^{2\sigma}g_{\mathrm{hyp}}$, any smooth metric in the conformal class.
> **(H3)** Theorem 5.1(i) or (ii), and [[Ext - Polyakov Conformal Anomaly Formula|(P)]].
>
> **Produces.** $\log{\det}_\zeta\Delta_{X,g}$ for **every** metric in the class, as $P_X(\sigma)$ plus a quantity computed entirely from the hyperbolic length spectrum and Brownian loop masses:
> $$\log{\det}_\zeta\Delta_X=P_X(\sigma)+\mathrm{Area}(X)E-C-\sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X\big(\mathcal{C}_X(\gamma)\big)-\int_0^\infty\frac{\mathrm{d}\big(N_X(R)-\widetilde{\mathrm{Li}}(e^R)\big)}{e^R-1},\tag{57}$$
> $$=P_X(\sigma)+\mathrm{Area}(X)E+\log Z_X'(1).\tag{58}$$
>
> **Lets you.** Remove the constant-curvature restriction from §5.1 entirely. The loop measure only ever needs to be computed once per conformal class, on the hyperbolic representative.

---

# Statement

> **Corollary 5.4 (Polyakov's formula via Brownian loop measure).** Assume (H1)–(H3). Then (57) holds, and equivalently (58) via the $\kappa\to0^+$ limit (49).

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Ext - Polyakov Conformal Anomaly Formula\|(P)(F1)]] | $g_0=g_{\mathrm{hyp}}$, $g=e^{2\sigma}g_{\mathrm{hyp}}$ | $\log{\det}_\zeta\Delta_g=P_X(\sigma)+\log{\det}_\zeta\Delta_{g_{\mathrm{hyp}}}$ |
| [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)\|(46)]] | $\log{\det}_\zeta\Delta_{g_{\mathrm{hyp}}}$ | the loop-measure expression, sign-flipped |
| [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)\|(49)]] | the same | $\mathrm{Area}(X)E+\log Z_X'(1)$, giving (58) |
| Gauss–Bonnet | $g_{\mathrm{hyp}}$ | $\mathrm{Area}(X)=4\pi(g-1)$, the constant inside $P_X(\sigma)$ |

---

# Proof

**Strategy.** Substitute Theorem 5.1's value of $\log{\det}_\zeta\Delta_{g_{\mathrm{hyp}}}$ into the specialisation (F1) of Polyakov's formula. There is no further content.

> [!note]- Proof (skippable)
> By (P) with $g_0=g_{\mathrm{hyp}}$ and the specialisation (F1), $\log{\det}_\zeta\Delta_{X,g}=P_X(\sigma)+\log{\det}_\zeta\Delta_{X,g_{\mathrm{hyp}}}$. Theorem 5.1(i), i.e. (46), gives $\log{\det}_\zeta\Delta_{X,g_{\mathrm{hyp}}}$ as the negative of the right-hand side of (46), which is the tail of (57). Using instead the $\kappa\to0^+$ form (49) gives (58). $\;\square$

---

# What this assumes, and where to climb

- **(P)** — [[Ext - Polyakov Conformal Anomaly Formula]]. Quoted, and the only ingredient not already in §5.1.
- **Existence and uniqueness of $g_{\mathrm{hyp}}$ in the conformal class** — uniformisation, genus $g\geq2$. Cf. [[Ext - Uniformisation of Punctured Hyperbolic Surfaces]].
- **Theorem 5.1** — hence (N), (STF), (PGT$'$), and the whole §3–§4 stack.
- **Not assumed:** anything about $\sigma$ beyond smoothness. $P_X(\sigma)$ is finite for every smooth $\sigma$ on a closed surface.

---

# Consumed by

- [[§5 Zeta-Regularised Determinants and the Polyakov Anomaly]] §5.1.1
- Nothing further in the paper. §5.2 is about a different failure (continuous spectrum), not about conformal changes.

---

# Commentary

> [!note]- Commentary (skippable)
> The corollary is a two-line assembly, and its value is that it tells the reader exactly how far §5.1's machinery reaches: **the whole conformal class, from one computation on the hyperbolic representative.** The loop measure is genuinely tied to constant curvature — the unfolding argument of §3 uses that $X=\Gamma\backslash\mathbb{H}^2$ with $\Gamma$ acting by isometries, and the (WX) strip identity is a hyperbolic computation — so (57) is not a small extension.
>
> Read from the physics side, (58) is a complete answer to the one-loop partition function of a free scalar on any metric in a fixed conformal class of a genus-$g$ surface: a local Liouville-type functional $P_X(\sigma)$, plus a local area term, plus one global number $\log Z_X'(1)$ that depends on the point of Teichmüller space. Since $Z_X'(1)$ is determined by the length spectrum, and — by [[Thm - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]] — the marked length spectrum is determined by the loop masses, the entire content is visible to Brownian loops.
