---
type: exercise
subject: category-theory
difficulty: "⭐"
prereqs:
  - "Def - Limit and Colimit"
  - "Def - Product and Coproduct"
  - "Def - Category"
tags: [category-theory, foundations]
---

# Problem Statement

Let $(P, \le)$ be a [[Def - Category|poset]], regarded as a category with one morphism $a \to b$ exactly when $a \le b$. Show that the [[Def - Limit and Colimit|limit]] of a family $(a_i)_{i \in I}$ in $P$ is its **greatest lower bound** (infimum / meet) $\bigwedge_i a_i$, and the colimit is its **least upper bound** (supremum / join) $\bigvee_i a_i$. In particular the binary [[Def - Product and Coproduct|product]] is the meet $a \wedge b$ and the coproduct is the join $a \vee b$. Deduce that $P$ is a [[Def - Complete and Cocomplete Category|complete category]] if and only if it is a complete lattice.

**Recall:**

A **poset as a category** has objects the elements of $P$ and a single morphism $a \to b$ iff $a \le b$ (so there is at most one morphism between any two objects). Composition is transitivity; identities are reflexivity.

A **limit** of a diagram $D : J \to \mathcal{C}$ is the terminal [[Def - Cone and Cocone|cone]]; a cone with apex $X$ is a family $X \to D_j$ commuting with the diagram.

---

# Convergent Strategy

**Problem class:** This is a "decode a universal property in a thin category" problem — interpreting limits and colimits in a poset, where the at-most-one-morphism structure trivialises commutativity and turns universal properties into order inequalities. The routine: write the cone/universal-property conditions, then read each "there exists a unique morphism" as an inequality.

**Assumption pattern:** The decisive feature is that $P$ is **thin** (at most one morphism between any two objects). This means every diagram automatically commutes, every cone is just a lower bound, and "unique morphism" is free — existence of a morphism *is* the inequality. Recognising "thin $\Rightarrow$ universal properties become order relations" is the whole unlock.

**Theorem routing:** A [[Def - Cone and Cocone|cone]] over $(a_i)$ with apex $x$ is a morphism $x \to a_i$ for each $i$, i.e. $x \le a_i$ for all $i$ — a lower bound. The terminal cone is the *greatest* lower bound, the meet. Dually, a cocone is an upper bound and the colimit is the least upper bound, the join. Completeness ("all small limits") becomes "all subsets have infima", i.e. a complete lattice.

**Key decision point:** The subtle point is why uniqueness is automatic: in a thin category there is *at most one* morphism between any two objects, so the "unique" in the universal property costs nothing, and the limit is determined purely by the *existence* of comparison morphisms — which is the order relation. The temptation to look for a "canonical" comparison map is misplaced; there is only ever one candidate.

---

# Legal Operations Used

1. **Decode a cone as an order relation (from the topic page: a cone is a compatible family of maps).** In a thin category a cone over $(a_i)$ with apex $x$ is exactly the conjunction of inequalities $x \le a_i$.

2. **Read terminality as "greatest" (operation: limit $=$ terminal cone).** The terminal lower bound is the greatest lower bound, since "every other lower bound maps to it" means "every other lower bound is $\le$ it".

3. **Translate completeness into lattice completeness (operation: all small limits exist).** "$P$ has all small limits" unpacks to "every subset has an infimum", the definition of a complete lattice.

---

# Hints

> [!note]- Hint 1
> In a poset-as-category there is at most one arrow between any two objects, so every commutativity condition is automatic and "unique map" is free. A cone over $(a_i)$ with apex $x$ is just: $x \le a_i$ for all $i$.

> [!note]- Hint 2
> The limit is the terminal cone. A terminal lower bound is a lower bound $\ell$ such that every lower bound $x$ has $x \le \ell$ — that is the greatest lower bound, $\bigwedge a_i$.

> [!note]- Hint 3
> Dualize for colimits: a cocone is an upper bound, and the initial upper bound is the least upper bound $\bigvee a_i$.

> [!note]- Hint 4
> "$P$ complete as a category" means every small diagram has a limit, i.e. every subset has a meet. A poset with all meets (equivalently all joins) is a complete lattice.

---

# Solution

The plan: use thinness to reduce cones to lower bounds, read the terminal cone as the greatest lower bound, dualize to joins, and unpack completeness as the complete-lattice condition.

**Step 1: Cones over a family are lower bounds.**

> [!note]- Derivation
> Let $D : J \to P$ pick out the family $(a_i)_{i \in I}$ (the index category is discrete, or more generally any $J$ — commutativity is automatic). A [[Def - Cone and Cocone|cone]] with apex $x$ is a family of morphisms $x \to a_i$, one per $i$. In the poset category a morphism $x \to a_i$ exists iff $x \le a_i$, and there is at most one. So a cone with apex $x$ is precisely the statement that $x$ is a *lower bound*: $x \le a_i$ for all $i$. The commutativity conditions hold automatically because $P$ is thin.

**Step 2: The limit is the greatest lower bound.**

> [!note]- Derivation
> The [[Def - Limit and Colimit|limit]] is the terminal cone: a lower bound $\ell$ such that every cone (lower bound) $x$ admits a unique morphism $x \to \ell$, i.e. $x \le \ell$. So $\ell$ is a lower bound that every lower bound is $\le$ — the *greatest* lower bound $\ell = \bigwedge_i a_i$. Uniqueness of the comparison is automatic (thinness). For two elements this is the [[Def - Product and Coproduct|product]] $a \wedge b$.

**Step 3: The colimit is the least upper bound.**

> [!note]- Derivation
> Dually, a [[Def - Cone and Cocone|cocone]] under $(a_i)$ with nadir $x$ is a family $a_i \to x$, i.e. $a_i \le x$ for all $i$ — an upper bound. The colimit is the initial cocone: an upper bound $u$ with $u \le x$ for every upper bound $x$, i.e. the *least* upper bound $\bigvee_i a_i$. For two elements this is the coproduct $a \vee b$.

**Step 4: Completeness as a category equals being a complete lattice.**

> [!note]- Derivation
> $P$ is [[Def - Complete and Cocomplete Category|complete]] as a category iff every small diagram has a limit, iff every (small) family of elements has a greatest lower bound, iff every subset of $P$ has an infimum — which is the definition of a **complete lattice**. (A poset in which every subset has an infimum automatically has all suprema too: $\bigvee S = \bigwedge\{u : u \ge s\ \forall s \in S\}$, so complete-as-a-limit-category coincides with complete-as-a-colimit-category, both equal to "complete lattice".)

> [!note]- Complete formal solution
> Regard $(P, \le)$ as a thin category. For a family $(a_i)_{i\in I}$, a [[Def - Cone and Cocone|cone]] with apex $x$ is a family of morphisms $x \to a_i$, equivalently $x \le a_i$ for all $i$ — a lower bound — with all commutativity automatic by thinness. The [[Def - Limit and Colimit|limit]] is the terminal cone, i.e. a lower bound $\ell$ with $x \le \ell$ for every lower bound $x$: the greatest lower bound $\bigwedge_i a_i$, with uniqueness free. Binary case: the [[Def - Product and Coproduct|product]] is $a \wedge b$. Dually a cocone is an upper bound and the colimit is the least upper bound $\bigvee_i a_i$, with the coproduct $a \vee b$. Hence $P$ is complete as a category iff every subset has an infimum, iff $P$ is a complete lattice (equivalently every subset has a supremum). $\blacksquare$

---

# Key Takeaways

**In a thin category, universal properties degenerate into order relations, and limits become meets.** The reusable insight is that when there is at most one morphism between any two objects, every commutativity condition is vacuous and every "unique morphism" is free, so a [[Def - Cone and Cocone|cone]] is just a lower bound and the [[Def - Limit and Colimit|limit]] is the greatest lower bound. This is the cleanest illustration that limits generalise infima and colimits generalise suprema — the order-theoretic notions are the thin-category shadow of the categorical ones. The trigger: whenever a category is a preorder (thin), translate all categorical questions into order-theoretic ones, because the morphism data carries no information beyond the relation.

**Product = meet, coproduct = join — the order-theoretic dictionary makes the duality concrete.** Seeing the product as the greatest lower bound and the coproduct as the least upper bound is the most memorable instance of the product/coproduct duality, and it grounds the abstract definitions in the familiar lattice operations. The diagnostic value is bidirectional: lattice facts (distributivity, modularity, completeness) become statements about limits and colimits, and conversely categorical theorems specialise to lattice theorems — for example "[[Thm - Right Adjoints Preserve Limits|right adjoints preserve limits]]" becomes "a Galois connection's upper adjoint preserves meets", which is the lattice form of adjunction used throughout order theory and domain theory.

**Categorical completeness = lattice completeness, and the limit/colimit completeness coincide here.** That $P$ is a [[Def - Complete and Cocomplete Category|complete category]] exactly when it is a complete lattice, and that completeness for limits automatically gives completeness for colimits (via $\bigvee S = \bigwedge \{\text{upper bounds}\}$), is a special feature of posets worth remembering: in general a category can be complete without being cocomplete, but a complete lattice is automatically a "complete and cocomplete" thin category. The transferable principle is that the existence of all infima forces all suprema in the order setting — a phenomenon that reappears for [[Thm - Products and Equalizers Give All Limits|complete categories]] only under extra hypotheses (e.g. via the adjoint functor theorem), so the poset case is the clean prototype where the two completeness notions collapse into one.
