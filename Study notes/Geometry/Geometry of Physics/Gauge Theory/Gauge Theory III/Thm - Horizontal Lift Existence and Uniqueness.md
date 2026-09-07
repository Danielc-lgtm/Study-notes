---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Horizontal Subspace"
  - "Def - Connection 1-Form on a Principal Bundle"
tags: [gauge-theory, horizontal-lift, ode]
---

# Prerequisite Concepts

- [[Def - Horizontal Subspace]]
- [[Def - Connection 1-Form on a Principal Bundle]]

# Statement

> [!theorem] Horizontal lift
> Let $\gamma:[a,b]\to M$ be piecewise smooth and $p_0\in P_{\gamma(a)}$. There is a unique piecewise-smooth curve $\widetilde\gamma:[a,b]\to P$ such that
> $$\pi\widetilde\gamma=\gamma,\qquad \widetilde\gamma(a)=p_0,\qquad
> \omega(\dot{\widetilde\gamma})=0.$$
> It exists on the whole compact interval and obeys
> $$\widetilde\gamma_{p_0g}(t)=\widetilde\gamma_{p_0}(t)g.$$

# Formal Proof

> [!proof]- Formal Proof
> Work first where $P|_U\cong U\times G$ and write the connection as
> $$\omega_{(x,h)}=\operatorname{Ad}_{h^{-1}}A_x+h^{-1}dh.$$
> A lift has the form $(\gamma(t),h(t))$. Horizontality is equivalent to
> $$h(t)^{-1}\dot h(t)=-\operatorname{Ad}_{h(t)^{-1}}A_{\gamma(t)}(\dot\gamma(t)),$$
> or, for a matrix group, $\dot h=-A(\dot\gamma)h$. This is a smooth time-dependent ODE on $G$, so local existence and uniqueness hold for each initial value.
>
> Cover the compact image of each smooth segment of $\gamma$ by finitely many bundle charts and subdivide $[a,b]$ so that every subpath lies in one chart. Solve successively, using the previous endpoint as initial condition. The local solutions agree on overlapping time intervals by uniqueness, giving a lift on all of $[a,b]$. The same argument handles finitely many piecewise-smooth segments.
>
> Right invariance of $H$ shows that $\widetilde\gamma(t)g$ is horizontal and begins at $p_0g$. Uniqueness therefore gives the equivariance formula.

# Rederivation Scaffold

Choose a gauge. A lift is a base curve plus one unknown group-valued function; horizontality is a first-order ODE for that function.
