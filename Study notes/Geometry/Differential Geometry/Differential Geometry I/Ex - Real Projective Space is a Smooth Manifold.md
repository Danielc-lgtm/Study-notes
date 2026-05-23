---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Atlas and Smooth Structure"
  - "Def - Transition Function"
  - "Def - Topological Manifold"
  - "Thm - Smooth Structure from Maximal Atlas"
tags: [geometry, differential-geometry]
---

# Problem Statement

Show that the real projective space $\mathbb{RP}^n$ — the set of one-dimensional linear [[Def - Subspace|subspaces]] of $\mathbb{R}^{n+1}$ — admits a smooth manifold structure of [[Def - Dimension|dimension]] $n$.

Define $\mathbb{RP}^n = (\mathbb{R}^{n+1} \setminus \{0\}) / \sim$, where $x \sim y$ iff $y = \lambda x$ for some $\lambda \in \mathbb{R} \setminus \{0\}$. The equivalence class of $x = (x^1, \dots, x^{n+1})$ is the **homogeneous coordinate** $[x^1 : \dots : x^{n+1}]$, well-defined up to scaling. Equip $\mathbb{RP}^n$ with the quotient topology induced by the natural surjection $\pi : \mathbb{R}^{n+1} \setminus \{0\} \to \mathbb{RP}^n$.

(a) Define the $n+1$ affine charts $(U_i, \varphi_i)$ for $i = 1, \dots, n+1$ on $\mathbb{RP}^n$, where $U_i = \{[x^1 : \dots : x^{n+1}] : x^i \neq 0\}$ and $\varphi_i$ "dehomogenizes" by dividing by the $i$-th coordinate. Verify each $\varphi_i$ is a homeomorphism onto $\mathbb{R}^n$.

(b) Compute the transition function $\varphi_j \circ \varphi_i^{-1}$ for some choice of $i \neq j$.

(c) Verify each transition function is smooth, so $\{(U_i, \varphi_i)\}_{i=1}^{n+1}$ is a smooth atlas on $\mathbb{RP}^n$.

(d) Verify $\mathbb{RP}^n$ is Hausdorff and second-countable, so that the atlas determines a smooth manifold structure.

**Recall:**

The smooth atlas / smooth structure framework:

![[Def - Smooth Atlas and Smooth Structure#The Definition]]

The quotient topology on $\mathbb{RP}^n$: a subset $V \subseteq \mathbb{RP}^n$ is open iff $\pi^{-1}(V) \subseteq \mathbb{R}^{n+1} \setminus \{0\}$ is open. The natural projection $\pi$ is then continuous (in fact, an open map, as we will verify).

---

# Convergent Strategy

**Problem class:** Constructing a smooth structure on a quotient space — type 2 of the problem-solving routine in [[Differential Geometry I — Smooth Manifolds and Atlases#Problem-Solving Strategy]]. The space is presented as a quotient, and the strategy is to lift charts from the covering space (here, $\mathbb{R}^{n+1} \setminus \{0\}$) by restricting the quotient map to open sets where it is a homeomorphism onto its image.

**Assumption pattern:** $\mathbb{RP}^n$ is the quotient of $\mathbb{R}^{n+1} \setminus \{0\}$ by the action of $\mathbb{R} \setminus \{0\}$ via scaling. The key topological observation is that the quotient map $\pi$ is an *open map*: if $W \subseteq \mathbb{R}^{n+1} \setminus \{0\}$ is open, then $\pi(W)$ is open in $\mathbb{RP}^n$, equivalently $\pi^{-1}(\pi(W))$ is open in $\mathbb{R}^{n+1} \setminus \{0\}$. This is because $\pi^{-1}(\pi(W)) = \bigcup_{\lambda \neq 0} \lambda W$ — a union of dilations of $W$, each of which is open. Once $\pi$ is open, the open sets of $\mathbb{RP}^n$ are precisely the images of open sets in $\mathbb{R}^{n+1} \setminus \{0\}$, and we can construct charts by restricting $\pi$ to suitable open subsets where it becomes a homeomorphism.

**Theorem routing:** The smooth atlas of $n+1$ affine charts is the natural cover, and [[Thm - Smooth Structure from Maximal Atlas]] gives the smooth structure once smoothness of transitions is verified. Hausdorff requires extra care (it does not follow automatically from being a quotient of a Hausdorff space); the standard verification uses the open-map property and explicit separation of [[Def - Coset|cosets]].

**Key decision point:** The non-obvious choice is the *form* of the chart maps. The natural impulse is to project to a particular hyperplane (e.g., $x^{n+1} = 1$) — but this only covers one chart's worth of $\mathbb{RP}^n$. The full $(n+1)$-chart construction uses each coordinate hyperplane in turn: $U_i$ is the locus where the $i$-th coordinate is nonzero, and $\varphi_i$ divides by that coordinate. The choice is essentially forced by the symmetry of the $n+1$ coordinate directions, and the resulting transition functions are rational with poles at the "missing" coordinate hyperplane.

---

# Legal Operations Used

1. **Operation 1 from the topic page (cover with charts).** The $n+1$ affine charts $\{(U_i, \varphi_i)\}_{i=1}^{n+1}$ cover $\mathbb{RP}^n$ — every line through the origin has at least one nonzero coordinate.

2. **Operation 2 from the topic page (compute transitions).** We compute $\varphi_j \circ \varphi_i^{-1}$ explicitly as a rational function and verify smoothness on its domain.

3. **Operation 7 from the topic page (quotient by a properly discontinuous [[Def - Group|group]] action).** $\mathbb{RP}^n = (\mathbb{R}^{n+1} \setminus \{0\}) / \mathbb{R}^\times$ is a quotient by the action of $\mathbb{R}^\times$ via scaling; the action is free (no nonzero $x$ is scaled to itself by a nontrivial $\lambda$) and proper, hence the quotient is a smooth manifold (we verify this directly without invoking the general theorem, which is more delicate for non-discrete [[Def - Group|groups]]).

4. **Operation 8 from the topic page (verify Hausdorff and second countability).** Hausdorff requires explicit verification using the open-map property of $\pi$; second countability follows from $\mathbb{R}^{n+1} \setminus \{0\}$ being second-countable and $\pi$ open.

---

# Hints

> [!note]- Hint 1
> Think of $\mathbb{RP}^n$ as "the space of lines through the origin in $\mathbb{R}^{n+1}$." A line is determined by any nonzero point on it; the equivalence relation is "lies on the same line", which is scaling.

> [!note]- Hint 2
> The affine chart $\varphi_i([x^1 : \dots : x^{n+1}]) = (x^1/x^i, \dots, \widehat{x^i/x^i}, \dots, x^{n+1}/x^i)$ — drop the $i$-th coordinate (it's always $1$ after dehomogenizing). The chart $U_i$ is the locus where the $i$-th homogeneous coordinate is nonzero.

> [!note]- Hint 3
> For the transition: $\varphi_i^{-1}$ inserts $1$ in the $i$-th position. Then $\varphi_j$ divides through by the $j$-th coordinate, which (in $\varphi_i$-coordinates) is the $(j-1)$-th or $j$-th coordinate of the input, depending on whether $j < i$ or $j > i$.

> [!note]- Hint 4
> To verify $\mathbb{RP}^n$ is Hausdorff: given two distinct lines $L_1, L_2$ through the origin, pick representatives $x_1, x_2$ with $|x_1| = |x_2| = 1$, then $x_1 \neq \pm x_2$ since they represent different lines. Separate $x_1, x_2$ by disjoint open neighbourhoods in $S^n$; their saturations under scaling give disjoint open neighbourhoods of $L_1, L_2$ in $\mathbb{RP}^n$.

---

# Solution

The proof breaks into four steps. Step 1 defines the affine charts $\varphi_i$ and computes $\varphi_i^{-1}$. Step 2 verifies the charts are [[Def - Homeomorphism|homeomorphisms]] and computes a sample transition. Step 3 verifies smoothness of the transition function. Step 4 verifies the topological properties (Hausdorff and second countability). The non-obvious move is in Step 4, where verifying Hausdorff requires the open-map property of $\pi$ plus the antipodal-free structure of the quotient.

**Step 1: Define the affine charts.**

For $i = 1, \dots, n+1$, let
$$U_i = \{[x^1 : \dots : x^{n+1}] \in \mathbb{RP}^n : x^i \neq 0\},$$
$$\varphi_i([x^1 : \dots : x^{n+1}]) = \left(\frac{x^1}{x^i}, \dots, \frac{x^{i-1}}{x^i}, \frac{x^{i+1}}{x^i}, \dots, \frac{x^{n+1}}{x^i}\right) \in \mathbb{R}^n.$$
(The $i$-th coordinate, which would be $x^i/x^i = 1$, is omitted.)

> [!note]- Derivation
> *Well-defined on $U_i$:* If $y^j = \lambda x^j$ for $\lambda \neq 0$, then $y^j/y^i = (\lambda x^j)/(\lambda x^i) = x^j/x^i$. So $\varphi_i$ depends only on the equivalence class, not the representative. ✓
>
> *Surjective onto $\mathbb{R}^n$:* For any $u = (u^1, \dots, u^n) \in \mathbb{R}^n$, take $x = (u^1, \dots, u^{i-1}, 1, u^i, \dots, u^n) \in \mathbb{R}^{n+1} \setminus \{0\}$ (with $1$ in the $i$-th position); then $[x] \in U_i$ and $\varphi_i([x]) = u$. ✓
>
> *Injective on $U_i$:* If $\varphi_i([x]) = \varphi_i([y])$, then $x^j/x^i = y^j/y^i$ for all $j \neq i$, i.e. $y^j = (y^i/x^i) x^j$ for $j \neq i$, and $y^i = (y^i/x^i) x^i$ trivially. So $y = (y^i/x^i) x$, hence $[y] = [x]$. ✓
>
> So $\varphi_i$ is a bijection $U_i \to \mathbb{R}^n$.

**Step 2: $\varphi_i$ is a homeomorphism; compute a transition function.**

The inverse $\varphi_i^{-1} : \mathbb{R}^n \to U_i$ is
$$\varphi_i^{-1}(u^1, \dots, u^n) = [u^1 : \dots : u^{i-1} : 1 : u^i : \dots : u^n].$$
For $i < j$, the transition function $\varphi_j \circ \varphi_i^{-1}$ is a smooth map from $\varphi_i(U_i \cap U_j) \subseteq \mathbb{R}^n$ to $\varphi_j(U_i \cap U_j) \subseteq \mathbb{R}^n$. Specifically,
$$\varphi_i(U_i \cap U_j) = \{u \in \mathbb{R}^n : u^{j-1} \neq 0\} \quad \text{(for } i < j\text{)}$$
(the $(j-1)$-th coordinate of $u$ corresponds to the $j$-th homogeneous coordinate of $\varphi_i^{-1}(u)$, since $u$ has coordinates indexed $1, \dots, i-1, i, \dots, n$ corresponding to homogeneous indices $1, \dots, i-1, i+1, \dots, n+1$).

> [!note]- Derivation
> *Continuity of $\varphi_i$:* $\varphi_i \circ \pi : \pi^{-1}(U_i) \to \mathbb{R}^n$ is the map $x \mapsto (x^1/x^i, \dots, x^{n+1}/x^i)$ minus the $i$-th coordinate. Each component is continuous on $\pi^{-1}(U_i) = \{x : x^i \neq 0\}$, so $\varphi_i \circ \pi$ is continuous, and by the universal property of the quotient topology, $\varphi_i$ is continuous.
>
> *Continuity of $\varphi_i^{-1}$:* $\varphi_i^{-1}$ is the composition $u \mapsto (u^1, \dots, u^{i-1}, 1, u^i, \dots, u^n) \mapsto [(u^1, \dots, u^{i-1}, 1, u^i, \dots, u^n)]$. The first arrow is continuous (a polynomial map), and the second is $\pi$, also continuous. So $\varphi_i^{-1}$ is continuous.
>
> So $\varphi_i : U_i \to \mathbb{R}^n$ is a homeomorphism.
>
> *Transition $\varphi_j \circ \varphi_i^{-1}$ for $i < j$:* Take $u \in \varphi_i(U_i \cap U_j)$, equivalently $u^{j-1} \neq 0$ (since the $j$-th homogeneous coordinate of $\varphi_i^{-1}(u)$ is $u^{j-1}$). Compute:
> $$\varphi_i^{-1}(u) = [u^1 : \dots : u^{i-1} : 1 : u^i : \dots : u^n],$$
> $$\varphi_j(\varphi_i^{-1}(u)) = \frac{1}{u^{j-1}}(u^1, \dots, u^{i-1}, 1, u^i, \dots, u^{j-2}, \widehat{u^{j-1}}, u^j, \dots, u^n) \in \mathbb{R}^n,$$
> where $\widehat{u^{j-1}}$ indicates that the $(j-1)$-th coordinate (which would have been $u^{j-1}/u^{j-1} = 1$) is omitted.

**Step 3: Verify smoothness.**

Each component of $\varphi_j \circ \varphi_i^{-1}$ is a rational function with denominator $u^{j-1}$ (nonzero on the domain), hence smooth on $\{u^{j-1} \neq 0\} \subseteq \mathbb{R}^n$.

> [!note]- Derivation
> Explicitly: for $k \neq j-1$, the $k$-th component of $\varphi_j(\varphi_i^{-1}(u))$ is one of:
> - $u^k/u^{j-1}$ (for $k < i-1$, taking $u^k$ as $x^k$ in the homogeneous coordinates, divided by $u^{j-1} = x^j$);
> - $1/u^{j-1}$ (for the position where the homogeneous coordinate would have been the inserted "$1$" of $\varphi_i^{-1}$);
> - $u^{k'}/u^{j-1}$ for some shifted $k'$ when $k > j-1$ (due to omission of the $(j-1)$-th coordinate after division).
>
> All of these are rational functions with denominator $u^{j-1}$, nonzero on the domain. Hence smooth.
>
> By the same argument with the roles of $i$ and $j$ swapped, the inverse transition $\varphi_i \circ \varphi_j^{-1}$ is smooth on its domain. So the charts $(U_i, \varphi_i)$ and $(U_j, \varphi_j)$ are smoothly compatible.

**Step 4: Verify Hausdorff and second countability; conclude.**

$\mathbb{RP}^n$ is Hausdorff because the quotient map $\pi : S^n \to \mathbb{RP}^n$ (restricting from $\mathbb{R}^{n+1} \setminus \{0\}$ to the unit sphere) is a quotient map by a free action of $\mathbb{Z}/2 = \{\pm 1\}$ on $S^n$ via antipodal action, and this quotient is Hausdorff because the action is free and properly discontinuous. Alternatively, one constructs disjoint open neighbourhoods directly.

$\mathbb{RP}^n$ is second countable because $\mathbb{R}^{n+1} \setminus \{0\}$ is, $\pi$ is open, and a countable basis $\mathcal{B}$ of $\mathbb{R}^{n+1} \setminus \{0\}$ produces a countable basis $\{\pi(B) : B \in \mathcal{B}\}$ of $\mathbb{RP}^n$.

> [!note]- Derivation
> *Open-map property of $\pi$:* If $W \subseteq \mathbb{R}^{n+1} \setminus \{0\}$ is open, then $\pi^{-1}(\pi(W)) = \bigcup_{\lambda \neq 0} \lambda W$. Each $\lambda W$ is open (multiplication by $\lambda$ is a homeomorphism), so the union is open. Hence $\pi(W)$ is open in $\mathbb{RP}^n$ (by definition of quotient topology).
>
> *Hausdorff via $S^n \to \mathbb{RP}^n$:* The restriction of $\pi$ to $S^n$ is the quotient $S^n \to S^n / \{\pm 1\}$, which is $\mathbb{RP}^n$ (every line through $0$ in $\mathbb{R}^{n+1}$ meets $S^n$ at a pair of antipodal points). The $\mathbb{Z}/2$ action on $S^n$ is free and properly discontinuous (in fact: the action map $\mathbb{Z}/2 \times S^n \to S^n \times S^n$ is proper, since $S^n$ is compact). By a standard result in covering-space theory, the quotient of a Hausdorff space by a free properly discontinuous action is Hausdorff.
>
> *Direct verification of Hausdorff:* Given two distinct lines $L_1, L_2 \in \mathbb{RP}^n$, pick representatives $x_1 \in L_1, x_2 \in L_2$ in $S^n$. Since $L_1 \neq L_2$, $x_1 \neq \pm x_2$. Choose $\varepsilon < |x_1 - x_2|/2$ and $\varepsilon < |x_1 + x_2|/2$. The open balls $B_\varepsilon(x_1), B_\varepsilon(x_2)$ in $S^n$ are disjoint, and the saturation $\pm B_\varepsilon(x_i) = B_\varepsilon(x_i) \cup B_\varepsilon(-x_i)$ — open by the open-map property — are also disjoint. Their images $\pi(B_\varepsilon(x_1))$ and $\pi(B_\varepsilon(x_2))$ are disjoint open neighbourhoods of $L_1$ and $L_2$ in $\mathbb{RP}^n$.
>
> *Second countability:* $\mathbb{R}^{n+1} \setminus \{0\}$ has a countable basis $\mathcal{B}$ (open balls with rational radii and rational centres in $\mathbb{R}^{n+1} \setminus \{0\}$). By the open-map property, $\{\pi(B) : B \in \mathcal{B}\}$ is a countable family of open subsets of $\mathbb{RP}^n$. To see it is a basis: any open $V \subseteq \mathbb{RP}^n$ has $\pi^{-1}(V)$ open in $\mathbb{R}^{n+1} \setminus \{0\}$, hence $\pi^{-1}(V) = \bigcup_i B_i$ for some $B_i \in \mathcal{B}$, and $V = \pi(\pi^{-1}(V)) = \bigcup_i \pi(B_i)$.
>
> *Conclusion.* $\mathbb{RP}^n$ is a topological $n$-manifold (Hausdorff, second-countable, locally Euclidean via the $\varphi_i$). The atlas $\{(U_i, \varphi_i)\}_{i=1}^{n+1}$ is smooth by Step 3. By [[Thm - Smooth Structure from Maximal Atlas]], it determines a unique smooth manifold structure on $\mathbb{RP}^n$.

> [!note]- Complete formal solution
> **Claim.** $\mathbb{RP}^n$, with the smooth structure determined by the affine atlas $\{(U_i, \varphi_i)\}_{i=1}^{n+1}$, is a smooth $n$-manifold.
>
> *Proof.* Equip $\mathbb{RP}^n = (\mathbb{R}^{n+1} \setminus \{0\}) / \sim$ with the quotient topology under the projection $\pi : \mathbb{R}^{n+1} \setminus \{0\} \to \mathbb{RP}^n$. We verify each requirement of a smooth manifold.
>
> **Step 0 — Open-map property of $\pi$.** For $W \subseteq \mathbb{R}^{n+1} \setminus \{0\}$ open, $\pi^{-1}(\pi(W)) = \bigcup_{\lambda \neq 0} \lambda W$ is open as a union of open sets (each $\lambda W$ is open since multiplication by $\lambda \neq 0$ is a homeomorphism of $\mathbb{R}^{n+1} \setminus \{0\}$). So $\pi$ is an open map.
>
> **Step 1 — The affine charts are [[Def - Homeomorphism|homeomorphisms]].** For $i = 1, \dots, n+1$, define $U_i = \pi(\{x : x^i \neq 0\})$ (open by Step 0) and
> $$\varphi_i([x]) = \left(\frac{x^1}{x^i}, \dots, \frac{\widehat{x^i}}{x^i}, \dots, \frac{x^{n+1}}{x^i}\right).$$
> This is well-defined (invariant under scaling), bijective onto $\mathbb{R}^n$, continuous (descends from a continuous map on $\pi^{-1}(U_i)$ by the universal property of the quotient topology), and has continuous inverse $\varphi_i^{-1}(u) = [u^1 : \dots : u^{i-1} : 1 : u^i : \dots : u^n]$. So each $\varphi_i : U_i \to \mathbb{R}^n$ is a homeomorphism, and $\{U_i\}_{i=1}^{n+1}$ covers $\mathbb{RP}^n$ (every nonzero vector has at least one nonzero coordinate).
>
> **Step 2 — Smooth compatibility.** Take $i < j$. On $U_i \cap U_j = \pi(\{x : x^i \neq 0, x^j \neq 0\})$, the transition function $\varphi_j \circ \varphi_i^{-1}$ at $u \in \varphi_i(U_i \cap U_j) = \{u^{j-1} \neq 0\}$ is
> $$\varphi_j(\varphi_i^{-1}(u)) = \frac{1}{u^{j-1}}(u^1, \dots, u^{i-1}, 1, u^i, \dots, \widehat{u^{j-1}}, \dots, u^n).$$
> Each component is a rational function of $u$ with denominator $u^{j-1} \neq 0$, hence smooth on the domain. The case $i > j$ is symmetric. So all transitions are smooth.
>
> **Step 3 — Hausdorff.** Given distinct $[x_1], [x_2] \in \mathbb{RP}^n$, take unit representatives $x_1, x_2 \in S^n$. Distinctness in $\mathbb{RP}^n$ means $x_1 \neq \pm x_2$. Choose $\varepsilon < \frac{1}{2}\min(|x_1 - x_2|, |x_1 + x_2|)$. The sets $B_\varepsilon(x_1), B_\varepsilon(x_2) \subseteq \mathbb{R}^{n+1} \setminus \{0\}$ are open and disjoint from $B_\varepsilon(-x_1), B_\varepsilon(-x_2)$ respectively. The saturations $B_\varepsilon(x_1) \cup B_\varepsilon(-x_1)$ and $B_\varepsilon(x_2) \cup B_\varepsilon(-x_2)$ — still open — are disjoint after suitable choice of $\varepsilon$, and their images $\pi(B_\varepsilon(x_i))$ are disjoint open neighbourhoods of $[x_1], [x_2]$.
>
> **Step 4 — Second countability.** A countable basis $\mathcal{B}$ of $\mathbb{R}^{n+1} \setminus \{0\}$ projects to a countable basis $\{\pi(B) : B \in \mathcal{B}\}$ of $\mathbb{RP}^n$ via the open-map property (every open $V \subseteq \mathbb{RP}^n$ equals $\pi(\pi^{-1}(V)) = \bigcup_i \pi(B_i)$ for a basis cover $\pi^{-1}(V) = \bigcup_i B_i$).
>
> **Conclusion.** $\mathbb{RP}^n$ is Hausdorff, second-countable, and locally Euclidean of [[Def - Dimension|dimension]] $n$; the affine atlas is smooth. By [[Thm - Smooth Structure from Maximal Atlas]], $\mathbb{RP}^n$ has a unique smooth manifold structure determined by this atlas. $\blacksquare$

> [!warning] Illegal but tempting alternative route: identifying with $S^n / \{\pm 1\}$ from the start
> One could try to define $\mathbb{RP}^n = S^n / \{\pm 1\}$ — the quotient of the sphere by the antipodal action — and conclude from "quotient by free properly discontinuous action of a finite group on a manifold is a manifold" that $\mathbb{RP}^n$ is a smooth manifold. This is true but invokes a substantial theorem (covering space theory + smoothness of the quotient) that is more sophisticated than needed. The direct approach above — explicit affine charts and direct verification — is more elementary and gives concrete coordinates for later computation.

---

# Key Takeaways

**Quotient manifolds: charts are lifted from the covering space.** When a manifold $M$ is presented as a quotient $M = \widetilde{M}/\Gamma$ (by a discrete group $\Gamma$ or by an equivalence relation), the most natural way to put charts on $M$ is to lift them from $\widetilde{M}$: find an open set $\widetilde{U} \subseteq \widetilde{M}$ on which the quotient map $\pi : \widetilde{M} \to M$ is a homeomorphism onto its image (this happens when $\widetilde{U}$ meets each $\Gamma$-orbit in at most one point), and push forward the chart on $\widetilde{U}$ to a chart on $\pi(\widetilde{U})$. The construction here uses $\widetilde{U}_i = \{x : x^i \neq 0\}$ and a section of $\pi$ given by "set the $i$-th coordinate to $1$"; the chart $\varphi_i$ is the composition of this section with the projection of $\mathbb{R}^{n+1}$ onto the remaining $n$ coordinates.

**The open-map property of the quotient projection is the key technical lemma.** Hausdorff and second-countability of a quotient space are *not* automatic — they require the quotient map to be "well-behaved", which here means open. The proof of openness for $\pi : \mathbb{R}^{n+1} \setminus \{0\} \to \mathbb{RP}^n$ uses the *structure of the equivalence relation*: orbits of the $\mathbb{R}^\times$-action are unions of dilations of any given set. Whenever you encounter a quotient by a continuous group action, openness of $\pi$ is typically the first thing to verify, and it makes Hausdorff + second-countability proofs much cleaner.

**The $n+1$ affine charts have rational transition functions — a hallmark of *algebraic-geometric* manifolds.** The transition functions on $\mathbb{RP}^n$ are not just smooth but *rational* — quotients of polynomials. This is the defining feature of $\mathbb{RP}^n$ as a **projective variety** in algebraic geometry: the same smooth structure is obtained by viewing $\mathbb{RP}^n$ as an algebraic variety with affine open cover by the $U_i$ (each isomorphic to $\mathbb{A}^n$, affine $n$-space) and rational transition maps. This is the bridge between differential geometry and algebraic geometry; the manifold $\mathbb{RP}^n$ is the simplest non-trivial projective variety, and the same affine atlas appears in algebraic geometry as the standard open cover of $\mathbb{P}^n$. **Complex projective space** $\mathbb{CP}^n$ (Lee Problem 1-9) has the same charts but with complex coefficients and holomorphic transitions, making it a complex manifold of complex dimension $n$.

**The choice of normalization point in each chart's section is arbitrary — but the smooth structure is canonical.** The affine charts use "set the $i$-th coordinate to $1$" as their normalization. One could equivalently use "set the $i$-th coordinate to a fixed nonzero constant" or even "set the $i$-th coordinate to a smooth function of the other coordinates"; the resulting smooth structures all agree (the smooth structures generated are equivalent via smooth compatibility). The choice is conventional, and the canonical smooth structure on $\mathbb{RP}^n$ is invariant under it.

**$\mathbb{RP}^n$ is compact and the link to topology.** Like $S^n$, $\mathbb{RP}^n$ is compact (a quotient of the compact $S^n$), so it requires at least two charts to cover. The minimum number is two for $\mathbb{RP}^1 = S^1$ (which is just a circle), but for $n \geq 2$ the affine cover with $n+1$ charts is the most symmetric. The number of charts in the affine cover equals the codimension of the "missing locus" $\{x^i = 0\}$ in each chart, which is essentially $1$ — a hyperplane removed in each chart, and we need $n+1$ such hyperplanes to cover everything.
