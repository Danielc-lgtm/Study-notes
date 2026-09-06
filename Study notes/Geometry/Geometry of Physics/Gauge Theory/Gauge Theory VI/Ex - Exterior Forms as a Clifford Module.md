---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs: ["Def - Clifford Algebra and Clifford Module"]
tags: [gauge-theory, clifford-algebra, differential-forms]
---

# Problem Statement

For $c(v)=\iota_v-v^\flat\wedge$ on $\Lambda^*V^*$, prove the Clifford relation and identify the associated Dirac operator on a Riemannian manifold.

# Solution

> [!solution]- Solution
> The identities $\iota_v^2=(v^\flat\wedge)^2=0$ and
> $\iota_v(v^\flat\wedge\alpha)+v^\flat\wedge\iota_v\alpha=|v|^2\alpha$ give $c(v)^2=-|v|^2$. Polarization gives the full anticommutator. With the Levi–Civita connection,
> $$\sum_j(e^j\wedge-\iota_{e_j})\nabla_{e_j}=d+d^*$$
> for this sign choice, since the alternating part is $d$ and the contraction part is its formal adjoint. Thus the Hodge–de Rham operator is a Dirac operator.

