---
type: exercise
subject: group-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
tags: [algebra, group-theory]
---

# Problem Statement

Prove that a group is never the union of two proper [[Def - Subgroup|subgroups]]. That is, if $H$ and $K$ are [[Def - Subgroup|subgroups]] of a group $G$ and $G = H \cup K$, then $H = G$ or $K = G$.

*(This is Putnam 1969, Problem B-2.)*

**Recall:**

A **subgroup** $H \leq G$ is a subset that contains the identity, is closed under the group operation, and is closed under taking inverses:

![[Def - Subgroup#The Definition]]

A subgroup $H$ is **proper** if $H \neq G$. The **union** $H \cup K$ is the set of elements lying in $H$ or in $K$ (or both). Saying $G = H \cup K$ means every element of $G$ belongs to at least one of $H, K$.

The one closure fact the argument leans on: in a subgroup $H$, if a product $ab$ lies in $H$ and one of the factors lies in $H$, then so does the other. For instance, if $ab \in H$ and $b \in H$, then $a = (ab)b^{-1} \in H$, since $H$ is closed under inverses and products. This "two out of three" principle for the equation $a \cdot b = ab$ inside a subgroup is the engine of the proof.

The group $G$ here is **arbitrary** — finite or infinite, abelian or not. No counting and no order hypotheses are used.

---

# Convergent Strategy

**Problem class.** This is a *structural non-existence proof*: you must show a certain configuration — a group exhausted by two proper subgroups — cannot occur. The parent page's [[Group Theory I — §1.1–1.2#Problem-Solving Strategy|Problem-Solving Strategy]] notes that non-existence claims are naturally attacked by *contradiction*: assume the forbidden configuration exists and derive an impossibility.

**Assumption pattern.** Suppose, for contradiction, that $G = H \cup K$ with both $H$ and $K$ proper. "Proper" is the load-bearing word: $H \neq G$ means there is an element of $G$ *outside* $H$, and since $G = H \cup K$, that element must lie in $K$. Symmetrically there is an element outside $K$ and hence inside $H$. So the properness of each subgroup, combined with the covering hypothesis, *manufactures witnesses*: an element $a$ in $H$ but not $K$, and an element $b$ in $K$ but not $H$.

**Theorem routing.** No named theorem is invoked — the proof is pure subgroup-closure reasoning. The route is: extract the witnesses $a \in H \setminus K$ and $b \in K \setminus H$; form the product $ab$; ask which of $H, K$ contains it; show that *neither* can, using the "two out of three" closure principle in each subgroup; conclude $ab \notin H \cup K = G$, contradicting that $ab$ is an element of the group.

**Key decision point.** The non-obvious move — the entire idea of the proof — is to consider the single element $ab$, the product of one witness from each subgroup. Once you write down $ab$ and ask "is it in $H$? is it in $K$?", closure forces a "no" both times. The temptation is to look for an element constructed more elaborately, or to argue by cardinality (which fails for infinite [[Def - Group|groups]]); the elegance is that one product of two cleverly chosen elements suffices.

---

# Legal Operations Used

1. **Argue by contradiction** — assume $G = H \cup K$ with $H, K$ both proper, and aim to construct an element of $G$ lying in neither.

2. **Extract a witness from a properness hypothesis** — $H$ proper and $G = H \cup K$ together yield an element $a \in H \setminus K$; symmetrically an element $b \in K \setminus H$.

3. **Form a product and test membership via closure** — build $ab$ and apply the subgroup-closure "two out of three" principle inside $H$ and inside $K$ to show $ab$ lies in neither.

---

# Hints

> [!note]- Hint 1
> Argue by contradiction: suppose $G = H \cup K$ with both $H$ and $K$ proper. Since each is proper, each *misses* some element of $G$. Where does a missed element have to be?

> [!note]- Hint 2
> You can find $a \in H$ with $a \notin K$, and $b \in K$ with $b \notin H$. Now consider a single element built from $a$ and $b$. Try their product $ab$.

> [!note]- Hint 3
> Suppose $ab \in H$. You also know $a \in H$, so $a^{-1} \in H$, so $a^{-1}(ab) = b \in H$ — but $b \notin H$. Contradiction. Run the symmetric argument to rule out $ab \in K$.

---

# Solution

**Step 1: Set up the contradiction and extract witnesses.**

Assume $G = H \cup K$ with $H \neq G$ and $K \neq G$. Properness of each subgroup yields elements $a \in H \setminus K$ and $b \in K \setminus H$.

> [!note]- Derivation
> Suppose, for contradiction, that $G = H \cup K$ with both $H$ and $K$ proper.
>
> Since $K \neq G$, there exists an element of $G$ not in $K$. Call it $a$. Because $G = H \cup K$, the element $a$ lies in $H$ or in $K$; it is not in $K$, so $a \in H$. Thus $a \in H \setminus K$.
>
> Symmetrically, since $H \neq G$ there is an element $b \in G$ with $b \notin H$; as $b \in H \cup K$ and $b \notin H$, we get $b \in K$. Thus $b \in K \setminus H$.

**Step 2: The product $ab$ cannot lie in $H$.**

If $ab \in H$, then since $a \in H$ we could solve for $b = a^{-1}(ab) \in H$, contradicting $b \notin H$.

> [!note]- Derivation
> Suppose $ab \in H$. We have $a \in H$, and $H$ is a subgroup, so $a^{-1} \in H$. Then $H$ is closed under products, so
> $$a^{-1}(ab) = (a^{-1}a)b = eb = b \in H.$$
> But $b \in K \setminus H$, so $b \notin H$ — a contradiction. Hence $ab \notin H$.

**Step 3: The product $ab$ cannot lie in $K$.**

If $ab \in K$, then since $b \in K$ we could solve for $a = (ab)b^{-1} \in K$, contradicting $a \notin K$.

> [!note]- Derivation
> Suppose $ab \in K$. We have $b \in K$, and $K$ is a subgroup, so $b^{-1} \in K$. Then $K$ is closed under products, so
> $$(ab)b^{-1} = a(bb^{-1}) = ae = a \in K.$$
> But $a \in H \setminus K$, so $a \notin K$ — a contradiction. Hence $ab \notin K$.

**Step 4: Conclude.**

The element $ab$ lies in neither $H$ nor $K$, so $ab \notin H \cup K = G$. But $ab$ is a product of two elements of the group $G$, so $ab \in G$ — a contradiction. Therefore $H$ or $K$ equals $G$.

> [!note]- Derivation
> By Steps 2 and 3, $ab \notin H$ and $ab \notin K$, so $ab \notin H \cup K$. By assumption $H \cup K = G$, so $ab \notin G$.
>
> On the other hand, $a, b \in G$ and $G$ is closed under its operation, so $ab \in G$.
>
> These contradict one another. The assumption that $G = H \cup K$ with both subgroups proper is therefore untenable: if $G = H \cup K$, then $H = G$ or $K = G$. $\qquad\blacksquare$

> [!note]- Complete formal solution
> Let $H, K \leq G$ with $G = H \cup K$. Suppose, for contradiction, that both are proper.
>
> Since $K \ne G$, choose $a \in G \setminus K$; as $a \in H \cup K$ and $a \notin K$, we have $a \in H$. Since $H \ne G$, choose $b \in G \setminus H$; as $b \in H \cup K$ and $b \notin H$, we have $b \in K$.
>
> Consider $ab \in G$. It lies in $H \cup K$, so $ab \in H$ or $ab \in K$.
>
> If $ab \in H$: since $a \in H$, also $a^{-1} \in H$, hence $b = a^{-1}(ab) \in H$, contradicting $b \notin H$.
>
> If $ab \in K$: since $b \in K$, also $b^{-1} \in K$, hence $a = (ab)b^{-1} \in K$, contradicting $a \notin K$.
>
> Both cases are impossible, yet one must hold — contradiction. Hence $H$ and $K$ cannot both be proper: if $G = H \cup K$ then $H = G$ or $K = G$. $\qquad\blacksquare$

---

# Key Takeaways

**Two subgroups can never cover a group — but three sometimes can.** It is sharp folklore that the bound "two" in this problem is the best possible: a group *can* be the union of three proper subgroups. The minimal witness is the **Klein four-group** $V = \{e, a, b, c\}$, in which every non-identity element has order $2$. Its three proper non-trivial subgroups are $\{e, a\}$, $\{e, b\}$, $\{e, c\}$, and their union is all four elements of $V$ — the identity lies in each, and $a, b, c$ are picked up one apiece. So $V = \{e,a\} \cup \{e,b\} \cup \{e,c\}$. The contrast is instructive: with two subgroups the product $ab$ of cross-witnesses has nowhere to live, but with three subgroups it can fall into the third. The general theorem (Scorza, and later refinements) characterizes exactly which [[Def - Group|groups]] are unions of three proper subgroups — they are precisely those with a quotient isomorphic to the Klein four-group — and no group is a union of three proper subgroups unless one such configuration is forced. Knowing that "two is impossible, three is sometimes possible, and the Klein four-group is the boundary case" is the durable takeaway.

**To refute a covering hypothesis, build the one element that escapes — and the right element is a product of cross-witnesses.** The reusable technique is a template for *non-existence by explicit construction inside a contradiction*. Whenever you must show a structure cannot be covered or partitioned in some way, assume it is, harvest a *witness* from each piece (here properness hands you an element each subgroup misses), and then combine the witnesses into a single object that demonstrably belongs to none of the pieces. The decisive choice is *how* to combine them: the product $ab$ of a witness from $H$ and a witness from $K$ works because subgroup closure is a "two out of three" constraint — knowing two of $a$, $b$, $ab$ lie in a subgroup forces the third, so if $a \in H$ and $b \notin H$ then $ab \notin H$. This same "an element outside both, built from elements inside each" idea recurs in covering and partition problems throughout algebra and combinatorics; the skill is recognizing which algebraic combination of the witnesses is closed-form-forbidden from every piece at once.

**Closure is a solving tool, not just a defining axiom.** The proof never counts, never uses finiteness, and invokes no theorem — it runs entirely on the subgroup axioms, and specifically on the consequence that $ab \in H$ together with $a \in H$ forces $b \in H$. It is easy to read the subgroup definition as a static checklist (contains $e$, closed under products, closed under inverses) and forget that closure is *actively usable*: it lets you solve equations within a subgroup. The trigger to watch for is any situation where you know a product and one factor lie somewhere structured — closure then delivers the other factor for free. This "solve for the missing factor" move is exactly what the Recall section calls the two-out-of-three principle, and it is the kind of low-level operation that, once internalized, makes many subgroup arguments fall out in one line.
