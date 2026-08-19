---
type: proposition
subject: probability-geometry
prereqs:
  - "Def - Marked Length Spectrum"
  - "Thm - Mass of a Free Homotopy Class"
  - "Thm - Mass of a Subordinate Brownian Loop Class"
  - "Remark - The Range of the Killing Parameter"
tags: [paper, brownian-loops, spectral-geometry]
source: "Brownian Loops — Homotopy and Homology"
paper-ref: "Proposition 3.11"
---

# Notation

- $X = \Gamma\backslash\mathbb{H}^2$ — a geometrically finite hyperbolic surface.
- $\gamma \in \mathcal{P}_X$ — a primitive closed geodesic; $\ell_\gamma > 0$ its length.
- $C_X(\gamma^m)$ — the free homotopy class of the $m$-fold winding, mass $\mu_X(C_X(\gamma^m))$.
- $\mu_X$ — the standard Brownian loop measure on $X$; $\mu^\kappa_X$ the killed version with parameter $\kappa\ge -\tfrac14$.
- $\mathrm{MLS}$ — the marked length spectrum (Def 3.10).

> [!recall]- Marked length spectrum (Def 3.10)
> **Formally:** $\mathrm{MLS}(C_X(\gamma^m)) := \inf_{\eta\in C_X(\gamma^m)}\ell_g(\eta) = m\ell_\gamma$ on a hyperbolic surface. The *marked* aspect: the class label $C_X(\gamma^m)$ is preserved, not just the length value.
> **In words:** the length of the shortest (i.e. geodesic) representative of each free homotopy class, labelled by which class it comes from.
> **Concretely:** on a genus-2 surface with $\ell_{\gamma_1} = 1$, $\ell_{\gamma_2} = 1.5$, $\ell_{\gamma_3} = 2$: $\mathrm{MLS}$ maps $C_X(\gamma_1)\mapsto 1$, $C_X(\gamma_1^2)\mapsto 2$, $C_X(\gamma_2)\mapsto 1.5$, $C_X(\gamma_2^2)\mapsto 3$, $C_X(\gamma_3)\mapsto 2$, and so on — an infinite labelled sequence of positive reals. Note two classes share the same length ($C_X(\gamma_1^2)$ and $C_X(\gamma_3)$ both $\mapsto 2$), so the *unlabelled* length spectrum loses information. Full detail: [[Def - Marked Length Spectrum]].

> [!recall]- Closed forms of the Brownian and killed class-masses (§3.1)
> **Formally:** for $L = m\ell_\gamma$: 
> - **Brownian** ($\kappa = 0$): $\mu_X(C_X(\gamma^m)) = \frac{1}{m(e^L - 1)}$.
> - **Killed with $\kappa \ge -\tfrac14$**: $\mu^\kappa_X(C_X(\gamma^m)) = \frac{1}{m}\cdot\frac{e^{(\frac12 - \sqrt{1/4+\kappa})L}}{e^L - 1}$.
> Both are positive real numbers depending on $(\ell_\gamma, m, \kappa)$.
> **In words:** the closed-form class-mass has the exponential in the numerator and $e^L - 1$ in the denominator; the ratio is a strictly-decreasing function of $L$ in the useful range, so invertible.
> **Concretely:** for Brownian, $\ell_\gamma = 1$, $m = 1$: $\mu_X(C_X(\gamma)) = 1/(e - 1) \approx 0.582$; $\ell_\gamma = 2$, $m = 1$: $\mu_X(C_X(\gamma)) = 1/(e^2 - 1) \approx 0.157$. Larger geodesic ⇒ smaller mass, one-to-one. Full detail: [[Thm - Mass of a Subordinate Brownian Loop Class]] §3.1.1–3.1.2.

> [!recall]- Injectivity of a strictly-decreasing function
> **Formally:** if $f : (a, b)\to\mathbb{R}$ is strictly decreasing, then $f$ is injective: $f(x_1) = f(x_2) \Rightarrow x_1 = x_2$. Its inverse $f^{-1}$ is well-defined on the range of $f$.
> **In words:** a function that always goes down can never revisit the same value, so knowing $f(x)$ uniquely determines $x$.
> **Concretely:** $f(L) = e^{(1/2 - \sqrt{1/4+\kappa})L}/(e^L - 1)$ for $L > 0$, $\kappa\ge -\tfrac14$: to check it strictly decreases in $L$, compute the logarithmic derivative $\frac{d}{dL}\log f(L) = (\tfrac12 - \sqrt{1/4+\kappa}) - \frac{e^L}{e^L - 1}$; the first term is $\le \tfrac12$ (since $\sqrt{1/4+\kappa} \ge 0$), and the second term $\frac{e^L}{e^L - 1} > 1$, so $\log f'/f \le \tfrac12 - 1 = -\tfrac12 < 0$.

---

# Statement

> **Proposition (loop masses determine the length spectrum; Belyaev–Huseynli 3.11).** Let $X = \Gamma\backslash\mathbb{H}^2$ be a geometrically finite hyperbolic surface.
> (i) For every $\gamma\in\mathcal{P}_X$,
> $$\ell_\gamma \;=\; \log\!\Big(1 + \frac{1}{\mu_X(C_X(\gamma))}\Big).$$
> (ii) For the killed Brownian loop measure with parameter $\kappa \ge -\tfrac14$ (so $\phi(\lambda) = \lambda + \kappa$; see [[Remark - The Range of the Killing Parameter|Remark 3.7]]), $\mu^\kappa_X(C_X(\gamma))$ is strictly decreasing in $\ell_\gamma$, hence determines $\ell_\gamma$ uniquely (by inversion of the closed form of [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] §3.1.2). 
> In either case (i) or (ii), the family of loop-masses $\{\mu_X(C_X(\gamma^m)) : \gamma\in\mathcal{P}_X,\;m\ge 1\}$ determines the marked length spectrum $\mathrm{MLS}$ of $X$.

---

# In One Line

Invert the closed-form Brownian class-mass $\mu_X(C_X(\gamma)) = 1/(e^{\ell_\gamma} - 1)$ to read the geodesic length off the loop mass — and analogously for the killed case, where a strict-monotonicity argument replaces the algebraic inversion.

---

# Why It's True

**Mechanism (one sentence).** *The closed-form Brownian class-mass $\mu_X(C_X(\gamma)) = 1/(e^{\ell_\gamma} - 1)$ is an algebraic identity solvable for $\ell_\gamma$, and the killed version's log-derivative is strictly negative, so both maps $\ell_\gamma\mapsto\mu^\kappa_X(C_X(\gamma))$ are one-to-one, hence recoverable.*

The proposition is a straightforward *inversion* argument once the closed forms of §3.1 are in hand. The two parts differ only in how the inversion is done: for the Brownian case ($\kappa = 0$) it is a bare algebraic solve; for the killed case ($\kappa > 0$ or $\kappa\in[-\tfrac14, 0)$) the inversion is not in closed form but is guaranteed by strict monotonicity (the derivative argument).

The upshot: two hyperbolic surfaces $(X, g_1)$ and $(X, g_2)$ with the *same* class-mass function have the same primitive lengths $\ell_\gamma$ for every $\gamma\in\mathcal{P}_X$ (with matching class labels), hence the same marked length spectrum $\mathrm{MLS}$. This is the crucial input to [[Cor - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]], which then uses Otal–Croke rigidity to conclude that the two metrics agree up to Teichmüller-space isotopy.

---

# Proof

> [!note]- Gap-free proof
> **Part (i) — Brownian case.** By [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] §3.1.1, applied at $m = 1$ (so $L = \ell_\gamma$):
> $$\mu_X(C_X(\gamma)) \;=\; \frac{1}{1\cdot(e^{\ell_\gamma} - 1)} \;=\; \frac{1}{e^{\ell_\gamma} - 1}.$$
> Solve for $\ell_\gamma$: $e^{\ell_\gamma} - 1 = 1/\mu_X(C_X(\gamma))$, so $e^{\ell_\gamma} = 1 + 1/\mu_X(C_X(\gamma))$, and taking logs (the RHS is $> 1$, so the log is $> 0$):
> $$\ell_\gamma \;=\; \log\Big(1 + \frac{1}{\mu_X(C_X(\gamma))}\Big). \qquad\checkmark$$
>
> **Part (ii) — killed case.** By [[Thm - Mass of a Subordinate Brownian Loop Class|Theorem 3.5]] §3.1.2 at $m = 1$ (so $L = \ell_\gamma$):
> $$\mu^\kappa_X(C_X(\gamma)) \;=\; \frac{1}{1}\cdot\frac{e^{(\frac12 - \sqrt{1/4+\kappa})\ell_\gamma}}{e^{\ell_\gamma} - 1} \;=\; \frac{e^{(\frac12 - \sqrt{1/4+\kappa})\ell_\gamma}}{e^{\ell_\gamma} - 1}.$$
> Compute the logarithmic derivative in $\ell = \ell_\gamma$: writing $A := \tfrac12 - \sqrt{1/4+\kappa}$ and $f(\ell) := e^{A\ell}/(e^\ell - 1)$,
> $$\frac{d}{d\ell}\log f(\ell) \;=\; A - \frac{e^\ell}{e^\ell - 1}.$$
> - The first term $A = \tfrac12 - \sqrt{1/4+\kappa}$. Since $\kappa\ge -\tfrac14$, $\sqrt{1/4+\kappa}\ge 0$, so $A \le \tfrac12$.
> - The second term $\frac{e^\ell}{e^\ell - 1} = 1 + \frac{1}{e^\ell - 1} > 1$ for every $\ell > 0$.
> - Therefore $\frac{d}{d\ell}\log f(\ell) \le \tfrac12 - 1 = -\tfrac12 < 0$ uniformly in $\ell > 0$.
>
> So $\ell\mapsto\log f(\ell)$ is strictly decreasing in $\ell$, hence $\ell\mapsto f(\ell) = \mu^\kappa_X(C_X(\gamma))$ is strictly decreasing in $\ell = \ell_\gamma$. A strictly decreasing function is injective, so knowing $\mu^\kappa_X(C_X(\gamma))$ determines $\ell_\gamma$ uniquely. Same argument for every $m\ge 1$ (replace $\ell_\gamma$ by $L = m\ell_\gamma$; the monotonicity in $L$ is identical, and knowing $\mu^\kappa_X(C_X(\gamma^m))$ determines $L$, then dividing by $m$ gives $\ell_\gamma$).
>
> **Conclusion.** Both parts show: knowing $\mu^\kappa_X(C_X(\gamma^m))$ for all $(\gamma, m)$ determines $\ell_\gamma$ for every $\gamma\in\mathcal{P}_X$ (and hence the total length $m\ell_\gamma$ for every $(\gamma, m)$), with the class label $C_X(\gamma^m)$ preserved. So the loop-mass function *is* the marked length spectrum (up to an invertible reparametrisation). $\blacksquare$

---

# Where the paper uses this

Introduced in [[Paper - Brownian Loops — Homotopy and Homology — §3 Decomposition over Homotopy Classes|§3.4]]. The immediate downstream consequence is [[Cor - Loop Masses Determine the Hyperbolic Surface|Corollary 3.12]]: (loop masses ⇒ MLS by this Proposition) + (MLS ⇒ metric by Otal–Croke rigidity) ⇒ loop masses determine the surface up to Teichmüller-space isotopy.
