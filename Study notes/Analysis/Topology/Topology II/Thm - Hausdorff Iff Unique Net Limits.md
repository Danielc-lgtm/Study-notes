---
type: theorem
subject: topology
prereqs:
  - "Def - Separation Axioms"
  - "Def - Directed Set and Net"
  - "Def - Net Convergence"
  - "Def - Topological Space"
tags: [analysis, topology, separation, nets]
---

# Notation

$X$ is a [[Def - Topological Space|topological space]]. A **net** in $X$ is a function $\Phi : D \to X$ from a [[Def - Directed Set and Net|directed set]] $(D, \leq)$ to $X$; we write $\{x_\alpha\}_{\alpha \in D}$ for $\Phi$. The net **converges to** $x \in X$, written $x_\alpha \to x$, if for every neighborhood $U$ of $x$ there is $\alpha_0 \in D$ with $x_\alpha \in U$ for all $\alpha \geq \alpha_0$ (see [[Def - Net Convergence]]). The space $X$ is **Hausdorff** ([[Def - Separation Axioms|T₂]]) if for any two distinct points $x, y \in X$ there exist disjoint open sets $U \ni x$, $V \ni y$. The full registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Theorem.** A topological space $X$ is **Hausdorff** if and only if every convergent net in $X$ has a unique limit.

The forward direction is immediate. The reverse — net-uniqueness implies Hausdorff — is the substantive half, and it requires constructing a specific net witnessing the failure when Hausdorff fails.

---

# Motivation

The Hausdorff axiom looks innocuous: any two points can be put inside disjoint open sets. But what is it *for*? The honest answer is: *Hausdorff is the precise topological condition that makes "the limit" a well-defined notion*. In a Hausdorff space, the phrase "$\lim x_\alpha = x$" determines $x$ uniquely, so it is meaningful as a definite description; in a non-Hausdorff space, a sequence or net can converge to several points at once, and "the limit" is ambiguous.

This is not a metaphysical observation — it is a checkable theorem, this one. And the reverse direction is what gives the result its power: non-uniqueness of limits implies non-Hausdorff. So when one wants to prove a space is *not* Hausdorff, the cleanest method is to exhibit a net (or in nice spaces, a sequence) converging to two distinct points. The cofinite topology on an infinite set is the canonical example: every nonempty open set is cofinite, so two opens always intersect, so points cannot be separated; and indeed every injective sequence converges to *every* point.

The deeper reason this matters: many theorems in analysis are about the limit of an approximation procedure (an iteration, a sequence of solutions, an integral as a limit of Riemann sums). For these to make sense as statements about a *specific* object, the ambient space must be Hausdorff. This theorem makes the link between "I can separate points" (a structural axiom) and "limits are unique" (an operational consequence) precise.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$X$ is Hausdorff".

The first disguised source is **$X$ is a metric space**. Property $B$: $X$ has a metric $d$. The bridge: distinct $x \neq y$ have $d(x, y) = r > 0$, and the open balls $B_{r/2}(x), B_{r/2}(y)$ are disjoint by the triangle inequality. *Example:* every $\mathbb{R}^n$, every Hilbert space, every Banach space, every function space with a sup norm — all are metric, hence Hausdorff, hence the limit notation is well-defined.

The second disguised source is **$X$ is a subspace, product, or coproduct of Hausdorff spaces**. Property $B$: $X$ inherits from known Hausdorff spaces by a topological construction. The bridge: subspaces, arbitrary products, and disjoint unions of Hausdorff spaces are Hausdorff. *Example:* the product $\prod_\alpha X_\alpha$ of Hausdorff spaces is Hausdorff, so weak topologies (subspaces of products) are Hausdorff. The infinite-product example is what makes the [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Tychonoff theorem]] in conjunction with this useful: a product of compact Hausdorff spaces is compact Hausdorff.

The third disguised source is **$X$ has the property that the diagonal $\Delta = \{(x, x) : x \in X\}$ is closed in $X \times X$**. Property $B$: $\Delta$ is closed. The bridge: $X$ Hausdorff if and only if $\Delta$ is closed in $X \times X$. The proof: if $X$ is Hausdorff and $(x, y) \notin \Delta$, separate $x, y$ by $U, V$; then $U \times V$ is an open neighborhood of $(x, y)$ avoiding $\Delta$. Conversely, if $\Delta$ is closed and $x \neq y$, then $(x, y) \notin \Delta$ has an open box neighborhood $U \times V$ avoiding $\Delta$, meaning $U \cap V = \emptyset$. *Example:* this is the working characterization in algebraic geometry, where Hausdorffness fails for the Zariski topology but the "separated" condition (closed diagonal in the *fibre product*) is the scheme-theoretic analog.

**Targets (Output Amplification)**

The conclusion is "every convergent net in $X$ has a unique limit", which lets one *use* the notation $\lim x_\alpha$.

Combine the conclusion with **continuity of a function**. Property $D$: $f : X \to Y$ is continuous and $Y$ is Hausdorff, with $X_0 \subseteq X$ dense and $f|_{X_0} = g|_{X_0}$ for another continuous $g : X \to Y$. Amplified result $E$: $f = g$ on all of $X$. The bridge: for any $x \in X$, $x$ is the limit of a net in $X_0$ ($X_0$ is dense), and continuity gives $f(x_\alpha) \to f(x)$, $g(x_\alpha) \to g(x)$. The two image nets agree (since $f = g$ on $X_0$), and by uniqueness $f(x) = g(x)$. This is the standard "two continuous functions agreeing on a dense set are equal" argument, foundational for distributional calculus and unique extensions.

Combine the conclusion with **compactness of $X$**. Property $D$: $X$ is compact. Amplified result $E$: every net has a convergent subnet *with a unique limit*, and compact Hausdorff spaces enjoy a vast list of structural consequences: they are normal (Bredon 7.11), continuous bijections out of them to Hausdorff are homeomorphisms ([[Thm - Compact to Hausdorff Continuous Bijection is Homeomorphism]]), and the topology is "rigid" — neither weaker nor stronger topologies on the same set are both compact and Hausdorff. The compact-Hausdorff combination is the gold standard in topology.

Combine the conclusion with **the topology being defined by a family of seminorms**. Property $D$: $X = V$ is a topological vector space and the topology is given by seminorms $\{p_\alpha\}$. Amplified result $E$: the topology is Hausdorff if and only if the seminorms *separate points* (i.e., $p_\alpha(x) = 0$ for all $\alpha$ implies $x = 0$). This is the operational form of Hausdorffness in functional analysis and is what distinguishes weakly Hausdorff topologies (good) from non-Hausdorff topological vector spaces (rare and pathological).

---

# Why Is It True

The forward direction is mechanical: if $x \neq y$, disjoint opens $U \ni x$, $V \ni y$ exist; a net cannot be eventually in both $U$ and $V$ (they are disjoint), so it cannot converge to both $x$ and $y$.

The reverse direction is the substantive one. The intuition: if $X$ is *not* Hausdorff, then there exist two points $x \neq y$ that cannot be separated. This means *every* open neighborhood of $x$ intersects *every* open neighborhood of $y$. So one can always find a point in the intersection — a point that is "close to both". By making such choices systematically across all neighborhood pairs of $x$ and $y$, one builds a net that converges to both, breaking uniqueness.

The systematic choice mechanism is the directed-set construction:

- *Index set:* all pairs $(U, V)$ where $U$ is an open neighborhood of $x$ and $V$ is an open neighborhood of $y$.
- *Ordering:* $(U_1, V_1) \geq (U_2, V_2)$ if and only if $U_1 \subseteq U_2$ *and* $V_1 \subseteq V_2$ (i.e., reverse inclusion in each coordinate).
- *Direction:* $(U_1, V_1)$ and $(U_2, V_2)$ both lie below $(U_1 \cap U_2, V_1 \cap V_2)$ in the order, and the intersection is open. So any two indices have an upper bound — the index set is directed.
- *Net value:* at index $(U, V)$, pick any point $z_{(U, V)} \in U \cap V$. This is possible because $x$ and $y$ cannot be separated, so $U \cap V \neq \emptyset$.

Now check: for any neighborhood $W$ of $x$, the index $(W, X)$ exists; and at any $(U, V) \geq (W, X)$, $U \subseteq W$, so $z_{(U, V)} \in U \cap V \subseteq W$. So the net is eventually in $W$. Hence it converges to $x$. Symmetrically, it converges to $y$. Two limits, distinct, of a single net.

So the failure of Hausdorff is *literally* a failure of net-limit uniqueness, witnessed by an explicit net constructed from the inseparable pair. The directed set "reverse inclusion in each coordinate" is what allows the net to be systematically "close to both" without choice favouring one limit over the other.

Why does the construction need *nets*, not *sequences*? Because in general topological spaces, the neighborhood basis at a point is not countable. The indexing set of *all* neighborhood pairs $(U, V)$ can be enormous — there is no way to enumerate it as $\mathbb{N}$, so one cannot extract a sequence with the desired behavior in general. In first-countable spaces (in particular, metric spaces), countability lets sequences suffice; in arbitrary spaces, nets are essential.

---

# What Makes This Hard

The non-obvious step is *constructing* the witness net for the reverse direction — specifically choosing the index set to be *pairs* of neighborhoods of $x$ and $y$, with reverse-inclusion-in-each-coordinate ordering, so that an upper bound combines two indices via *intersection*. A common error is to try indexing by neighborhoods of one of the points only, which produces a net converging to that point but not the other; the symmetry between the two limits comes from the *product* indexing. A second common error is to forget that "cannot be separated" is the *negation* of Hausdorff, so $U \cap V \neq \emptyset$ for every pair $(U, V)$ — this is what makes the net values exist at all.

---

# Rederivation Scaffold

**High-level strategy:**
The forward direction is one line: disjoint opens prevent convergence to two points. The reverse direction constructs a net whose existence breaks Hausdorff: index by pairs of neighborhoods of the inseparable points ordered by reverse inclusion in each, pick points in the (nonempty) intersection, and show the resulting net converges to both.

**Subgoal decomposition:**

1. **(Forward) Hausdorff implies unique net limits.** Suppose $X$ is Hausdorff and $x_\alpha \to x, x_\alpha \to y$ with $x \neq y$. Derive a contradiction.
   - *Hint:* Disjoint opens $U \ni x, V \ni y$ exist by Hausdorff; net is eventually in both, but they are disjoint.
   - *Why needed:* The easy direction.

2. **(Reverse) Set up the contrapositive.** Suppose $X$ is not Hausdorff. Then there exist $x \neq y$ with the property that every neighborhood of $x$ intersects every neighborhood of $y$.
   - *Hint:* Negate the Hausdorff axiom.
   - *Why needed:* It produces the inseparable pair from which the witness net is built.

3. **(Reverse) Construct the index directed set.** Let $D = \{(U, V) : U \text{ open nbhd of } x, V \text{ open nbhd of } y\}$ ordered by $(U_1, V_1) \geq (U_2, V_2) \iff U_1 \subseteq U_2 \text{ and } V_1 \subseteq V_2$.
   - *Hint:* The upper bound of $(U_1, V_1)$ and $(U_2, V_2)$ is $(U_1 \cap U_2, V_1 \cap V_2)$.
   - *Why needed:* The reverse-inclusion ordering is what makes the net "go to both".

4. **(Reverse) Define the net.** At each $(U, V) \in D$, pick $z_{(U, V)} \in U \cap V$. This is possible because $U \cap V \neq \emptyset$.
   - *Hint:* Axiom of choice (or just pick one once $U \cap V$ is known nonempty).
   - *Why needed:* It uses the inseparability of $x$ and $y$ — the negation of Hausdorff.

5. **(Reverse) Verify $z_{(U, V)} \to x$ and $z_{(U, V)} \to y$.** For any neighborhood $W$ of $x$, the indices $\geq (W, X)$ all give $z \in U \subseteq W$.
   - *Hint:* The "second coordinate $X$" trick: every $(U, V) \geq (W, X)$ has $U \subseteq W$, regardless of $V$.
   - *Why needed:* This is the asymmetry: convergence to $x$ uses only the first coordinate of the index, so the second coordinate is "free" to do the work for $y$.

6. **(Reverse) Conclude.** Two limits, contradiction with uniqueness, so the hypothesis "not Hausdorff" is incompatible with "unique limits".

---

# Lemma Decomposition

> [!note]- Lemma 1: Pairs ordered by reverse inclusion in each coordinate form a directed set
> **Statement:** Let $\mathcal{N}_x$ be the open neighborhoods of $x$ and $\mathcal{N}_y$ those of $y$. The set $D = \mathcal{N}_x \times \mathcal{N}_y$ with $(U_1, V_1) \geq (U_2, V_2) \iff U_1 \subseteq U_2 \text{ and } V_1 \subseteq V_2$ is a directed set.
>
> **Hint:** The upper bound of $(U_1, V_1)$ and $(U_2, V_2)$ is $(U_1 \cap U_2, V_1 \cap V_2)$.
>
> **Why needed:** It is the indexing set for the witness net.
>
> > [!note]- Full proof
> > Reflexivity and transitivity of $\leq$ follow from those of set inclusion. For directedness: given $(U_1, V_1), (U_2, V_2) \in D$, the intersection $U_1 \cap U_2$ is open and contains $x$ (so it is in $\mathcal{N}_x$); similarly $V_1 \cap V_2 \in \mathcal{N}_y$. Then $(U_1 \cap U_2, V_1 \cap V_2)$ is an upper bound of both: $U_1 \cap U_2 \subseteq U_1$ and $U_1 \cap U_2 \subseteq U_2$, so $(U_1 \cap U_2, V_1 \cap V_2) \geq (U_1, V_1)$ and similarly $\geq (U_2, V_2)$.

> [!note]- Lemma 2: Failure of Hausdorff means every neighborhood of $x$ meets every neighborhood of $y$
> **Statement:** $X$ is not Hausdorff $\iff$ there exist $x \neq y$ such that for every open $U \ni x$ and every open $V \ni y$, $U \cap V \neq \emptyset$.
>
> **Hint:** Direct negation of the Hausdorff axiom.
>
> **Why needed:** It supplies the points $z_{(U, V)} \in U \cap V$ that define the witness net.
>
> > [!note]- Full proof
> > Hausdorff says: for all $x \neq y$, there exist disjoint open $U \ni x, V \ni y$. The negation is: there exist $x \neq y$ such that for every choice of opens $U \ni x, V \ni y$, $U \cap V \neq \emptyset$.

> [!note]- Lemma 3: The witness net converges to both $x$ and $y$
> **Statement:** Let $X$ not be Hausdorff, $x \neq y$ inseparable, $D$ as in Lemma 1, and $z : D \to X$ with $z_{(U, V)} \in U \cap V$. Then $z_{(U, V)} \to x$ and $z_{(U, V)} \to y$.
>
> **Hint:** For the $x$-convergence, use indices $\geq (W, X)$; for the $y$-convergence, use indices $\geq (X, W)$.
>
> **Why needed:** It is the witness of non-uniqueness.
>
> > [!note]- Full proof
> > Fix a neighborhood $W$ of $x$. For any $(U, V) \geq (W, X)$, $U \subseteq W$, so $z_{(U, V)} \in U \cap V \subseteq W$. Hence the net is eventually in $W$, so $z \to x$.
> >
> > By symmetry, with $(X, W)$ in place of $(W, X)$: for any $(U, V) \geq (X, W)$, $V \subseteq W$ (where $W$ is now a neighborhood of $y$), so $z_{(U, V)} \in U \cap V \subseteq W$. Hence $z \to y$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> **Forward direction ($\Rightarrow$).** Suppose $X$ is Hausdorff. Let $\{x_\alpha\}_{\alpha \in D}$ be a net with $x_\alpha \to x$ and $x_\alpha \to y$. If $x \neq y$, by Hausdorff there are disjoint open $U \ni x, V \ni y$. By the definition of convergence, there are $\alpha_1, \alpha_2 \in D$ with $x_\alpha \in U$ for $\alpha \geq \alpha_1$ and $x_\alpha \in V$ for $\alpha \geq \alpha_2$. Choose $\alpha \geq \alpha_1, \alpha_2$ (using directedness of $D$); then $x_\alpha \in U \cap V = \emptyset$, contradiction. So $x = y$.
>
> **Reverse direction ($\Leftarrow$, contrapositive).** Suppose $X$ is *not* Hausdorff. Then by Lemma 2, there exist $x \neq y$ with $U \cap V \neq \emptyset$ for every open $U \ni x, V \ni y$.
>
> By Lemma 1, $D = \mathcal{N}_x \times \mathcal{N}_y$ ordered by $(U_1, V_1) \geq (U_2, V_2) \iff U_1 \subseteq U_2$ and $V_1 \subseteq V_2$ is a directed set. For each $(U, V) \in D$, choose $z_{(U, V)} \in U \cap V$ (using nonemptiness of the intersection); this defines a net $z : D \to X$.
>
> By Lemma 3, $z \to x$ and $z \to y$. Since $x \neq y$, $X$ has a convergent net with non-unique limit. Contrapositively, if every convergent net in $X$ has a unique limit, then $X$ is Hausdorff. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Proving the cofinite topology on $\mathbb{N}$ is not Hausdorff.** In $(\mathbb{N}, \tau_{\text{cof}})$, every nonempty open is cofinite, so any two nonempty opens intersect — the inseparable-pair construction picks any two distinct points, and the witness net (which can be taken as the sequence $z_n = n$ with $D = \mathbb{N}$) is eventually in every cofinite set. So it converges to *every* point of $\mathbb{N}$. By this theorem (contrapositively), $(\mathbb{N}, \tau_{\text{cof}})$ is not Hausdorff. The application makes the abstract theorem concrete and shows how a single net can witness massive failure of uniqueness.

**The zero-section of a non-separated scheme.** In algebraic geometry, the *affine line with doubled origin* is built by gluing two copies of $\mathbb{A}^1$ along $\mathbb{A}^1 \setminus \{0\}$. The two origins cannot be separated, and the analog of the witness net is the "sequence approaching zero from the right" — which has both origins as limits. This is exactly the algebraic-geometric incarnation of non-Hausdorffness; "separatedness" of a scheme is the scheme-theoretic Hausdorff axiom (defined via closed diagonal in the fibre product), and the failure mode is identical.

**Hausdorffness via the closed-diagonal criterion in product topology.** A topological group $G$ is Hausdorff if and only if $\{e\}$ is closed (because the diagonal $\Delta \subseteq G \times G$ is the preimage of $\{e\}$ under the continuous map $(g, h) \mapsto gh^{-1}$). Combined with this theorem: $\{e\}$ closed implies every net's limit is unique. This is the operational form in [[Group Theory I — §1.1–1.2|topological group theory]] and shows the depth of the closed-diagonal characterization.

---

# Bridges

- **[[Def - Separation Axioms]]** — Hausdorff is $T_2$, the middle separation axiom. This theorem is its operational characterization: $T_2$ buys uniqueness of limits.

- **[[Thm - Continuity via Nets]]** — the companion characterization of continuity via nets. Together, this theorem and continuity-via-nets give the complete net-theoretic restatement of the basic structures of point-set topology: convergence (nets), continuity (preservation of nets), closure (set of net-limits), and Hausdorffness (uniqueness of net-limits).

- **[[Thm - Closure via Nets]]** — closure equals the set of net-limits. In a Hausdorff space, this set is "small" in the sense that limits are unique — but the set of nets converging to $x$ is still huge.

- **[[Def - Net Convergence]]** — the foundational definition this theorem characterizes.

- **The closed-diagonal characterization** — $X$ is Hausdorff iff the diagonal $\Delta \subseteq X \times X$ is closed. This is the *external* (product-topology) characterization, complementing the *internal* (uniqueness-of-net-limits) characterization given by this theorem.

---

# Unlocked by This

> [!tip] Unique Limits and the Notation $\lim x_\alpha$ *(General Convention)*
> In a Hausdorff space, when a net converges, *the* limit is well-defined, and the notation $\lim_\alpha x_\alpha$ refers to it unambiguously. This convention is so universal that "Hausdorff" is often left implicit — it is the minimal assumption that lets limit notation be used.

> [!tip] Separated Schemes *(from Algebraic Geometry)*
> The Zariski topology is rarely Hausdorff, but the **separated** condition in scheme theory is its replacement: a morphism $X \to S$ is separated if the diagonal $X \to X \times_S X$ is a closed immersion. This is the closed-diagonal characterization elevated to the scheme-theoretic level, and it plays the role Hausdorffness plays in topology — uniqueness of limits in a categorical sense.

> [!tip] Weak Topologies in Functional Analysis *(from Functional Analysis)*
> The **weak topology** on a normed space $V$ — the coarsest topology making all $\varphi \in V^*$ continuous — is Hausdorff if and only if $V^*$ separates points (always true by Hahn–Banach for normed spaces). So Hausdorffness on the weak topology is automatic, and limits in the weak sense are unique by this theorem.
