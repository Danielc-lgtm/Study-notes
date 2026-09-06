---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Associated Bundle"
  - "Def - Covering Space"
tags: [gauge-theory, associated-bundle, mobius]
---

# Problem Statement

View $p:S^1\to S^1$, $p(z)=z^2$, as a principal $\mathbb Z/2$-bundle. Let the nontrivial element act on $\mathbb R$ by $t\mapsto-t$. Prove that the associated line bundle is the Möbius line bundle. Compare with the trivial representation.

# Solution

> [!proof]- Solution
> Parametrize the total circle by $e^{i\theta}$; its deck transformation is $\theta\mapsto\theta+\pi$. The associated bundle is
> $$
> (S^1\times\mathbb R)/((e^{i\theta},t)\sim(-e^{i\theta},-t)).
> $$
> Choose the interval $0\le\theta\le\pi$ as representatives of base points. The quotient becomes
> $$([0,\pi]\times\mathbb R)/((0,t)\sim(\pi,-t)),$$
> which is the standard Möbius line bundle over a circle. If the action on $\mathbb R$ is trivial, the endpoint relation is $(0,t)\sim(\pi,t)$ and the result is $S^1\times\mathbb R$.
>
> Nontriviality can be seen directly: a nowhere-zero section would lift to a continuous function $f:S^1\to\mathbb R\setminus\{0\}$ satisfying $f(-z)=-f(z)$. Along a semicircle, $f$ changes sign, so the intermediate value theorem forces a zero, a contradiction.

# Key Takeaways

The same principal bundle produces different associated bundles when the representation changes. The topology lies jointly in the principal cocycle and the way $G$ acts on the fibre.
