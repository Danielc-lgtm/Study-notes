---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - Polyakov's Conformal Anomaly Formula"
  - "Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)"
  - "Constr - The Brownian Loop Measure"
tags: [paper, spectral-geometry, determinants, conformal-geometry, loop-measures]
---

# Notation

- $X$ — a closed hyperbolic surface of genus $g$; $g_{\mathrm{hyp}}$ the hyperbolic representative of its conformal class
- $g=e^{2\sigma}g_{\mathrm{hyp}}$ — any smooth metric in that conformal class
- $P_X(\sigma)$ — the [[Thm - Polyakov's Conformal Anomaly Formula|Polyakov correction]] relative to $g_{\mathrm{hyp}}$
- $E\approx0.0538$, $C$ — the constants of Theorem 5.1; $\mathcal{G}(X)\setminus\mathcal{P}_X$ the non-primitive closed geodesics
- $N_X(R)$, $\widetilde{\mathrm{Li}}$ — the counting function and the cutoff logarithmic integral
- $Z'_X(1)$ — the derivative of the Selberg zeta function at $s=1$

---

# Type card

> [!abstract] Type card — Corollary 5.4 (Polyakov's formula via Brownian loop measure)
> **Given.** A closed hyperbolic surface $X$ of genus $g$; any smooth metric $g=e^{2\sigma}g_{\mathrm{hyp}}$ in the conformal class of $X$; [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1]] at the hyperbolic representative and [[Thm - Polyakov's Conformal Anomaly Formula|Theorem 5.3]] for the transformation law.
>
> **Produces.** $\log\det_\zeta\Delta_X$ for **every** metric in the conformal class, as the loop-measure formula at $g_{\mathrm{hyp}}$ plus the explicit Polyakov correction $P_X(\sigma)$ — a real number, in two equivalent forms (truncated Brownian, and the $\kappa\to0^+$ limit).
>
> **Lets you.** Move off the hyperbolic representative without recomputing anything: the loop-measure content is conformally invariant and therefore untouched, and all the metric dependence sits in one explicit local functional.

---

# Statement

> **Corollary 5.4 (Polyakov's formula via Brownian loop measure).** Let $X$ be a closed hyperbolic surface of genus $g$, and let $g=e^{2\sigma}g_{\mathrm{hyp}}$ be any smooth metric in the conformal class of $X$. Then
> $$\log\det{}_\zeta\Delta_X = P_X(\sigma) + \mathrm{Area}(X)E - C - \sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X\big(\mathcal{C}_X(\gamma)\big) - \int_{R=0}^\infty\frac{1}{e^R-1}\,\mathrm{d}\Big(N_X(R)-\widetilde{\mathrm{Li}}(e^R)\Big).\tag{57}$$
> Equivalently, via the $\kappa\to0^+$ limit in (49),
> $$\log\det{}_\zeta\Delta_X = P_X(\sigma) + \mathrm{Area}(X)E + \log Z'_X(1).\tag{58}$$

---

# Why it is true

One observation, and it is the payoff of a property established in §2.1.

**The loop-measure terms are conformally invariant.** By [[Constr - The Brownian Loop Measure|the second structural property]], $\mu_X$ is unchanged by a conformal rescaling $g_{\mathrm{hyp}}\mapsto e^{2\sigma}g_{\mathrm{hyp}}$; and the geodesic-counting terms $N_X(R)$, $\widetilde{\mathrm{Li}}(e^R)$, $\mathcal{P}_X$ and $Z'_X(1)$ are all computed in the *hyperbolic* metric, which is fixed. So every term on the right-hand side of Theorem 5.1 except $\mathrm{Area}(X)E$ — and $\mathrm{Area}(X)$ is the *hyperbolic* area, also fixed — is a conformal invariant.

Therefore the entire metric dependence of $\log\det_\zeta\Delta_g$ as $g$ ranges over the conformal class is carried by the single term $P_X(\sigma)$ that Theorem 5.3 supplies. The corollary is Theorem 5.1 plus Theorem 5.3, with nothing to reconcile.

**The mechanism in one line: the loop-measure formula is conformally invariant, so rescaling the metric moves only the explicitly computable Polyakov correction.**

**Why this is not circular.** Theorem 5.1 was proved at the hyperbolic representative, using the Selberg trace formula, which requires a hyperbolic metric. Polyakov's formula requires no hyperbolicity — it holds for any conformal rescaling of any metric on a closed surface. The two therefore combine: one anchors the value at a distinguished point of the conformal class, the other propagates it to the whole class.

---

# Strategy

**Strategy.** Substitute Theorem 5.1's value of $\log\det_\zeta\Delta_{g_{\mathrm{hyp}}}$ into Theorem 5.3's specialised transformation law $\log\det_\zeta\Delta_g=P_X(\sigma)+\log\det_\zeta\Delta_{g_{\mathrm{hyp}}}$, noting that all the loop-measure and geodesic-counting terms are computed in the hyperbolic metric and are therefore unmoved.

> [!note]- Proof (skippable)
> By the specialisation of [[Thm - Polyakov's Conformal Anomaly Formula|Theorem 5.3]] to $g_0=g_{\mathrm{hyp}}$,
> $$\log\det{}_\zeta\Delta_g = P_X(\sigma) + \log\det{}_\zeta\Delta_{g_{\mathrm{hyp}}}.$$
> By [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)|Theorem 5.1(i)]], negating (46),
> $$\log\det{}_\zeta\Delta_{g_{\mathrm{hyp}}} = \mathrm{Area}(X)E - C - \sum_{\gamma\in\mathcal{G}(X)\setminus\mathcal{P}_X}\mu_X\big(\mathcal{C}_X(\gamma)\big) - \int_{R=0}^\infty\frac{1}{e^R-1}\,\mathrm{d}\Big(N_X(R)-\widetilde{\mathrm{Li}}(e^R)\Big),$$
> and substituting gives (57). Substituting instead the $\kappa\to0^+$ form (49), $\log\det_\zeta\Delta_{g_{\mathrm{hyp}}}=\mathrm{Area}(X)E+\log Z'_X(1)$, gives (58). $\;\square$

---

# What this assumes, and where to climb

**Theorem 5.1** — [[Thm - Zeta-Regularised Determinant via Loop Measure (Compact Case)]], and through it the Selberg trace formula, Naud's formula, the refined prime geodesic theorem, and [[Thm - Selberg Zeta Identity (Killing Case)|Corollary 4.3]].

**Theorem 5.3** — [[Thm - Polyakov's Conformal Anomaly Formula]], quoted.

**Conformal invariance of $\mu_X$** — [[Constr - The Brownian Loop Measure]]. This is the load-bearing hypothesis and the reason the corollary is one line rather than a recomputation. **It is available only for pure two-dimensional Brownian motion**: for any nonlinear subordination the operator $\phi(\Delta_{X,g})$ depends on $g$ and not merely on $[g]$, so there is no $\alpha$-stable or killing analogue of this corollary. Note the asymmetry with Theorem 5.1, which *does* have all three parts.

**Closedness and hyperbolicity of $X$**, inherited from both inputs.

---

# What consumes this

Nothing. Corollary 5.4 is the terminal result of §5.1 and of the compact case; §5.2 restarts with a different determinant on a different class of surfaces, and §6 uses Corollary 4.3 rather than anything from §5.1.

Its role is completeness: it extends a formula proved at one distinguished metric to an entire conformal class, and it does so at essentially no cost because of a property established two sections earlier.

---

# Reading it against the rest of the paper

This is the **second and last place conformal invariance is spent**, the first being [[Thm - Length-Spectrum Identity under Puncturing|Theorem 3.9]]. Reading the two together is the efficient way to see what the property is worth, and the mechanism is identical in both: an object built from $\mu_X$ does not move under a conformal change, so all the metric dependence isolates into an explicitly computable remainder. In §3.4 the remainder is the difference of two length spectra; here it is the local functional $P_X(\sigma)$.

The contrast with §7 is also worth drawing. §7 opens by asking what tied the construction to surfaces, and answers: conformal invariance, used in exactly two places — the Polyakov formula and the §3.4 length-spectrum identity. Since both die under subordination, working with $\kappa>0$ frees the whole construction from dimension two. **Corollary 5.4 is therefore one of the two results that §7 explicitly cannot generalise, and knowing why is knowing why §7 exists.**
