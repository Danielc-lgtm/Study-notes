---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Separation Axioms"
  - "Def - Topological Space"
tags: [analysis, topology, separation-axioms, counterexample]
---

# Problem Statement

The **cofinite topology** on an infinite set $X$ has as its open sets $\emptyset$ together with all sets whose complement in $X$ is finite. Take $X = \mathbb{N}$ (or any other countably infinite set, or $\mathbb{R}$) equipped with this topology.

**(a)** Verify that the cofinite topology is indeed a topology.

**(b)** Show that $(\mathbb{N}, \text{cofinite})$ is $T_1$: every singleton is closed.

**(c)** Show that $(\mathbb{N}, \text{cofinite})$ is *not* Hausdorff: any two nonempty open sets intersect.

**(d)** Show concretely that the failure of Hausdorff is visible at the level of sequences: the sequence $x_n = n$ converges to *every* point $k \in \mathbb{N}$ in the cofinite topology.

**Recall:**

The separation axioms used here:

![[Def - Separation Axioms#The Definition]]

A topology on a set $X$ is a collection $\tau \subseteq \mathcal{P}(X)$ satisfying:
- $\emptyset, X \in \tau$;
- arbitrary unions of members of $\tau$ are in $\tau$;
- finite intersections of members of $\tau$ are in $\tau$.

A sequence $\{x_n\}$ in a topological space $X$ **converges to** $x \in X$ if for every open $U \ni x$ there is $N$ with $x_n \in U$ for all $n \geq N$.

A set $A$ is **cofinite** in $X$ if $X \setminus A$ is finite. The cofinite open sets are $\emptyset$ together with cofinite subsets of $X$.

---

# Convergent Strategy

**Problem class.** Construction of a *named counterexample* in the separation hierarchy: a space showing that $T_1$ is strictly weaker than $T_2$. The cofinite topology is the canonical example, simple enough to verify by hand at each level.

**Assumption pattern.** Each of the four parts has its own pattern: (a) is verification of axioms; (b) and (c) are direct from cofinite-versus-finite complement counts; (d) is the demonstration that *every* point of $\mathbb{N}$ is a limit of $x_n = n$ — the most extreme possible failure of Hausdorff at the sequence level.

**Theorem routing.** No prior theorems beyond the definitions. The single underlying combinatorial fact is: the union of two finite sets is finite, hence the intersection of two cofinite sets is cofinite, hence nonempty when the ambient set is infinite. This drives both (a) and (c).

**Key decision point.** The conceptual content is in (d): even sequences notice the failure of Hausdorff. The point $k$ has open neighbourhoods which are all cofinite, so each contains all but finitely many of the $x_n = n$ — hence $x_n$ is eventually in every neighbourhood of every point. Non-Hausdorff is literally "limits are not unique", and this example demonstrates it maximally.

---

# Legal Operations Used

This solution deploys the following legal operations from the [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness#Legal Operations|topic page's Legal Operations]]:

1. **Reduce a Hausdorff statement to nets (or sequences) having unique limits.** The contrapositive: a sequence with multiple limits demonstrates non-Hausdorff. This converts the abstract definition into a concrete check.

2. **Take complements to convert between open/closed conditions.** The cofinite topology is most cleanly described in terms of closed sets (finite sets), and the disjoint-opens condition for Hausdorff becomes "two cofinite sets are disjoint", which fails immediately by finite-union counting.

3. **Use cardinality (finite vs. infinite) as a discriminator.** When the ambient space is infinite, every cofinite subset is infinite. This is what kills Hausdorff: disjoint cofinite sets would require their union to be all of $X$ with finite complement, but it must also equal $X$ with the *sum* of finite complements removed — yielding a non-cofinite set, contradiction.

---

# Hints

> [!note]- Hint 1
> For (a) and (c): the key combinatorial fact is that the union of finitely many finite sets is finite. So the intersection of finitely many cofinite sets is cofinite (take complements). Hence the cofinite open sets are closed under finite intersection, and any two nonempty opens have *cofinite* complement of union, but their intersection has *finite-union* complement — also finite, hence cofinite, hence nonempty.

> [!note]- Hint 2
> For (b): $\{k\}$ is closed if and only if $\mathbb{N} \setminus \{k\}$ is open. The complement of $\{k\}$ has finite complement ($\{k\}$ itself, one element), so it is cofinite, so it is open. Hence $\{k\}$ is closed. This works for any singleton, giving $T_1$.

> [!note]- Hint 3
> For (d): take any $k \in \mathbb{N}$. A neighbourhood of $k$ in the cofinite topology is a cofinite set $U \ni k$. The complement $\mathbb{N} \setminus U$ is finite, so $x_n = n \in U$ for all $n$ except finitely many — eventually $x_n \in U$. Hence $x_n \to k$.

---

# Solution

The cofinite topology trades the metric intuition of "balls of radius $\varepsilon$" for the combinatorial intuition of "everything except finitely many things". Each separation axiom is then a question about how finite sets are structured, and the answers reveal the precise level at which the cofinite topology sits in the separation hierarchy.

**Step 1: Part (a) — verify the cofinite topology is a topology.**

The cofinite collection $\tau = \{\emptyset\} \cup \{U \subseteq \mathbb{N} : \mathbb{N} \setminus U \text{ is finite}\}$ satisfies the three axioms.

> [!note]- Derivation
> *$\emptyset, \mathbb{N} \in \tau$.* $\emptyset \in \tau$ by definition. $\mathbb{N} \in \tau$ because $\mathbb{N} \setminus \mathbb{N} = \emptyset$ is finite, so $\mathbb{N}$ is cofinite.
>
> *Closure under arbitrary unions.* If $\{U_\alpha\}_{\alpha \in I} \subseteq \tau$ with each $U_\alpha$ cofinite (or $\emptyset$, which contributes nothing), then $\mathbb{N} \setminus \bigcup_\alpha U_\alpha = \bigcap_\alpha (\mathbb{N} \setminus U_\alpha) \subseteq \mathbb{N} \setminus U_{\alpha_0}$ for any fixed $\alpha_0$ with $U_{\alpha_0}$ cofinite. Hence the complement of the union is contained in a finite set, hence is itself finite, hence the union is cofinite. (If all $U_\alpha = \emptyset$, the union is $\emptyset \in \tau$.)
>
> *Closure under finite intersections.* If $U_1, \ldots, U_k \in \tau$ all nonempty (otherwise the intersection is $\emptyset \in \tau$), then $\mathbb{N} \setminus \bigcap_i U_i = \bigcup_i (\mathbb{N} \setminus U_i)$, a finite union of finite sets, hence finite. So the intersection is cofinite.

**Step 2: Part (b) — singletons are closed ($T_1$).**

For any $k \in \mathbb{N}$, $\mathbb{N} \setminus \{k\}$ has finite complement $\{k\}$, hence is open. So $\{k\}$ is closed.

> [!note]- Derivation
> Pick $k \in \mathbb{N}$. The set $U = \mathbb{N} \setminus \{k\}$ has complement $\mathbb{N} \setminus U = \{k\}$, which has cardinality $1$, hence is finite. By definition of the cofinite topology, $U$ is open. So $\{k\} = \mathbb{N} \setminus U$ is closed.
>
> For the $T_1$ axiom on points $k \neq \ell$: the open set $\mathbb{N} \setminus \{\ell\}$ contains $k$ but not $\ell$, and the open set $\mathbb{N} \setminus \{k\}$ contains $\ell$ but not $k$. Both are cofinite, both are open. So $\mathbb{N}$ is $T_1$.

**Step 3: Part (c) — Hausdorff fails.**

Any two nonempty open sets $U, V$ in $(\mathbb{N}, \text{cofinite})$ have $U \cap V \neq \emptyset$, so no two distinct points can be separated by disjoint opens.

> [!note]- Derivation
> Take nonempty open $U, V \subseteq \mathbb{N}$ in the cofinite topology. Their complements $\mathbb{N} \setminus U$ and $\mathbb{N} \setminus V$ are finite. The complement of their intersection is
> $$\mathbb{N} \setminus (U \cap V) = (\mathbb{N} \setminus U) \cup (\mathbb{N} \setminus V),$$
> a union of two finite sets, hence finite. Since $\mathbb{N}$ is infinite and $\mathbb{N} \setminus (U \cap V)$ is finite, $U \cap V$ is infinite and in particular nonempty.
>
> So any two nonempty opens intersect. In particular, for distinct $k, \ell \in \mathbb{N}$, no disjoint pair of open neighbourhoods $U \ni k, V \ni \ell$ can exist (both opens are nonempty, hence intersect). So $\mathbb{N}$ is not Hausdorff.

**Step 4: Part (d) — every sequence converges to every point.**

The sequence $x_n = n$ converges to every $k \in \mathbb{N}$ in the cofinite topology.

> [!note]- Derivation
> Fix $k \in \mathbb{N}$ and an open neighbourhood $U \ni k$. By definition of the cofinite topology, $\mathbb{N} \setminus U$ is finite. Let $F = \mathbb{N} \setminus U$ and let $N = \max F + 1$ (or $N = 0$ if $F = \emptyset$). For $n \geq N$, $n \notin F$ (because $n > \max F$), so $n \in U$. Hence $x_n = n \in U$ for all $n \geq N$, i.e., $x_n$ is eventually in $U$. This shows $x_n \to k$.
>
> Since $k \in \mathbb{N}$ was arbitrary, $x_n$ converges to every point of $\mathbb{N}$. (Indeed, *any* sequence of distinct points in $(\mathbb{N}, \text{cofinite})$ converges to every point: the same finite-tail argument works as long as the sequence eventually leaves every finite set, which it does whenever its terms are eventually distinct.)

> [!note]- Complete formal solution
> **(a) Topology axioms.** $\emptyset, \mathbb{N} \in \tau$ by definition. For a union of cofinite sets, the complement is contained in any single complement, hence finite. For a finite intersection of cofinite sets, the complement is the (finite) union of (finite) complements, hence finite. So $\tau$ is a topology.
>
> **(b) $T_1$.** Each singleton $\{k\}$ has cofinite complement $\mathbb{N} \setminus \{k\}$, hence is closed. So singletons are closed and $\mathbb{N}$ is $T_1$.
>
> **(c) Not Hausdorff.** Two nonempty opens $U, V$ in the cofinite topology have finite complements; the complement of their intersection $\mathbb{N} \setminus (U \cap V) = (\mathbb{N}\setminus U) \cup (\mathbb{N}\setminus V)$ is finite, so $U \cap V$ has cofinite complement and is therefore infinite, hence nonempty. So no two nonempty opens are disjoint, ruling out separating any two distinct points by disjoint opens.
>
> **(d) Sequential pathology.** For any $k \in \mathbb{N}$ and any open $U \ni k$, $\mathbb{N} \setminus U$ is finite; for $n > \max(\mathbb{N}\setminus U)$, $x_n = n \in U$. So $x_n \to k$ for every $k \in \mathbb{N}$. $\blacksquare$

---

# Key Takeaways

**The cofinite topology is the universal $T_1$-but-not-Hausdorff example because the separation axioms cleanly stratify by what the closed sets look like.** In the cofinite topology the closed sets are precisely the finite sets together with $\mathbb{N}$ itself. This makes singletons closed (giving $T_1$), but disjoint pairs of cofinite sets cannot exist on an infinite ambient — there is simply not enough room. The pattern to remember: each separation axiom imposes a *combinatorial restriction* on the closed sets (and dually, on the opens), and the cofinite topology is what you get when the closed sets are as small as possible while still containing every singleton. Any time you want a $T_1$-not-Hausdorff example, the cofinite topology is the default.

**Sequences fail to have unique limits in a non-Hausdorff space — this is the *operational* content of non-Hausdorff.** The abstract definition says "disjoint opens can't separate points", but the trigger for *using* non-Hausdorff is "a sequence (or net) has more than one limit". The implication runs both ways for nets: by [[Thm - Hausdorff Iff Unique Net Limits]], a space is Hausdorff if and only if every convergent net has a unique limit. For sequences alone the implication is one-way (Hausdorff $\Rightarrow$ unique sequential limits), with the converse holding only under first-countability. The cofinite topology on $\mathbb{N}$ is first-countable in fact (every singleton's cofinite neighbourhoods include the basis $\{\mathbb{N}\setminus F_n\}$ for an enumeration of finite sets), and the example here is even sequential-level: $x_n = n$ converges everywhere.

**Cofinite topology arises naturally as the Zariski topology on $\mathbb{A}^1$ over an infinite field — non-Hausdorff is the *normal* state of affairs in algebraic geometry.** In algebraic geometry, the affine line $\mathbb{A}^1_k = \operatorname{Spec} k[x]$ (for $k$ an infinite field) has closed points $=$ maximal ideals $(x - a) \cong k$, and the Zariski-closed sets are the zero sets of polynomials, which are the finite sets together with the whole space. So the Zariski topology on $\mathbb{A}^1$ is *exactly* the cofinite topology on $k$ (modulo the generic point). The non-Hausdorffness of the Zariski topology is a feature, not a bug — it reflects the fact that polynomial functions cannot distinguish "nearby" points without measuring them at a positive distance. The trigger: whenever you see Zariski topology and infinite ground field, expect cofinite-style non-Hausdorff phenomena.

**The construction "every neighbourhood of every point is cofinite, hence contains all but finitely many sequence terms" generalizes to nets and is the source of every "net converges to many limits" example.** The cofinite topology is the simplest such, but the same pattern generates examples in much larger settings: a discrete net indexed by finite subsets of an infinite directed set, evaluated by picking elements in the complement of the indexing set, will converge to every point of a non-Hausdorff topology. See [[Ex - A net that converges to two points]] for a directed-set version. The take-home: producing multiple-limit examples is mechanical once you understand "every neighbourhood is large" — the failure of Hausdorff is equivalent to the existence of such neighbourhoods around different points that always overlap.
