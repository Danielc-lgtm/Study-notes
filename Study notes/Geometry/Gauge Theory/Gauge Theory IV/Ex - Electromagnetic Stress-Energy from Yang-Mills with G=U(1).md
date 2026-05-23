---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - The Yang-Mills Lagrangian"
  - "Def - The Yang-Mills Field Strength"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Problem Statement

Derive the **electromagnetic stress-energy tensor** $T_{\mu\nu}^{\text{EM}}$ from the Yang-Mills Lagrangian $\mathcal{L}_{\text{YM}} = -\tfrac14 F^{\mu\nu}F_{\mu\nu}$ for $G = U(1)$, via the standard variational recipe $T_{\mu\nu} = -\frac{2}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,\mathcal{L})}{\delta g^{\mu\nu}}$. Verify that the resulting tensor:

(a) has the closed form $T_{\mu\nu}^{\text{EM}} = F_{\mu\alpha}F_\nu{}^\alpha - \tfrac14\eta_{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}$;
(b) is symmetric ($T_{\mu\nu} = T_{\nu\mu}$);
(c) is traceless ($T^\mu{}_\mu = 0$, in 4 dimensions);
(d) is conserved on shell: $\partial^\mu T_{\mu\nu} = 0$ when the Maxwell equation $\partial^\mu F_{\mu\nu} = 0$ holds (sourceless case).

**Recall:**

![[Def - The Yang-Mills Lagrangian#The Definition]]

![[Def - The Yang-Mills Field Strength#The Definition]]

The **electromagnetic field strength** for $G = U(1)$ is $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ (the commutator term vanishes). The components are $F_{0i} = -E_i$ (electric field) and $F_{ij} = \epsilon_{ijk}B_k$ (magnetic field).

The **stress-energy tensor** of a field theory is the symmetric tensor sourcing gravity in Einstein's equations $G_{\mu\nu} = 8\pi G T_{\mu\nu}$. It is the conserved current associated to spacetime translation invariance (the Noether charge of the external diffeomorphism symmetry), formalised as the variational derivative of the action with respect to the metric.

---

# Convergent Strategy

**Problem class.** This is a *Lagrangian-to-stress-energy* exercise — given an action, compute the stress-energy tensor via the metric-variation formula. The problem class is a standard one for any field theory coupled to gravity: scalar fields, Dirac spinors, electromagnetism, Yang-Mills, etc. all follow the same recipe. The topic page's problem-solving strategy identifies "derive an equation from a Lagrangian" as one of the dominant problem families, and this exercise is its stress-energy variant: instead of deriving an EOM by varying with respect to the dynamical field, derive $T_{\mu\nu}$ by varying with respect to the metric.

**Assumption pattern.** The single hypothesis is the form of the Maxwell Lagrangian $\mathcal{L}_{\text{YM}} = -\tfrac14 F^{\mu\nu}F_{\mu\nu}$. The key feature is that $\mathcal{L}_{\text{YM}}$ depends on the metric in two ways: through the explicit $g^{\mu\alpha}g^{\nu\beta}$ contractions in $F^{\mu\nu}F_{\mu\nu}$, and through the volume measure $\sqrt{-g}\,d^4x$ in the action. Both contributions must be tracked carefully under metric variation.

**Theorem routing.** No major theorem is needed — the calculation is a direct variational derivative. The route is: (1) compute $\delta(\sqrt{-g}) = -\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$; (2) compute $\delta(g^{\mu\alpha}g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta}) = 2 F^{\mu\nu}F_\mu{}^\beta\delta g_{\nu\beta} = -2 F_\mu{}^\alpha F_{\nu\alpha}\delta g^{\mu\nu}$ (after raising/lowering); (3) combine and read off $T_{\mu\nu}$ by the variational formula. The trace-freeness will follow from the special property that $F_{\mu\nu}$ is a *2-form* in 4 dimensions — the trace of "$F_{\mu\alpha}F^\nu{}^\alpha$" combined with the $\eta_{\mu\nu}$ contraction gives an exact cancellation.

**Key decision point.** The non-obvious choice is to *vary $g^{\mu\nu}$ rather than $g_{\mu\nu}$*. Both are valid (related by $\delta g^{\mu\nu} = -g^{\mu\alpha}g^{\nu\beta}\delta g_{\alpha\beta}$), but the variational formula for $T_{\mu\nu}$ is conventionally written in terms of $\delta g^{\mu\nu}$ — the upper-index metric. Choosing this convention from the start avoids sign errors and keeps the indices in the natural position. A second decision point: the *trace-freeness* in 4D is a coincidence of dimension. In $n$ dimensions, the trace is $T^\mu{}_\mu = (n-4)/4 \cdot F_{\alpha\beta}F^{\alpha\beta}$, vanishing only for $n = 4$. This reflects the **conformal invariance** of Maxwell theory in 4 dimensions and only in 4 dimensions.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory IV — Yang–Mills Fields and Instantons#Legal Operations|the topic page's Legal Operations]]:

1. **Use the trace pairing on the Lie algebra as an inner product** (operation 5). Although $\mathfrak{u}(1)$ is one-dimensional, the trace pairing reduces to the obvious scalar product, and the Yang-Mills Lagrangian $-\tfrac14 F^{\mu\nu}F_{\mu\nu}$ is built from this pairing — which the metric variation then varies.

2. **Integrate by parts in the Hodge inner product** (operation 1). Implicit in the variational derivation: when varying $\int \sqrt{-g}\,\mathcal{L}_{\text{YM}}\,d^4x$, the integration-by-parts machinery (and the fact that boundary terms vanish for compactly-supported metric variations) is what allows the integrand to be read off as $T_{\mu\nu}$.

---

# Hints

> [!note]- Hint 1
> The variational formula $T_{\mu\nu} = -\frac{2}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,\mathcal{L})}{\delta g^{\mu\nu}}$ involves the variation of both $\sqrt{-g}$ and $\mathcal{L}$ with respect to $g^{\mu\nu}$. Start by computing $\delta\sqrt{-g}$ in terms of $\delta g^{\mu\nu}$.

> [!note]- Hint 2
> $\delta\sqrt{-g} = \tfrac12\sqrt{-g}\,g^{\mu\nu}\delta g_{\mu\nu} = -\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$ (using $\delta g_{\mu\nu} = -g_{\mu\alpha}g_{\nu\beta}\delta g^{\alpha\beta}$). Now compute $\delta(F^{\mu\nu}F_{\mu\nu}) = \delta(g^{\mu\alpha}g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta})$, treating $F_{\mu\nu}$ as a fixed 2-form (the components $\partial_\mu A_\nu - \partial_\nu A_\mu$ do not involve the metric).

> [!note]- Hint 3
> The variation $\delta(g^{\mu\alpha}g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta})$ produces two terms (one for each $g^{-1}$ factor), each of the form $F_{\mu\nu}F_\alpha{}^\nu \delta g^{\mu\alpha}$ or similar. By symmetry, both terms can be combined as $2 F_{\mu\alpha}F^\nu{}^\alpha\delta g^{\mu\nu}$. Then collect with the $\delta\sqrt{-g}$ contribution to get $T_{\mu\nu}$.

---

# Solution

The strategy is to compute the metric variation of $\sqrt{-g}\,\mathcal{L}_{\text{YM}}$ in three pieces: the variation of $\sqrt{-g}$, the variation of $\mathcal{L}_{\text{YM}}$ via its two metric contractions. Combining gives $T_{\mu\nu}$, and direct algebra verifies symmetry, tracelessness, and conservation.

**Step 1: Variation of $\sqrt{-g}$.**

The standard formula is $\delta\sqrt{-g} = -\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$.

> [!note]- Derivation
> Use Jacobi's formula for the variation of a determinant: $\delta(\det M) = (\det M)\operatorname{tr}(M^{-1}\delta M)$. Applied to $M = g_{\mu\nu}$, this gives $\delta g = g\cdot g^{\mu\nu}\delta g_{\mu\nu}$, where $g = \det g_{\mu\nu}$. For a Lorentzian metric, $g < 0$, so $\sqrt{-g}$ is real, and $\delta(-g) = -\delta g = -g\cdot g^{\mu\nu}\delta g_{\mu\nu}$. Hence $\delta\sqrt{-g} = \delta((-g)^{1/2}) = \tfrac12(-g)^{-1/2}\delta(-g) = \tfrac12\sqrt{-g}\,g^{\mu\nu}\delta g_{\mu\nu}$.
>
> Convert to the upper-index variation: $g^{\mu\alpha}g_{\alpha\nu} = \delta^\mu_\nu \implies \delta g^{\mu\alpha}\cdot g_{\alpha\nu} + g^{\mu\alpha}\delta g_{\alpha\nu} = 0 \implies \delta g_{\alpha\nu} = -g_{\alpha\rho}g_{\nu\sigma}\delta g^{\rho\sigma}$. So $g^{\mu\nu}\delta g_{\mu\nu} = -g^{\mu\nu}g_{\mu\rho}g_{\nu\sigma}\delta g^{\rho\sigma} = -\delta^\nu_\rho g_{\nu\sigma}\delta g^{\rho\sigma} = -g_{\rho\sigma}\delta g^{\rho\sigma} = -g_{\mu\nu}\delta g^{\mu\nu}$ (relabelling). Hence $\delta\sqrt{-g} = -\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$.

**Step 2: Variation of $\mathcal{L}_{\text{YM}}$.**

$\delta\mathcal{L}_{\text{YM}} = -\tfrac14 \delta(g^{\mu\alpha}g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta}) = -\tfrac12 F^{\mu\nu}F_\nu{}^\beta\delta g_{\mu\beta} = +\tfrac12 F_\mu{}^\nu F_\nu{}^\beta g_{\mu\rho}g_{\beta\sigma}\delta g^{\rho\sigma}$ — i.e., $-\tfrac12 F_{\mu\alpha}F_\nu{}^\alpha\delta g^{\mu\nu}$ in the end.

> [!note]- Derivation
> $\delta(g^{\mu\alpha}g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta}) = 2 g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta}\delta g^{\mu\alpha}$ (the two metric variations give equal contributions by symmetry). Substituting and lowering indices: $g^{\nu\beta}F_{\mu\nu}F_{\alpha\beta} = F_{\mu\nu}F_\alpha{}^\nu$. So $\delta\mathcal{L}_{\text{YM}} = -\tfrac14 \cdot 2\cdot F_{\mu\nu}F_\alpha{}^\nu\delta g^{\mu\alpha} = -\tfrac12 F_{\mu\nu}F_\alpha{}^\nu\delta g^{\mu\alpha}$. Relabelling $\alpha \to \nu$ (free index): $\delta\mathcal{L}_{\text{YM}} = -\tfrac12 F_{\mu\alpha}F_\nu{}^\alpha\delta g^{\mu\nu}$.

**Step 3: Combine via the variational formula.**

$\delta(\sqrt{-g}\,\mathcal{L}_{\text{YM}}) = \delta\sqrt{-g}\cdot\mathcal{L}_{\text{YM}} + \sqrt{-g}\,\delta\mathcal{L}_{\text{YM}} = \sqrt{-g}\left[-\tfrac12 g_{\mu\nu}\mathcal{L}_{\text{YM}} - \tfrac12 F_{\mu\alpha}F_\nu{}^\alpha\right]\delta g^{\mu\nu}$.

Using $T_{\mu\nu} = -\frac{2}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,\mathcal{L})}{\delta g^{\mu\nu}}$ gives $T_{\mu\nu} = g_{\mu\nu}\mathcal{L}_{\text{YM}} + F_{\mu\alpha}F_\nu{}^\alpha = -\tfrac14 g_{\mu\nu}F^{\alpha\beta}F_{\alpha\beta} + F_{\mu\alpha}F_\nu{}^\alpha$, the EM stress-energy tensor.

> [!note]- Derivation
> Combining Steps 1 and 2: $\delta(\sqrt{-g}\,\mathcal{L}_{\text{YM}}) = -\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}\cdot\mathcal{L}_{\text{YM}} + \sqrt{-g}\cdot(-\tfrac12 F_{\mu\alpha}F_\nu{}^\alpha\delta g^{\mu\nu})$. Factor out $\sqrt{-g}\delta g^{\mu\nu}$: $\delta(\sqrt{-g}\,\mathcal{L}_{\text{YM}}) = \sqrt{-g}\delta g^{\mu\nu}\cdot[-\tfrac12 g_{\mu\nu}\mathcal{L}_{\text{YM}} - \tfrac12 F_{\mu\alpha}F_\nu{}^\alpha]$.
>
> Apply the formula $T_{\mu\nu} = -\frac{2}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,\mathcal{L})}{\delta g^{\mu\nu}} = -2[-\tfrac12 g_{\mu\nu}\mathcal{L}_{\text{YM}} - \tfrac12 F_{\mu\alpha}F_\nu{}^\alpha] = g_{\mu\nu}\mathcal{L}_{\text{YM}} + F_{\mu\alpha}F_\nu{}^\alpha$.
>
> Substituting $\mathcal{L}_{\text{YM}} = -\tfrac14 F^{\alpha\beta}F_{\alpha\beta}$:
> $$T_{\mu\nu}^{\text{EM}} = F_{\mu\alpha}F_\nu{}^\alpha - \tfrac14\eta_{\mu\nu}F^{\alpha\beta}F_{\alpha\beta},$$
> where $\eta_{\mu\nu} = g_{\mu\nu}|_{\text{flat}}$ for the Minkowski case.

**Step 4: Verify symmetry, tracelessness, and conservation.**

*Symmetry:* $T_{\mu\nu} = T_{\nu\mu}$ because $F_{\mu\alpha}F_\nu{}^\alpha = F_\nu{}^\alpha F_{\mu\alpha}$ (commutative scalar product) and $\eta_{\mu\nu}$ is symmetric.

*Tracelessness in 4D:* $T^\mu{}_\mu = F^{\mu\alpha}F_{\mu\alpha} - \tfrac14\delta^\mu_\mu F^{\alpha\beta}F_{\alpha\beta} = F^{\alpha\beta}F_{\alpha\beta} - \tfrac14 \cdot 4 \cdot F^{\alpha\beta}F_{\alpha\beta} = 0$.

*Conservation on shell:* $\partial^\mu T_{\mu\nu} = \partial^\mu(F_{\mu\alpha}F_\nu{}^\alpha) - \tfrac14\partial_\nu(F^{\alpha\beta}F_{\alpha\beta})$. The first term is $(\partial^\mu F_{\mu\alpha})F_\nu{}^\alpha + F_{\mu\alpha}\partial^\mu F_\nu{}^\alpha$. The Maxwell equation $\partial^\mu F_{\mu\alpha} = 0$ kills the first piece. The second piece combines with the gradient term via the Bianchi identity $\partial_\mu F_{\nu\rho} + \partial_\nu F_{\rho\mu} + \partial_\rho F_{\mu\nu} = 0$ to give a vanishing total. Details below.

> [!note]- Derivation
> *Conservation calculation.* $\partial^\mu T_{\mu\nu} = (\partial^\mu F_{\mu\alpha})F_\nu{}^\alpha + F_{\mu\alpha}\partial^\mu F_\nu{}^\alpha - \tfrac12 F^{\alpha\beta}\partial_\nu F_{\alpha\beta}$.
>
> The first term vanishes by Maxwell's equation $\partial^\mu F_{\mu\alpha} = 0$ (sourceless case).
>
> For the remaining two terms, use the Bianchi identity $\partial^\mu F_\nu{}^\alpha + \partial_\nu F^{\alpha\mu} + \partial^\alpha F^\mu{}_\nu = 0$ (cycled in $(\mu, \nu, \alpha)$ in the lower indices, raised appropriately). Equivalently $\partial^\mu F_\nu{}^\alpha = -\partial_\nu F^{\alpha\mu} - \partial^\alpha F^\mu{}_\nu$. Substituting:
> $$F_{\mu\alpha}\partial^\mu F_\nu{}^\alpha = -F_{\mu\alpha}\partial_\nu F^{\alpha\mu} - F_{\mu\alpha}\partial^\alpha F^\mu{}_\nu.$$
> The first piece becomes $-F_{\mu\alpha}\partial_\nu F^{\alpha\mu} = +F_{\mu\alpha}\partial_\nu F^{\mu\alpha} = +\tfrac12\partial_\nu(F_{\mu\alpha}F^{\mu\alpha})$ (the antisymmetry $F^{\alpha\mu} = -F^{\mu\alpha}$ flips the sign once, then $\tfrac12$ comes from the product rule absorbing the symmetric pair).
>
> The second piece $-F_{\mu\alpha}\partial^\alpha F^\mu{}_\nu$ equals $F_{\alpha\mu}\partial^\alpha F^\mu{}_\nu$ (by antisymmetry of $F$ in $(\mu, \alpha)$), which by relabelling dummies $(\alpha\leftrightarrow\mu)$ is $F_{\mu\alpha}\partial^\mu F^\alpha{}_\nu = -F_{\mu\alpha}\partial^\mu F_\nu{}^\alpha$, equal in magnitude and opposite sign to the LHS. So we have $F_{\mu\alpha}\partial^\mu F_\nu{}^\alpha = \tfrac12\partial_\nu(F_{\mu\alpha}F^{\mu\alpha}) - F_{\mu\alpha}\partial^\mu F_\nu{}^\alpha$, giving $2 F_{\mu\alpha}\partial^\mu F_\nu{}^\alpha = \tfrac12\partial_\nu(F_{\mu\alpha}F^{\mu\alpha})$, i.e., $F_{\mu\alpha}\partial^\mu F_\nu{}^\alpha = \tfrac14\partial_\nu(F_{\mu\alpha}F^{\mu\alpha})$. This *exactly cancels* the third term $-\tfrac14\partial_\nu(F^{\alpha\beta}F_{\alpha\beta})$ in $\partial^\mu T_{\mu\nu}$.
>
> So $\partial^\mu T_{\mu\nu} = 0$ on shell. $\blacksquare$

> [!note]- Complete formal solution
> *Given:* Maxwell Lagrangian $\mathcal{L}_{\text{YM}} = -\tfrac14 F^{\mu\nu}F_{\mu\nu}$ for $G = U(1)$, with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ independent of the metric.
>
> *To compute:* The stress-energy tensor $T_{\mu\nu} = -\frac{2}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,\mathcal{L})}{\delta g^{\mu\nu}}$.
>
> By Jacobi's formula, $\delta\sqrt{-g} = -\tfrac12\sqrt{-g}\,g_{\mu\nu}\delta g^{\mu\nu}$. By direct calculation with the metric contractions, $\delta\mathcal{L}_{\text{YM}} = -\tfrac12 F_{\mu\alpha}F_\nu{}^\alpha\delta g^{\mu\nu}$. Combining:
> $$\delta(\sqrt{-g}\,\mathcal{L}_{\text{YM}}) = \sqrt{-g}\left[-\tfrac12 g_{\mu\nu}\mathcal{L}_{\text{YM}} - \tfrac12 F_{\mu\alpha}F_\nu{}^\alpha\right]\delta g^{\mu\nu}.$$
> Hence $T_{\mu\nu} = g_{\mu\nu}\mathcal{L}_{\text{YM}} + F_{\mu\alpha}F_\nu{}^\alpha = -\tfrac14\eta_{\mu\nu}F^{\alpha\beta}F_{\alpha\beta} + F_{\mu\alpha}F_\nu{}^\alpha$, the standard EM stress-energy.
>
> *Symmetric* ($T_{\mu\nu} = T_{\nu\mu}$): immediate from the symmetry of both summands.
>
> *Traceless in 4D* ($T^\mu{}_\mu = 0$): $T^\mu{}_\mu = F^{\mu\alpha}F_{\mu\alpha} - \tfrac14\cdot 4\cdot F^{\alpha\beta}F_{\alpha\beta} = 0$. (In $n$ dimensions, $T^\mu{}_\mu = (1 - n/4)F^{\alpha\beta}F_{\alpha\beta}$, vanishing only in 4D — reflecting conformal invariance of Maxwell in 4D.)
>
> *Conserved* ($\partial^\mu T_{\mu\nu} = 0$ on shell): see the derivation under Step 4. The key combinatorial identity uses both Maxwell's equation $\partial^\mu F_{\mu\alpha} = 0$ and the Bianchi identity $\partial_{[\mu}F_{\nu\rho]} = 0$ — both halves of the Maxwell pair are needed to ensure conservation. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might try to compute $T_{\mu\nu}$ as the "canonical stress-energy tensor" via the Noether construction for spacetime translations: $T^{\mu\nu}_{\text{can}} = \partial^\nu\phi\cdot(\partial\mathcal{L}/\partial(\partial_\mu\phi)) - \eta^{\mu\nu}\mathcal{L}$. For Maxwell with $\phi = A^\alpha$, this gives $T^{\mu\nu}_{\text{can}} = \partial^\nu A^\alpha\cdot F^\mu{}_\alpha - \tfrac14\eta^{\mu\nu}F^{\alpha\beta}F_{\alpha\beta}$, which is *not* gauge-invariant (it depends on $A$, not just on $F$) and is not symmetric in $(\mu, \nu)$. The "improvement procedure" (Belinfante–Rosenfeld) adds a tensor of the form $\partial_\lambda(A^\nu F^{\mu\lambda})$ to symmetrise and gauge-invariantise, producing the same $T^{\mu\nu}_{\text{EM}}$ as the metric variation. The metric-variation route is *cleaner* because it produces the symmetric, gauge-invariant form directly.

---

# Key Takeaways

**The metric variation is the universal recipe for the stress-energy tensor.** Whenever a field theory is coupled to gravity via $S = \int\sqrt{-g}\,\mathcal{L}\,d^4x$, the stress-energy tensor is $T_{\mu\nu} = -\frac{2}{\sqrt{-g}}\frac{\delta(\sqrt{-g}\,\mathcal{L})}{\delta g^{\mu\nu}}$. This recipe automatically produces a *symmetric*, *gauge-invariant* (when $\mathcal{L}$ is gauge-invariant) tensor — unlike the canonical Noether-construction stress-energy, which generically lacks both properties. The reusable principle: when in doubt about whether you have the "correct" stress-energy tensor, use the metric variation. It produces the tensor that sources Einstein's equations and that is conserved on shell, and it does so without ambiguity. The trigger to recognise the technique: any field theory whose Lagrangian explicitly involves the metric (either through index contractions or through the volume measure $\sqrt{-g}$) admits a stress-energy tensor computable by this recipe. For Maxwell, the result $T_{\mu\nu}^{\text{EM}} = F_{\mu\alpha}F_\nu{}^\alpha - \tfrac14\eta_{\mu\nu}F^2$ is the unique gauge-invariant symmetric traceless conserved 2-tensor built from $F$, which is the reason it appears in every electrodynamics textbook from Jackson onwards.

**Conformal invariance manifests as tracelessness in 4D.** The Maxwell Lagrangian $-\tfrac14 F^{\mu\nu}F_{\mu\nu}\sqrt{-g}\,d^4x$ is invariant under conformal rescalings $g_{\mu\nu} \to e^{2\sigma}g_{\mu\nu}$ in 4 dimensions: the factor $\sqrt{-g} \to e^{4\sigma}\sqrt{-g}$ scales by $e^{4\sigma}$, the inverse-metric factors $g^{\mu\alpha}g^{\nu\beta}$ in $F^{\mu\nu}F_{\mu\nu}$ scale by $e^{-4\sigma}$, and the product is invariant. By the variational identity, conformal invariance of the action implies tracelessness of the stress-energy tensor: $T^\mu{}_\mu = 0$ in 4D. This is the structural reason for the trace-freeness — not a coincidence of dimension but a consequence of the conformal-invariance feature special to 4D Maxwell. The transferable lesson: tracelessness of $T_{\mu\nu}$ is the *infinitesimal generator* of conformal symmetry, in the same way that $\partial^\mu T_{\mu\nu}$ generates translations. Theories with conformal invariance have traceless stress-energy; theories without it have non-zero trace ("trace anomaly" in the quantum theory).

**Bianchi + Maxwell = conservation: both halves of the Maxwell pair are needed.** The proof that $\partial^\mu T_{\mu\nu}^{\text{EM}} = 0$ uses *both* the inhomogeneous Maxwell equation $\partial^\mu F_{\mu\alpha} = 0$ (which kills one term directly) *and* the Bianchi identity $\partial_{[\mu}F_{\nu\rho]} = 0$ (which is needed to cancel the remaining two terms via a non-trivial algebraic identity). This is a beautiful illustration of how the *pair* (Bianchi, Maxwell) — not either equation alone — is what allows the stress-energy tensor to be conserved. The structural lesson: conservation laws in field theory typically require multiple ingredients to be simultaneously satisfied. For Einstein's equations, $\nabla^\mu G_{\mu\nu} = 0$ follows from the contracted Bianchi identity of the Riemann tensor (an automatic identity), but $\nabla^\mu T_{\mu\nu} = 0$ requires the matter equation of motion. The pattern "automatic identity + dynamical equation = conservation" appears throughout physics, and the EM stress-energy is its first example.
