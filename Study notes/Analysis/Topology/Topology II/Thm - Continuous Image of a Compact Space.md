---
type: theorem
subject: topology
prereqs:
  - "Def - Compact Space"
  - "Def - Continuous Map"
  - "Def - Topological Space"
tags: [analysis, topology, compactness]
---

# Notation

$X, Y$ are [[Def - Topological Space|topological spaces]] and $f : X \to Y$ a continuous map (see [[Def - Continuous Map]]). $X$ is **compact** if every open cover of $X$ has a finite subcover (see [[Def - Compact Space]]). The image $f(X) \subseteq Y$ is equipped with the [[Def - Subspace Topology|subspace topology]]. The full registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Theorem.** Let $f : X \to Y$ be a continuous map and suppose $X$ is **compact**. Then the image $f(X) \subseteq Y$, with the subspace topology, is compact.

The proof is one line: pull back any open cover of $f(X)$ via $f$ to get an open cover of $X$, extract a finite subcover, push forward.

---

# Motivation

Compactness is the topological encoding of "finite enough to make analysis work" — the property that lets one extract finite descriptions from infinite covers, attain extrema, pass between sequences and subsequences. The question this theorem answers is: *which structural properties of a space transfer to its continuous images*?

For connectedness, the analog ([[Thm - Continuous Image of a Connected Space]]) is true and proven by a similar one-line argument. For Hausdorffness, no such propagation holds in general (the image of a Hausdorff space under a continuous map can be non-Hausdorff: the quotient of $\mathbb{R}$ identifying $(0, \infty)$ to a point is not Hausdorff). But for compactness, the answer is yes and free: continuous maps preserve compactness.

The reason it works: compactness is about open covers, and continuity controls open covers in *reverse* — preimages of opens are open. So an open cover of $f(X)$ pulls back to an open cover of $X$; compactness of $X$ gives a finite subcover of $X$; the corresponding finite collection of opens on $Y$ covers $f(X)$. The argument is the same structural pattern as the connectedness propagation: continuity controls the relevant structure (open covers / clopen subsets) backwards, and the source-side hypothesis (compactness / connectedness) does the rest.

The most important corollary of this theorem is the **Extreme Value Theorem**: a continuous real-valued function on a compact space attains its maximum and minimum. The proof is: by this theorem, $f(X) \subseteq \mathbb{R}$ is compact, hence closed and bounded by [[Thm - Heine–Borel Theorem|Heine–Borel]], hence has a maximum and minimum that are attained (because $f(X)$ is closed, the supremum is in $f(X)$). The Extreme Value Theorem is the engine behind every existence-of-extremizer argument in analysis — variational principles, optimization on compact domains, the existence of critical points in finite-dimensional problems. All of it descends from this theorem.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$X$ is compact".

The first disguised source is **$X$ is a closed bounded subset of $\mathbb{R}^n$**. Property $B$: $X \subseteq \mathbb{R}^n$ is closed and bounded. The bridge: by [[Thm - Heine–Borel Theorem|Heine–Borel]], $X$ is compact. *Example:* $[a, b]$ in $\mathbb{R}$, closed disks $\overline{D^n}$ in $\mathbb{R}^n$, the sphere $S^n$. Every concrete compactness argument in real analysis routes through Heine–Borel, then this theorem.

The second disguised source is **$X$ is a closed subset of a compact space**. Property $B$: $X \subseteq Z$ closed, $Z$ compact. The bridge: by [[Thm - Closed Subset of Compact is Compact]]. *Example:* a closed subset of $[0, 1]^n$ is compact (the cube is compact by Tychonoff finite case, then this); a closed subset of any Banach space's closed unit ball in the weak topology is compact (by Banach–Alaoglu).

The third disguised source is **$X$ is a product of compact spaces**. Property $B$: $X = \prod_\alpha X_\alpha$ with each $X_\alpha$ compact. The bridge: by **Tychonoff's theorem** (in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]). *Example:* the cube $[0, 1]^A$ for any index set $A$ is compact, so any continuous image of it is compact — this is the engine of the Stone-Čech compactification, weak-$*$ compactness of bounded sets, and the Tychonoff topology in algebraic geometry.

The fourth disguised source is **the image is of a sequentially compact set under a continuous map in a metric space**. Property $B$: $X$ is sequentially compact (every sequence has a convergent subsequence), and the target is metric. The bridge: in metric spaces, sequentially compact equals compact (via Bolzano–Weierstrass-style arguments). *Example:* in $\mathbb{R}^n$, sequentially compact = closed and bounded by Bolzano–Weierstrass.

**Targets (Output Amplification)**

The conclusion is "$f(X)$ is compact in $Y$".

Combine the conclusion with **$Y = \mathbb{R}$**. Property $D$: $f$ real-valued. Amplified result $E$: $f$ attains its maximum and minimum. The bridge: by [[Thm - Heine–Borel Theorem|Heine–Borel]], $f(X)$ is closed and bounded in $\mathbb{R}$; hence $\sup f(X) = \max f(X)$ exists and is attained, and similarly for $\min$. This is the **Extreme Value Theorem**. *Example:* every variational problem on a compact domain — minimum-area surface with fixed boundary, shortest path in a compact metric space, etc. — has a solution.

Combine the conclusion with **$Y$ Hausdorff**. Property $D$: $Y$ is Hausdorff. Amplified result $E$: $f(X)$ is closed in $Y$ (by [[Thm - Compact Subset of Hausdorff is Closed]]). The bridge: compact subsets of Hausdorff spaces are closed. *Example:* this gives the **closed map property**: $f$ takes closed sets in $X$ to closed sets in $Y$ — a continuous map from a compact space to a Hausdorff space is automatically closed.

Combine the conclusion with **a continuous bijection $f$ to Hausdorff $Y$**. Property $D$: $f$ is bijective, $Y$ Hausdorff. Amplified result $E$: $f$ is a homeomorphism (by [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]]). The bridge: closed map + bijective continuous = homeomorphism. *Example:* every continuous bijection between compact Hausdorff spaces is automatically a homeomorphism — eliminating the need to verify continuity of $f^{-1}$ in a vast class of identifications.

Combine the conclusion with **the FIP characterization or convergent-subnet characterization of compactness**. Property $D$: a sequence of approximations $\{y_n\} \subseteq f(X)$. Amplified result $E$: by compactness, $\{y_n\}$ has a convergent subsequence (in a sequentially compact = compact metric space), or a convergent subnet (in general). *Example:* every minimizing sequence for a continuous functional on a compact space has a convergent subsequence — the foundation of the direct method in the calculus of variations.

---

# Why Is It True

The theorem is a structural propagation: compactness on $X$ is an open-cover property; continuity controls open covers in reverse via preimages; so a finite-subcover property transports through.

The mechanical argument:

- Let $\{V_i\}_{i \in I}$ be an open cover of $f(X)$ in the subspace topology. Each $V_i = U_i \cap f(X)$ for some open $U_i \subseteq Y$ (or, working in $Y$, take an open cover of $f(X)$ by opens of $Y$).
- The preimages $\{f^{-1}(U_i)\}_{i \in I}$ are open in $X$ (continuity), and they cover $X$: any $x \in X$ has $f(x) \in f(X)$, hence $f(x) \in U_i$ for some $i$, hence $x \in f^{-1}(U_i)$.
- By compactness of $X$, extract a finite subcover $\{f^{-1}(U_{i_1}), \ldots, f^{-1}(U_{i_n})\}$.
- Then $\{U_{i_1}, \ldots, U_{i_n}\}$ covers $f(X)$: any $y \in f(X)$ has $y = f(x)$ for some $x \in X$; $x$ is in some $f^{-1}(U_{i_k})$, so $y = f(x) \in U_{i_k}$.

So the finite subcover of $X$ has its image covering $f(X)$, giving the required finite subcover of the original cover of $f(X)$.

The geometric picture: a continuous map "shrinks or stretches" — but it cannot create complexity beyond what the source has. If the source has the finiteness property (compactness), the image inherits it, because any covering structure of the image pulls back to a covering structure of the source.

The reason this *fails* for non-compactness statements is that one cannot "push covers forward" in general — continuity only controls *preimages*, not images. So if an open set in $Y$ contains $f(X)$, its preimage might be larger than needed, and the cover structure on $X$ might not match. The compactness argument works precisely because the finite-subcover property is about the *source*, and continuity lets one pull a cover of the image back to one of the source.

---

# What Makes This Hard

The theorem itself is one line, but the *applications* require recognizing the disguised source: many compactness hypotheses arrive as "closed and bounded in $\mathbb{R}^n$", "closed subset of a compact set", "product of compacts", or "sequentially compact metric", and the reader must reroute each to compactness before applying the theorem. The most common error is to confuse direction: continuity controls preimages, so one pulls covers of the *image* back to covers of the *source*, not the other way. A second pitfall is to forget that the image carries the *subspace topology* — opens of $f(X)$ are intersections of opens of $Y$ with $f(X)$, not just opens of $Y$.

---

# Rederivation Scaffold

**High-level strategy:**
Pull back any open cover of $f(X)$ via $f$ to get an open cover of $X$; extract a finite subcover via compactness of $X$; the corresponding finitely many opens of $Y$ cover $f(X)$.

**Subgoal decomposition:**

1. **Set up: an open cover of $f(X)$.** Take an open cover $\{V_i\}$ of $f(X)$ in $Y$ (equivalently $V_i = U_i \cap f(X)$ for open $U_i$).
   - *Hint:* Compactness is a finite-subcover property; start with an arbitrary cover.

2. **Pull back to an open cover of $X$.** $\{f^{-1}(U_i)\}$ is an open cover of $X$.
   - *Hint:* Continuity gives openness of $f^{-1}(U_i)$; surjectivity onto $f(X)$ gives covering.
   - *Why needed:* It is the only step using continuity.

3. **Extract a finite subcover of $X$.** By compactness of $X$.
   - *Hint:* Definition of compactness.

4. **Push forward to a finite cover of $f(X)$.** $\{U_{i_1}, \ldots, U_{i_n}\}$ has images covering $f(X)$.
   - *Hint:* Surjectivity: each $y \in f(X)$ is $f(x)$ for some $x$, which is in some $f^{-1}(U_{i_k})$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Continuous preimages of an open cover form an open cover of the domain
> **Statement:** If $\{V_i\}_{i \in I}$ is an open cover of $f(X)$ (in $f(X)$'s subspace topology, equivalently $V_i = U_i \cap f(X)$ for open $U_i \subseteq Y$), then $\{f^{-1}(U_i)\}_{i \in I}$ is an open cover of $X$.
>
> **Hint:** Openness from continuity; covering from $f(X) \subseteq \bigcup_i U_i$.
>
> **Why needed:** It is the pullback construction.
>
> > [!note]- Full proof
> > *Openness:* each $f^{-1}(U_i)$ is the preimage of an open set under the continuous $f$, hence open.
> >
> > *Covering:* for any $x \in X$, $f(x) \in f(X) \subseteq \bigcup_i U_i$, so $f(x) \in U_i$ for some $i$, hence $x \in f^{-1}(U_i)$. So $X = \bigcup_i f^{-1}(U_i)$.

> [!note]- Lemma 2: Pushing a finite subcover of $X$ forward gives a finite cover of $f(X)$
> **Statement:** If $\{f^{-1}(U_{i_k})\}_{k=1}^n$ covers $X$, then $\{U_{i_k}\}_{k=1}^n$ covers $f(X)$ in $Y$ (equivalently $\{V_{i_k}\} = \{U_{i_k} \cap f(X)\}$ covers $f(X)$ in subspace topology).
>
> **Hint:** Image of a point in $f^{-1}(U)$ is in $U$.
>
> **Why needed:** It is the forward push.
>
> > [!note]- Full proof
> > Let $y \in f(X)$, $y = f(x)$ for some $x \in X$. Since $\{f^{-1}(U_{i_k})\}_{k=1}^n$ covers $X$, $x \in f^{-1}(U_{i_k})$ for some $k$, i.e., $f(x) \in U_{i_k}$. So $y \in U_{i_k}$. As $y$ was arbitrary, $f(X) \subseteq \bigcup_{k=1}^n U_{i_k}$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> Let $f : X \to Y$ be continuous with $X$ compact. We show $f(X)$ (with subspace topology) is compact.
>
> Let $\{V_i\}_{i \in I}$ be an open cover of $f(X)$. Write $V_i = U_i \cap f(X)$ for opens $U_i \subseteq Y$. By Lemma 1, $\{f^{-1}(U_i)\}_{i \in I}$ is an open cover of $X$.
>
> By compactness of $X$, extract a finite subcover $\{f^{-1}(U_{i_k})\}_{k=1}^n$. By Lemma 2, $\{U_{i_k}\}_{k=1}^n$ covers $f(X)$, equivalently $\{V_{i_k}\}_{k=1}^n$ covers $f(X)$ in subspace topology.
>
> So every open cover of $f(X)$ has a finite subcover, hence $f(X)$ is compact. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Extreme Value Theorem in $\mathbb{R}^n$.** Let $f : K \to \mathbb{R}$ be continuous on a compact $K \subseteq \mathbb{R}^n$. By this theorem, $f(K) \subseteq \mathbb{R}$ is compact. By [[Thm - Heine–Borel Theorem|Heine–Borel]] in dimension 1, $f(K)$ is closed and bounded, hence has a maximum and minimum, both attained at points of $f(K)$. So $f$ attains its max and min on $K$. This is the workhorse theorem for every optimization problem on a compact domain.

**Existence of geodesics in compact Riemannian manifolds.** On a compact Riemannian manifold $M$, between any two points there is a length-minimizing geodesic. The proof: the space of paths between the two points (with appropriate topology) is "compact in spirit" via Arzelà–Ascoli; the length functional is continuous; by this theorem (applied at the function-space level), the image is compact in $[0, \infty)$, so the minimum is attained. This is a typical "compactness $\to$ extremum exists" argument in differential geometry.

**Compactness of the closed unit ball in finite-dimensional normed spaces.** The closed unit ball $B$ in $\mathbb{R}^n$ is compact (closed and bounded, by [[Thm - Heine–Borel Theorem|Heine–Borel]]). For any continuous linear functional $\varphi : \mathbb{R}^n \to \mathbb{R}$, by this theorem $\varphi(B)$ is compact in $\mathbb{R}$, hence bounded — so $\varphi$ is *bounded* on $B$. This is the trivial finite-dim case of the operator-norm theorem. The deeper version (Banach–Alaoglu) generalizes the conclusion to weak-$*$ topology on infinite-dim duals.

**Continuous image of $[0, 1]$ in any space is "compact-like".** A path $\gamma : [0, 1] \to X$ has image $\gamma([0, 1])$ compact in $X$ by this theorem. Hence every path is bounded (in any metric on $X$), and any continuous function on the path is bounded. The image of a path is the prototype of a "compact piece of a space" — what makes path-connectedness so well-behaved compared to general connectedness.

---

# Bridges

- **[[Thm - Continuous Image of a Connected Space]]** — the connectedness analog. Same structural argument: continuity controls the relevant structure (clopen subsets vs open covers) backwards, and the source hypothesis (connectedness vs compactness) supplies the conclusion.

- **[[Thm - Compact Subset of Hausdorff is Closed]]** — the complementary upgrade. In a Hausdorff target $Y$, the compact image $f(X)$ is automatically closed, giving the closed map property of continuous maps from compact spaces to Hausdorff.

- **[[Thm - Closed Subset of Compact is Compact]]** — provides one of the canonical sources of compact sets: closed subsets of known-compact. Combined with this theorem: continuous image of a closed subset of a known compact is compact.

- **[[Thm - Heine–Borel Theorem]]** — in $\mathbb{R}^n$, compactness is closed and bounded. This is the concrete checkable form of compactness, and this theorem combined with Heine–Borel gives every concrete extremum existence argument.

- **The Extreme Value Theorem** — the canonical corollary. Real-valued continuous functions on compact spaces attain their maximum and minimum.

---

# Unlocked by This

> [!tip] **Extreme Value Theorem** *(from Real Analysis)*
> A continuous real-valued function on a compact space attains its maximum and minimum. Foundation of every optimization problem on a compact domain.

> [!tip] **Closed Map Property** *(from Topology)*
> A continuous map from a compact space to a Hausdorff space is a closed map: it sends closed sets to closed sets. Combined with bijectivity, this gives [[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism|the homeomorphism criterion]].

> [!tip] **Existence of Minimizers in the Calculus of Variations** *(from Functional Analysis)*
> Minimization problems on compact sets in function spaces (typically obtained via Arzelà–Ascoli, Rellich-Kondrachov, Banach–Alaoglu) have solutions whenever the functional is continuous. This theorem applied at the function-space level is the foundation.

> [!tip] **Compactness of the Spectrum in Operator Theory** *(from Functional Analysis)*
> The spectrum $\sigma(T)$ of a bounded operator $T$ on a Banach space is a compact subset of $\mathbb{C}$. The argument uses continuity of the resolvent $z \mapsto (T - zI)^{-1}$ on the resolvent set, which is open and unbounded; compactness of $\sigma(T)$ then comes from a careful boundedness argument plus this theorem.
