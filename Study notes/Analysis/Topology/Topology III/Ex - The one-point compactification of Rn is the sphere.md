---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Thm - One-Point Compactification"
  - "Def - Locally Compact Space"
tags: [analysis, topology]
---

# Problem Statement

Let $S^n = \{x \in \mathbb{R}^{n+1} : \lVert x \rVert = 1\}$ be the unit sphere in $\mathbb{R}^{n+1}$, with $N = (0, \dots, 0, 1) \in S^n$ the **north pole**. Define the **stereographic projection** $\sigma : S^n \setminus \{N\} \to \mathbb{R}^n$ by
$$\sigma(x_1, \dots, x_n, x_{n+1}) = \frac{1}{1 - x_{n+1}}(x_1, \dots, x_n).$$

(a) Show that $\sigma$ is a homeomorphism between $S^n \setminus \{N\}$ and $\mathbb{R}^n$.

(b) Extend $\sigma$ to a continuous map $\widetilde\sigma : S^n \to (\mathbb{R}^n)^+$ (the [[Thm - One-Point Compactification|one-point compactification]] of $\mathbb{R}^n$) by sending $N \mapsto \infty$. Show that $\widetilde\sigma$ is a homeomorphism.

In particular, $(\mathbb{R}^n)^+ \cong S^n$ — the one-point compactification of Euclidean space is the sphere of one higher dimension.

**Recall:**

The [[Thm - One-Point Compactification|one-point compactification]] $X^+ = X \cup \{\infty\}$ of a locally compact Hausdorff space $X$ has topology consisting of: every open set of $X$, plus every set of the form $\{\infty\} \cup (X \setminus K)$ for $K \subseteq X$ compact. The point $\infty$ has, as a neighborhood basis, the "deep neighborhoods" — complements of compact subsets of $X$. The space $X^+$ is compact Hausdorff, and $X \hookrightarrow X^+$ is an open dense embedding.

![[Thm - One-Point Compactification#Statement]]

A **homeomorphism** between compact Hausdorff and Hausdorff spaces is automatic from being a continuous bijection: any continuous bijection $f : K \to Y$ with $K$ compact and $Y$ Hausdorff is automatically a homeomorphism, because closed subsets of $K$ are compact, hence $f$-images are compact, hence closed in $Y$.

---

# Convergent Strategy

**Problem class.** *Explicit homeomorphism construction* — exhibit a specific map and verify it is a continuous bijection between compact and Hausdorff spaces, then invoke "compact-to-Hausdorff continuous bijection ⇒ homeomorphism".

**Assumption pattern.** Stereographic projection has a long-standing explicit formula. Geometrically: draw a line from the north pole through any other point of the sphere; the line meets the equatorial hyperplane $\{x_{n+1} = 0\}$ in a unique point — this is the projected image. As the source point approaches the north pole, the projected image escapes to infinity in the equatorial hyperplane. Adjoining a single point $\infty$ to the codomain captures this escape and makes the map a bijection on the closed-up sphere.

**Theorem routing.** Three steps: (i) compute the inverse $\sigma^{-1}$ explicitly to verify bijection $S^n \setminus \{N\} \leftrightarrow \mathbb{R}^n$; (ii) note continuity of both $\sigma$ and $\sigma^{-1}$ as rational functions of the coordinates with non-vanishing denominator (so already a homeomorphism without needing the compact-Hausdorff trick); (iii) extend by $N \mapsto \infty$, check continuity at $N$ using "deep neighborhoods" of $\infty$, then invoke the compact-to-Hausdorff trick to conclude the extended map is a homeomorphism.

**Key decision point.** The continuity *at $N$* of the extended map is the only nontrivial step. A basic neighborhood of $\infty$ in $(\mathbb{R}^n)^+$ is $\{\infty\} \cup (\mathbb{R}^n \setminus K)$ for $K$ compact, i.e. "everything outside a compact set". Its preimage under $\widetilde\sigma$ is $\{N\} \cup \sigma^{-1}(\mathbb{R}^n \setminus K) = \{N\} \cup (S^n \setminus \sigma^{-1}(K)) \setminus \{N\}$... need to show this is open at $N$ — equivalently, $\sigma^{-1}(K)$ is compact in $S^n \setminus \{N\}$, hence closed in $S^n$, hence its complement (in $S^n$) is open. Compactness of $\sigma^{-1}(K)$ follows since $\sigma^{-1}$ is a homeomorphism on $\mathbb{R}^n$ and $K$ is compact.

---

# Legal Operations Used

1. **Construct an explicit formula and verify bijection via inverse.** When given a specific map, compute the inverse to check bijectivity directly.

2. **Use the compact-to-Hausdorff continuous bijection trick.** Any continuous bijection $K \to Y$ with $K$ compact, $Y$ Hausdorff is a homeomorphism — closed images of closed sets, so $f^{-1}$ is continuous.

3. **Identify deep neighborhoods of $\infty$ in $X^+$.** A neighborhood of $\infty$ contains a "tail" $X^+ \setminus K$ for some compact $K \subseteq X$. To check continuity of a map *to* $X^+$ at the point mapped to $\infty$, the preimages of these deep neighborhoods must be open.

4. **Reduce continuity questions for extensions to "open preimages of basic opens"** — a standard technique whenever a map's continuity is being checked at a single newly-added point.

---

# Hints

> [!note]- Hint 1
> *Inverse formula.* For $y \in \mathbb{R}^n$, the point on $S^n$ collinear with $N$ and $(y, 0) \in \mathbb{R}^{n+1}$, other than $N$, is given by
> $$\sigma^{-1}(y) = \frac{1}{1 + \lVert y \rVert^2}(2y, \lVert y \rVert^2 - 1).$$
> Verify $\lVert \sigma^{-1}(y) \rVert = 1$ and $\sigma(\sigma^{-1}(y)) = y$.

> [!note]- Hint 2
> Both $\sigma$ and $\sigma^{-1}$ are rational with non-vanishing denominator ($1 - x_{n+1}$ for $\sigma$, $1 + \lVert y \rVert^2$ for $\sigma^{-1}$ — both positive on their domain). So both are continuous, giving the homeomorphism on $S^n \setminus \{N\} \leftrightarrow \mathbb{R}^n$.

> [!note]- Hint 3
> *Continuity of $\widetilde\sigma$ at $N$.* A basic neighborhood of $\widetilde\sigma(N) = \infty$ is $\{\infty\} \cup (\mathbb{R}^n \setminus K)$ for $K$ compact. Its preimage in $S^n$ is $\{N\} \cup (S^n \setminus \{N\} \setminus \sigma^{-1}(K)) = S^n \setminus \sigma^{-1}(K)$. Compactness of $\sigma^{-1}(K)$ (continuous image of compact) makes it closed in $S^n$, so its complement is open, witnessing continuity.

> [!note]- Hint 4
> $\widetilde\sigma$ is a continuous bijection from the compact $S^n$ to the Hausdorff $(\mathbb{R}^n)^+$ (the one-point compactification is Hausdorff because $\mathbb{R}^n$ is locally compact Hausdorff). So $\widetilde\sigma$ is a homeomorphism.

---

# Solution

Stereographic projection turns the sphere with the north pole removed into $\mathbb{R}^n$ — and the north pole, the "missing point", precisely captures the "point at infinity" of $\mathbb{R}^n$. The one-point compactification of $\mathbb{R}^n$ adjoins exactly such a missing point, with neighborhoods of "infinity" being complements of compact sets — which the north pole's neighborhoods on the sphere literally are.

**Step 1: $\sigma$ has an explicit inverse, hence is a bijection.**

Define
$$\sigma^{-1}(y) = \frac{1}{1 + \lVert y \rVert^2}(2y, \lVert y \rVert^2 - 1) \quad \text{for } y \in \mathbb{R}^n.$$

> [!note]- Derivation
> *$\sigma^{-1}(y) \in S^n$.* The squared norm is
> $$\left\lVert\frac{2y}{1 + \lVert y \rVert^2}\right\rVert^2 + \left(\frac{\lVert y \rVert^2 - 1}{1 + \lVert y \rVert^2}\right)^2 = \frac{4\lVert y \rVert^2 + (\lVert y \rVert^2 - 1)^2}{(1 + \lVert y \rVert^2)^2} = \frac{(\lVert y \rVert^2 + 1)^2}{(1 + \lVert y \rVert^2)^2} = 1.$$
> So $\sigma^{-1}(y) \in S^n$.
>
> *$\sigma^{-1}(y) \neq N$.* The last coordinate of $\sigma^{-1}(y)$ is $(\lVert y \rVert^2 - 1)/(1 + \lVert y \rVert^2) < 1$ for all $y$ (the denominator exceeds the numerator), so $\sigma^{-1}(y)$ is never the north pole.
>
> *$\sigma \circ \sigma^{-1} = \mathrm{id}$.* For $y \in \mathbb{R}^n$, $\sigma(\sigma^{-1}(y))$ has first $n$ coordinates
> $$\frac{1}{1 - (\lVert y \rVert^2 - 1)/(1 + \lVert y \rVert^2)} \cdot \frac{2y}{1 + \lVert y \rVert^2} = \frac{1 + \lVert y \rVert^2}{2} \cdot \frac{2y}{1 + \lVert y \rVert^2} = y.$$
>
> *$\sigma^{-1} \circ \sigma = \mathrm{id}$.* For $x \in S^n \setminus \{N\}$, $\sigma^{-1}(\sigma(x))$: write $\sigma(x) = y$, then $\lVert y \rVert^2 = \lVert(x_1, \dots, x_n)\rVert^2/(1-x_{n+1})^2 = (1 - x_{n+1}^2)/(1 - x_{n+1})^2 = (1 + x_{n+1})/(1 - x_{n+1})$ (using $\lVert x \rVert = 1$). Then $1 + \lVert y \rVert^2 = 2/(1 - x_{n+1})$, and reading off the last coordinate of $\sigma^{-1}(y)$: $(\lVert y \rVert^2 - 1)/(1 + \lVert y \rVert^2) = ((1 + x_{n+1})/(1 - x_{n+1}) - 1)/(2/(1 - x_{n+1})) = (2x_{n+1}/(1 - x_{n+1}))(1 - x_{n+1})/2 = x_{n+1}$. The first $n$ coordinates similarly recover the $(x_1, \dots, x_n)$.
>
> Hence $\sigma$ and $\sigma^{-1}$ are mutual inverses.

**Step 2: $\sigma$ and $\sigma^{-1}$ are continuous, so $\sigma$ is a homeomorphism $S^n \setminus \{N\} \to \mathbb{R}^n$.**

> [!note]- Derivation
> $\sigma(x_1, \dots, x_{n+1}) = (x_1, \dots, x_n)/(1 - x_{n+1})$. The denominator $1 - x_{n+1} > 0$ on $S^n \setminus \{N\}$ (since $x_{n+1} < 1$ when $x \neq N$). Each coordinate of $\sigma$ is a quotient of continuous functions (polynomial in $x$, then divided by a non-vanishing continuous denominator), hence continuous.
>
> Similarly $\sigma^{-1}(y) = (2y, \lVert y \rVert^2 - 1)/(1 + \lVert y \rVert^2)$, denominator $1 + \lVert y \rVert^2 > 0$ everywhere, so continuous.
>
> Continuous bijection with continuous inverse = homeomorphism.

**Step 3: Extend by $N \mapsto \infty$ to $\widetilde\sigma : S^n \to (\mathbb{R}^n)^+$; check continuity at $N$.**

> [!note]- Derivation
> *Bijection.* $\widetilde\sigma$ is a bijection: $\sigma$ is a bijection $S^n \setminus \{N\} \to \mathbb{R}^n$, and the extension sends the missing $N$ to the missing $\infty$.
>
> *Continuity on $S^n \setminus \{N\}$.* This is the continuity of $\sigma$, already established.
>
> *Continuity at $N$.* A neighborhood basis of $\infty$ in $(\mathbb{R}^n)^+$ consists of sets $V_K = \{\infty\} \cup (\mathbb{R}^n \setminus K)$ for $K \subseteq \mathbb{R}^n$ compact. For continuity at $N$, we need that for every such $V_K$ there exists a neighborhood $U$ of $N$ in $S^n$ with $\widetilde\sigma(U) \subseteq V_K$.
>
> Equivalently, the preimage $\widetilde\sigma^{-1}(V_K)$ must contain a neighborhood of $N$. Compute:
> $$\widetilde\sigma^{-1}(V_K) = \widetilde\sigma^{-1}(\{\infty\}) \cup \widetilde\sigma^{-1}(\mathbb{R}^n \setminus K) = \{N\} \cup \sigma^{-1}(\mathbb{R}^n \setminus K) = \{N\} \cup (S^n \setminus \{N\}) \setminus \sigma^{-1}(K) = S^n \setminus \sigma^{-1}(K).$$
>
> We need $\sigma^{-1}(K)$ to be a closed subset of $S^n$ *not* containing $N$ — then its complement is an open neighborhood of $N$.
>
> $K \subseteq \mathbb{R}^n$ is compact. $\sigma^{-1} : \mathbb{R}^n \to S^n \setminus \{N\}$ is continuous, so $\sigma^{-1}(K)$ is a compact subset of $S^n \setminus \{N\}$ — in particular *not* containing $N$. As a compact subset of the Hausdorff $S^n$, $\sigma^{-1}(K)$ is closed in $S^n$. Hence $S^n \setminus \sigma^{-1}(K)$ is open in $S^n$ and contains $N$.
>
> So $\widetilde\sigma$ is continuous at $N$, hence on all of $S^n$.

**Step 4: Conclude $\widetilde\sigma$ is a homeomorphism.**

> [!note]- Derivation
> $\widetilde\sigma : S^n \to (\mathbb{R}^n)^+$ is a continuous bijection. $S^n$ is *compact* (closed bounded in $\mathbb{R}^{n+1}$, Heine–Borel). $(\mathbb{R}^n)^+$ is *Hausdorff* — by [[Thm - One-Point Compactification]], the one-point compactification of a locally compact Hausdorff space (and $\mathbb{R}^n$ is locally compact Hausdorff: open balls are compact-closed, points have compact neighborhoods) is compact Hausdorff.
>
> The standard fact: a continuous bijection $f : K \to Y$ with $K$ compact and $Y$ Hausdorff is automatically a homeomorphism. Proof: for closed $C \subseteq K$, $C$ is compact (closed subset of compact); $f(C)$ is compact (continuous image of compact); $f(C)$ is closed in $Y$ (compact subset of Hausdorff is closed). So $f$ sends closed to closed, equivalently $f^{-1}$ is continuous.
>
> Applying this to $\widetilde\sigma$: it is a homeomorphism. Hence $(\mathbb{R}^n)^+ \cong S^n$.

> [!note]- Complete formal solution
> *Bijection.* $\sigma^{-1}(y) = (2y, \lVert y \rVert^2 - 1)/(1 + \lVert y \rVert^2) \in S^n \setminus \{N\}$; direct verification $\sigma \circ \sigma^{-1} = \mathrm{id}$, $\sigma^{-1} \circ \sigma = \mathrm{id}$.
>
> *Homeomorphism on $S^n \setminus \{N\}$.* Both $\sigma, \sigma^{-1}$ are continuous as rational functions with positive denominators on their domains.
>
> *Extension.* Set $\widetilde\sigma(N) = \infty$. For continuity at $N$: a basic neighborhood of $\infty$ is $V_K = \{\infty\} \cup (\mathbb{R}^n \setminus K)$ ($K$ compact in $\mathbb{R}^n$); preimage is $S^n \setminus \sigma^{-1}(K)$, which is open (the compact $\sigma^{-1}(K) \subseteq S^n \setminus \{N\}$ is closed in $S^n$).
>
> *Homeomorphism.* $\widetilde\sigma$ is a continuous bijection from compact $S^n$ to Hausdorff $(\mathbb{R}^n)^+$, hence a homeomorphism. $\blacksquare$

---

# Key Takeaways

**The compact-to-Hausdorff continuous bijection trick is one of the most-used tools in topology for promoting a continuous bijection to a homeomorphism.** It avoids the hassle of verifying continuity of the inverse map directly. The hypothesis "$K$ compact, $Y$ Hausdorff" is essential: without compactness, closed subsets need not have compact images; without Hausdorffness, compact subsets need not be closed. When both hold, the inverse map sends opens to opens (equivalently, the map sends closeds to closeds) automatically. This is the standard finishing move whenever you have an explicit candidate homeomorphism between a "small" compact space and a "large" non-compact Hausdorff space — the typical use is *defining a homeomorphism by a formula* and then invoking this trick.

**Stereographic projection is the model "almost-homeomorphism" of geometry — extends to a true homeomorphism by adjoining one point.** The same logic applies to many "natural maps with a singularity at a single point": the Cayley transform between $S^1$ and $\mathbb{R}$ (or $S^2$ and $\mathbb{C} \cup \{\infty\}$, the Riemann sphere); the natural map $\overline{\mathbb{D}} \to \overline{\mathbb{R}^2}$ where the unit disk is sent to the closed half-plane via a Möbius transformation; the projective compactification of affine space. In each case, the original map is a homeomorphism away from a single singularity, and adjoining a single "point at infinity" extends it to a homeomorphism of compactifications.

**One-point compactification has a clean *geometric* model when the source is $\mathbb{R}^n$: it is just $S^n$.** This sometimes lets you replace a hard question about $\mathbb{R}^n$ (no compactness) with the same question on $S^n$ (compactness, Heine–Borel, fixed-point theorems, etc.), provided the question respects the compactification (i.e., behaves well at $\infty$). A typical use: studying a continuous map $f : \mathbb{R}^n \to \mathbb{R}^n$ with $f(x) \to \infty$ as $|x| \to \infty$ becomes a continuous map $\widetilde f : S^n \to S^n$ with $\widetilde f(N) = N$, on which one can apply the Brouwer degree, Lefschetz number, and so on. The compactified picture brings the full apparatus of algebraic topology to bear on what was a non-compact problem.

**Trigger-reaction: "I want to compactify $\mathbb{R}^n$" ⇒ "use $S^n$, via stereographic projection".** This is the most concrete and visualizable compactification, and it should be the first one tried when working with $\mathbb{R}^n$. The Stone–Čech compactification $\beta\mathbb{R}^n$ is much larger and harder to visualize. The projective compactification $\mathbb{RP}^n$ adds a whole hyperplane at infinity rather than a single point; it is the right choice for problems involving lines/directions but is *not* the one-point compactification. Identifying which compactification matches the problem at hand is a recurring decision in geometry and analysis.

**Continuity-at-a-newly-added-point: always check the "deep neighborhoods" criterion.** When extending a continuous map to include a single new point of the codomain, the only nontrivial step is continuity at the corresponding new point of the domain (or, equivalently, the points in the source that map to it). The criterion is "preimage of every neighborhood of the new point is open" — which, for one-point compactifications, becomes "preimage of every complement-of-compact is open". This is a standard pattern: it appears in defining continuous extensions to a Stone–Čech compactification, to a one-point compactification, to a closure, to a completion. Always: identify the local neighborhood basis of the new point, check open-preimage for those basic neighborhoods.

**The connection to homotopy: $S^n = (\mathbb{R}^n)^+$ is foundational for cohomology with compact support and Pontryagin duality.** The reduced cohomology of $(\mathbb{R}^n)^+$ equals the compactly-supported cohomology of $\mathbb{R}^n$, by the long exact sequence of the pair $((\mathbb{R}^n)^+, \infty)$. So topology of $S^n$ controls compactly-supported phenomena on $\mathbb{R}^n$. This is one of the reasons $S^n$ is the *canonical* compact $n$-manifold without boundary: it is the one-point compactification of the standard local model $\mathbb{R}^n$. Many deep theorems (Poincaré duality, the Atiyah–Singer index theorem, K-theory of Euclidean space) hinge on this identification.
