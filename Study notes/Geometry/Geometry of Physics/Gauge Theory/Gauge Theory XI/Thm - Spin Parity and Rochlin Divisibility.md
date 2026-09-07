---
type: theorem
subject: gauge-theory
prereqs: ["Def - Intersection Form of a Four-Manifold", "Def - Spin and Spin-c Structures"]
tags: [four-manifolds, spin, rochlin]
---

# Prerequisite Concepts

- [[Def - Intersection Form of a Four-Manifold]]
- [[Def - Spin and Spin-c Structures]]

# Statement
> [!theorem] Parity and Rochlin
> For a closed simply connected oriented smooth four-manifold, $Q_X$ is even exactly when $X$ is spin. If it is even, then $\sigma(X)\equiv0\pmod{16}$.

# Proof architecture
Wu's formula gives $x^2\equiv\langle w_2(X),x\rangle\pmod2$. Since simply connectedness removes the relevant torsion ambiguity, evenness is equivalent to $w_2(X)=0$, hence to a spin structure.

For spin $X$, the complex Dirac index is $\operatorname{ind}_{\mathbb C}D^+=-\sigma(X)/8$ by Atiyah–Singer. In dimension four the spin representations carry a quaternionic structure commuting with $D^+$, so kernel and cokernel have even complex dimensions. The index is therefore even, forcing $\sigma(X)/8$ even and hence $16\mid\sigma(X)$.

# Obstruction
The even unimodular form $E_8$ has signature $8$. Freedman's theorem realizes it topologically, but Rochlin forbids any smooth spin manifold with that form.
