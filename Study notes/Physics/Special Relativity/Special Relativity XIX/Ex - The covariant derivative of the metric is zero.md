---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Covariant Derivative"
  - "Def - Christoffel Symbols"
tags: [physics, special-relativity]
---

# Problem Statement

Show that the covariant derivative of the metric tensor vanishes, $\boldsymbol{\nabla}g = 0$, i.e. $\nabla_\gamma g_{\alpha\beta} = 0$, in two complementary ways.

1. **Conceptually.** Argue in one sentence that $\boldsymbol{\nabla}g = 0$ on flat spacetime because $g$ is a *constant tensor field*.
2. **By direct computation.** Write out $\nabla_\gamma g_{\alpha\beta}$ using the lower-index covariant-derivative rule and the Christoffel symbols, and show that it vanishes — first abstractly (using the Christoffel formula), then explicitly in spherical coordinates for the component $\nabla_r g_{\theta\theta}$.
3. Deduce that the covariant derivative commutes with raising and lowering indices, $\nabla_\mu v_\alpha = g_{\alpha\beta}\nabla_\mu v^\beta$.
4. Explain why this same equation $\boldsymbol{\nabla}g = 0$ is *trivial* here but becomes the *defining condition* of the connection in general relativity.

**Recall:**

![[Def - The Covariant Derivative#The Definition]]

The covariant derivative of a type $(0,2)$ tensor is $\nabla_\gamma T_{\alpha\beta} = \partial_\gamma T_{\alpha\beta} - \Gamma^\mu{}_{\alpha\gamma}T_{\mu\beta} - \Gamma^\mu{}_{\beta\gamma}T_{\alpha\mu}$. The Christoffel symbols are $\Gamma^\gamma{}_{\alpha\beta} = \tfrac12 g^{\gamma\mu}(\partial_\alpha g_{\mu\beta}+\partial_\beta g_{\alpha\mu}-\partial_\mu g_{\alpha\beta})$ (see [[Special Relativity XIX/Def - Christoffel Symbols|Def - Christoffel Symbols]]).

---

# Convergent Strategy

**Problem class.** A *verify-a-tensor-identity* problem, and the canonical calibration of metric compatibility. There are two routes — a conceptual one (constant tensor) and a computational one (plug in the Christoffels) — and the exercise demands both because each illuminates the other.

**Assumption pattern.** Conceptually: the flat metric is the same bilinear form at every event, hence a constant tensor field. Computationally: the Christoffel symbols are *built from* the metric derivatives, so substituting them into $\nabla_\gamma g_{\alpha\beta}$ is bound to cancel.

**Theorem routing.** Part 1 uses the definition of the covariant derivative of a constant field. Part 2 routes through the lower-index rule and the Christoffel formula of [[Special Relativity XIX/Def - Christoffel Symbols|Def - Christoffel Symbols]]. Part 3 uses the Leibniz rule. Part 4 is conceptual, contrasting flat and curved.

**Key decision point.** The computational crux is recognising that $\nabla_\gamma g_{\alpha\beta} = \partial_\gamma g_{\alpha\beta} - \Gamma^\mu{}_{\alpha\gamma}g_{\mu\beta} - \Gamma^\mu{}_{\beta\gamma}g_{\alpha\mu}$ is *exactly* the relation the Christoffel formula was constructed to satisfy — the two $\Gamma g$ terms reassemble $\partial_\gamma g_{\alpha\beta}$. Seeing this is the whole point; brute-forcing it in components also works but obscures why it had to vanish.

---

# Legal Operations Used

1. **Covariantly differentiate a tensor** (operation 3 from the topic page). Apply the lower-index rule to $g_{\alpha\beta}$.
2. **Use $\boldsymbol{\nabla}g = 0$ to commute the metric past the derivative** (operation 4 from the topic page). Once established, deduce that index-raising commutes with $\boldsymbol{\nabla}$.

---

# Hints

> [!note]- Hint 1
> The metric $g$ is a fixed type $(0,2)$ tensor — the same bilinear form at every event of flat spacetime. The covariant derivative measures the *variation* of a tensor field; a field that does not vary has zero variation.

> [!note]- Hint 2
> Write $\nabla_\gamma g_{\alpha\beta} = \partial_\gamma g_{\alpha\beta} - \Gamma^\mu{}_{\alpha\gamma}g_{\mu\beta} - \Gamma^\mu{}_{\beta\gamma}g_{\alpha\mu}$. Now substitute the Christoffel formula. The combination $\Gamma^\mu{}_{\alpha\gamma}g_{\mu\beta} + \Gamma^\mu{}_{\beta\gamma}g_{\alpha\mu}$ should reassemble into $\partial_\gamma g_{\alpha\beta}$.

> [!note]- Hint 3
> $\Gamma^\mu{}_{\alpha\gamma}g_{\mu\beta} = \tfrac12 g^{\mu\nu}g_{\mu\beta}(\partial_\alpha g_{\nu\gamma}+\partial_\gamma g_{\alpha\nu}-\partial_\nu g_{\alpha\gamma}) = \tfrac12\delta^\nu_\beta(\partial_\alpha g_{\nu\gamma}+\partial_\gamma g_{\alpha\nu}-\partial_\nu g_{\alpha\gamma}) = \tfrac12(\partial_\alpha g_{\beta\gamma}+\partial_\gamma g_{\alpha\beta}-\partial_\beta g_{\alpha\gamma})$. Add the $\beta$-version and watch the cross terms cancel, leaving $\partial_\gamma g_{\alpha\beta}$.

> [!note]- Hint 4
> For the spherical check, take $\nabla_r g_{\theta\theta} = \partial_r g_{\theta\theta} - 2\Gamma^\mu{}_{\theta r}g_{\mu\theta}$. With $\partial_r g_{\theta\theta} = -2r$, $\Gamma^\theta{}_{\theta r} = 1/r$, $g_{\theta\theta} = -r^2$: $-2r - 2(1/r)(-r^2) = -2r + 2r = 0$.

---

# Solution

The plan: Part 1 gives the one-sentence conceptual argument. Part 2 proves $\nabla_\gamma g_{\alpha\beta} = 0$ abstractly by substituting the Christoffel formula and watching the terms reassemble, then checks one component in spherical coordinates. Part 3 deduces index-commutation; Part 4 contrasts with general relativity.

**Step 1: Conceptual argument — $g$ is a constant tensor.**

> [!note]- Derivation
> The Minkowski metric $g$ is a *single* symmetric bilinear form, the same at every event of flat spacetime; as a tensor field it is constant. The covariant derivative $\boldsymbol{\nabla}g$ measures the first-order variation of $g$ between neighbouring events (it is defined by $\mathrm{d}g = \boldsymbol{\nabla}_{\mathrm{d}\vec{x}}g$). A constant field has zero variation, so
> $$\boldsymbol{\nabla}g = 0, \qquad \nabla_\gamma g_{\alpha\beta} = 0.$$
> (This is unambiguous despite the components $g_{\alpha\beta}(M)$ varying in curvilinear coordinates: the *tensor* is constant; only its *components in a position-dependent basis* vary, and the covariant derivative is precisely the derivative that sees through that and reports zero.)

**Step 2: Direct computation.**

> [!note]- Derivation
> *Abstract.* By the lower-index rule,
> $$\nabla_\gamma g_{\alpha\beta} = \partial_\gamma g_{\alpha\beta} - \Gamma^\mu{}_{\alpha\gamma}g_{\mu\beta} - \Gamma^\mu{}_{\beta\gamma}g_{\alpha\mu}.$$
> Compute the first $\Gamma g$ term using $\Gamma^\mu{}_{\alpha\gamma} = \tfrac12 g^{\mu\nu}(\partial_\alpha g_{\nu\gamma}+\partial_\gamma g_{\alpha\nu}-\partial_\nu g_{\alpha\gamma})$ and $g^{\mu\nu}g_{\mu\beta} = \delta^\nu_\beta$:
> $$\Gamma^\mu{}_{\alpha\gamma}g_{\mu\beta} = \tfrac12\big(\partial_\alpha g_{\beta\gamma}+\partial_\gamma g_{\alpha\beta}-\partial_\beta g_{\alpha\gamma}\big).$$
> By the symmetric computation (swap $\alpha\leftrightarrow\beta$),
> $$\Gamma^\mu{}_{\beta\gamma}g_{\alpha\mu} = \tfrac12\big(\partial_\beta g_{\alpha\gamma}+\partial_\gamma g_{\alpha\beta}-\partial_\alpha g_{\beta\gamma}\big).$$
> Add them: the $\pm\partial_\alpha g_{\beta\gamma}$ cancel, the $\mp\partial_\beta g_{\alpha\gamma}$ cancel, and the two $\tfrac12\partial_\gamma g_{\alpha\beta}$ add to $\partial_\gamma g_{\alpha\beta}$. Hence
> $$\Gamma^\mu{}_{\alpha\gamma}g_{\mu\beta} + \Gamma^\mu{}_{\beta\gamma}g_{\alpha\mu} = \partial_\gamma g_{\alpha\beta},$$
> and therefore $\nabla_\gamma g_{\alpha\beta} = \partial_\gamma g_{\alpha\beta} - \partial_\gamma g_{\alpha\beta} = 0$. The two connection terms reassemble exactly the partial derivative they were subtracted from — which is no accident, since the Christoffel formula was *derived* by solving $\nabla_\gamma g_{\alpha\beta} = 0$.
>
> *Spherical check.* Take $\alpha=\beta=\theta$, $\gamma=r$. Only $\mu=\theta$ contributes (diagonal metric):
> $$\nabla_r g_{\theta\theta} = \partial_r g_{\theta\theta} - 2\,\Gamma^\theta{}_{\theta r}\,g_{\theta\theta} = (-2r) - 2\Big(\tfrac1r\Big)(-r^2) = -2r + 2r = 0. \checkmark$$

**Step 3: Index-raising commutes with $\boldsymbol{\nabla}$.**

> [!note]- Derivation
> Lower an index with the metric, $v_\alpha = g_{\alpha\beta}v^\beta$, and covariantly differentiate using the Leibniz rule:
> $$\nabla_\mu v_\alpha = \nabla_\mu(g_{\alpha\beta}v^\beta) = (\nabla_\mu g_{\alpha\beta})v^\beta + g_{\alpha\beta}\nabla_\mu v^\beta = 0 + g_{\alpha\beta}\nabla_\mu v^\beta = g_{\alpha\beta}\nabla_\mu v^\beta,$$
> using $\nabla_\mu g_{\alpha\beta} = 0$. So the covariant derivative of the lowered vector is the lowered covariant derivative: one may freely move the metric in and out of $\boldsymbol{\nabla}$, and raising or lowering an index commutes with covariant differentiation. The same holds for $g^{\alpha\beta}$ (since $\nabla_\mu g^{\alpha\beta} = 0$ too, from $\nabla_\mu(g^{\alpha\nu}g_{\nu\beta}) = \nabla_\mu\delta^\alpha_\beta = 0$).

**Step 4: Trivial here, defining there.**

> [!note]- Derivation
> On flat spacetime $\boldsymbol{\nabla}g = 0$ is *trivial*: $g$ is literally a constant bilinear form, so its constancy is given, and the equation says nothing one did not already know. But in general relativity the metric $g_{\mu\nu}(x)$ is a genuine, position-dependent dynamical field — there is no sense in which it is "constant" — and there the requirement $\boldsymbol{\nabla}g = 0$ becomes a substantive *condition* that, together with torsion-freeness, *determines* the connection from the metric (it is exactly the equation solved to obtain the Christoffel formula). So the same equation plays two roles: here it is a consequence of flatness, providing the calibration check that the covariant derivative is doing its job; there it is the postulate (metric compatibility) that defines the Levi-Civita connection and hence the gravitational field. Recognising this is recognising that the apparatus is identical and only the status of the metric changes.

> [!note]- Complete formal solution
> *Conceptual:* the flat metric is a constant tensor field, and the covariant derivative of a constant field is zero, so $\boldsymbol{\nabla}g = 0$. *Computational:* $\nabla_\gamma g_{\alpha\beta} = \partial_\gamma g_{\alpha\beta} - \Gamma^\mu{}_{\alpha\gamma}g_{\mu\beta} - \Gamma^\mu{}_{\beta\gamma}g_{\alpha\mu}$; substituting the Christoffel formula gives $\Gamma^\mu{}_{\alpha\gamma}g_{\mu\beta} = \tfrac12(\partial_\alpha g_{\beta\gamma}+\partial_\gamma g_{\alpha\beta}-\partial_\beta g_{\alpha\gamma})$ and its $\alpha\leftrightarrow\beta$ partner, whose sum is $\partial_\gamma g_{\alpha\beta}$, so $\nabla_\gamma g_{\alpha\beta} = 0$. In spherical coordinates $\nabla_r g_{\theta\theta} = -2r - 2(1/r)(-r^2) = 0$. From $\nabla_\mu g_{\alpha\beta} = 0$ and Leibniz, $\nabla_\mu v_\alpha = g_{\alpha\beta}\nabla_\mu v^\beta$, so index-raising commutes with $\boldsymbol{\nabla}$. The equation is trivial here (constant metric) but is the defining metric-compatibility condition of the Levi-Civita connection in general relativity (position-dependent metric). $\blacksquare$

---

# Key Takeaways

**Metric compatibility $\boldsymbol{\nabla}g = 0$ is what lets you move indices through the covariant derivative — the single most-used consequence.** The practical payoff of $\boldsymbol{\nabla}g = 0$ is not the identity itself but its corollary: raising and lowering indices commutes with covariant differentiation, so $\nabla_\mu v_\alpha = g_{\alpha\beta}\nabla_\mu v^\beta$ and you may treat $\nabla_\mu v^\alpha$ and $\nabla_\mu v_\alpha$ as the same operation up to an index move. This is used constantly: it is why $\nabla_\mu(v^\alpha w_\alpha) = (\nabla_\mu v^\alpha)w_\alpha + v^\alpha\nabla_\mu w_\alpha$ behaves like an ordinary product rule, why the divergence of $T^{\mu\nu}$ and of $T_{\mu}{}^{\nu}$ are related by lowering an index, and why one can raise the index on the wave operator at will. The trigger to reach for it is any covariant derivative in which an index needs raising or lowering; the metric simply passes through.

**The reassembly of the two $\Gamma g$ terms into $\partial g$ is not luck — the Christoffel formula was built to make $\boldsymbol{\nabla}g$ vanish.** When you substitute the Christoffel symbols into $\nabla_\gamma g_{\alpha\beta}$ and the connection terms exactly reconstruct the partial derivative they were subtracted from, it can look like a small miracle; it is in fact the formula working backwards. The Christoffel formula $\Gamma = \tfrac12 g^{-1}(\partial g + \partial g - \partial g)$ was *derived* by imposing $\nabla_\gamma g_{\alpha\beta} = 0$ and solving the resulting system with the cyclic-permutation trick. So $\boldsymbol{\nabla}g = 0$ and the Christoffel formula are logically equivalent — each implies the other — and verifying one is verifying the other. The transferable insight is that metric compatibility is not an extra fact layered on top of the connection; it is the very condition that defines the connection, which is why on a curved spacetime $\boldsymbol{\nabla}g = 0$ is the equation you solve to find the Christoffel symbols.

**A constant tensor can have non-constant components, and the covariant derivative is the tool that tells the difference.** The deepest takeaway is that "the components $g_{\alpha\beta}(M)$ vary with position" and "the tensor $g$ is constant" are perfectly compatible statements, because the variation of the components is entirely due to the position-dependence of the basis, not of the tensor. The partial derivative $\partial_\gamma g_{\alpha\beta} = -2r \neq 0$ sees only the components and wrongly suggests $g$ changes; the covariant derivative adds the connection terms that account for the turning basis and correctly reports $\nabla_\gamma g_{\alpha\beta} = 0$. This is the same lesson as $\boldsymbol{\nabla}\vec{e}_r \neq 0$ for a constant-component field, run in reverse: there, constant components hid a changing field; here, changing components hide a constant field. In both cases the covariant derivative is the only derivative that gives the geometrically correct answer, and this exercise is the cleanest demonstration of why the chapter needs it.
