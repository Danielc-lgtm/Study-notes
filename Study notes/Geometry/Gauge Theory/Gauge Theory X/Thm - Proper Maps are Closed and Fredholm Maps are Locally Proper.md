---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Banach Manifold and Smooth Maps between Banach Spaces"
  - "Thm - Kuranishi Model for a Fredholm Map"
  - "Thm - Compactness in Metric Spaces (Three Equivalents)"
  - "Def - Fredholm Map and Its Index"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $X$ and $Y$ are topological spaces and $F : X \to Y$ is a continuous map; from Part (ii) onward they are Banach manifolds and $F$ is smooth. We use the following standard vocabulary, each item typed here so the page is self-contained.

A subset $K$ of a topological space is **compact** if every open cover of $K$ has a finite subcover. A space is **Hausdorff** if any two distinct points have disjoint open neighbourhoods. A space is **locally compact** if every point has a compact neighbourhood, that is, a compact set $K$ with the point in its interior $\operatorname{int} K$. A space is **metrisable** if its topology is induced by some metric $d$; a metrisable space is automatically Hausdorff. For a subset $S$, $\overline{S}$ denotes its closure and $\operatorname{int} S$ its interior.

A continuous map $F : X \to Y$ is **proper** if the preimage $F^{-1}(K)$ of every compact set $K \subseteq Y$ is compact. It is **closed** if the image $F(C)$ of every closed set $C \subseteq X$ is closed in $Y$. These are the two properties the theorem relates.

For the second part we use the language of the [[Def - Banach Manifold and Smooth Maps between Banach Spaces|Banach-manifold framework]]. A **Banach manifold** is a Hausdorff, second countable space with an atlas of charts into open subsets of a fixed separable Banach space with smooth transition maps; a **chart** near $p$ is a homeomorphism $\kappa$ from an open neighbourhood of $p$ onto an open subset of the model Banach space. A smooth map $F$ between Banach manifolds is a [[Def - Fredholm Map and Its Index|Fredholm map]] if its differential $d_pF : T_pX \to T_{F(p)}Y$ is a [[Def - Fredholm Operator and Index|Fredholm operator]] at every point $p$ — a bounded linear map with finite-dimensional kernel $\ker d_pF$ and finite-dimensional cokernel $\operatorname{coker} d_pF = T_{F(p)}Y / \operatorname{im} d_pF$ and closed range $\operatorname{im} d_pF$. Its **index** is $\operatorname{index} d_pF = \dim \ker d_pF - \dim \operatorname{coker} d_pF$.

In Part (ii) the [[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model]] supplies, near a chosen point, a splitting $\mathbb{X} = X_0 \oplus X_1$ of the model Banach space of $X$ with $X_0 = \ker d_pF$ finite-dimensional, a splitting $\mathbb{Y} = Y_0 \oplus Y_1$ of the model Banach space of $Y$ with $Y_0 = \operatorname{im} d_pF$ closed and $Y_1$ finite-dimensional, a bounded linear isomorphism $T : X_1 \to Y_0$, a local diffeomorphism $\phi$, and a smooth remainder $f$ valued in $Y_1$. We write $\pi_{Y_0} : \mathbb{Y} \to Y_0$ and $\pi_{Y_1} : \mathbb{Y} \to Y_1$ for the projections of the direct sum $\mathbb{Y} = Y_0 \oplus Y_1$, and $\pi_{X_0}, \pi_{X_1}$ for those of $\mathbb{X} = X_0 \oplus X_1$; on $\mathbb{X}$ and $\mathbb{Y}$ we use the sum norm $\lVert x_0 + x_1 \rVert = \lVert x_0 \rVert + \lVert x_1 \rVert$, which is equivalent to the given norm because both summands are closed and the splitting is topological. We write $\overline{B}_r = \{x \in \mathbb{X} : \lVert x \rVert \le r\}$ for the closed ball of radius $r$.

> [!warning] Convention: paracompact versus second countable
> Haydys states the Sard–Smale theorem and the degree for maps between **paracompact** Banach manifolds. Following the series convention (design note in the chapter manifest), all our Banach manifolds are **second countable and metrisable**; a metrisable space is paracompact, so our setting is a special case of Haydys's, and the metrisable hypothesis is exactly what lets Part (i) run through convergent sequences. Every place a compactness fact is used, we say which hypothesis on $Y$ — local compactness or metrisability — supplies it.

---

# Statement

> **Theorem (proper maps are closed; Fredholm maps are locally proper).**
>
> **(i)** Let $F : X \to Y$ be a continuous map between topological spaces, with $X$ Hausdorff and $Y$ locally compact and Hausdorff, and suppose $F$ is **proper**, meaning $F^{-1}(K)$ is compact for every compact $K \subseteq Y$. Then $F$ is **closed**: $F(C)$ is closed in $Y$ for every closed $C \subseteq X$. The same conclusion holds when the hypothesis "$Y$ locally compact and Hausdorff" is replaced by "$Y$ metrisable".
>
> **(ii)** Let $F : X \to Y$ be a smooth Fredholm map between Banach manifolds. Then $F$ is **locally proper**: every point $p \in X$ has an open neighbourhood $U_p$ such that the restriction $F|_{\overline{U_p}} : \overline{U_p} \to Y$ is a proper map, where $\overline{U_p}$ is the closure of a small coordinate ball around $p$.

---

# Motivation

The degree theory built in this chapter counts, modulo $2$ or with signs, the points in the preimage $F^{-1}(y)$ of a regular value $y$ of a Fredholm map $F : X \to Y$ of index zero. For this count to be a finite number at all, $F^{-1}(y)$ — which the regular-value theorem makes a zero-dimensional manifold — must be a *finite* set rather than a discrete infinite one; and for the count to be an *invariant*, independent of the regular value chosen, it must be locally constant as $y$ varies. Both of these are consequences of one hypothesis: that $F$ is **proper**. Properness makes $F^{-1}(y)$ compact, hence finite, and — through the present theorem — makes the set of critical values $F(\operatorname{Crit} F)$ closed, so that its complement, the regular values, is open and the count cannot jump across it. Without properness the degree collapses: the map $\arctan : \mathbb{R} \to (-\tfrac{\pi}{2}, \tfrac{\pi}{2})$ is a smooth Fredholm map of index zero, yet every value in $(-\tfrac{\pi}{2}, \tfrac{\pi}{2})$ has one preimage while every nearby value outside the image has none, so no locally constant count exists. Properness is the exact hypothesis that excludes this.

Part (i) is the mechanism by which properness does its work. It says that a proper map exports the topology of the target back to the source: because compact sets pull back to compact sets, and compact sets are closed in a Hausdorff target, a proper map carries closed sets to closed sets. This is the single fact that the well-definedness proof of the degree invokes when it says "the critical values are closed".

Part (ii) is the reassurance that the properness hypothesis is not vacuous or hard to arrange. A Fredholm map need not be proper globally — $\arctan$ shows that — but it is *always* proper on small neighbourhoods, and this local properness is exactly what the Sard–Smale argument needs to convert a measure-theoretic statement ("the critical values meet every finite-dimensional slice in a null set") into a topological one ("the critical values are nowhere dense"). The reason local properness is automatic is structural: near any point a Fredholm map looks, after the [[Thm - Kuranishi Model for a Fredholm Map|Kuranishi change of coordinates]], like a linear isomorphism $T$ in the infinite-dimensional directions plus a smooth map into a finite-dimensional cokernel. The isomorphism pins the infinite-dimensional coordinate of a fibre to a *compact* set — the continuous image of the compact target set — and the finite-dimensional kernel coordinate is pinned by the Heine–Borel theorem. Logically this page precedes the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]], which lists it as a prerequisite: Part (i) is used to close the critical values, and Part (ii) is used to make the critical values closed *locally* before the covering argument assembles them.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of Part (i) is "proper", so the source question is: when does a problem hand you a proper map without saying so?

The first disguised source is **a map out of a space that is compact, or one whose sublevel sets are compact — a coercivity or growth condition**. If $X$ is compact then every continuous $F : X \to Y$ is proper, because $F^{-1}(K)$ is a closed subset of the compact $X$ and hence compact; more usefully, a map $F : \mathbb{R}^n \to \mathbb{R}^m$ with $\lVert F(x) \rVert \to \infty$ as $\lVert x \rVert \to \infty$ (a coercive or proper-in-the-analyst's-sense map) is proper, because the preimage of a bounded set is bounded and closed. The non-obvious bridge is that a purely quantitative growth estimate — "the map blows up at infinity" — is precisely the topological statement "preimages of compact sets are compact". *Example problem:* show that a polynomial map $p : \mathbb{C} \to \mathbb{C}$ of degree $k \ge 1$ is proper, hence closed, hence surjective, recovering the fundamental theorem of algebra from properness plus connectedness of the image.

The second disguised source is **a closed embedding, or a map that is a homeomorphism onto a closed subset**. A closed topological embedding is proper when the ambient target is locally compact, because a compact set of the target meets the closed image in a compact set whose preimage is its homeomorphic copy. The non-obvious step is recognising that "closed image" upgrades an embedding to a proper map, so that Part (i) then returns the closedness one started with as a *consequence available for all closed subsets of the domain*, not just the whole domain. *Example problem:* deduce that the graph of a continuous $g : \mathbb{R}^n \to \mathbb{R}^m$, viewed as a map $\mathbb{R}^n \to \mathbb{R}^{n+m}$, is a proper closed embedding.

The third disguised source is **a smooth Fredholm map restricted to a small neighbourhood** — this is exactly Part (ii). Any semilinear elliptic operator plus a lower-order nonlinearity, read between the appropriate Sobolev completions, is a Fredholm map (its linearisation is elliptic, hence Fredholm), and therefore locally proper for free, with no growth estimate to check. The non-obvious content is that the *analytic* Fredholm property, established once via elliptic theory, delivers the *topological* local properness needed for degree theory without any further work. *Example problem:* given that $u \mapsto \Delta u + u^3$ on a closed surface is a Fredholm map between Sobolev spaces, conclude that it is locally proper and identify the neighbourhood on which the coordinate model holds.

**Targets (Output Amplification)**

Combine Part (i) with **the openness of the surjectivity of a Fredholm operator**. The critical set $\operatorname{Crit} F = \{x : d_xF \text{ not surjective}\}$ is closed, because surjectivity of a Fredholm operator is an open condition on $x$. If moreover $F$ is proper, then Part (i) makes $F(\operatorname{Crit} F)$ closed, so the regular values form an *open* set. The payoff is that "the regular values are open and dense" — the first step of the degree's well-definedness — is nothing but Part (i) plus openness of surjectivity plus the [[Thm - Sard-Smale Theorem|Sard–Smale theorem]] for density.

Combine Part (i) with **the local model near a regular value**. If $y$ is a regular value of a proper index-zero Fredholm map with $F^{-1}(y) = \{x_1, \dots, x_k\}$, the inverse function theorem makes $F$ a diffeomorphism near each $x_j$, and properness — through the closedness of Part (i) — is exactly what excludes preimages of nearby values escaping to infinity. The payoff is that the count $y \mapsto \# F^{-1}(y)$ is locally constant, so it descends to a well-defined degree.

Combine Part (i) with **connectedness of the target and a nonzero degree**. A proper index-zero Fredholm map of nonzero mod-$2$ degree is surjective: every value is a limit of regular values, each with nonempty preimage, and closedness of $F$ (Part (i)) forces the limit into the image. The payoff is a fixed-point-style existence theorem — a nonvanishing degree guarantees solutions of $F(x) = y$ for every $y$ — which is the shape of every application of degree theory to nonlinear equations.

---

# Why Is It True

Picture Part (i) first. To say a set $F(C)$ is closed is to say it contains all its limit points, and a limit point $y$ of $F(C)$ is approached by images $F(c)$ of points $c \in C$. The difficulty is that the approaching points $c$ could wander off to infinity in $X$, so that no single point of $C$ actually maps to $y$. Properness forbids exactly this wandering: the approaching values $F(c)$ eventually sit inside a fixed compact neighbourhood $K$ of $y$ (or, in the metrisable case, inside the compact set consisting of a convergent sequence and its limit), so the approaching points $c$ are trapped inside the compact set $F^{-1}(K)$. A trapped sequence cannot escape; its images form a *closed* set that already contains $y$. The whole content is that properness turns "$y$ is approached from $F(C)$" into "$y$ is hit by $C$".

> **Mechanism of Part (i): a proper map exports the compactness of the target into the source, so the closure of an image is captured inside the image of a compact — hence closed — piece of the domain.**

Now Part (ii). In infinite dimensions a Fredholm map cannot be pinned down by boundedness, because bounded sets are not precompact. What saves us is the [[Thm - Kuranishi Model for a Fredholm Map|Kuranishi decomposition]]: after a smooth change of coordinates the map reads $(x_0, x_1) \mapsto Tx_1 + f(x_0, x_1)$, where $T : X_1 \to Y_0$ is a linear isomorphism of the infinite-dimensional directions and $f$ takes values in the finite-dimensional cokernel $Y_1$. If a fibre point maps into a compact target set $K$, then its $Y_0$-component is $Tx_1$, and $x_1 = T^{-1}(\text{that component})$ is the image of a compact set under the continuous map $T^{-1}$ — hence lies in a *compact* set, even though $X_1$ is infinite-dimensional. The remaining coordinate $x_0$ lives in the finite-dimensional kernel and is bounded by the radius of the ball, so it is trapped by the Heine–Borel theorem. Both coordinates trapped in compact sets means the whole fibre is trapped, which is properness.

> **Mechanism of Part (ii): the Kuranishi split makes a Fredholm map an isomorphism plus a finite-dimensional remainder; the isomorphism converts the compactness of a target set into compactness of the infinite-dimensional fibre coordinate, and Heine–Borel handles the finite-dimensional one.**

---

# What Makes This Hard

The non-obvious step in Part (i) is realising that closedness is not automatic and that the only obstruction is escape to infinity, which properness precisely rules out; a common error is to try to prove closedness directly, forgetting that without properness a proper-looking map like $\arctan$ genuinely fails to be closed. The non-obvious step in Part (ii) is that boundedness is useless in infinite dimensions — the closed unit ball of an infinite-dimensional Banach space is *not* compact — so one must extract compactness from the isomorphism $T$ by writing the trapped coordinate as $T^{-1}$ applied to a *compact* image, never as "a bounded subset of $X_1$". A subtler pitfall, which Haydys's terse account passes over, is that on a genuine Banach *manifold* the target chart covers only a neighbourhood of $F(p)$, so a compact test set $K$ can straddle the chart boundary; the neighbourhood $U_p$ must be shrunk so that the closure of $F(\overline{U_p})$ stays inside one chart, or the coordinate argument would compare $K$ against coordinates that are not defined.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For Part (i), fix a closed set $C$ and a point $y$ in the closure of $F(C)$, manufacture a compact set $K \subseteq Y$ that captures how $F(C)$ approaches $y$, and show that the image of the compact piece $C \cap F^{-1}(K)$ is closed and already contains $y$. For Part (ii), pass to a Kuranishi chart, choose the neighbourhood so that images stay inside one target chart, and use the isomorphism $T$ and the Heine–Borel theorem to trap the preimage of a compact set inside a compact box.

**Subgoal decomposition:**

1. **Assemble a compactness toolkit.** Establish that closed subsets of compact sets are compact, that continuous images of compact sets are compact, and that compact subsets of a Hausdorff space are closed.
   - *Hint:* Each is a one-paragraph open-cover or point-separation argument.
   - *Why needed:* Every line of both parts is an application of one of these three facts.

2. **Part (i), common core.** With $C$ closed and $y \in \overline{F(C)}$, given a compact $K \subseteq Y$, show $A := C \cap F^{-1}(K)$ is compact and $F(A)$ is closed.
   - *Hint:* $F^{-1}(K)$ is compact by properness; $A$ is closed in it; apply the toolkit.
   - *Why needed:* This is the engine; the two cases only differ in how $K$ is produced.

3. **Part (i), locally compact case.** Produce $K$ as a compact neighbourhood of $y$ and show $y \in \overline{F(A)} = F(A)$.
   - *Hint:* Local compactness gives $K$ with $y \in \operatorname{int} K$; intersect neighbourhoods of $y$ with $\operatorname{int} K$.
   - *Why needed:* Handles targets like manifolds and locally compact groups that are not assumed metrisable.

4. **Part (i), metrisable case.** Produce $K$ as a convergent sequence with its limit and conclude.
   - *Hint:* In a metric space $y \in \overline{F(C)}$ gives $y_n = F(c_n) \to y$; take $K = \{y_n\} \cup \{y\}$.
   - *Why needed:* This is the case actually used by the degree, where $Y$ is a metrisable Banach manifold.

5. **Part (ii), model properness.** In the Kuranishi coordinates, show the preimage of a compact set inside a closed ball is compact.
   - *Hint:* The $Y_0$-projection of the map is $Tx_1$, so $x_1 \in T^{-1}\pi_{Y_0}(K)$, compact; $x_0$ is bounded in a finite-dimensional space.
   - *Why needed:* This is the whole analytic content of local properness.

6. **Part (ii), chart transfer.** Choose $U_p$ so that $\overline{F(\overline{U_p})}$ lies in one target chart, and transport the model statement back to $F$.
   - *Hint:* Only $K \cap \overline{F(\overline{U_p})}$ is relevant; it is compact and lives inside the chart, so it becomes a compact set in the model.
   - *Why needed:* Bridges the Banach-space model to a genuine Banach manifold without a chart-boundary gap.

---

# Lemma Decomposition

> [!note]- Lemma 1: Elementary facts about compact sets
> **Statement:** Let $Z$ and $Z'$ be topological spaces. (a) A closed subset of a compact subset of $Z$ is compact. (b) If $g : Z \to Z'$ is continuous and $A \subseteq Z$ is compact, then $g(A)$ is compact. (c) If $Z$ is Hausdorff, then every compact subset of $Z$ is closed.
>
> **Hint:** For (a) add the complement of the closed set to any cover; for (b) pull back a cover through $g$; for (c) separate a fixed exterior point from each point of the compact set and take a finite subcover.
>
> **Why needed:** Part (i) uses all three (properness gives a compact preimage, (a) trims it by the closed set $C$, (b) makes its image compact, (c) makes that image closed); Part (ii) uses (a) and (b) to trap the fibre.
>
> > [!note]- Full proof
> > **(a).** Let $K \subseteq Z$ be compact and $D \subseteq K$ closed in $Z$ (equivalently $D$ closed in $K$). Let $\{U_\alpha\}_{\alpha}$ be an open cover of $D$ by sets open in $Z$. Then $\{U_\alpha\} \cup \{Z \setminus D\}$ is an open cover of $K$ (every point of $K$ is either in $D$, hence in some $U_\alpha$, or outside $D$, hence in $Z \setminus D$; and $Z \setminus D$ is open because $D$ is closed). By compactness of $K$ there is a finite subcover $U_{\alpha_1}, \dots, U_{\alpha_n}, Z \setminus D$ of $K$, hence of $D$. Since $Z \setminus D$ contains no point of $D$, the sets $U_{\alpha_1}, \dots, U_{\alpha_n}$ alone cover $D$. Therefore $D$ is compact.
> >
> > **(b).** Let $\{V_\beta\}_\beta$ be an open cover of $g(A)$ by sets open in $Z'$. Then $\{g^{-1}(V_\beta)\}_\beta$ is a cover of $A$ by sets open in $Z$ (open because $g$ is continuous; a cover because for $a \in A$ we have $g(a) \in g(A)$, so $g(a) \in V_\beta$ for some $\beta$, whence $a \in g^{-1}(V_\beta)$). By compactness of $A$ there are $\beta_1, \dots, \beta_n$ with $A \subseteq \bigcup_{i} g^{-1}(V_{\beta_i})$. Applying $g$ gives $g(A) \subseteq \bigcup_i V_{\beta_i}$ (if $a \in g^{-1}(V_{\beta_i})$ then $g(a) \in V_{\beta_i}$). Therefore $g(A)$ is compact.
> >
> > **(c).** Let $K \subseteq Z$ be compact with $Z$ Hausdorff; we show $Z \setminus K$ is open. Fix $z \in Z \setminus K$. For each $k \in K$, the Hausdorff property gives disjoint open sets $O_k \ni k$ and $W_k \ni z$. The family $\{O_k\}_{k \in K}$ is an open cover of $K$, so by compactness finitely many $O_{k_1}, \dots, O_{k_n}$ cover $K$. Set $W := \bigcap_{i=1}^n W_{k_i}$, a finite intersection of open sets, hence open, and $z \in W$. For each $i$, $W \subseteq W_{k_i}$ is disjoint from $O_{k_i}$, so $W$ is disjoint from $\bigcup_i O_{k_i} \supseteq K$; thus $W \subseteq Z \setminus K$. Hence every point of $Z \setminus K$ has an open neighbourhood inside $Z \setminus K$, so $Z \setminus K$ is open and $K$ is closed.

> [!note]- Lemma 2: A convergent sequence together with its limit is compact
> **Statement:** In any topological space $Y$, if $y_n \to y$ (every open set containing $y$ contains all but finitely many $y_n$), then $K := \{y_n : n \ge 1\} \cup \{y\}$ is compact.
>
> **Hint:** In any open cover, one set contains $y$ and therefore all but finitely many terms; cover the finitely many exceptions individually.
>
> **Why needed:** It supplies the compact test set $K$ in the metrisable case of Part (i), where $y$ is a sequential limit of points of $F(C)$.
>
> > [!note]- Full proof
> > Let $\{U_\alpha\}_\alpha$ be an open cover of $K$. Since $y \in K$, some member $U_{\alpha_0}$ contains $y$. By the definition of convergence $y_n \to y$, the open set $U_{\alpha_0}$ contains all but finitely many terms of the sequence; let $y_{n_1}, \dots, y_{n_m}$ be the finitely many terms not in $U_{\alpha_0}$. Each $y_{n_j}$ lies in $K$, hence in some $U_{\alpha_j}$. Then
> > $$K \subseteq U_{\alpha_0} \cup U_{\alpha_1} \cup \cdots \cup U_{\alpha_m},$$
> > because any element of $K$ is either $y$ or a term $y_n$: if $y_n \in U_{\alpha_0}$ it is covered, and otherwise $y_n = y_{n_j}$ for some $j$ and lies in $U_{\alpha_j}$ (since $\{y_{n_1}, \dots, y_{n_m}\}$ are all the terms outside $U_{\alpha_0}$). This is a finite subcover, so $K$ is compact.

> [!note]- Lemma 3: Properness of the Kuranishi model
> **Statement:** Let $\mathbb{X} = X_0 \oplus X_1$ and $\mathbb{Y} = Y_0 \oplus Y_1$ be topological direct sums of Banach spaces with $\dim X_0 < \infty$ and $\dim Y_1 < \infty$, so that the projections $\pi_{X_0}, \pi_{X_1}, \pi_{Y_0}, \pi_{Y_1}$ are bounded. Let $T : X_1 \to Y_0$ be a bounded linear isomorphism (so $T^{-1}$ is bounded), let $\Omega \subseteq \mathbb{X}$ be open with $0 \in \Omega$, and let $G : \Omega \to \mathbb{Y}$ be a continuous map of the form
> $$G(x_0, x_1) = Tx_1 + f(x_0, x_1), \qquad f : \Omega \to Y_1 \text{ continuous.}$$
> Fix $r > 0$ with $\overline{B}_r \subseteq \Omega$. Then for every compact $L \subseteq \mathbb{Y}$, the set $A := \{x \in \overline{B}_r : G(x) \in L\}$ is compact.
>
> **Hint:** Applying $\pi_{Y_0}$ to $G$ kills $f$ and leaves $Tx_1$, so $x_1$ is $T^{-1}$ of a point of the compact $\pi_{Y_0}(L)$; the finite-dimensional $x_0$ is bounded by $r$; then extract a convergent subsequence coordinate by coordinate.
>
> **Why needed:** This is the entire analytic content of local properness (Part (ii)): the Fredholm map, read in Kuranishi coordinates, has proper restrictions to closed balls.
>
> > [!note]- Full proof
> > We show $A$ is sequentially compact; since $\mathbb{X}$ is a Banach space and hence metrisable, sequential compactness is equivalent to compactness (by the [[Thm - Compactness in Metric Spaces (Three Equivalents)|equivalence of compactness and sequential compactness in metric spaces]]: in a metric space, a subset is compact if and only if every sequence in it has a subsequence converging to a point of the subset). Let $(x^{(n)})_{n \ge 1}$ be a sequence in $A$, and write $x^{(n)} = (x_0^{(n)}, x_1^{(n)})$ with $x_0^{(n)} \in X_0$, $x_1^{(n)} \in X_1$.
> >
> > **Step 1 — the $X_1$-coordinate lies in a compact set.** For each $n$, since $x^{(n)} \in A$ we have $G(x^{(n)}) \in L$. Apply the bounded projection $\pi_{Y_0}$:
> > $$\pi_{Y_0}\big(G(x^{(n)})\big) = \pi_{Y_0}\big(T x_1^{(n)} + f(x^{(n)})\big) = T x_1^{(n)} \qquad (\text{since } T x_1^{(n)} \in Y_0 \text{ and } f(x^{(n)}) \in Y_1 = \ker \pi_{Y_0}).$$
> > Hence $T x_1^{(n)} \in \pi_{Y_0}(L)$, and applying $T^{-1}$,
> > $$x_1^{(n)} = T^{-1}\big(\pi_{Y_0}(G(x^{(n)}))\big) \in T^{-1}\big(\pi_{Y_0}(L)\big) =: Q_1.$$
> > The set $Q_1$ is compact: $\pi_{Y_0}(L)$ is the continuous image of the compact $L$ under the bounded map $\pi_{Y_0}$, hence compact by Lemma 1(b), and $T^{-1}(\pi_{Y_0}(L))$ is the continuous image of that compact set under the bounded map $T^{-1}$, hence compact by Lemma 1(b) again. Thus $x_1^{(n)} \in Q_1$ for all $n$, and $Q_1$ is a compact subset of the metric space $X_1$; by sequential compactness there is a subsequence $(x_1^{(n_j)})_j$ converging to some $x_1^\ast \in Q_1$.
> >
> > **Step 2 — the $X_0$-coordinate lies in a compact set.** For each $n$, $x^{(n)} \in \overline{B}_r$ means $\lVert x_0^{(n)} \rVert + \lVert x_1^{(n)} \rVert = \lVert x^{(n)} \rVert \le r$ (sum norm), so in particular $\lVert x_0^{(n)} \rVert \le r$. Thus $x_0^{(n)} \in Q_0 := \{v \in X_0 : \lVert v \rVert \le r\}$, a closed and bounded subset of the finite-dimensional space $X_0$. By the [[Thm - Heine–Borel Theorem|Heine–Borel theorem]] — in a finite-dimensional normed space a subset is compact if and only if it is closed and bounded — $Q_0$ is compact. Passing to a further subsequence of the indices $n_j$ already chosen, which we relabel $n_j$ again, we obtain $x_0^{(n_j)} \to x_0^\ast$ for some $x_0^\ast \in Q_0$, while retaining $x_1^{(n_j)} \to x_1^\ast$.
> >
> > **Step 3 — the limit lies in $A$.** Set $x^\ast := (x_0^\ast, x_1^\ast)$. Then $x^{(n_j)} = (x_0^{(n_j)}, x_1^{(n_j)}) \to (x_0^\ast, x_1^\ast) = x^\ast$ in $\mathbb{X}$ (convergence in each summand of a topological direct sum gives convergence of the sum). Since $\overline{B}_r$ is closed and contains every $x^{(n_j)}$, the limit satisfies $x^\ast \in \overline{B}_r \subseteq \Omega$. Because $G$ is continuous on $\Omega$, $G(x^{(n_j)}) \to G(x^\ast)$; each $G(x^{(n_j)}) \in L$ and $L$ is closed (compact in the metric, hence Hausdorff, space $\mathbb{Y}$, by Lemma 1(c)), so $G(x^\ast) \in L$. Therefore $x^\ast \in \{x \in \overline{B}_r : G(x) \in L\} = A$.
> >
> > We have produced, from an arbitrary sequence in $A$, a subsequence converging to a point of $A$. Hence $A$ is sequentially compact, and therefore compact.

---

# Formal Proof

> [!note]- Complete formal proof
>
> ## Part (i): a proper map into a locally compact Hausdorff, or metrisable, target is closed
>
> **Step 0 — reduction to a single point of the closure.** Let $C \subseteq X$ be closed. We must show $F(C)$ is closed, that is, $\overline{F(C)} \subseteq F(C)$. Fix $y \in \overline{F(C)}$; it suffices to prove $y \in F(C)$. We remark that the hypothesis "$X$ Hausdorff" is part of the standing setting but is not invoked below: the compactness of the set $A$ constructed next uses only that $C$ is closed and that a closed subset of a compact space is compact.
>
> **Step 1 — the common core.** Suppose we have produced a compact set $K \subseteq Y$ (the two cases below produce it differently). Set
> $$A := C \cap F^{-1}(K).$$
> Since $F$ is **proper**, $F^{-1}(K)$ is compact. Since $C$ is closed in $X$, the set $A = C \cap F^{-1}(K)$ is closed in $F^{-1}(K)$, hence compact by Lemma 1(a) (a closed subset of a compact set is compact). Its image $F(A)$ is compact by Lemma 1(b) (continuous image of a compact set), and therefore **closed** in $Y$ by Lemma 1(c), since $Y$ is Hausdorff (a locally compact Hausdorff space is Hausdorff by assumption; a metrisable space is Hausdorff automatically). Thus in both cases $F(A)$ is a closed set, and it remains only to show $y \in \overline{F(A)}$, for then $y \in \overline{F(A)} = F(A) \subseteq F(C)$, which finishes the proof.
>
> **Case 1 — $Y$ locally compact and Hausdorff.** Because $Y$ is locally compact, $y$ has a compact neighbourhood $K$, that is, a compact set $K$ with $y \in V := \operatorname{int} K$. We claim $y \in \overline{F(A)}$. Let $W$ be any open neighbourhood of $y$. Then $W \cap V$ is an open neighbourhood of $y$, and since $y \in \overline{F(C)}$, the set $W \cap V$ meets $F(C)$: there is $c \in C$ with
> $$F(c) \in W \cap V \subseteq W \cap K \qquad (\text{because } V = \operatorname{int} K \subseteq K).$$
> From $F(c) \in K$ we get $c \in F^{-1}(K)$, and with $c \in C$ this gives $c \in C \cap F^{-1}(K) = A$; from $F(c) \in W$ we get that $W$ meets $F(A)$. As $W$ was an arbitrary open neighbourhood of $y$, we conclude $y \in \overline{F(A)}$, and by Step 1, $y \in F(A) \subseteq F(C)$.
>
> **Case 2 — $Y$ metrisable.** Fix a metric $d$ inducing the topology of $Y$. Since $y \in \overline{F(C)}$, for each integer $n \ge 1$ the open ball $\{z \in Y : d(z, y) < 1/n\}$ meets $F(C)$; choose $c_n \in C$ with $y_n := F(c_n)$ satisfying $d(y_n, y) < 1/n$. Then $y_n \to y$. Put
> $$K := \{y_n : n \ge 1\} \cup \{y\},$$
> which is compact by Lemma 2 (a convergent sequence together with its limit is compact). Apply the common core of Step 1 with this $K$. Each $c_n$ lies in $A = C \cap F^{-1}(K)$, because $c_n \in C$ and $F(c_n) = y_n \in K$; hence $y_n = F(c_n) \in F(A)$ for all $n$. Since $y_n \to y$ and $F(A)$ is closed (Step 1), the limit $y$ lies in $F(A)$. Therefore $y \in F(A) \subseteq F(C)$.
>
> In either case $y \in F(C)$. As $y \in \overline{F(C)}$ was arbitrary, $\overline{F(C)} \subseteq F(C)$, so $F(C)$ is closed and $F$ is a closed map. This proves Part (i).
>
> ## Part (ii): a smooth Fredholm map is locally proper
>
> Let $F : X \to Y$ be a smooth Fredholm map between Banach manifolds and fix $p \in X$.
>
> **Step 0 — charts and the Kuranishi model.** Choose a chart $\kappa_X$ carrying an open neighbourhood of $p$ homeomorphically onto an open subset of the model Banach space $\mathbb{X}$, with $\kappa_X(p) = 0$, and a chart $\kappa_Y$ carrying an open neighbourhood $N$ of $F(p)$ homeomorphically onto an open subset $\widehat{N} \subseteq \mathbb{Y}$, with $\kappa_Y(F(p)) = 0$. Shrinking the domain of $\kappa_X$ if necessary, the coordinate representative $\widehat{F} := \kappa_Y \circ F \circ \kappa_X^{-1}$ is a smooth Fredholm map between open subsets of the Banach spaces $\mathbb{X}$ and $\mathbb{Y}$, defined near $0$. Apply the following, restated at the point of use.
>
> > **[[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model]] (restated).** For the smooth Fredholm map $\widehat{F}$ with $\widehat{F}(0) = 0$, set $X_0 := \ker d_0\widehat{F}$ (finite-dimensional) and $Y_0 := \operatorname{im}\, d_0\widehat{F}$ (closed), and choose topological complements $\mathbb{X} = X_0 \oplus X_1$ and $\mathbb{Y} = Y_0 \oplus Y_1$ with $Y_1$ finite-dimensional. Then there are a diffeomorphism $\phi$ from a neighbourhood $\Omega$ of $0$ in $\mathbb{X}$ onto a neighbourhood of $0$ with $\phi(0) = 0$, a bounded linear isomorphism $T := d_0\widehat{F}|_{X_1} : X_1 \to Y_0$, and a smooth map $f : \Omega \to Y_1$, such that $\widehat{F}(\phi(x_0, x_1)) = Tx_1 + f(x_0, x_1)$ for $(x_0, x_1) \in \Omega$.
>
> Write $G := \widehat{F} \circ \phi : \Omega \to \mathbb{Y}$; by the model $G(x_0, x_1) = Tx_1 + f(x_0, x_1)$ with $f$ valued in $Y_1$, exactly the form required by Lemma 3. Because $Y_1$ is finite-dimensional and $Y_0$ is closed, the direct sum $\mathbb{Y} = Y_0 \oplus Y_1$ is topological and the projection $\pi_{Y_0}$ is bounded; because $T$ is a bounded linear isomorphism of Banach spaces its inverse $T^{-1}$ is bounded; and $\dim X_0 < \infty$. These are precisely the standing hypotheses of Lemma 3.
>
> **Step 1 — choice of the neighbourhood so that images stay in one chart.** The manifold $Y$, being metrisable, is regular, so we may choose an open set $N'$ with $F(p) \in N'$ and $\overline{N'} \subseteq N$. Since $F$ is continuous and $F(p) \in N'$, the composite $F \circ \kappa_X^{-1} \circ \phi$ is continuous at $0$ and maps $0$ to $F(p) \in N'$; hence there is $r > 0$ with $\overline{B}_r \subseteq \Omega$ and
> $$F\big(\kappa_X^{-1}(\phi(\overline{B}_r))\big) \subseteq N'.$$
> Define $U_p := \kappa_X^{-1}(\phi(B_r))$ (open, since $\kappa_X^{-1}$ and $\phi$ are homeomorphisms and $B_r$ is open) and $\overline{U_p} := \kappa_X^{-1}(\phi(\overline{B}_r))$, its closure. Write $\psi := \kappa_X^{-1} \circ \phi : \overline{B}_r \to \overline{U_p}$, a homeomorphism. By construction $F(\overline{U_p}) \subseteq N'$, so
> $$\overline{F(\overline{U_p})} \subseteq \overline{N'} \subseteq N,$$
> using that $\overline{N'} \subseteq N$ is closed. This is the step that keeps every relevant image inside the single target chart $\kappa_Y$.
>
> **Step 2 — reduction of an arbitrary compact set to a compact set of the model.** Let $K \subseteq Y$ be compact; we must show $(F|_{\overline{U_p}})^{-1}(K) = \overline{U_p} \cap F^{-1}(K)$ is compact. First, only the part of $K$ actually hit matters:
> $$\overline{U_p} \cap F^{-1}(K) = \overline{U_p} \cap F^{-1}\big(K \cap \overline{F(\overline{U_p})}\big),$$
> because for $x \in \overline{U_p}$ we have $F(x) \in F(\overline{U_p}) \subseteq \overline{F(\overline{U_p})}$, so $F(x) \in K$ holds if and only if $F(x) \in K \cap \overline{F(\overline{U_p})}$. Now set
> $$K_0 := K \cap \overline{F(\overline{U_p})}.$$
> The set $K_0$ is a closed subset of the compact $K$ (an intersection of $K$ with the closed set $\overline{F(\overline{U_p})}$), hence compact by Lemma 1(a); and $K_0 \subseteq \overline{F(\overline{U_p})} \subseteq N$ by Step 1, so $K_0$ lies entirely inside the target chart. Therefore
> $$L := \kappa_Y(K_0) \subseteq \widehat{N} \subseteq \mathbb{Y}$$
> is well-defined, and it is compact by Lemma 1(b), being the continuous image of the compact $K_0$ under the homeomorphism $\kappa_Y$.
>
> **Step 3 — apply the model properness.** Transport the preimage into the coordinates through $\psi$. For $\xi \in \overline{B}_r$, writing $x = \psi(\xi) \in \overline{U_p}$, we have $F(x) \in K_0$ if and only if $\kappa_Y(F(x)) \in L$ (as $K_0 \subseteq N$ and $\kappa_Y$ is a bijection on $N$), and $\kappa_Y(F(x)) = \kappa_Y(F(\kappa_X^{-1}(\phi(\xi)))) = \widehat{F}(\phi(\xi)) = G(\xi)$. Hence
> $$\psi^{-1}\big(\overline{U_p} \cap F^{-1}(K_0)\big) = \{\xi \in \overline{B}_r : G(\xi) \in L\}.$$
> By Lemma 3, with the compact set $L \subseteq \mathbb{Y}$, the right-hand side is compact. Applying the homeomorphism $\psi$, which preserves compactness by Lemma 1(b),
> $$\overline{U_p} \cap F^{-1}(K) = \overline{U_p} \cap F^{-1}(K_0) = \psi\big(\{\xi \in \overline{B}_r : G(\xi) \in L\}\big)$$
> is compact. Since $K \subseteq Y$ was an arbitrary compact set, the restriction $F|_{\overline{U_p}}$ is proper.
>
> As $p \in X$ was arbitrary, every point has such a neighbourhood, so $F$ is locally proper. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Covering maps and deck transformations (algebraic topology).** A covering map $\pi : \widetilde{Z} \to Z$ with a finite fibre over each point of a locally compact Hausdorff $Z$ is proper, so by Part (i) it is closed; combined with the fact that it is open, this shows its image is clopen, hence all of $Z$ when $Z$ is connected. The theorem applies because the finiteness of the fibre plus local triviality forces preimages of compact sets to be compact, and the non-obvious point is that "closed" is not automatic for covering maps of infinite total space until properness is checked. This is the mechanism behind the statement that a finite-sheeted covering of a connected base is surjective.

**Coercive variational problems (calculus of variations, PDE).** A functional whose gradient map $F = \nabla E : H \to H^\ast$ on a Hilbert space is Fredholm and coercive — meaning $\lVert F(u) \rVert \to \infty$ as $\lVert u \rVert \to \infty$ — is proper, so its critical values are closed and its degree is defined; Part (ii) already guarantees local properness, and the coercivity is exactly the extra global hypothesis that upgrades local to global properness. The theorem applies because coercivity is the analyst's phrasing of "preimages of bounded sets are bounded", and the non-obvious step is recognising that a growth estimate at infinity is the topological properness that degree theory demands.

**Proper group actions and quotients (Lie theory, geometry).** An action of a locally compact group $G$ on a locally compact Hausdorff space $Z$ is proper when the map $G \times Z \to Z \times Z$, $(g, z) \mapsto (g \cdot z, z)$, is proper; Part (i) then makes the orbit map closed, so orbits are closed and the quotient $Z/G$ is Hausdorff. The theorem applies because Hausdorffness of the quotient is exactly the closedness of the orbit equivalence relation, and the non-obvious content is that a single properness hypothesis on the action controls the separation properties of the quotient — the reason "proper" is the standing hypothesis throughout the theory of homogeneous spaces and moduli.

---

# Bridges

- **[[Thm - Sard-Smale Theorem|Sard–Smale theorem]]** — the immediate consumer. Its proof covers $X$ by the countably many neighbourhoods $U_p$ of Part (ii); on each, $F|_{\overline{U_p}}$ is proper, so by Part (i) the image $F(\operatorname{Crit} F \cap \overline{U_p})$ of the closed critical set is closed. A closed set that meets every finite-dimensional Kuranishi slice in a Lebesgue-null set has empty interior, so each such image is nowhere dense, and the regular values are the complement of a countable union of nowhere dense sets, a residual — hence dense, by Baire — set. Part (i) is the exact step that turns "null in every slice" into "nowhere dense".

- **[[Def - Mod-2 Degree of a Proper Fredholm Map|Mod-2 degree]]** — the definition this page underwrites. For a proper index-zero Fredholm map, a regular value $y$ has $F^{-1}(y)$ a compact zero-dimensional manifold, hence finite, and $\deg_2 F := \# F^{-1}(y) \bmod 2$. Compactness of $F^{-1}(y)$ is properness applied to the compact set $\{y\}$; the well-definedness proof then uses Part (i) to make the regular values open, so that the count is locally constant.

- **The inverse function theorem near a regular value** — the complementary local picture. Where Part (ii) controls the *global* preimage of a compact set by trapping it in a compact box, the [[Thm - Kuranishi Model for a Fredholm Map|Kuranishi model]] with vanishing cokernel makes $F$ a local diffeomorphism at each preimage point; combining the two shows that near a regular value a proper index-zero Fredholm map is a finite covering, which is the geometric content of local constancy of the degree.

- **Heine–Borel and the failure of compactness in infinite dimensions** — the dividing line the proof respects. In the finite-dimensional kernel $X_0$ the [[Thm - Heine–Borel Theorem|Heine–Borel theorem]] trades boundedness for compactness directly; in the infinite-dimensional complement $X_1$ that trade is illegal, and compactness of the fibre coordinate is instead produced as the continuous image $T^{-1}(\pi_{Y_0}(K))$ of a compact target set. The construction is a template for every compactness argument in infinite-dimensional geometry: never from boundedness, always from a continuous image of something already known compact.

---

# Unlocked by This

> [!tip] The critical values of a proper Fredholm map are closed *(from Fredholm degree theory)*
> Because surjectivity of a Fredholm operator is an open condition, $\operatorname{Crit} F$ is closed; Part (i) then makes $F(\operatorname{Crit} F)$ closed, so the regular values are open. This is the opening move of [[Thm - Sard-Smale Theorem|Sard–Smale]] and of the well-definedness of the degree.

> [!tip] Local properness is free for elliptic problems *(from geometric analysis)*
> A semilinear elliptic operator plus a lower-order nonlinearity, read between Sobolev completions, is a Fredholm map, so by Part (ii) it is locally proper with no estimate to check. Global properness must still be arranged — by an a priori bound or a compactness theorem — but the local half is automatic, which is why the Seiberg–Witten and Yang–Mills moduli problems reduce to establishing *global* compactness.
