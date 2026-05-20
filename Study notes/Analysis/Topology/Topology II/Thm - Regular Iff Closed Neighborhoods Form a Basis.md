---
type: theorem
subject: topology
prereqs:
  - "Def - Separation Axioms"
  - "Def - Topological Space"
  - "Def - Neighbourhood and Neighbourhood Basis"
tags: [analysis, topology, separation]
---

# Notation

$X$ is a Hausdorff [[Def - Topological Space|topological space]]. A **neighborhood** of $x \in X$ is a set $N$ such that $x$ lies in the interior of $N$; a [[Def - Neighbourhood and Neighbourhood Basis|neighborhood basis]] at $x$ is a family of neighborhoods such that every neighborhood of $x$ contains one of them. A neighborhood is **closed** if it is a closed set in $X$ (which contains an open neighborhood of $x$ as its interior). The space $X$ is **regular** ([[Def - Separation Axioms|T₃]]) if it is $T_1$ and for any point $x$ and disjoint closed set $C$ not containing $x$, there exist disjoint open sets $U \ni x$ and $V \supseteq C$. The full registry is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Statement

> **Theorem.** A Hausdorff space $X$ is **regular** if and only if at every point $x \in X$, the closed neighborhoods of $x$ form a neighborhood basis: for every open $V \ni x$, there is a *closed* neighborhood $N$ of $x$ with $N \subseteq V$.

The theorem rephrases the regularity axiom — point-from-closed-set separation — into the operational form "every open neighborhood contains a closed one". The latter is the form used in nearly every proof that invokes regularity.

---

# Motivation

The regularity axiom (separate a point from a disjoint closed set by disjoint opens) is structural and a bit hard to use directly. What one *wants* in practice is to *shrink open sets to smaller closed ones around a point* — to say "if $V$ is an open neighborhood of $x$, I can find an open neighborhood $U$ with $x \in U \subseteq \overline{U} \subseteq V$". This is the operational restatement: closed neighborhoods form a basis.

The two formulations capture the same content from different angles. The separation form says "I can put disjoint covers around a point and a closed set". The basis form says "I can shrink any open neighborhood to a closed one inside it". The bridge between them is that the closed set in the basis form is the complement of an open cover of "everywhere except a small neighborhood of $x$", and vice versa.

The operational form is what makes regularity *useful*. It lets one do "shrink-and-cover" arguments: start with an open cover of a closed set, shrink each open to a closed-inside-open pair, and the closed pieces give you a tighter cover. This is the structural content of Urysohn's lemma (which needs normal, not just regular) and Tietze extension. Regularity buys you the basis form, normal buys you the function form, and the chain ends at metrization (Urysohn's metrization theorem: every regular second-countable Hausdorff space is metrizable).

A second motivation: subspaces of regular spaces are regular. This is one of the cleanest inheritance results for separation axioms, and it follows immediately from the basis form: intersect a closed neighborhood basis at $x \in A$ with $A$ to get a closed-in-$A$ neighborhood basis at $x$ in the subspace topology. The same is *not* true of normality — normality is not preserved by arbitrary subspaces. So regular sits at the sweet spot: strong enough to support basis arguments and inherited cleanly by subspaces.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$X$ is regular Hausdorff".

The first disguised source is **$X$ is a metric space**. Property $B$: $X$ has a metric. The bridge: every metric space is normal (see [[Thm - Metric Spaces are Normal]]), normal implies regular (a point is a closed set, so point-vs-closed-set separation follows from closed-set-vs-closed-set), so every metric space is regular. *Example:* every $\mathbb{R}^n$, every Hilbert space, every Banach space is regular; this is where the closed-neighborhood basis $\overline{B_{r/2}(x)} \subseteq B_r(x)$ comes from.

The second disguised source is **$X$ is a locally compact Hausdorff space**. Property $B$: $X$ is Hausdorff and every point has a compact neighborhood. The bridge: a compact subset of a Hausdorff space is closed (by [[Thm - Compact Subset of Hausdorff is Closed]]), and one can shrink an open neighborhood to a precompact open whose closure is contained inside — this is the key technical lemma in the theory of locally compact Hausdorff spaces, and it is *exactly* this basis form of regularity. *Example:* every locally compact Hausdorff space is regular (and in fact completely regular, by Urysohn-type constructions involving partitions of unity in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]).

The third disguised source is **$X$ is a subspace of a regular space**. Property $B$: $X \subseteq Y$ with $Y$ regular. The bridge: regularity is inherited by subspaces (Corollary 5.3 in Bredon). This is the cleanest separation-axiom inheritance — neither $T_4$ (normal) nor compactness need be preserved by arbitrary subspaces, but regularity is. *Example:* any subspace of $\mathbb{R}^n$, any Lie group as a subspace of $\mathrm{GL}_n(\mathbb{R})$, any manifold as a subspace of $\mathbb{R}^N$ (Whitney embedding) — all are automatically regular.

**Targets (Output Amplification)**

The conclusion is "closed neighborhoods form a basis at every point".

Combine the conclusion with **a compactness hypothesis**. Property $D$: $X$ is regular and a subset $K$ is compact. Amplified result $E$: given any open $V \supseteq K$, there is an open $U$ with $K \subseteq U \subseteq \overline{U} \subseteq V$ (a precompact "tube" around $K$). The bridge: at each $x \in K$, choose a closed neighborhood inside $V$; the interiors cover $K$; extract a finite subcover by compactness; take the union of the chosen open interiors. *Example:* this is the engine of Urysohn-style bump function constructions in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]].

Combine the conclusion with **a sequential or net-continuity argument**. Property $D$: a function $f$ is sequentially continuous (in a first-countable space) or net-continuous. Amplified result $E$: in a regular space with countable neighborhood basis at each point, one can extract a *closed* neighborhood basis, which makes net arguments cleaner — closure operations and limits commute well. *Example:* in functional analysis, the regular structure of locally convex topological vector spaces lets one approximate any open set by closed seminorm balls.

Combine the conclusion with **second countability**. Property $D$: $X$ has a countable basis. Amplified result $E$: by [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Urysohn's metrization theorem]], $X$ is metrizable. The bridge: regular + second countable + Hausdorff implies normal (a Lindelöf argument), then Urysohn produces an embedding into $[0, 1]^{\mathbb{N}}$ via a countable family of continuous functions, yielding a metric. *Example:* every separable metric space could in principle be characterized purely topologically by "regular Hausdorff second-countable", with metrizability emerging from these conditions.

---

# Why Is It True

Both directions of the equivalence are unpackings of definitions, and the geometric picture is the same in both: a *closed neighborhood inside an open one* is precisely *a neighborhood that excludes a closed set surrounding it*.

**Forward direction (regular ⇒ closed-neighborhood basis).** Suppose $X$ is regular, and $V$ is an open neighborhood of $x$. The complement $C = X \setminus V$ is closed and disjoint from $x$. By regularity, separate them by disjoint opens: $U \ni x$ and $W \supseteq C$ with $U \cap W = \emptyset$. Now consider $N = X \setminus W$. This is *closed* (complement of open), and it *contains $U$* (since $U \cap W = \emptyset$ means $U \subseteq X \setminus W$), so $x \in U \subseteq N$ and $N$ has $x$ in its interior — hence $N$ is a closed neighborhood. And $N \subseteq X \setminus W \subseteq X \setminus C = V$. So we have constructed a closed neighborhood $N$ of $x$ with $N \subseteq V$. Done.

The geometric content: $V$ is open around $x$; $C = X \setminus V$ is the "danger zone" outside $V$. Regularity lets you put a "safety zone" $W$ around $C$, disjoint from a neighborhood $U$ of $x$. The complement of the safety zone is a closed neighborhood of $x$ — closed because complementing an open set produces a closed one, and a neighborhood of $x$ because it contains $U$, which is open and contains $x$.

**Reverse direction (closed-neighborhood basis ⇒ regular).** Suppose closed neighborhoods form a basis at every point, and let $x \notin C$ with $C$ closed. Then $V = X \setminus C$ is open and contains $x$. By the basis assumption, there is a closed neighborhood $N$ of $x$ with $N \subseteq V$, so $N \cap C = \emptyset$. Set $U = \mathrm{int}(N)$ (interior of $N$) and $W = X \setminus N$ (complement of $N$). Then $U \ni x$ is open, $W$ is open (complement of closed), $C \subseteq W$ (since $N \subseteq V = X \setminus C$ means $C \subseteq X \setminus N = W$), and $U \cap W = \mathrm{int}(N) \cap (X \setminus N) = \emptyset$. So $U$ and $W$ are disjoint open neighborhoods of $x$ and $C$ respectively. Regularity holds.

The geometric content is symmetric: a closed neighborhood $N$ of $x$ has an *interior* $U$ around $x$ and an *exterior* $X \setminus N$ around $C$, disjoint by construction.

The equivalence is therefore an articulation of the same separation content in two complementary languages: "disjoint open covers of a point and a closed set" and "closed neighborhoods inside open ones". The first is the axiom, the second is the operational tool.

---

# What Makes This Hard

The non-obvious step is recognizing that *the complement of an open cover of $C$ is a closed neighborhood of $x$* — provided the open cover is disjoint from some open neighborhood $U$ of $x$. The most common error is to forget the "neighborhood" requirement (a closed set is not automatically a neighborhood — it must contain a *open* neighborhood as its interior), which trips up readers who try to set $N = X \setminus W$ without verifying that the open $U \subseteq N$ provides the interior. A second common slip is forgetting that the reverse direction uses the *interior* of the closed neighborhood as the open set around $x$ — the closed neighborhood itself is not open, but its interior is open and still contains $x$.

---

# Rederivation Scaffold

**High-level strategy:**
Both directions rest on the identity "complement of an open separating set $W \supseteq C$ is a closed neighborhood of $x$". Forward: get $W$ from regularity, complement it. Reverse: get the closed neighborhood from the basis, then its interior and complement give the open separating sets.

**Subgoal decomposition (forward):**

1. **Convert "$V$ open around $x$" into "$C$ closed away from $x$".** Set $C = X \setminus V$. Then $C$ is closed and $x \notin C$.
   - *Hint:* Complement of open is closed.
   - *Why needed:* Sets up the regularity hypothesis.

2. **Apply regularity to separate $x$ from $C$.** Get disjoint opens $U \ni x$ and $W \supseteq C$.
   - *Hint:* This is the regularity axiom.
   - *Why needed:* It produces the "safety zone" $W$.

3. **Set $N = X \setminus W$ and verify it works.** $N$ is closed (complement of open), contains $U$ (since $U \cap W = \emptyset$), hence $x \in U \subseteq N$ — a closed neighborhood. And $N \subseteq X \setminus C = V$ since $W \supseteq C$.
   - *Hint:* Closed neighborhood = closed set containing an open neighborhood of the point.
   - *Why needed:* This is the conclusion.

**Subgoal decomposition (reverse):**

1. **Convert "$x \notin C$ closed" into "$V$ open around $x$ disjoint from $C$".** Set $V = X \setminus C$.
   - *Hint:* Complement of closed is open.

2. **Apply the basis to find a closed neighborhood $N \subseteq V$.** By hypothesis.

3. **Take $U = \mathrm{int}(N)$ and $W = X \setminus N$ as the separating opens.** $U$ open around $x$, $W$ open containing $C$, disjoint.
   - *Hint:* Interior of $N$ is the largest open subset of $N$; complement of $N$ is open.

---

# Lemma Decomposition

> [!note]- Lemma 1: The complement of an open neighborhood of a closed set is a closed neighborhood of any point separated from the closed set
> **Statement:** Let $C \subseteq X$ be closed, $x \notin C$, and $U, W$ disjoint open with $x \in U$, $C \subseteq W$. Then $N = X \setminus W$ is a closed neighborhood of $x$.
>
> **Hint:** Closed is by complement. Neighborhood: $U \subseteq N$, since $U$ and $W$ are disjoint.
>
> **Why needed:** It is the forward construction.
>
> > [!note]- Full proof
> > $N = X \setminus W$ is closed because $W$ is open. To see $N$ is a neighborhood of $x$: $U$ is open with $x \in U$, and $U \cap W = \emptyset$ means $U \subseteq X \setminus W = N$. So $x$ has an open neighborhood $U$ inside $N$, hence $N$ is a neighborhood of $x$.

> [!note]- Lemma 2: A closed neighborhood disjoint from a closed set produces disjoint open separations
> **Statement:** Let $N$ be a closed neighborhood of $x$ with $N \cap C = \emptyset$ (where $C$ is closed). Set $U = \mathrm{int}(N)$ and $W = X \setminus N$. Then $U, W$ are disjoint open with $x \in U$, $C \subseteq W$.
>
> **Hint:** $U \cap W = \mathrm{int}(N) \cap (X \setminus N) \subseteq N \cap (X \setminus N) = \emptyset$.
>
> **Why needed:** It is the reverse construction.
>
> > [!note]- Full proof
> > Since $N$ is a closed neighborhood of $x$, $x$ has an open neighborhood inside $N$, so $x \in \mathrm{int}(N) = U$, which is open by definition of interior.
> >
> > $W = X \setminus N$ is open (complement of closed).
> >
> > $C \subseteq W$: $N \cap C = \emptyset$ means $C \subseteq X \setminus N = W$.
> >
> > $U \cap W = \mathrm{int}(N) \cap (X \setminus N) \subseteq N \cap (X \setminus N) = \emptyset$.

---

# Formal Proof

> [!note]- Complete formal proof
>
> Let $X$ be Hausdorff.
>
> **($\Rightarrow$) Regular implies closed neighborhoods form a basis.** Let $x \in V$ with $V$ open. Set $C = X \setminus V$, which is closed and disjoint from $x$. By regularity, there are disjoint opens $U \ni x$ and $W \supseteq C$. Apply Lemma 1: $N = X \setminus W$ is a closed neighborhood of $x$. And $N = X \setminus W \subseteq X \setminus C = V$, since $W \supseteq C$. So $N$ is a closed neighborhood of $x$ with $N \subseteq V$. As $V$ was arbitrary, the closed neighborhoods of $x$ form a neighborhood basis.
>
> **($\Leftarrow$) Closed neighborhoods form a basis implies regular.** Let $x \notin C$ with $C \subseteq X$ closed. Then $V = X \setminus C$ is open and $x \in V$. By the basis assumption, there is a closed neighborhood $N$ of $x$ with $N \subseteq V$; equivalently $N \cap C = \emptyset$. Apply Lemma 2: $U = \mathrm{int}(N)$ and $W = X \setminus N$ are disjoint opens with $x \in U$ and $C \subseteq W$. Hence $X$ is regular (recall $X$ is already $T_1$ by being Hausdorff). $\blacksquare$
>
> **Corollary (subspaces of regular are regular).** Let $A \subseteq X$ with $X$ regular, and take the subspace topology on $A$. For any $a \in A$ and any subspace-open $V_A \ni a$, write $V_A = V \cap A$ with $V$ open in $X$. By the above, there is a closed-in-$X$ neighborhood $N$ of $a$ with $N \subseteq V$. Then $N \cap A$ is closed in $A$ (subspace topology), and it is a neighborhood of $a$ in $A$ (containing the open-in-$A$ set $\mathrm{int}(N) \cap A \ni a$), and $N \cap A \subseteq V \cap A = V_A$. So closed-in-$A$ neighborhoods of $a$ form a neighborhood basis, and by the equivalence, $A$ is regular. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Closed support of a continuous function.** In a regular space, if $f$ is continuous and $K = \{x : f(x) \geq \epsilon\}$ is bounded away from zero on an open neighborhood, the closed neighborhood basis lets one find a closed $N$ with $K \subseteq N$ and $N$ strictly inside the support. This is the precursor of the partition-of-unity construction on regular spaces in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]. The application is nonobvious because the closed-neighborhood basis lets you *upgrade* a non-closed-support function to a closed-support approximation.

**Embedding theorems via regular plus second-countable.** Urysohn's metrization theorem requires regular plus second-countable plus Hausdorff, and the proof embeds $X$ into the Hilbert cube $[0, 1]^{\mathbb{N}}$ via countably many continuous separating functions. The construction of these functions uses closed neighborhoods as basic building blocks — each function vanishes outside a closed neighborhood of a basis element and is positive inside. The closed-neighborhood basis is the *combinatorial input* to the metrization machinery.

**Local compactness via closed neighborhoods.** A Hausdorff space is locally compact if and only if every point has a *compact* closed neighborhood. The basis form of regularity is needed to extract *which* closed neighborhood to use — given any open $V \ni x$, one wants a compact closed $N \subseteq V$, and the basis argument lets one shrink and shrink until compactness is captured. This is the technical lemma underlying every "extend by zero" or "cutoff function" argument in distribution theory.

---

# Bridges

- **[[Def - Separation Axioms]]** — regularity is $T_3$. This theorem gives its operational form, the form actually used in proofs.

- **[[Thm - Metric Spaces are Normal]]** — every metric space is normal, hence regular, hence (by this theorem) has the closed-neighborhood basis property. The metric-space proof of this is the elementary observation $\overline{B_{r/2}(x)} \subseteq B_r(x)$, which is the closed-neighborhood basis made very explicit.

- **Subspaces of regular spaces are regular** — a clean inheritance result that this theorem makes immediate (intersect a closed-neighborhood basis in $X$ with $A$).

- **Urysohn's lemma** — for *normal* spaces (the next axiom up), one gets a continuous function separating disjoint closed sets, generalizing the metric-space proof in [[Thm - Metric Spaces are Normal]]. The closed-neighborhood basis is the step on the way: shrink-and-cover constructions use this theorem at each iteration.

---

# Unlocked by This

> [!tip] Urysohn's Lemma *(from Topology III)*
> In a **normal** space (one axiom up from regular), any two disjoint closed sets can be separated by a continuous function — i.e., there is $f : X \to [0, 1]$ continuous with $f = 0$ on one, $f = 1$ on the other. The proof iteratively constructs a sequence of open sets between the two closed sets using exactly the basis-shrinking argument from this theorem (applied to closed-set separation, not just point separation).

> [!tip] Urysohn's Metrization Theorem *(from Topology III)*
> A topological space is metrizable (with separable metric) if and only if it is **regular, Hausdorff, and second-countable**. The proof builds a metric from countably many separating continuous functions, each of which exists by Urysohn's lemma — which in turn uses the closed-neighborhood basis form of regularity (this theorem).

> [!tip] Tietze Extension Theorem *(from Topology III)*
> A continuous function on a closed subspace of a normal space extends continuously to the whole space. The proof builds the extension as a uniform limit of approximations, each constructed using Urysohn's lemma — and ultimately the closed-neighborhood basis form of regularity.
