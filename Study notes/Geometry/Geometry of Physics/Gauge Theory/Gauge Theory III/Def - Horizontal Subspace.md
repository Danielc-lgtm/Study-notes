---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Fundamental Vector Field of a Principal Bundle"
tags: [gauge-theory, principal-connection, horizontal-distribution]
---

# Prerequisite Concepts

- [[Def - Fundamental Vector Field of a Principal Bundle]]

# The Definition

> [!definition] Horizontal distribution
> A **principal horizontal distribution** on $P\to M$ is a smooth subbundle $H\subset TP$ such that
> $$T_pP=H_p\oplus V_pP,\qquad (dR_g)_pH_p=H_{pg}.$$
> A vector in $H_p$ is horizontal.

Since $d\pi_p$ has kernel $V_pP$, its restriction
$$d\pi_p|_{H_p}:H_p\xrightarrow{\sim}T_{\pi(p)}M$$
is an isomorphism. Thus every base vector $X\in T_xM$ has a unique horizontal lift $X_p^H\in H_p$ at each $p\in P_x$.

# Axiom Motivation

Vertical directions merely change the point inside one gauge fibre. A horizontal complement declares which infinitesimal motions represent genuine motion in the base without an additional gauge rotation. Right equivariance makes that declaration independent of the chosen point in the torsor.

# Curvature as Nonintegrability

If horizontal vector fields $X^H,Y^H$ are lifted from the base, their bracket need not be horizontal. Its vertical component is
$$([X^H,Y^H])^V=-\bigl(\Omega(X^H,Y^H)\bigr)_P.$$
Thus curvature is precisely the obstruction to Frobenius integrability of $H$.

# Unlocked by This

Integrating the distribution along a base curve gives [[Thm - Horizontal Lift Existence and Uniqueness|horizontal lifts]] and parallel transport.
