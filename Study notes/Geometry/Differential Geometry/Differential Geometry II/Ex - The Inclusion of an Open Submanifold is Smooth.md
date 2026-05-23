---
type: exercise
subject: differential-geometry
difficulty: "⭐"
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
  - "Def - Diffeomorphism"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $M$ be a smooth manifold and let $U \subseteq M$ be an open subset. The set $U$ inherits a smooth manifold structure from $M$: its charts are the restrictions of the charts on $M$ to $U$ (intersected with the chart domains).

Show that the inclusion map $\iota : U \hookrightarrow M$, $\iota(p) = p$, is a smooth map. Show further that $\iota$ is a diffeomorphism onto its image — i.e., the open submanifold $U$ is diffeomorphic to the open subset $U$ of $M$ (which is itself, of course, but understood with the inherited smooth structure).

**Recall:**

A smooth map is defined by:

![[Def - Smooth Map between Manifolds#The Definition]]

A diffeomorphism is:

![[Def - Diffeomorphism#The Definition]]

The inherited smooth structure on an open submanifold $U \subseteq M$: if $(W, \varphi)$ is a smooth chart on $M$ with $W \cap U \neq \emptyset$, then $(W \cap U, \varphi|_{W \cap U})$ is a smooth chart on $U$. The collection of all such restricted charts is a smooth atlas on $U$.

---

# Convergent Strategy

**Problem class:** Verification of smoothness, plus checking that a smooth bijection is a diffeomorphism. The two together test the most basic structural property of open submanifolds: the inclusion is not just continuous (which is obvious from the open-[[Def - Subspace|subspace]] topology) but smooth, and the restriction is moreover a diffeomorphism in the strong sense.

**Assumption pattern:** $U \subseteq M$ is open. $U$ carries the smooth structure inherited from $M$. The smoothness of $\iota$ is then almost tautological — but the *almost* requires us to verify the chart-by-chart condition explicitly.

**Theorem routing:** Pick a chart on $M$ containing the image, restrict to $U$ to get a chart on $U$ for the source. The coordinate representation of $\iota$ is the identity on the chart's image — manifestly smooth. For the diffeomorphism part, $\iota$ is a bijection onto its image $U \subseteq M$; we need to verify the inverse $\iota^{-1} : \iota(U) = U \to U$ is also smooth. But $\iota^{-1}$ is again the identity (in the appropriate sense), and the same argument gives smoothness.

**Key decision point:** The non-obvious point — small but easily missed — is what "smooth" means for the *inverse* $\iota^{-1}$. The inclusion's image is $U$ (as a subset of $M$); the inverse takes $U$ (as a subset of $M$) back to $U$ (the smooth submanifold). The two copies of $U$ are *the same set* but with different roles (codomain of $\iota$, vs the smooth manifold). The smoothness of $\iota^{-1}$ amounts to saying that the smooth structure on $U$ inherited from $M$ is *compatible* with the smooth structure $U$ has as an open submanifold — but these are the same structure by definition. So $\iota^{-1}$ is smooth in any reasonable interpretation.

---

# Legal Operations Used

1. **Pull back to charts to check smoothness (operation 1 from the topic page).** We verify smoothness of $\iota$ by writing its coordinate representation and recognizing it as smooth in Euclidean coordinates.

2. **Use chart containment $F(U) \subseteq V$ (operation 2 from the topic page).** Since $\iota(U) = U \subseteq M$, every chart on $U$ has its image (under $\iota$) inside the same chart on $M$ — by construction.

3. **Verify a diffeomorphism by exhibiting smooth maps both ways (operation 8 from the topic page).** $\iota$ and its inverse (the "restriction" map) are both smooth.

---

# Hints

> [!note]- Hint 1
> The smoothness of $\iota$ is almost tautological. Pick a chart $(W, \varphi)$ on $M$ with $W \cap U \neq \emptyset$. By the inherited smooth structure, $(W \cap U, \varphi|_{W \cap U})$ is a chart on $U$. The coordinate representation of $\iota$ in the chart pair $((W \cap U, \varphi|_{W \cap U}), (W, \varphi))$ is $\varphi \circ \iota \circ (\varphi|_{W \cap U})^{-1}$ — what is this composition?

> [!note]- Hint 2
> The composition $\varphi \circ \iota \circ (\varphi|_{W \cap U})^{-1}$ sends $y \in \varphi(W \cap U) \subseteq \varphi(W)$ to $\varphi(\iota((\varphi|_{W \cap U})^{-1}(y))) = \varphi((\varphi|_{W \cap U})^{-1}(y)) = y$. So it is the identity map on $\varphi(W \cap U) \subseteq \mathbb{R}^m$ — manifestly smooth.

> [!note]- Hint 3
> For the diffeomorphism claim, $\iota : U \to U \subseteq M$ is a bijection onto its image $U$. The inverse $\iota^{-1} : U \to U$ takes a point of $U$ (as a subset of $M$) back to the same point (as an element of the smooth manifold $U$). This is again the identity on charts, hence smooth.

---

# Solution

The proof is a one-paragraph verification. The coordinate representation of $\iota$ in any chart pair built from the inherited smooth structure is the identity, hence smooth. The inverse is also the identity, smooth by the same reason.

**Step 1: $\iota$ is smooth.**

Let $p \in U$. Pick a smooth chart $(W, \varphi)$ on $M$ with $p \in W$ (exists by the smooth structure on $M$). Then $W \cap U$ is open in $U$ (it is the intersection of two open sets) and $p \in W \cap U$. The restricted chart $(W \cap U, \varphi|_{W \cap U})$ is a smooth chart on $U$ by the inherited smooth structure.

The coordinate representation of $\iota$ in the chart pair $((W \cap U, \varphi|_{W \cap U}), (W, \varphi))$ is the map
$$\widehat \iota : \varphi(W \cap U) \to \varphi(W), \quad \widehat \iota(y) = (\varphi \circ \iota \circ (\varphi|_{W \cap U})^{-1})(y).$$

Computing: $(\varphi|_{W \cap U})^{-1}(y)$ is the point $q \in W \cap U$ with $\varphi(q) = y$. Then $\iota(q) = q \in W$, and $\varphi(\iota(q)) = \varphi(q) = y$. So $\widehat \iota(y) = y$ — the identity map on $\varphi(W \cap U) \subseteq \mathbb{R}^m$.

The identity map is smooth in the Euclidean sense (its partial derivatives are constant: $\partial y^i / \partial y^j = \delta^i_j$, smooth).

The chart-containment $\iota(W \cap U) \subseteq W$ holds because $\iota(q) = q \in W \cap U \subseteq W$.

So the chart pair $((W \cap U, \varphi|_{W \cap U}), (W, \varphi))$ witnesses the smoothness of $\iota$ at $p$. Since $p$ was arbitrary, $\iota$ is smooth.

> [!note]- Derivation
> Each verification:
>
> - $W \cap U$ open in $U$: $W$ is open in $M$, $U$ is open in $M$, so $W \cap U$ is open in $M$, hence open in the open submanifold $U$ (since $U$ has the [[Def - Subspace|subspace]] topology and $W \cap U \subseteq U$).
> - $(W \cap U, \varphi|_{W \cap U})$ is a smooth chart on $U$: the restriction of a smooth chart on $M$ to an open subset of $M$ contained in the chart's domain is a smooth chart on the open submanifold. The image of the restriction is $\varphi(W \cap U) \subseteq \mathbb{R}^m$, an open subset.
> - $\widehat \iota$ is the identity: direct computation as above.
> - The identity map on a Euclidean open set is smooth: trivial.
> - Chart containment: $\iota$ maps $W \cap U \subseteq M$ to itself (since $\iota$ is inclusion), and $W \cap U \subseteq W$.

**Step 2: $\iota$ is a diffeomorphism onto its image $U \subseteq M$.**

$\iota$ is a bijection $U \to U$ (where the target $U$ is viewed as a subset of $M$). The inverse $\iota^{-1} : U \to U$ (target $U$ now as the smooth submanifold) is the identity-as-a-map: takes a point of $U$ (sitting in $M$) to the same point of $U$ (sitting in the submanifold).

The smoothness of $\iota^{-1}$ is verified analogously: in any chart pair $((W, \varphi), (W \cap U, \varphi|_{W \cap U}))$ with $p \in W \cap U$, the coordinate representation of $\iota^{-1}$ is $\varphi|_{W \cap U} \circ \iota^{-1} \circ \varphi^{-1}|_{\varphi(W \cap U)}$, which by direct computation is the identity map on $\varphi(W \cap U)$ — smooth.

> [!note]- Derivation
> $\iota^{-1}$ takes a point $q \in U \subseteq M$ to the same point $q$ in the smooth manifold $U$. In coordinates:
>
> The chart on the source (the image $U \subseteq M$, viewed as an open subset of $M$, *but* considered as the codomain of $\iota$) — for $\iota^{-1}$, the source is "the open set $U$ in $M$" and the target is "the smooth submanifold $U$".
>
> However, $U$ (as a subset of $M$) and $U$ (as the smooth submanifold) have the *same* charts and the *same* smooth structure, by definition of the inherited smooth structure. So smoothness of $\iota^{-1}$ in any chart pair is the same calculation as smoothness of $\iota$.
>
> Alternative argument: the composition $\iota^{-1} \circ \iota = \operatorname{id}_U$, and if $\iota$ is a smooth bijection with a left inverse that is the identity, then any candidate for the right inverse is also smooth (in this case, the identity itself).

Therefore $\iota$ is a diffeomorphism from $U$ (smooth submanifold) onto $U$ (subset of $M$).

> [!note]- Complete formal solution
> **Claim.** Let $M$ be a smooth manifold and $U \subseteq M$ an open submanifold. The inclusion $\iota : U \hookrightarrow M$ is a smooth map, and a diffeomorphism onto its image.
>
> *Proof.* The inherited smooth structure on $U$ consists of charts $(W \cap U, \varphi|_{W \cap U})$ for $(W, \varphi)$ a smooth chart on $M$ with $W \cap U \neq \emptyset$.
>
> For any $p \in U$, choose a smooth chart $(W, \varphi)$ on $M$ with $p \in W$. The restricted chart $(W \cap U, \varphi|_{W \cap U})$ on $U$ contains $p$. The chart pair $((W \cap U, \varphi|_{W \cap U}), (W, \varphi))$ has chart containment $\iota(W \cap U) = W \cap U \subseteq W$.
>
> The coordinate representation is $\varphi \circ \iota \circ (\varphi|_{W \cap U})^{-1} : \varphi(W \cap U) \to \varphi(W)$. For $y \in \varphi(W \cap U)$, let $q = (\varphi|_{W \cap U})^{-1}(y) \in W \cap U$; then $\iota(q) = q$, and $\varphi(\iota(q)) = \varphi(q) = y$. So the coordinate representation is the identity map $\varphi(W \cap U) \to \varphi(W \cap U) \subseteq \varphi(W)$, manifestly smooth.
>
> Hence $\iota$ is smooth at $p$. Since $p$ was arbitrary, $\iota$ is smooth.
>
> For the diffeomorphism claim: $\iota : U \to U$ (where the codomain is $U$ as a subset of $M$, with its subspace topology and inherited smooth structure) is a bijection. The inverse $\iota^{-1}$, taking a point of $U \subseteq M$ to the same point in the smooth submanifold $U$, is the identity map. By the same chart calculation (with $M$ and $U$ swapped in the roles), $\iota^{-1}$ has identity coordinate representation in any restricted chart pair, hence is smooth.
>
> So $\iota$ is a diffeomorphism. $\quad\blacksquare$

---

# Key Takeaways

**The inherited smooth structure on an open submanifold is "the same" as the ambient.** The charts on $U$ are restrictions of the charts on $M$, and the smooth structure is determined by the same transition maps as the ambient. As a result, virtually any smoothness check on a map involving $U$ reduces to a smoothness check on $M$. This makes open submanifolds extremely cheap to work with — they inherit *everything* from the ambient manifold, and the inclusion is a smooth open embedding. The trigger is: any time you see "let $U \subseteq M$ be open" with no further structure, $U$ is automatically a smooth manifold with all the structures of $M$ restricted, and any inclusion is smooth.

**Smoothness of the identity-in-coordinates is the simplest verification.** When the coordinate representation of a map is literally the identity, smoothness is immediate (the identity is the simplest smooth function). This recurs in many situations: the inclusion of an open submanifold, the chart map of a chart (which is a diffeomorphism onto its image), the canonical projection to a quotient that admits a section. Whenever the coordinate representation is the identity, smoothness is one line. The trigger is recognizing the situation; the reaction is "it's the identity, hence smooth".

**[[Def - Diffeomorphism|Diffeomorphism]] in the open-submanifold case is bootstrap-trivial.** $\iota$ and $\iota^{-1}$ are both identity-in-coordinates, hence both smooth, hence $\iota$ is a diffeomorphism. This is in stark contrast to the general situation where smooth bijection $\not\Rightarrow$ diffeomorphism (e.g., $x \mapsto x^3$ on $\mathbb{R}$). The reason the inclusion works is that the smooth structure on $U$ is *defined* to be the restriction of the smooth structure on $M$ — there is no opportunity for the structures on the two sides to disagree.

The exercise is the simplest case of a general principle: smoothness checks for "tautological" maps (inclusion, projection to a quotient, chart maps) reduce to identity-in-coordinates and are immediate. The more interesting cases — quotient maps, smooth bijections that fail to be [[Def - Diffeomorphism|diffeomorphisms]], compositions — are where the chart-pull-back machinery does real work. Companion exercises: [[Ex - Composition of Smooth Maps is Smooth]] establishes the composition routine that this exercise simplifies trivially; [[Ex - A Continuous Function on a Compact Manifold Attains its Maximum]] uses compactness on an open submanifold to derive continuity facts.
