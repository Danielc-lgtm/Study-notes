---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Vector Space"
  - "Def - Subspace"
tags: [algebra, linear-algebra]
---

# Problem Statement

Let $V$ be a vector space over a field $\mathbb{F}$, and let $\{V_\alpha\}_{\alpha \in A}$ be an arbitrary (possibly infinite) family of subspaces of $V$. Show that the intersection

$$\bigcap_{\alpha \in A} V_\alpha = \{v \in V : v \in V_\alpha \text{ for every } \alpha \in A\}$$

is a subspace of $V$.

The special case of two subspaces $V_1, V_2$ is LADR Exercise 1C.10; the general case is LADR Exercise 1C.11.

**Recall:**

A [[Def - Subspace|subspace]] is a non-empty subset closed under addition and scalar multiplication, equivalently satisfying:

![[Def - Subspace#The Definition]]

The intersection of a family of sets is the set of elements belonging to *every* set in the family.

---

# Convergent Strategy

**Problem class:** This is a **closure-of-operations** problem: showing that a particular set-theoretic operation (intersection) preserves the subspace property. Such problems are ubiquitous in algebra — any time you want to show "the operation of $X$ gives back $X$", you check the defining conditions of $X$ on the output.

**Assumption pattern:** Each $V_\alpha$ is a subspace, so each contains $0$, each is closed under addition, each is closed under scalar multiplication. We are not told the family is finite, so the proof must work for arbitrary intersections.

**Theorem routing:** The route is direct — apply the [[Def - Subspace|subspace criterion]] to $\bigcap V_\alpha$. Containment of $0$ comes from the fact that every $V_\alpha$ contains $0$; closure under addition and scalar multiplication come from the corresponding closure of each $V_\alpha$ together with the characterization "in the intersection iff in every $V_\alpha$".

**Key decision point:** The non-obvious choice is that the proof works for *arbitrary* index sets, including uncountable ones, with no extra effort. The reason is that the subspace conditions are all *universally quantified* over the family: containment of $0$ in every $V_\alpha$ implies containment in the intersection, and closure under operations in every $V_\alpha$ implies closure in the intersection. Universal quantifiers cooperate well with intersection. The same proof, with "subspace" replaced by "subgroup" or "submodule" or "closed set", works in many other settings; the structural reason is that subspaces are defined by *Horn clauses* (universally-quantified implications), which are preserved under arbitrary intersection.

---

# Legal Operations Used

1. **Verify a subset is a subspace by checking the three subspace conditions.** From the topic page's legal operations. Applied here to the intersection $\bigcap V_\alpha$.

2. **Use the characterization "$v \in \bigcap V_\alpha$ iff $v \in V_\alpha$ for every $\alpha$".** A set-theoretic identity that is the heart of every intersection argument: to verify $v$ is in the intersection, verify it is in every member of the family.

3. **Quantify universally over the index set.** Closure conditions for each $V_\alpha$ are statements "for all $u, w \in V_\alpha$, $u + w \in V_\alpha$". To show closure for the intersection, take $u, w$ in the intersection, and exploit closure of every individual $V_\alpha$ separately.

---

# Hints

> [!note]- Hint 1
> Apply the subspace criterion directly to $\bigcap V_\alpha$. Verify the three conditions: contains $0$, closed under addition, closed under scalar multiplication.

> [!note]- Hint 2
> For "contains $0$": each $V_\alpha$ contains $0$, so $0$ lies in every $V_\alpha$, hence in the intersection.

> [!note]- Hint 3
> For "closed under addition": take $u, w$ in the intersection. By definition $u, w \in V_\alpha$ for every $\alpha$. By closure of each $V_\alpha$ under addition, $u + w \in V_\alpha$ for every $\alpha$. So $u + w \in \bigcap V_\alpha$.

> [!note]- Hint 4
> The infinite-index case is no harder than the finite case: at no point do we need to do anything that depends on the size of the family. The proof is purely formal.

---

# Solution

The proof is a direct application of the subspace criterion: verify $0 \in \bigcap V_\alpha$, then closure under addition, then closure under scalar multiplication, in each case using that the corresponding property holds for every $V_\alpha$.

**Step 1: $0 \in \bigcap V_\alpha$.**

> [!note]- Derivation
> For each $\alpha \in A$, $V_\alpha$ is a subspace, so $0 \in V_\alpha$. Hence $0$ lies in every $V_\alpha$, which is by definition the condition for $0 \in \bigcap V_\alpha$.

**Step 2: $\bigcap V_\alpha$ is closed under addition.**

> [!note]- Derivation
> Let $u, w \in \bigcap V_\alpha$. By definition of intersection, $u \in V_\alpha$ and $w \in V_\alpha$ for every $\alpha \in A$. Each $V_\alpha$ is closed under addition, so $u + w \in V_\alpha$ for every $\alpha$. Hence $u + w \in \bigcap V_\alpha$.

**Step 3: $\bigcap V_\alpha$ is closed under scalar multiplication.**

> [!note]- Derivation
> Let $\lambda \in \mathbb{F}$ and $u \in \bigcap V_\alpha$. Then $u \in V_\alpha$ for every $\alpha$. Each $V_\alpha$ is closed under scalar multiplication, so $\lambda u \in V_\alpha$ for every $\alpha$. Hence $\lambda u \in \bigcap V_\alpha$.

> [!note]- Complete formal solution
> **Claim.** For any family $\{V_\alpha\}_{\alpha \in A}$ of subspaces of $V$, the intersection $\bigcap_\alpha V_\alpha$ is a subspace of $V$.
>
> *Proof.* We verify the three conditions of the [[Def - Subspace|subspace criterion]].
>
> *Zero.* Each $V_\alpha$ is a subspace, so contains $0$. Hence $0 \in V_\alpha$ for every $\alpha \in A$, i.e. $0 \in \bigcap_\alpha V_\alpha$.
>
> *Closure under addition.* Let $u, w \in \bigcap_\alpha V_\alpha$. Then for every $\alpha$, $u, w \in V_\alpha$. Each $V_\alpha$ is closed under addition, so $u + w \in V_\alpha$ for every $\alpha$. Hence $u + w \in \bigcap_\alpha V_\alpha$.
>
> *Closure under scalar multiplication.* Let $\lambda \in \mathbb{F}$ and $u \in \bigcap_\alpha V_\alpha$. Then $u \in V_\alpha$ for every $\alpha$. Each $V_\alpha$ is closed under scalar multiplication, so $\lambda u \in V_\alpha$ for every $\alpha$. Hence $\lambda u \in \bigcap_\alpha V_\alpha$.
>
> All three conditions hold, so $\bigcap_\alpha V_\alpha$ is a subspace of $V$. $\blacksquare$

---

# Key Takeaways

**Subspaces are closed under arbitrary intersection, but not under unions or sums.** The result here is one half of a structural fact about the subspace lattice: arbitrary intersections of subspaces are subspaces, but the union of two subspaces is rarely a subspace (see [[Ex - Union of subspaces is a subspace iff one contains the other]]). The asymmetry is because subspaces are defined by *universally-quantified closure conditions* ("for all $u, w \in U$, $u + w \in U$"), which intersection respects: if every $V_\alpha$ satisfies the condition, so does the intersection. Union, on the other hand, is an existence operation: $u \in V_1 \cup V_2$ means $u$ is in *some* $V_i$, and there is no reason a combination $u_1 + u_2$ of elements from different pieces should land in the union. The lesson is general: any structure defined by Horn clauses (universally-quantified implications) is closed under arbitrary intersection. Topologies (closed sets), $\sigma$-algebras, subrings, subgroups, ideals — all are closed under arbitrary intersection, by exactly the same argument as here.

**Intersection gives the lattice-theoretic meet of subspaces, dual to the sum giving the join.** The intersection $\bigcap V_\alpha$ is the meet of the subspaces in the lattice $\operatorname{Sub}(V)$, while the sum $\sum V_\alpha$ is the join (see [[Ex - Sum of two subspaces is the smallest containing both]]). Together they give the lattice structure: every collection of subspaces has both a largest common lower bound (intersection) and a smallest common upper bound (sum). The fact that intersection is set-theoretic (just the intersection of sets) while join is sum (not union) is a recurring asymmetry in algebra. In set theory the meet and join are intersection and union, both set-theoretic; in algebraic structures the join often must be enriched to include all the combinations the structure can form. This asymmetry is the source of much of the structural richness — and challenge — of the subspace lattice.

**The proof template "verify each property using the corresponding property of each piece" is universal.** Almost every "intersection preserves $X$" proof has the same form: take an arbitrary element of the intersection, observe that it lies in every piece, exploit the $X$-property of every piece, conclude the $X$-property of the intersection. This template works whenever $X$ is defined by universal quantification over its elements. Recognizing this pattern lets you write closure-of-intersection proofs almost mechanically: identify the defining conditions of $X$, observe that each is universally quantified over $X$, and let the universal quantifier do the work. The same template proves: the intersection of subgroups is a subgroup, of submodules is a submodule, of closed sets is closed, of $\sigma$-algebras is a $\sigma$-algebra. In each case the structure of the proof is identical; only the specific closure conditions change.

**Closure under intersection is what licenses the "smallest subspace containing $S$" construction.** The **span** of a set $S \subseteq V$ is defined as the intersection of all subspaces of $V$ containing $S$. This makes sense — produces an actual subspace — because of the result here: an arbitrary intersection of subspaces is a subspace. The intersection is non-empty because $V$ itself is a subspace containing $S$, and it is the smallest because any other subspace containing $S$ appears in the family being intersected, hence contains the intersection. The pattern recurs throughout algebra: any "smallest $X$ containing $S$" construction is built by intersecting all $X$ containing $S$, and the construction works precisely when arbitrary intersections of $X$ are $X$. So this exercise's result is the unsung hero behind all the "generate" operations in algebra: span (subspace generated by vectors), subgroup generated by elements, ideal generated by elements, $\sigma$-algebra generated by a collection of sets.
