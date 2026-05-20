---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Thm - Tietze Extension Theorem"
  - "Def - Product Topology"
tags: [analysis, topology]
---

# Problem Statement

Let $X$ be a normal topological space, $F \subseteq X$ a closed subset, and $f : F \to \mathbb{R}^n$ a continuous function. Show that $f$ extends continuously to all of $X$: there exists continuous $g : X \to \mathbb{R}^n$ with $g|_F = f$.

If $f(F) \subseteq B$ for some closed convex (or even just closed) set $B \subseteq \mathbb{R}^n$, show that the extension can be arranged so that $g(X) \subseteq B$ as well — modulo a comment about which target sets admit this preservation.

**Recall:**

[[Thm - Tietze Extension Theorem|Tietze's extension theorem]] (scalar case): if $X$ is normal and $F \subseteq X$ is closed, every continuous bounded $f : F \to \mathbb{R}$ extends to continuous $g : X \to \mathbb{R}$, with the same bounds. The unbounded case follows by composing with a homeomorphism $\mathbb{R} \to (-1, 1)$ and back.

![[Thm - Tietze Extension Theorem#Statement]]

A function $f : F \to \mathbb{R}^n$ is continuous if and only if each coordinate $f_i = \pi_i \circ f : F \to \mathbb{R}$ is continuous (universal property of the [[Def - Product Topology|product topology]] on $\mathbb{R}^n$).

---

# Convergent Strategy

**Problem class.** A *reduction-to-scalar* problem: convert a vector-valued extension question to $n$ scalar extension questions, then use the scalar result. The whole exercise is one observation — coordinatewise continuity in $\mathbb{R}^n$ — combined with the standard scalar Tietze theorem.

**Assumption pattern.** A continuous map to $\mathbb{R}^n = \prod_{i=1}^n \mathbb{R}$. By the universal property of the product topology, this is *the same* as $n$ continuous maps to $\mathbb{R}$. Each scalar component is a continuous real-valued function on $F$, which extends by scalar Tietze; the $n$ extensions assemble into a vector extension.

**Theorem routing.** Decompose $f = (f_1, \dots, f_n)$ with each $f_i : F \to \mathbb{R}$ continuous. Apply scalar [[Thm - Tietze Extension Theorem|Tietze]] to each $f_i$, getting continuous $g_i : X \to \mathbb{R}$ extending $f_i$. Assemble $g = (g_1, \dots, g_n) : X \to \mathbb{R}^n$. By the same universal property, $g$ is continuous; on $F$, $g|_F = (g_1|_F, \dots, g_n|_F) = (f_1, \dots, f_n) = f$.

**Key decision point.** The whole proof is the observation that continuity in product topology is coordinatewise. There is no other technical content. Where things get interesting is the *range-preservation* claim: if $f(F)$ lies in a closed convex set $B$, can the extension be made to lie in $B$? For convex $B$, yes — use a retraction; for non-convex closed $B$, generally no.

---

# Legal Operations Used

1. **Use coordinatewise continuity in the product topology.** A map to $\prod_i Y_i$ is continuous iff each $\pi_i \circ f$ is.

2. **Apply scalar Tietze coordinate-by-coordinate** to extend each component, then reassemble.

3. **For range-preservation in convex $B$:** the standard move is to project the extension onto $B$ using the nearest-point projection $\pi_B : \mathbb{R}^n \to B$ (which is continuous and is a retraction when $B$ is closed convex). Apply $\pi_B$ to the coordinate-wise extension.

---

# Hints

> [!note]- Hint 1
> A continuous map $f : F \to \mathbb{R}^n$ has $n$ coordinate maps $f_i : F \to \mathbb{R}$. By the universal property of the product topology, $f$ is continuous iff each $f_i$ is. The reverse direction (assembling continuous coordinates into a continuous map) is the key.

> [!note]- Hint 2
> Apply scalar [[Thm - Tietze Extension Theorem|Tietze]] to each $f_i$: get $g_i : X \to \mathbb{R}$ continuous with $g_i|_F = f_i$.

> [!note]- Hint 3
> Assemble $g(x) = (g_1(x), \dots, g_n(x))$. Continuity follows from coordinatewise continuity in the product topology. Restriction: $g|_F = (g_1|_F, \dots, g_n|_F) = (f_1, \dots, f_n) = f$.

> [!note]- Hint 4
> *Range-preservation in convex $B$:* the nearest-point projection $\pi_B : \mathbb{R}^n \to B$ is continuous (closed convex sets have continuous metric projections by uniqueness of closest points). If $g$ extends $f$, so does $\pi_B \circ g$ (and lies in $B$).

---

# Solution

The vector Tietze theorem follows from the scalar one by the simple observation that continuity in a finite product is coordinatewise — applying scalar Tietze to each coordinate and assembling gives the extension.

**Step 1: Decompose $f$ into scalar coordinates.**

Write $f = (f_1, \dots, f_n) : F \to \mathbb{R}^n$ with $f_i = \pi_i \circ f : F \to \mathbb{R}$.

> [!note]- Derivation
> The projections $\pi_i : \mathbb{R}^n \to \mathbb{R}$ are continuous. So $f_i = \pi_i \circ f$ is continuous as a composition of continuous functions. Conversely, since the [[Def - Product Topology|product topology]] on $\mathbb{R}^n$ is the coarsest topology making the projections continuous, a map $h : Y \to \mathbb{R}^n$ is continuous iff each $\pi_i \circ h$ is. So $f$ continuous ⇔ each $f_i$ continuous.

**Step 2: Extend each scalar coordinate via scalar Tietze.**

By [[Thm - Tietze Extension Theorem|Tietze's extension theorem]] applied to each $f_i : F \to \mathbb{R}$ on the closed $F \subseteq X$ in normal $X$, there exists a continuous $g_i : X \to \mathbb{R}$ with $g_i|_F = f_i$. (If $f$ was bounded, choose $g_i$ with $\sup_X g_i = \sup_F f_i$, $\inf_X g_i = \inf_F f_i$.)

> [!note]- Derivation
> Apply [[Thm - Tietze Extension Theorem|Tietze]] coordinate by coordinate. Each application requires (i) $X$ normal — given — and (ii) $F$ closed in $X$ — given. The extension $g_i$ is continuous, real-valued, and equals $f_i$ on $F$. For bounded $f_i$, the extension can be arranged to have the same bounds; for unbounded $f_i$, Tietze still gives an extension after composing with a homeomorphism $\mathbb{R} \to (-1, 1)$ and back.

**Step 3: Reassemble the extensions into a continuous $g : X \to \mathbb{R}^n$.**

Define $g(x) = (g_1(x), \dots, g_n(x))$. Then $g$ is continuous (coordinates are) and $g|_F = f$.

> [!note]- Derivation
> *Continuity.* By the universal property of the product topology (one of the defining properties of $\mathbb{R}^n$ as a product), $g$ is continuous if and only if each $\pi_i \circ g = g_i$ is continuous. Each $g_i$ is continuous from Step 2, so $g$ is.
>
> *Restriction.* For $x \in F$, $g(x) = (g_1(x), \dots, g_n(x)) = (f_1(x), \dots, f_n(x)) = f(x)$.

**Step 4: Range-preservation for closed convex targets.**

If $f(F) \subseteq B$ for some closed convex $B \subseteq \mathbb{R}^n$, the extension can be arranged to satisfy $g(X) \subseteq B$.

> [!note]- Derivation
> Let $g$ be the extension from Step 3 (which may take values outside $B$). The *nearest-point projection* $\pi_B : \mathbb{R}^n \to B$, defined by $\pi_B(y) = \arg\min_{b \in B} \lVert y - b \rVert$, is well-defined and continuous for closed convex $B$ (uniqueness of the minimizer is by convexity + strict convexity of $\lVert \cdot \rVert^2$, continuity is a standard convex analysis result — the projection is in fact $1$-Lipschitz for closed convex $B$). Furthermore, $\pi_B$ restricted to $B$ is the identity (a retraction).
>
> Define $\widetilde g = \pi_B \circ g : X \to B \subseteq \mathbb{R}^n$. Then $\widetilde g$ is continuous (composition), $\widetilde g(X) \subseteq B$, and for $x \in F$, $g(x) = f(x) \in B$ so $\widetilde g(x) = \pi_B(f(x)) = f(x)$. So $\widetilde g$ is an extension of $f$ taking values in $B$.
>
> *Non-convex closed $B$ does not work in general.* If $B = \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 = 1\}$ is the unit circle, the question becomes: given a continuous map from a closed subset $F \subseteq X$ to $S^1$, can it always be extended? The answer is no — it depends on whether the map is null-homotopic. (For instance, the identity $S^1 \to S^1$ does *not* extend to a map $D^2 \to S^1$, by the no-retraction theorem.) Topological obstructions in the target prevent the general claim.

> [!note]- Complete formal solution
> *Existence of extension.* Decompose $f = (f_1, \dots, f_n)$ with $f_i = \pi_i \circ f$ continuous. By [[Thm - Tietze Extension Theorem|Tietze]] applied to each $f_i$ on the closed $F$ in normal $X$, there exist continuous $g_i : X \to \mathbb{R}$ with $g_i|_F = f_i$. Set $g = (g_1, \dots, g_n) : X \to \mathbb{R}^n$. By coordinatewise continuity in the product topology, $g$ is continuous; on $F$, $g = f$.
>
> *Range-preservation for closed convex $B$.* If $f(F) \subseteq B$, take $\widetilde g = \pi_B \circ g$ where $\pi_B$ is the continuous nearest-point projection. Then $\widetilde g : X \to B$, $\widetilde g$ extends $f$, and is continuous. $\blacksquare$

---

# Key Takeaways

**Continuity into a product is coordinatewise — this single fact reduces every vector-valued question to $n$ scalar questions.** It is the universal property of the product topology that makes this work: $g : X \to \prod_i Y_i$ is continuous iff each $\pi_i \circ g : X \to Y_i$ is. The consequence is that essentially every theorem about continuous real-valued functions extends *for free* to continuous $\mathbb{R}^n$-valued functions, with a one-line proof: do each coordinate separately. Examples: vector-valued integration ($\int f = (\int f_1, \dots, \int f_n)$), vector-valued differentiation (the Jacobian is the matrix of partial derivatives), vector-valued mean value theorem (false in general!), vector-valued Tietze (this exercise), vector-valued Stone–Weierstrass, vector-valued Arzelà–Ascoli. The structural reason: $\mathbb{R}^n$ is a *finite* product, so cofiniteness is automatic and product topology agrees with box topology, so the coordinate-by-coordinate decomposition is faithful.

**The trigger-reaction "I have a fact about real-valued functions and need its vector-valued version" ⇒ "do each coordinate separately and assemble".** This is one of the most-deployed moves in analysis. The exception: when the question involves a *single* number derived from the vector (the norm, or the determinant, or the trace), the per-coordinate decomposition does not respect the question, and one needs a vector-aware argument. The vector mean value theorem is the classic example: each coordinate satisfies MVT, but the points witnessing it depend on the coordinate, so there is no single point witnessing the vector MVT. *Always check whether the question survives per-coordinate decomposition before applying this technique.*

**Range-preservation in closed convex sets uses the metric projection $\pi_B$.** The metric projection onto a closed convex set is continuous (in fact $1$-Lipschitz), and is a retraction of $\mathbb{R}^n$ onto $B$. This is the standard tool for "force the extension to stay inside a target set". The trigger: any time you need an extension into a special subset of $\mathbb{R}^n$, ask whether the subset is closed convex. If yes, project after extending. The standard non-convex obstruction is *topological* — the target $S^{n-1}$ has nontrivial homotopy and not every map into it extends. This is where algebraic topology enters: the obstruction to extending continuous maps is exactly the homotopy of the target. For convex targets, no homotopy: contractible, so all maps extend.

**Vector Tietze + the inverse function theorem ⇒ many "extension of structure" theorems on manifolds.** A typical use: given a vector field defined on a closed subset of a manifold, can it be extended? Locally (in a chart $U \cong \mathbb{R}^n$), the field is a continuous function to $\mathbb{R}^n$, and on the closed restriction $F \cap U$ we can apply vector Tietze to get a local extension. Then a partition of unity argument (see [[Ex - Partition of unity for a smooth manifold]]) glues local extensions into a global one. The same recipe works for tensors, connections, Riemannian metrics, foliations. Each is an extension problem reducible to (a) coordinate-wise scalar extension + (b) partition of unity gluing.

**The scalar Tietze theorem is the "fundamental existence theorem" for continuous functions, and this vector version makes it apply universally.** From the bare hypothesis that the ambient space is normal and the source is closed, you can extend *any* finite-dimensional continuous map from the source to the whole space. This is what makes normal spaces "function-rich". The progression is: completely regular (separate points from closed sets) → normal (separate two closed sets) → vector-Tietze (extend arbitrary finite-dimensional continuous maps from closed subsets). Once vector Tietze is available, virtually every "build a continuous extension" argument in analysis on normal spaces becomes available. Without normality (see [[Ex - Failure of Tietze without normality]]), the whole edifice falls.
