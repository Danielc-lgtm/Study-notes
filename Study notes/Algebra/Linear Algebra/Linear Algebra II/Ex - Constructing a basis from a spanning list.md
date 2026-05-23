---
type: exercise
subject: linear-algebra
difficulty: "⭐"
prereqs:
  - "Def - Basis"
  - "Def - Linear Independence"
  - "Def - Linear Combination and Span"
  - "Thm - Every Spanning List Contains a Basis"
tags: [algebra, linear-algebra]
---

# Problem Statement

(Adapted from LADR 2.30, illustrative example.) Consider the list
$$(1, 2),\;(3, 6),\;(4, 7),\;(5, 9)$$
in $F^2$.

(a) Show that this list spans $F^2$.

(b) Apply [[Thm - Every Spanning List Contains a Basis|the reduction of LADR 2.30]] to identify which vectors are deleted, and exhibit the resulting basis of $F^2$.

**Recall.**

![[Thm - Every Spanning List Contains a Basis#Statement]]

The reduction algorithm proceeds left-to-right: at each step $k$, delete $v_k$ if and only if $v_k \in \operatorname{span}(v_1, \ldots, v_{k-1})$ where the span is over the *surviving* predecessors. Equivalently, delete $v_k$ if and only if $v_k$ is in the span of the previous *kept* vectors.

A list is a [[Def - Basis|basis]] iff it is linearly independent and spans (LADR Def 2.26).

---

# Convergent Strategy

**Problem class:** This is a *reduce-a-spanning-list* problem — the canonical use of [[Thm - Every Spanning List Contains a Basis|LADR 2.30]] applied concretely to vectors in $F^n$. The technique is operation 1 from the topic page, run by hand. The problem class encompasses every "find a basis of $\operatorname{span}(v_1, \ldots, v_m)$" computation, and the algorithm is mechanically Gaussian elimination on the matrix whose columns are the $v_i$.

**Assumption pattern:** We are given a concrete list of vectors and are told (or can easily verify) that the list spans the target space $F^2$. The list is *known* to have redundancy because its length exceeds $\dim F^2 = 2$. The reduction will delete $4 - 2 = 2$ vectors and produce a basis of length 2.

**Theorem routing:** The verification of spanning in (a) can be done by inspection (the first two vectors $(1, 2), (3, 6)$ are linearly dependent — $(3, 6) = 3 \cdot (1, 2)$ — but the first and third $(1, 2), (4, 7)$ are independent, so the span already includes a basis of $F^2$, hence equals $F^2$). The reduction in (b) proceeds by left-to-right testing of each vector for membership in the span of its surviving predecessors.

**Key decision point:** The non-obvious bookkeeping is to be careful about what "predecessors" means when some have been deleted — it is the *surviving* predecessors at the moment the next entry is examined, not the predecessors in the original list. Also: which vectors get deleted depends on the *order* of the list; reordering would produce a different (but equinumerous) basis.

---

# Legal Operations Used

1. **Reduce a spanning list to a basis (operation 1).** Run the algorithm of [[Thm - Every Spanning List Contains a Basis|2.30]] left-to-right.

2. **Recognise dependency by scalar multiplication.** A list of length 2 is dependent iff one vector is a scalar multiple of the other.

3. **Test membership in a 2D span by solving a linear system.** $v \in \operatorname{span}(v_1, v_2)$ iff $v = a v_1 + b v_2$ has a solution for $a, b \in F$.

---

# Hints

> [!note]- Hint 1
> Process the vectors one at a time, left-to-right. At each step, ask: is the current vector in the span of the *surviving* predecessors so far?

> [!note]- Hint 2
> $(1, 2)$ is nonzero, so it survives (its only predecessor is the empty list, with span $\{0\}$, and $(1, 2) \notin \{0\}$).

> [!note]- Hint 3
> $(3, 6) = 3 \cdot (1, 2)$, so $(3, 6) \in \operatorname{span}((1, 2))$. Hence $(3, 6)$ is deleted.

> [!note]- Hint 4
> $(4, 7)$ must be tested against $\operatorname{span}((1, 2))$ — note that $(3, 6)$ has been deleted, so it is *not* a surviving predecessor. Is $(4, 7)$ a scalar multiple of $(1, 2)$?

---

# Solution

**Plan.** Part (a) is a quick check that the list spans $F^2$ by exhibiting two non-collinear vectors. Part (b) applies the reduction algorithm step-by-step: $(1, 2)$ survives, $(3, 6)$ is deleted (it is $3 \cdot (1, 2)$), $(4, 7)$ survives (not a multiple of $(1, 2)$), and $(5, 9)$ is deleted (a combination of the surviving $(1, 2), (4, 7)$). The resulting basis is $(1, 2), (4, 7)$.

**Step 1: The list spans $F^2$.**

> [!note]- Derivation
> The vectors $(1, 2)$ and $(4, 7)$ are not scalar multiples of each other (their ratio is $4/1 = 4$ in the first coordinate but $7/2 = 3.5$ in the second; over any field, $4 \cdot 2 = 8 \neq 7$, so $(4, 7) \neq 4 \cdot (1, 2)$). Hence $(1, 2), (4, 7)$ is a linearly independent list of length 2 in $F^2$. By the length-of-basis shortcut ([[Ex - A list with the right length is a basis iff spanning iff independent]]) applied to $F^2$ with $\dim F^2 = 2$, this list is already a basis of $F^2$. So $\operatorname{span}((1, 2), (4, 7)) = F^2$, and a fortiori $\operatorname{span}((1, 2), (3, 6), (4, 7), (5, 9)) = F^2$.

**Step 2: Apply the reduction algorithm — step 1, examine $(1, 2)$.**

> [!note]- Derivation
> The current surviving list is empty. The span of the empty list is $\{0\}$. Is $(1, 2) \in \{0\}$? No, $(1, 2) \neq (0, 0)$. So $(1, 2)$ survives.
>
> Updated surviving list: $(1, 2)$.

**Step 3: Step 2, examine $(3, 6)$.**

> [!note]- Derivation
> Current surviving list: $(1, 2)$. Is $(3, 6) \in \operatorname{span}((1, 2))$? Yes, $(3, 6) = 3 \cdot (1, 2)$. So $(3, 6)$ is deleted.
>
> Updated surviving list: $(1, 2)$.

**Step 4: Step 3, examine $(4, 7)$.**

> [!note]- Derivation
> Current surviving list: $(1, 2)$. Is $(4, 7) \in \operatorname{span}((1, 2)) = \{(a, 2a) : a \in F\}$? The second coordinate of any multiple of $(1, 2)$ is twice the first. For $(4, 7)$, twice 4 is 8, not 7. So $(4, 7) \notin \operatorname{span}((1, 2))$. Hence $(4, 7)$ survives.
>
> Updated surviving list: $(1, 2), (4, 7)$.

**Step 5: Step 4, examine $(5, 9)$.**

> [!note]- Derivation
> Current surviving list: $(1, 2), (4, 7)$. Is $(5, 9) \in \operatorname{span}((1, 2), (4, 7))$?
>
> We check: solve $(5, 9) = a (1, 2) + b (4, 7)$. From the first coordinate, $a + 4b = 5$; from the second, $2a + 7b = 9$. Solving: from the first, $a = 5 - 4b$; substituting, $2(5 - 4b) + 7b = 9$, i.e. $10 - 8b + 7b = 9$, i.e. $-b = -1$, so $b = 1$, $a = 1$. Hence $(5, 9) = 1 \cdot (1, 2) + 1 \cdot (4, 7) = (1, 2) + (4, 7) = (5, 9)$. So $(5, 9) \in \operatorname{span}((1, 2), (4, 7))$. Hence $(5, 9)$ is deleted.
>
> Updated surviving list: $(1, 2), (4, 7)$.
>
> (Alternative observation: the surviving list $(1, 2), (4, 7)$ is already a basis of $F^2$ by Step 1, so $\operatorname{span}((1, 2), (4, 7)) = F^2$, and every vector of $F^2$ including $(5, 9)$ is in this span. So the deletion is forced.)

**Step 6: The reduction terminates with the basis $(1, 2), (4, 7)$.**

> [!note]- Derivation
> After processing all four vectors, the surviving list is $(1, 2), (4, 7)$. By [[Thm - Every Spanning List Contains a Basis|2.30]], this list is a basis of $F^2$.
>
> Verification: it has length 2 = $\dim F^2$, and we showed in Step 1 that it is linearly independent and spans. So it is indeed a basis.

> [!warning] Illegal but tempting alternative route
> A student might be tempted to *first* delete all vectors that are scalar multiples of each other, then handle the rest. This is wrong: the procedure must run left-to-right and test each vector against the *surviving* predecessors only. If we deleted $(5, 9)$ first because it equals $(1, 2) + (4, 7)$, the algorithm would not be valid — at the point we examine $(4, 7)$, we have not yet seen $(5, 9)$, so we cannot use it as a predecessor. The order matters: different orderings can produce different bases. In the original order, the basis is $(1, 2), (4, 7)$; if we reordered to $(5, 9), (4, 7), (3, 6), (1, 2)$, the basis would be $(5, 9), (4, 7)$ — both correct, both length 2, but different lists.

> [!note]- Complete formal solution
> *Part (a): the list spans $F^2$.* The sublist $(1, 2), (4, 7)$ is linearly independent in $F^2$ (the second coordinate of any scalar multiple $a \cdot (1, 2)$ is $2a$, which equals 7 only if $a = 7/2$, but $7/2 \cdot 1 = 7/2 \neq 4$, so $(4, 7) \neq a \cdot (1, 2)$ for any $a$). By [[Ex - A list with the right length is a basis iff spanning iff independent|the length-of-basis shortcut in dimension 2]], $(1, 2), (4, 7)$ is a basis of $F^2$. So $\operatorname{span}((1, 2), (4, 7)) = F^2$, hence $\operatorname{span}((1, 2), (3, 6), (4, 7), (5, 9)) \supseteq F^2$, so the span is $F^2$.
>
> *Part (b): apply [[Thm - Every Spanning List Contains a Basis|LADR 2.30]].* Initialise the surviving list $B = ()$. Process vectors left-to-right:
>
> - Step 1: $(1, 2) \notin \operatorname{span}(B) = \{0\}$ since $(1, 2) \neq 0$. Keep. $B = ((1, 2))$.
> - Step 2: $(3, 6) = 3 \cdot (1, 2) \in \operatorname{span}(B)$. Delete. $B = ((1, 2))$.
> - Step 3: $(4, 7) \notin \operatorname{span}(B) = \{(a, 2a) : a \in F\}$ since the second coordinate of $(4, 7)$ is $7$, not $2 \cdot 4 = 8$. Keep. $B = ((1, 2), (4, 7))$.
> - Step 4: $(5, 9) = (1, 2) + (4, 7) \in \operatorname{span}(B)$. Delete. $B = ((1, 2), (4, 7))$.
>
> At termination, $B = (1, 2), (4, 7)$ is the basis of $F^2$ produced by the reduction.
> $\qquad\blacksquare$

---

# Key Takeaways

**The reduction algorithm is left-to-right and depends on the surviving predecessors.** This is the bookkeeping that students miss most often. When testing whether $v_k$ should be deleted, the criterion is "is $v_k$ in the span of the surviving predecessors *at this moment*?" — not the span of all predecessors in the original list, nor the span computed once at the start. Different orderings of the same list can produce different bases: in this exercise, $(1, 2), (4, 7)$ was the output, but reordering to $(5, 9), (4, 7), \ldots$ would have produced $(5, 9), (4, 7)$ instead. Both are bases; both have length 2; they differ as ordered lists.

**Linear dependence in $F^2$ is "scalar multiple" — for higher [[Def - Dimension|dimensions]], it is a linear system.** In two [[Def - Dimension|dimensions]], $v_2 \in \operatorname{span}(v_1)$ iff $v_2 = c v_1$ for some scalar $c$, which is easy to test by ratio of coordinates. In higher dimensions the analogous test "$v_k \in \operatorname{span}(v_1, \ldots, v_{k-1})$" is a linear system in $k - 1$ unknowns, which is the engine of Gaussian elimination. The exercise is the simplest illustration of the algorithm; the principle scales.

**Gaussian elimination is the matrix realisation of this algorithm.** Forming the matrix $M = [(1, 2)^T | (3, 6)^T | (4, 7)^T | (5, 9)^T]$ and row-reducing, the **pivot columns** correspond to the surviving basis vectors and the **non-pivot columns** correspond to the deleted ones. Pivots are determined by the same left-to-right scan: a column becomes a pivot iff its leading entry creates a new linearly independent direction. So when you do the manual reduction in this exercise, you are reproducing Gaussian elimination by hand. For computational purposes (large lists, vectors in $F^n$ for large $n$), Gaussian elimination is the standard way to extract a basis from a spanning list.

**Trigger-reaction pattern.** "Given a spanning list, asked to find a basis $\to$ left-to-right scan, delete each redundant vector, the survivors are a basis." This is the bread-and-butter computation of linear algebra. Almost every problem that asks "find a basis of $\operatorname{span}(\ldots)$" reduces to this scan. The cost is at most $O(n^2 \dim V)$ membership tests; in practice via Gaussian elimination it is $O(\dim V^2 \cdot n)$ in the matrix representation. Drill this until it is automatic.
