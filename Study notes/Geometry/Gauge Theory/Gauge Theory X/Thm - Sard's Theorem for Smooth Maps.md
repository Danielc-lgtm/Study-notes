---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Set of Measure Zero on a Manifold"
  - "Def - Regular and Critical Points"
  - "Def - Smooth Manifold"
  - "Thm - Heine–Borel Theorem"
  - "Thm - Taylor's Theorem in Several Variables"
  - "Thm - The Mean Value Inequality"
  - "Def - First and Second Countable"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $m$ and $n$ are positive integers, $U \subseteq \mathbb{R}^m$ is an open set, and $f : U \to \mathbb{R}^n$ is a smooth ($C^\infty$) map with component functions $f = (f_1, \dots, f_n)$. The differential of $f$ at a point $x \in U$ is the linear map $df_x : \mathbb{R}^m \to \mathbb{R}^n$ represented by the Jacobian matrix $\big(\partial_i f_j(x)\big)_{j,i}$, where $\partial_i = \partial/\partial x_i$. A point $x$ is a **critical point** of $f$ when $df_x$ fails to be surjective, that is, when $\operatorname{rank} df_x < n$; the set of critical points is $\operatorname{Crit}(f)$, and its image $f(\operatorname{Crit}(f)) \subseteq \mathbb{R}^n$ is the set of **critical values**. A value that is not critical is **regular** (see [[Def - Regular and Critical Points]]).

We use multi-index notation: for $\alpha = (\alpha_1, \dots, \alpha_m) \in \mathbb{N}^m$ we write $|\alpha| = \alpha_1 + \cdots + \alpha_m$, $\alpha! = \alpha_1! \cdots \alpha_m!$, $h^\alpha = h_1^{\alpha_1} \cdots h_m^{\alpha_m}$ for $h \in \mathbb{R}^m$, and $\partial^\alpha = \partial_1^{\alpha_1} \cdots \partial_m^{\alpha_m}$. The Euclidean norm is $\lVert \cdot \rVert$. A **cube** in $\mathbb{R}^p$ is a set of the form $\prod_{i=1}^{p} [a_i, a_i + s]$ with common side length $s > 0$; its $p$-dimensional volume is $s^p$.

**Measure zero.** A subset $A \subseteq \mathbb{R}^p$ has **Lebesgue measure zero** (is **null**) if for every $\delta > 0$ there is a countable collection of cubes covering $A$ whose total volume is less than $\delta$. For a subset of a manifold, "measure zero" is the chart-based notion of [[Def - Set of Measure Zero on a Manifold]]: $A \subseteq M$ has measure zero if $\varphi(A \cap U_\varphi)$ is null in $\mathbb{R}^m$ for the charts $(U_\varphi, \varphi)$ of some atlas covering $A$. We will use two elementary facts recorded there and reproved on this page as they are needed: a countable union of null sets is null, and a nonempty open subset of $\mathbb{R}^p$ is not null (so the complement of a null set is dense).

> [!warning] Convention: cubes, balls, rectangles
> The definition of "measure zero" is unchanged if "cubes" is replaced by "open cubes", "balls", or "axis-aligned rectangles": each shape of small volume is contained in a shape of another kind whose volume exceeds it only by a fixed dimensional constant, and multiplying every total by that constant does not affect whether the totals can be made arbitrarily small. We use closed cubes for the covering estimates and note the shape only where it matters.

> [!warning] Convention: this page proves what Haydys imports
> Haydys states Sard's theorem without proof, citing Bott–Tu [BT03, Thm 9.5.4], because his interest is the infinite-dimensional Sard–Smale theorem (Theorem 164), for which the finite-dimensional statement is a black box. Under the vault-wide proof standard the finite-dimensional Sard theorem is not imported: it is proved here in full, following Milnor (*Topology from the Differentiable Viewpoint*, §3, after Pontryagin), so that [[Thm - Sard-Smale Theorem|Sard–Smale]] rests on a proved base case. The reader may also consult Lee, *Introduction to Smooth Manifolds*, 2nd ed., Theorem 6.10, and Sternberg, *Lectures on Differential Geometry*, II.3, for the same argument.

The full symbol registry for this chapter lives on the parent page **Gauge Theory X — Fredholm Maps, Transversality, and Degree**.

---

# Statement

> **Sard's Theorem (Euclidean form).** Let $U \subseteq \mathbb{R}^m$ be open and $f : U \to \mathbb{R}^n$ smooth. Let
> $$\operatorname{Crit}(f) = \{\, x \in U : df_x \text{ is not surjective} \,\} = \{\, x \in U : \operatorname{rank} df_x < n \,\}.$$
> Then the set of critical values $f(\operatorname{Crit}(f))$ has Lebesgue measure zero in $\mathbb{R}^n$.

> **Sard's Theorem (manifold form).** Let $f : M \to N$ be a smooth map between smooth manifolds, with $M$ second countable and $\dim N = n$. Then the set of critical values of $f$ has measure zero in $N$. Consequently the set of regular values of $f$ is dense in $N$: every nonempty open subset of $N$ contains a regular value.

The manifold form is deduced from the Euclidean form by covering $M$ and $N$ with countably many charts; the second countability of $M$ is exactly what makes "countably many" possible. The density of regular values then follows because a set of measure zero has dense complement. We prove the Euclidean form first and reduce the manifold form to it in the final step of the formal proof.

---

# Motivation

The [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] is the standard machine for producing submanifolds: if $c$ is a regular value of a smooth map $f : M \to N$, then $f^{-1}(c)$ is an embedded submanifold of $M$ of dimension $\dim M - \dim N$, with tangent space $\ker df_x$ at each point. The machine is useless, however, unless regular values exist. One might hope that regularity is generic, but nothing in the definition guarantees even a single regular value: a priori every value could be critical. Sard's theorem is the statement that this fear is unfounded — the critical values are confined to a set of measure zero, so regular values are not merely present but dense, and one may perturb any chosen value by an arbitrarily small amount to land on a regular one.

This single density statement is the quiet engine beneath a striking amount of differential topology and geometric analysis. Transversality — the condition that lets one intersect submanifolds cleanly and count intersections — is generic precisely because the failure of transversality is the criticality of an auxiliary map, and Sard makes criticality rare. The mapping degree, the signed count of preimages of a regular value, is well defined only because regular values exist and the count is independent of which one is chosen. The Whitney embedding and immersion theorems project a manifold generically into Euclidean space, avoiding a measure-zero set of bad directions supplied by Sard. Morse functions — smooth functions whose critical points are all nondegenerate — are generic by a Sard-type argument applied to the differential. And in the infinite-dimensional world that this chapter is building toward, the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]] extends Sard's conclusion to Fredholm maps between Banach manifolds by reducing, in Kuranishi charts, to the finite-dimensional statement proved here; that extension is what makes the moduli spaces of Seiberg–Witten and Donaldson theory generically smooth.

There is a second reason to prove the theorem rather than cite it. The mechanism of the proof — the filtration of the critical set by the order to which the map is flat, the Taylor estimate on the flattest part, and the dimensional induction on the rest — is itself the model for every later genericity argument in the chapter, most directly the slice-by-slice application of Sard inside the proof of Sard–Smale. Seeing the finite-dimensional argument in full is the best preparation for its infinite-dimensional descendant.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is mild — any smooth map between open sets, or between second-countable manifolds, qualifies — so the useful question is which apparently different situations secretly present a smooth map to which Sard applies.

The first disguised source is **a map of merely finite smoothness $C^r$**. The proof never differentiates $f$ more than $k+1$ times, where $k$ is the least integer with $(k+1)n > m$; consequently the conclusion holds already for $f \in C^r$ with $r \ge \max(1,\, m-n+1)$. This is the sharp regularity of Sard's theorem, and it is not a technicality: it is exactly the hypothesis Smale needs for the Sard–Smale theorem, where the relevant Fredholm map is only required to be $C^q$ with $q > \max(\operatorname{index} F, 0)$. The bridge $B \Rightarrow A$ is "finitely differentiable with $r \ge m-n+1$ implies the Taylor estimate to order $k+1$ is available," and the non-obvious part is that no higher derivative is ever used. *Example problem:* show that a $C^2$ map $f : \mathbb{R}^3 \to \mathbb{R}^2$ has critical values of measure zero even though $f$ is not smooth, by tracking the derivative order used in each step.

The second disguised source is **a smooth family of maps**. A parametrised map $F : U \times W \to \mathbb{R}^n$, smooth jointly in the point and the parameter, is itself a single smooth map on the product, so Sard applies to $F$ and produces a regular value $y$ of $F$; the parametric transversality argument then converts "regular value of the total map" into "regular value of $F(\cdot, w)$ for almost every parameter $w$." The bridge is that joint smoothness makes the parametrised object one map on a larger domain, and the non-obvious step is the passage from the total map's regular value to the individual maps' regular values via the projection of the universal zero set. *Example problem:* given $F(x,w) = g(x) - w$ with $g$ smooth, deduce from Sard applied to $F$ that almost every $w$ is a regular value of $g$; recognise this as the proof of [[Thm - Parametric Transversality|parametric transversality]] in miniature.

The third disguised source is **a genericity question with no visible connection to critical values**. Many statements of the form "the generic object has property $P$" are proved by exhibiting a smooth map whose regular values are exactly the objects with property $P$, and then invoking Sard. The classic instance is Morse functions: for a fixed function $f$ on a manifold, the functions $f_a(x) = f(x) - a \cdot x$ (in a chart) are Morse for almost every $a$, because the nondegeneracy of a critical point of $f_a$ is the regularity of $a$ as a value of the gradient map $x \mapsto \nabla f(x)$. The bridge is "property $P$ fails exactly on the critical values of an auxiliary smooth map," and the non-obvious step is the construction of that auxiliary map. *Example problem:* show that for almost every $a \in \mathbb{R}^n$ the function $x \mapsto \lvert x - a \rvert^2$ on a submanifold $M \subseteq \mathbb{R}^n$ is Morse, by applying Sard to the endpoint map of the normal bundle.

**Targets (Output Amplification)**

Combine Sard with **the regular value theorem**. Sard supplies a dense set of regular values $c$; the [[Thm - Regular Value Theorem on Manifolds|regular value theorem]] then makes each $f^{-1}(c)$ an embedded submanifold of dimension $\dim M - \dim N$. The extra ingredient is the implicit function theorem inside the regular value theorem, and the payoff is a manufacturing device for submanifolds of controlled dimension: whenever one needs a submanifold cut out by equations, Sard guarantees the equations can be perturbed to a regular level.

Combine Sard with **properness and a parity argument**. For a proper map of index zero, a regular value has a finite preimage; Sard makes such values dense, and a cobordism argument along a path of regular values shows the parity of the count is independent of the value. The extra ingredient is properness (compact preimages) plus the classification of compact one-manifolds, and the payoff is the well-defined [[Def - Mod-2 Degree of a Proper Fredholm Map|mod-2 degree]] and, with orientations, the integer degree.

Combine Sard with **the Kuranishi model for a Fredholm map**. In a Kuranishi chart an infinite-dimensional Fredholm map is a linear isomorphism in the cokernel-complement directions plus a finite-dimensional map on the kernel; applying the finite-dimensional Sard theorem slice by slice, and using local properness to convert "null in every slice" into "nowhere dense," yields the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]]. The extra ingredient is the reduction to finite dimensions supplied by the Fredholm property, and the payoff is genericity in infinite-dimensional variational problems, which is the working hypothesis of gauge theory.

Combine Sard with **a dimension count that leaves a value uncovered**. If $\dim M < \dim N$ then every point of $M$ is critical and Sard says $f(M)$ has measure zero, so $f$ misses a point of $N$; when $N$ is a sphere, a smooth map missing a point is null-homotopic, giving $\pi_k(S^m) = 0$ for $k < m$ (developed in the homotopy chapter, **chapter XII**). The extra ingredient is that a map into a punctured sphere contracts, and the payoff is the vanishing of low homotopy groups of spheres from a pure measure argument.

---

# Why Is It True

Forget the induction for a moment and picture the two extreme kinds of critical point. At a point where the differential has rank exactly $n-1$ — the mildest possible failure of surjectivity — the map still spreads the domain out in $n-1$ independent directions and only collapses one. Its image near such a point is a hypersurface-like piece: $(n-1)$-dimensional to first order, hence thin in $\mathbb{R}^n$, yet not evidently of measure zero, because a hypersurface swept out over a range of the missing direction could in principle fill volume. At the opposite extreme sits a point where every derivative up to high order vanishes — the map is extraordinarily flat there — and near such a point the image is genuinely tiny, because a flat map cannot move points far.

The proof organises the critical set between these extremes by a filtration: $C_1 \supseteq C_2 \supseteq \cdots$, where $C_i$ is the set of points at which all partial derivatives of $f$ up to order $i$ vanish. The flattest part $C_k$, with $k$ large enough that $(k+1)n > m$, is handled by the elementary end of the argument: Taylor's theorem says a map that is flat to order $k$ moves a point by no more than a constant times the $(k+1)$-st power of the displacement, so a small cube of side $s$ has image inside a cube of side of order $s^{k+1}$; subdividing a fixed cube into $r^m$ pieces and adding up the tiny image volumes gives a total of order $r^{m - (k+1)n}$, which tends to zero precisely because $(k+1)n > m$. This is where the numerical threshold comes from — one must be flat enough that the image shrinks faster than the number of pieces grows.

Everything between the flattest part and the full critical set is reduced to a lower-dimensional Sard theorem by induction. On the shallowly critical part $C \setminus C_1$, some first derivative is nonzero, so one coordinate of the map (or an auxiliary function) can be promoted to a coordinate of the domain; in these coordinates the map preserves the level hyperplanes, and its restriction to each hyperplane is a map in one fewer dimension whose critical values are null by the inductive hypothesis. A Fubini-type lemma then upgrades "null in every hyperplane slice" to "null in the whole space." The successive strata $C_i \setminus C_{i+1}$ are handled the same way, using a derivative of order $i$ as the promoted coordinate.

**The one-sentence mechanism: a critical point collapses at least one direction, and the flatter the map the more it collapses, so the deeply-flat set has a demonstrably tiny image by Taylor's estimate while the shallowly-critical set is thinned one dimension at a time by induction and a Fubini slice argument.** The threshold $(k+1)n > m$ is the exact accounting that makes the shrinking images beat the growing count of cubes.

---

# What Makes This Hard

The genuinely non-obvious idea is the filtration of the critical set by order of flatness, together with the realisation that the shallowly-critical part $C \setminus C_1$ — where the differential is only mildly degenerate — is the *hard* part, not the easy one. A first reading expects rank-deficiency alone to force the image to be measure zero, but it does not: a rank-$(n-1)$ map can locally sweep an $(n-1)$-dimensional sheet across the missing direction, and only the inductive slice argument, resting on the Fubini-type lemma, rules out that the sheets accumulate into positive volume. The deeply-flat part, by contrast, is the *easy* part, dispatched by a one-line Taylor estimate once the threshold $(k+1)n > m$ is arranged. The common error is to attempt the whole theorem by the Taylor estimate, which fails on $C \setminus C_1$ because there the map is not flat and the estimate gives no shrinkage; the second common error is to forget that the Fubini lemma needs the set to be compact (or measurable) before "null in every slice" is allowed to imply "null," which is why the proof restricts to compact cubes before slicing.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove the Euclidean statement by induction on the domain dimension $m$ (all target dimensions $n$ at once). Split the critical set $C = \operatorname{Crit}(f)$ into the shallowly-critical part $C \setminus C_1$, the intermediate strata $C_i \setminus C_{i+1}$, and the deeply-flat part $C_k$ for the least $k$ with $(k+1)n > m$, where $C_i$ is the set on which all partials of order $\le i$ vanish. Show each piece has null image and take the finite union. Deduce the manifold statement by a countable atlas.

**Subgoal decomposition:**

1. **Null sets are stable under $C^1$ maps in equal dimension.** Show a $C^1$ map between open subsets of $\mathbb{R}^p$ carries null sets to null sets.
   - *Hint:* Exhaust the domain by compact convex cubes; on each, the map is Lipschitz by the mean value inequality, and a Lipschitz map inflates the covering volume by only a fixed factor.
   - *Why needed:* It makes "measure zero" a coordinate-free notion, licensing the change of variables in Steps 3–4 and the atlas argument for the manifold form.

2. **A Fubini-type slice lemma.** Show a compact set in $\mathbb{R}^n$ that meets every hyperplane $\{x_1 = c\}$ in an $(n-1)$-null set is itself null.
   - *Hint:* Cover each compact slice by finitely many open cubes of small total $(n-1)$-volume, thicken in the $x_1$-direction by a tube-lemma argument, and integrate the slice volume over a bounded range of $c$.
   - *Why needed:* It converts "the image is null in every hyperplane" (obtained from the inductive hypothesis) into "the image is null."

3. **The shallowly-critical set $C \setminus C_1$.** Near a point where some first partial is nonzero, change coordinates so that $f$ preserves the level hyperplanes; the restriction to each hyperplane is a lower-dimensional map whose critical values are null by induction. Apply the slice lemma.
   - *Hint:* Use $h(x) = (f_1(x), x_2, \dots, x_m)$ as a local diffeomorphism when $\partial_1 f_1 \ne 0$; then $g = f \circ h^{-1}$ carries $\{t\} \times \mathbb{R}^{m-1}$ into $\{t\} \times \mathbb{R}^{n-1}$.
   - *Why needed:* It is the base of the dimensional reduction; without it the mildly degenerate points are uncontrolled.

4. **The strata $C_i \setminus C_{i+1}$, $i \ge 1$.** Near such a point some $(i+1)$-st partial is nonzero; use an $i$-th partial as an auxiliary coordinate to push $C_i$ into a hyperplane of the domain, restrict, and induct.
   - *Hint:* If $w = \partial^\beta f_j$ with $|\beta| = i$ satisfies $\partial_1 w(x) \ne 0$, set $h(x) = (w(x), x_2, \dots, x_m)$; then $C_i$ maps into $\{0\} \times \mathbb{R}^{m-1}$ and $df = 0$ on $C_i$ makes the restricted map critical there.
   - *Why needed:* It fills the gap between the shallowly-critical set and the deeply-flat set.

5. **The deeply-flat set $C_k$.** With $(k+1)n > m$, Taylor's theorem gives $\lVert f(x+h) - f(x) \rVert \le c\lVert h \rVert^{k+1}$ for $x \in C_k$; a subdivided cube then has image of total volume tending to zero.
   - *Hint:* Split a fixed cube into $r^m$ subcubes of side $\to 0$; each meeting $C_k$ has image in a cube of side $\lesssim r^{-(k+1)}$; total volume $\lesssim r^{m-(k+1)n} \to 0$.
   - *Why needed:* It closes the induction, since the strata terminate at $C_k$.

6. **Assemble and pass to manifolds.** Take the finite union of the null images; then cover $M$ by countably many charts (second countability) and use the coordinate-free notion of null from Step 1.
   - *Hint:* Regularity is preserved by the chart diffeomorphisms (chain rule), and a countable union of null sets is null; density of regular values follows because a null set has empty interior.
   - *Why needed:* It produces the two statements as written.

---

# Lemma Decomposition

> [!note]- Lemma 1: A $C^1$ map in equal dimension carries null sets to null sets
> **Statement:** Let $V \subseteq \mathbb{R}^p$ be open, $g : V \to \mathbb{R}^p$ a $C^1$ map, and $A \subseteq V$ a set of Lebesgue measure zero. Then $g(A)$ has measure zero in $\mathbb{R}^p$.
>
> **Hint:** Write $V$ as a countable union of compact cubes; on each, $g$ is Lipschitz by the mean value inequality, and a Lipschitz map with constant $L$ carries a cube of side $s$ into a cube of side $L\sqrt{p}\,s$, inflating covering volume by the fixed factor $(L\sqrt{p})^p$.
>
> **Why needed:** It shows "measure zero" is invariant under diffeomorphisms, so the change of coordinates in Steps 3–4 does not disturb null images and the manifold notion of measure zero is well posed.
>
> > [!note]- Full proof
> > **Goal.** Given that $A$ is null, produce for each $\delta > 0$ a countable cube cover of $g(A)$ of total volume less than $\delta$.
> >
> > **Step 1 — exhaust the domain by compact cubes.** The open set $V$ is a countable union $V = \bigcup_{j \in \mathbb{N}} Q_j$ of closed cubes $Q_j \subseteq V$: for instance, take all closed cubes with rational vertices and rational side that are contained in $V$; there are countably many, and each point of the open set $V$ lies in the interior of one of them, so they cover $V$. It suffices to show $g(A \cap Q_j)$ is null for each $j$, because $g(A) = \bigcup_j g(A \cap Q_j)$ and a countable union of null sets is null (given covers of total volume $< \delta/2^{j+1}$ for the $j$-th set, their union is a cover of total volume $< \delta$).
> >
> > **Step 2 — Lipschitz bound on a compact cube.** Fix $j$ and write $Q = Q_j$. A closed cube is closed and bounded, hence compact by the [[Thm - Heine–Borel Theorem|Heine–Borel theorem]] — a subset of $\mathbb{R}^p$ is compact if and only if it is closed and bounded — and it is convex. The derivative $x \mapsto df_x$ is continuous (as $g$ is $C^1$), so $L := \sup_{x \in Q} \lVert dg_x \rVert$ is finite (a continuous function on a compact set is bounded). By the vector mean value inequality — for a differentiable map on an open set and a segment $[x,y]$ lying in the domain, $\lVert g(x) - g(y) \rVert \le \big(\sup_{\xi \in [x,y]} \lVert dg_\xi \rVert\big)\lVert x - y \rVert$, restated from [[Thm - The Mean Value Inequality]] — and using that $Q$ is convex so that every segment $[x,y]$ with $x,y \in Q$ lies in $Q$, we get
> > $$\lVert g(x) - g(y) \rVert \le L \lVert x - y \rVert \qquad \text{for all } x,y \in Q \quad \text{(mean value inequality; convexity of } Q \text{ puts the segment in } Q\text{)}.$$
> > Thus $g$ is $L$-Lipschitz on $Q$.
> >
> > **Step 3 — a Lipschitz map inflates covering volume by a fixed factor.** Since $A \cap Q$ is null, for any $\varepsilon > 0$ cover it by countably many cubes $R_1, R_2, \dots$ of sides $s_1, s_2, \dots$ and total volume $\sum_i s_i^p < \varepsilon$; replacing each $R_i$ by $R_i \cap Q$ and enlarging slightly we may assume each $R_i \subseteq Q$ (this only decreases sides). A cube $R_i$ of side $s_i$ has diameter $\sqrt{p}\, s_i$, so by the Lipschitz bound $g(R_i \cap Q)$ has diameter at most $L\sqrt{p}\, s_i$ and therefore lies in a cube $R_i'$ of side $L\sqrt{p}\, s_i$ (a set of diameter $d$ fits in a cube of side $d$). Then
> > $$\sum_i \operatorname{vol}(R_i') = \sum_i (L\sqrt{p}\, s_i)^p = (L\sqrt{p})^p \sum_i s_i^p < (L\sqrt{p})^p\, \varepsilon \qquad \text{(Lipschitz diameter bound; } \operatorname{vol} = \text{side}^p\text{)}.$$
> > As $\varepsilon > 0$ is arbitrary and $(L\sqrt{p})^p$ is a fixed constant, the cubes $R_i'$ cover $g(A \cap Q)$ with total volume as small as desired. Hence $g(A \cap Q)$ is null.
> >
> > **Conclusion.** Each $g(A \cap Q_j)$ is null, so their countable union $g(A)$ is null. $\blacksquare$

> [!note]- Lemma 2: Fubini-type slice lemma for compact sets
> **Statement:** Let $A \subseteq \mathbb{R}^n = \mathbb{R} \times \mathbb{R}^{n-1}$ (with coordinates written $(t, y)$, $t \in \mathbb{R}$, $y \in \mathbb{R}^{n-1}$) be compact, and suppose that for every $c \in \mathbb{R}$ the slice $A_c := \{\, y \in \mathbb{R}^{n-1} : (c,y) \in A \,\}$ has $(n-1)$-dimensional measure zero. Then $A$ has $n$-dimensional measure zero.
>
> **Hint:** Each slice is compact, hence covered by finitely many open cubes of small total $(n-1)$-volume; a tube-lemma argument thickens the cover to a slab $(c - \eta, c + \eta) \times V$; cover the bounded $t$-range by finitely many slabs and add up the volumes.
>
> **Why needed:** In Steps 3–4 the inductive hypothesis gives that the critical-value image is null in each hyperplane $\{t\} \times \mathbb{R}^{n-1}$; this lemma is what turns that slicewise nullity into nullity of the whole image.
>
> > [!note]- Full proof
> > **Goal.** Given that every slice $A_c$ is $(n-1)$-null, cover the compact set $A$ by cubes of total $n$-volume less than any prescribed $\delta > 0$.
> >
> > **Step 0 — the $t$-range is bounded.** Since $A$ is compact, its projection to the $t$-axis is a compact, hence bounded, subset of $\mathbb{R}$; choose a closed interval $[a,b]$ containing it, so $A \subseteq [a,b] \times \mathbb{R}^{n-1}$. Fix $\delta > 0$ and set $\varepsilon := \delta / (b - a)$ (if $b = a$ the set lies in one slice, which is null, and there is nothing to prove).
> >
> > **Step 1 — cover each slice by an open set of small volume.** Fix $c \in [a,b]$. The slice $A_c$ has $(n-1)$-measure zero, so it is covered by countably many open cubes in $\mathbb{R}^{n-1}$ of total volume less than $\varepsilon$. The slice $A_c$ is compact: it is the image of the compact set $A \cap (\{c\} \times \mathbb{R}^{n-1})$ (closed subset of the compact $A$) under the projection $(c,y) \mapsto y$, which is continuous. By compactness, finitely many of those open cubes suffice; let $V_c \subseteq \mathbb{R}^{n-1}$ be their union, an open set with
> > $$A_c \subseteq V_c, \qquad \operatorname{vol}_{n-1}(V_c) < \varepsilon \qquad \text{(finite subcover of a cover of total volume } < \varepsilon\text{)}.$$
> > Here $\operatorname{vol}_{n-1}(V_c)$ denotes the total volume of the finitely many covering cubes; it bounds the volume of $V_c$ and is what we carry forward.
> >
> > **Step 2 — thicken to a slab (tube lemma).** We claim there is $\eta_c > 0$ with
> > $$A \cap \big( (c - \eta_c,\, c + \eta_c) \times \mathbb{R}^{n-1} \big) \subseteq (c - \eta_c,\, c + \eta_c) \times V_c.$$
> > Consider the set $B := A \setminus (\mathbb{R} \times V_c)$. It is compact, being the intersection of the compact $A$ with the closed set $\mathbb{R} \times (\mathbb{R}^{n-1} \setminus V_c)$ (the complement of the open $\mathbb{R} \times V_c$). No point of $B$ lies in the slice $t = c$: if $(c,y) \in B$ then $(c,y) \in A$ so $y \in A_c \subseteq V_c$, contradicting $(c,y) \notin \mathbb{R} \times V_c$. Thus the continuous function $(t,y) \mapsto \lvert t - c \rvert$ is strictly positive on the compact set $B$, so it attains a positive minimum $\eta_c > 0$ (a continuous function on a nonempty compact set attains its infimum; if $B = \varnothing$ take $\eta_c = 1$). Then every point of $A$ with $\lvert t - c \rvert < \eta_c$ lies outside $B$, i.e. in $\mathbb{R} \times V_c$, proving the claim.
> >
> > **Step 3 — a finite slab cover of the compact range.** The open intervals $\{(c - \eta_c, c + \eta_c)\}_{c \in [a,b]}$ cover the compact interval $[a,b]$, so finitely many of them cover it, say those centred at $c_1, \dots, c_N$. Discarding overlaps, choose disjoint half-open subintervals $J_1, \dots, J_N$ with $\bigcup_r J_r = [a,b]$ and each $J_r$ contained in the interval centred at $c_{r'}$ for some $r'$; write $V^{(r)} := V_{c_{r'}}$ and $\ell_r := \operatorname{length}(J_r)$, so $\sum_r \ell_r = b - a$. By Step 2, $A \cap (J_r \times \mathbb{R}^{n-1}) \subseteq J_r \times V^{(r)}$.
> >
> > **Step 4 — add up the volumes.** The sets $J_r \times V^{(r)}$ cover $A$. Each is a union of the finitely many cubes $J_r \times (\text{one cube of } V^{(r)})$; a slab over a cube of side $s$ in $\mathbb{R}^{n-1}$ across an interval of length $\ell_r$ is a box of $n$-volume $\ell_r s^{n-1}$, and subdividing the interval turns each box into cubes of the same total volume. Hence the total $n$-volume of the cover is
> > $$\sum_{r=1}^{N} \ell_r \cdot \operatorname{vol}_{n-1}(V^{(r)}) < \sum_{r=1}^{N} \ell_r \cdot \varepsilon = (b-a)\,\varepsilon = \delta \qquad \text{(Step 1 bound on each } V^{(r)}\text{; } \textstyle\sum_r \ell_r = b-a\text{; } \varepsilon = \delta/(b-a)\text{)}.$$
> >
> > **Conclusion.** For every $\delta > 0$ the compact set $A$ has a cube cover of total volume less than $\delta$, so $A$ has measure zero. $\blacksquare$

> [!note]- Lemma 3: The deeply-flat set has null image (the Taylor estimate)
> **Statement:** Let $f : U \to \mathbb{R}^n$ be smooth, $U \subseteq \mathbb{R}^m$ open, and for $k \ge 1$ let $C_k = \{\, x \in U : \partial^\alpha f_j(x) = 0 \text{ for all } j \text{ and all } 1 \le |\alpha| \le k \,\}$. If $(k+1)n > m$, then $f(C_k)$ has measure zero in $\mathbb{R}^n$.
>
> **Hint:** On a compact cube, Taylor's theorem with the $(k+1)$-st derivative bounds $\lVert f(x+h) - f(x) \rVert \le c\lVert h \rVert^{k+1}$ for $x \in C_k$. Subdivide the cube into $r^m$ subcubes; each meeting $C_k$ has image in a cube of side of order $r^{-(k+1)}$; total volume is of order $r^{m-(k+1)n} \to 0$.
>
> **Why needed:** It is the terminal step of the induction: the strata $C_i \setminus C_{i+1}$ stop at $C_k$, whose image must be null on its own.
>
> > [!note]- Full proof
> > **Goal.** Show $f(C_k)$ is null when $(k+1)n > m$.
> >
> > **Step 0 — reduce to a compact cube.** Since $U$ is open it is a countable union of closed cubes $I_\ell \subseteq U$ (as in Lemma 1, Step 1), so $C_k = \bigcup_\ell (C_k \cap I_\ell)$ and $f(C_k) = \bigcup_\ell f(C_k \cap I_\ell)$; a countable union of null sets is null, so it suffices to show $f(C_k \cap I)$ is null for a single closed cube $I \subseteq U$ of side $a$.
> >
> > **Step 1 — the Taylor estimate.** Because $f$ is smooth and $I$ is compact, $M_{k+1} := \max_{|\alpha| = k+1}\ \max_{x \in I}\ \lvert \partial^\alpha f_j(x) \rvert$ (maximum over the components $j$ too) is finite. Fix $x \in C_k \cap I$ and $x + h \in I$; the segment from $x$ to $x+h$ lies in the convex set $I$. Apply [[Thm - Taylor's Theorem in Several Variables|Taylor's theorem]] to each component $f_j$ at $x$ to order $k$: with integral remainder,
> > $$f_j(x+h) = \sum_{|\alpha| \le k} \frac{\partial^\alpha f_j(x)}{\alpha!}\, h^\alpha + R_j(x,h), \qquad R_j(x,h) = \int_0^1 (k+1)(1-t)^k \sum_{|\alpha|=k+1} \frac{\partial^\alpha f_j(x+th)}{\alpha!}\, h^\alpha\, dt.$$
> > Every term of the polynomial sum with $1 \le |\alpha| \le k$ vanishes because $x \in C_k$ (all partials of order between $1$ and $k$ are zero there), and the $|\alpha| = 0$ term is $f_j(x)$; hence
> > $$f_j(x+h) - f_j(x) = R_j(x,h) \qquad \text{(all order-}1\text{-to-}k \text{ partials vanish on } C_k\text{)}.$$
> > Bounding the remainder, and using $\lvert h^\alpha \rvert \le \lVert h \rVert^{|\alpha|} = \lVert h \rVert^{k+1}$ for $|\alpha| = k+1$ together with $\int_0^1 (k+1)(1-t)^k\,dt = 1$,
> > $$\lvert f_j(x+h) - f_j(x) \rvert \le \Big(\sum_{|\alpha| = k+1} \tfrac{1}{\alpha!}\Big) M_{k+1}\, \lVert h \rVert^{k+1} \qquad \text{(triangle inequality on the integral; } \lvert h^\alpha \rvert \le \lVert h \rVert^{k+1}\text{)}.$$
> > Writing $c := \sqrt{n}\,\big(\sum_{|\alpha|=k+1} \tfrac{1}{\alpha!}\big) M_{k+1}$ and combining the $n$ components,
> > $$\lVert f(x+h) - f(x) \rVert \le c\, \lVert h \rVert^{k+1} \qquad \text{for all } x \in C_k \cap I,\ x+h \in I \quad \text{(sum of } n \text{ squared component bounds)}.$$
> >
> > **Step 2 — subdivide and count.** Fix a positive integer $r$ and cut $I$ into $r^m$ closed subcubes of side $a/r$. Let $I'$ be one of these subcubes that contains a point $x \in C_k$. Every point of $I'$ has the form $x + h$ with $\lVert h \rVert \le \operatorname{diam}(I') = \sqrt{m}\,(a/r)$. By Step 1, $f(I')$ lies in the closed ball of radius $c\,(\sqrt{m}\, a/r)^{k+1}$ about $f(x)$, hence in a cube of side
> > $$2c\,(\sqrt{m}\, a)^{k+1}\, r^{-(k+1)} =: b\, r^{-(k+1)} \qquad \text{(a ball of radius } \rho \text{ fits in a cube of side } 2\rho\text{)},$$
> > where $b := 2c\,(\sqrt{m}\,a)^{k+1}$ does not depend on $r$. The number of subcubes meeting $C_k$ is at most the total number $r^m$.
> >
> > **Step 3 — total volume tends to zero.** Summing the image-cube volumes over the at most $r^m$ relevant subcubes,
> > $$\operatorname{vol}\big(\text{cover of } f(C_k \cap I)\big) \le r^m \cdot \big(b\, r^{-(k+1)}\big)^n = b^n\, r^{\,m - (k+1)n} \qquad \text{(count } \times \text{ volume per image cube)}.$$
> > By hypothesis $(k+1)n > m$, so the exponent $m - (k+1)n$ is strictly negative and $b^n\, r^{\,m-(k+1)n} \to 0$ as $r \to \infty$. Thus $f(C_k \cap I)$ is covered by cubes of arbitrarily small total volume and is null.
> >
> > **Conclusion.** $f(C_k \cap I)$ is null for each cube $I$, so $f(C_k)$ is null. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the Euclidean form, then reduce the manifold form to it. Assume throughout that $n \ge 1$; if $n = 0$ then $\mathbb{R}^0$ is a single point, every differential $df_x : \mathbb{R}^m \to \mathbb{R}^0$ is surjective, $\operatorname{Crit}(f) = \varnothing$, and there is nothing to prove.
>
> **Step 0 — the filtration and the reduction to strata.** For $x \in U$ recall $\operatorname{Crit}(f) = \{x : \operatorname{rank} df_x < n\}$, and define for $i \ge 1$
> $$C_i := \{\, x \in U : \partial^\alpha f_j(x) = 0 \text{ for every component } j \text{ and every multi-index } 1 \le |\alpha| \le i \,\}.$$
> These are nested, $C_1 \supseteq C_2 \supseteq \cdots$, and $C_1 \subseteq \operatorname{Crit}(f)$: if all first partials of every component vanish at $x$ then $df_x = 0$, which is not surjective onto $\mathbb{R}^n$ since $n \ge 1$. Write $C := \operatorname{Crit}(f)$. For any integer $k \ge 1$,
> $$C = (C \setminus C_1) \ \cup\ (C_1 \setminus C_2) \ \cup\ \cdots\ \cup\ (C_{k-1} \setminus C_k) \ \cup\ C_k \qquad \text{(telescoping of the nested sets, with } C \supseteq C_1\text{)}.$$
> Choosing $k$ to be the least integer with $(k+1)n > m$, we show below that each of the finitely many pieces has null image; since a finite union of null sets is null, $f(C)$ is then null. We prove the nullity of the pieces by induction on the domain dimension $m$, the statement being taken for all target dimensions $n$ simultaneously.
>
> **Step 1 — base of the induction, $m = 0$.** When $m = 0$, $U$ is a subset of the one-point space $\mathbb{R}^0$, so $f(U)$ is at most a single point of $\mathbb{R}^n$, which has measure zero (a point is covered by one cube of side $\to 0$). Hence the theorem holds for $m = 0$ and every $n$. Assume now $m \ge 1$ and that the theorem — in the full form "$f(\operatorname{Crit}(f))$ is null" — holds for every smooth map whose domain is an open subset of $\mathbb{R}^{m-1}$, into any $\mathbb{R}^{n'}$.
>
> **Step 2 — the image of $C \setminus C_1$ is null.** Let $x_0 \in C \setminus C_1$. Since $x_0 \notin C_1$, some first partial derivative is nonzero at $x_0$; after relabelling the components of $f$ and the coordinates of $\mathbb{R}^m$ we may assume $\partial_1 f_1(x_0) \ne 0$. **Promote $f_1$ to a coordinate.** Define
> $$h : U \to \mathbb{R}^m, \qquad h(x) = (f_1(x),\, x_2,\, \dots,\, x_m).$$
> Its Jacobian at $x_0$ has first row $(\partial_1 f_1, \dots, \partial_m f_1)$ and rows $2,\dots,m$ equal to the standard basis covectors $e_2^{*}, \dots, e_m^{*}$, so $\det dh_{x_0} = \partial_1 f_1(x_0) \ne 0$. By the [[Thm - The Inverse Function Theorem|inverse function theorem]] — a smooth map with invertible differential at a point is a diffeomorphism of a neighbourhood onto an open set — $h$ restricts to a diffeomorphism $h : W \to W'$ of an open neighbourhood $W \ni x_0$ onto an open $W' \subseteq \mathbb{R}^m$. **Change coordinates.** Set $g := f \circ h^{-1} : W' \to \mathbb{R}^n$. Writing a point of $W'$ as $(t,z)$ with $t \in \mathbb{R}$, $z \in \mathbb{R}^{m-1}$, the first coordinate of $h$ is $f_1$, so $g_1(t,z) = f_1(h^{-1}(t,z)) = t$; that is,
> $$g(t,z) = (t,\, \bar g(t,z)) \qquad \text{for some smooth } \bar g : W' \to \mathbb{R}^{n-1} \quad \text{(the first coordinate of } g \text{ is } t \text{ by construction)}.$$
> Consequently $g$ maps the slice $(\{t\} \times \mathbb{R}^{m-1}) \cap W'$ into the slice $\{t\} \times \mathbb{R}^{n-1}$. For each fixed $t$ let
> $$g^t : (\{t\} \times \mathbb{R}^{m-1}) \cap W' \to \mathbb{R}^{n-1}, \qquad g^t(z) = \bar g(t,z),$$
> a smooth map on an open subset of $\mathbb{R}^{m-1}$. **Criticality is preserved and localises to slices.** Because $h$ is a diffeomorphism, $dg_{(t,z)} = df_{h^{-1}(t,z)} \circ (dh_{h^{-1}(t,z)})^{-1}$ has the same rank as $df$ at the corresponding point, so $h$ carries critical points of $f$ in $W$ bijectively to critical points of $g$ in $W'$. Now the Jacobian of $g = (t, \bar g)$ at $(t,z)$ is block lower-triangular,
> $$dg_{(t,z)} = \begin{pmatrix} 1 & 0 \\ \partial_t \bar g & \partial_z \bar g \end{pmatrix},$$
> so $dg_{(t,z)}$ is surjective onto $\mathbb{R}^n$ if and only if the block $\partial_z \bar g = d(g^t)_z$ is surjective onto $\mathbb{R}^{n-1}$ (the top row already supplies the first target direction, and the remaining directions must come from the $z$-derivatives). Hence a point $(t,z) \in W'$ is critical for $g$ exactly when $z$ is critical for $g^t$. **Apply the inductive hypothesis slicewise.** The domain of $g^t$ is an open subset of $\mathbb{R}^{m-1}$, so by the inductive hypothesis the critical values of $g^t$ form a null set in $\mathbb{R}^{n-1}$. The critical values of $g$ lying in the slice $\{t\} \times \mathbb{R}^{n-1}$ are precisely $\{t\} \times (\text{critical values of } g^t)$, by the previous sentence; thus the set $\operatorname{Crit\text{-}val}(g)$ of critical values of $g$ meets every hyperplane $\{t\} \times \mathbb{R}^{n-1}$ in a null subset of that hyperplane. **Upgrade to full nullity by the slice lemma.** Cover $W'$ by countably many compact cubes $K_\ell \subseteq W'$ (Lemma 1, Step 1). For each $\ell$ the set $g(\operatorname{Crit}(g) \cap K_\ell)$ is compact (continuous image of a compact set, since $\operatorname{Crit}(g)$ is closed in $W'$ and $\operatorname{Crit}(g) \cap K_\ell$ is a closed subset of the compact $K_\ell$), and its slice at any $t$ is contained in the critical values of $g^t$, hence null. By **Lemma 2** applied to this compact set, $g(\operatorname{Crit}(g) \cap K_\ell)$ is null; taking the countable union over $\ell$, $g(\operatorname{Crit}(g))$ is null. Finally, on $W$ we have $f = g \circ h$, so
> $$f\big((C \setminus C_1) \cap W\big) \subseteq f(\operatorname{Crit}(f) \cap W) = g\big(h(\operatorname{Crit}(f) \cap W)\big) = g(\operatorname{Crit}(g) \cap W'),$$
> which is null. The point $x_0 \in C \setminus C_1$ was arbitrary, so every point of $C \setminus C_1$ has such a neighbourhood $W$ with null image; covering $C \setminus C_1$ by countably many of these neighbourhoods (possible because $U$, being an open subset of $\mathbb{R}^m$, is second countable, so any open cover has a countable subcover), and using that a countable union of null sets is null, we conclude $f(C \setminus C_1)$ is null.
>
> **Step 3 — the image of $C_i \setminus C_{i+1}$ is null, for each $1 \le i \le k-1$.** Let $x_0 \in C_i \setminus C_{i+1}$. Since $x_0 \notin C_{i+1}$, some partial derivative of order $i+1$ of some component is nonzero at $x_0$; write it as $\partial_s(\partial^\beta f_j)(x_0) \ne 0$ with $|\beta| = i$, and set $w := \partial^\beta f_j$, a partial derivative of $f$ of order $i \ge 1$. **Two facts about $w$.** First, $w$ vanishes on $C_i$: it is a partial of order $|\beta| = i$ with $1 \le i$, and $C_i$ is defined by the vanishing of all partials of order $1$ through $i$. Second, $\partial_s w(x_0) \ne 0$; after relabelling coordinates assume $s = 1$, so $\partial_1 w(x_0) \ne 0$. **Promote $w$ to a coordinate.** Define
> $$h : U \to \mathbb{R}^m, \qquad h(x) = (w(x),\, x_2,\, \dots,\, x_m),$$
> with $\det dh_{x_0} = \partial_1 w(x_0) \ne 0$, so by the inverse function theorem $h$ is a diffeomorphism of a neighbourhood $W \ni x_0$ onto an open $W' \subseteq \mathbb{R}^m$. Because $w = 0$ on $C_i$, the diffeomorphism $h$ carries $C_i \cap W$ into the hyperplane $\{0\} \times \mathbb{R}^{m-1}$. Set $g := f \circ h^{-1} : W' \to \mathbb{R}^n$ and let
> $$\bar g : (\{0\} \times \mathbb{R}^{m-1}) \cap W' \to \mathbb{R}^n, \qquad \bar g(z) = g(0,z),$$
> the restriction of $g$ to that hyperplane, a smooth map on an open subset of $\mathbb{R}^{m-1}$ into $\mathbb{R}^n$. **Every image point comes from a critical point of $\bar g$.** Since $i \ge 1$ we have $C_i \subseteq C_1 \subseteq \operatorname{Crit}(f)$, and on $C_i$ all first partials of $f$ vanish, so $df = 0$ there; hence for $x \in C_i \cap W$, $dg_{h(x)} = df_x \circ (dh_x)^{-1} = 0$, and a fortiori the differential of the restriction $\bar g$ at $h(x)$ is zero, which is not surjective onto $\mathbb{R}^n$ (as $n \ge 1$). Thus every point of $h(C_i \cap W) \subseteq \{0\} \times \mathbb{R}^{m-1}$ is a critical point of $\bar g$. Therefore
> $$f(C_i \cap W) = g(h(C_i \cap W)) = \bar g\big(h(C_i \cap W)\big) \subseteq \bar g(\operatorname{Crit}(\bar g)),$$
> using $f = g \circ h$ on $W$ and that $h(C_i \cap W)$ lies in the hyperplane where $g$ restricts to $\bar g$. **Apply the inductive hypothesis.** The domain of $\bar g$ is an open subset of $\mathbb{R}^{m-1}$, so by the inductive hypothesis $\bar g(\operatorname{Crit}(\bar g))$ is null in $\mathbb{R}^n$; hence $f(C_i \cap W)$ is null. Covering $C_i \setminus C_{i+1}$ by countably many such neighbourhoods $W$ (second countability of $U$) and taking the union, $f(C_i \setminus C_{i+1})$ is null. This holds for every $i$ with $1 \le i \le k-1$.
>
> **Step 4 — the image of $C_k$ is null.** By the choice of $k$, $(k+1)n > m$, so **Lemma 3** applies directly and $f(C_k)$ is null.
>
> **Step 5 — assemble the Euclidean statement.** Combining the decomposition of Step 0 with the nullity established in Steps 2, 3, and 4,
> $$f(C) = f(C \setminus C_1) \cup \bigcup_{i=1}^{k-1} f(C_i \setminus C_{i+1}) \cup f(C_k),$$
> a union of finitely many null sets, hence null. This proves the Euclidean form, completing the induction on $m$.
>
> **Step 6 — the manifold form.** Let $f : M \to N$ be smooth with $M$ second countable and $\dim N = n$, $\dim M = m$. Choose a smooth atlas $\{(V_\beta, \psi_\beta)\}_{\beta}$ of $N$ with $\psi_\beta : V_\beta \to \mathbb{R}^n$; each $V_\beta$ is second countable and hence its preimage contributes below. For each point of $M$ pick a chart $(U, \varphi)$, $\varphi : U \to \mathbb{R}^m$, small enough that $f(U) \subseteq V_\beta$ for some $\beta$; these chart domains form an open cover of $M$. **Extract a countable subcover.** Because $M$ is second countable it is Lindelöf — restating [[Def - First and Second Countable]]: from a countable basis $\{B_p\}$, for any open cover choose, for each basis element $B_p$ contained in some cover member, one such member; every point lies in a basis element contained in a cover member, so these countably many members cover $M$. Thus countably many charts $(U_\alpha, \varphi_\alpha)$ with $f(U_\alpha) \subseteq V_{\beta(\alpha)}$ cover $M$. **Critical points correspond under charts.** On $U_\alpha$ the coordinate representative $\tilde f_\alpha := \psi_{\beta(\alpha)} \circ f \circ \varphi_\alpha^{-1}$ is a smooth map between open subsets of $\mathbb{R}^m$ and $\mathbb{R}^n$; by the chain rule $d(\tilde f_\alpha) = d\psi_{\beta(\alpha)} \circ df \circ d\varphi_\alpha^{-1}$, and since $\varphi_\alpha, \psi_{\beta(\alpha)}$ are diffeomorphisms their differentials are isomorphisms, so $d(\tilde f_\alpha)$ is surjective exactly where $df$ is. Hence $\varphi_\alpha(\operatorname{Crit}(f) \cap U_\alpha) = \operatorname{Crit}(\tilde f_\alpha)$, and
> $$\psi_{\beta(\alpha)}\big( f(\operatorname{Crit}(f) \cap U_\alpha) \big) = \tilde f_\alpha\big(\operatorname{Crit}(\tilde f_\alpha)\big),$$
> which is null in $\mathbb{R}^n$ by the Euclidean form (Step 5). By the one-cover-suffices characterisation of [[Def - Set of Measure Zero on a Manifold|measure zero on a manifold]] — a set is null in $N$ when its image is null in $\mathbb{R}^n$ in the charts of some cover — this exhibits $f(\operatorname{Crit}(f) \cap U_\alpha)$ as null in $N$. **Countable union.** The full critical-value set is $f(\operatorname{Crit}(f)) = \bigcup_\alpha f(\operatorname{Crit}(f) \cap U_\alpha)$, a countable union of null subsets of $N$, hence null in $N$ (closure of the null sets under countable unions, established chart by chart via the same estimate as in $\mathbb{R}^n$).
>
> **Step 7 — density of regular values.** Let $O \subseteq N$ be a nonempty open set. In any chart $\psi_\beta$ meeting $O$, the image $\psi_\beta(O \cap V_\beta)$ is a nonempty open subset of $\mathbb{R}^n$ and therefore contains a cube of positive volume, so it is not null; hence $O$ is not contained in the critical-value set (which is null). Therefore $O$ contains a point that is not a critical value, i.e. a regular value. As $O$ was an arbitrary nonempty open set, the regular values are dense in $N$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The fundamental theorem of algebra by degree.** A complex polynomial $p$ of degree $d \ge 1$, viewed as a smooth map $\mathbb{R}^2 \to \mathbb{R}^2$, is proper, and its critical points are the finitely many zeros of $p'$. By Sard the critical values are null, so almost every value is regular with a finite preimage; a homotopy-invariance argument shows the number of preimages (counted mod $2$, or with sign) is constant on regular values and equals $d$, so $p$ is surjective and in particular attains the value $0$. Sard is what guarantees a regular value with which to start the count; the exercise is to see that the argument collapses without the existence of even one regular value.

**Genericity of Morse functions on a surface.** For a compact surface $\Sigma \subseteq \mathbb{R}^3$ and the height functions $h_a(x) = a \cdot x$ indexed by $a \in S^2$, the function $h_a$ is Morse for almost every direction $a$. The exercise is to identify the bad directions as the critical values of the Gauss map $\Sigma \to S^2$ (a point is a degenerate critical point of $h_a$ exactly when $a$ is a critical value of the Gauss map) and to invoke Sard on the Gauss map. This is non-obvious because the object one wants to be generic — a Morse function — is a whole function, yet its non-genericity is pinned to the critical values of a single auxiliary smooth map.

**Vanishing of low homotopy groups of spheres.** A smooth map $f : S^k \to S^m$ with $k < m$ has $\operatorname{Crit}(f) = S^k$ (the differential cannot be surjective for dimension reasons), so by Sard $f(S^k)$ has measure zero in $S^m$ and $f$ misses a point $q$; the complement $S^m \setminus \{q\}$ is diffeomorphic to $\mathbb{R}^m$, which is contractible, so $f$ is null-homotopic. After the smoothing of continuous maps (developed in **chapter XII**) this gives $\pi_k(S^m) = 0$ for $k < m$. The exercise applies Sard where there is no obvious "critical value problem" at all — the whole domain is critical — and extracts a topological conclusion from a measure-theoretic one.

---

# Bridges

- **[[Thm - Sard-Smale Theorem|Sard–Smale theorem]].** The infinite-dimensional analogue replaces $f$ by a smooth Fredholm map $F : X \to Y$ between Banach manifolds and concludes that the regular values are residual, hence dense. Its proof is built on this page: in a Kuranishi chart $F$ takes the form $(x_0, x_1) \mapsto Tx_1 + f(x_0,x_1)$ with $T$ a linear isomorphism and $x_0$ ranging over the finite-dimensional kernel; the critical values in each slice are then the critical values of the finite-dimensional map $x_0 \mapsto f(x_0, \cdot)$, to which the present theorem applies, and local properness turns "null in every slice" into "nowhere dense." The construction here — finite-dimensional Sard applied slice by slice — is exactly the ingredient Sard–Smale imports.

- **[[Thm - Regular Value Theorem on Manifolds|Regular value theorem]].** Sard and the regular value theorem are complementary: the regular value theorem says a regular value's level set is a submanifold, and Sard says regular values are dense, so the two together turn "cut out by equations" into "generically a submanifold of the expected dimension." Whenever a moduli space is defined as a level set, this pair is what makes it smooth for a generic choice.

- **[[Def - Mod-2 Degree of a Proper Fredholm Map|Degree theory]].** The mod-2 and integer degrees count preimages of a regular value of a proper map. Sard provides the regular values; properness makes the preimage finite; a cobordism between the fibres over two regular values, itself a compact one-manifold with boundary, makes the count independent of the value. Sard is the first of these three inputs and the reason the definition is not vacuous.

- **[[Def - Set of Measure Zero on a Manifold|Measure zero on a manifold]].** This page is the principal customer of the chart-based notion of measure zero: Sard's conclusion is stated in that language, and the proof of its coordinate-independence (Lemma 1 here) is what makes the manifold statement well posed. The two pages are the definition and its central theorem.

---

# Unlocked by This

> [!tip] Parametric transversality *(from this chapter)*
> Applying Sard to a jointly smooth family $F : U \times W \to \mathbb{R}^n$ and projecting the universal zero set to the parameter space $W$ shows that for almost every parameter $w$ the individual map $F(\cdot, w)$ has $y$ as a regular value. This is the mechanism of [[Thm - Parametric Transversality|parametric transversality]] and, one level up, of the generic smoothness of the Seiberg–Witten moduli space.

> [!tip] Transversality is generic *(from Differential Topology)*
> Two submanifolds can be made transverse by an arbitrarily small perturbation of one of them, because the failure of transversality is the criticality of an auxiliary evaluation map, and Sard confines critical values to a null set. This is the foundation of intersection theory and of the Thom transversality theorem.

> [!tip] The weak Whitney embedding theorem *(from Differential Topology)*
> A compact $m$-manifold embeds in $\mathbb{R}^{2m+1}$: starting from any immersion into a high-dimensional Euclidean space, one projects along a generic direction, and Sard (applied to a secant and a tangent map) shows that the directions destroying injectivity or immersivity form a measure-zero set, so a good projection direction exists.
