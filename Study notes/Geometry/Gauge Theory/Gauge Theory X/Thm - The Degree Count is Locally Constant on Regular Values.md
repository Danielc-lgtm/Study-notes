---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Mod-2 Degree of a Proper Fredholm Map"
  - "Thm - Inverse Function Theorem on Banach Spaces"
  - "Thm - Proper Maps are Closed and Fredholm Maps are Locally Proper"
  - "Def - Fredholm Map and Its Index"
  - "Def - Fredholm Operator and Index"
  - "Def - Regular Value and Transversality for Fredholm Maps"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $X$ and $Y$ are smooth Banach manifolds that are Hausdorff and second countable; every Banach manifold in this series is therefore metrisable, a fact we use freely and recall where it does work. For a smooth map $F : X \to Y$ and a point $x \in X$, the symbol $d_x F : T_x X \to T_{F(x)} Y$ denotes the differential (the Fréchet derivative read in charts), a bounded linear map between the model Banach spaces of $X$ at $x$ and of $Y$ at $F(x)$; the notion of tangent space and of smooth map between Banach manifolds is the one fixed on **[[Def - Banach Manifold and Smooth Maps between Banach Spaces]]**.

The map $F$ is a **[[Def - Fredholm Map and Its Index|Fredholm map]]** if each differential $d_x F$ is a **[[Def - Fredholm Operator and Index|Fredholm operator]]**: a bounded linear map $T : E \to G$ between Banach spaces whose kernel $\ker T = \{v \in E : Tv = 0\}$ is finite-dimensional and whose image $\operatorname{im} T = T(E)$ is closed of finite codimension, with **index** $\operatorname{index} T = \dim \ker T - \dim \operatorname{coker} T$, where the cokernel is $\operatorname{coker} T = G / \operatorname{im} T$. On a connected $X$ this integer is the same at every point (the index is locally constant, proved on [[Def - Fredholm Map and Its Index]]), written $\operatorname{index} F$. We assume $\operatorname{index} F = 0$ throughout.

A point $y \in Y$ is a **[[Def - Regular Value and Transversality for Fredholm Maps|regular value]]** of $F$ if $d_x F$ is surjective for every $x \in F^{-1}(y)$; this holds vacuously when $F^{-1}(y) = \varnothing$. The set of regular values is written $Y_{\mathrm{reg}} \subseteq Y$; its complement is the set of critical values. A map $F$ is **[[Def - Mod-2 Degree of a Proper Fredholm Map|proper]]** if the preimage $F^{-1}(K)$ of every compact $K \subseteq Y$ is compact. The symbol $\#S$ denotes the cardinality of a finite set $S$, $\sqcup$ and $\bigsqcup$ denote disjoint union, and $\blacksquare$ closes a proof. Chart-metric balls are written $B(y, r) = \{y' : d_Y(y', y) < r\}$ for a metric $d_Y$ on $Y$ compatible with its topology.

> [!warning] Convention: index and regularity
> We follow Haydys throughout. A regular value asks only that $d_x F$ be *surjective* at each preimage point — not that $d_x F$ be an isomorphism — because in infinite dimensions a surjective differential can still have a kernel. It is the extra hypothesis $\operatorname{index} F = 0$ that upgrades surjectivity to invertibility, and this upgrade is the first step of the proof below. Where a source writes "$0$ is a regular value" it means $y = 0$ in the target; we keep a general regular value $y$.

---

# Statement

> **Theorem (the degree count is locally constant on regular values).** Let $F : X \to Y$ be a proper Fredholm map of index $0$ between second-countable Banach manifolds, and let $y \in Y$ be a regular value of $F$ with $F^{-1}(y) = \{x_1, \dots, x_k\}$ (a finite set, possibly empty). Then there exist pairwise disjoint open sets $V_1, \dots, V_k \subseteq X$ with $x_j \in V_j$, and an open set $U \subseteq Y$ with $y \in U$, such that
> $$F|_{V_j} : V_j \longrightarrow U \quad \text{is a diffeomorphism for each } j, \qquad\text{and}\qquad F^{-1}(U) \subseteq \bigsqcup_{j=1}^{k} V_j.$$
> Consequently every $y' \in U$ is a regular value of $F$ with $\#F^{-1}(y') = k$. Hence the function
> $$N : Y_{\mathrm{reg}} \longrightarrow \mathbb{Z}_{\ge 0}, \qquad N(y) = \#F^{-1}(y),$$
> is locally constant on the open set $Y_{\mathrm{reg}}$ of regular values.

When $k = 0$ the statement reads: there is an open $U \ni y$ with $F^{-1}(U) = \varnothing$, so $N \equiv 0$ near $y$. The finiteness of $F^{-1}(y)$ is not an extra assumption but a consequence of the standing hypotheses, recalled in the Motivation.

---

# Motivation

The mod-2 degree $\deg_2 F$ of a proper index-zero Fredholm map is *defined* as the parity $\#F^{-1}(y) \bmod 2$ of the number of solutions of $F(x) = y$ over a regular value $y$ (**[[Def - Mod-2 Degree of a Proper Fredholm Map]]**). For this definition to mean anything, two independent facts must hold. First, the count $\#F^{-1}(y)$ must be a finite number, so that its parity is defined; this is where properness and index zero earn their keep, because $F^{-1}(y)$ is then a compact zero-dimensional manifold, hence a finite set of points. Second — and this is the present theorem — the parity must not jump wildly as the chosen regular value $y$ is nudged; the count has to be *stable* under small perturbations of $y$.

This page supplies the second fact in its sharpest local form: not merely that the parity is locally constant, but that the honest integer count $N(y) = \#F^{-1}(y)$ itself is locally constant on the open set of regular values. It is the workhorse behind the well-definedness of the degree. The full argument that $\deg_2 F$ is independent of the regular value chosen, and is a homotopy invariant, proceeds in six steps (**[[Thm - Well-Definedness and Homotopy Invariance of the Degree]]**); this theorem is Step 2 of that argument, isolated here and proved completely. In the source (Haydys, Theorem 166, Step 2, p. 54) the local diffeomorphism part is given in three lines and the crucial properness estimate — the containment $F^{-1}(U) \subseteq \bigsqcup_j V_j$ after shrinking $U$ — is asserted parenthetically without proof. We restore that estimate in full, since without it the neighbourhoods $V_j$ might fail to catch *all* the solutions over a nearby $y'$, and the count could rise.

The theorem is the infinite-dimensional analogue of an elementary fact in finite dimensions: a smooth map between manifolds of equal dimension is, near a regular value, a covering of a small ball by finitely many sheets, and the number of sheets — the local degree — cannot change as long as one stays over regular values. The Banach setting adds exactly one genuine difficulty, which is that a target ball need not be small enough to be covered by the sheets alone; properness is what confines the solutions and rules out mass escaping to infinity.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is a proper Fredholm map of index zero with a regular value in hand. The interesting question is when a problem hands you such a map without announcing it.

The first disguised source is **a nonlinear elliptic boundary-value or field equation whose linearisation is elliptic**. A map of the form $u \mapsto L u + N(u)$, with $L$ a linear elliptic operator between Sobolev completions and $N$ a lower-order nonlinearity, has differential $d_u F = L + d_u N$, an elliptic operator perturbed by a compact term; elliptic operators on closed manifolds are Fredholm (**[[Thm - Elliptic Operators on Closed Manifolds are Fredholm]]**) and the Fredholm property survives compact perturbation (**[[Thm - Stability of the Fredholm Property under Small and Compact Perturbations]]**), so $F$ is a Fredholm map, and one tunes the domain and target Sobolev exponents to make the index vanish. The bridge $B \Rightarrow A$ here is "elliptic with vanishing analytic index" $\Rightarrow$ "index-zero Fredholm map". *Example problem:* count, modulo $2$, the solutions of a semilinear equation $\Delta u + f(u) = g$ on a closed surface as $g$ ranges over generic right-hand sides, once properness is arranged by an a priori bound.

The second disguised source is **a finite-dimensional smooth map between manifolds of equal dimension that happens to be proper**. Every such map is trivially Fredholm of index $\dim X - \dim Y = 0$, its differential a square matrix, and properness is automatic when the domain is compact. The theorem then reduces to the classical local-covering statement, and this is the case in which the reader should first check the argument. *Example problem:* a proper polynomial map $\mathbb{R}^n \to \mathbb{R}^n$ (properness follows from a growth estimate $|F(x)| \to \infty$), whose local sheet count over regular values is the object studied in **[[Ex - The Mod-2 Degree of a Complex Polynomial Map]]**.

The third disguised source is **a family of Fredholm maps restricted to one parameter value**. In the parametric transversality setup one is given $\mathcal{F} : X \times W \to Y$ with each slice $\mathcal{F}_w = \mathcal{F}(\cdot, w)$ Fredholm and proper; fixing $w$ produces exactly a map of the kind this theorem governs, and the theorem is what lets one transport the count from one generic parameter to another. The non-obviousness is that the single map inherits properness and the index from the family, not from any structure visible in $\mathcal{F}_w$ alone. *Example problem:* show that the generic-parameter count is the same for all $w$ in a connected parameter space, the content of **[[Thm - The Generic Parametric Count Defines the Mod-2 Degree]]**.

**Targets (Output Amplification)**

The bare conclusion is a locally constant integer count near a regular value.

Combine the conclusion with **connectedness of the target $Y$ together with the density of regular values**. Local constancy on the open set $Y_{\mathrm{reg}}$ does not by itself make $N$ globally constant, because $Y_{\mathrm{reg}}$ can be disconnected even when $Y$ is connected. The extra ingredient is a diffeomorphism of $Y$, homotopic to the identity, carrying one regular value to another (Steps 4–6 of **[[Thm - Well-Definedness and Homotopy Invariance of the Degree]]**), which shows the *parity* is the same across components of $Y_{\mathrm{reg}}$. The payoff $E$ is that $\deg_2 F$ is a single well-defined element of $\mathbb{Z}/2$, and the present theorem is exactly what makes it locally well-defined before that global bridge is built.

Combine the conclusion with **an orientation of the family of differentials**, packaged as a trivialisation of the determinant line bundle. Then each local diffeomorphism $F|_{V_j}$ carries a sign $\varepsilon_j \in \{\pm 1\}$, and the locally constant count refines to a locally constant *signed* count $\sum_j \varepsilon_j$ (**[[Def - Integer Degree of an Oriented Proper Fredholm Map]]**, **[[Def - Determinant Line Bundle of a Family of Fredholm Operators]]**). The payoff is the integer-valued degree, a strictly finer invariant than the parity, obtained by decorating the very neighbourhoods this theorem produces.

Combine the conclusion with **the observation that a nonzero count forces a nonempty preimage everywhere**. If $N(y) \ne 0$ over some regular value and the count is a homotopy invariant, then no proper homotopy can reduce it to zero, so $F$ must be surjective onto a neighbourhood of $Y_{\mathrm{reg}}$ and, by density, onto $Y$. The payoff $E$ is a solvability theorem: $F(x) = y'$ has a solution for every $y'$ (**[[Thm - Nonzero Degree Implies Surjectivity]]**), an existence result extracted from a counting argument with no fixed-point theorem in sight.

---

# Why Is It True

Forget the estimates and picture the map near the fibre over $y$. There are finitely many solutions $x_1, \dots, x_k$ of $F(x) = y$. At each of them the differential $d_{x_j} F$ is surjective because $y$ is regular, and it has index zero because $F$ does; a surjective linear map of index zero has no kernel, so it is invertible. An invertible differential means $F$ looks, near $x_j$, exactly like an invertible linear map looks near a point: it stretches a small neighbourhood $V_j$ of $x_j$ diffeomorphically onto a small neighbourhood of $y$. So over a small enough ball $U$ around $y$, the map $F$ has, near each $x_j$, precisely one sheet — one solution of $F(x) = y'$ for each $y' \in U$.

That gives at least $k$ solutions over each nearby $y'$. The one thing that could go wrong is that a *new* solution, born far away from all the $x_j$, could sail into the picture as $y'$ moves — a solution not accounted for by any $V_j$. This is where properness intervenes and where the source is silent. If such intruders existed for arbitrarily small balls around $y$, we would have a sequence of them $x_n$ with $F(x_n) \to y$; properness says the preimage of the compact set $\{F(x_n)\} \cup \{y\}$ is compact, so the $x_n$ cannot escape to infinity — they must accumulate, and their limit is forced to be a solution of $F(x) = y$, that is, one of the $x_j$. But then the intruders were sitting arbitrarily close to $x_j$, so they were in $V_j$ after all, contradicting their intruder status. Properness is precisely the hypothesis that forbids solutions from leaking in from infinity.

> **Mechanism in one sentence:** near a regular value a proper index-zero Fredholm map is a finite covering — invertible differentials make it a covering, and properness makes the number of sheets a complete count — so the number of solutions is locally constant.

---

# What Makes This Hard

The subtle point is not the local diffeomorphisms; those follow mechanically from the inverse function theorem once one notices that index zero plus surjectivity gives invertibility. The genuine difficulty is the containment $F^{-1}(U) \subseteq \bigsqcup_j V_j$: choosing $U$ small enough that the neighbourhoods $V_j$ capture *every* solution over $U$, not just the ones near the original $x_j$. In finite dimensions with a compact domain this is nearly free; in the Banach setting a solution can in principle wander off to infinity, and only properness confines it. The common error is to prove the local diffeomorphism statement and then assert the count without this containment — exactly the gap in the source — which silently assumes no solutions appear from outside the $V_j$. The second trap is forgetting that "regular value" in infinite dimensions means surjective, not bijective, differential; without the index-zero hypothesis the differential could be surjective with an infinite-dimensional kernel and $F$ would not be locally injective at all.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Turn each solution into a single sheet by inverting the differential and applying the inverse function theorem, then use properness to prove that a small enough target ball has no solutions outside those sheets, and finally read off the count.

**Subgoal decomposition:**

1. **Invertibility of the differential at each solution.** Show that at every $x_j$ the differential $d_{x_j} F$ is a Banach-space isomorphism.
   - *Hint:* Regularity gives surjectivity, so the cokernel is zero; index zero then forces the kernel to be zero; a continuous linear bijection between Banach spaces is an isomorphism by the open mapping theorem.
   - *Why needed:* The inverse function theorem needs an invertible, not merely surjective, differential.

2. **A single sheet at each solution.** Produce disjoint open $V_j \ni x_j$ and one common open $U \ni y$ with $F|_{V_j} : V_j \to U$ a diffeomorphism.
   - *Hint:* Apply the Banach inverse function theorem at each $x_j$; use that $X$ is Hausdorff and $k$ is finite to make the neighbourhoods disjoint; intersect the images to get a common target $U$ and pull back.
   - *Why needed:* This puts exactly one solution over each $y' \in U$ inside each $V_j$.

3. **No solutions escape the sheets.** Show that after shrinking $U$, $F^{-1}(U) \subseteq \bigsqcup_j V_j$.
   - *Hint:* Suppose not; extract a sequence of stray solutions over $y_n \to y$; the set $\{y_n\} \cup \{y\}$ is compact, so properness makes the strays accumulate at a solution over $y$, i.e. at some $x_j$, contradicting that they avoid $V_j$.
   - *Why needed:* Without it the count over $y'$ could exceed $k$.

4. **The count and its regularity.** For $y' \in U$ show $\#F^{-1}(y') = k$ and $y'$ is regular; treat $k = 0$ separately via closedness of $F(X)$.
   - *Hint:* Each $V_j$ contributes exactly one preimage of $y'$ and, being a diffeomorphism image, keeps the differential invertible. For $k = 0$ use that a proper map into a metrisable space is closed.
   - *Why needed:* This is the conclusion, and local constancy is its immediate corollary.

---

# Lemma Decomposition

> [!note]- Lemma 1: A surjective Fredholm operator of index zero is a Banach-space isomorphism
> **Statement:** Let $T : E \to G$ be a bounded linear operator between Banach spaces that is Fredholm with $\operatorname{index} T = 0$. If $T$ is surjective, then $T$ is a bijection and its inverse $T^{-1} : G \to E$ is bounded; that is, $T$ is a topological linear isomorphism.
>
> **Hint:** Surjectivity kills the cokernel; the index equation then kills the kernel; invoke the open mapping theorem for the boundedness of the inverse.
>
> **Why needed:** It converts the analytic hypothesis "$y$ is a regular value" (surjective differentials) into the algebraic hypothesis the inverse function theorem requires (invertible differentials).
>
> > [!note]- Full proof
> > **Cokernel is zero.** By hypothesis $T$ is surjective, so $\operatorname{im} T = G$ and the cokernel $\operatorname{coker} T = G / \operatorname{im} T = G / G = \{0\}$ is the trivial vector space; hence $\dim \operatorname{coker} T = 0$.
> >
> > **Kernel is zero.** By the definition of the Fredholm index, $\operatorname{index} T = \dim \ker T - \dim \operatorname{coker} T$. Substituting $\operatorname{index} T = 0$ (hypothesis) and $\dim \operatorname{coker} T = 0$ (previous paragraph) gives
> > $$0 = \dim \ker T - 0, \qquad \text{so} \qquad \dim \ker T = 0 \quad \text{(solving the index equation).}$$
> > Thus $\ker T = \{0\}$, and $T$ is injective.
> >
> > **Bijection with bounded inverse.** Being surjective (hypothesis) and injective (previous paragraph), $T : E \to G$ is a bijection, so it has a linear inverse $T^{-1} : G \to E$. Both $E$ and $G$ are Banach spaces and $T$ is a bounded linear surjection, so by the open mapping theorem — for a bounded linear surjection between Banach spaces the image of every open set is open, restated on [[Thm - Banach–Steinhaus and Open Mapping (Application of Baire)|the open mapping theorem]] — the map $T$ is open. An open bijection has continuous inverse: for any open $O \subseteq E$, the preimage $(T^{-1})^{-1}(O) = T(O)$ is open, so $T^{-1}$ is continuous, that is, bounded (linearity plus continuity at $0$). Therefore $T$ is a topological linear isomorphism. $\blacksquare$

> [!note]- Lemma 2: Local diffeomorphism onto a common target at the solutions
> **Statement:** Let $F : X \to Y$ be a smooth Fredholm map of index $0$ between Banach manifolds, and let $y$ be a regular value with $F^{-1}(y) = \{x_1, \dots, x_k\}$ finite. Then there exist pairwise disjoint open sets $V_1, \dots, V_k \subseteq X$ with $x_j \in V_j$ and a single open set $U \subseteq Y$ with $y \in U$ such that $F|_{V_j} : V_j \to U$ is a diffeomorphism for every $j$.
>
> **Hint:** Invert each differential by Lemma 1, apply the Banach inverse function theorem at each $x_j$, separate the finitely many points by the Hausdorff property, take $U$ to be the intersection of the sheet images, and pull it back.
>
> **Why needed:** It produces one sheet over each $y' \in U$ at each solution; the count $\ge k$ comes from here.
>
> > [!note]- Full proof
> > **Invert the differentials.** Fix $j \in \{1, \dots, k\}$. Since $y$ is a regular value, $d_{x_j} F : T_{x_j} X \to T_y Y$ is surjective; since $\operatorname{index} F = 0$, this Fredholm operator has index $0$. By Lemma 1, $d_{x_j} F$ is a Banach-space isomorphism.
> >
> > **Apply the inverse function theorem.** By the inverse function theorem on Banach manifolds — restated: *if a smooth map has invertible differential at a point, it restricts to a diffeomorphism between an open neighbourhood of that point and an open neighbourhood of its image* ([[Thm - Inverse Function Theorem on Banach Spaces|inverse function theorem]], part (i)) — there are open sets $W_j \ni x_j$ and $O_j \ni y$ with $F|_{W_j} : W_j \to O_j$ a diffeomorphism.
> >
> > **Separate the solutions.** The Banach manifold $X$ is Hausdorff, and $\{x_1, \dots, x_k\}$ is a finite set of distinct points. For each ordered pair $i \ne j$ choose disjoint open sets $P_{ij} \ni x_i$ and $Q_{ij} \ni x_j$ (Hausdorff property), and set $W_j' := W_j \cap \bigcap_{i \ne j} Q_{ij}$. Then $W_j'$ is open, contains $x_j$, is contained in $W_j$, and $W_i' \cap W_j' = \varnothing$ for $i \ne j$ (because $W_i' \subseteq P_{ij}$ and $W_j' \subseteq Q_{ij}$ are disjoint). Restricting the diffeomorphism $F|_{W_j}$ to the open subset $W_j' \subseteq W_j$ keeps it a diffeomorphism onto its image $F(W_j')$, which is open in $O_j$ (a diffeomorphism is an open map) and contains $y$.
> >
> > **Build the common target and pull it back.** Set $U := \bigcap_{j=1}^{k} F(W_j')$. As a finite intersection of open sets each containing $y$, the set $U$ is open and $y \in U$. For each $j$, since $U \subseteq F(W_j')$ and $F|_{W_j'} : W_j' \to F(W_j')$ is a diffeomorphism, its restriction to the preimage of the open subset $U$,
> > $$V_j := \big(F|_{W_j'}\big)^{-1}(U) = W_j' \cap F^{-1}(U),$$
> > is an open subset of $W_j'$ mapped diffeomorphically by $F$ onto $U$. The $V_j$ inherit pairwise disjointness from the $W_j'$ ($V_j \subseteq W_j'$), each contains $x_j$ (because $F(x_j) = y \in U$ and $x_j \in W_j'$), and $F|_{V_j} : V_j \to U$ is a diffeomorphism. $\blacksquare$

> [!note]- Lemma 3: Properness confines the preimage to a given cover of a fibre
> **Statement:** Let $F : X \to Y$ be a proper continuous map with $Y$ metrisable and $X$ Hausdorff, let $y \in Y$, and suppose $F^{-1}(y) = \{x_1, \dots, x_k\}$ is finite. If $V_1, \dots, V_k \subseteq X$ are open sets with $x_j \in V_j$, then there is an open set $U \subseteq Y$ with $y \in U$ and $F^{-1}(U) \subseteq \bigcup_{j=1}^{k} V_j$. (The statement holds trivially with any $U$ containing no other solutions when $k = 0$, treated separately below.)
>
> **Hint:** Argue by contradiction using a shrinking sequence of balls; a convergent sequence together with its limit is compact, so properness makes the stray points accumulate at a point of the fibre.
>
> **Why needed:** This is the properness estimate the source omits; it guarantees the sheets $V_j$ catch every nearby solution, so the count over $y'$ is exactly $k$ and not more.
>
> > [!note]- Full proof
> > Assume $k \ge 1$ (the case $k = 0$ is handled in the formal proof by closedness of the image). Write $V := \bigcup_{j=1}^{k} V_j$, an open set containing the whole fibre $F^{-1}(y)$. Fix a metric $d_Y$ on $Y$ compatible with its topology, which exists because $Y$ is metrisable.
> >
> > **Set up the contradiction.** Suppose, for contradiction, that *no* open neighbourhood of $y$ has its preimage contained in $V$. In particular, for each integer $n \ge 1$ the ball $B(y, 1/n) = \{y' \in Y : d_Y(y', y) < 1/n\}$ is an open neighbourhood of $y$, so by our assumption $F^{-1}(B(y, 1/n)) \not\subseteq V$. Choose a point
> > $$x_n \in F^{-1}\big(B(y, 1/n)\big) \setminus V, \qquad \text{and set } \; y_n := F(x_n).$$
> > Then $y_n \in B(y, 1/n)$, so $d_Y(y_n, y) < 1/n$, whence $y_n \to y$ as $n \to \infty$ (by definition of convergence in $(Y, d_Y)$).
> >
> > **Compactness of the target sequence.** The set $K := \{y_n : n \ge 1\} \cup \{y\}$ is compact: given any open cover, one member contains the limit $y$, hence contains all $y_n$ with $n$ beyond some $N$ (since $y_n \to y$), and finitely many further members cover the remaining $y_1, \dots, y_N$. (This is the standard fact that a convergent sequence together with its limit is compact.)
> >
> > **Properness makes the strays accumulate.** By properness of $F$, the preimage $F^{-1}(K)$ is compact. Each $x_n$ satisfies $F(x_n) = y_n \in K$, so $x_n \in F^{-1}(K)$ for all $n$. A compact subset of a metric space is sequentially compact — by [[Thm - Compactness in Metric Spaces (Three Equivalents)|the equivalence of compactness, limit-point compactness, and sequential compactness in metric spaces]], and $F^{-1}(K)$ is metrisable as a subspace of the metrisable $X$ — so the sequence $(x_n)$ has a subsequence $(x_{n_\ell})_{\ell \ge 1}$ converging to some $x_\infty \in F^{-1}(K)$.
> >
> > **Locate the limit in the fibre.** By continuity of $F$,
> > $$F(x_\infty) = \lim_{\ell \to \infty} F(x_{n_\ell}) = \lim_{\ell \to \infty} y_{n_\ell} = y \qquad \text{(continuity of } F \text{; then } y_{n_\ell} \to y \text{ as a subsequence of } y_n \to y).$$
> > Hence $x_\infty \in F^{-1}(y) = \{x_1, \dots, x_k\}$, so $x_\infty = x_j$ for some fixed $j$.
> >
> > **Derive the contradiction.** The set $V_j$ is an open neighbourhood of $x_j = x_\infty$, and $x_{n_\ell} \to x_\infty$, so there is $L$ with $x_{n_\ell} \in V_j \subseteq V$ for all $\ell \ge L$. This contradicts the choice $x_{n_\ell} \notin V$ made in the first paragraph. The contradiction is between "$x_{n_\ell} \in V$ for large $\ell$" and "$x_n \notin V$ for every $n$".
> >
> > **Conclude.** The assumption was false: some open neighbourhood $U$ of $y$ satisfies $F^{-1}(U) \subseteq V = \bigcup_{j=1}^{k} V_j$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F : X \to Y$ be a proper Fredholm map of index $0$ between second-countable Banach manifolds and let $y$ be a regular value.
>
> **Step 0 — preconditions: the fibre is finite.** Because $y$ is a regular value and $\operatorname{index} F = 0$, the regular-value theorem for Fredholm maps ([[Thm - Inverse Function Theorem on Banach Spaces|regular-value theorem]], part (iii): *if $y$ is a regular value of a Fredholm map then $F^{-1}(y)$ is an embedded submanifold of dimension $\operatorname{index} F$*) shows $F^{-1}(y)$ is a smooth manifold of dimension $\operatorname{index} F = 0$, that is, a discrete set of points. It is compact: the one-point set $\{y\}$ is compact and $F$ is proper, so $F^{-1}(\{y\}) = F^{-1}(y)$ is compact. A compact discrete space is finite, so we may write $F^{-1}(y) = \{x_1, \dots, x_k\}$ with $k \ge 0$. We treat $k \ge 1$ first and dispose of $k = 0$ in Step 4.
>
> **Step 1 — one sheet at each solution over a common target.** Assume $k \ge 1$. By Lemma 2 (whose hypotheses — $F$ a smooth index-zero Fredholm map, $y$ a regular value, $F^{-1}(y)$ finite — all hold by Step 0), there are pairwise disjoint open sets $V_1^{(0)}, \dots, V_k^{(0)} \subseteq X$ with $x_j \in V_j^{(0)}$ and an open set $U^{(0)} \ni y$ such that
> $$F|_{V_j^{(0)}} : V_j^{(0)} \longrightarrow U^{(0)} \quad \text{is a diffeomorphism for each } j. \tag{1}$$
> This gives, over each $y' \in U^{(0)}$, exactly one solution inside each $V_j^{(0)}$; it does not yet rule out solutions outside $\bigsqcup_j V_j^{(0)}$.
>
> **Step 2 — confine all solutions to the sheets.** The map $F$ is proper, the target $Y$ is metrisable (a second-countable Banach manifold is metrisable), the domain $X$ is Hausdorff, and $F^{-1}(y) = \{x_1, \dots, x_k\}$ is finite with $x_j \in V_j^{(0)}$. By Lemma 3, there is an open set $U \ni y$ with
> $$F^{-1}(U) \subseteq \bigcup_{j=1}^{k} V_j^{(0)}. \tag{2}$$
> We may shrink $U$ to lie inside $U^{(0)}$ by replacing it with $U \cap U^{(0)}$ (still open, still containing $y$, and (2) is preserved because the left side only shrinks). Now set
> $$V_j := V_j^{(0)} \cap F^{-1}(U) = \big(F|_{V_j^{(0)}}\big)^{-1}(U) \qquad (j = 1, \dots, k).$$
> Since $U \subseteq U^{(0)}$ and $F|_{V_j^{(0)}} : V_j^{(0)} \to U^{(0)}$ is a diffeomorphism (by (1)), its restriction to the preimage of the open subset $U$ is a diffeomorphism $F|_{V_j} : V_j \to U$. The sets $V_j$ are open, pairwise disjoint (as subsets of the pairwise disjoint $V_j^{(0)}$), and contain $x_j$ (because $x_j \in V_j^{(0)}$ and $F(x_j) = y \in U$). Finally,
> $$F^{-1}(U) \;\overset{(2)}{\subseteq}\; \Big(\bigcup_{j} V_j^{(0)}\Big) \cap F^{-1}(U) \;=\; \bigcup_{j}\big(V_j^{(0)} \cap F^{-1}(U)\big) \;=\; \bigsqcup_{j=1}^{k} V_j, \tag{3}$$
> where the first step uses that $F^{-1}(U) \subseteq F^{-1}(U)$ and (2), the middle equality distributes intersection over union, and the union is disjoint because the $V_j$ are. Thus $U$ and $V_1, \dots, V_k$ satisfy both conclusions displayed in the Statement.
>
> **Step 3 — the count over $U$ is $k$, and every $y' \in U$ is regular.** Fix $y' \in U$. By (3), every preimage $x' \in F^{-1}(y')$ lies in exactly one $V_j$ (the union in (3) is disjoint). Within $V_j$ the map $F|_{V_j} : V_j \to U$ is a bijection (being a diffeomorphism), so it has exactly one point over $y'$. Therefore
> $$F^{-1}(y') = \bigsqcup_{j=1}^{k} \big(F|_{V_j}\big)^{-1}(y'), \qquad \#F^{-1}(y') = \sum_{j=1}^{k} 1 = k \qquad \text{(each summand a single point, by (3) and (1)).}$$
> Moreover $y'$ is a regular value: for any $x' \in F^{-1}(y')$ we have $x' \in V_j$ for some $j$, and since $F|_{V_j}$ is a diffeomorphism, its differential $d_{x'}(F|_{V_j}) = d_{x'} F$ is a Banach-space isomorphism, in particular surjective; as $x'$ was an arbitrary point of $F^{-1}(y')$, the value $y'$ is regular. Hence $U \subseteq Y_{\mathrm{reg}}$ and $N \equiv k$ on $U$.
>
> **Step 4 — the empty case $k = 0$.** Suppose $F^{-1}(y) = \varnothing$. Then $y \notin F(X)$, for if $y = F(x)$ then $x \in F^{-1}(y)$, contrary to emptiness. The map $F$ is proper and $Y$ is metrisable, so by [[Thm - Proper Maps are Closed and Fredholm Maps are Locally Proper|the fact that a proper map into a metrisable space is closed]] (part (i), restated: *a proper continuous map into a metrisable space sends closed sets to closed sets*), applied to the closed set $X \subseteq X$, the image $F(X)$ is closed in $Y$. Therefore $U := Y \setminus F(X)$ is open, contains $y$, and has empty preimage:
> $$F^{-1}(U) = F^{-1}\big(Y \setminus F(X)\big) = \varnothing.$$
> Consequently every $y' \in U$ is (vacuously) a regular value with $\#F^{-1}(y') = 0 = k$, and $N \equiv 0$ on $U$.
>
> **Step 5 — local constancy on $Y_{\mathrm{reg}}$.** Steps 3 and 4 together show: for every regular value $y \in Y_{\mathrm{reg}}$ there is an open neighbourhood $U \subseteq Y$ with $U \subseteq Y_{\mathrm{reg}}$ (every point of $U$ is regular) and $N \equiv N(y)$ on $U$. The first property shows $Y_{\mathrm{reg}}$ is open, since each of its points is interior to it. The second is exactly the statement that $N : Y_{\mathrm{reg}} \to \mathbb{Z}_{\ge 0}$ is locally constant. Therefore the number of preimages of a regular value is locally constant on the open set of regular values. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Winding number of a proper planar map.** Let $f : \mathbb{C} \to \mathbb{C}$ be a proper smooth map of the plane to itself — for instance a monic polynomial, which satisfies $|f(z)| \to \infty$ and is therefore proper. Its differential is the real $2 \times 2$ Jacobian, trivially a Fredholm operator of index $\dim - \dim = 0$, and a value $w$ is regular exactly when the Jacobian determinant is nonzero at each solution of $f(z) = w$. The theorem says the number of preimages of $w$ is locally constant on the regular values; combined with a signed count this recovers the algebraic count of roots and, ultimately, that a degree-$n$ polynomial has $n$ roots. The application is non-obvious because "number of solutions is stable" is doing the work usually attributed to the fundamental theorem of algebra, and properness — not compactness of the domain — is the hypothesis that makes it run.

**Solutions of a semilinear elliptic equation as the datum varies.** Consider $F : W^{k,2}(M) \to W^{k-2,2}(M)$, $F(u) = \Delta u + g(u)$, on a closed Riemannian manifold $M$, with $g$ a nonlinearity for which an a priori bound makes $F$ proper. The differential $d_u F = \Delta + g'(u)$ is a compact perturbation of the elliptic Laplacian, hence Fredholm; tuning exponents gives index zero. For a generic right-hand side $h$ (a regular value), the theorem asserts that the number of solutions of $\Delta u + g(u) = h$ is locally constant in $h$. The point worth appreciating is that this stability is not a perturbation-of-solutions statement about one solution but a *global* count, and properness — encoding an a priori estimate — is what prevents solutions from disappearing to infinity as $h$ moves.

**Sheet number of a proper covering-like map in Morse theory.** Given a proper smooth map $F$ between equal-dimensional manifolds arising as the gradient-endpoint map of a family of Morse functions, the regular values are the parameters at which no critical value collision occurs, and the locally constant count is the number of trajectories. The theorem explains why the trajectory count changes only across critical (non-regular) parameters — the walls of chamber structure in bifurcation diagrams. The subtlety is that one must certify properness (no trajectory escaping the manifold), which in the noncompact case is a genuine analytic hypothesis rather than a formality.

---

# Bridges

- **[[Thm - Well-Definedness and Homotopy Invariance of the Degree]]** — the theorem this page feeds. That result proves $\deg_2 F = \#F^{-1}(y) \bmod 2$ is independent of the regular value and is a proper-homotopy invariant, in six steps. The present theorem is its Step 2, providing the local constancy of the count; the remaining steps build a diffeomorphism of $Y$ moving any regular value to any other (to compare parities across the components of $Y_{\mathrm{reg}}$) and a cobordism-of-fibres argument for homotopies. The construction here — the finite family of sheets $V_j$ over a ball $U$ — is exactly what those steps manipulate.

- **[[Thm - Regular Values of a Proper Fredholm Map are Open and Dense]]** — a companion. Step 5 above shows *openness* of $Y_{\mathrm{reg}}$ as a by-product; that page proves the full statement, adding *density* via the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]]. Openness is the topological half (critical values are closed because $\operatorname{Crit}(F)$ is closed and proper maps are closed), density is the measure-theoretic half; together they guarantee a regular value exists to compute the degree at.

- **[[Def - Integer Degree of an Oriented Proper Fredholm Map]]** — the signed refinement. Once the family of differentials is oriented, via a trivialisation of the [[Def - Determinant Line Bundle of a Family of Fredholm Operators|determinant line bundle]], each sheet $F|_{V_j}$ acquires a sign $\varepsilon_j = \pm 1$ recording whether it preserves or reverses orientation. The construction of the neighbourhoods $V_j$ is identical; only the bookkeeping changes, replacing $\#F^{-1}(y') = \sum_j 1$ by the signed sum $\sum_j \varepsilon_j$, which the same local argument shows is locally constant.

- **[[Thm - Regular Value Theorem on Manifolds]]** — the finite-dimensional prototype. In finite dimensions the identical statement holds and is easier: a proper map between equal-dimensional manifolds is, near a regular value, a finite covering. Reading this page against that one isolates exactly the extra work the Banach setting demands, which is Lemma 3, since in the finite-dimensional compact case the confinement of solutions is automatic.

---

# Unlocked by This

> [!tip] The degree of a proper map *(from Differential Topology)*
> The locally constant count over regular values, refined by signs, is the degree of a proper smooth map between oriented manifolds of equal dimension — the invariant that counts preimages with sign and is unchanged under proper homotopy. This theorem is the infinite-dimensional generalisation of the local step in its construction. See **[[Def - Brouwer Degree of a Map]]** for the compact finite-dimensional case.

> [!tip] Counting solutions of nonlinear equations *(from Nonlinear Analysis)*
> The stability of the solution count under perturbation of the data is the engine of degree-theoretic existence proofs: a nonzero degree at one datum forces solutions at every nearby regular datum, and by homotopy at data that are far away. This is how one proves existence for nonlinear elliptic problems without a variational structure. See **[[Thm - Nonzero Degree Implies Surjectivity]]**.
