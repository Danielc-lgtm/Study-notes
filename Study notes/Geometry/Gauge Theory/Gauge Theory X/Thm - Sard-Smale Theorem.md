---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Sard's Theorem for Smooth Maps"
  - "Thm - Kuranishi Model for a Fredholm Map"
  - "Def - Residual Set and Generic Property"
  - "Def - Fredholm Map and Its Index"
  - "Thm - Regular Value and Transversality Theorems for Fredholm Maps"
  - "Thm - Proper Maps are Closed and Fredholm Maps are Locally Proper"
  - "Thm - Stabilisation of Fredholm Operators and Continuity of the Kernel"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $X$ and $Y$ are **Banach manifolds** that are Hausdorff and second countable, modelled on separable Banach spaces, in the sense of [[Def - Banach Manifold and Smooth Maps between Banach Spaces|the standing framework of this chapter]]. Because a Banach manifold is locally homeomorphic to a normed space it is locally metrisable, and a Hausdorff, second countable, locally metrisable space is regular and second countable, hence metrisable by the [[Thm - Urysohn Metrization Theorem|Urysohn metrization theorem]] — so both $X$ and $Y$ carry a metric inducing their topology. This metrisability is used twice below, and we invoke it by name each time.

The map $F : X \to Y$ is **smooth**, $F \in C^\infty(X;Y)$, and is a [[Def - Fredholm Map and Its Index|Fredholm map]]: at every point $x \in X$ the differential
$$d_x F : T_x X \longrightarrow T_{F(x)} Y$$
is a [[Def - Fredholm Operator and Index|Fredholm operator]], meaning it has finite-dimensional kernel $\ker d_x F$, closed range, and finite-dimensional cokernel $\operatorname{coker} d_x F = T_{F(x)} Y / \operatorname{im} d_x F$. Its **index** is $\operatorname{index} d_x F = \dim \ker d_x F - \dim \operatorname{coker} d_x F$; on a connected $X$ this integer is independent of $x$ and is written $\operatorname{index} F$.

A point $x \in X$ is a **critical point** of $F$ if $d_x F$ is not surjective; the set of critical points is $\operatorname{Crit}(F) = \{x \in X : d_x F \text{ not surjective}\}$, and $F(\operatorname{Crit}(F)) \subseteq Y$ is the set of **critical values**. A point $y \in Y$ is a **regular value** if $d_x F$ is surjective for every $x \in F^{-1}(y)$; a value with empty preimage, $F^{-1}(y) = \varnothing$, is vacuously regular. Thus the regular values are exactly $Y \setminus F(\operatorname{Crit}(F))$.

A subset of a topological space is [[Def - Residual Set and Generic Property|residual]] if it contains a countable intersection of open dense subsets. For the Kuranishi normal form we use the notation of [[Thm - Kuranishi Model for a Fredholm Map|the Kuranishi model]]: at a point $p$ we split the model spaces of charts around $p$ and $F(p)$ as $X = X_0 \oplus X_1$ and $Y = Y_0 \oplus Y_1$ with $X_0 = \ker d_p F$ (finite-dimensional), $Y_0 = \operatorname{im} d_p F$, and $Y_1$ a finite-dimensional complement of $Y_0$; $\pi_{Y_0}$ and $\pi_{Y_1}$ denote the projections onto $Y_0$ and $Y_1$, and $T := d_p F|_{X_1} : X_1 \to Y_0$ is a linear isomorphism.

> [!warning] Convention: "residual" for Haydys's "second category"
> Haydys (Definition, p. 53) calls a countable intersection of open dense subsets a set **of second category**. This clashes with Baire's original terminology, in which "second category" means merely "not meagre" — a much weaker property. To avoid the collision the whole series says **residual** (equivalently *comeagre*) for a set containing a countable intersection of open dense subsets, and reserves "meagre" and "not meagre" for their classical meanings. Wherever a source writes "of second category" for the strong property, read "residual".

> [!warning] Convention: second countable in place of paracompact
> Haydys (Theorem 164, p. 53) states the theorem for **paracompact** Banach manifolds. The series works with second countable Banach manifolds throughout. A second countable metrisable space is Lindelöf, and a Lindelöf metrisable space is paracompact, so our hypothesis is a special case of Haydys's; and the proof uses only what second countability supplies directly — the Lindelöf property (every open cover has a countable subcover, proved as Lemma 3 below) and metrisability of $Y$ (for the closed-map property and for Baire's theorem). We record this reduction and use only those two consequences.

---

# Statement

> **Sard–Smale theorem (Smale 1965).** Let $F : X \to Y$ be a smooth [[Def - Fredholm Map and Its Index|Fredholm map]] between second countable [[Def - Banach Manifold and Smooth Maps between Banach Spaces|Banach manifolds]]. Then the set of regular values of $F$,
> $$\operatorname{Reg}(F) \;=\; Y \setminus F\big(\operatorname{Crit}(F)\big),$$
> is [[Def - Residual Set and Generic Property|residual]] in $Y$ — it is a countable intersection of open dense subsets — and in particular it is dense in $Y$.

The finite-dimensional case, in which $X$ and $Y$ are ordinary smooth manifolds, is [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]]; the content of Smale's extension is that the conclusion survives verbatim into infinite dimensions once "Fredholm" replaces the automatic finiteness that finite-dimensional manifolds provide.

> [!note]- Regularity hypothesis: why smoothness is more than enough
> Smale's theorem is usually stated for maps of class $C^q$ with $q > \max(\operatorname{index} F, 0)$. The reason is visible in the proof: the theorem is reduced, in a Kuranishi chart, to the finite-dimensional Sard theorem applied to a map $g : \mathbb{R}^{\dim X_0} \to \mathbb{R}^{\dim Y_1}$, and [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]] for such a map requires class $C^q$ with $q \ge \max(1, \dim X_0 - \dim Y_1 + 1)$. Since $\dim X_0 - \dim Y_1 = \dim\ker d_p F - \dim\operatorname{coker} d_p F = \operatorname{index} F$, this is exactly $q > \max(\operatorname{index} F, 0)$. As we assume $F \in C^\infty$, the hypothesis holds with room to spare, and we do not track it further.

---

# Motivation

The whole of transversality theory, degree theory, and the construction of gauge-theoretic moduli spaces rests on being able to say the phrase "for a generic value" or "after a small generic perturbation" and have it mean something. In finite dimensions this is the everyday use of [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]]: almost every value of a smooth map is regular, so almost every level set is a manifold of the expected dimension, and one may always nudge a construction into general position. The question this theorem answers is whether the same freedom exists for the maps that actually arise in gauge theory, which live on infinite-dimensional spaces — spaces of connections, spaces of Sobolev sections, configuration spaces of a variational problem.

The obstacle is that the finite-dimensional argument is measure-theoretic through and through: it counts, via Lebesgue measure, how thin the image of the critical set is. On an infinite-dimensional Banach space there is no translation-invariant measure at all, so "almost every value" has no literal meaning and Sard's proof cannot even be started. Smale's insight is that the maps one cares about are never arbitrary: they are **Fredholm**, and a Fredholm map is, up to a change of coordinates, a linear isomorphism in all but finitely many directions plus a finite-dimensional nonlinearity. All of the map's failure to be a submersion is concentrated in a finite-dimensional corner, where Sard's theorem does apply. The theorem is the statement that this local finite-dimensional picture can be assembled into a global topological one, with the measure-theoretic notion "null" upgraded to the purely topological notion "residual".

Concretely, the reader should carry the smallest genuine example in mind. Let $L$ be an elliptic operator on a closed manifold and $N$ a lower-order nonlinearity; then $F(u) = Lu + N(u)$, read between the appropriate Sobolev completions, is a smooth Fredholm map, and Sard–Smale says a residual — hence dense — set of right-hand sides $w$ makes $u \mapsto Lu + N(u) - w$ have $0$ as a regular value, so that the solution set of $Lu + N(u) = w$ is a smooth finite-dimensional manifold of dimension $\operatorname{index} L$. Every genericity statement in [[Thm - Parametric Transversality|parametric transversality]] and in [[Def - Seiberg-Witten Moduli Space|Seiberg–Witten theory]] is a descendant of this one.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is bare — a smooth Fredholm map — so the skill is recognising when a problem hands you such a map without naming it.

The first disguised source is **an elliptic operator perturbed by lower-order nonlinear terms on a closed manifold**. Suppose $F(u) = Lu + N(u)$, where $L$ is a linear elliptic differential operator of order $m$ and $N$ collects terms of lower differential order, and $F$ is read as a map between Sobolev completions $F : W^{k+m,2}(M;E) \to W^{k,2}(M;E)$ on a closed manifold $M$. The bridge to "smooth Fredholm map" runs in two steps. First, [[Thm - Elliptic Operators on Closed Manifolds are Fredholm|an elliptic operator on a closed manifold is Fredholm]] of index equal to the topological index of its symbol; second, the differential $d_u F = L + dN_u$ differs from $L$ by an operator that factors through a more regular Sobolev space and so is compact by the [[Thm - Rellich Compactness Theorem|Rellich compactness theorem]], and [[Thm - Stability of the Fredholm Property under Small and Compact Perturbations|a compact perturbation of a Fredholm operator is Fredholm of the same index]]. The non-obvious part is that "lower order" is precisely the analytic condition that turns the nonlinear correction into a compact, hence Fredholm-preserving, perturbation. *Example problem:* show that $u \mapsto \Delta u + u^3$ on a closed surface is a smooth Fredholm map of index $0$, and conclude by this theorem that a residual set of $w$ are regular values of $u \mapsto \Delta u + u^3 - w$.

The second disguised source is **the defining map of a gauge-theoretic moduli space, after gauge fixing and Sobolev completion**. The anti-self-duality equations and the [[Def - Seiberg-Witten Equations|Seiberg–Witten equations]] are, once a slice for the gauge group is chosen, the zero set of a smooth map between Hilbert manifolds whose linearisation is an elliptic complex's deformation operator. The bridge is that this deformation operator is elliptic on a closed four-manifold, hence Fredholm, so the defining map is a Fredholm map and its regular values — equivalently, after the parametric reformulation, its generic perturbations — are governed by this theorem. The non-obviousness is entirely in the reduction to a Fredholm setting: raw, before gauge fixing, the map is not Fredholm because the gauge orbit directions fill an infinite-dimensional kernel. *Example problem:* deduce that for a residual set of perturbations the Seiberg–Witten moduli space is a smooth manifold of the dimension predicted by the index of the deformation operator.

The third disguised source is, paradoxically, **an ordinary smooth map between finite-dimensional manifolds**. If $F : M \to N$ is smooth with $M, N$ finite-dimensional, then at each point $d_x F$ has finite-dimensional domain and codomain, so its kernel and cokernel are automatically finite-dimensional and its range is automatically closed; $F$ is a Fredholm map of index $\dim M - \dim N$. The bridge is trivial, and its payoff is conceptual: Sard–Smale contains [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]] as its finite-dimensional special case, so any genericity argument one already trusts in finite dimensions is a corollary. *Example problem:* recover the density of regular values of a smooth map $S^n \to S^n$, the fact underlying the well-definedness of the [[Def - Brouwer Degree of a Map|Brouwer degree]], as the finite-dimensional instance of this theorem.

**Targets (Output Amplification)**

The bare conclusion — a dense supply of regular values — becomes structural when combined with three further ingredients.

Combine the conclusion with **the regular-value theorem for Fredholm maps**. By [[Thm - Regular Value and Transversality Theorems for Fredholm Maps|the regular-value theorem]], if $y$ is a regular value then $F^{-1}(y)$ is a smooth embedded submanifold of $X$ of dimension $\operatorname{index} F$, with $T_x F^{-1}(y) = \ker d_x F$. The extra ingredient is that theorem; the payoff is that Sard–Smale plus the regular-value theorem together say **a residual set of level sets are manifolds of the expected dimension** — the working definition of "in general position" for an infinite-dimensional problem.

Combine the conclusion with **properness and vanishing index**. If in addition $F$ is proper and $\operatorname{index} F = 0$, then for a regular value $y$ the preimage $F^{-1}(y)$ is a compact $0$-manifold, hence a finite set, and the parity of its cardinality is the [[Def - Mod-2 Degree of a Proper Fredholm Map|mod-2 degree]]. The extra ingredient is properness, which guarantees the preimage is compact; Sard–Smale is what guarantees such a $y$ exists at all. The payoff is a well-defined degree theory in infinite dimensions.

Combine the conclusion with **the parametric setup**. Given a smooth Fredholm family $\mathcal F : X \times W \to Y$ with $y$ a regular value of $\mathcal F$ itself, applying this theorem to the restricted projection $\pi : \mathcal F^{-1}(y) \to W$ produces a residual set of parameters $w$ for which $y$ is a regular value of the individual map $\mathcal F_w = \mathcal F(\cdot, w)$; this is [[Thm - Parametric Transversality|parametric transversality]]. The extra ingredient is the diagram chase identifying the cokernel of $d\pi$ with the cokernel of $d_x \mathcal F_w$. The payoff is genericity when the value cannot be moved — the situation forced by symmetry in the Seiberg–Witten equations, where $y$ must be a fixed point of the group action, so one perturbs the map rather than the value. This is the use recorded as items I6.3.3 (in §10.3) and I7.1.14 (in the Seiberg–Witten chapter).

---

# Why Is It True

Forget for a moment that $X$ and $Y$ are infinite-dimensional and look at what the [[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model]] says about $F$ near a point $p$. In suitable charts, and after splitting the model spaces as $X = X_0 \oplus X_1$ and $Y = Y_0 \oplus Y_1$ with $X_0 = \ker d_p F$ and $Y_0 = \operatorname{im} d_p F$ both singled out by $d_p F$, the map takes the normal form
$$F \circ \phi (x_0, x_1) = T x_1 + f(x_0, x_1), \qquad T : X_1 \xrightarrow{\ \cong\ } Y_0,\quad f : X \to Y_1,$$
in which the only non-linear, non-invertible behaviour lives in the finite-dimensional map $x_0 \mapsto f(x_0, x_1)$ from $X_0$ (dimension $\dim\ker d_p F$) to $Y_1$ (dimension $\dim\operatorname{coker} d_p F$). In the $Y_0$-directions the map is the isomorphism $T$ and can never fail to be a submersion; all the criticality is confined to the finite-dimensional corner. On that corner the ordinary [[Thm - Sard's Theorem for Smooth Maps|Sard theorem]] applies, and it says the critical values, seen slice-by-slice over the $Y_0$-coordinate, form a set that meets each slice in a Lebesgue-null subset of the finite-dimensional $Y_1$.

The remaining difficulty is that "null in each slice" is a measure-theoretic statement, and there is no measure on $Y$. The trick is to trade measure for topology. A set which meets some finite-dimensional slice in a null set cannot contain an open box, because an open box would meet that slice in a set of positive measure — so the critical values on a Kuranishi neighbourhood have **empty interior**. To turn "empty interior" into the topologically robust "nowhere dense", one needs the set to be closed, and this is exactly what **local properness** buys: a proper map is a closed map (into a metrisable target), so the critical values of $F$ restricted to a closed local piece form a closed set with empty interior, that is, a nowhere-dense set whose complement is open and dense. Finally, second countability lets one cover $X$ by countably many such pieces, and the regular values are the countable intersection of the corresponding open dense sets — a residual set, dense by Baire.

> **The mechanism in one sentence:** a Fredholm map is, in Kuranishi coordinates, an isomorphism in the cokernel-free directions plus a finite-dimensional map in the kernel–cokernel corner, so Sard's theorem controls the critical values slice by slice, and local properness turns "measure zero in every slice" into "closed with empty interior", which countable covering assembles into "residual".

---

# What Makes This Hard

The single conceptual hurdle is that **measure-zero has no meaning on a Banach space**, so the finite-dimensional proof cannot be transported directly; the entire architecture exists to reduce to a finite-dimensional slice where measure returns. The non-obvious technical step is the passage from "the critical values meet each slice in a null set" (a statement about the finite-dimensional Kuranishi corner) to "the critical values are nowhere dense in $Y$" (a topological statement); this passage is not automatic and fails without **properness**, which is what makes the critical-value set closed so that empty interior is equivalent to nowhere density. The common error is to work with the open neighbourhood $U_p$ throughout: its image under a proper map need not be closed, and one must instead take the closed piece $\overline{U_p}$ to get a closed image — while checking, separately, that enlarging $U_p$ to $\overline{U_p}$ does not destroy the empty-interior property, which it does not because Sard's theorem bounds the critical values over the whole closed slice.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Localise. Around each point $p$ put the map into Kuranishi normal form and choose a closed bounded piece $\overline{U_p}$ on which $F$ is proper. On such a piece, prove that the critical values are (a) closed, by properness, and (b) of empty interior, by the finite-dimensional Sard theorem applied slice-by-slice in the Kuranishi corner; together these say the complement $R_p$ of the critical values on $\overline{U_p}$ is open and dense. Cover $X$ by countably many such pieces using second countability; the regular values are the intersection of the corresponding $R_{p_i}$, a residual set, dense by Baire.

**Subgoal decomposition:**

1. **The critical set is closed.** Show $\operatorname{Crit}(F)$ is closed in $X$.
   - *Hint:* surjectivity of a Fredholm operator is preserved under small perturbation, and $x \mapsto d_x F$ is continuous in charts.
   - *Why needed:* so that $\operatorname{Crit}(F) \cap \overline{U_p}$ is closed and its image can be controlled by properness.

2. **Local properness.** Show each $p$ has a closed bounded neighbourhood $\overline{U_p}$ (in a Kuranishi chart) with $F|_{\overline{U_p}}$ proper.
   - *Hint:* in the normal form $Tx_1 + f(x_0,x_1)$ the preimage of a compact set has its $x_1$-part in the compact $T^{-1}\pi_{Y_0}(K)$ and its $x_0$-part in a bounded subset of the finite-dimensional $X_0$.
   - *Why needed:* properness makes $F|_{\overline{U_p}}$ a closed map, so critical values are closed.

3. **Critical values are closed on $\overline{U_p}$.** Combine 1 and 2 with "proper maps are closed".
   - *Hint:* a proper continuous map into a metrisable space is closed.
   - *Why needed:* it makes the complement $R_p$ open.

4. **Critical values have empty interior.** In the Kuranishi chart, reduce criticality to a finite-dimensional map and apply Sard.
   - *Hint:* $d(F\phi)_{(x_0,x_1)}$ is surjective if and only if $\partial_{x_0} f$ is surjective onto $Y_1$; fix the $Y_0$-coordinate and apply finite-dimensional Sard to the resulting map $X_0 \to Y_1$.
   - *Why needed:* it makes the complement $R_p$ dense.

5. **Assemble.** Cover $X$ by countably many $U_{p_i}$; show $\operatorname{Reg}(F) = \bigcap_i R_{p_i}$.
   - *Hint:* second countable implies Lindelöf; a value is regular exactly when no critical point in any $\overline{U_{p_i}}$ maps to it.
   - *Why needed:* it produces the countable intersection of open dense sets and, by Baire, density.

---

# Lemma Decomposition

> [!note]- Lemma 1: The set of critical points of a Fredholm map is closed
> **Statement:** Let $F : X \to Y$ be a smooth Fredholm map between Banach manifolds. Then the set of regular points $\{x \in X : d_x F \text{ surjective}\}$ is open in $X$; equivalently, $\operatorname{Crit}(F) = \{x : d_x F \text{ not surjective}\}$ is closed.
>
> **Hint:** Surjectivity of a Fredholm operator is stable under small perturbation, and in a chart $x \mapsto d_x F$ is a continuous map into bounded operators.
>
> **Why needed:** It guarantees that $\operatorname{Crit}(F) \cap \overline{U_p}$ is a closed subset, which — together with local properness — forces its image to be closed (Step 2 of the formal proof).
>
> > [!note]- Full proof
> > Fix a regular point $x_0$, so $d_{x_0} F$ is surjective. Choose a chart $\psi : U \to X_m$ of $X$ around $x_0$ (with $X_m$ the model Banach space) and a chart $\chi$ of $Y$ around $F(x_0)$, and let $\hat F = \chi \circ F \circ \psi^{-1}$ be the local representative, a smooth map between open subsets of Banach spaces. Because charts are diffeomorphisms, $d_x F$ is surjective if and only if $d_{\psi(x)} \hat F$ is surjective, so it suffices to prove that the set of points where $d\hat F$ is surjective is open.
> >
> > **The differential is continuous.** Since $F$ is smooth, $\hat F$ is $C^1$, so the map $u \mapsto d_u \hat F$ from $\psi(U)$ into the Banach space $\mathcal{L}(X_m, Y_m)$ of bounded linear operators (with the operator-norm topology) is continuous (by the definition of $C^1$ between Banach spaces).
> >
> > **Surjectivity is an open condition.** Each $d_u\hat F$ is a Fredholm operator (as $F$ is a Fredholm map). By [[Thm - Stabilisation of Fredholm Operators and Continuity of the Kernel|the stabilisation theorem]], part (ii) — *if $A_0 : X_m \to Y_m$ is a surjective Fredholm operator, then there is $\varepsilon > 0$ such that every bounded operator $A$ with $\lVert A - A_0 \rVert < \varepsilon$ is again surjective* (the dimension of the cokernel is upper semicontinuous and can only drop under small perturbation, and $0$ cannot drop) — there is $\varepsilon > 0$ with every operator within $\varepsilon$ of $d_{\psi(x_0)}\hat F$ surjective.
> >
> > **Combine.** By continuity of $u \mapsto d_u \hat F$ there is a neighbourhood $V \ni \psi(x_0)$ with $\lVert d_u \hat F - d_{\psi(x_0)}\hat F \rVert < \varepsilon$ for all $u \in V$; by the open condition, $d_u\hat F$ is surjective for every $u \in V$. Pulling back, $d_x F$ is surjective for every $x \in \psi^{-1}(V)$, an open neighbourhood of $x_0$. Hence the set of regular points is open, so $\operatorname{Crit}(F)$ is closed. $\blacksquare$

> [!note]- Lemma 2: On a Kuranishi neighbourhood the critical values have empty interior
> **Statement:** Let $p \in X$ and let $F \circ \phi(x_0, x_1) = T x_1 + f(x_0, x_1)$ be the [[Thm - Kuranishi Model for a Fredholm Map|Kuranishi normal form]] of $F$ on a chart neighbourhood $V$ of $0$, with $T : X_1 \to Y_0$ a linear isomorphism, $f$ smooth into the finite-dimensional space $Y_1$, and $X_0 = \ker d_p F$ finite-dimensional. Let $S \subseteq V$ be any subset. Then the set of critical values $F\phi\big(\operatorname{Crit}(F\phi) \cap S\big) \subseteq Y_0 \oplus Y_1$ has empty interior in $Y$.
>
> **Hint:** First reduce surjectivity of the full differential to surjectivity of the partial derivative $\partial_{x_0} f : X_0 \to Y_1$; then fix the $Y_0$-coordinate and apply the finite-dimensional [[Thm - Sard's Theorem for Smooth Maps|Sard theorem]] to a map between finite-dimensional spaces.
>
> **Why needed:** It is the crux of the whole theorem — the step where the finite-dimensional Sard theorem enters — and it makes the complement $R_p$ dense (Step 3 of the formal proof).
>
> > [!note]- Full proof
> > We treat the two cases $\dim Y_1 = 0$ and $\dim Y_1 \ge 1$; they are exhaustive because $Y_1$ is a finite-dimensional vector space.
> >
> > **Case $\dim Y_1 = 0$.** Then $Y = Y_0$ and $F\phi(x_0, x_1) = T x_1$. For every $(x_0, x_1)$ the differential $d(F\phi)_{(x_0,x_1)}(v_0, v_1) = T v_1$ is surjective, because $T : X_1 \to Y_0 = Y$ is an isomorphism. Hence $\operatorname{Crit}(F\phi) \cap V = \varnothing$, so $F\phi(\operatorname{Crit}(F\phi) \cap S) = \varnothing$, which has empty interior. This is the sub-case in which $p$ is a regular point.
> >
> > **Case $\dim Y_1 \ge 1$.** Write $\partial_{x_0} f|_{(x_0,x_1)} : X_0 \to Y_1$ and $\partial_{x_1} f|_{(x_0,x_1)} : X_1 \to Y_1$ for the partial derivatives of $f$ (both land in $Y_1$ because $f$ takes values in $Y_1$).
> >
> > **Reduce criticality to the finite-dimensional corner.** Differentiating the normal form,
> > $$d(F\phi)_{(x_0,x_1)}(v_0, v_1) \;=\; T v_1 + \partial_{x_0} f\, v_0 + \partial_{x_1} f\, v_1 \qquad \text{(chain rule on } Tx_1 + f(x_0,x_1)\text{, } T \text{ linear).}$$
> > Since $T v_1 \in Y_0$ and the derivatives of $f$ lie in $Y_1$, the $Y_0$- and $Y_1$-components of this map are
> > $$\pi_{Y_0}\, d(F\phi)(v_0,v_1) = T v_1, \qquad \pi_{Y_1}\, d(F\phi)(v_0,v_1) = \partial_{x_0} f\, v_0 + \partial_{x_1} f\, v_1.$$
> > We claim $d(F\phi)_{(x_0,x_1)}$ is surjective onto $Y_0 \oplus Y_1$ **if and only if** $\partial_{x_0} f|_{(x_0,x_1)} : X_0 \to Y_1$ is surjective. For the forward direction, suppose the full differential is surjective and let $w_1 \in Y_1$; there is $(v_0, v_1)$ with $T v_1 = 0$ and $\partial_{x_0} f\, v_0 + \partial_{x_1} f\, v_1 = w_1$, and $T v_1 = 0$ forces $v_1 = 0$ ($T$ injective), so $\partial_{x_0} f\, v_0 = w_1$; hence $\partial_{x_0} f$ is onto. For the converse, suppose $\partial_{x_0} f$ is onto and let $(w_0, w_1) \in Y_0 \oplus Y_1$ be arbitrary; set $v_1 := T^{-1} w_0$ (so $T v_1 = w_0$, using that $T$ is an isomorphism), and choose $v_0 \in X_0$ with $\partial_{x_0} f\, v_0 = w_1 - \partial_{x_1} f\, v_1$ (possible since $\partial_{x_0} f$ is onto); then $d(F\phi)(v_0, v_1) = (w_0, w_1)$. This proves the claim.
> >
> > **Identify criticality with criticality of a finite-dimensional map.** For fixed $x_1$ define the smooth map
> > $$g_{x_1} : X_0 \longrightarrow Y_1, \qquad g_{x_1}(x_0) := f(x_0, x_1),$$
> > between the finite-dimensional spaces $X_0$ and $Y_1$; its differential at $x_0$ is exactly $\partial_{x_0} f|_{(x_0,x_1)}$. By the claim, $(x_0, x_1)$ is a critical point of $F\phi$ if and only if $x_0$ is a critical point of $g_{x_1}$.
> >
> > **Compute the critical values slice by slice.** A point $(y_0, y_1) \in Y_0 \oplus Y_1$ is a critical value of $F\phi$ on $S$ precisely when there is a critical point $(x_0, x_1) \in S$ with $F\phi(x_0, x_1) = (y_0, y_1)$, that is, with $T x_1 = y_0$ and $f(x_0, x_1) = y_1$. The first equation determines $x_1 = T^{-1} y_0$ uniquely; substituting, the condition becomes: $x_0$ is a critical point of $g_{T^{-1}y_0}$, lies in the slice $S_{y_0} := \{x_0 : (x_0, T^{-1}y_0) \in S\}$, and satisfies $g_{T^{-1}y_0}(x_0) = y_1$. Therefore, for each fixed $y_0$,
> > $$\big\{\, y_1 \in Y_1 : (y_0, y_1) \text{ is a critical value of } F\phi \text{ on } S \,\big\} \;\subseteq\; g_{T^{-1}y_0}\big(\operatorname{Crit}(g_{T^{-1}y_0})\big),$$
> > the set of critical values of the finite-dimensional map $g_{T^{-1}y_0} : X_0 \to Y_1$. By [[Thm - Sard's Theorem for Smooth Maps|Sard's theorem]] — *the critical values of a smooth map between finite-dimensional manifolds form a set of Lebesgue measure zero* — this right-hand set has measure zero in $Y_1 \cong \mathbb{R}^{\dim Y_1}$. Hence every $y_0$-slice of the critical-value set is Lebesgue-null in $Y_1$.
> >
> > **From null slices to empty interior.** Suppose, for contradiction, that the critical-value set contained a nonempty open set $O \subseteq Y_0 \oplus Y_1$. Since the topology of $Y_0 \oplus Y_1$ is the product topology, $O$ contains a nonempty basic open box $O_0 \times O_1$ with $O_0 \subseteq Y_0$ and $O_1 \subseteq Y_1$ open and nonempty. Fix any $y_0 \in O_0$; then $\{y_0\} \times O_1 \subseteq O$ is contained in the critical-value set, so $O_1$ is contained in the $y_0$-slice, which we just showed is Lebesgue-null. But $O_1$ is a nonempty open subset of $Y_1 \cong \mathbb{R}^{\dim Y_1}$ with $\dim Y_1 \ge 1$, hence has strictly positive Lebesgue measure — contradicting nullity. Therefore the critical-value set contains no nonempty open set; it has empty interior. $\blacksquare$

> [!note]- Lemma 3: A second countable space is Lindelöf
> **Statement:** If a topological space $Z$ has a countable base, then every open cover of $Z$ has a countable subcover.
>
> **Hint:** For each covering set and each base element inside it, keep one covering set; there are only countably many base elements.
>
> **Why needed:** It reduces the a-priori uncountable cover of $X$ by Kuranishi neighbourhoods $\{U_p\}_{p \in X}$ to a countable one, so that the regular values are a *countable* intersection of open dense sets — the very definition of residual (Step 4 of the formal proof).
>
> > [!note]- Full proof
> > Let $\mathcal{B} = \{B_n\}_{n \in \mathbb{N}}$ be a countable base for $Z$ and let $\mathcal{U} = \{U_\alpha\}_{\alpha \in A}$ be an open cover. Let
> > $$\mathcal{N} := \{\, n \in \mathbb{N} : B_n \subseteq U_\alpha \text{ for some } \alpha \in A \,\}.$$
> > For each $n \in \mathcal{N}$ choose (this uses only countable choice, over the countable set $\mathcal{N}$) one index $\alpha_n \in A$ with $B_n \subseteq U_{\alpha_n}$. The family $\{U_{\alpha_n}\}_{n \in \mathcal{N}}$ is countable; we show it covers $Z$. Let $z \in Z$. Since $\mathcal{U}$ covers $Z$, there is $\alpha$ with $z \in U_\alpha$; since $\mathcal{B}$ is a base and $U_\alpha$ is open, there is $B_n \in \mathcal{B}$ with $z \in B_n \subseteq U_\alpha$. Then $n \in \mathcal{N}$, and $z \in B_n \subseteq U_{\alpha_n}$. Hence every point of $Z$ lies in some $U_{\alpha_n}$, so $\{U_{\alpha_n}\}_{n \in \mathcal{N}}$ is a countable subcover. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F : X \to Y$ be a smooth Fredholm map between second countable Banach manifolds. We must show that $\operatorname{Reg}(F) = Y \setminus F(\operatorname{Crit}(F))$ is a countable intersection of open dense subsets of $Y$, and is dense.
>
> **Step 0 — preliminaries in force.** Both $X$ and $Y$ are metrisable, by the [[Thm - Urysohn Metrization Theorem|Urysohn metrization theorem]] applied to the Hausdorff, regular, second countable spaces $X$ and $Y$ (regularity holds because they are locally metrisable). By Lemma 1, $\operatorname{Crit}(F)$ is closed in $X$. These two facts are used repeatedly below.
>
> **Step 1 — a proper closed local piece around each point.** Fix $p \in X$. By [[Thm - Proper Maps are Closed and Fredholm Maps are Locally Proper|the local-properness theorem]], part (ii) — *a smooth Fredholm map is locally proper: every $p$ has an open neighbourhood $U_p$, lying in a Kuranishi chart, whose closure $\overline{U_p}$ is a closed bounded set on which $F|_{\overline{U_p}}$ is proper (preimages of compact sets are compact)* — we obtain such a $U_p$ with $\overline{U_p}$ contained in the domain of a chart on which $F$ has the [[Thm - Kuranishi Model for a Fredholm Map|Kuranishi normal form]] $F\phi(x_0,x_1) = Tx_1 + f(x_0,x_1)$.
>
> **Step 2 — the critical values on $\overline{U_p}$ are closed.** The set $\operatorname{Crit}(F) \cap \overline{U_p}$ is closed in $X$, being the intersection of the closed set $\operatorname{Crit}(F)$ (Step 0) with the closed set $\overline{U_p}$; in particular it is a closed subset of $\overline{U_p}$. By [[Thm - Proper Maps are Closed and Fredholm Maps are Locally Proper|the same theorem]], part (i) — *a proper continuous map into a metrisable space is closed (it sends closed sets to closed sets)* — applied to the proper map $F|_{\overline{U_p}}$ into the metrisable space $Y$ (Step 0), the image
> $$F\big(\operatorname{Crit}(F) \cap \overline{U_p}\big) \subseteq Y \qquad \text{is closed.}$$
>
> **Step 3 — the critical values on $\overline{U_p}$ have empty interior.** Apply Lemma 2 with $S := \phi^{-1}(\overline{U_p})$, the closed piece read in the Kuranishi chart (which lies in the chart domain $V$ by Step 1). Lemma 2 gives that $F\phi(\operatorname{Crit}(F\phi) \cap S)$ has empty interior; since $\phi$ is a diffeomorphism onto its image and $\overline{U_p} = \phi(S)$, this set equals $F(\operatorname{Crit}(F) \cap \overline{U_p})$. Hence
> $$F\big(\operatorname{Crit}(F) \cap \overline{U_p}\big) \qquad \text{has empty interior in } Y.$$
>
> **Step 4 — the complement is open and dense.** Set $R_p := Y \setminus F(\operatorname{Crit}(F) \cap \overline{U_p})$. By Step 2 the removed set is closed, so $R_p$ is open; by Step 3 the removed set is closed with empty interior, hence nowhere dense, so its complement $R_p$ is dense. Thus **each $R_p$ is open and dense in $Y$.**
>
> **Step 5 — pass to a countable subcover.** The family $\{U_p\}_{p \in X}$ is an open cover of $X$ (each $p$ lies in its own $U_p$). Since $X$ is second countable, Lemma 3 (second countable implies Lindelöf) yields a countable subcover $\{U_{p_i}\}_{i \in \mathbb{N}}$, so
> $$X = \bigcup_{i} U_{p_i} \subseteq \bigcup_i \overline{U_{p_i}} \subseteq X, \qquad \text{hence } \bigcup_i \overline{U_{p_i}} = X.$$
>
> **Step 6 — the regular values are exactly $\bigcap_i R_{p_i}$.** Because $\bigcup_i \overline{U_{p_i}} = X$ (Step 5), every critical point lies in some $\overline{U_{p_i}}$, so
> $$F\big(\operatorname{Crit}(F)\big) = F\Big(\bigcup_i \big(\operatorname{Crit}(F) \cap \overline{U_{p_i}}\big)\Big) = \bigcup_i F\big(\operatorname{Crit}(F) \cap \overline{U_{p_i}}\big) \qquad \text{(image of a union is the union of images).}$$
> Taking complements,
> $$\operatorname{Reg}(F) = Y \setminus F\big(\operatorname{Crit}(F)\big) = Y \setminus \bigcup_i F\big(\operatorname{Crit}(F) \cap \overline{U_{p_i}}\big) = \bigcap_i \Big( Y \setminus F\big(\operatorname{Crit}(F) \cap \overline{U_{p_i}}\big) \Big) = \bigcap_i R_{p_i} \qquad \text{(De Morgan).}$$
> By Step 4 each $R_{p_i}$ is open and dense, so $\operatorname{Reg}(F)$ is a countable intersection of open dense subsets of $Y$ — a **residual** set, by definition.
>
> **Step 7 — density.** By [[Def - Residual Set and Generic Property|the density of residual sets]] — *a residual subset of a Banach manifold is dense, because such a manifold is a Baire space (it is locally completely metrisable and second countable, so the [[Thm - Baire Category Theorem|Baire category theorem]] applies), and in a Baire space a countable intersection of open dense sets is dense* — the residual set $\operatorname{Reg}(F)$ is dense in $Y$.
>
> **Conclusion.** The set of regular values of $F$ is residual in $Y$ and dense. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The fundamental theorem of algebra as a degree computation.** View a complex polynomial $p : \mathbb{C} \to \mathbb{C}$ of degree $k$ as a smooth map $\mathbb{R}^2 \to \mathbb{R}^2$. It is a finite-dimensional, hence Fredholm, map of index $0$, and it is proper. Sard–Smale (here just Sard) gives a dense set of regular values; over a regular value the preimage is a finite set whose count, taken mod $2$ or with sign, is the degree. The theorem applies because a finite-dimensional smooth map is automatically Fredholm — the non-obvious recognition being that the classical Sard theorem one uses here is literally the finite-dimensional instance of the infinite-dimensional statement.

**Generic level sets of a semilinear elliptic equation.** On a closed Riemannian surface consider $F : W^{2,2} \to L^2$, $F(u) = \Delta u + u^3$. Using the Sobolev multiplication theorem for smoothness and the Rellich theorem for the compactness of $u \mapsto u^3$'s linearisation, $F$ is a smooth Fredholm map of index $0$. Sard–Smale then delivers a dense set of $w$ for which the solution set of $\Delta u + u^3 = w$ is a compact $0$-manifold, so that the number of solutions is finite and locally constant in $w$. This is non-obvious because nothing in the equation looks measure-theoretic, yet genericity of $w$ is exactly a Sard–Smale conclusion.

**Transversality of two submanifolds of a Hilbert manifold via a defining map.** Given a Fredholm map $F : X \to Y$ and a finite-dimensional embedded submanifold $Z \subseteq Y$ cut out locally as the zero set of a submersion $g$, the composite $g \circ F$ is Fredholm, and Sard–Smale supplies regular values of $g \circ F$; translating back, a small generic perturbation makes $F$ transverse to $Z$, so $F^{-1}(Z)$ is a manifold of dimension $\operatorname{index} F + \dim Z$. The application is non-obvious because transversality of $F$ to $Z$ is recast as regularity of a value of a *different* Fredholm map, the one that defines $Z$.

---

# Bridges

- **[[Thm - Regular Value and Transversality Theorems for Fredholm Maps|The regular-value theorem for Fredholm maps]]** — the natural partner. Sard–Smale produces the regular value; the regular-value theorem tells you what its preimage looks like, namely a smooth submanifold of dimension $\operatorname{index} F$ with tangent space $\ker d_x F$. The two are always used in tandem: existence of a regular value, then the structure of its level set. The bridge is direct — Sard–Smale is the hypothesis-supplier for the regular-value theorem — and requires no intermediate construction.

- **[[Def - Mod-2 Degree of a Proper Fredholm Map|The mod-2 and integer degrees]]** — the first serious payoff. For a proper Fredholm map of index $0$, Sard–Smale guarantees regular values, over each of which the preimage is a compact $0$-manifold, hence finite. Counting the preimage (mod $2$, or with orientations via the [[Def - Determinant Line Bundle of a Family of Fredholm Operators|determinant line bundle]]) defines a degree; its independence of the chosen regular value and its homotopy invariance are proved separately, but its very definability rests on Sard–Smale.

- **[[Thm - Parametric Transversality|Parametric transversality]]** — the form used in gauge theory. When the value $y$ is pinned by symmetry and cannot be moved, one introduces a parameter $w \in W$ and a family $\mathcal F : X \times W \to Y$, and applies Sard–Smale not to the individual maps but to the projection $\pi : \mathcal F^{-1}(y) \to W$. The construction that makes this work is the identification of $\operatorname{coker} d\pi$ with $\operatorname{coker} d_x \mathcal F_w$; granted that, Sard–Smale on $\pi$ says a residual set of parameters make $y$ regular for $\mathcal F_w$. This is the route to the generic smoothness of the [[Def - Seiberg-Witten Moduli Space|Seiberg–Witten moduli space]].

- **[[Thm - Sard's Theorem for Smooth Maps|Sard's theorem in finite dimensions]]** — both the special case and the engine. Sard–Smale contains Sard as the finite-dimensional instance, and simultaneously *uses* Sard as the one place where a genuine measure-theoretic fact is imported: the whole infinite-dimensional apparatus exists only to reduce the problem, in a Kuranishi chart, to Sard on a map between the finite-dimensional kernel and cokernel.

---

# Unlocked by This

> [!tip] Generic regularity of moduli spaces *(from Gauge Theory)*
> Together with [[Thm - Parametric Transversality|parametric transversality]], this theorem is what lets one say that "for a generic metric" or "for a generic perturbation" the anti-self-dual and Seiberg–Witten moduli spaces are smooth manifolds of the expected dimension. See **Generic Regularity and Orientability of the Seiberg–Witten Moduli Space**.

> [!tip] Degree theory in infinite dimensions *(from Nonlinear Analysis)*
> The Leray–Schauder degree for compact perturbations of the identity, and its Fredholm refinement, are built on exactly this genericity: a dense supply of regular values with finite preimage. See [[Def - Mod-2 Degree of a Proper Fredholm Map|the mod-2 degree]].
