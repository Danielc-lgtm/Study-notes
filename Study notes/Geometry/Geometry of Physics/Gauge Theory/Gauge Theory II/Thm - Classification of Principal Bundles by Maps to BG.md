---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Universal Bundle and Classifying Space"
  - "Def - Principal G-Bundle"
tags: [gauge-theory, classifying-spaces, classification]
---

# Statement

> [!theorem] Classification theorem
> Let $G$ be a Lie group and $B$ a paracompact Hausdorff space having the homotopy type of a CW complex. Pullback of a universal bundle induces a natural bijection
> $$
> [B,BG]\xrightarrow{\sim}\operatorname{Prin}_G(B),
> \qquad [f]\longmapsto[f^*EG],
> $$
> where the right side denotes isomorphism classes of numerable principal $G$-bundles. Every principal bundle over a smooth manifold is numerable.

# Motivation

Transition functions classify locally but depend on a cover and local sections. A classifying map compresses all that data into one homotopy class. Characteristic classes then arise by pulling universal cohomology classes back from $BG$.

# Lemma Decomposition

> [!note]- Lemma 1 — A numerable bundle admits a $G$-equivariant map to $EG$
> Use a countable locally finite trivializing cover $(U_i)$, a subordinate partition $(\lambda_i)$, and local sections $s_i$. Write $p=s_i(\pi p)g_i(p)$ on $U_i$. In Milnor's infinite-join model
> $$EG=G*G*\cdots,$$
> define $\Phi(p)$ to have barycentric coordinates $\lambda_i(\pi p)$ and $i$th group coordinate $g_i(p)$. Coordinates with zero weight are ignored. Then $\Phi(pg)=\Phi(p)g$.

> [!note]- Lemma 2 — Equivariant maps classify pullbacks
> A $G$-equivariant map $\Phi:P\to EG$ descends to $f:B\to BG$ and the map $p\mapsto(\pi(p),\Phi(p))$ is a principal-bundle isomorphism $P\cong f^*EG$.

> [!note]- Lemma 3 — Any two equivariant maps $P\to EG$ are equivariantly homotopic
> The join model permits disjoint-coordinate interpolation: place the coordinates of the first map in even slots and those of the second in odd slots, then linearly transfer barycentric weights. This stays in the join, is continuous, and respects the diagonal right action.

# Formal Proof

> [!proof]- Formal Proof
> A locally trivial principal bundle on a paracompact base admits a locally finite trivializing refinement and subordinate partition of unity, hence is numerable. Lemma 1 constructs a $G$-equivariant $\Phi:P\to EG$. It descends to $f:B=P/G\to EG/G=BG$. By Lemma 2, $P\cong f^*EG$, proving surjectivity.
>
> If $f_0$ and $f_1$ are homotopic through $H:B\times I\to BG$, then
> $H^*EG\to B\times I$ restricts to $f_i^*EG$ at the endpoints. A numerable bundle over $B\times I$ has isomorphic endpoint restrictions: trivialize successively over a locally finite cover and use the contractibility of $I$ to transport the cocycle; equivalently apply homotopy invariance of pullback bundles. Thus the construction depends only on $[f]$.
>
> Conversely suppose $f_0^*EG\cong f_1^*EG=P$. The canonical equivariant maps from these pullbacks to $EG$, transported to $P$, are equivariantly homotopic by Lemma 3. Passing to orbit spaces gives a homotopy $f_0\simeq f_1$. Hence the map is injective.
>
> Naturality follows from $(f\circ h)^*EG\cong h^*(f^*EG)$.

# Rederivation Scaffold

A numerable cover and partition of unity turn transition data into barycentric coordinates in $EG$. Contractibility makes the resulting equivariant map unique up to equivariant homotopy. Existence and uniqueness are exactly surjectivity and injectivity of the classification map.

# Examples / Corollaries

For $G=U(1)$ this gives line bundles $\leftrightarrow H^2(B;\mathbb Z)$. For $G=SU(2)$ and a closed four-dimensional CW complex, it gives $SU(2)$ bundles $\leftrightarrow H^4(B;\mathbb Z)$, with the integer represented by the second Chern class after fixing its generator.
