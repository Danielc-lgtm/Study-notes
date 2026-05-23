---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Coordinate Chart and Atlas"
  - "Def - Smooth Atlas and Smooth Structure"
tags: [geometry, differential-geometry]
---

# Notation

$M$ denotes a smooth manifold of dimension $m$ — a topological space (Hausdorff, second-countable) carrying a maximal smooth atlas (see [[Def - Smooth Manifold]]). A **smooth chart** $(U, \varphi)$ consists of an open $U \subseteq M$ and a homeomorphism $\varphi : U \to \widetilde U$ onto an open subset $\widetilde U \subseteq \mathbb{R}^m$, with $\varphi$ belonging to the smooth structure. For a function $f : M \to \mathbb{R}$, the **coordinate representation** in the chart $(U, \varphi)$ is $\widehat f = f \circ \varphi^{-1} : \widetilde U \to \mathbb{R}$. The full registry lives on [[Differential Geometry II — Smooth Maps and Partitions of Unity]].

---

# Axiom Motivation

We want to declare a real-valued function $f : M \to \mathbb{R}$ on a smooth manifold to be **smooth**. The difficulty is that we have no calculus on $M$ itself — $M$ is a topological space with extra structure, but partial derivatives, Taylor expansions, and even ordinary differentiation are not defined on it. What we do have is a Euclidean model of the manifold near every point: a chart $\varphi : U \to \widetilde U \subseteq \mathbb{R}^m$, on $\widetilde U$ we have all the calculus we want. So the only natural way to declare $f$ to be smooth is to demand that its appearance through the chart — the function $\widehat f = f \circ \varphi^{-1} : \widetilde U \to \mathbb{R}$ — be smooth in the ordinary Euclidean sense.

This is the entire idea. The remaining question is whether the answer depends on the chart we picked. We have, after all, many charts at any point $p \in M$, and a definition that gives different answers in different charts would be useless. The chart-independence of the definition is precisely what the smooth-atlas axiom of [[Def - Smooth Atlas and Smooth Structure]] is there to guarantee.

Here is the calculation. Suppose $\widehat f = f \circ \varphi^{-1}$ is smooth in the chart $(U, \varphi)$ at $\varphi(p)$, and let $(U', \varphi')$ be another smooth chart with $p \in U'$. We want to know whether $f \circ \varphi'^{-1}$ is smooth at $\varphi'(p)$. Write
$$f \circ \varphi'^{-1} = (f \circ \varphi^{-1}) \circ (\varphi \circ \varphi'^{-1}).$$
The first factor is smooth by assumption, the second factor is the **transition map** $\varphi \circ \varphi'^{-1}$ — and the smooth-atlas axiom is *exactly* the statement that all transition maps are smooth [[Def - Diffeomorphism|diffeomorphisms]] between Euclidean open sets. So $f \circ \varphi'^{-1}$ is the composition of two smooth Euclidean maps, hence smooth. The answer does not depend on the chart. *This calculation is the engine of every manifold-level definition by chart-pullback*, and the reason the smooth-atlas axiom is the axiom of choice for smooth manifold theory: it is what makes the chart-pulling-back construction well-defined.

Could we have defined smoothness directly, without reference to charts? In principle one could try — for instance, demand that $f$ have continuous derivatives along every smooth curve through $p$. But "smooth curve" itself is a chart-pulled-back concept, so this is circular. Or: declare $f$ smooth if there is some open cover of $M$ in which $f$ restricts to a smooth function on each open set. But "smooth on an open set" is again a chart-level concept. *There is no calculus prior to charts*; charts are how the calculus on Euclidean space transfers to the manifold. The definition by chart-pullback is therefore forced.

A subtle point: the definition demands smoothness *at one* chart, and the chart-independence calculation upgrades this to smoothness *in every* compatible chart. So the verifier may use whichever chart is convenient — typically the chart in which $f$ has the simplest coordinate expression — and the user of $f$'s smoothness may assume any chart at all. This asymmetry between verification (one chart) and use (every chart) is part of what makes the manifold-level definition usable: you do not have to check smoothness in every chart, only in one.

Finally, why $C^\infty$ (infinitely differentiable) rather than $C^k$ for some finite $k$? Lee's convention, which we follow, is that "smooth" means $C^\infty$ throughout. The reason is that intersections of $C^k$ structures with $C^\infty$ are usually $C^\infty$ — and the smooth category is closed under all the operations we want (composition, inverses, products), whereas $C^k$ categories have annoying boundary effects (the composition of two $C^k$ maps is $C^k$ but the differential drops a degree of regularity). For most theorems we will encounter, the regularity threshold is far below $C^\infty$; we choose $C^\infty$ for technical convenience, not because anything genuinely requires it.

---

# The Definition

Let $M$ be a smooth manifold. A function $f : M \to \mathbb{R}$ is **smooth at a point $p \in M$** if there exists a smooth chart $(U, \varphi)$ on $M$ with $p \in U$ such that the coordinate representation
$$\widehat f = f \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}$$
is smooth in the Euclidean sense (i.e. $C^\infty$) at $\varphi(p)$.

The function $f$ is **smooth on $M$** if it is smooth at every point of $M$.

The set of all smooth functions $M \to \mathbb{R}$ is denoted $C^\infty(M)$. It is a commutative $\mathbb{R}$-algebra under pointwise operations; see [[Def - The Smooth Functions Ring]].

**Equivalent formulation.** The function $f$ is smooth on $M$ if and only if for every smooth chart $(U, \varphi)$ on $M$ (in particular, every chart in the maximal atlas), the function $f \circ \varphi^{-1} : \varphi(U) \to \mathbb{R}$ is smooth in the Euclidean sense. (The non-trivial direction is the upgrade from "exists one chart" to "every chart"; the proof is the transition-map calculation in the Axiom Motivation.)

A function $f$ is **smooth on an open set $U \subseteq M$** if its restriction $f|_U$ is smooth, viewing $U$ as an open submanifold with the induced smooth structure.

---

# Categorical Definition

A smooth manifold $M$ comes with a **sheaf of smooth functions** $\mathcal{O}_M$: to each open $U \subseteq M$ we assign the $\mathbb{R}$-algebra $\mathcal{O}_M(U) = C^\infty(U)$, and restriction is just the usual restriction of functions. *Smoothness* of a function $f : M \to \mathbb{R}$ is then the statement that $f$ is a *global section* of this sheaf: $f \in \mathcal{O}_M(M) = C^\infty(M)$.

The sheaf axioms — locality (a function smooth on each member of an open cover is smooth globally) and gluing (compatible smooth local sections glue to a global smooth section) — are immediate from the chart definition: smoothness is checked at each point in a chart, and a function smooth in a chart neighbourhood of every point is smooth.

The pair $(M, \mathcal{O}_M)$ is a **ringed space**, and the entire category of smooth manifolds embeds as a full subcategory of ringed spaces. Under this embedding, a continuous $F : M \to N$ is a smooth map iff the induced pullback $F^* : \mathcal{O}_N \to F_* \mathcal{O}_M$ takes smooth sections to smooth sections — concretely, $g \in C^\infty(N) \Rightarrow g \circ F \in C^\infty(M)$. So *smoothness is the morphism condition in the category of ringed spaces with structure sheaf $\mathcal{O}^\infty$*. This is the conceptual content of Lee's Problem 2-10.

---

# Relate to Other Fields / Compression

The definition is **the prototype of "manifold-level concept by chart-pullback"**. Every concept defined for smooth manifolds — smooth maps, tangent vectors, differentials, vector fields, differential forms — uses the same template: declare the concept by demanding that its coordinate representation, in some chart, satisfy the Euclidean version of the concept; check chart-independence using the smooth-atlas axiom. So this definition is not just *a* definition but *the template*.

The same construction gives **holomorphic functions** on a complex manifold (chart-representation is holomorphic in the Euclidean sense), **real-analytic functions** on an analytic manifold ($C^\omega$ chart-representation), **$C^k$ functions** on a $C^k$ manifold. The relevant category structures differ — analytic is rigid, smooth is flexible — but the manifold-level definition is uniformly chart-pullback. *This is literally the same construction as smoothness of a map between Euclidean open sets, specialized to the category of $C^\infty$ manifolds via charts.*

**True name:** *the smoothness of $f$ is the smoothness of every chart-representation $f \circ \varphi^{-1}$*. The official definition only demands one chart-representation be smooth; the operational meaning is that all of them are. This is the form you use when applying smoothness — pick the chart that makes the computation cleanest.

---

# Examples / Corollaries

**Is an instance: constant functions.** Every constant function $f \equiv c : M \to \mathbb{R}$ is smooth. In any chart, $\widehat f = c$ is the constant Euclidean function, which is smooth. (The smoothness is the only verification; this is the trivial case but also the base case for $C^\infty(M)$ containing $\mathbb{R}$ as a [[Def - Subring|subring]].)

**Is an instance: coordinate functions.** If $(U, \varphi)$ is a smooth chart with coordinate functions $\varphi^i : U \to \mathbb{R}$ ($i = 1, \ldots, m$), then each $\varphi^i$ is smooth on $U$ (and extends by zero outside, multiplied by a bump, to a smooth function on $M$). In the chart $\varphi$, $\widehat{\varphi^i}(x) = x^i$, the $i$th Euclidean projection — manifestly smooth. Coordinate functions are the prototype of "smooth function locally available in every chart".

**Is an instance: smooth functions on $\mathbb{R}^n$.** The manifold $\mathbb{R}^n$ has a single global chart (the identity), so a function $f : \mathbb{R}^n \to \mathbb{R}$ is smooth in the manifold sense if and only if it is smooth in the ordinary Euclidean sense. The manifold-level definition reduces to the Euclidean one when $M$ is itself Euclidean — and this is the reason the manifold definition deserves to be called "smoothness".

**Is an instance: composing a smooth function with a smooth map.** If $F : M \to N$ is a smooth map and $g : N \to \mathbb{R}$ is smooth, then $g \circ F : M \to \mathbb{R}$ is smooth. This is the *pullback* operation, and verifying it is a chart computation: pick charts $(U, \varphi)$ on $M$ and $(V, \psi)$ on $N$ with $F(U) \subseteq V$; then $\widehat{g \circ F} = \widehat g \circ \widehat F$ is the composition of two smooth Euclidean maps.

**Is NOT an instance: the function $f : \mathbb{R} \to \mathbb{R}$, $f(x) = |x|$.** Absolute value is continuous on $\mathbb{R}$ but not smooth at $0$, since its derivative does not exist at $0$. In the standard chart (the identity), the coordinate representation is $|x|$, which is not smooth in the Euclidean sense. This is the standard non-example: a continuous function whose only failure of smoothness is at a single point.

**Is NOT an instance: a function defined chart-by-chart that fails to glue smoothly.** Consider $M = S^1$, the unit circle, with stereographic charts from the north and south poles. Suppose we define $f$ on each chart to be the identity in chart coordinates. The two coordinate expressions look smooth, but the transition between charts is $x \mapsto 1/x$, and the function defined this way may fail to glue continuously, let alone smoothly. The chart-pulling-back construction must respect the transition functions; not every assignment "smooth in each chart" arises from a globally defined function.

**Corollary (smoothness is local).** A function $f : M \to \mathbb{R}$ is smooth if and only if it is smooth in a neighbourhood of each point. Both directions are immediate from the definition — smoothness at $p$ depends only on $f$'s values in a chart around $p$, which is a neighbourhood. This is the sheaf locality axiom.

**Corollary (smooth functions form an algebra).** If $f, g \in C^\infty(M)$ and $\lambda \in \mathbb{R}$, then $f + g$, $fg$, and $\lambda f$ are all in $C^\infty(M)$. In any chart, $\widehat{f + g} = \widehat f + \widehat g$, $\widehat{fg} = \widehat f \cdot \widehat g$, $\widehat{\lambda f} = \lambda \widehat f$ — and sums, products, and scalar multiples of smooth Euclidean functions are smooth. See [[Def - The Smooth Functions Ring]] for the full algebra structure.

**Corollary (composition).** If $f \in C^\infty(M)$ and $\eta \in C^\infty(\mathbb{R})$, then $\eta \circ f \in C^\infty(M)$. This is a special case of pullback by a smooth map; routine verification.

**Calibration check.** Verify the following: (i) the function $f : \mathbb{R}^2 \to \mathbb{R}$, $f(x, y) = e^{xy}$ is smooth — write the coordinate representation in the identity chart and observe it is smooth in the Euclidean sense. (ii) On $S^1 \subseteq \mathbb{R}^2$, the function "first coordinate" $f(x, y) = x$ is smooth — in stereographic coordinates from the north pole, $f(\widetilde x) = (2\widetilde x)/(1 + \widetilde x^2)$, smooth as a rational function with non-vanishing denominator. (iii) On any smooth manifold, the constant function $1$ is smooth, and any sum or product of smooth functions is smooth.

---

# Unlocked by This

> [!tip] The Algebra $C^\infty(M)$ *(from Algebraic Geometry / Ringed Spaces)*
> Once smooth functions are defined, $C^\infty(M)$ becomes an $\mathbb{R}$-algebra under pointwise operations. This is the algebraic incarnation of the smooth manifold, and (by Lee Problem 2-10) the smooth structure is recoverable from this algebra. See [[Def - The Smooth Functions Ring]] for the full algebraic structure and the ringed-space viewpoint.

> [!tip] Tangent Vectors as Derivations *(from Differential Geometry)*
> A **tangent vector at $p$** can be defined as an $\mathbb{R}$-linear map $v : C^\infty(M) \to \mathbb{R}$ satisfying the Leibniz rule $v(fg) = v(f)g(p) + f(p)v(g)$ — a *derivation at $p$* of the algebra $C^\infty(M)$. This is one of three equivalent definitions of the tangent space and is the operationally cleanest one. Developed in [[Differential Geometry III — Tangent Vectors and the Differential|DG III]].

> [!tip] Smooth Vector Fields *(from Differential Geometry)*
> A **smooth vector field** on $M$ is, equivalently, a derivation of $C^\infty(M)$ as an $\mathbb{R}$-algebra: an $\mathbb{R}$-linear map $X : C^\infty(M) \to C^\infty(M)$ satisfying $X(fg) = X(f)g + fX(g)$. The Lie bracket of vector fields is then literally the commutator of derivations. Developed in [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket|DG V]].
