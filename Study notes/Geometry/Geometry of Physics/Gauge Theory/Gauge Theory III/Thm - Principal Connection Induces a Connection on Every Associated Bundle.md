---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Exterior Covariant Derivative on Associated Bundles"
  - "Def - Associated Bundle"
tags: [gauge-theory, associated-bundle, induced-connection]
---

# Statement

> [!theorem] Induced connection
> A principal connection on $P$ induces, for every representation $\rho:G\to\mathrm{GL}(V)$, a unique connection on $E=P\times_\rho V$ whose local expression is
> $$\nabla=d+\rho_*(A).$$
> Its curvature is $\rho_*(F_A)$, and the construction respects direct sums, tensor products, duals, symmetric powers, and exterior powers.

# Formal Proof

> [!proof]- Formal Proof
> Let $s_\alpha$ be local sections, $A_\alpha=s_\alpha^*\omega$, and write a section of $E$ as coefficient functions $v_\alpha$. On overlaps $s_\beta=s_\alpha g_{\alpha\beta}$ and
> $$v_\beta=\rho(g_{\alpha\beta}^{-1})v_\alpha.$$
> The gauge-covariance calculation on [[Def - Exterior Covariant Derivative on Associated Bundles]] gives
> $$
> (d+\rho_*A_\beta)v_\beta
> =\rho(g_{\alpha\beta}^{-1})(d+\rho_*A_\alpha)v_\alpha.
> $$
> This is exactly the overlap law for an $E$-valued $1$-form, so the local expressions glue to a global operator $\nabla$. Each local expression is linear and satisfies
> $$\nabla(fv)=df\otimes v+f\nabla v,$$
> hence it is a connection. Any connection with the stated local expressions agrees on a cover, proving uniqueness.
>
> Squaring locally gives $\nabla^2=\rho_*(F_A)$, and gauge covariance makes this global. The derived representations on sums, tensors, and duals obey the corresponding algebraic Leibniz rules; inserting them into $d+\rho_*A$ proves compatibility with those operations.

# Rederivation Scaffold

Associated-section coefficients transform by $\rho(g^{-1})$. Differentiate that expression; the derivative of $g$ is precisely cancelled by the $g^{-1}dg$ term in the transformed potential.
