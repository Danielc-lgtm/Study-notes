---
type: corollary
subject: spectral-geometry
prereqs:
  - "Thm - Determinant as Renormalised Loop Mass"
  - "Thm - Polyakov Conformal Anomaly Formula"
  - "Def - Zeta-Regularised Determinant of the Laplacian"
  - "Def - Selberg and Ruelle Zeta Functions and the Critical Exponent"
tags: [paper, brownian-loops, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Corollary 5.4"
---

# Notation

- $X$ — a closed hyperbolic surface of genus $g \ge 2$, with its **hyperbolic metric** $g_{\mathrm{hyp}}$ (constant curvature $K \equiv -1$, so $\operatorname{Area}(X) = 4\pi(g - 1)$ by Gauss–Bonnet).
- $\sigma : X \to \mathbb R$ — a smooth real function on $X$, the **conformal factor** — i.e. $\sigma$ is the pointwise "log stretch factor" of the new metric relative to the hyperbolic one: at a point $p$ where $\sigma(p) = a$, every $g_{\mathrm{hyp}}$-length near $p$ is multiplied by $e^a$ to get the $g$-length.
- $g := e^{2\sigma}\,g_{\mathrm{hyp}}$ — an arbitrary smooth metric in the conformal class of $g_{\mathrm{hyp}}$.
- $\Delta_X = \Delta_{g_{\mathrm{hyp}}}$ (in the loop-measure identity) — the positive Laplace–Beltrami operator of the *hyperbolic* representative, whose loop measures $\mu^\kappa_X$ appear on the right-hand side.
- $\Delta_g$ — the positive Laplace–Beltrami operator of the general conformal metric $g$; its zeta-determinant $\det_\zeta\Delta_g$ (zero mode excluded) is the object of the corollary.
- $|\nabla\sigma|^2 = |\nabla_{g_{\mathrm{hyp}}}\sigma|^2$ — squared gradient computed in the hyperbolic metric.
- $\operatorname{vol}_g(X)$, $dA_{\mathrm{hyp}}$ — the area of $X$ in the metric $g$; the hyperbolic area element.
- $E$, $C$, $Z_X'(1)$, $N_X$, $\widetilde{\mathrm{Li}}$ — as in [[Thm - Determinant as Renormalised Loop Mass|Theorem 5.1]] (Naud constant, universal constant, Selberg derivative at $s = 1$, primitive geodesic counting function, cutoff logarithmic integral).
- $P_X(\sigma) := -\frac{1}{12\pi}\int_X |\nabla\sigma|^2\,dA_{\mathrm{hyp}} + \frac{1}{6\pi}\int_X \sigma\,dA_{\mathrm{hyp}} + \log\frac{\operatorname{vol}_g(X)}{4\pi(g - 1)}$ — the **Polyakov correction** relative to the hyperbolic metric.

> [!recall]- Conformally equivalent metrics $g = e^{2\sigma}\,g_{\mathrm{hyp}}$
> **Formally:** two Riemannian metrics $g_{\mathrm{hyp}}, g$ on the same smooth surface are conformally equivalent if there is a smooth $\sigma : X \to \mathbb R$ with $g_p = e^{2\sigma(p)}(g_{\mathrm{hyp}})_p$ at every point $p$. Pointwise, $g$ is a positive scalar multiple of $g_{\mathrm{hyp}}$.
> **In words:** the two metrics measure lengths differently (a segment of $g_{\mathrm{hyp}}$-length $L$ has $g$-length $e^{\sigma(p)}L$ at $p$) but measure **angles the same** — conformal equivalence preserves angles and rescales lengths pointwise. On a surface, every smooth metric is conformally equivalent to the (essentially unique) hyperbolic representative in its conformal class (Uniformisation Theorem).
> **Concretely:** on the round sphere $S^2$ with the standard metric $g_0$ of curvature $+1$, take $\sigma \equiv \log R$: then $g = R^2 g_0$ is the round metric of radius $R$; lengths are scaled by $R$, angles are unchanged. On a genus-$2$ hyperbolic surface, any smooth metric can be written $g = e^{2\sigma}\,g_{\mathrm{hyp}}$ for a unique $\sigma$ (up to a constant).

> [!recall]- Zeta-regularised determinant $\det_\zeta\Delta_g$
> **Formally:** for a closed surface with metric $g$ and Laplace eigenvalues $0 = \lambda_0 < \lambda_1 \le \cdots$, the spectral zeta $\zeta_{X,g}(s) = \sum_{j \ge 1}\lambda_j^{-s}$ (a series in a complex variable $s$) continues meromorphically, is regular at $s = 0$, and $\log\det_\zeta\Delta_g := -\zeta_{X,g}'(0)$.
> **In words:** the finite canonical stand-in for the divergent product of Laplace eigenvalues. Although the series $\sum_j \lambda_j^{-s}$ in a complex variable $s$ only converges when $\operatorname{Re} s > 1$, it extends to a well-defined complex-analytic function of $s$ on all of $\mathbb C$ except a few isolated poles — so its derivative at $s = 0$ is a definite finite number, and $-\zeta'(0)$ is finite.
> **Concretely:** $\det_\zeta\Delta_g$ is a positive real number attached to the surface-with-metric $(X, g)$. It depends on $g$ (not just the conformal class), and its dependence on the conformal factor is given by [[Thm - Polyakov Conformal Anomaly Formula|Polyakov's formula]]. See [[Def - Zeta-Regularised Determinant of the Laplacian]].

> [!recall]- Polyakov's conformal anomaly formula
> **Formally:** for a closed surface with $g = e^{2\sigma}g_0$ and $K_0$ the Gauss curvature of $g_0$,
> $$\log\det_\zeta\Delta_g \;=\; -\frac{1}{12\pi}\int_X|\nabla_{g_0}\sigma|^2\,d\!\operatorname{vol}_{g_0} - \frac{1}{6\pi}\int_X K_0\,\sigma\,d\!\operatorname{vol}_{g_0} + \log\frac{\operatorname{vol}_g(X)}{\operatorname{vol}_{g_0}(X)} + \log\det_\zeta\Delta_{g_0}.$$
> **In words:** the zeta-determinant is not conformally invariant on a surface; its variation under $g_0 \mapsto e^{2\sigma}g_0$ is an *explicit local integral* in $\sigma$ and the curvature $K_0$ of $g_0$, plus a volume-ratio term. This is the "conformal anomaly" of the 2-D scalar determinant.
> **Concretely:** if $\sigma$ is constant, $\int|\nabla\sigma|^2 = 0$ and $\int K_0\,\sigma\,d\!\operatorname{vol} = 2\pi\chi(X)\,\sigma$ by Gauss–Bonnet; the volume ratio is $e^{2\sigma}$; the formula becomes $\log\det_\zeta\Delta_g = -\frac{\chi(X)}{3}\sigma + 2\sigma + \log\det_\zeta\Delta_{g_0}$, an explicit shift. See [[Thm - Polyakov Conformal Anomaly Formula]].

---

# Statement

> **Corollary (Polyakov via loop measure; Belyaev–Huseynli Corollary 5.4).** Let $X$ be a closed hyperbolic surface of genus $g \ge 2$ with hyperbolic metric $g_{\mathrm{hyp}}$, and let $g = e^{2\sigma}\,g_{\mathrm{hyp}}$ be any smooth metric in the conformal class of $g_{\mathrm{hyp}}$. Then $\log\det_\zeta\Delta_g$ equals the Polyakov correction $P_X(\sigma)$ plus the same loop-measure expression as in the compact case of [[Thm - Determinant as Renormalised Loop Mass|Theorem 5.1]] evaluated on the *hyperbolic* representative:
> $$\log\det_\zeta\Delta_g \;=\; P_X(\sigma) \;+\; \operatorname{Area}(X)\,E \;-\; C \;-\; \!\!\!\sum_{\gamma \in \mathcal G(X) \setminus \mathcal P_X}\!\!\!\mu_X\big(C_X(\gamma)\big) \;-\; \int_0^\infty\frac{1}{e^R - 1}\,d\!\big(N_X(R) - \widetilde{\mathrm{Li}}(e^R)\big),$$
> equivalently (via the $\kappa \to 0$ limit of Theorem 5.1(ii)),
> $$\log\det_\zeta\Delta_g \;=\; P_X(\sigma) \;+\; \operatorname{Area}(X)\,E \;+\; \log Z_X'(1),$$
> where $\operatorname{Area}(X) = 4\pi(g - 1)$ is the hyperbolic area (not $\operatorname{vol}_g(X)$) and $\mu_X$, $Z_X'(1)$ are computed from the hyperbolic representative.

---

# In One Line

The zeta-determinant of the Laplacian on *any* metric in the conformal class of a closed hyperbolic surface is (loop-measure content of the hyperbolic representative) $+$ (explicit local Polyakov correction $P_X(\sigma)$) — a clean split between spectral/geodesic information (invariant across the conformal class) and conformal information (captured by $\sigma$).

---

# Why It's True

**Mechanism (one sentence).** *[[Thm - Determinant as Renormalised Loop Mass|Theorem 5.1]] (specifically its $\kappa \to 0$ limit form) computes $\log\det_\zeta\Delta_{g_{\mathrm{hyp}}}$ on the hyperbolic representative as $\operatorname{Area}(X)\,E + \log Z_X'(1)$; [[Thm - Polyakov Conformal Anomaly Formula|Polyakov's formula (Theorem 5.3)]] adds $P_X(\sigma)$ to move from $g_{\mathrm{hyp}}$ to $g = e^{2\sigma}g_{\mathrm{hyp}}$; substituting one into the other produces the corollary.*

Loop measures and the Selberg zeta are conformally *invariant* on a hyperbolic surface: they depend only on the length spectrum of closed geodesics, which is a property of the *hyperbolic* structure (Uniformisation gives a unique hyperbolic metric per conformal class, up to isometry). Polyakov's formula, by contrast, records *exactly* the conformal-anomaly correction between the hyperbolic representative and any other metric in the class. The corollary combines the two: the loop-measure content is the "hyperbolic invariant" of the conformal class, and $P_X(\sigma)$ is the piece that varies with the choice of metric.

---

# Proof

> [!note]- Proof (short — combine Theorems 5.1 and 5.3)
> **Step 1 — apply Polyakov's formula.** Take $g_0 = g_{\mathrm{hyp}}$ in [[Thm - Polyakov Conformal Anomaly Formula|Theorem 5.3]]. Since $g_{\mathrm{hyp}}$ has constant curvature $K_0 \equiv -1$, the curvature term is $-\frac{1}{6\pi}\int_X K_0\,\sigma\,dA_{\mathrm{hyp}} = \frac{1}{6\pi}\int_X\sigma\,dA_{\mathrm{hyp}}$. Substituting,
> $$\log\det_\zeta\Delta_g \;=\; -\frac{1}{12\pi}\int_X|\nabla\sigma|^2\,dA_{\mathrm{hyp}} \;+\; \frac{1}{6\pi}\int_X\sigma\,dA_{\mathrm{hyp}} \;+\; \log\frac{\operatorname{vol}_g(X)}{\operatorname{vol}_{g_{\mathrm{hyp}}}(X)} \;+\; \log\det_\zeta\Delta_{g_{\mathrm{hyp}}}.$$
> The first three terms on the right collect (with $\operatorname{vol}_{g_{\mathrm{hyp}}}(X) = 4\pi(g - 1)$) to exactly $P_X(\sigma)$ as defined in the Notation. So
> $$\log\det_\zeta\Delta_g \;=\; P_X(\sigma) \;+\; \log\det_\zeta\Delta_{g_{\mathrm{hyp}}}.$$
>
> **Step 2 — substitute Theorem 5.1's $\kappa \to 0$ line.** By Theorem 5.1(ii), $\kappa \to 0^+$ limit ([[Thm - Determinant as Renormalised Loop Mass]]), on the hyperbolic representative
> $$\log\det_\zeta\Delta_{g_{\mathrm{hyp}}} \;=\; \operatorname{Area}(X)\,E + \log Z_X'(1).$$
> Substituting into Step 1's conclusion gives the second form of the corollary. For the first form, use case (i) of Theorem 5.1 (the Brownian identity for $-\log\det_\zeta\Delta_{g_{\mathrm{hyp}}}$) and negate to get $\log\det_\zeta\Delta_{g_{\mathrm{hyp}}} = \operatorname{Area}(X)\,E - C - \sum_{\gamma \in \mathcal G(X)\setminus\mathcal P_X}\mu_X(C_X(\gamma)) - \int_0^\infty \frac{1}{e^R - 1}\,d(N_X - \widetilde{\mathrm{Li}}(e^R))$; adding $P_X(\sigma)$ yields the first display. $\blacksquare$

---

# Where the paper uses this

Central result of [[Paper - Brownian Loops — Homotopy and Homology — §5 Renormalising the Total Mass|§5.1.1]] — extends [[Thm - Determinant as Renormalised Loop Mass|Theorem 5.1]] from the hyperbolic representative to every metric in the conformal class. This is the version that connects the paper to Polyakov / bosonic-string / worldsheet-partition-function contexts, where $\log\det_\zeta\Delta_g$ appears as the sum-over-fluctuations weight around a classical background and one wants its dependence on the conformal factor.
