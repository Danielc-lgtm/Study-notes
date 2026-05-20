---
type: exercise
subject: topology
difficulty: "⭐"
prereqs:
  - "Def - Product Topology"
  - "Def - Hausdorff Space"
tags: [analysis, topology]
---

# Problem Statement

Let $\{X_\alpha\}_{\alpha \in A}$ be a family of **Hausdorff** topological spaces. Show that the [[Def - Product Topology|product]] $\prod_{\alpha \in A} X_\alpha$ is Hausdorff in the product topology.

**Recall:**

A topological space $X$ is **Hausdorff** if for every pair of distinct points $x, y \in X$ there exist disjoint open sets $U \ni x$ and $V \ni y$. This is the most-used separation axiom: it is what makes limits unique, what allows compactness to deliver closedness, and what every analysis-flavored topology assumes by default.

The **product topology** on $\prod_\alpha X_\alpha$ is the coarsest topology making every projection $\pi_\beta : \prod_\alpha X_\alpha \to X_\beta$, $(x_\alpha) \mapsto x_\beta$, continuous. A subbasis consists of the cylinders $\pi_\beta^{-1}(U)$ for $U \subseteq X_\beta$ open and $\beta \in A$. The full basis is finite intersections of cylinders — sets of the form $\prod_\alpha V_\alpha$ where $V_\alpha = X_\alpha$ for all but finitely many $\alpha$. Coordinate projections are open and continuous, and the preimage of an open set in any one factor is open in the product.

![[Def - Product Topology#The Definition]]

---

# Convergent Strategy

**Problem class.** This is a *preservation* problem: an axiom of $X_\alpha$ (Hausdorffness) is being pushed up to the product. As discussed in the topic page's [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact#Problem-Solving Strategy|problem-solving strategy]], constructions on products almost always proceed by reducing a global statement about $\prod_\alpha X_\alpha$ to a single-coordinate statement and pulling back via a projection.

**Assumption pattern.** Two distinct points $x = (x_\alpha)$ and $y = (y_\alpha)$ of the product *must* differ in at least one coordinate — that is what "distinct in the product" means. Once you fix any single such coordinate $\alpha_0$ with $x_{\alpha_0} \neq y_{\alpha_0}$, the Hausdorffness of $X_{\alpha_0}$ provides disjoint open neighborhoods there.

**Theorem routing.** Pull the disjoint open neighborhoods back to the product via $\pi_{\alpha_0}^{-1}$. Since $\pi_{\alpha_0}$ is continuous, the preimages are open; since preimages preserve disjointness ($\pi^{-1}(U) \cap \pi^{-1}(V) = \pi^{-1}(U \cap V) = \pi^{-1}(\emptyset) = \emptyset$), they are disjoint; and they obviously contain $x$ and $y$ respectively.

**Key decision point.** The whole exercise reduces to the observation that *one bad coordinate is enough*. You do not need to separate every coordinate — you only need to separate the coordinate where the points disagree, and the projection back to the product does the rest. This compression — using just one coordinate — is the standard pattern for proving properties of products that are inherited factor-by-factor.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact#Legal Operations|the topic page]]:

1. **Pull back a property from a single factor via a projection.** Given a property in $X_{\alpha_0}$ (a pair of disjoint opens), pull back via $\pi_{\alpha_0}^{-1}$ to a property in the product (a pair of disjoint cylinders). Continuity of projections makes the preimages open; the set-theoretic identity $\pi^{-1}(U) \cap \pi^{-1}(V) = \pi^{-1}(U \cap V)$ preserves disjointness.

2. **Reduce a multi-coordinate statement to a single coordinate.** Since distinct points of the product differ in at least one coordinate, any single-coordinate-witnessed property of the factors lifts to the product.

---

# Hints

> [!note]- Hint 1
> Two distinct points $x = (x_\alpha)$ and $y = (y_\alpha)$ in the product differ in *at least one* coordinate. Find one such coordinate and do all of your work there.

> [!note]- Hint 2
> Pick $\alpha_0$ with $x_{\alpha_0} \neq y_{\alpha_0}$, then use Hausdorffness of $X_{\alpha_0}$ to get disjoint opens $U_0 \ni x_{\alpha_0}$, $V_0 \ni y_{\alpha_0}$ in $X_{\alpha_0}$.

> [!note]- Hint 3
> The pullbacks $\pi_{\alpha_0}^{-1}(U_0)$ and $\pi_{\alpha_0}^{-1}(V_0)$ are open cylinders in the product, contain $x$ and $y$ respectively, and are disjoint because preimages preserve disjointness.

---

# Solution

Two distinct points in the product disagree in some coordinate; Hausdorffness in that coordinate gives disjoint open neighborhoods there; pulling them back via the projection produces disjoint open cylinders separating the points in the product.

**Step 1: Distinct points in the product differ in some coordinate.**

Suppose $x = (x_\alpha)_{\alpha \in A}$ and $y = (y_\alpha)_{\alpha \in A}$ are distinct points of $\prod_\alpha X_\alpha$. Then there exists $\alpha_0 \in A$ with $x_{\alpha_0} \neq y_{\alpha_0}$.

> [!note]- Derivation
> Tuples are equal precisely when they agree in every coordinate. So $x \neq y$ in the product means $\{x_\alpha\}_\alpha$ and $\{y_\alpha\}_\alpha$ disagree on at least one index — fix one such index and call it $\alpha_0$. This step is purely set-theoretic: no topology has been used yet. We have transferred the problem from the product to a single factor.

**Step 2: Separate the disagreeing coordinate by disjoint opens in $X_{\alpha_0}$.**

By the **Hausdorff** property of $X_{\alpha_0}$, there exist open sets $U_0, V_0 \subseteq X_{\alpha_0}$ with $x_{\alpha_0} \in U_0$, $y_{\alpha_0} \in V_0$, and $U_0 \cap V_0 = \emptyset$.

> [!note]- Derivation
> This is the *direct application* of the Hausdorff hypothesis on $X_{\alpha_0}$: distinct points $x_{\alpha_0} \neq y_{\alpha_0}$ get separated by disjoint opens. The whole proof would collapse if the factor were not Hausdorff — and indeed, products of non-Hausdorff spaces need not be Hausdorff.

**Step 3: Pull back to disjoint open neighborhoods in the product.**

Set $U = \pi_{\alpha_0}^{-1}(U_0)$ and $V = \pi_{\alpha_0}^{-1}(V_0)$. Then $U$ and $V$ are open in the product, contain $x$ and $y$ respectively, and are disjoint.

> [!note]- Derivation
> *Openness.* $U_0$ is open in $X_{\alpha_0}$ and the projection $\pi_{\alpha_0}$ is continuous (one of the defining properties of the [[Def - Product Topology|product topology]]). So $U = \pi_{\alpha_0}^{-1}(U_0)$ is open in the product; the same for $V$. Explicitly, $U$ is the cylinder $\prod_\alpha W_\alpha$ with $W_{\alpha_0} = U_0$ and $W_\alpha = X_\alpha$ for $\alpha \neq \alpha_0$ — a basic open set in the product topology.
>
> *Containment.* $x \in U$ because $\pi_{\alpha_0}(x) = x_{\alpha_0} \in U_0$; similarly $y \in V$.
>
> *Disjointness.* Preimages preserve set operations:
> $$U \cap V = \pi_{\alpha_0}^{-1}(U_0) \cap \pi_{\alpha_0}^{-1}(V_0) = \pi_{\alpha_0}^{-1}(U_0 \cap V_0) = \pi_{\alpha_0}^{-1}(\emptyset) = \emptyset.$$
> This single identity is what makes "separate in one factor and pull back" work as a proof technique throughout the theory of product spaces.

> [!note]- Complete formal solution
> Let $x = (x_\alpha) \neq y = (y_\alpha)$ in $\prod_\alpha X_\alpha$. Pick $\alpha_0 \in A$ with $x_{\alpha_0} \neq y_{\alpha_0}$. By Hausdorffness of $X_{\alpha_0}$, choose disjoint open $U_0, V_0 \subseteq X_{\alpha_0}$ with $x_{\alpha_0} \in U_0$, $y_{\alpha_0} \in V_0$. The cylinders $U = \pi_{\alpha_0}^{-1}(U_0)$, $V = \pi_{\alpha_0}^{-1}(V_0)$ are open in the product (continuity of $\pi_{\alpha_0}$), contain $x$ and $y$ respectively, and $U \cap V = \pi_{\alpha_0}^{-1}(U_0 \cap V_0) = \emptyset$. So the product is Hausdorff. $\blacksquare$

---

# Key Takeaways

**Hausdorffness — and more generally any single-coordinate separation property — is inherited by arbitrary products.** The same proof shows that products of regular, completely regular, or $T_1$ spaces are regular, completely regular, $T_1$ respectively. The mechanism in every case is identical: a separation between points (or between a point and a closed set) in one factor lifts to a separation in the product via $\pi^{-1}$. The structural reason is that the product topology is *exactly* coarse enough for projections to be continuous, hence cylinders are open, hence single-coordinate separations always lift. Normality, by contrast, is *not* inherited by arbitrary products — that involves separating two closed sets, each of which can spread across many coordinates simultaneously, and the single-coordinate move fails.

**The trigger-reaction pattern: "property of all factors $X_\alpha$ ⇒ property of product?" — try the single-coordinate reduction.** If the property is witnessed by a finite amount of data in one coordinate (separating points, $T_1$, regular, completely regular, first countability when the index set is countable), it lifts. If it requires data spread across many coordinates, it may not. This is one of the cleanest examples in topology of a structural argument: reduce to a single factor, exploit the hypothesis there, and use the projection's continuity to lift the result back. The compactness of products is a striking exception — Tychonoff's theorem ([[Thm - Tychonoff Theorem]]) shows that the global property of compactness *also* lifts, but the proof is much harder and uses universal nets or ultrafilters because compactness is not a "single-coordinate witnessed" property.

**The set-theoretic identity $\pi^{-1}(U) \cap \pi^{-1}(V) = \pi^{-1}(U \cap V)$ is the workhorse.** This identity, together with the continuity of projections, is what lets disjointness in a factor be pulled back to disjointness in the product. It deserves to be internalized as a mental reflex: any time you have a continuous map and a set-theoretic relation between subsets of the target, the relation is preserved by preimage. Disjointness is preserved, intersections are preserved, complements are preserved, but *images* of these operations are not, which is why the "$\pi^{-1}$ direction" is the safe direction for these arguments.
