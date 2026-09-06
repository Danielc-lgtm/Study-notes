---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Connection on a Vector Bundle"
  - "Def - Gauge Transformation"
tags: [gauge-theory, holonomy, wilson-line]
---

# Notation

Let $\gamma:[0,1]\to M$ be piecewise smooth and let $\nabla=d+A$ in a frame along $\gamma$. Parallel transport $U_\gamma(t)$ is normalized by $U_\gamma(0)=I$.

# The Definition

> [!definition] Wilson transport and holonomy
> Parallel transport is the solution of
> $$
> \frac{dU_\gamma}{dt}=-A_{\gamma(t)}(\dot\gamma(t))U_\gamma(t),
> \qquad U_\gamma(0)=I.
> $$
> Its endpoint is the **Wilson line**
> $$U_\gamma=\mathcal P\exp\!\left(-\int_\gamma A\right):E_{\gamma(0)}\to E_{\gamma(1)}.$$
> If $\gamma$ is a loop based at $x$, $U_\gamma\in\mathrm{GL}(E_x)$ is its **holonomy**.

The path-ordering symbol $\mathcal P$ is required when matrices $A(\dot\gamma(t))$ at different times fail to commute. For a $U(1)$ connection $d+iqA$,
$$
U_\gamma=\exp\!\left(-iq\int_\gamma A\right).
$$

# Gauge Behaviour

Under an active gauge transformation $g$, transport changes by endpoint conjugation:
$$
U_\gamma^{,g}=g(\gamma(1))U_\gamma g(\gamma(0))^{-1}.
$$
For a closed loop this is conjugation, so $\operatorname{tr}U_\gamma$ is gauge invariant. In $U(1)$, conjugation is trivial and the holonomy itself is invariant.

# Examples / Corollaries

If $F=0$, transport is invariant under endpoint-fixed homotopies of paths. It need not depend only on endpoints: a flat connection defines a representation $\pi_1(M,x)\to G$. On a simply connected region every flat connection is gauge-equivalent to the trivial one.

When $U(1)$ curvature is exact on a surface $\Sigma$ with $\partial\Sigma=\gamma$, Stokes gives
$$U_\gamma=\exp\!\left(-iq\int_\Sigma F\right).$$
This formula requires a compatible trivialization over $\Sigma$; the holonomy definition does not.

# Unlocked by This

The Aharonov–Bohm effect detects flat holonomy, while Chern–Simons theory studies functionals whose critical points are flat connections.
