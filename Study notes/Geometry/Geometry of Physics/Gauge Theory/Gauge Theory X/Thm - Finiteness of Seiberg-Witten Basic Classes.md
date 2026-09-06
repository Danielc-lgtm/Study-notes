---
type: theorem
subject: gauge-theory
prereqs: ["Def - Seiberg-Witten Invariant", "Thm - Compactness and Smoothness of the Seiberg-Witten Moduli Space"]
tags: [gauge-theory, seiberg-witten, basic-class]
---

# Statement

> [!theorem] Finiteness
> On a fixed closed oriented Riemannian four-manifold, only finitely many spin-c structures have nonzero Seiberg–Witten invariant.

# Proof architecture

Nonvanishing forces a nonempty moduli space and hence nonnegative expected dimension. The curvature estimate bounds the norm of $c_1(L)$, and a lattice contains only finitely many points in a bounded set.

> [!proof]- Formal Proof
> If $\operatorname{SW}_X(\mathfrak s)\ne0$, then $\mathcal M_\eta(\mathfrak s)$ is nonempty and $d(\mathfrak s)\ge0$. The perturbed compactness estimate bounds $\|F_A\|_{L^2}$ by a constant depending only on the fixed metric and perturbation bound, not on the solution. Chern–Weil theory identifies
> $$c_1(L)=\left[\frac{F_A}{2\pi i}\right],$$
> so harmonic projection and the $L^2$ estimate bound the norm of $c_1(L)$ in $H^2(X;\mathbb R)$. Integral cohomology modulo torsion is a lattice in this finite-dimensional space and therefore meets a bounded set in finitely many points. The torsion subgroup of $H^2(X;\mathbb Z)$ is finite. Finally, spin-c structures with fixed determinant Chern class form a torsor for a subgroup of the finite torsion group, so only finitely many such $\mathfrak s$ occur. Hence only finitely many invariants can be nonzero.

# Terminology

A class $c_1(L)$ arising from a spin-c structure with nonzero invariant is called a **Seiberg–Witten basic class**.
