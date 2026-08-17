---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds"
  - "Thm - The H3 Fundamental-Slab Heat-Kernel Identity"
  - "Thm - Collapsing the Time Integral into the Weighted Potential Measure"
tags: [paper, loop-measures, kleinian-groups]
---

# Signature

| symbol | type |
|---|---|
| $\phi$ | one of the Bernstein functions treated; $V_\phi$ its [[Constr - The Weighted Potential Measure Vϕ\|weighted potential measure]] |
| $L$ | $=mL_\gamma=m\ell_\gamma+im\theta_\gamma\in\mathbb{C}$ |
| $\lvert e^{L}-1\rvert^2$ | $=2e^{m\ell_\gamma}\big(\cosh(m\ell_\gamma)-\cos(m\theta_\gamma)\big)>0$ |
| $s$ | the **subordination** variable inside the integral (not the spectral parameter) |
| $\psi^\phi_t$ | the law of the subordinator at time $t$ |

> **Convention.** In §7, $s$ denotes the subordination time, as in §2; the spectral parameter of §4–§6 does not appear, because §7 proves no zeta identity.

---

# Type card

> [!abstract] Type card — Theorem 7.2
> **Given.**
> **(H1)** $\phi$ Bernstein satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]].
> **(H2)** $\gamma\in\mathcal{P}_X$, $m\geq1$; $\tau$ in standard form (82), $L=mL_\gamma$.
> **(H3)** Theorem 7.1 and the slab identity (88).
>
> **Produces.**
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{\lvert e^{L}-1\rvert^2}\int_{(0,\infty)}\frac{2s\,e^{-s}}{(4\pi s)^{3/2}}\,e^{-(m\ell_\gamma)^2/4s}\,V_\phi(\mathrm{d}s).\tag{90}$$
>
> **Lets you.** Read off every subordinate case on a hyperbolic $3$-manifold from one integral against $V_\phi$ — the exact analogue of [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]], with the same geometric/analytic factorisation.

---

# Statement

> **Theorem 7.2 (mass of subordinate Brownian loop measure on hyperbolic $3$-manifolds).** Assume (H1)–(H3). Then (90) holds for every $\gamma\in\mathcal{P}_X$ and $m\geq1$.

---

# Discharges

| result | applied to | returns |
|---|---|---|
| [[Thm - General Homotopy Class Decomposition for Hyperbolic 3-Manifolds\|(85)]] | $p^E=p^\phi_{\mathbb{H}^3}$ | $\mu^\phi_X(\mathcal{C}_X(\gamma^m))=\int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}p^\phi_{\mathbb{H}^3}(t,w,\tau^mw)\,\mathrm{d}\mathrm{vol}$ |
| [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms\|(6)]] | $p^\phi_{\mathbb{H}^3}(t,\cdot,\cdot)=\int_{[0,\infty)}p_{\mathbb{H}^3}(s,\cdot,\cdot)\,\psi^\phi_t(\mathrm{d}s)$ | eq. (86) |
| [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity\|(88)]] | the inner spatial integral at time $s$ | $\frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{\lvert e^{L}-1\rvert^2}\cdot\frac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}$ |
| [[Thm - Collapsing the Time Integral into the Weighted Potential Measure\|Lem 2.11]] | $h(s)=\frac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}$ | $\int_0^\infty\frac{\mathrm{d}t}{t}\int h\,\mathrm{d}\psi^\phi_t=\int h\,\mathrm{d}V_\phi$ — giving (90) |
| [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]] | $\psi^\phi_t(\{0\})=0$ | the $s$-integral is over $(0,\infty)$, not $[0,\infty)$ |

---

# Proof

**Strategy.** Substitute the subordination formula into (85), evaluate the inner spatial integral by (88), then collapse the $\mathrm{d}t/t$-integral by Lemma 2.11. Three steps, each a citation.

> [!note]- Proof (skippable)
> Starting from (85) with $p^E=p^\phi_{\mathbb{H}^3}$ and expanding by Phillips subordination,
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\int_0^\infty\frac{\mathrm{d}t}{t}\int_{F_\tau}\int_{[0,\infty)}p_{\mathbb{H}^3}(s,w,\tau^mw)\,\psi^\phi_t(\mathrm{d}s)\,\mathrm{d}\mathrm{vol}_{\mathbb{H}^3}(w).\tag{86}$$
> The inner spatial integral is taken against the **Brownian** kernel at the subordination time $s$, so (88) applies with $t$ replaced by $s$:
> $$\mu^\phi_X\big(\mathcal{C}_X(\gamma^m)\big)=\frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{\lvert e^{L}-1\rvert^2}\int_0^\infty\frac{\mathrm{d}t}{t}\int_{[0,\infty)}\frac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}\,\psi^\phi_t(\mathrm{d}s).$$
> Applying Lemma 2.11 with $h(s)=\frac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}$ collapses the double integral into a single integral against $V_\phi$, giving (90). $\;\square$

---

# What this assumes, and where to climb

- **Theorem 7.1** — hence the unfolding stack, and the **assumed** periodisation convergence [[Constr - Loxodromic Standard Form and the H3 Fundamental Slab|(P5)]].
- **The slab identity (88)** — [[Thm - The H3 Fundamental-Slab Heat-Kernel Identity]], the one genuinely new computation of §7.
- **Lemma 2.11 and Assumption 2.3** — [[Thm - Collapsing the Time Integral into the Weighted Potential Measure]], [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)]]. Both are dimension-independent: they are statements about $(0,\infty)$.
- **Invariance transfer under subordination** — [[Ext - Phillips Subordination of Semigroups and Dirichlet Forms|(C5)]], which is what lets the subordinate kernel be lifted and periodised like the Brownian one.
- **Not assumed:** conformal invariance, or any restriction to $\theta_\gamma=0$.
- **The measure being computed** — [[Constr - The Subordinate Brownian Loop Measure]]; for jump $\phi$ the class must be read as in [[Constr - Loop Mass in a Homotopy Class for Jump Processes]].

---

# Consumed by

- [[Thm - Mass of Brownian Loop Measure in a Class on 3-Manifolds]] — the $\phi(\lambda)=\lambda$ case
- [[§7 Brownian Loops on Hyperbolic 3-Manifolds]] §7.2

---

# Commentary

> [!note]- Commentary (skippable)
> The theorem is Theorem 3.5 in dimension $3$ and the proof follows the same three moves — subordinate, evaluate spatially, collapse the time integral — with only the middle one different. That is the section's design: §3's architecture is dimension-independent, and the single dimension-specific input is the slab identity, which §7 supplies itself because the $\mathbb{H}^3$ heat kernel is elementary.
>
> The factorisation is worth reading off (90) directly. The **geometric** factor $\frac{2\pi e^{m\ell_\gamma}\ell_\gamma}{\lvert e^{L}-1\rvert^2}$ knows the complex length and nothing about $\phi$; the **analytic** factor $\int\frac{2se^{-s}}{(4\pi s)^{3/2}}e^{-(m\ell_\gamma)^2/4s}\,V_\phi(\mathrm{d}s)$ knows $\phi$ and only the real part $m\ell_\gamma$. So the holonomy angle $\theta_\gamma$ enters **only** through the denominator, never through the subordination integral — which is exactly why the special cases of §7 differ from those of §3 by a change of prefactor and nothing else.
>
> Note the shift in the analytic factor relative to §3: $e^{-s}$ rather than $e^{-s/4}$, and $s^{-3/2}\cdot s$ rather than $s^{-1/2}$, both coming from the $\mathbb{H}^3$ kernel's normalisation. When [[Ext - Gaussian Reciprocal Integral Identity|(GI)]] is applied in the Brownian case it is at $a=1$, not $a=\tfrac14$.
