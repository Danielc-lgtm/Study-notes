---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - The Yang-Mills Action Functional"
  - "Def - The Yang-Mills Lagrangian"
tags: [geometry, gauge-theory, mathematical-physics]
---

# Problem Statement

Show that the **Yang-Mills action** $S_{\text{YM}}[A] = -\tfrac12\int_M\operatorname{tr}(F\wedge\star F)$ on an oriented 4-dimensional Riemannian manifold $(M, g)$ is invariant under **conformal rescalings** of the metric: $g_{\mu\nu} \to \tilde g_{\mu\nu} = e^{2\sigma(x)}g_{\mu\nu}$ for any smooth function $\sigma : M \to \mathbb{R}$.

Specifically:
(a) Compute how the volume form $\operatorname{vol}_g = \sqrt{|g|}\,d^4x$ transforms under conformal rescaling.
(b) Compute how the Hodge star $\star$ acting on 2-forms transforms.
(c) Combine to show $S_{\text{YM}}[A; \tilde g] = S_{\text{YM}}[A; g]$.
(d) Show that this conformal invariance is *special to 4 dimensions*: in $n \neq 4$ dimensions, the YM action scales as $S_{\text{YM}} \to e^{(n-4)\sigma}\cdot S_{\text{YM}}$ (in the constant-$\sigma$ case), with non-trivial scaling.
(e) Discuss the consequence for instantons: scale-invariance of the action allows BPST to have a continuous one-parameter family parameterised by the scale $\rho$, all with the *same* action $S = 8\pi^2$.

**Recall:**

![[Def - The Yang-Mills Action Functional#The Definition]]

A **conformal transformation** is a metric rescaling $g_{\mu\nu} \to e^{2\sigma(x)}g_{\mu\nu}$ that preserves angles (but not lengths). The set of conformal transformations forms a group: composition of conformal rescalings is again a conformal rescaling.

The Hodge star $\star : \Omega^k(M) \to \Omega^{n-k}(M)$ on an $n$-dimensional manifold transforms under conformal rescaling as $\star_{\tilde g} = e^{(n-2k)\sigma}\star_g$ on $k$-forms — i.e., the conformal weight of the Hodge star is $n - 2k$.

---

# Convergent Strategy

**Problem class.** This is a *scaling-analysis* exercise — track how a geometric functional transforms under a metric rescaling, and identify the dimension where the rescaling cancels. The general technique: compute the conformal weights of each ingredient (volume form, inverse metric, Hodge star), sum them, and identify the dimension where the total weight vanishes.

**Assumption pattern.** The single assumption is the conformal rescaling rule $g_{\mu\nu} \to e^{2\sigma}g_{\mu\nu}$. The consequences for derived quantities are:
- Inverse metric: $g^{\mu\nu} \to e^{-2\sigma}g^{\mu\nu}$.
- Metric determinant: $g \to e^{2n\sigma}g$, so $\sqrt{|g|} \to e^{n\sigma}\sqrt{|g|}$.
- Volume form: $\operatorname{vol}_g \to e^{n\sigma}\operatorname{vol}_g$.
- Hodge star on $k$-forms: $\star_g \to e^{(n-2k)\sigma}\star_g$.
- Field strength $F$ (a 2-form): metric-independent.

The total weight of the YM integrand $\operatorname{tr}(F\wedge\star F)$ is $0 + (n - 2\cdot 2) = n - 4$. So $S_{\text{YM}} \to e^{(n-4)\sigma}S_{\text{YM}}$.

**Theorem routing.** No major theorem is needed — the computation is direct scaling analysis. The conclusion follows from the *dimension count* $n - 4 = 0$ iff $n = 4$.

**Key decision point.** The non-obvious point is that *conformal invariance is dimension-specific* — it holds for YM only in 4D, for scalar $\sigma$-models only in 2D, for Einstein gravity only in 2D (where it is trivial), and for Chern–Simons in 3D. This special dimensionality is not a coincidence but a structural feature: it is the unique dimension where the kinetic term of the relevant theory has zero conformal weight. The decision: *make the conformal-weight calculation the central tool*, not the detailed mechanics of any specific transformation. This generalises to any theory.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory V — Hodge Theory, Maxwell, Yang–Mills, and Instantons#Legal Operations|the topic page's Legal Operations]]:

1. **Use the trace pairing on the Lie algebra as an inner product** (operation 5). The Yang-Mills action is built from this pairing combined with the metric and the Hodge star.

2. **Decompose a 2-form on a 4-manifold into self-dual and anti-self-dual parts** (operation 4). Although not used directly in this exercise, the conformal invariance of YM is closely related to the conformal invariance of the SD/ASD decomposition — both reflect the fact that $\star^2 = 1$ on 2-forms in 4D, a dimension-special property.

---

# Hints

> [!note]- Hint 1
> The Yang-Mills integrand $\operatorname{tr}(F\wedge\star F)$ is built from $F$ (a 2-form independent of the metric) and the Hodge star $\star$ (which depends on the metric). The whole integrand is then integrated against $\operatorname{vol}_g = \sqrt{|g|}\,d^4x$. Track the conformal weight of each ingredient.

> [!note]- Hint 2
> $F$ is metric-independent (built from $A$ and $d$, no metric needed). The Hodge star on 2-forms in $n$ dimensions has conformal weight $n - 2\cdot 2 = n - 4$. The volume form has conformal weight $n$. But wait — $\star F$ is a $(n-2)$-form, and the wedge $F\wedge\star F$ is an $n$-form, which when integrated picks up no additional weight from the volume form because $F\wedge\star F$ is *already* an $n$-form.

> [!note]- Hint 3
> Actually, more carefully: the YM action $S_{\text{YM}} = -\tfrac12\int\operatorname{tr}(F\wedge\star F)$ does *not* involve $\sqrt{|g|}\,d^4x$ explicitly — the Hodge star $\star F$ already absorbs the volume form. So the conformal weight of the YM action is the conformal weight of $\star F$, which is $n - 2k = n - 4$. For $n = 4$, this is zero: conformal invariance.

---

# Solution

The strategy is to compute the conformal weight of each factor in the YM action and verify their sum is zero in 4D.

**Step 1: Conformal weight of the volume form.**

$\sqrt{|g|} \to e^{n\sigma}\sqrt{|g|}$, so $\operatorname{vol}_g = \sqrt{|g|}\,d^4x \to e^{n\sigma}\operatorname{vol}_g$.

> [!note]- Derivation
> $g_{\mu\nu} \to e^{2\sigma}g_{\mu\nu}$ rescales the metric tensor by $e^{2\sigma}$. The determinant in $n$ dimensions: $g \to e^{2n\sigma}g$ (each of the $n$ rows scales by $e^{2\sigma}$, giving a total factor of $e^{2n\sigma}$ in the determinant). So $\sqrt{|g|} \to e^{n\sigma}\sqrt{|g|}$, and the volume form $\operatorname{vol}_g \to e^{n\sigma}\operatorname{vol}_g$.

**Step 2: Conformal weight of the Hodge star.**

On $k$-forms in $n$ dimensions, $\star_g \to e^{(n-2k)\sigma}\star_g$.

> [!note]- Derivation
> The Hodge star is defined by $\alpha\wedge\star\beta = \langle\alpha, \beta\rangle\operatorname{vol}_g$ for $k$-forms $\alpha, \beta$, where $\langle, \rangle$ is the metric-induced inner product on $k$-forms. The inner product on $k$-forms involves $k$ factors of $g^{\mu\nu}$ (one for each index), so it scales as $e^{-2k\sigma}$. The volume form scales as $e^{n\sigma}$. So $\alpha\wedge\star\beta \to e^{(n-2k)\sigma}\alpha\wedge\star\beta$, i.e., $\star\beta \to e^{(n-2k)\sigma}\star\beta$.

**Step 3: Combine for the YM action.**

$F$ is metric-independent (conformal weight 0). $\star F$ on 2-forms in 4D has weight $4 - 2\cdot 2 = 0$. The wedge $F\wedge\star F$ is a 4-form, automatically integrable on $M$ (no further $\operatorname{vol}_g$ factor needed). So
$$S_{\text{YM}}[A; \tilde g] = -\tfrac12\int_M\operatorname{tr}(F\wedge\star_{\tilde g}F) = -\tfrac12\int_M\operatorname{tr}(F\wedge e^0\star_g F) = S_{\text{YM}}[A; g].$$

In $n$ dimensions, the weight of $\star_g F$ is $n - 4$, so $S_{\text{YM}}[A; \tilde g] = e^{(n-4)\sigma}S_{\text{YM}}[A; g]$ for constant $\sigma$. Only for $n = 4$ does this give invariance.

> [!note]- Derivation
> $S_{\text{YM}} = -\tfrac12\int_M\operatorname{tr}(F\wedge\star F)$. Under conformal rescaling:
> - $F$ unchanged (no metric in its definition).
> - $\star F$ scales as $e^{(n-2\cdot 2)\sigma} = e^{(n-4)\sigma}$ on a 2-form in $n$ dimensions.
> - The wedge $F\wedge\star F$ is an $n$-form, with the trace $\operatorname{tr}(\cdot)$ being a scalar.
> - Integration over $M$ takes the $n$-form to a number — no additional metric factor.
>
> Hence $S_{\text{YM}}[A; \tilde g] = -\tfrac12\int_M e^{(n-4)\sigma}\operatorname{tr}(F\wedge\star_g F) = e^{(n-4)\sigma}\cdot S_{\text{YM}}[A; g]$ for constant $\sigma$.
>
> For non-constant $\sigma(x)$, the same calculation gives the local statement: the integrand picks up a factor $e^{(n-4)\sigma(x)}$ pointwise. For $n = 4$, this factor is 1 everywhere, so $S_{\text{YM}}$ is invariant under all (not just constant) conformal rescalings. For $n \neq 4$, the integrand acquires a non-trivial $x$-dependence, and the action is not invariant.

**Step 4: Consequence for instantons.**

Conformal invariance of $S_{\text{YM}}$ in 4D implies that **the action of an instanton does not depend on its size**: rescaling $x \to \lambda x$ (a conformal rescaling with constant $\sigma = -\ln\lambda$) leaves $S_{\text{YM}}$ invariant. So the BPST family $A_\rho$ for $\rho > 0$ has the *same* action $S = 8\pi^2$ for all $\rho$.

> [!note]- Derivation
> The BPST connection $A_\rho(x) = (\rho^2/(\rho^2 + r^2))g^{-1}dg$ at scale $\rho$ is related to $A_1(x) = (1/(1+r^2))g^{-1}dg$ at scale 1 by the rescaling $x \to x/\rho$, equivalently $r \to r/\rho$. Under this transformation, $A_\rho(x) = (\rho^2/(\rho^2 + r^2))g^{-1}dg = ((1/(1 + r^2/\rho^2)))g^{-1}dg$, which in the new variable $x' = x/\rho$ becomes $A_1(x')$ — the same connection at unit scale.
>
> The action $S_{\text{YM}}[A_\rho]$ is computed in the original $x$-coordinates: $\int|F|^2(x)\,d^4x$. Under $x = \rho x'$, $d^4x = \rho^4 d^4x'$, and $|F(x)|^2$ (which involves two $g^{\mu\nu}$ factors) scales as $\rho^{-4}|F(x')|^2$. The product $|F|^2 d^4x = \rho^{-4}\cdot\rho^4 |F(x')|^2 d^4x' = |F(x')|^2 d^4x'$ — unchanged! Hence $S_{\text{YM}}[A_\rho] = S_{\text{YM}}[A_1] = 8\pi^2$, independent of $\rho$.
>
> This scale-invariance is *unique to 4D*. In any other dimension, BPST-like solutions would have action depending on $\rho$, and the "scale-zero limit" $\rho \to 0$ would either give zero action or infinite action — neither matching the topological-quantisation $S = 8\pi^2|k|$ of BPS-saturating instantons.

> [!note]- Complete formal solution
> *Conformal rescaling:* $g_{\mu\nu} \to e^{2\sigma(x)}g_{\mu\nu}$. Derived quantities:
> - $g^{\mu\nu} \to e^{-2\sigma}g^{\mu\nu}$.
> - $\operatorname{vol}_g \to e^{n\sigma}\operatorname{vol}_g$.
> - $\star_g$ on $k$-forms $\to e^{(n-2k)\sigma}\star_g$.
>
> *YM action under conformal rescaling:*
> $$S_{\text{YM}}[A; \tilde g] = -\tfrac12\int_M\operatorname{tr}(F\wedge\star_{\tilde g}F) = -\tfrac12\int_M e^{(n-4)\sigma}\operatorname{tr}(F\wedge\star_g F).$$
>
> For $n = 4$: $S_{\text{YM}}[A; \tilde g] = S_{\text{YM}}[A; g]$, conformal invariance.
>
> For $n \neq 4$: scaling by $e^{(n-4)\sigma}$, *not* invariant.
>
> *Consequence:* In 4D, the YM action depends only on the conformal class of the metric, not on the metric itself. BPST instantons of different scales $\rho$ have the same action $S = 8\pi^2$, reflecting the scale-invariance of the underlying flat 4D theory.
>
> *Group of conformal transformations on $\mathbb{R}^4$:* The conformal group of $\mathbb{R}^4$ with the flat metric is $SO(5, 1)$ (the Lorentz group of $\mathbb{R}^{5,1}$), with 15 generators: 4 translations, 6 rotations, 1 dilation, 4 special conformal transformations. The instanton moduli space carries an action of this group, and the BPST family is a single orbit under this action. $\blacksquare$

---

# Key Takeaways

**Conformal invariance is encoded in the conformal weights summing to zero.** The Yang-Mills action's invariance under metric rescalings in 4D is a *dimension-counting* fact: the conformal weight of the YM integrand is $n - 4$, which vanishes only in $n = 4$. The same conformal-weight analysis applies to any field theory: identify the conformal weights of each ingredient, demand their sum vanishes, and the dimension where the sum vanishes is the unique dimension of conformal invariance. For scalar $\sigma$-models $\int|\nabla\phi|^2 d^nx$, the answer is $n = 2$. For Chern–Simons $\int\operatorname{tr}(A\wedge dA + \tfrac23 A\wedge A\wedge A)$, $n = 3$. For YM, $n = 4$. The pattern: *kinetic-energy actions are typically conformally invariant in exactly one specific dimension*, the dimension where the gradient operator scaling matches the volume form scaling.

**Conformal invariance of YM in 4D is what makes instantons possible.** The continuous one-parameter family of BPST instantons parameterised by $\rho$ exists *because* the action is invariant under scaling. If YM were not conformally invariant in 4D, the scale-rescaled BPST connections would have different actions, and the moduli space would be discrete (only specific scales saturating the BPS bound). Conformal invariance *creates* the moduli space. The transferable principle: *whenever a field theory admits a continuous moduli space of solutions, look for a symmetry of the action that acts non-trivially on the moduli space*. For YM the symmetry is conformal; for vortices on $\mathbb{R}^2$, it is also conformal (2D); for monopoles on $\mathbb{R}^3$, it is the scale symmetry of the dimensionless Bogomolny limit; for BPS branes in string theory, it is supersymmetric scale-invariance.

**Conformal invariance is a quantum anomaly to watch out for.** Although classical Yang-Mills in 4D is conformally invariant, the *quantum theory* is not — the regularised quantum action acquires a logarithmic dependence on energy scales (asymptotic freedom in QCD), and the trace of the quantum stress-energy tensor $T^\mu{}_\mu = (\beta(g)/2g)F^a_{\mu\nu}F^{a,\mu\nu}$ is non-zero, where $\beta(g)$ is the renormalisation-group beta function. This is the **trace anomaly** (or **scale anomaly**) of Yang-Mills theory, and is responsible for *dimensional transmutation*: the emergence of an intrinsic mass scale $\Lambda_{\text{QCD}}$ in a theory whose classical Lagrangian contains no mass scale. The transferable lesson: classical conformal invariance does not guarantee quantum conformal invariance; the quantum-anomaly question must be checked separately. In supersymmetric theories the trace anomaly is often constrained by superconformal symmetry, leading to exact conformal field theories in 4D (the $\mathcal{N} = 4$ super-Yang-Mills theory is exactly conformally invariant at the quantum level).
